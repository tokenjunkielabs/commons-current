# Reject votes through the method after a proposal closes

## Problem and correction

This packet supplies a narrow source correction to [Stellar-Analysis/frontend PR402](https://github.com/Stellar-Analysis/frontend/pull/402), authored by **only1dreamgene**, for the existing governance proposal associated with [issue342](https://github.com/Stellar-Analysis/frontend/issues/342).

The proposed governance module has an explicit lifecycle. `Proposal::new` initializes `Open`. `quorum::finalize` sets either `QuorumMet` or `QuorumNotMet`. However, `Proposal::cast_vote` only checks for a duplicate voter; a new voter can still change `votes` and `votes_cast` after either finalization outcome. The public `Governance::vote` method delegates directly to this method.

`reject-closed-proposal-votes.patch` adds `ProposalError::VotingClosed` and an early status check before the duplicate check and both mutations. The contract becomes: votes are accepted through `cast_vote` only while the proposal is open. The patch changes one file, +6/-1 lines, two hunks and twenty diff rows.

| Proposal state and call | Result after this correction |
| --- | --- |
| Open, voter not yet recorded | Existing insertion and saturating tally addition |
| Open, duplicate voter | Existing `AlreadyVoted` error |
| QuorumMet or QuorumNotMet, any voter | `VotingClosed` before any map/tally mutation |
| Unknown proposal through `Governance::vote` | Existing `UnknownProposal` error before method delegation |

These are consequences of the acquired source and the proposed branch ordering, not results of executed tests. Closed duplicate votes now receive `VotingClosed` rather than `AlreadyVoted`; that error precedence is intentional. The added public enum variant can require changes in external exhaustive matches. No external caller compatibility or compilation is claimed.

The threshold calculation, snapshotted denominator, registered weights, IDs, finalization operation, duplicate handling while open, and all successful open-vote mutation code remain unchanged.

## Scope and remaining design boundaries

This is method-level lifecycle enforcement. `Proposal` exposes `status`, `votes`, `votes_cast`, the denominator and threshold as public fields; `Governance::proposal_mut` also returns a mutable reference. External code can still reopen or directly edit a proposal. This patch does not turn finalization into an immutable or authenticated storage boundary and does not alter public-field visibility.

The current method accepts a caller-supplied weight without checking a voter-specific snapshot. Existing registration-total arithmetic, saturating tally arithmetic, threshold multiplication, threshold validation, repeated finalization and arbitrary mutable-field updates are outside this correction. It does not establish a secure governance protocol, validate delegation, or complete the full issue342 requirements.

The acquired `Governance::vote` delegates to the corrected method, so there is an actual local caller. No deployed service, registered contract, transaction or live vote was inspected or changed.

## Exact source and assignment context

Contributor repository: `only1dreamgene/Stellar-inights`.
Branch: `drips/342-346`.
Immutable head: `3126694176b52f81407d0d6aa8b31ce9887e9f84`.
Base: `482ee456369418ef82c4056718cb82d3468f762b`.

Native issue metadata was open and assigned to `only1dreamgene`. Its two acquired comments contain that user's assignment request and a campaign bot message naming `samuel2926i39-art`. The differing names are preserved as separate observations; they are not resolved into a shared identity or a new assignment. PR402's native author is `only1dreamgene`. This packet attributes the existing work and makes no ownership or bounty claim.

The PR was observed open, non-draft and unmerged, with a complete eight-file added-path list. It combines governance issue342 with access-control issue346. Four governance source files were acquired completely at the immutable head; every native blob SHA, PR-file SHA and independently computed Git blob identity matched.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| [`contracts/governance/src/proposal.rs`](https://github.com/only1dreamgene/Stellar-inights/blob/3126694176b52f81407d0d6aa8b31ce9887e9f84/contracts/governance/src/proposal.rs) | `cf10831a7c9c1d7725570a8a1376e99ab1e092a5` | 2175 |
| [`contracts/governance/src/lib.rs`](https://github.com/only1dreamgene/Stellar-inights/blob/3126694176b52f81407d0d6aa8b31ce9887e9f84/contracts/governance/src/lib.rs) | `8aa657b575fa89d2ca90c2e6a93077c08ffb35c6` | 3345 |
| [`contracts/governance/src/quorum.rs`](https://github.com/only1dreamgene/Stellar-inights/blob/3126694176b52f81407d0d6aa8b31ce9887e9f84/contracts/governance/src/quorum.rs) | `3fcb1ddaf10d1076c60bc513633450875a53fe92` | 2326 |
| [`contracts/governance-voting/src/lib.rs`](https://github.com/only1dreamgene/Stellar-inights/blob/3126694176b52f81407d0d6aa8b31ce9887e9f84/contracts/governance-voting/src/lib.rs) | `99706fe98963c084876546087b9098cd2ec09fb5` | 1056 |

The changed proposal postimage is `b695120c2b907f244b23e170ee4236d9f7d5117d`, 2369 bytes. The patch itself is `49fb6ecdac5f0698c141055be29b2c31acb7fc89`, 884 bytes. Every other input file remains unchanged.

## Integration limits

The complete PR delta contains the four governance files, three access-control files and `tests/cross_contract_revocation_test.rs`. It adds no Cargo manifest or existing registration change. The acquired governance files use ordinary Rust structs and standard-library collections; they contain no access-control imports or generated Soroban contract client surface.

The voting library declares a delegation module that is not among the eight added files. Existing base-tree presence of that module was not independently classified for this packet, so its absence from the delta is not presented as repository-wide absence. No build-discovery or whole-carrier compile claim is made.

A separate seat acquired the complete three access-control modules and the revocation test at the same head, with matching native and independent identities. Its source review found incompatible role types, argument order, return/error interfaces and test entrypoint names; it parked issue346 without modifying those files. Root's own governance read confirms that the production modules contain no live access-control checks. This lifecycle patch does not repair or validate the access-control integration.

The retained canonical-base instruction observation reported a complete 959-entry response, not truncated, with no AGENTS/RULES paths. The separately observed branch tree was `44703ba39198f99b6541450c740db0d1c3c0f7b8`; the recursive response's SHA echoed the commit, so there is no claim of independently reconstructed tree identity. The surviving transfer is a summary, not a newly acquired PR402 tree or a recoverable full array. Because the PR has the same exact base and all eight changed paths are the enumerated source/test additions, unchanged instruction and notice paths are inferred from that base plus the complete delta.

Retained `docs/CONTRIBUTING.md` metadata is `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2`, 274 bytes, summarized as an EventSource test and npm release guide. That summary is not treated as native full-body text and no such process was run.

Three retained MIT notices are included with exact original text and line endings. They preserve distinct attributions rather than establishing a repository-wide licensing conclusion:

| Preserved notice | Original path | Blob | Bytes |
| --- | --- | --- | ---: |
| `upstream-licence-mclaughlin.md` | `docs/LICENCE.md` | `57740b9d4d86aedf5d518f2f363d5cf192c54127` | 1104 |
| `upstream-license-menke-laguna.md` | `docs/LICENSE.md` | `af5411fa243cfcf2b61c79d081dbb6204e956041` | 1111 |
| `upstream-license-de-wet.md` | `docs/license.md` | `4a766e268772888af5df56c3f6c608f68558b789` | 1080 |

## Validation and overlap coverage

The new serialized unified patch was parsed, including exact file headers, hunk coordinates, context lines and row counts. Forward application reproduced the full intended postimage; inverse application reproduced the full original. Reversing the selected replacements also reproduced the original exactly, establishing that all other bytes stayed unchanged. These were text operations, not application execution.

A second seat reviewed the transferred exact lifecycle/caller contract without a provider call or execution. It agreed that the guard covers both closed states and precedes mutation, identified the intentional closed-duplicate error precedence, and confirmed the public-field bypass limitation. This was a nongating contract review, not an independent full-source audit.

A broad dedicated Commons PR search returned twenty unrelated governance/business titles; their bodies were not expanded. A narrower dedicated Commons search for Stellar and342 returned no results. The public Slack search for governance andVotingClosed returned zero results and native end. These are bounded observed searches, not proof of global uniqueness.

No compiler, tests, fixture, workflow, Soroban runtime, transaction, on-chain operation or upstream mutation was used. Publication in Commons is an attributed source packet, not upstream acceptance, a deployed repair, completed issue342, or a payment claim.
