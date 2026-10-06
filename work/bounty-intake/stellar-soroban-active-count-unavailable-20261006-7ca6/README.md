# Show an unavailable active-contract count after a failed request

## Problem and correction

The mounted Soroban dashboard calls `fetchSorobanActiveContracts("7d")`. Its helper catches a failed request and returns `{ count: 0, window }`. The page stores that object and passes the count to `ActiveContractsPanel`, which formats it as a measured “Active Contracts” value. A failed request therefore looks like a successful count of zero.

This three-file patch carries an explicit optional `unavailable` flag through that existing helper, page and panel. The helper's caught-failure return sets the flag. The page's own aggregate-failure fallback sets it too. The panel displays **Unavailable** with **Unable to load the count** and omits the trend and its direction when flagged.

A successful response containing zero keeps the existing zero display. A subsequent successful result replaces the prior state object and its absent flag defaults to false, so the ordinary display resumes. The numeric `count` field remains present for compatibility. The helper comment now states that a failed request supplies a marked placeholder.

The patch is +12/-7 lines across three files, eight hunks and 66 diff rows. All other bytes remain exact.

| Existing path | Corrected presentation |
| --- | --- |
| Helper catches fetch, non-OK response or awaited JSON failure | Unavailable count, with no trend |
| Page aggregate load reaches its catch | Unavailable count, with no trend |
| Successful numeric zero | Existing formatted zero and window label |
| Successful other numeric count | Existing number formatting and optional trend |
| Initial loading | Existing skeleton |
| A caller omits the optional flag | Existing presentation |

These rows describe the acquired code and new branch conditions, not executed tests.

## Actual caller and error chain

The complete API module contains a shared `fetchJson` that awaits fetch, throws for non-OK responses and returns the JSON promise. The active-contract helper awaits that call inside its try/catch, so a rejected JSON promise also reaches the existing catch. This differs from a caller that returns an unawaited JSON promise directly from its own try block.

The mounted page calls five helpers with `Promise.all`, writes their responses into separate state, and passes the active count, window, trend and loading state to the acquired panel. The added prop carries the new flag along this real caller path. It does not depend on a hypothetical integration.

The page-level catch can result from an unexpected failure in a sibling helper. Its flagged fallback means the page cannot present the count; it does not prove that the active-contract endpoint itself was the source of every aggregate failure.

Existing successful-response normalization stays unchanged. In particular, a missing or nonnumeric successful count is still normalized to zero, and number values are not newly checked for finiteness, negativity or integer range. This patch distinguishes the explicit caught-failure paths only. It does not establish a validated backend schema or trustworthy upstream data.

## Scope

The following behavior remains unchanged: endpoint and query construction, fetch options, non-OK handling, logging, successful normalization, all other helpers, the page's request ordering, refresh button, effects, loading flags, response replacement and the panel's loading skeleton and formatting function.

Other dashboard panels retain their existing empty/placeholder behavior. No broader dashboard availability or provenance claim is made. The patch adds no request cancellation, latest-request guard, retry policy, service health probe, account action or contract interaction.

The panel already supplies a string value to `MetricCard` through its formatter; the new unavailable branch also supplies a string. Its existing optional trend/direction props receive undefined in the unavailable branch. The shared MetricCard source was not reacquired or independently audited for this packet, and no runtime layout or accessibility result is claimed.

The three source changes should be applied together. Applying only the helper flag without passing and rendering it would leave the visible count unchanged.

## Exact source and attribution

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at `482ee456369418ef82c4056718cb82d3468f762b`. Fresh main metadata acquired during qualification still identified this donor. The complete source bodies were each fetched once for this new task; native file SHA and independently computed Git blob identities matched.

| Complete input | Original Git blob | Bytes | Postimage Git blob | Bytes |
| --- | --- | ---: | --- | ---: |
| [src/lib/soroban-api.ts](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/lib/soroban-api.ts) | `935249600cc5b3c4619c281d9516f8b95cc95671` | 8846 | `30fda2ab0e697c3edc64da7e7c836dd1bc22f4c5` | 8972 |
| [src/app/[locale]/soroban/page.tsx](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/app/%5Blocale%5D/soroban/page.tsx) | `8c4dd50dc6593505a680b4071967c72ee77411b3` | 6064 | `617360329cf2f722fdd1d38b929ff39d0497e668` | 6136 |
| [src/components/soroban/ActiveContractsPanel.tsx](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/components/soroban/ActiveContractsPanel.tsx) | `9e798f63dc91a025e027f6fc24d30c14205c37c7` | 1251 | `56f76087005e608b23853edfd650bc34ee867f37` | 1414 |

Patch identity: `69056f6f8a6d8b6fd7bd91dcd868322be7302e76`, 2935 UTF-8 bytes.

The bounded API path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, authored by **christabel888**. That commit moved the existing frontend into the repository root. This credits the observed canonical history without claiming that a one-entry path-history response exhausts authorship. Comments referring to backend issues are existing source context; those backend implementations and their completion status were not inspected for this change.

A retained historical canonical-base instruction summary reported a complete 959-entry response without AGENTS/RULES paths. The full historical array is no longer in working custody and is not being presented as a newly acquired or independently reconstructed tree. CONTRIBUTING metadata previously retained was `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2`, 274 bytes, summarized as an EventSource test/npm release guide; its complete native body is not retained for this packet. No such process was executed.

Three preserved MIT notices were acquired from their known immutable public blobs for this new packet and matched independent byte identities. Their original text and line endings are included without combining the attributions or claiming a repository-wide licensing determination.

| Included notice | Original donor path | Git blob | Bytes |
| --- | --- | --- | ---: |
| upstream-licence-mclaughlin.md | docs/LICENCE.md | `57740b9d4d86aedf5d518f2f363d5cf192c54127` | 1104 |
| upstream-license-menke-laguna.md | docs/LICENSE.md | `af5411fa243cfcf2b61c79d081dbb6204e956041` | 1111 |
| upstream-license-de-wet.md | docs/license.md | `4a766e268772888af5df56c3f6c608f68558b789` | 1080 |

## Verification and publication boundary

Each selected replacement was unique, and reversing the replacements restored every original byte. The complete serialized patch was separately parsed for exact file headers, hunk coordinates, context and row counts. Forward application reproduced each full intended postimage; inverse application restored each original. These checks operated on source strings; no application code ran.

A second seat reviewed the transferred helper/page/panel contract without additional source or provider calls. It found no concrete semantic flaw, confirmed successful zero and later recovery behavior, and identified the page aggregate-failure wording limit recorded above. This was a nongating contract review, not a full independent source or runtime audit.

The dedicated Commons PR search for Soroban, unavailable and active returned zero results. A public Slack search for fetchSorobanActiveContracts and unavailable returned zero with native end. These bounded results do not prove global uniqueness or provide ownership.

No compiler, tests, fixture, browser, API request to the application, contract call, transaction, workflow or upstream mutation was performed. Commons publication is an attributed source proposal, not a deployed fix, accepted upstream change, completed bounty or payment claim.
