# Gemma 4 paper IGRB retrievers

This packet implements the retrieval-policy slice of the **Issue-to-Graph
Retrieval Benchmark (IGRB)** for the Gemma 4 Developer Agent paper track. It is
dependency-free Python and exposes lexical, graph-expansion, and hybrid
reciprocal-rank-fusion policies through one fixed-symbol-budget interface.

The implementation is deliberately separated from reference-patch labels.
Reference patches are evaluation gold only: freeze a retrieval receipt first,
then score it in the separate evaluator. Never place reference fixes in the
query, graph index, prompt, or same-task training data.

## Index contract

```json
{
  "nodes": [
    {"id": "module:symbol", "name": "symbol", "text": "public source text", "source_chars": 123}
  ],
  "edges": [
    {"source": "module:a", "target": "module:b", "relation": "calls"}
  ]
}
```

Node IDs are unique. Edge endpoints must exist. The graph policy treats allowed
relations as undirected navigation evidence, starts from the same lexical seeds,
and applies a deterministic hop decay. The hybrid policy fuses the complete
lexical and graph rankings using reciprocal-rank fusion. All ties break by node
ID, and the receipt binds the query, index, configuration, returned symbols,
candidate-character budget, and a stable receipt hash.

## Run

```bash
python retrievers.py \
  --index graph.json \
  --query "request authorization failure" \
  --method hybrid \
  --budget-k 20 \
  --seed-count 5 \
  --hops 2 \
  --relation calls \
  --relation imports \
  --output receipt.json
```

Focused checks:

```bash
python -m unittest -v test_retrievers.py
python -m py_compile retrievers.py test_retrievers.py
```

The bundled checks use small synthetic graphs only. They establish deterministic
ranking, budget enforcement, relation filtering, cycle handling, receipt
stability, and fail-closed validation. They do **not** establish retrieval gains
on the official 129-task public set, Gemma agent performance, paper eligibility,
Kaggle submission, or prize entitlement.

## Next evidence gate

Run lexical, graph, and hybrid policies on the same frozen repository-stratified
split of the official public tasks. Report Recall@5/10/20, MRR, nDCG, gold-file
recall, candidate characters, and latency from receipts. Promote a graph-aware
policy only if it improves recall at equal evidence budget or reduces evidence
budget at equal recall; a clean negative result is valid.
