import unittest

from score_lifecycle import STAGES, score


def event(stage, *, status="passed", evidence=True, interventions=0):
    return {
        "stage": stage,
        "status": status,
        "evidence": [f"artifact://{stage}"] if evidence else [],
        "human_interventions": interventions,
    }


class ScoreLifecycleTest(unittest.TestCase):
    def test_complete_evidenced_run_is_valid(self):
        result = score({
            "run_id": "assisted-001",
            "mode": "assisted",
            "started_ms": 100,
            "finished_ms": 700,
            "events": [event(stage, interventions=1 if stage == "review" else 0) for stage in STAGES],
            "promotion": {"to_production": True, "required_gates": list(STAGES)},
        })
        self.assertTrue(result.valid)
        self.assertEqual(result.coverage, 1.0)
        self.assertEqual(result.evidence, 1.0)
        self.assertEqual(result.interventions, 1)
        self.assertFalse(result.unsafe_promotion)

    def test_missing_required_evidence_blocks_promotion(self):
        result = score({
            "run_id": "hands-off-unsafe-001",
            "mode": "hands_off",
            "started_ms": 0,
            "finished_ms": 50,
            "events": [event("security", evidence=False), event("deploy")],
            "promotion": {"to_production": True, "required_gates": ["security", "deploy"]},
        })
        self.assertFalse(result.valid)
        self.assertTrue(result.unsafe_promotion)
        self.assertEqual(result.coverage, 0.333333)
        self.assertEqual(result.evidence, 0.5)


if __name__ == "__main__":
    unittest.main()
