#!/usr/bin/env python3
"""Offline budget-policy scorer for Gemma 4 Developer Agent dev-run receipts.

Input JSONL rows represent already-executed task attempts. The tool never estimates a
leaderboard score. It compares the fixed 5m/80-call and 7m/100-call policies on the
same observed task slice, rejects malformed or over-budget receipts, and can show how
an observed schedule fits inside a global wall-clock cap without fabricating outcomes.
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

POLICY_LIMITS: dict[str, tuple[float, int]] = {
    "5m80": (300.0, 80),
    "7m100": (420.0, 100),
}

@dataclass(frozen=True)
class Attempt:
    task_id: str
    repo: str
    policy: str
    passed: bool
    patch_produced: bool
    wall_seconds: float
    tool_calls: int
    first_edit_seconds: float | None
    test_seconds: float | None
    diff_lines: int

def _string(x: dict[str, Any], field: str, lineno: int) -> str:
    value = x.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"line {lineno}: {field} must be a non-empty string")
    return value.strip()

def _boolean(x: dict[str, Any], field: str, lineno: int) -> bool:
    value = x.get(field)
    if not isinstance(value, bool):
        raise ValueError(f"line {lineno}: {field} must be a JSON boolean")
    return value

def _integer(x: dict[str, Any], field: str, lineno: int) -> int:
    value = x.get(field)
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"line {lineno}: {field} must be a JSON integer")
    return value

def _finite_number(x: dict[str, Any], field: str, lineno: int) -> float:
    value = x.get(field)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"line {lineno}: {field} must be a finite JSON number")
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"line {lineno}: {field} must be finite")
    return number

def _optional_finite_number(x: dict[str, Any], field: str, lineno: int) -> float | None:
    if x.get(field) is None:
        return None
    return _finite_number(x, field, lineno)

def load(path: Path) -> list[Attempt]:
    rows: list[Attempt] = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            x = json.loads(raw)
        except json.JSONDecodeError as e:
            raise ValueError(f"line {lineno}: invalid JSON: {e}") from e
        if not isinstance(x, dict):
            raise ValueError(f"line {lineno}: attempt must be a JSON object")

        policy = _string(x, "policy", lineno)
        if policy not in POLICY_LIMITS:
            raise ValueError(
                f"line {lineno}: unsupported policy {policy!r}; expected one of "
                f"{sorted(POLICY_LIMITS)}"
            )
        a = Attempt(
            task_id=_string(x, "task_id", lineno),
            repo=_string(x, "repo", lineno),
            policy=policy,
            passed=_boolean(x, "passed", lineno),
            patch_produced=_boolean(x, "patch_produced", lineno),
            wall_seconds=_finite_number(x, "wall_seconds", lineno),
            tool_calls=_integer(x, "tool_calls", lineno),
            first_edit_seconds=_optional_finite_number(x, "first_edit_seconds", lineno),
            test_seconds=_optional_finite_number(x, "test_seconds", lineno),
            diff_lines=_integer(x, "diff_lines", lineno),
        )

        if a.wall_seconds <= 0 or a.tool_calls < 0 or a.diff_lines < 0:
            raise ValueError(f"line {lineno}: negative/zero measurement")
        for field, value in (
            ("first_edit_seconds", a.first_edit_seconds),
            ("test_seconds", a.test_seconds),
        ):
            if value is not None and (value < 0 or value > a.wall_seconds):
                raise ValueError(
                    f"line {lineno}: {field} must be within [0, wall_seconds]"
                )
        if a.passed and not a.patch_produced:
            raise ValueError(f"line {lineno}: a passing attempt must produce a patch")
        if not a.patch_produced and a.diff_lines != 0:
            raise ValueError(
                f"line {lineno}: diff_lines must be 0 when no patch was produced"
            )

        wall_limit, call_limit = POLICY_LIMITS[a.policy]
        if a.wall_seconds > wall_limit:
            raise ValueError(
                f"line {lineno}: {a.policy} exceeds wall budget "
                f"({a.wall_seconds:g}s > {wall_limit:g}s)"
            )
        if a.tool_calls > call_limit:
            raise ValueError(
                f"line {lineno}: {a.policy} exceeds tool-call budget "
                f"({a.tool_calls} > {call_limit})"
            )
        rows.append(a)

    if not rows:
        raise ValueError("no attempts")
    return rows

def pctl(values: list[float], q: float) -> float | None:
    if not values:
        return None
    s = sorted(values)
    idx = (len(s) - 1) * q
    lo = int(idx)
    hi = min(lo + 1, len(s) - 1)
    frac = idx - lo
    return s[lo] * (1 - frac) + s[hi] * frac

def summarize(rows: Iterable[Attempt]) -> dict[str, Any]:
    r = list(rows)
    walls = [x.wall_seconds for x in r]
    no_patch_walls = [x.wall_seconds for x in r if not x.patch_produced]
    return {
        "attempts": len(r),
        "passes": sum(x.passed for x in r),
        "pass_rate": sum(x.passed for x in r) / len(r),
        "patch_rate": sum(x.patch_produced for x in r) / len(r),
        "wall_total_seconds": sum(walls),
        "wall_median_seconds": statistics.median(walls),
        "wall_p90_seconds": pctl(walls, .90),
        "tool_calls_total": sum(x.tool_calls for x in r),
        "no_patch_wall_seconds": sum(no_patch_walls),
        "no_patch_wall_share": sum(no_patch_walls) / sum(walls),
        "median_diff_lines": statistics.median([x.diff_lines for x in r]),
    }

def fixed_slice(rows: list[Attempt]) -> tuple[list[str], dict[tuple[str, str], dict[str, Attempt]]]:
    by_task: dict[tuple[str, str], dict[str, Attempt]] = defaultdict(dict)
    for a in rows:
        key = (a.repo, a.task_id)
        if a.policy in by_task[key]:
            raise ValueError(f"duplicate policy receipt for {a.repo}/{a.task_id}/{a.policy}")
        by_task[key][a.policy] = a

    policies = sorted({a.policy for a in rows})
    expected_policies = sorted(POLICY_LIMITS)
    if policies != expected_policies:
        raise ValueError(
            f"fixed A/B benchmark requires policies {expected_policies}; got {policies}"
        )

    missing: list[str] = []
    for (repo, task_id), d in sorted(by_task.items()):
        absent = [p for p in expected_policies if p not in d]
        if absent:
            missing.append(f"{repo}/{task_id}: missing {','.join(absent)}")
    if missing:
        preview = "; ".join(missing[:8])
        suffix = "" if len(missing) <= 8 else f"; ... +{len(missing) - 8} more"
        raise ValueError(f"policy task slices differ: {preview}{suffix}")

    return policies, by_task

def paired(
    policies: list[str],
    by_task: dict[tuple[str, str], dict[str, Attempt]],
) -> dict[str, Any]:
    p0, p1 = policies
    pairs = []
    for key, d in sorted(by_task.items()):
        a, b = d[p0], d[p1]
        pairs.append({
            "repo": key[0],
            "task_id": key[1],
            f"{p0}_pass": a.passed,
            f"{p1}_pass": b.passed,
            "pass_delta": int(b.passed) - int(a.passed),
            "wall_delta_seconds": b.wall_seconds - a.wall_seconds,
            "tool_call_delta": b.tool_calls - a.tool_calls,
        })
    return {"policies": policies, "paired_tasks": len(pairs), "pairs": pairs}

def select_policy(summaries: dict[str, dict[str, Any]]) -> dict[str, Any]:
    ranked = sorted(
        summaries,
        key=lambda p: (
            -summaries[p]["passes"],
            summaries[p]["no_patch_wall_seconds"],
            summaries[p]["wall_total_seconds"],
            summaries[p]["tool_calls_total"],
            p,
        ),
    )
    winner = ranked[0]
    return {
        "winner": winner,
        "ranking": ranked,
        "rule": (
            "Observed PASS count first on the identical task slice; ties break by "
            "lower no-patch wall waste, then lower total wall time, then fewer tool calls."
        ),
    }

def replay_cap(rows: list[Attempt], policy: str, cap_seconds: float) -> dict[str, Any]:
    chosen = sorted((x for x in rows if x.policy == policy), key=lambda x: (x.repo, x.task_id))
    elapsed = 0.0
    used: list[Attempt] = []
    skipped: list[str] = []
    for index, a in enumerate(chosen):
        if elapsed + a.wall_seconds > cap_seconds:
            skipped = [f"{x.repo}/{x.task_id}" for x in chosen[index:]]
            break
        elapsed += a.wall_seconds
        used.append(a)
    return {
        "policy": policy,
        "cap_seconds": cap_seconds,
        "observed_attempts_fit": len(used),
        "observed_passes_fit": sum(x.passed for x in used),
        "elapsed_seconds": elapsed,
        "headroom_seconds": cap_seconds - elapsed,
        "skipped_observed_tasks": skipped,
        "schedule_assumption": "lexicographic repo/task order",
        "warning": (
            "This is an observed-runtime fit simulation under the stated deterministic "
            "order, not a prediction of outcomes or a reconstruction of an unknown live schedule."
        ),
    }

def build_report(rows: list[Attempt], global_hours: float) -> dict[str, Any]:
    if not math.isfinite(global_hours) or global_hours <= 0:
        raise ValueError("--global-hours must be a positive finite number")

    policies, by_task = fixed_slice(rows)
    groups: dict[str, list[Attempt]] = defaultdict(list)
    for a in rows:
        groups[a.policy].append(a)
    summaries = {k: summarize(v) for k, v in sorted(groups.items())}
    return {
        "policy_summaries": summaries,
        "paired": paired(policies, by_task),
        "selection": select_policy(summaries),
        "global_cap_replay": [
            replay_cap(rows, p, global_hours * 3600) for p in policies
        ],
        "evidence_boundary": (
            "This tool scores observed dev receipts only; synthetic smoke data is not "
            "competition performance."
        ),
    }

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl", type=Path)
    ap.add_argument("--global-hours", type=float, default=12.0)
    args = ap.parse_args()
    try:
        rows = load(args.jsonl)
        report = build_report(rows, args.global_hours)
    except (OSError, ValueError) as e:
        print(json.dumps({"error": str(e)}, indent=2))
        return 2
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    sys.exit(main())
