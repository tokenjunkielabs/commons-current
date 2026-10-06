# PR389 upgrade-scope documentation correction

PR389's privilege-graph document names its second invariant differently from the two source-level documentation assertions. It also describes the supplied V1-to-V2 regression as protection against arbitrary newly installed WASM. This packet corrects that heading and limits the documentation to the address checks and specific fixture assertions visible in the acquired source.

This is an attributed review patch for [Stellar-Analysis/frontend issue #381](https://github.com/Stellar-Analysis/frontend/issues/381) and [contributor PR #389](https://github.com/Stellar-Analysis/frontend/pull/389). It is not an upstream submission, security fix, runtime verification, whole-issue completion, or reward claim.

## Exact donor and authorship

- Contributor: **s6pa1rta3n-lab**, repository **s6pa1rta3n-lab/Stellar-inights**.
- Immutable donor head: `a66f57300a612dc5322915e4739de614946107d9`, branch `fix-issue-381`.
- Observed PR base: `1f9a81d18b7d84ba1892a6279017c434391cbe70`.
- Independently observed upstream main during qualification: `482ee456369418ef82c4056718cb82d3468f762b`. The donor changes are not asserted to exist there.
- PR389 was open and unmerged, with nine changed files. The dedicated all-state issue-number PR search returned PR389; it is a bounded query, not exhaustive semantic overlap clearance.
- Issue381 was open with no native assignees. Its four retrieved comments requested assignment. Those requests, the contributor's PR, and the issue's “Maybe Rewarded” label do not establish assignment, acceptance, a cash amount, or payment eligibility.
- Existing PR386, Infra's separate379 work, and assigned382 were excluded.

Original contributor and project authorship remain intact. This packet contains a narrow derived patch, explanatory provenance, and the notice texts found at the exact donor head; it does not repackage the full source tree.

## Changes

`pr389-doc-coverage.patch` changes two donor files, **36 added / 36 removed lines**:

1. `docs/contract-privilege-graph.md`: **+24/-21**. “Upgrade Manager Non-Self-Modification Invariant” now matches `scope.rs` and both existing document assertions. The overview, target row, diagram label, invariant scope, recorded-hook section and regression description distinguish direct address restrictions from the supplied target implementation's expected guards.
2. `contracts/upgrade/src/scope.rs`: **+12/-15**, documentation comments only. Direct governance/self target checks are separated from target-code assumptions and particular authentication regressions.

No test file or executable Rust statement is changed. No authentication check, target allowlist, WASM validation, upgrade flow, storage operation, dependency, build configuration, or fixture is added.

## Evidence and limits

At the donor head, document line54 says “Upgrade Orchestrator Non-Self-Modification Invariant”, while `tests/privilege_escalation_test.rs` line24 and `contracts/tests/privilege_escalation_test.rs` line28 look for “Upgrade Manager Non-Self-Modification Invariant”. The latter spelling also occurs in `scope.rs` line12. The literal mismatch is source-established; whether either wrapper test is discovered by a particular runner was not investigated.

The complete host test uploads `fixture_wasm("stellar_insights_v2")` and then calls that supplied implementation's setter, expecting `UpgradeManagerAlreadySet`. Other assertions make direct unauthenticated upgrade/migration/proposal calls. The test does not install an adversarial replacement fixture or enumerate every indirect privilege path. These specific source assertions do not establish universal enforcement against arbitrary replacement WASM.

The corrected prose does not assert that an attack was executed or that arbitrary-code escalation succeeds. It records the boundary of the acquired test and predicate. A runtime authorization design, adversarial fixture, broader contract audit and issue381's remaining acceptance criteria remain separate work. Other contract-inventory statements are inherited contributor context, not a new independent audit.

## Immutable source identities

All six complete source bodies were acquired at the donor head and matched both native and independently computed Git blob identities.

| Path | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `contracts/upgrade/src/scope.rs` | `d8762db443be9b01cf4d77f91a12ccb44659a242` | 3021 |
| `contracts/upgrade/tests/privilege_escalation_test.rs` | `f87d0df7d07829e7bedcc58f52b7fe217ba06ded` | 9807 |
| `contracts/upgrade/tests/test_support/mod.rs` | `886fe4732c7e7ec4146399b6083aeae55ec42add` | 5885 |
| `docs/contract-privilege-graph.md` | `ad7baff3f79983a3cf00981fefd8a870141a14b3` | 11098 |
| `contracts/tests/privilege_escalation_test.rs` | `7d55f1826551d0bb7649542b5c83cd030549f2cd` | 2519 |
| `tests/privilege_escalation_test.rs` | `d1ee47a97371b1506be2a48030690aee00b5fdae` | 2172 |

Patch preimages and reconstructed postimages:

| Donor path | Preimage blob | Postimage blob | Postimage bytes |
| --- | --- | --- | ---: |
| `docs/contract-privilege-graph.md` | `ad7baff3f79983a3cf00981fefd8a870141a14b3` | `fd992e243782b7590f3fec6b07f8fd12fb5813c1` | 11717 |
| `contracts/upgrade/src/scope.rs` | `d8762db443be9b01cf4d77f91a12ccb44659a242` | `5e37a03212540bf2fa699cd2cd7246ab92342825` | 2256 |

The postimage identities describe the patched donor files. Those files are represented here by the patch; they are not claimed to be separately native-blob acknowledged or installed upstream.

## Validation actually performed

- Compared the complete donor bodies with the PR file-map identities and independent Git blob hashes.
- Applied each generated unified-diff hunk to the retained exact preimage in memory and matched the complete intended postimage.
- Compared `scope.rs` before and after with documentation-comment lines removed: all remaining lines are identical.
- Inspected the changed wording and the exact heading/assertion strings.
- Kept the three acquired test files and test helper unchanged.

These are source/text checks, not execution of Rust tests. No shell, compiler, Cargo, Soroban host, WASM build, application runtime, network deployment, or upstream mutation was used. Neither `git apply --check` nor the contributor's claimed tests were run. No prior accepted computation or proof was replayed.

For later application, use the exact donor head and check the patch's preimage identities. A different head requires fresh composition; successful application alone would not establish issue381's security requirements.

## Notice provenance

The exact donor root had no root-level license file in the returned directory listing, and GitHub's returned repository license metadata was null. Its docs directory contained three differently attributed MIT notice files. Their exact bytes are retained separately:

| Donor path | Packet notice | Blob | Bytes |
| --- | --- | --- | ---: |
| `docs/LICENCE.md` | `NOTICE-MCLAUGHLIN-MIT.txt` | `57740b9d4d86aedf5d518f2f363d5cf192c54127` | 1104 |
| `docs/LICENSE.md` | `NOTICE-MENKE-LAGUNA-MIT.txt` | `af5411fa243cfcf2b61c79d081dbb6204e956041` | 1111 |
| `docs/license.md` | `NOTICE-DE-WET-MIT.txt` | `4a766e268772888af5df56c3f6c608f68558b789` | 1080 |

The notice texts retain their original copyright names and line endings. Their coexistence does not establish one repository-wide license or attribute the reviewed contract code to those named copyright holders. No broader license or authorship inference is made.

## Publication boundary

This packet is for Commons review only. The upstream issue, contributor PR, branch and comments were not changed. No maintainer/sponsor contact, assignment, acceptance, payout, or revenue claim is authorized by the packet. A fresh contributor-head guard precedes the guarded Commons publication; the publication receipt separately identifies its resulting commit and complete artifact checks.
