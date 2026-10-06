#!/usr/bin/env python3
"""BuildArena S02 telemetry gate and run comparator.

This module analyzes exported telemetry only.  It does not create vehicles,
controllers, MCP commands, or competition submissions.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


MIN_RADIUS = 1100.0
REQUIRED_ORBITS = 3


class TraceError(ValueError):
    """Raised when a telemetry export cannot be interpreted safely."""


def _finite_number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TraceError(f"{field} must be a number")
    number = float(value)
    if not math.isfinite(number):
        raise TraceError(f"{field} must be finite")
    return number


def load_samples(path: Path) -> list[dict[str, Any]]:
    """Load a JSON array/object or NDJSON telemetry export."""
    text = path.read_text(encoding="utf-8")
    stripped = text.lstrip()
    if not stripped:
        raise TraceError("telemetry file is empty")

    try:
        decoded = json.loads(text)
    except json.JSONDecodeError as error:
        if "Extra data" not in str(error):
            raise TraceError(f"invalid JSON telemetry: {error.msg}") from error
        samples = [json.loads(line) for line in text.splitlines() if line.strip()]
    else:
        if isinstance(decoded, dict):
            decoded = decoded.get("samples")
        if not isinstance(decoded, list):
            raise TraceError("JSON telemetry must be an array or {samples: [...]} object")
        samples = decoded

    if not samples or any(not isinstance(sample, dict) for sample in samples):
        raise TraceError("telemetry must contain at least one object sample")
    return samples


def score_run(samples: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Score one telemetry run against the public hard orbit gate."""
    points = list(samples)
    if not points:
        raise TraceError("run has no samples")

    maxima: dict[str, float] = defaultdict(lambda: float("-inf"))
    seen_optional: dict[str, list[float]] = {"machine_integrity": [], "fuel": []}
    payload_recovered = False
    landed = False
    landing_speeds: list[float] = []

    for index, sample in enumerate(points):
        orbit = sample.get("orbit_index")
        if orbit is None:
            continue
        if isinstance(orbit, bool) or not isinstance(orbit, (str, int)):
            raise TraceError(f"sample {index}: orbit_index must be a string or integer")
        if sample.get("orbit_valid") is False:
            continue
        radius = _finite_number(sample.get("radius"), f"sample {index}: radius")
        maxima[str(orbit)] = max(maxima[str(orbit)], radius)

        payload_recovered = payload_recovered or sample.get("payload_recovered") is True
        landed = landed or sample.get("landed") is True
        if sample.get("landing_speed") is not None:
            landing_speeds.append(abs(_finite_number(sample["landing_speed"], "landing_speed")))
        for field in seen_optional:
            if sample.get(field) is not None:
                seen_optional[field].append(_finite_number(sample[field], field))

    qualified = sorted(orbit for orbit, radius in maxima.items() if radius > MIN_RADIUS)
    result: dict[str, Any] = {
        "gate_pass": len(qualified) >= REQUIRED_ORBITS,
        "qualified_orbit_count": len(qualified),
        "qualified_orbits": qualified,
        "orbit_max_radius": dict(sorted(maxima.items())),
        "payload_recovered_observed": payload_recovered,
        "landed_observed": landed,
        "sample_count": len(points),
    }
    if landing_speeds:
        result["best_landing_speed"] = min(landing_speeds)
    for field, values in seen_optional.items():
        if values:
            result[f"mean_{field}"] = sum(values) / len(values)
    return result


def comparison_key(receipt: dict[str, Any]) -> tuple[Any, ...]:
    """Return a deterministic key; missing optional telemetry gives no advantage."""
    return (
        receipt["gate_pass"],
        receipt["qualified_orbit_count"],
        receipt.get("payload_recovered_observed", False),
        receipt.get("landed_observed", False),
        -receipt.get("best_landing_speed", float("inf")),
        receipt.get("mean_machine_integrity", float("-inf")),
        receipt.get("mean_fuel", float("-inf")),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("traces", nargs="+", type=Path)
    args = parser.parse_args()

    receipts = []
    for path in args.traces:
        receipt = score_run(load_samples(path))
        receipt["trace"] = str(path)
        receipts.append(receipt)
    receipts.sort(key=comparison_key, reverse=True)
    print(json.dumps({"ranked_runs": receipts}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
