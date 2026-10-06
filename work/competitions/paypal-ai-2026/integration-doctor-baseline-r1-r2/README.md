# PayPal Integration Doctor baseline R1

This packet implements the build contract's immediate PP-A, PP-B, and PP-E experiment:

- 20 frozen, sanitized synthetic traces balanced across request-shape, authentication/configuration, webhook, idempotency, and ambiguous cases;
- a deterministic normalizer that redacts common credential-bearing fields and rejects unsupported or non-finite values;
- an evidence-bounded rule baseline that abstains on missing or conflicting evidence;
- a receipt with top-1 accuracy, false-confidence rate, per-label counts, classifier calls, and observed p50/p95 classifier latency.

Run:

```bash
python -m unittest -v test_baseline.py
python -m py_compile baseline.py test_baseline.py
python baseline.py fixtures.json --out receipt.json
```

The fixtures are synthetic plumbing evidence. Their score does not establish performance on PayPal Sandbox traces, and this packet does not diagnose or repair a real integration. A useful next step is a separately authorized Sandbox-backed manifest with preserved request/response IDs, followed by an evidence-retrieval candidate compared against this exact baseline without increasing false confidence.

No PayPal or Devpost account action, API/model call, registration, rules acceptance, submission, sponsor contact, payment mutation, or paid compute is part of this artifact.

The event advertises $12,000, $8,000, and $5,000 grand prizes, $5,000 honorable-mention categories, and sponsor prizes. Proposed, promised, verified funded to this lane, awarded, invoiced, and received are all $0.
