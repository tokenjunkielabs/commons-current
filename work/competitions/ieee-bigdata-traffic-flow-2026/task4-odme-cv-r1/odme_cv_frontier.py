#!/usr/bin/env python3
"""Task 4 ODME regularization frontier for TrafficFlowBench 2026.

This utility deliberately optimizes only evidence available in the public
release. It never claims S_ODME, S_od, S_dev, or S_attr, whose path-flow truth
is withheld. Instead it screens non-negative ODME candidates by deterministic
held-out detector-count fit while reporting two guardrail proxies:
path-flow deviation from the released weak prior and destination-attraction
distribution drift.

The official baseline is exactly recovered by lambda=0.05, support_gamma=0.
Positive support_gamma gives paths with fewer training detector constraints a
stronger pull to the weak prior, while allowing better-observed paths to move
more freely.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import nnls


OFFICIAL_COMMIT = "c88cddf533bbf0afa4ff1fc6c031d760a08e7a31"
BASELINE_LAMBDA = 0.05
BASELINE_GAMMA = 0.0
EPS = 1e-12


@dataclass(frozen=True)
class OfficialAPI:
    load_operator: object
    released_counts: object
    released_prior: object


def load_official_api(official_repo: Path) -> OfficialAPI:
    src = (official_repo / "src").resolve()
    if not src.is_dir():
        raise FileNotFoundError(f"official repo missing src/: {official_repo}")
    sys.path.insert(0, str(src))
    try:
        from task4.build_task4_odme_artifacts import (  # type: ignore
            load_operator,
            released_counts,
            released_prior,
        )
    except Exception as exc:
        raise RuntimeError(
            "could not import official Task 4 helpers; use the pinned public repo "
            f"at {OFFICIAL_COMMIT}"
        ) from exc
    return OfficialAPI(load_operator, released_counts, released_prior)


def parse_grid(raw: str, *, name: str, minimum: float = 0.0) -> list[float]:
    out: list[float] = []
    for part in raw.split(","):
        value = float(part.strip())
        if not math.isfinite(value) or value < minimum:
            raise ValueError(f"{name} values must be finite and >= {minimum}: {raw}")
        out.append(value)
    if not out:
        raise ValueError(f"{name} cannot be empty")
    return sorted(set(out))


def stable_folds(panel: str, link_ids: list[str], folds: int) -> np.ndarray:
    """Balanced deterministic detector folds, independent of source row order."""
    if folds < 2:
        raise ValueError("--folds must be >= 2")
    if len(link_ids) < folds:
        raise ValueError(f"{panel}: {len(link_ids)} scored links cannot support {folds} folds")
    order = sorted(
        range(len(link_ids)),
        key=lambda i: hashlib.sha256(f"{panel}:{link_ids[i]}".encode()).digest(),
    )
    assignment = np.empty(len(link_ids), dtype=np.int64)
    for rank, idx in enumerate(order):
        assignment[idx] = rank % folds
    return assignment


def support_penalty_weights(A_train: np.ndarray, gamma: float) -> np.ndarray:
    """Regularization row multipliers for a support-weighted Tikhonov penalty.

    The objective contribution is:
        lambda * sum_j ((median_support+1)/(support_j+1))**gamma * (f_j-b_j)^2

    gamma=0 therefore reproduces uniform official-baseline regularization.
    """
    n_paths = A_train.shape[1]
    if gamma == 0:
        return np.ones(n_paths, dtype=np.float64)
    support = np.count_nonzero(A_train, axis=0).astype(np.float64)
    positive = support[support > 0]
    median = float(np.median(positive)) if len(positive) else 0.0
    factor = (median + 1.0) / (support + 1.0)
    return np.power(factor, gamma / 2.0)


def solve_weighted(
    A: np.ndarray,
    counts: np.ndarray,
    prior: np.ndarray,
    reg_lambda: float,
    support_gamma: float,
) -> np.ndarray:
    if reg_lambda <= 0:
        raise ValueError("lambda must be > 0; Task 4 is underdetermined and the prior is part of the contract")
    weights = support_penalty_weights(A, support_gamma)
    reg = np.sqrt(reg_lambda) * np.diag(weights)
    aa = np.vstack([A, reg])
    bb = np.concatenate([counts, np.sqrt(reg_lambda) * weights * prior])
    flow, _ = nnls(aa, bb)
    return flow


def s_link(A: np.ndarray, flow: np.ndarray, counts: np.ndarray) -> float:
    denom = max(float(np.sum(counts)), EPS)
    err = float(np.sum(np.abs(A @ flow - counts)))
    return max(0.0, 1.0 - err / denom)


def prior_relative_l1(flow: np.ndarray, prior: np.ndarray) -> float:
    return float(np.sum(np.abs(flow - prior))) / max(float(np.sum(np.abs(prior))), EPS)


def destination_tv(flow: np.ndarray, prior: np.ndarray, destinations: np.ndarray) -> float:
    """Total-variation distance between destination-attraction shares."""
    frame = pd.DataFrame({"destination": destinations, "flow": flow, "prior": prior})
    grouped = frame.groupby("destination", sort=False)[["flow", "prior"]].sum()
    f_total = float(grouped.flow.sum())
    p_total = float(grouped.prior.sum())
    if f_total <= EPS and p_total <= EPS:
        return 0.0
    f_share = grouped.flow.to_numpy(dtype=float) / max(f_total, EPS)
    p_share = grouped.prior.to_numpy(dtype=float) / max(p_total, EPS)
    return 0.5 * float(np.sum(np.abs(f_share - p_share)))


def pareto_flags(frame: pd.DataFrame) -> np.ndarray:
    """Non-dominated on CV link fit (max), prior drift (min), destination drift (min)."""
    vals = frame[["cv_s_link_mean", "prior_relative_l1", "destination_tv"]].to_numpy(float)
    keep = np.ones(len(frame), dtype=bool)
    for i, (score_i, prior_i, dest_i) in enumerate(vals):
        for j, (score_j, prior_j, dest_j) in enumerate(vals):
            if i == j:
                continue
            no_worse = score_j >= score_i and prior_j <= prior_i and dest_j <= dest_i
            strictly = score_j > score_i or prior_j < prior_i or dest_j < dest_i
            if no_worse and strictly:
                keep[i] = False
                break
    return keep


def prior_vector(prior_frame: pd.DataFrame | None, path_ids: list[str]) -> np.ndarray:
    if prior_frame is None:
        return np.zeros(len(path_ids), dtype=np.float64)
    frame = prior_frame.copy()
    frame["path_id"] = frame.path_id.astype(str)
    return (
        pd.to_numeric(frame.set_index("path_id").reindex(path_ids).path_flow, errors="coerce")
        .fillna(0.0)
        .to_numpy(dtype=np.float64)
    )


def panel_frontier(
    *,
    panel: str,
    family_id: str,
    release_root: Path,
    split: str,
    api: OfficialAPI,
    lambdas: list[float],
    gammas: list[float],
    folds: int,
) -> pd.DataFrame:
    network = release_root / "corridors" / panel / "network"
    path_ids, operator_link_ids, A_all, paths = api.load_operator(network)
    path_ids = [str(x) for x in path_ids]
    operator_link_ids = [str(x) for x in operator_link_ids]
    paths = paths.copy()
    paths["path_id"] = paths.path_id.astype(str)
    path_meta = paths.set_index("path_id").reindex(path_ids)
    destinations = path_meta.destination_zone.astype(str).to_numpy()

    counts_frame = api.released_counts(release_root, panel, split)
    if counts_frame is None:
        raise FileNotFoundError(
            f"{panel}: official release has no Task 4 link counts for split={split}"
        )
    counts_frame = counts_frame.copy()
    counts_frame["link_id"] = counts_frame.link_id.astype(str)
    index = {link: i for i, link in enumerate(operator_link_ids)}
    scored_links = [link for link in counts_frame.link_id if link in index]
    if len(scored_links) < folds:
        raise ValueError(f"{panel}: only {len(scored_links)} scored links for {folds} folds")
    rows = np.array([index[x] for x in scored_links], dtype=np.int64)
    A = A_all[rows, :]
    counts = (
        counts_frame.set_index("link_id")
        .reindex(scored_links)["count"]
        .fillna(0.0)
        .to_numpy(dtype=np.float64)
    )
    prior = prior_vector(api.released_prior(release_root, panel, split), path_ids)
    fold_id = stable_folds(panel, scored_links, folds)

    result: list[dict] = []
    for reg_lambda in lambdas:
        for gamma in gammas:
            start = time.perf_counter()
            fold_scores: list[float] = []
            for fold in range(folds):
                train = fold_id != fold
                holdout = ~train
                flow = solve_weighted(A[train], counts[train], prior, reg_lambda, gamma)
                fold_scores.append(s_link(A[holdout], flow, counts[holdout]))
            full_flow = solve_weighted(A, counts, prior, reg_lambda, gamma)
            result.append(
                {
                    "panel": panel,
                    "family_id": family_id,
                    "split": split,
                    "lambda": reg_lambda,
                    "support_gamma": gamma,
                    "is_official_baseline": bool(
                        abs(reg_lambda - BASELINE_LAMBDA) < 1e-15
                        and abs(gamma - BASELINE_GAMMA) < 1e-15
                    ),
                    "n_paths": len(path_ids),
                    "n_scored_links": len(scored_links),
                    "folds": folds,
                    "cv_s_link_mean": float(np.mean(fold_scores)),
                    "cv_s_link_min": float(np.min(fold_scores)),
                    "fit_s_link": s_link(A, full_flow, counts),
                    "prior_relative_l1": prior_relative_l1(full_flow, prior),
                    "destination_tv": destination_tv(full_flow, prior, destinations),
                    "runtime_seconds": time.perf_counter() - start,
                }
            )
    frame = pd.DataFrame(result)
    frame["is_pareto"] = pareto_flags(frame)
    return frame


def aggregate_frontier(frame: pd.DataFrame) -> pd.DataFrame:
    """Equal-family aggregate, mirroring the official family-equal philosophy."""
    family = (
        frame.groupby(["lambda", "support_gamma", "is_official_baseline", "family_id"], as_index=False)
        .agg(
            cv_s_link_mean=("cv_s_link_mean", "mean"),
            cv_s_link_min=("cv_s_link_min", "min"),
            fit_s_link=("fit_s_link", "mean"),
            prior_relative_l1=("prior_relative_l1", "mean"),
            destination_tv=("destination_tv", "mean"),
            runtime_seconds=("runtime_seconds", "sum"),
        )
    )
    out = (
        family.groupby(["lambda", "support_gamma", "is_official_baseline"], as_index=False)
        .agg(
            cv_s_link_mean=("cv_s_link_mean", "mean"),
            cv_s_link_min=("cv_s_link_min", "min"),
            fit_s_link=("fit_s_link", "mean"),
            prior_relative_l1=("prior_relative_l1", "mean"),
            destination_tv=("destination_tv", "mean"),
            runtime_seconds=("runtime_seconds", "sum"),
        )
    )
    out["is_pareto"] = pareto_flags(out)
    return out.sort_values(
        ["is_pareto", "cv_s_link_mean", "prior_relative_l1"],
        ascending=[False, False, True],
    )


def self_check() -> None:
    """One focused numerical invariant check; not a competition-performance claim."""
    A = np.array([[1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])
    counts = np.array([10.0, 30.0, 20.0])
    prior = np.array([12.0, 18.0])

    ours = solve_weighted(A, counts, prior, BASELINE_LAMBDA, 0.0)
    aa = np.vstack([A, np.sqrt(BASELINE_LAMBDA) * np.eye(A.shape[1])])
    bb = np.concatenate([counts, np.sqrt(BASELINE_LAMBDA) * prior])
    official_shape, _ = nnls(aa, bb)
    if not np.allclose(ours, official_shape, rtol=1e-12, atol=1e-12):
        raise AssertionError("gamma=0 does not reproduce the official uniform-regularization solve")
    if np.any(ours < 0) or s_link(A, ours, counts) < 0.95:
        raise AssertionError("non-negativity/link-fit invariant failed")
    folds = stable_folds("PANEL", ["L1", "L2", "L3", "L4"], 2)
    if sorted(np.bincount(folds).tolist()) != [2, 2]:
        raise AssertionError("deterministic fold balancing failed")
    print("self-check PASS: baseline equivalence, non-negativity, link fit, balanced folds")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--official-repo", type=Path)
    parser.add_argument("--release-root", type=Path)
    parser.add_argument("--split", default="train", choices=["train", "validation", "private"])
    parser.add_argument("--panel", action="append", help="corridor panel; repeatable")
    parser.add_argument("--lambda-grid", default="0.01,0.03,0.05,0.1,0.3")
    parser.add_argument("--support-gamma-grid", default="0,0.5,1")
    parser.add_argument("--folds", type=int, default=4)
    parser.add_argument("--output-dir", type=Path, default=Path("task4_odme_frontier"))
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()

    if args.self_check:
        self_check()
        return
    if args.official_repo is None or args.release_root is None:
        parser.error("--official-repo and --release-root are required unless --self-check is used")

    api = load_official_api(args.official_repo.resolve())
    manifest = json.loads((args.official_repo / "config" / "corridors.json").read_text(encoding="utf-8"))
    family = {str(p["corridor_id"]): str(p["family_id"]) for p in manifest["panels"]}
    panels = list(family)
    if args.panel:
        requested = set(args.panel)
        unknown = sorted(requested - set(panels))
        if unknown:
            raise ValueError(f"unknown panels: {unknown}")
        panels = [p for p in panels if p in requested]

    lambdas = parse_grid(args.lambda_grid, name="lambda", minimum=EPS)
    gammas = parse_grid(args.support_gamma_grid, name="support gamma", minimum=0.0)
    if BASELINE_LAMBDA not in lambdas or BASELINE_GAMMA not in gammas:
        print("warning: grid omits the official lambda=0.05/gamma=0 comparator", file=sys.stderr)

    frames = []
    for panel in panels:
        print(f"[Task4 ODME CV] {panel}", flush=True)
        frames.append(
            panel_frontier(
                panel=panel,
                family_id=family[panel],
                release_root=args.release_root.resolve(),
                split=args.split,
                api=api,
                lambdas=lambdas,
                gammas=gammas,
                folds=args.folds,
            )
        )

    frontier = pd.concat(frames, ignore_index=True)
    aggregate = aggregate_frontier(frontier)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    frontier.to_csv(args.output_dir / "panel_frontier.csv", index=False)
    aggregate.to_csv(args.output_dir / "aggregate_frontier.csv", index=False)

    print(f"Wrote {args.output_dir / 'panel_frontier.csv'}")
    print(f"Wrote {args.output_dir / 'aggregate_frontier.csv'}")
    print("These are public-count screening diagnostics only. Do not describe them as S_ODME or leaderboard performance.")
    print(aggregate.head(12).to_string(index=False))


if __name__ == "__main__":
    main()
