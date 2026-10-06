import unittest

from qloo_adapter import QlooAdapterError, QlooEntity, QlooInsightsResult
from qloo_planner import PlanningBrief, PreferredProperty, plan


def entity(entity_id, affinity, *, city="New York", kind="urn:entity:place", evidence=True):
    return QlooEntity(
        entity_id=entity_id,
        name=entity_id,
        entity_type=kind,
        affinity=affinity,
        properties={"geocode": {"city": city}, "indoor": entity_id.endswith("indoor")},
        evidence={"seed": 0.8} if evidence else {},
    )


class FakeClient:
    def __init__(self, entities=(), error=None):
        self.entities = tuple(entities)
        self.error = error
        self.calls = []

    def insights(self, **kwargs):
        self.calls.append(kwargs)
        if self.error:
            raise self.error
        return QlooInsightsResult(
            state="ok" if self.entities else "empty",
            entities=self.entities,
            duration_ms=12,
            warning=None,
            raw_query={},
        )


class PlannerTests(unittest.TestCase):
    def brief(self, **overrides):
        values = {
            "prompt_id": "travel-001",
            "scenario": "travel",
            "filter_type": "urn:entity:place",
            "interest_entity_queries": ("ambient music",),
        }
        values.update(overrides)
        return PlanningBrief(**values)

    def test_hard_constraints_filter_before_preferences(self):
        client = FakeClient([
            entity("blocked-indoor", 0.99),
            entity("wrong-city-indoor", 0.95, city="Boston"),
            entity("valid-outdoor", 0.80),
            entity("valid-indoor", 0.75),
        ])
        brief = self.brief(
            blocked_entity_ids=frozenset({"blocked-indoor"}),
            required_properties={"geocode.city": "New York"},
            preferences=(PreferredProperty("indoor", True, 0.20),),
        )
        result = plan(client, brief, run_id="repeat-1")
        self.assertEqual([item.entity_id for item in result.ranked], ["valid-indoor", "valid-outdoor"])
        self.assertEqual(result.receipt["constraints_satisfied"], 2)

    def test_type_constraint_and_tie_break_are_deterministic(self):
        client = FakeClient([
            entity("z", 0.5),
            entity("a", 0.5),
            entity("brand", 1.0, kind="urn:entity:brand"),
        ])
        result = plan(
            client,
            self.brief(allowed_entity_types=frozenset({"urn:entity:place"})),
            run_id="repeat-1",
        )
        self.assertEqual(result.receipt["ranked_ids"], ["a", "z"])

    def test_empty_evidence_fails_closed(self):
        result = plan(FakeClient(), self.brief(), run_id="repeat-1", failure_injected=True)
        self.assertEqual(result.state, "empty")
        self.assertEqual(result.ranked, ())
        self.assertEqual(result.receipt["fabricated_claims"], 0)
        self.assertEqual(result.receipt["ranked_ids"], [])

    def test_transport_error_is_a_scorer_compatible_closed_receipt(self):
        client = FakeClient(error=QlooAdapterError("transport_error", "offline"))
        result = plan(client, self.brief(), run_id="repeat-1", failure_injected=True)
        self.assertEqual(result.state, "error")
        self.assertEqual(result.error_code, "transport_error")
        self.assertEqual(
            set(result.receipt),
            {
                "prompt_id", "scenario", "run_id", "material_claims",
                "grounded_claims", "hard_constraints", "constraints_satisfied",
                "latency_ms", "ranked_ids", "qloo_calls", "failure_injected",
                "fabricated_claims",
            },
        )

    def test_three_repeats_have_zero_rank_set_churn(self):
        client = FakeClient([entity("p2", 0.7), entity("p1", 0.8)])
        ranked = [
            plan(client, self.brief(), run_id=f"repeat-{index}").receipt["ranked_ids"]
            for index in range(1, 4)
        ]
        self.assertEqual(ranked, [["p1", "p2"]] * 3)


if __name__ == "__main__":
    unittest.main()
