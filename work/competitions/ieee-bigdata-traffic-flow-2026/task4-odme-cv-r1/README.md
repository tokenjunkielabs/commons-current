# TrafficFlowBench Task 4 ODME CV frontier

Performance R&D for **2026 IEEE Big Data TrafficFlowBench — Task 4 (ODME)**,
bound to the official public repository at
`jacky850/trafficflowbench-public@c88cddf533bbf0afa4ff1fc6c031d760a08e7a31`.

## Why this exists

The official Task 4 baseline solves non-negative least squares with a uniform
weak-prior penalty at `lambda = 0.05`:

`min ||A f - c||^2 + lambda ||f - b||^2`, with `f >= 0`.

That is a strong baseline, but Task 4 is underdetermined: not every path is
equally constrained by measured links. This frontier adds one bounded
hypothesis without changing the competition contract:

> Pull weakly observed paths harder toward the released weak prior, and allow
> paths supported by more measured links to move more freely.

For a path with detector support `s`, the penalty becomes:

`lambda * ((median_support + 1) / (s + 1))^gamma * (f - b)^2`.

`gamma = 0` is exactly the official uniform-regularization shape; the shipped
grid always includes the official `lambda=.05, gamma=0` comparator.

## Performance gate

The script uses deterministic, balanced held-out **detector-link** folds. Each
candidate is fitted on one subset of released counts and evaluated on counts it
did not fit. It reports:

- mean and worst-fold held-out `S_link`;
- full-count `S_link`;
- relative L1 movement from the released weak path-flow prior;
- total-variation drift of destination-attraction shares from that prior;
- wall time;
- a Pareto flag across higher held-out link fit and lower prior/destination drift.

This is intentionally stricter than maximizing in-sample link fit.

**Important boundary:** the public repository says full Task 4 scoring is

`S_ODME = .45*S_od + .25*S_link + .15*S_dev + .15*S_attr`.

Only `S_link` is locally observable. The other terms use withheld path-flow
truth. This tool therefore does **not** invent, estimate, or claim `S_ODME`.
Prior and destination drift are guardrail diagnostics, not substitutes for
`S_dev` or `S_attr`.

## Run

Use the exact official repository checkout and released competition data:

```bash
python odme_cv_frontier.py --self-check

python odme_cv_frontier.py \
  --official-repo /path/to/trafficflowbench-public \
  --release-root /path/to/kaggle_public \
  --split train \
  --panel D12_I5_N \
  --output-dir reports/task4-odme-cv
```

Default frontier:

- `lambda`: `0.01, 0.03, 0.05, 0.1, 0.3`
- support exponent `gamma`: `0, 0.5, 1`
- four deterministic detector folds.

Drop `--panel` to evaluate all ten panels. The aggregate report first averages
within corridor families and then averages families, avoiding a large corridor
silently dominating the screen.

## Promotion rule

Do not promote a candidate from this tool merely because its held-out `S_link`
is higher. A data-bearing competition seat should require:

1. same frozen public release and train split for baseline and candidate;
2. held-out `S_link` lift that is not isolated to one corridor/fold;
3. prior and destination drift no worse than the chosen risk budget;
4. runtime receipt;
5. only then, a sparse leaderboard check if the authorized competition owner decides it is worth one.

This artifact performs no Kaggle login, join, rules acceptance, submission, or
leaderboard tuning.
