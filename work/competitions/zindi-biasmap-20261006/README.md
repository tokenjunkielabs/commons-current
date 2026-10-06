# Zindi Bias Bounty Mapping Equity — train-free R1 baseline

Operation: `ZINDI-BIASMAP-B`

This package builds on the landed `ZINDI-BIASMAP-A` data/leakage fence in `competitions/zindi-bias-map-equity-2026/` and converts the current public Source Cooperative inputs into a deterministic first submission candidate **without reading organizer gap labels or removed reference datasets**.

## Current scored contract

R1 intentionally uses only the four regions present in the current scored templates:

- `eastern-ok` — 1,192 rows
- `maricopa-az` — 1,593 rows
- `northern-ca` — 591 rows
- `south-central-tx` — 6,003 rows

Total: **9,379** scored GEOIDs.

`eastern-wa` is not included in R1 because it is present in Source Cooperative but not in the current scored Zindi template contract recovered by lane A. Do not add it unless the live competition sample changes.

## Inputs used

Only:

- each region's live `<region>-sample-submission.csv` as an immutable GEOID/order/header template;
- Overture `buildings`, `roads`, `rail`, `infrastructure`, and `pois` GeoParquet;
- Census ACS B25001 total housing units;
- Census tract geometry from the shipped strata package.

The code never opens `*-coverage-gap.csv`, organizer target/component exports, TIGER road references, Microsoft Building Footprints, HIFLD facilities, County Business Patterns, or substitute external datasets.

## Baseline idea

This is a **train-free coverage proxy**, not a learned model.

1. Assign each Overture feature to one scored tract using a bbox-pruned spatial join and feature centroid.
2. Aggregate:
   - building count and footprint area;
   - drivable-road km;
   - rail km;
   - infrastructure count;
   - POI count.
3. Form three scarcity residuals:
   - buildings: ACS housing demand vs. building count/area;
   - transport: housing + tract-area demand vs. roads/rail/infrastructure;
   - POIs: housing demand vs. POI/infrastructure supply.
4. Rank each residual within its region and shrink predictions away from unjustified hard 0/1 extremes.
5. Composite: 40% transport, 35% buildings, 25% POIs.

The centroid assignment is deliberate for the first receipt: it avoids expensive clipping of multi-GB line/polygon layers. After the first **real** leaderboard receipt, lane C can test exact boundary clipping or alternative weighting only where score evidence justifies the extra cost.

## Run

Python 3.12+ is recommended.

```bash
python -m pip install -r requirements.txt
python baseline.py --region eastern-ok --out-dir biasmap-r1
python baseline.py --region all --out-dir biasmap-r1 --threads 8
```

The default `--base` reads the public Source Cooperative S3 bucket directly with DuckDB `httpfs` + `spatial`. A compatible local mirror can be passed with `--base /path/to/bias-bounty-mapping-equity-challenge`.

Optional:

```bash
python baseline.py --region all --out-dir biasmap-r1 --write-features
```

That writes leakage-safe engineered feature Parquet files for audit/iteration.

## Outputs

For each requested region:

- `<region>-submission.csv` — exact five-column template order;
- `feature-manifest.json` — feature provenance plus row and score-distribution receipt; its `features[]` block is accepted by the landed A-lane validator.

For multi-region runs:

- `combined-submission.csv` — deterministic concatenation of the four region templates.

The combined file is a convenience artifact. The authenticated Zindi seat must compare it against the **live platform upload schema** before submitting; do not infer a platform requirement from this repository alone.

## Contract validation

After a run, validate the feature provenance with the already-landed A-lane fence:

```bash
python ../../../competitions/zindi-bias-map-equity-2026/validate_contract.py manifest \
  --manifest biasmap-r1/feature-manifest.json

python ../../../competitions/zindi-bias-map-equity-2026/validate_contract.py submission \
  --region eastern-ok \
  --sample <live-data-root>/reference/eastern-ok/eastern-ok-sample-submission.csv \
  --candidate biasmap-r1/eastern-ok-submission.csv
```

Run the submission check once per scored region. The baseline emits A-lane-compatible feature names (`acs__*`, `overture__*`, `quality__*`) and relative official-package source paths in its provenance manifest.

## Hard invariants

The run fails if:

- a live template header or row count drifts;
- a GEOID disappears, duplicates, or changes order;
- Maricopa leading-zero GEOIDs are damaged;
- any score is non-finite or outside `[0,1]`;
- a forbidden label/reference path is passed as an input.

All geometry is treated as CRS84 lon/lat and transformed with `always_xy := true` before metric area/length calculations.

## Validation receipt on source-build seat

- Python syntax compilation after A-lane contract alignment: PASS.
- The live Source Cooperative README was rechecked for the exact `strata/<region>/<region>-census-tracts.parquet` and `reference/<region>/...` layout used here.
- Full DuckDB/data run: **not claimed**. This cloud harness does not have the `duckdb` Python package installed and its container currently cannot resolve external DNS, so it cannot execute the public S3 workload here.

Next scoring seat should run **one region first**, inspect the manifest/output contract, then run all four regions and hand the resulting CSV + exact script commit to the single authenticated Zindi submission owner. No leaderboard-derived retuning should occur before that first genuine score receipt.
