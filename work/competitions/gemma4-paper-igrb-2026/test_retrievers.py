from __future__ import annotations

import unittest

from retrievers import RetrievalError, load_index, retrieve


INDEX = {
    "nodes": [
        {"id": "api:dispatch", "name": "dispatch_request", "text": "route an incoming HTTP request", "source_chars": 120},
        {"id": "auth:check", "name": "authorize", "text": "verify user permissions", "source_chars": 90},
        {"id": "cache:write", "name": "persist_entry", "text": "store an item", "source_chars": 80},
        {"id": "cache:evict", "name": "remove_stale", "text": "delete expired values", "source_chars": 70},
        {"id": "util:clock", "name": "monotonic_clock", "text": "time source", "source_chars": 40},
    ],
    "edges": [
        {"source": "api:dispatch", "target": "auth:check", "relation": "calls"},
        {"source": "cache:write", "target": "cache:evict", "relation": "calls"},
        {"source": "cache:evict", "target": "util:clock", "relation": "imports"},
        {"source": "util:clock", "target": "cache:write", "relation": "imports"},
    ],
}


class RetrieverTests(unittest.TestCase):
    def test_lexical_is_deterministic_and_budgeted(self) -> None:
        first = retrieve(INDEX, "expired cache values", method="lexical", budget_k=2)
        second = retrieve(INDEX, "expired cache values", method="lexical", budget_k=2)
        self.assertEqual(first, second)
        self.assertEqual(first["retrieved_symbols"][0], "cache:evict")
        self.assertEqual(len(first["retrieved_symbols"]), 2)
        self.assertEqual(first["candidate_chars"], 150)

    def test_graph_expansion_finds_vocabulary_mismatched_neighbor(self) -> None:
        receipt = retrieve(
            INDEX,
            "store item",
            method="graph",
            budget_k=3,
            seed_count=1,
            hops=1,
            relations=["calls"],
        )
        self.assertEqual(receipt["retrieved_symbols"][:2], ["cache:write", "cache:evict"])
        self.assertNotIn("util:clock", receipt["retrieved_symbols"])

    def test_hybrid_rrf_preserves_seed_and_structural_evidence(self) -> None:
        receipt = retrieve(
            INDEX,
            "incoming HTTP request",
            method="hybrid",
            budget_k=2,
            seed_count=1,
            hops=1,
            relations=["calls"],
        )
        self.assertEqual(receipt["retrieved_symbols"], ["api:dispatch", "auth:check"])
        self.assertEqual(receipt["config"]["method"], "hybrid")
        self.assertEqual(len(receipt["receipt_sha256"]), 64)

    def test_cycles_do_not_duplicate_results(self) -> None:
        receipt = retrieve(INDEX, "time source", method="graph", budget_k=5, seed_count=1, hops=2)
        self.assertEqual(len(receipt["retrieved_symbols"]), len(set(receipt["retrieved_symbols"])))
        self.assertEqual(set(receipt["retrieved_symbols"]), {"cache:write", "cache:evict", "util:clock"})

    def test_invalid_contracts_fail_closed(self) -> None:
        with self.assertRaises(RetrievalError):
            retrieve(INDEX, "cache", method="embedding", budget_k=1)
        with self.assertRaises(RetrievalError):
            retrieve(INDEX, "cache", method="lexical", budget_k=0)
        broken = {"nodes": INDEX["nodes"], "edges": [{"source": "missing", "target": "cache:write", "relation": "calls"}]}
        with self.assertRaises(RetrievalError):
            load_index(broken)


if __name__ == "__main__":
    unittest.main()
