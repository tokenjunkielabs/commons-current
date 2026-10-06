# Describe the backup helper's actual contract

## Correction

This packet corrects the API documentation around the proposed backup helpers in [Stellar-Analysis/frontend PR403](https://github.com/Stellar-Analysis/frontend/pull/403), attributed to **daniel6yi8-gif**. The contributor also owns the native assignment for [issue333](https://github.com/Stellar-Analysis/frontend/issues/333). This is a narrow documentation follow-up to that existing proposal, not a new ownership claim or completion of its full backup/restore task.

The complete source packages caller-supplied bytes, labels them with watermark values, filters cache entries, compares two numbers, and returns a prepared state. Its comments currently claim point-in-time consistency, reconciliation of snapshot skew, a safe resume point, and control over service startup. Those stronger behaviors are not implemented by these helpers.

`describe-backup-helper-contract.patch` changes only Rust documentation comments in two source files: +36/-35 lines, eight hunks, 120 diff rows. Every non-documentation line is identical. The watermark tolerance of one, all algorithms, signatures, data structures, errors and cache classification remain unchanged.

## What the source actually does

| Helper | Observed source behavior | Boundary made explicit |
| --- | --- | --- |
| `take_backup` | Receives a watermark, datastore byte vector and cache entries; filters by the existing classification and assigns the same supplied marker to both outputs | Does not collect a storage snapshot or verify when the supplied bytes were captured |
| `Watermark::reconcile` | Computes an absolute difference; accepts values within the supplied tolerance and returns their minimum | Does not inspect, rewind, replay or reconcile payload contents |
| `check_consistency` | Calls the watermark operation with `WATERMARK_TOLERANCE = 1` and maps its error | Checks marker compatibility rather than establishing physical snapshot consistency |
| `restore` | Checks the markers, clones datastore bytes unchanged, clones selected cache entries and returns `RestoredState` | Does not write to either store, cold-start a cache, or start or stop a service |

These statements come from the complete three-file module, including all sibling imports. The numeric operation's lower result is not by itself a proven recovery or resume point. Matching markers also do not establish consistency of opaque caller-supplied payloads. The caller must establish the relationship between the marker and the bytes and decide how to reconcile, apply and resume from them.

The correction keeps the existing tolerance policy. Tightening it to zero would change acceptance behavior and still would not prove that independently supplied bytes describe the same state. This packet does not substitute an unqualified recovery algorithm or change the contributor's chosen policy.

Classification remains as implemented: the existing helper retains its idempotency/cursor namespaces and drops the other/default classes. The patch does not establish whether that classification is appropriate for a real deployment, or whether omitted state is reconstructable. The documentation correction is confined to what these helper operations themselves perform.

## Exact contributor source

Repository: `daniel6yi8-gif/frontend`.
Head: `3566cbbd307c5fc1316477b3ef83c57b83af3eb9`.
Branch: `drips/333-334-335`.
Base: `482ee456369418ef82c4056718cb82d3468f762b`.

The native PR observation was open, non-draft and unmerged, with eleven added files. Its title emphasizes backup/restore, but its complete file list also contains the IP allowlist and job-runner modules. Those modules belong to separate follow-up work; this patch touches only backup documentation. The original assigned author and entire existing carrier remain credited.

All three backup source files were acquired completely at the immutable contributor head. Native file SHAs, complete PR-file SHAs and independently computed Git identities matched.

| Input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| [`backend/backup/mod.rs`](https://github.com/daniel6yi8-gif/frontend/blob/3566cbbd307c5fc1316477b3ef83c57b83af3eb9/backend/backup/mod.rs) | `2f3ef624b49e2aed8a7eb20a890d6b35408d7018` | 5084 |
| [`backend/backup/watermark.rs`](https://github.com/daniel6yi8-gif/frontend/blob/3566cbbd307c5fc1316477b3ef83c57b83af3eb9/backend/backup/watermark.rs) | `4df10a05a46927f660bfde99bf49ff03274891c4` | 2052 |
| [`backend/backup/classify.rs`](https://github.com/daniel6yi8-gif/frontend/blob/3566cbbd307c5fc1316477b3ef83c57b83af3eb9/backend/backup/classify.rs) | `fdcc6b9703b9144bb37b217766112b69d79dce96` | 2330 |

New documentation postimages:

| Changed source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `backend/backup/mod.rs` | `7e96f4db2395600fb1e3d3088352b93bdd697a21` | 5399 |
| `backend/backup/watermark.rs` | `ee1b37ebf87f1e55d1823a7e91ac17077283b9cc` | 2023 |

The patch blob is `7c2b8e44b78d84af9a55efa681b716dfc8832b1c`, 6898 bytes. The classification source remains byte-for-byte unchanged.

## Integration and repository context

The retained complete canonical base-tree response contained 959 entries, was not truncated and had no backend root or AGENTS/RULES entries. Separate retained branch metadata named tree `44703ba39198f99b6541450c740db0d1c3c0f7b8`; the recursive response's SHA echoed the requested commit, so this packet does not claim an independent reconstruction of that Git tree.

PR403's complete eleven-file delta adds the three backup files, three IP-allowlist files, four job files and one standalone disaster-recovery test source. It includes no Cargo manifest or existing application registration change. Build discovery, service mounting and deployment are therefore not established here. The test body was not acquired or executed for this correction.

Because the exact base matches the retained canonical context and all eleven changed paths are under backend, unchanged instruction/notice paths are inferred from the same base plus the complete delta. This is not a new recursive-tree acquisition at PR403 head. The retained `docs/CONTRIBUTING.md` metadata is `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` / 274 bytes; its transferred content summary identifies EventSource tests and an npm release process. The full native body remains in the infrastructure seat's custody. No transcription is treated as native source bytes and no release/test process was executed.

Three existing MIT notices are preserved with distinct names and exact original line endings. Their coexistence is not treated as a repository-wide backend ownership or licensing determination:

| Preserved file | Original path | Git blob | Bytes |
| --- | --- | --- | ---: |
| `upstream-licence-mclaughlin.md` | `docs/LICENCE.md` | `57740b9d4d86aedf5d518f2f363d5cf192c54127` | 1104 |
| `upstream-license-menke-laguna.md` | `docs/LICENSE.md` | `af5411fa243cfcf2b61c79d081dbb6204e956041` | 1111 |
| `upstream-license-de-wet.md` | `docs/license.md` | `4a766e268772888af5df56c3f6c608f68558b789` | 1080 |

## Validation and coverage

The new serialized multi-file diff was parsed, including both path headers, every hunk's coordinates and every context row. Forward application reproduced both intended full postimages; inverse application reproduced both complete inputs. Reversing every selected comment replacement also reproduced each original exactly. A separate comparison with documentation lines removed confirmed equality of every remaining line.

A second seat reviewed the transferred exact helper contract without a provider call or execution. It agreed that numeric marker compatibility does not prove physical payload consistency, automatic recovery or service gating. That was a nongating excerpt review, not an independent full-source audit.

A dedicated Commons PR search for backup, watermark and403 returned an empty bounded list. The public Slack query returned twenty historical headers and another-page cursor. Seventeen prefixes of at most150 characters were screened; three existing private-channel bodies stayed withheld. The observed prefixes concerned other owned, terminal, held or unrelated work. No full message was expanded and the search did not reach native end; global uniqueness is not claimed.

No backup operation, payload mutation, service lifecycle action, numeric experiment, Rust compilation, rustdoc run, test, fixture, workflow or upstream publication was performed. This packet improves the source's documented API contract. It does not make the proposed backup design point-in-time consistent, validate disaster recovery, establish a deployed caller, complete issue333 or claim acceptance or reward.
