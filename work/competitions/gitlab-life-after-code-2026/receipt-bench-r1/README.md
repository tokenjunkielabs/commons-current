# Life After Code — Post-code autonomy receipt benchmark R1

A deterministic benchmark floor for GitLab's **Life After Code** hackathon. It scores evidence emitted by an eventual GitLab Duo agent/flow across the post-code lifecycle instead of treating a successful demo as proof of safe autonomy.

## Metrics

- passed-stage coverage across review, test, security, compliance, deploy, observe;
- evidence completeness for passed stages;
- human-intervention count and intervention rate;
- end-to-end latency;
- unsafe production promotion when a required gate is missing, failed, or unevidenced.

## Run

```bash
python -m py_compile score_lifecycle.py tests/test_score_lifecycle.py
python -m unittest discover -s tests -v
python score_lifecycle.py fixtures/receipts.jsonl
```

## Evidence boundary

The included fixtures are synthetic lifecycle receipts. They validate scoring semantics only. They do **not** prove GitLab Duo execution, GitLab onboarding, deployment, or competition performance.

The next integration gate is to have real GitLab Duo Agent Platform agents/flows emit this receipt shape from visible pipeline/deployment evidence, then compare Assisted, Supervised, and Hands-off runs on the same workload.
