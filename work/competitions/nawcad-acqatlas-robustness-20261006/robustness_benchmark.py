#!/usr/bin/env python3
"""Measure AcqAtlas ranking stability under deterministic public-fixture perturbations."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import statistics
import sys
import time


ROOT = Path(__file__).resolve().parents[3]
ENGINE = ROOT / "competitions/nawcad-acqdoc-acqatlas-2026/acqatlas.py"
FIXTURE = ROOT / "competitions/nawcad-acqdoc-acqatlas-2026/fixtures/synthetic_procurements.jsonl"


def load_engine():
    spec = importlib.util.spec_from_file_location("acqatlas", ENGINE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {ENGINE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def canonical_bytes(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def transform(doc, variant: str, acqatlas):
    title, text = doc.title, doc.text
    if variant == "case-whitespace":
        title = title.swapcase()
        text = "\n\n  " + "   ".join(text.upper().split()) + "  \n"
    elif variant == "neutral-boilerplate":
        text = "The contractor shall provide services and support for the government. " + text
    elif variant == "section-reorder":
        clauses = [part.strip() for part in text.rstrip(".").split(",")]
        text = "; ".join(reversed(clauses)) + "."
    elif variant == "title-demotion":
        text = text + " " + title
        title = ""
    elif variant != "baseline":
        raise ValueError(f"unknown variant: {variant}")
    return acqatlas.Document(doc.doc_id, title, text, doc.vehicle, doc.acceptable_vehicles)


def top_vehicle_lists(analysis: dict) -> dict[str, list[str]]:
    return {
        doc_id: [item["vehicle"] for item in recommendations]
        for doc_id, recommendations in analysis["recommendations"].items()
    }


def cluster_partition(analysis: dict) -> list[list[str]]:
    return sorted(sorted(cluster["members"]) for cluster in analysis["clusters"])


def one_run(acqatlas) -> dict:
    docs = acqatlas.load_documents(FIXTURE)
    baseline_analysis = acqatlas.analyze(docs)
    baseline_lists = top_vehicle_lists(baseline_analysis)
    baseline_clusters = cluster_partition(baseline_analysis)
    variants = []
    for name in ("baseline", "case-whitespace", "neutral-boilerplate", "section-reorder", "title-demotion"):
        candidate = [transform(doc, name, acqatlas) for doc in docs]
        validation = acqatlas.validate_leave_one_out(candidate, top_k=5)
        analysis = acqatlas.analyze(candidate)
        ranked = top_vehicle_lists(analysis)
        top1_same = []
        jaccards = []
        for doc_id in sorted(baseline_lists):
            base = baseline_lists[doc_id]
            other = ranked[doc_id]
            top1_same.append(bool(base and other and base[0] == other[0]))
            union = set(base) | set(other)
            jaccards.append(len(set(base) & set(other)) / len(union) if union else 1.0)
        variants.append({
            "variant": name,
            "top1_accuracy": validation["top1_accuracy"],
            "top5_recall": validation["top5_recall"],
            "top1_rank_retention": round(sum(top1_same) / len(top1_same), 6),
            "mean_top5_set_jaccard": round(statistics.fmean(jaccards), 6),
            "cluster_partition_retained": cluster_partition(analysis) == baseline_clusters,
            "analysis_sha256": analysis["analysis_sha256"],
        })
    return {
        "schema": "acqatlas-public-robustness-v1",
        "evidence_boundary": "public synthetic fixture only; not sponsor/GFI performance",
        "document_count": len(docs),
        "engine_source_sha256": sha256(ENGINE.read_bytes()),
        "fixture_manifest_sha256": acqatlas.document_manifest_sha256(docs),
        "benchmark_source_sha256": sha256(Path(__file__).read_bytes()),
        "variants": variants,
        "network_calls": 0,
        "llm_tokens": 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    acqatlas = load_engine()
    hashes, elapsed = [], []
    result = None
    for _ in range(2):
        started = time.perf_counter()
        result = one_run(acqatlas)
        elapsed.append(round(time.perf_counter() - started, 6))
        hashes.append(sha256(canonical_bytes(result)))
    if len(set(hashes)) != 1:
        raise RuntimeError("robustness result changed across identical runs")
    receipt = dict(result or {})
    receipt.update({
        "deterministic_repeats": 2,
        "result_sha256": hashes[0],
        "runtime_seconds_each": elapsed,
    })
    rendered = canonical_bytes(receipt)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(rendered)
    print(rendered.decode(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
