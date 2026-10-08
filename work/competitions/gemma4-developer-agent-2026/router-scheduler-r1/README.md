# Offline task router and budget scheduler

G4-B implementation for the existing Gemma 4 Developer Agent intake. This module
makes a usable scheduling decision from a runner snapshot; it does not execute
commands, call models, produce patches, or change the accepted A/B scorer.

## Run and integrate

Use Python 3.10+ with no third-party dependencies:

```sh
python scheduler.py runner_snapshot.json
```

Use `-` to read the JSON snapshot from stdin, or import `decide(snapshot)`.
The CLI returns a decision as JSON, exits 0 on success, and emits a concise error
to stderr with exit 2 for malformed input. All decisions are deterministic and
include hashes of their input, policy, and complete decision.

The runner supplies an authoritative snapshot:

- `budget_seconds`: optional positive total allowance, at most 43,200 (default).
- `elapsed_seconds`: total budget-charged time, including all attempts and runner
  overhead. This must be at least the sum of task `charged_seconds`.
- `quantum_seconds`: optional maximum allocation between scheduler calls (default 60).
- `tasks`: ordered complete task history. Each row contains `repo`, `task_id`,
  `text`, `status` (pending, active, done, abandoned), `charged_seconds`, and
  `tool_calls`. Counters default to zero. There can be one active task, and
  duplicate repo/task identities are rejected. Pending rows cannot contain prior work.
- Optional row `shape`: bug, regression, behavior, navigation, or build. Freeze
  the chosen shape at first admission so later progress text cannot reset limits.
- Optional row `gain_estimate`: `probability` in [0,1], positive `seconds`, and
  nonempty `source`. This is the caller's estimate of **additional conditional**
  solve probability from the current state over that many additional seconds,
  not the task's original total success probability.

Output `action` is start, continue, switch, or stop. On switch/stop, `stop_task`
identifies the old task. `allocation` gives the selected identity, policy, maximum
seconds, remaining task seconds, and maximum additional tool calls. The runner
must enforce both limits, settle actual elapsed time/calls (including overhead),
mark stopped work abandoned and completed work done, and obtain a new decision
before another allocation. This pure module never advances counters on its own.
Keep the full history or preserve its charged time in the global counter.

The runner's charged-time definition must follow the final organizer contract.
The existing intake specifies that organizer validation time is excluded. Do not
silently subtract internal agent/tool time merely because it performs validation.

## Policy

The fixed initial policy maps bug/regression/build to the existing 5m80 limits
(300 seconds, 80 tool calls), and behavior/navigation to 7m100 (420 seconds,
100 calls). The lexical classifier prioritizes build cues, regression cues,
navigation cues, behavior cues, then falls back to bug; explicit shapes override it.
These are transparent engineering defaults awaiting G4-A calibration.

When every runnable task has an explicit gain estimate, choose the highest
conditional probability gain per second. A gain whose time estimate cannot fit
the remaining task or global budget is excluded. Equal rates keep the active
task, then preserve input queue order. If every feasible gain is zero, stop.
If any runnable task lacks an estimate, keep a viable active task or select the
first pending task; no synthetic success probability is substituted. Allocation
is always bounded by the decision quantum, task headroom, global headroom, and
the selected estimate duration when present.

This is a greedy online allocation policy, not a proof of an optimal schedule.
It makes no pass-rate prediction and reads no held-out outcomes. Existing observed
dev attempts should still be evaluated by `../budget-benchmark-r1/budget_benchmark.py`.
Do not feed hidden outcomes or the current task's eventual result into estimates.
Promote an estimate source only using the authorized frozen dev split.

## Custody and scope

Completes the G4-B work item from the existing build packet and October 6 TAKE;
the original intake and budget-scorer authorship remains intact. This delivery
does not launch competition runs, train models, join Kaggle, accept terms, spend
funds, or submit entries. The preparation and contribution rights are retained;
applicable competition award/payment decisions remain with the existing entrant
and organizer process. Settlement was not checked here.
