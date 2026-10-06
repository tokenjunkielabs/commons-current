# Gemma 4 Developer Agent — offline budget benchmark

Consumes JSONL receipts from already-executed dev tasks and compares the fixed
`5m80` and `7m100` budget policies on an identical task slice.

Selection is observed PASS count first. Ties break by lower no-patch wall waste,
then lower total wall time, then fewer tool calls.

The scorer fails closed when:
- either policy is missing a task present in the other policy,
- a receipt duplicates a repo/task/policy key,
- booleans or numeric fields have the wrong JSON type,
- metrics are non-finite or internally inconsistent,
- a receipt exceeds its policy wall-clock or tool-call budget.

It does not run Gemma, submit to Kaggle, or predict hidden-task outcomes.

Required receipt fields: repo, task_id, policy, passed, patch_produced,
wall_seconds, tool_calls, first_edit_seconds, test_seconds, diff_lines.

Example:
python budget_benchmark.py synthetic_ab.jsonl > report.json

Use the same fixed dev slice for each policy. Do not compare policies on
different task sets. The global-cap section is an observed-runtime fit simulation
under deterministic repo/task ordering, not a reconstruction of unknown live
scheduling.
