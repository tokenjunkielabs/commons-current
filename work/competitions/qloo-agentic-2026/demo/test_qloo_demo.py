from __future__ import annotations

import json
import unittest
from pathlib import Path

from qloo_demo import load_fixture, run_demo


FIXTURE = Path(__file__).with_name("fixtures.json")


class QlooDemoTest(unittest.TestCase):
    def test_three_scenarios_are_deterministic_and_constraint_safe(self) -> None:
        expected = {
            "launch": ["brand-pace", "brand-field"],
            "adjacency": ["brand-outdoor"],
            "travel": ["place-alfama"],
        }
        for scenario, ranked_ids in expected.items():
            with self.subTest(scenario=scenario):
                response = load_fixture(FIXTURE, scenario)
                first = run_demo(scenario, response, run_id="repeat")
                second = run_demo(scenario, response, run_id="repeat")
                self.assertEqual(first, second)
                self.assertEqual(first["state"], "ok")
                self.assertEqual(
                    [candidate["entity_id"] for candidate in first["ranked"]],
                    ranked_ids,
                )
                self.assertEqual(first["receipt"]["fabricated_claims"], 0)

    def test_empty_evidence_fails_closed(self) -> None:
        response = load_fixture(FIXTURE, "launch")
        output = run_demo("launch", response, run_id="empty", inject="empty")
        self.assertEqual(output["state"], "empty")
        self.assertEqual(output["ranked"], [])
        self.assertEqual(output["receipt"]["material_claims"], 0)

    def test_transport_failure_fails_closed_with_code(self) -> None:
        response = load_fixture(FIXTURE, "travel")
        output = run_demo("travel", response, run_id="transport", inject="transport")
        self.assertEqual(output["state"], "error")
        self.assertEqual(output["error_code"], "transport_error")
        self.assertEqual(output["ranked"], [])

    def test_invalid_fixture_is_rejected(self) -> None:
        bad = Path(__file__).with_name("invalid-fixture.tmp")
        bad.write_text(json.dumps({"launch": []}), encoding="utf-8")
        try:
            with self.assertRaisesRegex(ValueError, "no object"):
                load_fixture(bad, "launch")
        finally:
            bad.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
