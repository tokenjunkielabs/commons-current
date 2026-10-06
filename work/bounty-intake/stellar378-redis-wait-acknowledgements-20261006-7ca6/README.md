# Enforce configured Redis acquisition acknowledgements

## Deliverable and scope

This is an attributed source correction for the Redis store proposed in [Stellar-Analysis/frontend PR386](https://github.com/Stellar-Analysis/frontend/pull/386), associated with [issue378](https://github.com/Stellar-Analysis/frontend/issues/378). Apply `require-wait-acknowledgements.patch` to the exact contributor head below. The patch changes one production source file, with +11/-8 lines across two hunks. This Commons packet does not merge into the contributor branch or upstream repository.

The donor PR remains open and draft, unmerged, authored by **s6pa1rta3n-lab**. Its implementation and authorship remain distinct from this small follow-up. The PR's broad production, acceptance and testing statements are author claims, not validation established here. No whole-issue completion, upstream acceptance, deployment or reward is claimed.

## Concrete defect and corrected behavior

The source documents `wait_replicas` as the number of synchronous acknowledgements to require. After a successful acquisition script, however, the existing code ignores a `WAIT` error. A successful response with too few acknowledgements produces only a warning. Both branches then return the acquired fencing token as `Ok`.

The correction maps a `WAIT` command or response-conversion error to the existing `LockError::StorageError`, and returns that error variant for an acknowledgement count below the configured requirement. Either branch exits this attempt before the fencing token is returned. A count at or above the requirement retains the successful path. The configuration comment records that an error does not imply that the Redis key was never created.

| Existing configuration/result | Corrected acquisition attempt |
| --- | --- |
| `wait_replicas == 0` | Existing disabled mode; no `WAIT` command is introduced |
| `WAIT` returns an error | Return `StorageError` before returning the token |
| Count below `wait_replicas` | Return `StorageError` including observed and required counts |
| Count equals or exceeds `wait_replicas` | Continue to the existing token return |

These are source control-flow consequences, not executed scenarios. The command still uses the same connection on which the Lua acquisition ran, the same arguments, and the same `Result<u32, redis::RedisError>` type. No asynchronous API, dependency, script, key naming, expiry or retry policy is added.

## Why an error must not trigger rollback

The Lua acquisition runs before `WAIT`. By the time the acknowledgement check fails, the lock hash, fencing-counter advance and expiry may already exist. This change does not delete that uncertain lock, reset its expiry, decrement the counter or attempt another write. The existing Redis expiry continues to elapse. A returned error must not be treated as evidence that the preceding mutation did not occur. A counter gap is not rolled back.

The actual `DistributedLock::acquire` consumer retries store errors at its existing 50 ms interval, subject to its existing attempt limit, and assigns `self.token` only on a successful store return. It can therefore retry after this error and eventually succeed, or wrap a terminal error in `AcquisitionFailed`. The public wrapper does not necessarily return `StorageError` immediately.

## Primary command contract

The official [Redis WAIT documentation](https://redis.io/docs/latest/commands/WAIT//), accessed 2026-10-06, says the command reports the number of acknowledging replicas even when its timeout is reached. The caller must compare that count with the requested level. The acknowledgement concerns preceding writes on the same connection. A zero timeout blocks indefinitely. WAIT does not make Redis strongly consistent, and acknowledged writes can still be lost during failover.

That contract supports the count/error check; it does not establish the donor's broader distributed-lock guarantees. The same official page was retrieved by search and opened directly. Unrelated search results were not used.

## Exact source custody

Repository: `s6pa1rta3n-lab/Stellar-inights`.
Contributor branch: `fix-issue-378`.
Contributor head: `3da2886f213203d52f5f09ed52bed7fb7d1511d5`.
PR base: `d8bae439cbaeb0f6b3a4fb36ffe212993c3af617`.

The native PR and its complete eight-file listing were acquired. A later native PR observation still reported the same head, base, draft/open/unmerged status and eight changed files. Complete UTF-8 bodies below were read at that immutable contributor head; each independently computed Git blob identity matched both the native file response and the corresponding PR-file SHA.

| Complete input | Git blob | Bytes | Role |
| --- | --- | ---: | --- |
| `backend/src/distributed_lock/redis_store.rs` | `a642adb90aa618119a25d60e5fa23942509455a3` | 18148 | Corrected source |
| `backend/src/distributed_lock/store.rs` | `034911c8bfb47ea59654e764f996f11bdb56a4be` | 13884 | Trait and metadata contract |
| `backend/src/distributed_lock/fencing.rs` | `12d84b8fe4ed2c00711c7af689a6217c120cf675` | 6961 | Token representation |
| `backend/src/distributed_lock/mod.rs` | `70f5a23b0803f06d4f85314d6dc5222c4671486d` | 6678 | Error variants and actual wrapper |
| `backend/Cargo.toml` | `365a21fb317157449e26308fbbe84709b826a3a5` | 977 | Declared edition2021 and redis0.27 dependency |

The manifest is a declared dependency constraint, not an installed version observation. The changed test files and Cargo.lock were not acquired or executed for this correction. Embedded test tails in complete source bodies were not run. The full-source provenance does not establish another application caller outside this module.

The corrected source is `a1784185a8f819c1e1562b29d90a41384e2638c3` / 18494 bytes. The serialized patch is `852a2a797cd73b965d331fc746a5cddbd3a449e6` / 1751 bytes.

## Retained repository context and attribution

The parallel PR393 source qualification retained a complete 1,514-entry, non-truncated recursive tree at its own contributor head `2611c78bfe97abe6f23302078097ec454a3d5007`, tree `edba05f583ad7070c6770abe7816e7c952f1ba25`, with no AGENTS.md or RULES.md entries. PR393 and PR386 share the base above, and both complete eight-file change listings contain backend paths only. Unchanged instruction and notice paths are inferred from that shared base and the complete path deltas; this is not a fresh PR386 recursive-tree observation.

The retained `docs/CONTRIBUTING.md` is blob `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2`, 274 bytes. It identifies EventSource, requests tests for fixes and describes an npm release process. No release process or application execution was attempted; the active session excludes executor and test work. There is no new approval claim derived from this file.

Three existing MIT notices are copied byte-for-byte under distinct filenames. They are preserved notices from the repository, not a claim that one listed author solely owns this backend contribution. The contributor author remains credited above.

| Preserved notice | Original path | Git blob | Bytes |
| --- | --- | --- | ---: |
| `upstream-licence-mclaughlin.md` | `docs/LICENCE.md` | `57740b9d4d86aedf5d518f2f363d5cf192c54127` | 1104 |
| `upstream-license-menke-laguna.md` | `docs/LICENSE.md` | `af5411fa243cfcf2b61c79d081dbb6204e956041` | 1111 |
| `upstream-license-de-wet.md` | `docs/license.md` | `4a766e268772888af5df56c3f6c608f68558b789` | 1080 |

## Checks performed and limits

The actual serialized unified diff was parsed and applied to the complete retained input text, then inverted against the new text. Both directions matched exactly, including hunk line counts and context. The two replacements were independently reversed; every other source byte matched the original. The complete diff contains two hunks and 31 rows. This is text validation of a new correction, not execution of the Rust or Redis application.

A second seat reviewed the exact donor block, replacement and outer retry-loop contract as a nongating source review. It had the transferred excerpt, not the complete cross-seat source store. No provider lookup or runtime execution was part of that review.

A dedicated Commons PR search for RedisLockStore and WAIT returned a bounded empty normalized list. The corresponding public Slack search reached native pagination end with zero results. These observations are limited to the actual queries, not proof of global uniqueness or permission.

No Rust compilation, formatter, Redis process, failover experiment, synthetic fixture, test suite, workflow, benchmark, browser or upstream action was used. No runtime or performance measurement is asserted.

Several existing limitations remain material. WAIT may consume the lock's remaining lifetime before success returns. A reused DistributedLock may retain an earlier token when a later acquisition fails. Existing Lua numeric conversions, epoch arithmetic, client-time metadata, forced expiry cleanup and fencing semantics are unchanged. The donor's documentation has broader claims which this small correction does not validate. Successful acknowledgement is not proof of a valid remaining lease, linearizability, durable failover monotonicity or complete issue378 acceptance.

## Continuation: omit configured URL from constructor failures

The additional `omit-url-from-constructor-errors.patch` applies **after** the acknowledgement patch above, to its retained complete source postimage from [Commons #32090](https://github.com/woahwhattheheck/commons/pull/32090). The earlier patch, source receipts and three notice files remain unchanged. This continuation was composed directly from the saved postimage; the accepted earlier patch was not reapplied or rerun.

The constructor currently passes `config.url.as_str()` into `redis::Client::open`. Its error mapping then formats both the entire `config.url` and the parser error into the returned `LockError::StorageError`. The complete source of `LockError` also shows that the StorageError display includes that stored string. No actual log, error report or exposed credential was observed; the defect is the explicit data flow from configuration into this error value.

The new mapping retains the existing error variant and propagation, but returns only the fixed text `Invalid Redis connection URL`. It ignores the parser error instead of including potentially input-derived detail. The success branch receives exactly the same URL and proceeds through the same scripts and configuration storage.

The deliberate tradeoff is less detailed diagnostics for an invalid URL. The returned value still identifies the Redis connection configuration as the failing operation. There is no credential parsing, substring redaction, password-format assumption or fallback connection. All connection and lock operations remain unchanged.

The maintainer-authored current redis-rs connection documentation, already returned before the tagged lookup, describes URL forms with optional username and password fields ([IntoConnectionInfo](https://docs.rs/redis/latest/redis/trait.IntoConnectionInfo.html), retrieved 2026-10-06). It is used only to explain why a connection URL can contain credentials. This correction uses no new crate API.

A subsequent direct lookup of `https://docs.rs/redis/0.27.6/redis/trait.IntoConnectionInfo.html` returned an inaccessible-page result, despite the tool envelope's false error flag. That exact route is held: no retry or alternate tagged-source acquisition was made. The prior latest documentation is not a validation of the donor's resolved crate version or a clearance of that route. The source-qualified string replacement does not depend on an unobserved tagged implementation or an executed parser.

| Constructor continuation identity | Git blob | Bytes |
| --- | --- | ---: |
| Input: saved postimage after #32090 | `a1784185a8f819c1e1562b29d90a41384e2638c3` | 18494 |
| New complete source postimage | `c280bfcb2ad4d457facd1fabe47f7d6d0a3a0d12` | 18486 |
| Serialized constructor patch | `55399e470e66d756cdf0411617323c7a36f799c8` | 720 |

The actual serialized patch contains one hunk/eight rows and changes one line for one line. Parsing and applying its context and hunk counts to the complete saved input yields the exact new text; inverse application reproduces the exact input. Reversing the single replacement confirms every other byte is preserved, including the newly accepted WAIT handling.

A new dedicated Commons PR query and public Slack query for RedisLockStore and the invalid-URL error text returned bounded empty results; Slack reached native pagination end. This does not establish global absence of related work.

The guarantee is restricted to the `RedisLockStore::new` error value constructed by this mapping. The configuration's public URL field, derived Debug implementation, `config()` accessor, other connection errors, dependency-internal behavior and unrelated logging are unchanged. There is no repository-wide sanitization or incident-remediation claim. No real credentials or supplied connection URLs were used, and no parser, network connection, Rust build, test, fixture, workflow or application code was executed.
