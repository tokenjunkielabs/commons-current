from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "adapter"))
sys.path.insert(0, str(ROOT / "planner"))

from qloo_adapter import QlooAdapterError, QlooClient  # noqa: E402
from qloo_planner import PlanningBrief, PreferredProperty, plan  # noqa: E402


def fixture_transport(response: Mapping[str, Any]):
    def transport(
        _url: str,
        _headers: Mapping[str, str],
        _payload: Mapping[str, Any],
        _timeout_seconds: float,
    ) -> Mapping[str, Any]:
        return response

    return transport


def failing_transport(
    _url: str,
    _headers: Mapping[str, str],
    _payload: Mapping[str, Any],
    _timeout_seconds: float,
) -> Mapping[str, Any]:
    raise QlooAdapterError("transport_error", "injected offline transport failure")


def load_fixture(path: Path, scenario: str) -> Mapping[str, Any]:
    decoded = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(decoded, Mapping):
        raise ValueError("fixture root must be an object")
    response = decoded.get(scenario)
    if not isinstance(response, Mapping):
        raise ValueError(f"fixture has no object for scenario {scenario!r}")
    return response


def brief_for(scenario: str) -> PlanningBrief:
    if scenario == "launch":
        return PlanningBrief(
            prompt_id="demo-launch-001",
            scenario="launch",
            filter_type="urn:entity:brand",
            interest_entity_queries=("independent running",),
            allowed_entity_types=frozenset({"urn:entity:brand"}),
            required_properties={"available": True},
            preferences=(PreferredProperty("segment", "performance", 0.05),),
        )
    if scenario == "adjacency":
        return PlanningBrief(
            prompt_id="demo-adjacency-001",
            scenario="adjacency",
            filter_type="urn:entity:brand",
            interest_entity_ids=("brand-anchor",),
            blocked_entity_ids=frozenset({"brand-blocked"}),
            preferences=(PreferredProperty("segment", "outdoor", 0.04),),
        )
    if scenario == "travel":
        return PlanningBrief(
            prompt_id="demo-travel-001",
            scenario="travel",
            filter_type="urn:entity:place",
            interest_tags=("food", "design"),
            location_query="Lisbon",
            allowed_entity_types=frozenset({"urn:entity:place"}),
            required_properties={"open": True},
            preferences=(PreferredProperty("neighborhood", "Alfama", 0.03),),
        )
    raise ValueError(f"unsupported scenario: {scenario}")


def run_demo(
    scenario: str,
    response: Mapping[str, Any],
    *,
    run_id: str,
    inject: str | None = None,
) -> dict[str, Any]:
    if inject == "empty":
        response = {"success": True, "results": {"entities": []}, "query": {}}
    transport = failing_transport if inject == "transport" else fixture_transport(response)
    client = QlooClient("offline-fixture", transport=transport)
    result = plan(
        client,
        brief_for(scenario),
        run_id=run_id,
        failure_injected=inject is not None,
    )
    return {
        "mode": "offline_fixture",
        "scenario": scenario,
        "state": result.state,
        "error_code": result.error_code,
        "ranked": [
            {
                "entity_id": candidate.entity_id,
                "name": candidate.name,
                "score": candidate.score,
                "affinity": candidate.affinity,
                "evidence": candidate.evidence,
            }
            for candidate in result.ranked
        ],
        "receipt": dict(result.receipt),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the Qloo planner with deterministic offline evidence")
    parser.add_argument("--scenario", choices=("launch", "adjacency", "travel"), required=True)
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path(__file__).with_name("fixtures.json"),
        help="JSON fixture map; defaults to the bundled deterministic examples",
    )
    parser.add_argument("--run-id", default="offline-demo-001")
    parser.add_argument("--inject", choices=("empty", "transport"))
    args = parser.parse_args(argv)

    try:
        response = load_fixture(args.fixture, args.scenario)
        output = run_demo(args.scenario, response, run_id=args.run_id, inject=args.inject)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"state": "fixture_error", "error": str(exc)}, sort_keys=True))
        return 2

    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["state"] == "ok" else 3


if __name__ == "__main__":
    raise SystemExit(main())
