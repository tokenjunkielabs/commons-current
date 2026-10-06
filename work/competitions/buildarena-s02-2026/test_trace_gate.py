import json
import tempfile
import unittest
from pathlib import Path

from trace_gate import TraceError, comparison_key, load_samples, score_run


def sample(orbit, radius, **extra):
    return {"orbit_index": orbit, "radius": radius, **extra}


class TraceGateTests(unittest.TestCase):
    def test_requires_three_distinct_orbits_strictly_above_radius(self):
        receipt = score_run([
            sample(0, 1100), sample(0, 1200), sample(1, 1201), sample(2, 1202)
        ])
        self.assertTrue(receipt["gate_pass"])
        self.assertEqual(receipt["qualified_orbit_count"], 3)

    def test_invalid_orbits_and_missing_optional_fields_do_not_help(self):
        receipt = score_run([
            sample(0, 1300), sample(1, 1400, orbit_valid=False), sample(2, 1500)
        ])
        self.assertFalse(receipt["gate_pass"])
        self.assertNotIn("mean_fuel", receipt)
        self.assertNotIn("best_landing_speed", receipt)

    def test_comparator_prefers_gate_then_observed_recovery(self):
        fail = score_run([sample(0, 2000, landed=True, payload_recovered=True)])
        passed = score_run([sample(i, 1101 + i) for i in range(3)])
        recovered = score_run([
            sample(i, 1101 + i, payload_recovered=i == 2, landed=i == 2)
            for i in range(3)
        ])
        self.assertGreater(comparison_key(passed), comparison_key(fail))
        self.assertGreater(comparison_key(recovered), comparison_key(passed))

    def test_json_and_ndjson_loaders_match_and_malformed_fails_closed(self):
        rows = [sample(i, 1200 + i) for i in range(3)]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            array_path = root / "array.json"
            lines_path = root / "lines.ndjson"
            array_path.write_text(json.dumps({"samples": rows}), encoding="utf-8")
            lines_path.write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")
            self.assertEqual(load_samples(array_path), load_samples(lines_path))
            with self.assertRaises(TraceError):
                score_run([sample(0, float("nan"))])


if __name__ == "__main__":
    unittest.main()
