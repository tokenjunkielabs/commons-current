#!/usr/bin/env python3
"""Train-only A/B receipt gate for TrafficFlowBench Task 1 experiments."""
from __future__ import annotations
import argparse, hashlib, json, math, statistics, sys
from pathlib import Path

REQUIRED = {
    "experiment_id", "variant", "panel", "holdout", "split",
    "scorer", "data_fingerprint", "code_revision", "seed",
    "s_state", "runtime_s", "peak_rss_mb",
}

def fail(msg):
    raise ValueError(msg)

def load_rows(path: Path):
    rows = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as e:
            fail(f"line {n}: invalid JSON: {e.msg}")
        missing = REQUIRED - row.keys()
        if missing:
            fail(f"line {n}: missing fields: {', '.join(sorted(missing))}")
        if row["split"] != "train":
            fail(f"line {n}: only train receipts are allowed; got {row['split']!r}")
        if row["scorer"] != "official_task1_scorer":
            fail(f"line {n}: scorer must be 'official_task1_scorer'")
        if row["variant"] not in {"baseline", "candidate"}:
            fail(f"line {n}: variant must be baseline or candidate")
        for key in ("s_state", "runtime_s", "peak_rss_mb"):
            value = row[key]
            if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value):
                fail(f"line {n}: {key} must be finite numeric")
        if not 0 <= row["s_state"] <= 1:
            fail(f"line {n}: s_state out of [0,1]")
        if row["runtime_s"] < 0 or row["peak_rss_mb"] < 0:
            fail(f"line {n}: runtime_s/peak_rss_mb must be non-negative")
        rows.append(row)
    if not rows:
        fail("no receipts")
    return rows

def receipt_key(row):
    return (str(row["panel"]), str(row["holdout"]), int(row["seed"]))

def summarize(rows, min_mean_delta=0.0, max_panel_regression=0.0, max_runtime_ratio=None):
    by_variant = {"baseline": {}, "candidate": {}}
    identities, exp_ids = {}, set()
    revisions = {"baseline": set(), "candidate": set()}
    for row in rows:
        key = receipt_key(row)
        if key in by_variant[row["variant"]]:
            fail(f"duplicate {row['variant']} receipt for {key}")
        by_variant[row["variant"]][key] = row
        exp_ids.add(str(row["experiment_id"]))
        revisions[row["variant"]].add(str(row["code_revision"]))
        identities.setdefault(key, set()).add(str(row["data_fingerprint"]))
    if len(exp_ids) != 1:
        fail(f"expected one experiment_id, got {sorted(exp_ids)}")
    if len(revisions["baseline"]) != 1 or len(revisions["candidate"]) != 1:
        fail("each variant must use exactly one code_revision")
    bkeys, ckeys = set(by_variant["baseline"]), set(by_variant["candidate"])
    if bkeys != ckeys:
        fail(f"unpaired receipts; missing_candidate={sorted(bkeys-ckeys)} missing_baseline={sorted(ckeys-bkeys)}")
    for key, fps in identities.items():
        if len(fps) != 1:
            fail(f"data_fingerprint mismatch for {key}: {sorted(fps)}")

    pairs = []
    for key in sorted(bkeys):
        b, c = by_variant["baseline"][key], by_variant["candidate"][key]
        pairs.append({
            "panel": key[0], "holdout": key[1], "seed": key[2],
            "baseline_s_state": b["s_state"], "candidate_s_state": c["s_state"],
            "delta_s_state": c["s_state"] - b["s_state"],
            "baseline_runtime_s": b["runtime_s"], "candidate_runtime_s": c["runtime_s"],
        })
    deltas = [p["delta_s_state"] for p in pairs]
    baseline_scores = [p["baseline_s_state"] for p in pairs]
    candidate_scores = [p["candidate_s_state"] for p in pairs]
    baseline_rt = statistics.fmean(p["baseline_runtime_s"] for p in pairs)
    candidate_rt = statistics.fmean(p["candidate_runtime_s"] for p in pairs)
    runtime_ratio = candidate_rt / baseline_rt if baseline_rt > 0 else (1.0 if candidate_rt == 0 else math.inf)
    mean_delta, worst_delta = statistics.fmean(deltas), min(deltas)

    reasons = []
    if mean_delta < min_mean_delta:
        reasons.append(f"mean_delta {mean_delta:.9f} < {min_mean_delta:.9f}")
    if worst_delta < -max_panel_regression:
        reasons.append(f"worst_pair_delta {worst_delta:.9f} < {-max_panel_regression:.9f}")
    if max_runtime_ratio is not None and runtime_ratio > max_runtime_ratio:
        reasons.append(f"runtime_ratio {runtime_ratio:.6f} > {max_runtime_ratio:.6f}")

    report = {
        "schema": "trafficflowbench.task1_ab_receipt.v1",
        "experiment_id": next(iter(exp_ids)),
        "pair_count": len(pairs),
        "panels": sorted({p["panel"] for p in pairs}),
        "baseline_revision": next(iter(revisions["baseline"])),
        "candidate_revision": next(iter(revisions["candidate"])),
        "mean_baseline_s_state": statistics.fmean(baseline_scores),
        "mean_candidate_s_state": statistics.fmean(candidate_scores),
        "mean_delta_s_state": mean_delta,
        "worst_pair_delta_s_state": worst_delta,
        "mean_baseline_runtime_s": baseline_rt,
        "mean_candidate_runtime_s": candidate_rt,
        "runtime_ratio": runtime_ratio,
        "promotion_ready": not reasons,
        "promotion_reasons": reasons,
        "policy": {
            "min_mean_delta": min_mean_delta,
            "max_panel_regression": max_panel_regression,
            "max_runtime_ratio": max_runtime_ratio,
        },
        "pairs": pairs,
        "evidence_boundary": [
            "train split only",
            "s_state must come from the official Task 1 scorer",
            "no validation/private score is accepted by this tool",
            "Task 3 local proxy is intentionally excluded from promotion",
        ],
    }
    canonical = json.dumps(report, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    report["receipt_sha256"] = hashlib.sha256(canonical).hexdigest()
    return report

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("receipts", type=Path)
    ap.add_argument("--min-mean-delta", type=float, default=0.0)
    ap.add_argument("--max-panel-regression", type=float, default=0.0)
    ap.add_argument("--max-runtime-ratio", type=float)
    args = ap.parse_args(argv)
    try:
        report = summarize(load_rows(args.receipts), args.min_mean_delta, args.max_panel_regression, args.max_runtime_ratio)
    except ValueError as e:
        print(json.dumps({"error": str(e)}, sort_keys=True), file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))
    return 0 if report["promotion_ready"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
