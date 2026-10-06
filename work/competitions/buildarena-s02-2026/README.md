# BuildArena S02 telemetry gate

This directory contains a dependency-free analyzer for exported BuildArena telemetry. It closes the readiness gap left by the released local-only trace-gate build: the instrumentation is now durable, reviewable, and can produce comparable receipts once a permitted authenticated seat exports real traces.

It intentionally does **not** contain a vehicle, controller, MCP command sequence, tuned mission parameters, Kaggle integration, or submission automation.

## Receipt contract

Each JSON/NDJSON sample may include:

- `orbit_index` and `radius` for the hard gate;
- `orbit_valid` when the simulator explicitly marks an orbit invalid;
- `payload_recovered`, `landed`, and `landing_speed` for recovery proxies;
- `machine_integrity` and `fuel` only when the telemetry actually exposes them.

The gate passes only when three distinct non-invalid orbits each have an observed radius strictly greater than 1100. Missing optional fields are omitted and never imputed. Malformed/non-finite values fail closed.

Run focused checks:

```bash
python -m unittest -v test_trace_gate.py
```

Rank one or more exported traces:

```bash
python trace_gate.py run-a.ndjson run-b.json > receipt.json
```

## Evidence boundary

The focused tests use synthetic telemetry to verify parser, hard-gate, recovery, and comparison behavior. They are not evidence of a real simulator run, successful mission, valid Kaggle submission, leaderboard score, or prize eligibility.

Public intake recorded a **$3,000 advertised prize pool** and a **November 14, 2026 AOE deadline**. Proposed, promised, funded, awarded, invoiced, and received amounts for this artifact are all **$0**. The next useful action is one authenticated competition seat exporting a real ordinary run, then generating a receipt with this analyzer before any submission decision.
