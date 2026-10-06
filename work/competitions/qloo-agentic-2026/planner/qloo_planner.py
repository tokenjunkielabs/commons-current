from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol, Sequence

from qloo_adapter import QlooAdapterError, QlooEntity, QlooInsightsResult


SCENARIOS = frozenset({"launch", "adjacency", "travel"})


class InsightsClient(Protocol):
    def insights(
        self,
        *,
        filter_type: str,
        interest_entity_ids: Sequence[str] = (),
        interest_entity_queries: Sequence[str] = (),
        interest_tags: Sequence[str] = (),
        location_query: str | None = None,
        take: int = 10,
    ) -> QlooInsightsResult: ...


@dataclass(frozen=True)
class PreferredProperty:
    path: str
    value: Any
    weight: float = 0.05

    def __post_init__(self) -> None:
        if not self.path:
            raise ValueError("preferred property path is required")
        if self.weight < 0:
            raise ValueError("preferred property weight must be non-negative")


@dataclass(frozen=True)
class PlanningBrief:
    prompt_id: str
    scenario: str
    filter_type: str
    interest_entity_ids: tuple[str, ...] = ()
    interest_entity_queries: tuple[str, ...] = ()
    interest_tags: tuple[str, ...] = ()
    location_query: str | None = None
    take: int = 10
    allowed_entity_types: frozenset[str] = frozenset()
    blocked_entity_ids: frozenset[str] = frozenset()
    required_properties: Mapping[str, Any] = field(default_factory=dict)
    preferences: tuple[PreferredProperty, ...] = ()

    def __post_init__(self) -> None:
        if not self.prompt_id:
            raise ValueError("prompt_id is required")
        if self.scenario not in SCENARIOS:
            raise ValueError(f"unsupported scenario: {self.scenario}")


@dataclass(frozen=True)
class RankedCandidate:
    entity_id: str
    name: str
    score: float
    affinity: float | None
    evidence: Mapping[str, Any]


@dataclass(frozen=True)
class PlanResult:
    state: str
    ranked: tuple[RankedCandidate, ...]
    receipt: Mapping[str, Any]
    error_code: str | None = None


def plan(
    client: InsightsClient,
    brief: PlanningBrief,
    *,
    run_id: str,
    latency_ms: float = 0.0,
    failure_injected: bool = False,
) -> PlanResult:
    """Build a deterministic evidence-ranked plan or fail closed.

    Hard constraints are evaluated before preferences. Empty, malformed, and
    transport-failure paths never create fallback candidates or taste claims.
    """
    hard_constraint_count = _hard_constraint_count(brief)
    try:
        insights = client.insights(
            filter_type=brief.filter_type,
            interest_entity_ids=brief.interest_entity_ids,
            interest_entity_queries=brief.interest_entity_queries,
            interest_tags=brief.interest_tags,
            location_query=brief.location_query,
            take=brief.take,
        )
    except QlooAdapterError as exc:
        return _closed_result(
            brief,
            run_id,
            latency_ms,
            failure_injected,
            hard_constraint_count,
            state="error",
            error_code=exc.code,
        )

    if insights.state != "ok" or not insights.entities:
        return _closed_result(
            brief,
            run_id,
            latency_ms,
            failure_injected,
            hard_constraint_count,
            state="empty",
        )

    eligible = [entity for entity in insights.entities if _satisfies_hard_constraints(entity, brief)]
    if not eligible:
        return _closed_result(
            brief,
            run_id,
            latency_ms,
            failure_injected,
            hard_constraint_count,
            state="no_match",
        )

    ranked = tuple(
        sorted(
            (_ranked_candidate(entity, brief.preferences) for entity in eligible),
            key=lambda candidate: (-candidate.score, candidate.entity_id),
        )
    )
    grounded = sum(bool(item.evidence) or item.affinity is not None for item in ranked)
    receipt = _receipt(
        brief,
        run_id,
        latency_ms,
        failure_injected,
        material_claims=len(ranked),
        grounded_claims=grounded,
        hard_constraints=hard_constraint_count,
        constraints_satisfied=hard_constraint_count,
        ranked_ids=[item.entity_id for item in ranked],
        fabricated_claims=0,
    )
    return PlanResult(state="ok", ranked=ranked, receipt=receipt)


def _hard_constraint_count(brief: PlanningBrief) -> int:
    return (
        (1 if brief.allowed_entity_types else 0)
        + len(brief.blocked_entity_ids)
        + len(brief.required_properties)
    )


def _satisfies_hard_constraints(entity: QlooEntity, brief: PlanningBrief) -> bool:
    if brief.allowed_entity_types and entity.entity_type not in brief.allowed_entity_types:
        return False
    if entity.entity_id in brief.blocked_entity_ids:
        return False
    return all(_property(entity.properties, path) == value for path, value in brief.required_properties.items())


def _property(properties: Mapping[str, Any], path: str) -> Any:
    value: Any = properties
    for part in path.split("."):
        if not isinstance(value, Mapping) or part not in value:
            return None
        value = value[part]
    return value


def _ranked_candidate(entity: QlooEntity, preferences: Sequence[PreferredProperty]) -> RankedCandidate:
    score = entity.affinity if entity.affinity is not None else 0.0
    for preference in preferences:
        if _property(entity.properties, preference.path) == preference.value:
            score += preference.weight
    return RankedCandidate(
        entity_id=entity.entity_id,
        name=entity.name,
        score=score,
        affinity=entity.affinity,
        evidence=dict(entity.evidence),
    )


def _closed_result(
    brief: PlanningBrief,
    run_id: str,
    latency_ms: float,
    failure_injected: bool,
    hard_constraint_count: int,
    *,
    state: str,
    error_code: str | None = None,
) -> PlanResult:
    receipt = _receipt(
        brief,
        run_id,
        latency_ms,
        failure_injected,
        material_claims=0,
        grounded_claims=0,
        hard_constraints=hard_constraint_count,
        constraints_satisfied=hard_constraint_count,
        ranked_ids=[],
        fabricated_claims=0,
    )
    return PlanResult(state=state, ranked=(), receipt=receipt, error_code=error_code)


def _receipt(
    brief: PlanningBrief,
    run_id: str,
    latency_ms: float,
    failure_injected: bool,
    *,
    material_claims: int,
    grounded_claims: int,
    hard_constraints: int,
    constraints_satisfied: int,
    ranked_ids: list[str],
    fabricated_claims: int,
) -> dict[str, Any]:
    return {
        "prompt_id": brief.prompt_id,
        "scenario": brief.scenario,
        "run_id": run_id,
        "material_claims": material_claims,
        "grounded_claims": grounded_claims,
        "hard_constraints": hard_constraints,
        "constraints_satisfied": constraints_satisfied,
        "latency_ms": latency_ms,
        "ranked_ids": ranked_ids,
        "qloo_calls": 1,
        "failure_injected": failure_injected,
        "fabricated_claims": fabricated_claims,
    }
