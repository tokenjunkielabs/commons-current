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
