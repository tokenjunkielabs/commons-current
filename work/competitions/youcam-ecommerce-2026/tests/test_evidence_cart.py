import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from evidence_cart import FixtureProvider, benchmark, decide, normalize_observation  # noqa: E402


class EvidenceCartTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture_rows = json.loads((ROOT / "fixtures/cases.json").read_text())
        cls.provider = FixtureProvider({row["case_id"]: row for row in fixture_rows})
        cls.catalog = json.loads((ROOT / "fixtures/catalog.json").read_text())

    def test_normal_case_is_evidence_ranked_and_stable(self):
        first = decide(self.provider, "normal-dry-red", self.catalog)
        second = decide(self.provider, "normal-dry-red", self.catalog)
        self.assertEqual(first, second)
        self.assertEqual(first.status, "ok")
        self.assertEqual(first.recommendations[0].item_id, "calm-01")
        self.assertEqual(first.recommendations[0].matched_concerns, ("dryness", "redness"))

    def test_low_quality_is_weak_evidence(self):
        decision = decide(self.provider, "weak-low-quality", self.catalog)
        self.assertEqual((decision.status, decision.reason), ("weak_evidence", "low_quality"))
        self.assertFalse(decision.recommendations)

    def test_no_supported_catalog_item_is_explicit_zero_match(self):
        decision = decide(self.provider, "zero-match", self.catalog)
        self.assertEqual(decision.status, "zero_match")

    def test_timeout_and_partial_response_are_typed_provider_errors(self):
        timeout = decide(self.provider, "provider-timeout", self.catalog)
        partial = decide(self.provider, "invalid-partial-response", self.catalog)
        self.assertEqual(timeout.error_class, "TimeoutError")
        self.assertEqual(partial.error_class, "InvalidResponse")

    def test_normalization_rejects_nonfinite_or_duplicate_concerns(self):
        with self.assertRaises(ValueError):
            normalize_observation({"face_detected": True, "quality": float("nan"), "concerns": []})
        with self.assertRaisesRegex(ValueError, "duplicate concern"):
            normalize_observation({
                "face_detected": True,
                "quality": 0.9,
                "concerns": [
                    {"name": "Dryness", "confidence": 0.8},
                    {"name": "dryness", "confidence": 0.7},
                ],
            })

    def test_receipt_has_failure_coverage_without_raw_image_data(self):
        receipt = benchmark(
            self.provider,
            ["normal-dry-red", "weak-low-quality", "zero-match", "provider-timeout", "invalid-partial-response"],
            self.catalog,
        )
        self.assertEqual(receipt["case_count"], 5)
        self.assertEqual(receipt["status_counts"], {
            "ok": 1,
            "provider_error": 2,
            "weak_evidence": 1,
            "zero_match": 1,
        })
        self.assertTrue(receipt["deterministic"])
        self.assertEqual(receipt["grounding_rate"], 1.0)
        self.assertFalse(receipt["privacy"]["raw_image_in_receipt"])
        self.assertNotIn("image", json.dumps(receipt).lower().replace("raw_image", ""))


if __name__ == "__main__":
    unittest.main()
