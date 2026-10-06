import json, tempfile, unittest
from pathlib import Path
import trafficflowbench_receipt as t

def row(variant, panel, holdout, score, fp="data-r1", seed=7, runtime=10.0):
    return {
        "experiment_id": "blocked-month-r1", "variant": variant, "panel": panel,
        "holdout": holdout, "split": "train", "scorer": "official_task1_scorer",
        "data_fingerprint": fp,
        "code_revision": "base123" if variant == "baseline" else "cand456",
        "seed": seed, "s_state": score, "runtime_s": runtime, "peak_rss_mb": 120.0,
    }

class ReceiptTests(unittest.TestCase):
    def test_clean_pair_promotes(self):
        rows = [row("baseline","A","m8",.60), row("candidate","A","m8",.62),
                row("baseline","B","m8",.55), row("candidate","B","m8",.56)]
        report = t.summarize(rows)
        self.assertTrue(report["promotion_ready"])
        self.assertAlmostEqual(report["mean_delta_s_state"], .015)

    def test_panel_regression_blocks(self):
        rows = [row("baseline","A","m8",.60), row("candidate","A","m8",.64),
                row("baseline","B","m8",.55), row("candidate","B","m8",.54)]
        report = t.summarize(rows)
        self.assertFalse(report["promotion_ready"])
        self.assertTrue(any("worst_pair_delta" in x for x in report["promotion_reasons"]))

    def test_validation_receipt_rejected(self):
        bad = row("baseline","A","m8",.6); bad["split"] = "validation"
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"r.jsonl"; p.write_text(json.dumps(bad)+"\n")
            with self.assertRaisesRegex(ValueError, "only train"):
                t.load_rows(p)

    def test_mismatched_data_fingerprint_rejected(self):
        rows = [row("baseline","A","m8",.6,fp="x"), row("candidate","A","m8",.61,fp="y")]
        with self.assertRaisesRegex(ValueError, "data_fingerprint mismatch"):
            t.summarize(rows)

    def test_missing_pair_rejected(self):
        rows = [row("baseline","A","m8",.6), row("candidate","B","m8",.61)]
        with self.assertRaisesRegex(ValueError, "unpaired"):
            t.summarize(rows)

if __name__ == "__main__":
    unittest.main()
