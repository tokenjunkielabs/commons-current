# Keep deferred fanout cleanup bound to the failed connection

The existing draft implementation snapshots `Arc<Connection>` handles, sends through those handles, and later removes failures by string ID in a detached task. Both registry registration methods can replace an entry under that same ID. Between the snapshot and cleanup, an old failed connection can therefore be replaced, and the old cleanup can delete the replacement.

This two-file source continuation keeps the original failed Arc through deferred cleanup. A new crate-visible registry method compares the current entry with that exact allocation and removes it only when they still match. Comparison and removal occur under the same registry write lock.

## Existing issue, draft and source boundary

The public issue is [Stellar-Analysis/frontend #379](https://github.com/Stellar-Analysis/frontend/issues/379), concerning realtime fanout blocking. The existing whole-scope implementation is [draft PR #393](https://github.com/Stellar-Analysis/frontend/pull/393), authored by **s6pa1rta3n-lab**. Its exact acquired head is:

`2611c78bfe97abe6f23302078097ec454a3d5007`

The head repository is `s6pa1rta3n-lab/Stellar-inights`, branch `fix-issue-379`; the PR base was `d8bae439cbaeb0f6b3a4fb36ffe212993c3af617`. PR #393 was open and draft at acquisition. The same author's earlier [PR #385](https://github.com/Stellar-Analysis/frontend/pull/385) was closed, unmerged and draft at the same head. These are bounded native metadata observations.

This packet preserves that author's work and supplies only an adjacent residual correction against the draft head. It does not replace the whole-scope draft, close issue #379, claim its full acceptance criteria, or submit anything upstream. The draft author's assertions about performance, FIFO and tests were read as attributed claims and were not executed or independently certified.

Canonical frontend commit `482ee456369418ef82c4056718cb82d3468f762b` has no backend root in the previously retained complete tree. Accordingly, this patch targets the exact existing draft source above; it must not be treated as applicable to that canonical tree or as an already deployed backend fix.

## Complete acquired inputs

The native blob route returned full content without a separate SHA field. Each request-bound blob identity was independently matched using the complete UTF-8 string.

| Path | Input Git blob | UTF-8 bytes | Role |
| --- | --- | ---: | --- |
| `backend/src/realtime/fanout.rs` | `8dd75e7b04f9c5d647ee9a8949bb45ce4ace2eee` | 5,825 | Snapshot, failure classification and detached cleanup |
| `backend/src/realtime/mod.rs` | `a660680768f216ca08e3904231fd4048253e86ce` | 3,352 | Registry insertion, snapshots and removal |
| `backend/src/realtime/connection.rs` | `daee350da6b94b97310bc0076dd1f7f6c8c3f88c` | 7,386 | Connection ID, send and tracker methods |
| `backend/src/realtime/policy.rs` | `263d39492ceeece22130356d14335315fb1277ea` | 15,343 | Actual overflow routine and policy contract |
| `backend/Cargo.toml` | `6064f712d523c149e8d6b0f6f92c67b98cdddda7` | 886 | Rust 2021 edition and Tokio 1 dependency declaration |

The PR's native eight-file map identifies these source blobs. Its two integration-test files and Cargo.lock were not source-acquired or run for this task. Existing inline tests arrived inside complete production files and remain byte-exact.

The native Git commit binds the head to tree `edba05f583ad7070c6770abe7816e7c952f1ba25`. Its complete recursive response contains 1,514 entries, with truncated=false. It has no AGENTS or RULES file. The acquired `docs/CONTRIBUTING.md`, blob `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` (274 bytes), explicitly concerns EventSource and asks for tests/release commands there; no EventSource change or release is made here. No tests or release commands were invoked.

## Source-supported interleaving and correction

The actual call chain is `fanout_message` or `fanout_message_with_concurrency` into `fanout_message_detailed`, then `get_all_connections`, per-connection send/classification, and detached batch cleanup. The complete registry implements both `add` and `add_connection` using map insertion that can replace an existing ID. This is the production API boundary supporting the residual; no socket session was started and no particular deployed reconnect sequence was observed.

A possible source interleaving is:

1. Fanout retains connection A from the registry snapshot.
2. The registry installs distinct connection B under A's ID.
3. The send/classification for A produces an eviction candidate.
4. The old detached ID-only batch removal removes B.

After this patch, `DeliveryResult::Evict` carries the original `Arc<Connection>`. The detached task does not look up a replacement and reinterpret it as the failed connection. It passes those original handles to `remove_batch_if_current`.

That method acquires the registry's write lock once, compares each map entry using `Arc::ptr_eq`, and removes only matching entries before releasing that same guard. An absent ID or a distinct replacement is skipped. Holding the original Arc keeps that allocation alive through comparison. There is no await between comparison and removal, and other writers cannot replace the map entry inside that critical section. The existing public ID-only `remove_batch` is unchanged for all other callers.

The helper returns the IDs it actually removed. Existing `handle_overflow` calls move after guarded removal and apply only to those returned IDs. This ordering change is deliberate: a stale candidate that was skipped does not emit the existing overflow routine's eviction log/counter updates. The acquired overflow routine only logs and updates metrics; it does not itself close a socket. No physical disconnect guarantee is added, and later logging is not an atomic snapshot of the registry.

The existing `FanoutSummary.failed_evicted` field still counts failure classifications before detached cleanup. It is not changed into an actual-removal counter, and this packet does not present it as one. Detached-task scheduling and completion remain outside the returned summary.

## Primary contracts

The [Rust standard-library Arc documentation](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.ptr_eq) defines allocation identity comparison; equal connection ID strings alone do not establish this identity. The method is documented as stable since Rust 1.17. The inspected documentation was the current standard-library page, not an installed compiler observation.

The [Tokio RwLock write documentation](https://docs.rs/tokio/latest/tokio/sync/struct.RwLock.html#method.write) specifies exclusive write access and release when its guard is dropped. The source already uses this lock API for insertion and removal. This patch relies on that existing guard to keep comparison and removal together; it does not add a lock implementation or change lock policy.

These contracts and the acquired control flow support the interleaving analysis. They are not a compiler run, deployed concurrency observation, or benchmark.

## Exact postimages and limits

| Changed path | Postimage Git blob | UTF-8 bytes | Change |
| --- | --- | ---: | --- |
| `backend/src/realtime/fanout.rs` | `8445267f41c2149da4a13716154ca84890ffbd1a` | 5,840 | +8 / -8 |
| `backend/src/realtime/mod.rs` | `e52d2869014bca627941bcf29ac4bffc4fdfe824` | 4,146 | +21 / -0 |

The patch contains +29 / -8 across these two files. The fanout input and postimage both have no final newline; the registry retains its final newline. Existing send timeouts, concurrency limit, message cloning, classification conditions, quarantine decisions, ordering behavior, registry public removal methods, policy and connection code remain unchanged. No new test or fixture is included.

Validation consisted of complete source inspection, native source/metadata acquisition, primary contract reading, exact transformation and patch reconstruction, unchanged-section comparison, and independent UTF-8/Git-blob identities. No Rust compiler, Cargo command, test, shell, executor, workflow, network socket, delivery/load benchmark, or prior publication was run or replayed. FIFO, total timeout coverage, physical eviction, tracker correctness and whole-issue completion remain unclaimed.

This is a patch-plus-guide packet. Three differently attributed license notices in the draft tree match the already preserved notices in [the earlier generator packet](../stellaranalysis-issue-generator-layout-20261006-7ca6/); no repository-wide license scope is inferred and complete upstream modules are not republished. The existing draft author and carrier remain attributed. No account, payment, contact, ownership transfer or upstream action is included.
