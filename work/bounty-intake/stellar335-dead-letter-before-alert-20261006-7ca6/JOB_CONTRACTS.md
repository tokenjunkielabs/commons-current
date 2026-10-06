# Describe the job runner's handler obligations and storage scope

This continuation corrects two source documentation blocks in the existing PR403 job-runner proposal. Idempotency is a responsibility of each Job implementation. The supplied Scheduler retries calls and routes classified failures; it does not implement upserts or deduplicate calls. The supplied DeadLetterQueue stores copied entries in process memory, while AlertSink behavior belongs to the configured implementation.

The patch changes comments only. It does not add an idempotency mechanism, alter a retry, write a job, execute a sink or change the earlier queue-before-alert correction.

## Attributed donor and exact scope

Carrier: [Stellar-Analysis/frontend PR403](https://github.com/Stellar-Analysis/frontend/pull/403), authored by daniel6yi8-gif. The actual immutable donor is daniel6yi8-gif/frontend at `3566cbbd307c5fc1316477b3ef83c57b83af3eb9`, branch drips/333-334-335. The fresh metadata guard remains OPEN, unmerged and non-draft at that head, with base `482ee456369418ef82c4056718cb82d3468f762b` and eleven changed paths. Its 4553-character carrier body remains withheld.

This is a narrow documentation continuation for the supplied jobs335 modules. It neither claims nor takes ownership of the complete issue or of the contributor's combined 333/334/335 work. Root's backup333 comments and Infra's IP334 method alignment concern separate paths.

## What the complete retained code establishes

The Job trait has only name, payload and run methods. It declares no storage operation, idempotency key, completed-job registry or upsert requirement that the type system enforces. Its original comment required handlers to be idempotent but described their writes as upserts and inferred that repetition never double-applies. The new comment preserves the obligation while making the absence of trait enforcement explicit.

Scheduler::run calls job.run inside the configured attempt loop. A normal success returns Succeeded. Failures are recorded; a terminal classification leads to quarantine, and a retryable classification permits another attempt below the ceiling with the existing blocking backoff. Exhaustion also leads to quarantine. Nothing in that complete method inspects or deduplicates the handler's effects.

This source evidence supports a boundary statement about the supplied scheduler and trait. It does not establish whether every concrete or external Job implementation is safe or unsafe to repeat. In particular, the module references backfill, but that implementation is not among the eleven transferred PR403 added paths and was not acquired for this work.

DeadLetterQueue owns a Mutex<Vec<DeadLetter>>. Its quarantine method builds an entry, clones it into that vector and delegates notification to an AlertSink. RecordingAlertSink separately owns its own in-memory vector. The changed module comment describes the queue's actual memory storage and keeps external sink behavior separate. It does not generalize the recording sink's behavior to every possible AlertSink or promise durable retention, restart recovery or alert delivery.

## New source documentation

The module introduction now identifies handler-provided idempotency and in-memory quarantine. Its paragraph says that handlers must make repetition safe, that the scheduler does not enforce upserts or deduplicate calls, and that classifications select retries or quarantine. The Job trait comment likewise states the responsibility, including after partial failure, without presenting a storage mechanism as already enforced.

All imports, exports, signatures, structures, branches, calls, loops, locks, return values and error classifications remain byte-for-byte unchanged. No executable implementation, test or fixture is added.

| Source path | Original Git blob / UTF-8 bytes | Proposed Git blob / UTF-8 bytes |
|---|---|---|
| backend/jobs/mod.rs | `49e24f156ffc7a70953f258297908404fd50fad7` / 619 | `086faabf9a89654bfc41b3ae1ab798f764b8c1db` / 725 |
| backend/jobs/scheduler.rs | `dedcd602a8fab9aa32884a01b11f1223d57a50ec` / 2974 | `bb60da9bf89fbc94f2b023e3218fad79e6b6f1cb` / 2998 |

The complete serialized patch is 1537 UTF-8 bytes, Git blob `674d063b0fa5488f8eae85e7db0325ab08bc084a`: two hunks, twenty-four complete rows, +8/-6 documentation lines. Each segment applies forward to its exact postimage and inversely to its exact preimage. Removing only Rust documentation-comment lines from the before/after inputs leaves all remaining bytes equal.

## Preserved earlier ordering packet

Commons #32101 published store-before-alert.patch, its original README and three complete upstream notices in this same directory. That source correction remains separate and exact: backend/jobs/dead_letter.rs postimage `bebf0e1f2ac23357a0ba56ff6810ed01713c7075`, 2995 UTF-8 bytes. No new patch hunk touches that file.

Its queue insertion precedes the external alert callback, with the statement-scoped guard released first. Its documented panic propagation, volatile memory and lack of a successful Outcome guarantee still apply. This continuation changes no part of that reasoning or behavior and does not clear an earlier limitation.

The complete supporting job sources were acquired and checked for #32101, then retained for this new comment correction. They were not reacquired or executed. The error module remains `a789af804fd178241024edaaf774f8d5d9aedb60`, 1865 bytes. The original dead-letter module was `beb0aa6dfac9eb45588db4c5c8ec324697bea623`, 2995 bytes.

## Integration and attribution limits

The complete eleven-path PR403 map adds no Cargo manifest or module registration. The previously transferred complete base tree has no backend root. Those observations and the unresolved backfill reference prevent treating these supplied modules as an established mounted or built backend. This packet makes no integration, compiler, deployment, runtime, security, durable queue or whole335 acceptance claim.

Original contributors retain credit. Existing notices are preserved without rewriting their line endings:

| Existing notice | Git blob | UTF-8 bytes |
|---|---|---:|
| upstream-licence-mclaughlin.md | `57740b9d4d86aedf5d518f2f363d5cf192c54127` | 1104 |
| upstream-license-menke-laguna.md | `af5411fa243cfcf2b61c79d081dbb6204e956041` | 1111 |
| upstream-license-de-wet.md | `4a766e268772888af5df56c3f6c608f68558b789` | 1080 |

Preserving those complete notices is not a backend-wide licensing conclusion. No upstream repository or contributor PR is edited.

## Verification and publication

The newly issued dedicated Commons PR query for PR403, jobs and idempotency returned no entries. Root retained no exact prior comment correction in these paths. These bounded observations are not a global absence or assignment claim.

Validation consists of complete retained source inspection, the actual trait/scheduler/queue relationships, exact non-documentation-byte preservation and full serialized forward/inverse checks. No Rust code, scheduler, job, callback, mutex, thread, timer, fixture, test or compiler was executed. No external behavior or unacquired implementation was inferred from a title or comment.

Publication adds only describe-job-contracts.patch and this JOB_CONTRACTS.md to the existing Commons directory. Both complete immutable files, native and independent Git identities, exact added paths and final PR/tree/parent metadata are checked. The main-equality alias is used only when a separately observed main equals the verified merge/readback ref; otherwise both artifacts are read fully at one observed immutable main, without chasing later changes. Prior exact holds, including #32074's unrelated final-files metadata gap, remain unchanged.
