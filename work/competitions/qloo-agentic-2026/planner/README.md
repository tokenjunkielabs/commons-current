# TasteBench deterministic planner

This planner is the bounded decision layer between the existing Qloo adapter
and benchmark scorer. It supports the launch, product-adjacency, and travel
scenario families without inventing recommendations when Qloo evidence is
empty or unavailable.

## Behavior

1. PlanningBrief carries Qloo signals, hard constraints, and optional soft
   property preferences.
2. plan() calls the existing narrow adapter once.
3. Entity type, blocked-ID, and required-property constraints filter candidates
   before preferences are scored.
4. Remaining entities rank by affinity plus explicit preference weights, with
   entity ID as a deterministic tie break.
5. Empty, no-match, and adapter-error paths return no candidates and zero
   fabricated claims.
6. Every outcome emits the required fields consumed by score_receipts.py.

The planner does not contain a generic or model-generated fallback. A Qloo API
key and real endpoint verification remain required before any live benchmark or
public demo claim.

## Focused check

From work/competitions/qloo-agentic-2026:

    PYTHONPATH=adapter:planner python -m unittest planner/test_qloo_planner.py

The focused tests cover constraint-before-preference ordering, deterministic
ties, empty evidence, transport failure, receipt compatibility, and three
stable repeats.
