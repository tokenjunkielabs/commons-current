#!/usr/bin/env python3
"""Deterministic train-free baseline for Zindi Bias Bounty Mapping Equity.

Reads only the current Source Cooperative challenge inputs (Overture, ACS housing,
tract geometry, and sample-submission templates). It never reads organizer gap
labels or removed reference layers.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import duckdb
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype

REGIONS = {
    "eastern-ok": 1192,
    "maricopa-az": 1593,
    "northern-ca": 591,
    "south-central-tx": 6003,
}
OUTPUT_COLUMNS = [
    "GEOID",
    "transport_gap",
    "building_gap",
    "poi_gap",
    "coverage_gap_score",
]
DEFAULT_BASE = (
    "s3://us-west-2.opendata.source.coop/humane-intelligence/"
    "bias-bounty-mapping-equity-challenge"
)
FORBIDDEN_INPUT_TOKENS = (
    "coverage-gap",
    "coverage_gap_score",
    "transport_gap",
    "building_gap",
    "poi_gap",
    "tiger/line",
    "microsoft-building",
    "hifld",
    "county-business-pattern",
)


def uri(base: str, rel: str) -> str:
    return f"{base.rstrip('/')}/{rel.lstrip('/')}"


def assert_allowed_input(path: str) -> None:
    low = path.lower()
    hits = [token for token in FORBIDDEN_INPUT_TOKENS if token in low]
    if hits:
        raise ValueError(f"Leakage guard rejected input path {path!r}: {hits}")


def load_extension(con: duckdb.DuckDBPyConnection, name: str) -> None:
    try:
        con.execute(f"LOAD {name}")
    except duckdb.Error:
        con.execute(f"INSTALL {name}")
        con.execute(f"LOAD {name}")


def connect(threads: int) -> duckdb.DuckDBPyConnection:
    con = duckdb.connect()
    load_extension(con, "httpfs")
    load_extension(con, "spatial")
    con.execute("SET s3_region='us-west-2'")
    con.execute("SET s3_url_style='path'")
    con.execute(f"SET threads={max(1, int(threads))}")
    con.execute("SET preserve_insertion_order=false")
    return con


def read_template(con: duckdb.DuckDBPyConnection, base: str, region: str) -> pd.DataFrame:
    path = uri(base, f"reference/{region}/{region}-sample-submission.csv")
    # Template output columns are allowed; the template is never used as a feature source.
    df = con.sql(
        f"SELECT * FROM read_csv('{path}', types={{'GEOID': 'VARCHAR'}}, header=true)"
    ).df()
    if list(df.columns) != OUTPUT_COLUMNS:
        raise ValueError(f"{region}: unexpected sample header {list(df.columns)}")
    df["GEOID"] = df["GEOID"].astype(str)
    expected = REGIONS[region]
    if len(df) != expected:
        raise ValueError(f"{region}: expected {expected} template rows, got {len(df)}")
    if df["GEOID"].duplicated().any():
        raise ValueError(f"{region}: duplicate GEOIDs in sample template")
    return df


def read_housing(con: duckdb.DuckDBPyConnection, base: str, region: str) -> pd.DataFrame:
    path = uri(base, f"reference/{region}/{region}-census-acs-housing.parquet")
    assert_allowed_input(path)
    df = con.sql(f"SELECT * FROM '{path}'").df()
    if "GEOID" not in df.columns:
        raise ValueError(f"{region}: ACS housing file has no GEOID column")
    df["GEOID"] = df["GEOID"].astype(str)

    numeric = [c for c in df.columns if c != "GEOID" and is_numeric_dtype(df[c])]
    preferred_exact = [
        "B25001_001E",
        "B25001_001",
        "housing_units",
        "total_housing_units",
    ]
    housing_col = next((c for c in preferred_exact if c in df.columns), None)
    if housing_col is None:
        likely = [
            c
            for c in numeric
            if ("25001" in c.lower() or "housing" in c.lower())
            and "moe" not in c.lower()
            and not c.lower().endswith("m")
        ]
        if len(likely) == 1:
            housing_col = likely[0]
        elif len(numeric) == 1:
            housing_col = numeric[0]
        else:
            raise ValueError(
                f"{region}: cannot identify ACS B25001 total housing column; "
                f"numeric columns={numeric}"
            )
    out = df[["GEOID", housing_col]].rename(columns={housing_col: "acs__housing_units"})
    out["acs__housing_units"] = pd.to_numeric(out["acs__housing_units"], errors="coerce")
    return out


def tract_frame(
    con: duckdb.DuckDBPyConnection,
    base: str,
    region: str,
    template: pd.DataFrame,
) -> pd.DataFrame:
    tract_path = uri(base, f"strata/{region}/{region}-census-tracts.parquet")
    assert_allowed_input(tract_path)
    view = f"template_{region.replace('-', '_')}"
    con.register(view, template[["GEOID"]])
    # EPSG:5070 is a US equal-area CRS. always_xy is mandatory for CRS84 lon/lat.
    q = f"""
        SELECT t.GEOID::VARCHAR AS GEOID,
               ST_Area(ST_Transform(t.geometry, 'EPSG:4326', 'EPSG:5070', always_xy := true))
                 / 1000000.0 AS quality__tract_area_km2
        FROM '{tract_path}' t
        INNER JOIN {view} s ON t.GEOID::VARCHAR = s.GEOID
    """
    df = con.sql(q).df()
    if len(df) != len(template):
        raise ValueError(f"{region}: tract/template row mismatch {len(df)} != {len(template)}")
    return df


def aggregate_layer(
    con: duckdb.DuckDBPyConnection,
    base: str,
    region: str,
    template: pd.DataFrame,
    layer: str,
    metric: str,
) -> pd.DataFrame:
    """Aggregate Overture features to scored tracts using bbox prune + centroid assignment.

    Centroid assignment intentionally gives every source feature one tract owner, which is
    much faster than polygon/line clipping for this first train-free receipt. Length/area
    metrics use full source features after that assignment. A later scored iteration can
    replace this with exact boundary clipping if leaderboard evidence warrants the cost.
    """
    source_path = uri(base, f"reference/{region}/{region}-overture-{layer}.parquet")
    tract_path = uri(base, f"strata/{region}/{region}-census-tracts.parquet")
    assert_allowed_input(source_path)
    assert_allowed_input(tract_path)
    view = f"template_{region.replace('-', '_')}"
    con.register(view, template[["GEOID"]])

    if metric == "count":
        expr = "COUNT(o.geometry)::DOUBLE"
        col = f"overture__{layer.replace('-', '_')}_count"
    elif metric == "length_km":
        expr = (
            "COALESCE(SUM(ST_Length(ST_Transform(o.geometry, 'EPSG:4326', "
            "'EPSG:5070', always_xy := true))) / 1000.0, 0.0)"
        )
        col = f"overture__{layer.replace('-', '_')}_km"
    elif metric == "area_m2":
        expr = (
            "COALESCE(SUM(ST_Area(ST_Transform(o.geometry, 'EPSG:4326', "
            "'EPSG:5070', always_xy := true))), 0.0)"
        )
        col = f"overture__{layer.replace('-', '_')}_area_m2"
    else:
        raise ValueError(metric)

    q = f"""
        WITH tracts AS (
            SELECT t.GEOID::VARCHAR AS GEOID, t.geometry, t.bbox
            FROM '{tract_path}' t
            INNER JOIN {view} s ON t.GEOID::VARCHAR = s.GEOID
        )
        SELECT t.GEOID, {expr} AS {col}
        FROM tracts t
        LEFT JOIN '{source_path}' o
          ON o.bbox.xmin <= t.bbox.xmax
         AND o.bbox.xmax >= t.bbox.xmin
         AND o.bbox.ymin <= t.bbox.ymax
         AND o.bbox.ymax >= t.bbox.ymin
         AND ST_Intersects(t.geometry, ST_Centroid(o.geometry))
        GROUP BY t.GEOID
    """
    return con.sql(q).df()


def pct_gap(raw: pd.Series) -> pd.Series:
    x = pd.to_numeric(raw, errors="coerce")
    if x.notna().sum() == 0:
        return pd.Series(np.full(len(x), 0.5), index=x.index)
    x = x.fillna(x.median())
    # Shrink ranks away from hard 0/1 because the first receipt has no labels to justify extremes.
    return 0.05 + 0.90 * x.rank(method="average", pct=True)


def score_region(features: pd.DataFrame) -> pd.DataFrame:
    f = features.copy()
    for c in [
        "acs__housing_units",
        "quality__tract_area_km2",
        "overture__buildings_count",
        "overture__buildings_area_m2",
        "overture__roads_km",
        "overture__rail_km",
        "overture__infrastructure_count",
        "overture__pois_count",
    ]:
        f[c] = pd.to_numeric(f[c], errors="coerce").fillna(0.0).clip(lower=0.0)

    housing_demand = np.log1p(f["acs__housing_units"])
    land_demand = np.log1p(f["quality__tract_area_km2"])

    building_equiv = f["overture__buildings_count"] + f["overture__buildings_area_m2"] / 150.0
    building_raw = housing_demand - np.log1p(building_equiv)

    transport_supply = (
        f["overture__roads_km"]
        + 1.75 * f["overture__rail_km"]
        + 0.35 * f["overture__infrastructure_count"]
    )
    transport_raw = 0.65 * housing_demand + 0.35 * land_demand - np.log1p(transport_supply)

    poi_supply = f["overture__pois_count"] + 0.50 * f["infrastructure_count"]
    poi_raw = housing_demand - np.log1p(poi_supply)

    out = pd.DataFrame({"GEOID": f["GEOID"].astype(str)})
    out["transport_gap"] = pct_gap(transport_raw)
    out["building_gap"] = pct_gap(building_raw)
    out["poi_gap"] = pct_gap(poi_raw)
    out["coverage_gap_score"] = (
        0.40 * out["transport_gap"]
        + 0.35 * out["building_gap"]
        + 0.25 * out["poi_gap"]
    )
    return out[OUTPUT_COLUMNS]


def validate_output(template: pd.DataFrame, scored: pd.DataFrame, region: str) -> None:
    if list(scored.columns) != OUTPUT_COLUMNS:
        raise ValueError(f"{region}: output header mismatch")
    if len(scored) != REGIONS[region]:
        raise ValueError(f"{region}: output row count mismatch")
    if scored["GEOID"].astype(str).tolist() != template["GEOID"].astype(str).tolist():
        raise ValueError(f"{region}: GEOID membership/order differs from live template")
    vals = scored[OUTPUT_COLUMNS[1:]].to_numpy(dtype=float)
    if not np.isfinite(vals).all():
        raise ValueError(f"{region}: non-finite prediction")
    if ((vals < 0.0) | (vals > 1.0)).any():
        raise ValueError(f"{region}: prediction outside [0,1]")


def build_region(
    con: duckdb.DuckDBPyConnection,
    base: str,
    region: str,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    template = read_template(con, base, region)
    housing = read_housing(con, base, region)
    tracts = tract_frame(con, base, region, template)

    features = template[["GEOID"]].copy()
    features = features.merge(housing, on="GEOID", how="left", validate="one_to_one")
    features = features.merge(tracts, on="GEOID", how="left", validate="one_to_one")
    for layer, metric in [
        ("buildings", "count"),
        ("buildings", "area_m2"),
        ("roads", "length_km"),
        ("rail", "length_km"),
        ("infrastructure", "count"),
        ("pois", "count"),
    ]:
        agg = aggregate_layer(con, base, region, template, layer, metric)
        features = features.merge(agg, on="GEOID", how="left", validate="one_to_one")

    scored = score_region(features)
    # Restore exact template order after all joins.
    scored = template[["GEOID"]].merge(scored, on="GEOID", how="left", validate="one_to_one")
    validate_output(template, scored, region)
    return scored, features


def write_outputs(out_dir: Path, region_outputs: Iterable[tuple[str, pd.DataFrame]]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    region_outputs = list(region_outputs)
    combined = []
    for region, df in region_outputs:
        path = out_dir / f"{region}-submission.csv"
        df.to_csv(path, index=False, float_format="%.10f")
        reread = pd.read_csv(path, dtype={"GEOID": str})
        if reread["GEOID"].tolist() != df["GEOID"].astype(str).tolist():
            raise ValueError(f"{region}: written GEOID round-trip changed")
        combined.append(df)
    all_df = pd.concat(combined, ignore_index=True)
    expected_total = sum(len(df) for _, df in region_outputs)
    if len(all_df) != expected_total:
        raise ValueError("combined row-count invariant failed")
    all_df.to_csv(out_dir / "combined-submission.csv", index=False, float_format="%.10f")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--base", default=DEFAULT_BASE, help="Source Coop root or compatible local mirror")
    p.add_argument("--out-dir", default="biasmap-r1", help="Directory for submission CSVs and diagnostics")
    p.add_argument("--threads", type=int, default=8)
    p.add_argument("--region", choices=["all", *REGIONS], default="all")
    p.add_argument("--write-features", action="store_true", help="Also write leakage-safe engineered features")
    return p.parse_args()



def feature_manifest(regions: list[str]) -> list[dict[str, object]]:
    """Return a provenance manifest accepted by the landed ZINDI-BIASMAP-A validator."""
    def sources(suffix: str) -> list[str]:
        return [f"reference/{r}/{r}-{suffix}" for r in regions]

    return [
        {"name": "acs__housing_units", "sources": sources("census-acs-housing.parquet")},
        {
            "name": "quality__tract_area_km2",
            "sources": [f"strata/{r}/{r}-census-tracts.parquet" for r in regions],
        },
        {"name": "overture__buildings_count", "sources": sources("overture-buildings.parquet")},
        {"name": "overture__buildings_area_m2", "sources": sources("overture-buildings.parquet")},
        {"name": "overture__roads_km", "sources": sources("overture-roads.parquet")},
        {"name": "overture__rail_km", "sources": sources("overture-rail.parquet")},
        {
            "name": "overture__infrastructure_count",
            "sources": sources("overture-infrastructure.parquet"),
        },
        {"name": "overture__pois_count", "sources": sources("overture-pois.parquet")},
    ]


def main() -> int:
    args = parse_args()
    con = connect(args.threads)
    out_dir = Path(args.out_dir)
    regions = list(REGIONS) if args.region == "all" else [args.region]
    results: list[tuple[str, pd.DataFrame]] = []
    manifest: dict[str, object] = {
        "method": "train-free-rank-proxy-r1",
        "base": args.base,
        "features": feature_manifest(regions),
        "regions": {},
        "forbidden_label_inputs": list(FORBIDDEN_INPUT_TOKENS),
    }

    for region in regions:
        scored, features = build_region(con, args.base, region)
        results.append((region, scored))
        manifest["regions"][region] = {
            "rows": len(scored),
            "geoid_first": scored.iloc[0]["GEOID"],
            "geoid_last": scored.iloc[-1]["GEOID"],
            "coverage_mean": float(scored["coverage_gap_score"].mean()),
            "coverage_std": float(scored["coverage_gap_score"].std(ddof=0)),
        }
        if args.write_features:
            out_dir.mkdir(parents=True, exist_ok=True)
            features.to_parquet(out_dir / f"{region}-features.parquet", index=False)

    write_outputs(out_dir, results)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "feature-manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
