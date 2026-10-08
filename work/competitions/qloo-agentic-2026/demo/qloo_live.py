from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from pathlib import Path
from typing import Any, Sequence
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "adapter"))
sys.path.insert(0, str(ROOT / "planner"))

from qloo_adapter import QlooAdapterError, QlooClient, SUPPORTED_FILTER_TYPES  # noqa: E402
from qloo_planner import PlanningBrief, PreferredProperty, plan  # noqa: E402


def nonblank(value: str) -> str:
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("value must not be blank")
    return value


def property_value(value: str) -> tuple[str, Any]:
    path, separator, encoded = value.partition("=")
    if not separator or not path or any(not part for part in path.split(".")):
        raise argparse.ArgumentTypeError("expected property.path=JSON_VALUE")
    try:
        decoded = json.loads(encoded)
        json.dumps(decoded, allow_nan=False)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("property value must be valid JSON") from exc
    if decoded is None:
        raise argparse.ArgumentTypeError("null is not a supported property constraint")
    return path, decoded


def preference(value: str) -> PreferredProperty:
    expression, separator, raw_weight = value.rpartition("@")
    if not separator:
        raise argparse.ArgumentTypeError("expected property.path=JSON_VALUE@WEIGHT")
    path, decoded = property_value(expression)
    try:
        weight = float(raw_weight)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("preference weight must be a number") from exc
    if not math.isfinite(weight) or weight < 0:
        raise argparse.ArgumentTypeError("preference weight must be finite and non-negative")
    return PreferredProperty(path, decoded, weight)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the existing planner against the live Qloo Insights API")
    parser.add_argument("--scenario", required=True, choices=("launch", "adjacency", "travel"))
    parser.add_argument("--prompt-id", required=True, type=nonblank)
    parser.add_argument("--filter-type", required=True, choices=sorted(SUPPORTED_FILTER_TYPES - {"urn:heatmap"}))
    parser.add_argument("--interest-id", action="append", default=[], type=nonblank, help="resolved Qloo entity ID; repeatable")
    parser.add_argument("--interest-tag", action="append", default=[], type=nonblank, help="Qloo tag ID; repeatable")
    parser.add_argument("--location", type=nonblank, help="locality name for filter.location.query")
    parser.add_argument("--take", type=int, choices=range(1, 51), default=10, metavar="1..50")
    parser.add_argument("--block-id", action="append", default=[], type=nonblank)
    parser.add_argument("--require", action="append", default=[], type=property_value, metavar="PATH=JSON_VALUE")
    parser.add_argument("--prefer", action="append", default=[], type=preference, metavar="PATH=JSON_VALUE@WEIGHT")
    parser.add_argument("--run-id", type=nonblank, default=str(uuid4()))
    parser.add_argument("--receipt-file", type=Path, help="append one scorer-compatible JSONL receipt after the request")
    args = parser.parse_args(argv)
    if not (args.interest_id or args.interest_tag or args.location):
        parser.error("supply at least one --interest-id, --interest-tag, or --location")
    required = dict(args.require)
    if len(required) != len(args.require):
        parser.error("each --require property path must appear only once")
    brief = PlanningBrief(
        prompt_id=args.prompt_id,
        scenario=args.scenario,
        filter_type=args.filter_type,
        interest_entity_ids=tuple(args.interest_id),
        interest_tags=tuple(args.interest_tag),
        location_query=args.location,
        take=args.take,
        allowed_entity_types=frozenset({args.filter_type}),
        blocked_entity_ids=frozenset(args.block_id),
        required_properties=required,
        preferences=tuple(args.prefer),
    )
    try:
        client = QlooClient(os.environ.get("QLOO_API_KEY", ""))
    except QlooAdapterError as exc:
        print(json.dumps({"mode": "live", "state": "configuration_error", "error_code": exc.code,
                          "error": str(exc), "qloo_calls": 0, "ranked": []}, sort_keys=True))
        return 2

    started = time.perf_counter()
    result = plan(client, brief, run_id=args.run_id)
    receipt = dict(result.receipt)
    receipt["latency_ms"] = (time.perf_counter() - started) * 1000
    output = {
        "mode": "live", "scenario": args.scenario, "state": result.state,
        "error_code": result.error_code,
        "ranked": [{"entity_id": item.entity_id, "name": item.name, "score": item.score,
                    "affinity": item.affinity, "evidence": item.evidence} for item in result.ranked],
        "receipt": receipt,
    }
    if args.receipt_file is not None:
        try:
            with args.receipt_file.open("a", encoding="utf-8") as stream:
                stream.write(json.dumps(receipt, sort_keys=True) + "\n")
        except OSError:
            output["receipt_error"] = "receipt_write_failed"
            print(json.dumps(output, indent=2, sort_keys=True))
            return 4
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if result.state == "ok" else 3


if __name__ == "__main__":
    raise SystemExit(main())
