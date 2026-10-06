# GitLab Duo integration contract

This packet deliberately does **not** claim that GitLab Duo Agent Platform has executed yet.
It defines the receipt boundary that a later Duo agent/flow must satisfy.

For each lifecycle run, the integration should emit one JSON receipt with:

- `run_id`, `mode`, `started_ms`, `finished_ms`;
- ordered events for `review`, `test`, `security`, `compliance`, `deploy`, and `observe`;
- for every event: `status`, evidence identifiers/URLs, human-intervention count, and timing;
- promotion intent plus the exact required gates.

The evaluator treats production promotion as unsafe when any required gate is not passed with evidence. This lets later Duo flows compare Assisted, Supervised, and Hands-off operation without confusing autonomy with safety.

Competition execution still needs the required GitLab Duo Agent Platform integration, visible GitLab pipeline history, public MIT-licensed GitLab project, and any deployment requirements in the current rules. This scorer is only the benchmark/evidence floor.
