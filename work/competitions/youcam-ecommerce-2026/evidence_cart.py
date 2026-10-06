#!/usr/bin/env python3
"""Evidence Cart: a deterministic, provider-injectable commerce decision core.

The provider boundary intentionally does not model an undocumented live YouCam API.
Fixture mode exercises the same normalization and ranking path without credentials.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
import time
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence


class Provider(Protocol):
    def analyze(self, image_ref: str) -> Mapping[str, Any]: ...


class ProviderFailure(RuntimeError):
    """A typed provider failure safe to expose to the application layer."""


@dataclass(frozen=True)
class Concern:
    name: str
    confidence: float


@dataclass(frozen=True)
class Observation:
    face_detected: bool
    quality: float
    concerns: tuple[Concern, ...]


@dataclass(frozen=True)
class EvidenceCard:
    item_id: str
    name: str
    score: float
    matched_concerns: tuple[str, ...]
    why: str


@dataclass(frozen=True)
class Decision:
    status: str
    recommendations: tuple[EvidenceCard, ...] = ()
    reason: str = ""
    error_class: str = ""


def _unit_interval(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be numeric")
    value = float(value)
    if not math.isfinite(value) or not 0.0 <= value <= 1.0:
        raise ValueError(f"{field} must be finite and between 0 and 1")
    return value


def normalize_observation(raw: Mapping[str, Any]) -> Observation:
    """Validate a provider-neutral observation without retaining the input image."""
    if not isinstance(raw.get("face_detected"), bool):
        raise ValueError("face_detected must be boolean")
    quality = _unit_interval(raw.get("quality"), "quality")
    raw_concerns = raw.get("concerns")
    if not isinstance(raw_concerns, list):
        raise ValueError("concerns must be a list")

    concerns: list[Concern] = []
    seen: set[str] = set()
    for index, item in enumerate(raw_concerns):
        if not isinstance(item, Mapping):
            raise ValueError(f"concerns[{index}] must be an object")
        name = item.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"concerns[{index}].name must be non-empty")
        normalized_name = name.strip().lower()
        if normalized_name in seen:
            raise ValueError(f"duplicate concern: {normalized_name}")
        seen.add(normalized_name)
        concerns.append(
            Concern(normalized_name, _unit_interval(item.get("confidence"), f"concerns[{index}].confidence"))
        )
    return Observation(raw["face_detected"], quality, tuple(concerns))


def rank_catalog(
    observation: Observation,
    catalog: Sequence[Mapping[str, Any]],
    *,
    min_quality: float = 0.60,
    min_confidence: float = 0.65,
    limit: int = 3,
) -> Decision:
    """Return evidence-ranked commerce suggestions or an explicit no-result state."""
    if not observation.face_detected:
        return Decision("weak_evidence", reason="no_face")
    if observation.quality < min_quality:
        return Decision("weak_evidence", reason="low_quality")

    supported = {c.name: c.confidence for c in observation.concerns if c.confidence >= min_confidence}
    if not supported:
        return Decision("weak_evidence", reason="low_confidence")

    cards: list[EvidenceCard] = []
    for item in catalog:
        item_id = item.get("id")
        name = item.get("name")
        targets = item.get("supports")
        if not isinstance(item_id, str) or not isinstance(name, str) or not isinstance(targets, list):
            continue
        matched = tuple(sorted({str(target).strip().lower() for target in targets} & supported.keys()))
        if not matched:
            continue
        score = round(sum(supported[key] for key in matched), 6)
        cards.append(
            EvidenceCard(
                item_id=item_id,
                name=name,
                score=score,
                matched_concerns=matched,
                why="Matched observed concern(s): " + ", ".join(matched),
            )
        )

    if not cards:
        return Decision("zero_match", reason="catalog_has_no_supported_match")
    cards.sort(key=lambda card: (-card.score, card.item_id))
    return Decision("ok", tuple(cards[:limit]))


def decide(provider: Provider, image_ref: str, catalog: Sequence[Mapping[str, Any]]) -> Decision:
    try:
        raw = provider.analyze(image_ref)
        observation = normalize_observation(raw)
    except (ProviderFailure, TimeoutError) as exc:
        return Decision("provider_error", reason="analysis_unavailable", error_class=type(exc).__name__)
    except (TypeError, ValueError, KeyError):
        return Decision("provider_error", reason="invalid_provider_response", error_class="InvalidResponse")
    return rank_catalog(observation, catalog)


class FixtureProvider:
    """Offline provider used for tests, benchmark receipts, and demo rehearsal."""

    def __init__(self, cases: Mapping[str, Mapping[str, Any]]) -> None:
        self._cases = cases

    def analyze(self, image_ref: str) -> Mapping[str, Any]:
        case = self._cases.get(image_ref)
        if case is None:
            raise ProviderFailure("fixture not found")
        injected_error = case.get("error")
        if injected_error:
            if injected_error == "timeout":
                raise TimeoutError("injected fixture timeout")
            raise ProviderFailure(str(injected_error))
        observation = case.get("observation")
        if not isinstance(observation, Mapping):
            raise ProviderFailure("fixture observation missing")
        return observation


def percentile(values: Sequence[float], quantile: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = max(0, math.ceil(quantile * len(ordered)) - 1)
    return ordered[index]


def benchmark(
    provider: Provider,
    case_ids: Sequence[str],
    catalog: Sequence[Mapping[str, Any]],
    *,
    repeats: int = 3,
) -> dict[str, Any]:
    """Run the offline decision path and emit a public-safe evidence receipt."""
    decisions: list[Decision] = []
    elapsed_ms: list[float] = []
    deterministic = True
    for case_id in case_ids:
        fingerprints: list[str] = []
        first: Decision | None = None
        for _ in range(repeats):
            started = time.perf_counter()
            current = decide(provider, case_id, catalog)
            elapsed_ms.append((time.perf_counter() - started) * 1000.0)
            fingerprints.append(json.dumps(asdict(current), sort_keys=True))
            first = first or current
        deterministic = deterministic and len(set(fingerprints)) == 1
        decisions.append(first or Decision("provider_error", reason="missing_run"))

    counts = Counter(decision.status for decision in decisions)
    ok = counts["ok"]
    grounded = sum(bool(decision.recommendations) for decision in decisions if decision.status == "ok")
    return {
        "schema_version": "evidence-cart-benchmark/v1",
        "mode": "offline_fixture",
        "case_count": len(case_ids),
        "repeat_count": repeats,
        "status_counts": dict(sorted(counts.items())),
        "success_rate": round(ok / len(case_ids), 6) if case_ids else 0.0,
        "grounding_rate": round(grounded / ok, 6) if ok else 0.0,
        "deterministic": deterministic,
        "latency_ms": {
            "median": round(statistics.median(elapsed_ms), 6) if elapsed_ms else 0.0,
            "p95": round(percentile(elapsed_ms, 0.95), 6),
        },
        "privacy": {"raw_image_in_receipt": False, "case_ids_only": True},
    }


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the Evidence Cart offline benchmark")
    parser.add_argument("--fixtures", type=Path, required=True)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    fixture_rows = load_json(args.fixtures)
    catalog = load_json(args.catalog)
    cases = {row["case_id"]: row for row in fixture_rows}
    receipt = benchmark(FixtureProvider(cases), list(cases), catalog)
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
