#!/usr/bin/env python3
"""Deterministic, dependency-free retrievers for the Gemma 4 IGRB packet.

The module deliberately has no access to reference patches.  Gold labels belong
to the evaluator, which must run only after this module has frozen its output.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_]*")
ALLOWED_METHODS = frozenset({"lexical", "graph", "hybrid"})


class RetrievalError(ValueError):
    """Raised when an index or retrieval configuration is invalid."""


@dataclass(frozen=True)
class Node:
    node_id: str
    name: str
    text: str
    source_chars: int


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    relation: str


def _tokens(value: str) -> list[str]:
    # Splitting snake/camel identifiers makes issue vocabulary less brittle while
    # retaining the complete identifier as an additional exact-match token.
    result: list[str] = []
    for raw in TOKEN_RE.findall(value):
        whole = raw.lower()
        result.append(whole)
        for part in re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", raw).replace("_", " ").split():
            token = part.lower()
            if token and token != whole:
                result.append(token)
    return result


def _canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def _sha256(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value)).hexdigest()


def load_index(payload: Mapping[str, Any]) -> tuple[dict[str, Node], list[Edge]]:
    """Validate and normalize the public graph index contract."""
    if not isinstance(payload, Mapping):
        raise RetrievalError("index must be a JSON object")
    raw_nodes = payload.get("nodes")
    raw_edges = payload.get("edges", [])
    if not isinstance(raw_nodes, list) or not raw_nodes:
        raise RetrievalError("index.nodes must be a non-empty array")
    if not isinstance(raw_edges, list):
        raise RetrievalError("index.edges must be an array")

    nodes: dict[str, Node] = {}
    for raw in raw_nodes:
        if not isinstance(raw, Mapping):
            raise RetrievalError("each node must be an object")
        node_id, name, text = raw.get("id"), raw.get("name"), raw.get("text", "")
        source_chars = raw.get("source_chars")
        if not all(isinstance(item, str) for item in (node_id, name, text)):
            raise RetrievalError("node id, name, and text must be strings")
        if not node_id or not name or node_id in nodes:
            raise RetrievalError("node ids/names must be non-empty and ids unique")
        if isinstance(source_chars, bool) or not isinstance(source_chars, int) or source_chars < 0:
            raise RetrievalError("node source_chars must be a non-negative integer")
        nodes[node_id] = Node(node_id, name, text, source_chars)

    edges: list[Edge] = []
    seen_edges: set[tuple[str, str, str]] = set()
    for raw in raw_edges:
        if not isinstance(raw, Mapping):
            raise RetrievalError("each edge must be an object")
        source, target, relation = raw.get("source"), raw.get("target"), raw.get("relation")
        if not all(isinstance(item, str) and item for item in (source, target, relation)):
            raise RetrievalError("edge source, target, and relation must be non-empty strings")
        if source not in nodes or target not in nodes:
            raise RetrievalError("every edge endpoint must name an existing node")
        key = (source, target, relation)
        if key not in seen_edges:
            edges.append(Edge(*key))
            seen_edges.add(key)
    edges.sort(key=lambda edge: (edge.source, edge.target, edge.relation))
    return nodes, edges


def lexical_ranking(query: str, nodes: Mapping[str, Node]) -> list[tuple[str, float]]:
    """Return a stable BM25-style lexical ranking over symbol nodes."""
    if not isinstance(query, str) or not query.strip():
        raise RetrievalError("query must be a non-empty string")
    query_terms = Counter(_tokens(query))
    documents = {node_id: _tokens(f"{node.node_id} {node.name} {node.text}") for node_id, node in nodes.items()}
    lengths = {node_id: max(1, len(tokens)) for node_id, tokens in documents.items()}
    average_length = sum(lengths.values()) / len(lengths)
    document_frequency = Counter(term for tokens in documents.values() for term in set(tokens))
    total_documents = len(documents)
    k1, b = 1.2, 0.75

    scored: list[tuple[str, float]] = []
    for node_id, tokens in documents.items():
        counts = Counter(tokens)
        score = 0.0
        for term, query_count in query_terms.items():
            frequency = counts.get(term, 0)
            if not frequency:
                continue
            inverse_frequency = math.log(1.0 + (total_documents - document_frequency[term] + 0.5) / (document_frequency[term] + 0.5))
            denominator = frequency + k1 * (1.0 - b + b * lengths[node_id] / average_length)
            score += query_count * inverse_frequency * (frequency * (k1 + 1.0) / denominator)
        # Exact identifier matches should beat incidental prose matches.
        name_tokens = set(_tokens(nodes[node_id].name))
        score += 0.25 * len(name_tokens.intersection(query_terms))
        scored.append((node_id, score))
    # Do not consume the fixed evidence budget with arbitrary zero-evidence
    # symbols. An empty ranking is an explicit abstention.
    return sorted((item for item in scored if item[1] > 0), key=lambda item: (-item[1], item[0]))


def graph_ranking(
    lexical: Sequence[tuple[str, float]],
    nodes: Mapping[str, Node],
    edges: Sequence[Edge],
    *,
    seed_count: int = 5,
    hops: int = 1,
    decay: float = 0.65,
    relations: Iterable[str] | None = None,
) -> list[tuple[str, float]]:
    """Expand lexical seeds through allowed structural relations."""
    if seed_count < 1 or hops < 0 or not (0.0 < decay <= 1.0):
        raise RetrievalError("seed_count >=1, hops >=0, and 0 < decay <=1 are required")
    allowed = None if relations is None else frozenset(relations)
    adjacency: dict[str, set[str]] = defaultdict(set)
    for edge in edges:
        if allowed is not None and edge.relation not in allowed:
            continue
        adjacency[edge.source].add(edge.target)
        adjacency[edge.target].add(edge.source)

    seeds = list(lexical)[: min(seed_count, len(nodes))]
    max_seed = max((score for _, score in seeds), default=1.0) or 1.0
    scores: dict[str, float] = {node_id: 0.0 for node_id in nodes}

    for seed_rank, (seed, raw_score) in enumerate(seeds, start=1):
        seed_weight = (raw_score / max_seed) if raw_score > 0 else 1.0 / seed_rank
        queue = deque([(seed, 0)])
        best_hop = {seed: 0}
        while queue:
            node_id, distance = queue.popleft()
            scores[node_id] += seed_weight * (decay ** distance)
            if distance == hops:
                continue
            for neighbor in sorted(adjacency.get(node_id, ())):
                next_distance = distance + 1
                if next_distance < best_hop.get(neighbor, hops + 1):
                    best_hop[neighbor] = next_distance
                    queue.append((neighbor, next_distance))
    return sorted((item for item in scores.items() if item[1] > 0), key=lambda item: (-item[1], item[0]))


def reciprocal_rank_fusion(
    rankings: Sequence[Sequence[tuple[str, float]]], *, rrf_k: int = 60
) -> list[tuple[str, float]]:
    if rrf_k < 1 or not rankings:
        raise RetrievalError("rrf_k must be positive and at least one ranking is required")
    scores: dict[str, float] = defaultdict(float)
    for ranking in rankings:
        for rank, (node_id, _score) in enumerate(ranking, start=1):
            scores[node_id] += 1.0 / (rrf_k + rank)
    return sorted(scores.items(), key=lambda item: (-item[1], item[0]))


def retrieve(
    payload: Mapping[str, Any],
    query: str,
    *,
    method: str,
    budget_k: int,
    seed_count: int = 5,
    hops: int = 1,
    decay: float = 0.65,
    relations: Iterable[str] | None = None,
    rrf_k: int = 60,
) -> dict[str, Any]:
    """Run one frozen retrieval policy and emit a reproducible decision receipt."""
    if method not in ALLOWED_METHODS:
        raise RetrievalError(f"method must be one of {sorted(ALLOWED_METHODS)}")
    if isinstance(budget_k, bool) or not isinstance(budget_k, int) or budget_k < 1:
        raise RetrievalError("budget_k must be a positive integer")
    nodes, edges = load_index(payload)
    lexical = lexical_ranking(query, nodes)
    graph = graph_ranking(
        lexical,
        nodes,
        edges,
        seed_count=seed_count,
        hops=hops,
        decay=decay,
        relations=relations,
    )
    ranking = lexical if method == "lexical" else graph
    if method == "hybrid":
        ranking = reciprocal_rank_fusion((lexical, graph), rrf_k=rrf_k)

    chosen = ranking[: min(budget_k, len(ranking))]
    relation_list = None if relations is None else sorted(set(relations))
    config = {
        "method": method,
        "budget_k": budget_k,
        "seed_count": seed_count,
        "hops": hops,
        "decay": decay,
        "relations": relation_list,
        "rrf_k": rrf_k,
    }
    receipt = {
        "schema_version": 1,
        "query_sha256": hashlib.sha256(query.encode("utf-8")).hexdigest(),
        "index_sha256": _sha256(payload),
        "config": config,
        "retrieved_symbols": [node_id for node_id, _ in chosen],
        "scores": [round(float(score), 12) for _, score in chosen],
        "candidate_chars": sum(nodes[node_id].source_chars for node_id, _ in chosen),
        "node_count": len(nodes),
        "edge_count": len(edges),
    }
    receipt["receipt_sha256"] = _sha256(receipt)
    return receipt


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a deterministic IGRB retriever")
    parser.add_argument("--index", required=True, help="JSON graph index")
    parser.add_argument("--query", required=True)
    parser.add_argument("--method", required=True, choices=sorted(ALLOWED_METHODS))
    parser.add_argument("--budget-k", type=int, required=True)
    parser.add_argument("--seed-count", type=int, default=5)
    parser.add_argument("--hops", type=int, default=1)
    parser.add_argument("--decay", type=float, default=0.65)
    parser.add_argument("--relation", action="append", dest="relations")
    parser.add_argument("--rrf-k", type=int, default=60)
    parser.add_argument("--output")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    try:
        args = _parser().parse_args(argv)
        payload = json.loads(Path(args.index).read_text(encoding="utf-8"))
        receipt = retrieve(
            payload,
            args.query,
            method=args.method,
            budget_k=args.budget_k,
            seed_count=args.seed_count,
            hops=args.hops,
            decay=args.decay,
            relations=args.relations,
            rrf_k=args.rrf_k,
        )
        rendered = json.dumps(receipt, sort_keys=True, indent=2) + "\n"
        if args.output:
            Path(args.output).write_text(rendered, encoding="utf-8")
        else:
            print(rendered, end="")
        return 0
    except (OSError, json.JSONDecodeError, RetrievalError) as exc:
        print(f"IGRB retrieval error: {exc}", file=__import__("sys").stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
