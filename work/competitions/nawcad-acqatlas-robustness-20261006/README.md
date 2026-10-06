# AcqAtlas public-fixture robustness receipt

This is a measured, non-duplicate evidence layer for the engine already merged in Commons PR #14234. It does not change or copy the AcqAtlas engine.

The benchmark imports the exact current engine and its 20-document public synthetic fixture, then measures recommendation and cluster stability under four deterministic extraction-adjacent perturbations:

- case and whitespace noise;
- neutral acquisition boilerplate;
- section/clause reordering;
- moving the title into body text.

Run only the focused benchmark:

```bash
python work/competitions/nawcad-acqatlas-robustness-20261006/robustness_benchmark.py \
  --output work/competitions/nawcad-acqatlas-robustness-20261006/public-synthetic-receipt.json
```

The receipt binds the exact engine bytes, fixture manifest, and benchmark source; repeats the complete calculation twice; and records top-1 accuracy, top-5 recall, top-rank retention, top-5 set overlap, cluster-partition retention, and runtime. No network or model call is made.

## Current public-synthetic result

Two identical calculations produced stable result hash `fb27944d8dce2da94ad3f6d4d07a7a333b4a90320961b94b188efcb51bee222d` in 0.230759s and 0.281209s. All five variants retained 1.0 top-1 accuracy, 1.0 top-5 recall, the same top-ranked vehicle for every document, and a 1.0 mean top-5 set Jaccard. Case/whitespace, neutral boilerplate, and title demotion also retained the exact cluster partition. Section reordering retained vehicle rankings but changed the cluster partition, which is the concrete next GFI-side risk to measure before treating cluster membership as extraction-order robust.

## Evidence boundary

All metrics are public-synthetic engineering evidence only. They are not sponsor validation, GFI performance, registration, eligibility, submission, selection, prize, funding, award, invoice, or payment evidence. The remaining high-value gate is an authorized private GFI run and provider submission by an eligible entrant.
