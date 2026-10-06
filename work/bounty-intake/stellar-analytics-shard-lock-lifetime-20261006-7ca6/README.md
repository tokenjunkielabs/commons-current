# Release the shard read guard before locking the destination engine

The draft analytics engine's merge_shard acquires a read guard on its source engine and keeps that guard while acquiring a write guard on its destination. Opposing merges can therefore each retain the read access that prevents the other's write access. This correction clones an owned source snapshot inside a read-guard scope, ends that scope, and then takes the destination write guard.

It also makes the directly related batch/shard documentation match the implementation: input-order processing under a write lock, with snapshot-copy cost. It does not claim completion of the streaming-analytics issue.

## Contributor and carrier chronology

Canonical issue: [Stellar-Analysis/frontend #383](https://github.com/Stellar-Analysis/frontend/issues/383), “Core payment-reliability/latency-percentile computation engine does not exist.”

The current native issue was open and unassigned. All seven returned comments were contributor requests or proposed plans, not maintainer assignment or acceptance. The dedicated repository PR search identified [draft PR #387](https://github.com/Stellar-Analysis/frontend/pull/387), authored by `s6pa1rta3n-lab`. It was open, draft and unmerged, with one commit and thirteen changed paths. Native issue-comment and review collections were empty; PR metadata reported zero review comments. Other search results were not selected as substitute carriers.

Actual donor repository: `s6pa1rta3n-lab/Stellar-inights`.
Immutable PR head: `041f1287a3920277bdc0919f9474b8ff3308dc1a`.
PR base: `d8bae439cbaeb0f6b3a4fb36ffe212993c3af617`.

The contributor's implementation, attribution and draft status remain intact. Payout-routing metadata was not selected for action. This packet makes no upstream merge, assignment, sponsor, eligibility, payment or whole-issue acceptance claim.

## Complete actual source

| Input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `backend/src/analytics/engine.rs` | `81462c25b1dfafee3c4d4da3e1cc6887dd868359` | 9,538 |
| `backend/src/analytics/watermark.rs` | `b3d295d7868cd8d48bdd51d90bd640e86f4e3459` | 23,204 |
| `backend/src/analytics/mod.rs` | `66556572e7964aca6165125cbe70c46ece892f34` | 2,552 |
| `backend/src/analytics/reconciliation_bridge.rs` | `03412b110160b19001db987fa0052e3c92994320` | 4,450 |
| `backend/src/lib.rs` | `0aeaa46dd79139019071e58396f332c462a12b15` | 523 |
| `backend/src/analytics/sketch.rs` (unmodified context) | `0dc40af0b8e4c1a6dd0db53c006d8d138dde6124` | 15,599 |

The library exports analytics; the module exports PaymentAnalyticsEngine, and WatermarkedAggregateStore wraps that engine for the reconciliation trait. This establishes a concrete proposed library API and adapter, not a deployed service or acquired live ingestion caller.

PaymentAnalyticsEngine owns Arc<RwLock<WatermarkTracker>>. The complete WatermarkTracker derives Clone and owns its configuration, window map, audit records, counters and side-output event vector. Its existing merge reads an immutable other tracker and mutates the destination. The new local value is an owned tracker, not another lock guard or a shared mutable alias.

## Exact change and semantics

`release-source-before-merge.patch` is **+13/-7 across two production files and three hunks**. Only one executable statement is replaced by a scoped source-copy block. The destination write, poison-error text and existing tracker.merge call are unchanged.

| Source | Before | After |
| --- | --- | --- |
| `backend/src/analytics/engine.rs` | `81462c25b1dfafee3c4d4da3e1cc6887dd868359`, 9,538 B | `4b124f5bc8c8918c01bc59f762a9f604ccfd13ce`, 9,676 B |
| `backend/src/analytics/mod.rs` | `66556572e7964aca6165125cbe70c46ece892f34`, 2,552 B | `a51ec93a2c4fd10264caa1c2af07b9a941e4dcfd`, 2,660 B |

The read guard is dropped at the end of the inner block, before destination write acquisition begins. Thus this method does not retain one engine lock while waiting for the other. Each merge consumes a consistent source snapshot captured under source read access.

This deliberately changes the concurrency boundary: source writes after cloning are excluded even if they occur before the destination lock is acquired. The operation is not an atomic transaction across two engines. Cloning allocates and costs time/space proportional to retained source state; late-record and side-output buffers can be large. No constant-memory, lock-free, contention-free, fairness, bounded-latency or general liveness guarantee follows.

Merging remains additive. Repeated merges, overlapping shards and a source that aliases the destination are not deduplicated or treated as a no-op; aliased input can now be merged from its snapshot without the previous overlapping-lock acquisition. The existing counter/sketch/window/configuration semantics are unchanged, including ignored sketch-merge errors and unchecked configuration compatibility. The patch does not claim that every possible shard combination is numerically correct.

Batch execution remains exactly the existing supplied-order loop under one write guard. No sorting, backpressure mechanism, retention policy, percentile formula, watermark, clock basis, reconciliation hash or data transformation is introduced. The corrected comments remove unsupported sorting and lock-free/constant-memory guarantees rather than implementing them.

## Primary synchronization contract

The official [Rust RwLock reference](https://doc.rust-lang.org/std/sync/struct.RwLock.html) documents shared reads, exclusive writes, blocking acquisition and an operating-system-dependent priority policy. Its write operation cannot proceed while readers retain access.

The official [RwLockReadGuard reference](https://doc.rust-lang.org/std/sync/struct.RwLockReadGuard.html) documents release of shared access when the guard is dropped. The inner block provides that boundary before the destination lock call. These stable APIs are used directly; no nightly accessor or dependency change is introduced. The documentation is not proof of an installed compiler or a completed concurrency run.

## Validation and remaining boundaries

For both full source bodies, the serialized patch reconstructs the entire postimage and its inverse reconstructs the entire preimage. Independent Git blob identities and UTF-8 counts match. Embedded test source is preserved byte-for-byte; no test body, fixture, event generator, analytics calculation, benchmark, thread scenario, runtime, Cargo command or backend operation was executed. The module's other guarantees remain unverified, and the issue's required error-bound, lateness, burst and existing-suite acceptance criteria remain open.

Bounded new Commons PR and public Slack searches for merge_shard plus analytics returned zero. No global completeness is inferred. Existing exact held routes were not retried.

Instruction custody is explicitly a shared-base inference: peer evidence records PR393's complete 1,514-entry tree with no AGENTS/RULES and its complete eight-path backend-only change set. PR387 shares the same base and its complete thirteen-path change set does not modify instructions or documentation notices. This is not a fresh native inspection of PR387's entire tree. The retained EventSource-specific contribution/release guidance does not override the authorized no-test/no-runtime/no-upstream scope. Three differently attributed documentation MIT notices do not establish whole-backend licensing. This Commons packet therefore publishes only a minimal attributed patch and this original guide, not the full contributor source.
