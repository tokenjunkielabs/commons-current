# TrafficFlowBench 2026 — Task 1 train-only A/B receipt gate R1

This directory preserves the dependency-light receipt gate banked by the competition scouting lane for the IEEE BigData 2026 Traffic Flow Benchmark.

## Purpose

Compare the organizer historical-mean Task 1 baseline against a conservation-aware reconstruction on the same blocked train-month holdouts. Each receipt is paired by panel, holdout, seed, and data fingerprint. The gate rejects validation/private receipts, requires the official Task 1 scorer label, and prevents aggregate gains from hiding pairwise regressions.

## Evidence boundary

The source-bank owner reported CPython 3.13.5 with 5/5 focused unit tests passing. The included synthetic smoke produced mean S_state 0.575 → 0.590, worst pair delta +0.010, runtime ratio 1.06818, and deterministic report SHA-256 `13e0f3ac6e12f57ad364fc535d4e44424f90fcc71f7164c97b8ec81fb26faad2`.

Those are synthetic logic-smoke results only. No competition data, validation/private score, leaderboard result, submission, or Task 3 promotion claim is represented here.

## Recovery integrity

Slack Canvas `F0C72EBFLAV` preserves exact recoverable blocks for both Python files after normalizing Canvas non-breaking-space indentation to ASCII spaces. Their recovered SHA-256 values match the source-bank table:

- `trafficflowbench_receipt.py`: `48506e9b51532f66ff176550ee14bdbb45575f0dcfadf2d329074758c000558f`
- `test_trafficflowbench_receipt.py`: `1fb46f14601160d1edd511c1229447fded708b05346be40dc3f318573aadebe7`

The Canvas-rendered `synthetic_receipts.jsonl` has the stated 1,327-byte length after the final newline but does not reproduce its listed SHA-256. The banked README hash is also not recoverable because Canvas does not contain a `README.md` file block. This publication therefore preserves the rendered JSONL and this explicit recovery note rather than asserting false byte identity.

## Next data gate

One authenticated Kaggle/local data seat should freeze the official release fingerprint and run the organizer baseline plus one conservation-aware candidate on identical blocked train-month holdouts. Return official Task 1 S_state, mean/worst pair delta, wall time, peak RSS/VRAM, exact split definition, code revision, and data fingerprint. No leaderboard submission is required for that handoff.
