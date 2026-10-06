import json
import unittest
from pathlib import Path

from baseline import evaluate, normalize_case


ROOT = Path(__file__).parent


class BaselineTests(unittest.TestCase):
    def setUp(self):
        self.fixtures = json.loads((ROOT / "fixtures.json").read_text())

    def test_frozen_manifest_shape_and_balance(self):
        self.assertEqual(20, len(self.fixtures))
        counts = {}
        for row in self.fixtures:
            counts[row["expected"]] = counts.get(row["expected"], 0) + 1
        self.assertEqual({
            "request_shape": 4,
            "auth_config": 4,
            "webhook_event": 4,
            "idempotency_duplicate": 4,
            "abstain": 4,
        }, counts)

    def test_receipt_is_complete_and_fail_closed(self):
        receipt = evaluate(self.fixtures)
        self.assertEqual(20, receipt["case_count"])
        self.assertEqual(20, receipt["top1_correct"])
        self.assertEqual(0, receipt["false_confident_count"])
        self.assertEqual(20, receipt["classifier_calls"])
        self.assertEqual("abstain", next(r for r in receipt["rows"] if r["id"] == "amb-04")["predicted"])

    def test_redacts_sensitive_values(self):
        row = next(r for r in self.fixtures if r["id"] == "auth-03")
        normalized = normalize_case(row)
        self.assertEqual("[REDACTED]", normalized["trace"]["authorization"])

    def test_rejects_duplicates_and_non_finite_values(self):
        with self.assertRaisesRegex(ValueError, "duplicate case id"):
            evaluate([self.fixtures[0], self.fixtures[0]])
        bad = {"id": "bad", "expected": "abstain", "trace": {"score": float("nan")}}
        with self.assertRaisesRegex(ValueError, "non-finite"):
            evaluate([bad])


if __name__ == "__main__":
    unittest.main()
