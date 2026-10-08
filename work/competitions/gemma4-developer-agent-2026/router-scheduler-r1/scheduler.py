#!/usr/bin/env python3
"""Offline budget decisions; does not execute tasks or estimate benchmark outcomes."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path

POLICIES = {"5m80": (300.0, 80), "7m100": (420.0, 100)}
SHAPE_POLICY = {
    "bug": "5m80", "regression": "5m80", "build": "5m80",
    "behavior": "7m100", "navigation": "7m100",
}
SHAPE_WORDS = (
    ("build", {"dependency", "dependencies", "install", "packaging", "build", "ci", "configuration"}),
    ("regression", {"regression", "regressions", "test", "tests"}),
    ("navigation", {"repository", "architecture", "refactor", "refactoring", "cross-module"}),
    ("behavior", {"api", "support", "feature", "implement", "behavior"}),
)
GLOBAL_CAP = 12 * 3600.0
VERSION = 1


def number(value, label, minimum=0.0, maximum=None):
    if type(value) not in (int, float):
        raise ValueError(f"{label} must be a finite JSON number")
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError(f"{label} must be finite") from exc
    if not math.isfinite(result) or result < minimum or (maximum is not None and result > maximum):
        raise ValueError(f"{label} is outside its finite allowed range")
    return result


def string(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value.strip()


def classify(text):
    words = set(re.findall(r"[a-z]+(?:-[a-z]+)*", text.lower()))
    for shape, cues in SHAPE_WORDS:
        if words & cues:
            return shape
    return "bug"


def digest(value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    return hashlib.sha256(encoded).hexdigest()


def decide(snapshot):
    """Return one bounded allocation from a complete, authoritative runner snapshot."""
    if not isinstance(snapshot, dict):
        raise ValueError("snapshot must be a JSON object")
    cap = number(snapshot.get("budget_seconds", GLOBAL_CAP), "budget_seconds", 0.001, GLOBAL_CAP)
    elapsed = number(snapshot.get("elapsed_seconds"), "elapsed_seconds")
    quantum = number(snapshot.get("quantum_seconds", 60), "quantum_seconds", 0.001)
    raw_tasks = snapshot.get("tasks")
    if not isinstance(raw_tasks, list):
        raise ValueError("tasks must be a JSON array")

    tasks, seen, active, accounted = [], set(), None, 0.0
    for index, raw in enumerate(raw_tasks):
        if not isinstance(raw, dict):
            raise ValueError(f"task {index} must be an object")
        repo = string(raw.get("repo"), f"task {index} repo")
        task_id = string(raw.get("task_id"), f"task {index} task_id")
        key = (repo, task_id)
        if key in seen:
            raise ValueError(f"duplicate task identity: {repo}/{task_id}")
        seen.add(key)
        status = raw.get("status", "pending")
        if status not in ("pending", "active", "done", "abandoned"):
            raise ValueError(f"task {index}: unknown status")
        text = string(raw.get("text"), f"task {index} text")
        shape = raw.get("shape", classify(text))
        if shape not in SHAPE_POLICY:
            raise ValueError(f"task {index}: unknown task shape")
        policy = SHAPE_POLICY[shape]
        wall_limit, call_limit = POLICIES[policy]
        charged = number(raw.get("charged_seconds", 0), f"task {index} charged_seconds")
        calls = raw.get("tool_calls", 0)
        if type(calls) is not int or calls < 0:
            raise ValueError(f"task {index} tool_calls must be a non-negative JSON integer")
        if status == "pending" and (charged or calls):
            raise ValueError(f"task {index}: attempted work must be active or terminal")
        accounted += charged
        estimate = raw.get("gain_estimate")
        gain, estimate_seconds = None, None
        if estimate is not None:
            if not isinstance(estimate, dict):
                raise ValueError(f"task {index}: gain_estimate must be an object")
            gain = number(estimate.get("probability"), f"task {index} probability", 0, 1)
            estimate_seconds = number(estimate.get("seconds"), f"task {index} estimate seconds", 0.001)
            string(estimate.get("source"), f"task {index} estimate source")
        task = {
            "repo": repo, "task_id": task_id, "status": status, "shape": shape,
            "policy": policy, "seconds_left": max(0.0, wall_limit - charged),
            "calls_left": max(0, call_limit - calls), "gain": gain,
            "estimate_seconds": estimate_seconds, "index": index,
        }
        tasks.append(task)
        if status == "active":
            if active is not None:
                raise ValueError("only one active task is supported")
            active = task
    if accounted > elapsed + 1e-9:
        raise ValueError("elapsed_seconds must include all task charged_seconds and runner overhead")

    headroom = max(0.0, cap - elapsed)
    candidates = [
        task for task in tasks
        if task["status"] in ("pending", "active") and task["seconds_left"] > 0 and task["calls_left"] > 0
    ]
    mode = "estimate_rate" if candidates and all(t["gain"] is not None for t in candidates) else "fifo"
    chosen = None
    reason = "no_runnable_tasks"
    if headroom == 0:
        reason = "global_budget_exhausted"
    elif candidates:
        if mode == "estimate_rate":
            # The caller supplies conditional marginal gains; no outcome is read or fitted here.
            candidates = [t for t in candidates if t["estimate_seconds"] <= min(t["seconds_left"], headroom)]
            candidates.sort(key=lambda t: (
                -(t["gain"] / t["estimate_seconds"]),
                t is not active, t["index"],
            ))
            if not candidates:
                reason = "no_supplied_estimate_fits_remaining_budget"
            elif candidates[0]["gain"] > 0:
                chosen = candidates[0]
                reason = "highest_supplied_marginal_gain_per_second"
            else:
                reason = "all_supplied_marginal_gains_zero"
        else:
            # Missing estimates must not be replaced with fabricated success probabilities.
            chosen = active if active in candidates else candidates[0]
            reason = "active_then_fifo_without_complete_estimates"

    def identity(task):
        return {"repo": task["repo"], "task_id": task["task_id"]} if task else None

    allocation = None
    if chosen is not None:
        seconds = min(quantum, headroom, chosen["seconds_left"])
        if chosen["estimate_seconds"] is not None:
            seconds = min(seconds, chosen["estimate_seconds"])
        allocation = {
            **identity(chosen), "shape": chosen["shape"], "policy": chosen["policy"],
            "max_seconds": seconds, "max_additional_tool_calls": chosen["calls_left"],
            "task_seconds_remaining": chosen["seconds_left"],
        }
    action = "stop" if chosen is None else ("continue" if chosen is active else ("switch" if active else "start"))
    result = {
        "version": VERSION, "action": action, "reason": reason, "selection_mode": mode,
        "stop_task": identity(active) if active is not None and chosen is not active else None,
        "allocation": allocation, "global_seconds_remaining": headroom,
        "input_sha256": digest(snapshot),
        "policy_sha256": digest({"version": VERSION, "limits": POLICIES, "shapes": SHAPE_POLICY,
                                 "cues": [(s, sorted(w)) for s, w in SHAPE_WORDS], "global_cap": GLOBAL_CAP}),
        "evidence_boundary": "Budget decision only; supplied gain estimates are not measured pass rates.",
    }
    result["decision_sha256"] = digest(result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", help="Runner snapshot JSON path, or - for stdin")
    args = parser.parse_args()
    try:
        raw = sys.stdin.read() if args.snapshot == "-" else Path(args.snapshot).read_text(encoding="utf-8")
        result = decide(json.loads(raw))
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        print(json.dumps({"error": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
