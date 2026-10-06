# Soroban patch application order and source identities

This directory contains seven incremental source patches, their seven guides and three original license notices. The original README describes the first patch; it does not by itself describe the complete later chain. This document joins the recorded patch dependencies and exact file identities so a reviewer can select the correct inputs without inferring order from filenames or PR numbers.

The records below describe attributed candidate source changes published in Commons. They do not assert that the upstream application contains them, that the seven patches have been executed together, or that a compiled or deployed integration has passed.

## Starting point and review order

The canonical donor is [Stellar-Analysis/frontend at 482ee456369418ef82c4056718cb82d3468f762b](https://github.com/Stellar-Analysis/frontend/tree/482ee456369418ef82c4056718cb82d3468f762b). Each first-touched file must have the exact canonical preimage recorded below. Later patches require the earlier postimages for the paths they share.

A full-directory review can follow this order:

| Step | Packet and patch | Purpose | Required source state |
| --- | --- | --- | --- |
| 1 | [#32125](https://github.com/woahwhattheheck/commons/pull/32125) — [mark-active-count-unavailable.patch](mark-active-count-unavailable.patch) | Mark failed active-count data unavailable while preserving successful zero. | Canonical donor files. |
| 2 | [#32129](https://github.com/woahwhattheheck/commons/pull/32129) — [mark-soroban-collections-unavailable.patch](mark-soroban-collections-unavailable.patch) | Separate failed top-contract/event-series collections from successful empty results. | #32125 for the API and page; canonical table/chart files. |
| 3 | [#32132](https://github.com/woahwhattheheck/commons/pull/32132) — [describe-gas-placeholder.patch](describe-gas-placeholder.patch) | Describe unavailable gas data without asserting an unsupported backend cause. | #32129 for the API; canonical gas panel. |
| 4 | [#32134](https://github.com/woahwhattheheck/commons/pull/32134) — [describe-deployment-coverage.patch](describe-deployment-coverage.patch) | Describe deployment coverage without attributing an unverified ingestion failure. | #32132 for the API; #32129 for the page; canonical deployment list. |
| 5 | [#32142](https://github.com/woahwhattheheck/commons/pull/32142) — [preserve-contract-call-calendar-labels.patch](preserve-contract-call-calendar-labels.patch) | Keep exact-shaped date-only event labels in UTC. | #32129 for ContractCallsChart; no later API/page dependency. |
| 6 | [#32163](https://github.com/woahwhattheheck/commons/pull/32163) — [show-neutral-zero-trends.patch](show-neutral-zero-trends.patch) | Present a successful zero trend neutrally in the shared metric card. | Canonical MetricCard; no other source patch is a textual prerequisite. |
| 7 | [This continuation](LOAD_LIFETIME.md) — [guard-soroban-load-lifetime.patch](guard-soroban-load-lifetime.patch) | Ignore page state writes from superseded or cleaned-up loads. | #32134 for the Soroban page; all earlier page changes preserved. |

The strict shared-file chain among the earlier packets is #32125 → #32129 → #32132 → #32134. The API follows all four steps. The Soroban page follows #32125 → #32129 → #32134 because #32132 does not modify it. #32142 follows the chart postimage from #32129 and can be reviewed after that prerequisite. #32163 changes a separate canonical MetricCard file and has no textual dependency on the earlier patches; its guide uses the actual retained Soroban callers to explain the zero-trend path. The new load-lifetime patch follows #32134 for the page; it does not require the later chart or MetricCard files as textual inputs.

Treat each multi-file patch as its described change set. Omitting its API, prop or rendering part does not establish the packet's documented behavior. A mismatching input identity requires a separate integration decision; this document does not authorize fuzzy application, reconstruct an unknown prior input, or supply an automatically rebased patch.

## Exact per-patch transitions

Every identity is a Git SHA-1 blob identity over the complete UTF-8 file, followed by its UTF-8 byte count. Paths are relative to the donor repository root. The earlier values are copied from retained source receipts; the new continuation row comes from its complete source and new-patch receipt. Preparing this document did not reapply any accepted patch.

| Packet | Source path | Required preimage / bytes | Recorded postimage / bytes |
| --- | --- | --- | --- |
| #32125 | src/lib/soroban-api.ts | 935249600cc5b3c4619c281d9516f8b95cc95671 / 8846 | 30fda2ab0e697c3edc64da7e7c836dd1bc22f4c5 / 8972 |
| #32125 | src/app/[locale]/soroban/page.tsx | 8c4dd50dc6593505a680b4071967c72ee77411b3 / 6064 | 617360329cf2f722fdd1d38b929ff39d0497e668 / 6136 |
| #32125 | src/components/soroban/ActiveContractsPanel.tsx | 9e798f63dc91a025e027f6fc24d30c14205c37c7 / 1251 | 56f76087005e608b23853edfd650bc34ee867f37 / 1414 |
| #32129 | src/lib/soroban-api.ts | 30fda2ab0e697c3edc64da7e7c836dd1bc22f4c5 / 8972 | 05f0966bb312ce10e736992d85dd83ceb7e64c66 / 9206 |
| #32129 | src/app/[locale]/soroban/page.tsx | 617360329cf2f722fdd1d38b929ff39d0497e668 / 6136 | d3bd13f0d05f967de8bb5f52a8a9328b34071e7a / 6273 |
| #32129 | src/components/soroban/TopContractsTable.tsx | dc578372c7d69fbf6af5f4d7d4eb7f01c3fc71f9 / 4674 | 85c6bb47446fecb0a3e6a3b290bfd4a64737906d / 4939 |
| #32129 | src/components/charts/ContractCallsChart.tsx | f774ac5797f96ecf69e1cc3f89c44b533825dba0 / 6618 | d36e06e5ff150e852e5f982f309ae86a5856861e / 6668 |
| #32132 | src/lib/soroban-api.ts | 05f0966bb312ce10e736992d85dd83ceb7e64c66 / 9206 | 5c62261b3b66fbee54a819f4fdbeea0a7e875631 / 9241 |
| #32132 | src/components/soroban/GasUsagePanel.tsx | 4b17ea601724ba4a90634e2703e7cdffbf1586a6 / 2634 | b2c66d8de14ce8ee0bfdb13688326c826ef71f37 / 2643 |
| #32134 | src/lib/soroban-api.ts | 5c62261b3b66fbee54a819f4fdbeea0a7e875631 / 9241 | a3ba6bc1f13ec89d31191d18550e8bb0b584b407 / 9226 |
| #32134 | src/app/[locale]/soroban/page.tsx | d3bd13f0d05f967de8bb5f52a8a9328b34071e7a / 6273 | 80ba478b5aa34d8af463ea4a5c6f969eeca114fa / 6254 |
| #32134 | src/components/soroban/NewDeploymentsList.tsx | 6cb57ff2a5cfc8aa70bf602297264b7bb7f2c55c / 5326 | 3a6bdbcac7e120d8e01515569da43dfe874a0ead / 5237 |
| #32142 | src/components/charts/ContractCallsChart.tsx | d36e06e5ff150e852e5f982f309ae86a5856861e / 6668 | ceb784684589b3d10787d5035bd8ae080405f7fd / 6850 |
| #32163 | src/components/dashboard/MetricCard.tsx | 0be01cd20b73e9cd85b74e17f94398ae7f69e7f0 / 2043 | 4e4d9ca76aafe84d0411756e0e2ff85544645de6 / 2144 |
| This continuation | src/app/[locale]/soroban/page.tsx | 80ba478b5aa34d8af463ea4a5c6f969eeca114fa / 6254 | 4719b2c3b6ed7bddc8f3c1c282b601e622f58c68 / 6569 |

For the seven repeated-file edges in this sequence, the earlier recorded postimage identity and size equal the later recorded preimage identity and size. This is a comparison of recorded metadata, not a fresh application or runtime check.

## Recorded final source set

The following eight identities are the last retained postimages in this seven-patch chain. They are useful targets for a future authorized integrator; the table is not a claim that these files have been placed in a deployed checkout.

| Source path | Final recorded blob | UTF-8 bytes | Last changing packet |
| --- | --- | ---: | --- |
| src/lib/soroban-api.ts | a3ba6bc1f13ec89d31191d18550e8bb0b584b407 | 9226 | [#32134](https://github.com/woahwhattheheck/commons/pull/32134) |
| src/app/[locale]/soroban/page.tsx | 4719b2c3b6ed7bddc8f3c1c282b601e622f58c68 | 6569 | [This continuation](LOAD_LIFETIME.md) |
| src/components/soroban/ActiveContractsPanel.tsx | 56f76087005e608b23853edfd650bc34ee867f37 | 1414 | [#32125](https://github.com/woahwhattheheck/commons/pull/32125) |
| src/components/soroban/TopContractsTable.tsx | 85c6bb47446fecb0a3e6a3b290bfd4a64737906d | 4939 | [#32129](https://github.com/woahwhattheheck/commons/pull/32129) |
| src/components/charts/ContractCallsChart.tsx | ceb784684589b3d10787d5035bd8ae080405f7fd | 6850 | [#32142](https://github.com/woahwhattheheck/commons/pull/32142) |
| src/components/soroban/GasUsagePanel.tsx | b2c66d8de14ce8ee0bfdb13688326c826ef71f37 | 2643 | [#32132](https://github.com/woahwhattheheck/commons/pull/32132) |
| src/components/soroban/NewDeploymentsList.tsx | 3a6bdbcac7e120d8e01515569da43dfe874a0ead | 5237 | [#32134](https://github.com/woahwhattheheck/commons/pull/32134) |
| src/components/dashboard/MetricCard.tsx | 4e4d9ca76aafe84d0411756e0e2ff85544645de6 | 2144 | [#32163](https://github.com/woahwhattheheck/commons/pull/32163) |

Complete strings for these new source postimages were retained during their producing work. Public checkpoint locators below supplement that custody. No missing pre-loss source from unrelated work is reconstructed or required by this chain.

## Artifact inventory and review guides

All fifteen earlier artifacts remain unchanged. The two new source artifacts appear alongside them in this seventeen-item inventory; this order guide is an additional document. The individual guides describe each patch's narrow behavior and limits; this file provides their dependency map.

| Packet | Existing artifact | Git blob | UTF-8 bytes |
| --- | --- | --- | ---: |
| #32125 | [mark-active-count-unavailable.patch](mark-active-count-unavailable.patch) | 69056f6f8a6d8b6fd7bd91dcd868322be7302e76 | 2935 |
| #32125 | [README.md](README.md) | 7292a6d5ca1d096cdba61eabe5619a798f5d794d | 8670 |
| #32125 | [upstream-licence-mclaughlin.md](upstream-licence-mclaughlin.md) | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| #32125 | [upstream-license-menke-laguna.md](upstream-license-menke-laguna.md) | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| #32125 | [upstream-license-de-wet.md](upstream-license-de-wet.md) | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |
| #32129 | [mark-soroban-collections-unavailable.patch](mark-soroban-collections-unavailable.patch) | 8ecc1cb2de5dd57652ba80e24078b2ceb17c4213 | 6680 |
| #32129 | [COLLECTION_AVAILABILITY.md](COLLECTION_AVAILABILITY.md) | 4f90725cccd64d9dc187ff7c4071b8d2bb578734 | 7751 |
| #32132 | [describe-gas-placeholder.patch](describe-gas-placeholder.patch) | 7df1dc3a2fe7f21934a6fef395795459116bcf4e | 2304 |
| #32132 | [GAS_PLACEHOLDER.md](GAS_PLACEHOLDER.md) | 61216738a32b77bcb4cb2ab86b1424386c016543 | 6169 |
| #32134 | [describe-deployment-coverage.patch](describe-deployment-coverage.patch) | 96e0bdaf6d8a0214c79d38b6e2a8bd32b54caa82 | 2766 |
| #32134 | [DEPLOYMENT_NOTICES.md](DEPLOYMENT_NOTICES.md) | 99b0124865a42c3716c5002b62218a05a87e66fc | 7108 |
| #32142 | [preserve-contract-call-calendar-labels.patch](preserve-contract-call-calendar-labels.patch) | 561ecd870670d8f494b0e60ded1046a5a85ca891 | 580 |
| #32142 | [CALENDAR_LABELS.md](CALENDAR_LABELS.md) | c2bffbb721271175115ff30bfd77cf9113689a23 | 6871 |
| #32163 | [show-neutral-zero-trends.patch](show-neutral-zero-trends.patch) | d943783922a12400e9469111f7ca10dbb2fa2ec8 | 1425 |
| #32163 | [ZERO_TREND.md](ZERO_TREND.md) | 8588b98036fc77b9b479da0e05eccc26e3ebf6c0 | 6761 |
| This continuation | [guard-soroban-load-lifetime.patch](guard-soroban-load-lifetime.patch) | 25ab778356d455cfff3ab252ddd6c64f69d9c758 | 2022 |
| This continuation | [LOAD_LIFETIME.md](LOAD_LIFETIME.md) | 32938b960c865fc629a7e6d6061f2a8ca3e872a8 | 7873 |

The three notices supplied with #32125 retain their original source text and attribution. Their existing line endings and UTF-8 contents are part of their recorded identities. They must accompany any use that requires those notices; this document replaces none of them.

## Scope that remains unchanged

The availability work distinguishes caught failure fallbacks from successful zero or successful empty results. It does not prove server coverage, validate every malformed payload, or change every asynchronous rejection path. The gas and deployment notices remove unsupported causal wording; their flags, request policy and normalization conditions remain as described in their guides.

The calendar-label change selects UTC only for a string of exactly ten characters with the YYYY-MM-DD digit-and-hyphen shape. It is not calendar validation and does not change the existing formatting of full timestamps or other input forms. The zero-trend change has no rounding threshold: only trend === 0 receives neutral styling, no directional arrow and no success glow. Nonzero/inverse and missing-trend behavior remain unchanged.

The new lifetime patch gates this page's asynchronous success, fallback and final loading writes using a unique request-owner object. Effect cleanup clears that ownership. Original error logging, request calls, values and rendered markup remain unchanged. It does not abort, deduplicate, cancel or retry requests, change their helpers, or claim that a stale-response incident was reproduced.

Nothing here supplies or validates a backend active-contract endpoint or a universal seven-day event-time contract. The separate [backend source analysis #32147](https://github.com/woahwhattheheck/commons/pull/32147) records unresolved producer time and coverage contracts; this frontend chain does not resolve them.

Earlier network-chart calendar fixes, unrelated wallet changes and other components are outside this directory's chain. Their acceptance or custody cannot be inferred from this inventory.

## Publication and recovery locators

These are the recorded Commons merge identities and acknowledged public checkpoint manifests for the six earlier packets. The containing PR records this new continuation's publication; no future PR number or checkpoint identity is guessed here. A Commons merge publishes the review artifacts; it is not an upstream application merge.

| Packet | Commons merge | Checkpoint manifest | Manifest bytes |
| --- | --- | --- | ---: |
| [#32125](https://github.com/woahwhattheheck/commons/pull/32125) | 2ac18885e44c1a7bfeeaebb1726b7d9340e6ee6b | c6799624308a7875bc42add05bc845345d9bb772 | 2822 |
| [#32129](https://github.com/woahwhattheheck/commons/pull/32129) | ee100a3e53ca35e9ee23d695351792b34ff3c8fa | c92aa4a1e7927d744550c7eb661fa9f20049a974 | 3086 |
| [#32132](https://github.com/woahwhattheheck/commons/pull/32132) | 6fbc2e6a3d674a34df192d7542878d05cae1c5c5 | fe857136099c218b42c779c2fd9024a713f1815b | 1909 |
| [#32134](https://github.com/woahwhattheheck/commons/pull/32134) | 41b27207973eb1ff1bc96724bb7dc0c83fa644a6 | 63518084a46841ab670add0aa3f5d34ad99975c6 | 1509 |
| [#32142](https://github.com/woahwhattheheck/commons/pull/32142) | 5d8678568f0236bb5c167c190d5ebeb0bb894205 | a3cfd8c0a531ceecb7ba01f0dc63379b0ae520e0 | 1625 |
| [#32163](https://github.com/woahwhattheheck/commons/pull/32163) | 5900b99c7e9ec6f3021c1f1a42d54170f9e12b57 | f6cb1fba8ed70ebbca9c45a36cb644425039e28b | 1357 |

The refined #32134 manifest 63518084a46841ab670add0aa3f5d34ad99975c6 contains its final publication spec and final deployment-list postimage. Its predecessor 0a7e7e4150015e6498ab6545ff53f4f6e7513452 retains the final API and page postimages, but also an earlier superseded spec and deployment-list draft. Only the refined spec and the final list identity 3a6bdbcac7e120d8e01515569da43dfe874a0ead / 5237 bytes belong to the published packet.

Later calendar and MetricCard checkpoints add their new postimages and publication specs; they do not replace that predecessor's final API/page custody. The blob acknowledgments establish recorded recovery locators, not indefinite retention guarantees. Native private operational journals are not included in this document.

## Verification performed for this document

The directory and tables were assembled from the six retained completion receipts, their source identity records and the new load-lifetime candidate's receipt. Each later shared-file preimage was compared with its immediate earlier recorded postimage, and the relative artifact links were checked against the seventeen-name prior-and-new artifact inventory. The final eight-file table selects the last transition for each path; it includes the new page candidate rather than claiming that candidate is already deployed.

The earlier documentation-only preparation at manifest 35daebd74fd9be1005bd0f8de13d44ee0c3103ff and spec aff2da84c67eefc441af22b633eb817c3946f3d5 was never dispatched as a branch publication. It is superseded by this combined continuation and must not be treated as the current seven-patch guide.

No accepted source patch was applied, inverted, recomputed or rerun while preparing this guide. No upstream source, older PR or artifact body was reacquired for it. No application expression, endpoint, renderer, compiler, test, fixture, browser or workflow ran. This document adds integration instructions only. It creates no upstream submission, deployment, bounty claim, payment entitlement or new license grant.
