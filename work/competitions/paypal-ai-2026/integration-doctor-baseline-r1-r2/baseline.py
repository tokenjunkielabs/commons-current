#!/usr/bin/env python3
"""Deterministic, evidence-bounded baseline for sanitized PayPal traces."""

from __future__ import annotations

import argparse
import json
import math
import time
from collections import Counter
from pathlib import Path
from typing import Any

LABELS = {
    "request_shape",
    "auth_config",
    "webhook_event",
    "idempotency_duplicate",
    "abstain",
}
SENSITIVE_KEYS = {
    "authorization",
    "client_secret",
    "access_token",
    "refresh_token",
    "password",
}


def _clean(value: Any, key: str = "") -> Any:
    if key.lower() in SENSITIVE_KEYS:
        return "[REDACTED]"
    if isinstance(value, dict):
        return {str(k): _clean(v, str(k)) for k, v in sorted(value.items())}
    if isinstance(value, list):
        return [_clean(item) for item in value]
    if value is None or isinstance(value, (str, int, bool)):
        return value
    if isinstance(value, float) and math.isfinite(value):
        return value
    raise ValueError(f"unsupported or non-finite value at {key or '<root>'}")


def normalize_case(raw: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ValueError("case must be an object")
    case_id = raw.get("id")
    if not isinstance(case_id, str) or not case_id.strip():
        raise ValueError("case id must be a non-empty string")
    trace = raw.get("trace")
    if not isinstance(trace, dict):
        raise ValueError(f"{case_id}: trace must be an object")
    return {"id": case_id, "trace": _clean(trace)}


def classify(case: dict[str, Any]) -> dict[str, Any]:
    trace = case["trace"]
    candidates: list[tuple[str, list[str]]] = []

    status = trace.get("http_status")
    error = trace.get("error_name")
    if status in (400, 422) and error in {"INVALID_REQUEST", "VALIDATION_ERROR"}:
        candidates.append(("request_shape", ["http_status", "error_name"]))
    if status in (401, 403) and error in {"INVALID_CLIENT", "AUTHENTICATION_FAILURE"}:
        candidates.append(("auth_config", ["http_status", "error_name"]))
    if trace.get("webhook_verification") in {"failed", "missing"}:
        candidates.append(("webhook_event", ["webhook_verification"]))
    if trace.get("idempotency_result") in {"duplicate", "replayed"}:
        candidates.append(("idempotency_duplicate", ["idempotency_result"]))

    if len(candidates) != 1:
        reason = "no_supported_evidence" if not candidates else "conflicting_evidence"
        return {"label": "abstain", "reason": reason, "evidence": []}
    label, evidence = candidates[0]
    return {"label": label, "reason": "bounded_rule_match", "evidence": evidence}


def percentile(values: list[int], q: float) -> int:
    if not values:
        return 0
    ordered = sorted(values)
    index = math.ceil(q * len(ordered)) - 1
    return ordered[max(0, min(index, len(ordered) - 1))]


def evaluate(raw_cases: list[dict[str, Any]]) -> dict[str, Any]:
    seen: set[str] = set()
    rows = []
    durations = []
    for raw in raw_cases:
        expected = raw.get("expected")
        if expected not in LABELS:
            raise ValueError(f"invalid expected label: {expected!r}")
        case = normalize_case(raw)
        if case["id"] in seen:
            raise ValueError(f"duplicate case id: {case['id']}")
        seen.add(case["id"])
        started = time.perf_counter_ns()
        prediction = classify(case)
        durations.append((time.perf_counter_ns() - started) // 1_000)
        rows.append({
            "id": case["id"],
            "expected": expected,
            "predicted": prediction["label"],
            "reason": prediction["reason"],
            "evidence": prediction["evidence"],
        })

    correct = sum(row["expected"] == row["predicted"] for row in rows)
    ambiguous = [row for row in rows if row["expected"] == "abstain"]
    false_confident = sum(row["predicted"] != "abstain" for row in ambiguous)
    counts = Counter(row["expected"] for row in rows)
    return {
        "schema": "paypal-integration-doctor-baseline/v1",
        "fixture_kind": "synthetic_sanitized",
        "case_count": len(rows),
        "expected_counts": dict(sorted(counts.items())),
        "top1_correct": correct,
        "top1_accuracy": correct / len(rows) if rows else 0.0,
        "ambiguous_count": len(ambiguous),
        "false_confident_count": false_confident,
        "false_confident_rate": false_confident / len(ambiguous) if ambiguous else 0.0,
        "classifier_calls": len(rows),
        "latency_us": {"p50": percentile(durations, 0.50), "p95": percentile(durations, 0.95)},
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixtures", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    raw = json.loads(args.fixtures.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise SystemExit("fixture root must be an array")
    receipt = evaluate(raw)
    text = json.dumps(receipt, sort_keys=True, indent=2) + "\n"
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
