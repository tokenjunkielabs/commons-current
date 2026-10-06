# Use Redis expiry for expired-lock cleanup

## Defect and correction

The Redis lock proposal in [Stellar-Analysis/frontend PR386](https://github.com/Stellar-Analysis/frontend/pull/386), authored by **s6pa1rta3n-lab**, uses two different clock domains. Acquisition and renewal set the actual Redis key timeout using `PEXPIRE`, while also storing `expires_at_ms = caller_now + ttl` as hash metadata. The existing cleanup script compares that stored timestamp with the cleanup caller's wall clock and deletes the key when the latter is larger.

A cleanup caller whose clock is ahead of the acquiring caller can therefore authorize deletion while Redis still gives the lease positive remaining time. That follows from the source's different inputs; no clock experiment or observed production incident is claimed.

`use-redis-expiry-for-cleanup.patch` replaces the metadata/client-clock comparison with `PTTL` inside the existing single-key Lua script. It calls `DEL` only when Redis reports exactly zero milliseconds remaining and returns the actual deletion count. The Rust wrapper no longer computes or passes a wall-clock argument, and still returns `released == 1`.

The change is +4/-15 lines in two hunks, thirty-three diff rows, in `backend/src/distributed_lock/redis_store.rs`. Every other byte of the retained postimage remains exact, including the existing [#32090 WAIT acknowledgment correction](https://github.com/woahwhattheheck/commons/pull/32090) and [#32095 fixed constructor-error message](https://github.com/woahwhattheheck/commons/pull/32095).

## Deletion boundary

| Redis-reported TTL | New explicit script action |
| --- | --- |
| Positive milliseconds | Return zero without calling DEL |
| Exactly zero milliseconds | Call DEL and return its actual count |
| No expiration, represented by -1 | Return zero without calling DEL |
| Missing key, represented by -2 on Redis 2.8+ | Return zero without calling DEL |

The condition is equality with zero, not less-than-or-equal. Persistent keys are not authorized for deletion by this cleanup method. A key already expired or absent can return false: the method reports true only when its explicit DEL returns one. No true result is promised for every elapsed lease.

The [official PTTL command reference](https://redis.io/docs/latest/commands/pttl/) documents remaining milliseconds and the negative sentinel values; Redis 2.6 used the same negative sentinel for absent and persistent keys, both of which this equality check also excludes. The [official scripting reference](https://redis.io/docs/latest/develop/programmability/eval-intro/) documents atomic server-side script execution. The check and conditional deletion stay in one keyed invocation, without a separate client-side read/delete interval. These references describe the command contract, not an observed Redis deployment or a particular installed client library.

The patch does not modify the client-clock timestamps stored during acquisition or renewal. Those fields can still be misleading if interpreted elsewhere. Server clock changes, persistence, replication/failover, token precision, TTL input validation, other public mutation methods and multi-key cluster compatibility remain outside this correction. A key with its expiration removed will remain present until handled separately; this method does not infer expiry from its metadata.

## Source lineage and exact identities

Contributor repository: `s6pa1rta3n-lab/Stellar-inights`.
Immutable PR386 head: `3da2886f213203d52f5f09ed52bed7fb7d1511d5`.
Base: `d8bae439cbaeb0f6b3a4fb36ffe212993c3af617`.
The retained contributor proposal is open, draft and unmerged. It is attributed as existing work rather than represented as a new assignment or completion of issue378.

Apply the packet's source patches in this order:

1. `require-wait-acknowledgements.patch` from #32090.
2. `omit-url-from-constructor-errors.patch` from #32095.
3. `use-redis-expiry-for-cleanup.patch` from this continuation.

No accepted patch was replayed. The new change starts directly from the complete retained #32095 source postimage.

| Redis store stage | Git blob identity | UTF-8 bytes |
| --- | --- | ---: |
| Original complete contributor file | `a642adb90aa618119a25d60e5fa23942509455a3` | 18148 |
| Retained post-#32090 source | `a1784185a8f819c1e1562b29d90a41384e2638c3` | 18494 |
| Retained post-#32095 source, this patch's preimage | `c280bfcb2ad4d457facd1fabe47f7d6d0a3a0d12` | 18486 |
| New cleanup source postimage | `a6329e5c22762af4d304923d69059c4716f0f72c` | 18134 |

The new patch identity is `91b7e2177fbb2e7494021c3c7a9130cc8fbaeb51`, 1516 bytes. The new source postimage is a computed identity of the retained full source text, not a claim that the contributor repository now contains that blob.

Original complete inputs were acquired at the immutable head with matching native, PR-file and independently computed identities:

| Input | Blob | Bytes |
| --- | --- | ---: |
| [`backend/src/distributed_lock/redis_store.rs`](https://github.com/s6pa1rta3n-lab/Stellar-inights/blob/3da2886f213203d52f5f09ed52bed7fb7d1511d5/backend/src/distributed_lock/redis_store.rs) | `a642adb90aa618119a25d60e5fa23942509455a3` | 18148 |
| `backend/src/distributed_lock/store.rs` | `034911c8bfb47ea59654e764f996f11bdb56a4be` | 13884 |
| `backend/src/distributed_lock/fencing.rs` | `12d84b8fe4ed2c00711c7af689a6217c120cf675` | 6961 |
| `backend/src/distributed_lock/mod.rs` | `70f5a23b0803f06d4f85314d6dc5222c4671486d` | 6678 |
| `backend/Cargo.toml` | `365a21fb317157449e26308fbbe84709b826a3a5` | 977 |

The acquired `LockStore` trait explicitly exposes `force_release_expired` as cleanup and defines the boolean as whether a lock was actually released. The concrete Redis implementation is therefore an existing public library operation. The complete higher-level distributed-lock module does not call this cleanup method; an operational scheduler, service mount or deployed cleanup caller has not been established. This packet fixes the operation's own deletion authority without inventing such a caller.

## Repository context and preserved artifacts

The existing README and two earlier patches remain unchanged. The packet's three exact preserved MIT notices also remain unchanged:

- `upstream-licence-mclaughlin.md`: `57740b9d4d86aedf5d518f2f363d5cf192c54127`, 1104 bytes, original CRLF.
- `upstream-license-menke-laguna.md`: `af5411fa243cfcf2b61c79d081dbb6204e956041`, 1111 bytes.
- `upstream-license-de-wet.md`: `4a766e268772888af5df56c3f6c608f68558b789`, 1080 UTF-8 bytes.

These notices preserve their different attributions and are not presented as a repository-wide licensing determination.

The prior instruction-context transfer is unchanged: the infrastructure seat's complete 1514-entry, untruncated PR393 tree at `2611c78bfe97abe6f23302078097ec454a3d5007` (tree `edba05f583ad7070c6770abe7816e7c952f1ba25`) reported no AGENTS/RULES paths. That PR and PR386 share base `d8bae439cbaeb0f6b3a4fb36ffe212993c3af617`, and their complete changed-file lists are backend-only, supporting an inference that instruction/notice paths remain unchanged. This is not a newly acquired PR386 tree.

The retained contributing-note metadata is `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2`, 274 bytes, with a transferred summary describing EventSource tests and npm release commands. No transcription of that summary is treated as exact native content, and those commands were not executed.

## Validation and limits

The newly emitted patch was parsed with exact path headers, hunk coordinates, context and row counts. Forward application reproduced the complete intended new source; inverse application reproduced the complete preimage. Reversing the selected replacements also recovered the preimage exactly. All pre-existing WAIT and constructor changes were preserved byte-for-byte; their applications were not repeated.

A second seat reviewed the transferred cleanup/trait contract without provider acquisition or execution. It confirmed the explicit-zero boundary, handling of positive/persistent/absent keys, returned DEL count, and the remaining metadata-clock limitation. That was a nongating source-contract review, not an independent runtime validation.

Dedicated Commons and public Slack searches for Redis andforce_release_expired returned zero results, with native end on Slack. This is bounded overlap coverage, not global uniqueness.

The initial PTTL web search was displayed but was not assigned to a local raw-result store; it is not reconstructed or replayed. The subsequent two official page opens and selected finds are retained. The earlier inaccessible tagged docs.rs0.27.6 route remains held and was not retried or replaced by this command-level research.

No Redis instance, connection, lease acquisition, renewal, release, Lua execution, clock experiment, compiler, test, fixture or workflow was run. No real lock or stored data was changed. No upstream mutation, deployed remediation, overall fencing/linearizability guarantee, complete issue378, acceptance or payment is claimed.
