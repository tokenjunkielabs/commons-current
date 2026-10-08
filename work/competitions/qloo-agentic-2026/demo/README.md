# Qloo planner offline demo

This is a deterministic local entrypoint over the existing Qloo adapter and
planner. It exercises launch, product-adjacency, and travel briefs with bundled
fixture evidence, so reviewers can inspect hard-constraint filtering, ranking,
fail-closed behavior, and benchmark receipt output without an API key.

From `work/competitions/qloo-agentic-2026`:

```bash
python demo/qloo_demo.py --scenario launch --run-id review-001
python demo/qloo_demo.py --scenario adjacency --run-id review-002
python demo/qloo_demo.py --scenario travel --run-id review-003
```

Failure paths are explicit and return a non-zero exit status:

```bash
python demo/qloo_demo.py --scenario launch --inject empty
python demo/qloo_demo.py --scenario travel --inject transport
```

Focused validation:

```bash
PYTHONPATH=demo python -m unittest demo/test_qloo_demo.py
```

The fixtures are synthetic and the entrypoint never calls the live Qloo API.
It is a review/readiness artifact, not hosted deployment, live-key validation,
competition submission, leaderboard evidence, or a claim about real Qloo
recommendation quality. A real API key, official endpoint verification, and an
authorized entrant's hosting/submission actions remain separate gates.

## Live command

`qloo_live.py` connects the same adapter and planner to the production Qloo
Insights endpoint, `https://api.qloo.com/v2/insights`. Supply an existing
`QLOO_API_KEY` through the environment; never put it in a command argument,
receipt, or source file. The command has no fixture fallback.

From `work/competitions/qloo-agentic-2026`, with the key already present:

```bash
python demo/qloo_live.py --scenario travel --prompt-id nyc-places-001 \
  --filter-type urn:entity:place --location "New York City" \
  --run-id live-001 --receipt-file live-receipts.jsonl
```

Use repeatable `--interest-id` arguments for resolved Qloo entity IDs, or
`--interest-tag` for Qloo tag IDs. Use IDs returned by Qloo, not names or invented
identifiers. The live command does not send free-text interest strings:
the official POST contract documents name/address objects for that parameter.
`--location` accepts a locality name. `--take` is 1–50.

Results must match the requested entity category; the adapter reads the category
from Qloo's `subtype` before the generic `type`. Optional local constraints:

- `--block-id ENTITY_ID` excludes a returned entity; repeat as needed.
- `--require 'price_level=2'` requires an exact value in entity properties.
  Dotted paths address nested properties; values are JSON. Missing/null
  requirements are unsupported. Use property names observed in real responses.
- `--prefer 'price_level=2@0.05'` adds the given non-negative weight when that
  property matches. Repeat for multiple preferences.

Every completed request prints its state, ranked evidence, and a receipt whose
latency measures the actual call and planning work. `--receipt-file` appends just
the receipt as JSONL for the existing scorer. Explicit run IDs help identify
repeats. An empty/error/no-match result never invents fallback recommendations.

Exit codes: 0 means returned candidates; 2 means invalid input or missing key
(with zero API calls); 3 means request failure, empty evidence, or no constraint
match; 4 means the request completed but saving its receipt failed (the output
still contains the receipt, so retain it without repeating the API call).
Secrets and provider error bodies are not printed.

The live code path is implemented; a successful authenticated Qloo run has not
been established in this environment. Deployment, entrant eligibility, provider
submission, and prize outcome remain separate unresolved steps. Existing
entrant ownership and reward claims are preserved.

Official contract references:
[parameters](https://github.com/qloo/docs-public/blob/d4a0eb978518f7fb404993d1509d11b21239ada6/reference/insights-api-deep-dive.md)
and [entity response](https://github.com/qloo/docs-public/blob/d4a0eb978518f7fb404993d1509d11b21239ada6/reference/basic-insights-use-case.md).

