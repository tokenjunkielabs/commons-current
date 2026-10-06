# Distinguish unavailable Soroban collections from empty responses

## Problem and correction

This continuation applies after [Commons #32125](https://github.com/woahwhattheheck/commons/pull/32125), which corrected the active-contract count. The existing top-contract and contract-call helpers have the same information-loss boundary for collections: a caught request failure becomes an empty array without an availability signal.

The acquired TopContractsTable then reports “No contract activity in this window” and TOP_0. The acquired ContractCallsChart reports that no series exists yet. Those messages conflate a failed retrieval with a successful empty response.

The new patch carries optional `unavailable` flags through the two response interfaces, their existing caught-failure returns, the mounted page, and the two actual child components. It changes four files, +27/-15 lines, sixteen hunks and 156 diff rows.

- A flagged top-contract result displays an UNAVAILABLE badge, “Top contracts unavailable,” and fixed text pointing to the existing Refresh action.
- A flagged contract-call result displays fixed unavailable text pointing to the same existing action.
- A successful empty series states only that no daily event counts were returned for the period.
- Successful populated results retain their existing table rows, chart calculations, chart configuration and export surface.

Unavailable branches take precedence over the empty-result branch. The top-contract badge also uses the flag, so it does not continue to show TOP_0 beside an unavailable list.

The mounted page sets both flags in its existing aggregate-failure catch and passes the actual response flags to the children. An aggregate catch does not prove that each individual endpoint failed; it records that these results could not be presented through this page load.

## Preserved behavior and remaining limits

The API's request URLs, options, logging, successful-response normalization and Promise handling remain exact. The page's effects, request ordering, refresh handler, loading flags, state replacement and other panels remain exact. The completed active-contract availability implementation from #32125 remains intact in both shared source files, and its separate panel is not changed by this continuation.

Both new props default to false. Existing callers that omit them retain their previous behavior. A later successful result replaces the previous state object without the failure flag, restoring the ordinary populated or empty display.

The Refresh button was already present and calls the existing load function. This patch does not add automatic retry, cancellation, latest-request ownership, a new API request or an endpoint-specific retry mechanism. Loading branches retain their previous precedence and skeletons. During an existing refresh, the page retains its existing display behavior until the response is applied.

Successful malformed data remains subject to the current normalizers. A successful top-contract payload whose contracts value is not an array is still converted to an empty array. Contract-call normalization may filter rows or return an empty array for a shape it does not recognize. Those are not newly classified as unavailable. There is no new schema validation, finiteness rule, authenticity check or guarantee that a returned empty set proves no network activity.

The chart still maps dates and calculates its total, latest and peak values as before; its populated rendering is unchanged. No chart computation, browser layout, user interaction or export was executed.

## Exact source composition

Canonical donor remains [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at `482ee456369418ef82c4056718cb82d3468f762b`.

The API and route preimages below are the complete retained postimages from #32125, not a reconstructed application of its accepted patch. Their public recovery locators were already acknowledged in checkpoint manifest `c6799624308a7875bc42add05bc845345d9bb772` in woahwhattheheck/commons. This continuation did not reacquire or re-execute that accepted source correction.

The two child components were newly fetched in full at the canonical donor for this actual caller review. Each native file SHA matched its independent UTF-8 Git blob identity.

| Production path | This patch preimage | Bytes | This patch postimage | Bytes |
| --- | --- | ---: | --- | ---: |
| src/lib/soroban-api.ts | `30fda2ab0e697c3edc64da7e7c836dd1bc22f4c5` | 8972 | `05f0966bb312ce10e736992d85dd83ceb7e64c66` | 9206 |
| src/app/[locale]/soroban/page.tsx | `617360329cf2f722fdd1d38b929ff39d0497e668` | 6136 | `d3bd13f0d05f967de8bb5f52a8a9328b34071e7a` | 6273 |
| [src/components/soroban/TopContractsTable.tsx](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/components/soroban/TopContractsTable.tsx) | `dc578372c7d69fbf6af5f4d7d4eb7f01c3fc71f9` | 4674 | `85c6bb47446fecb0a3e6a3b290bfd4a64737906d` | 4939 |
| [src/components/charts/ContractCallsChart.tsx](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/components/charts/ContractCallsChart.tsx) | `f774ac5797f96ecf69e1cc3f89c44b533825dba0` | 6618 | `d36e06e5ff150e852e5f982f309ae86a5856861e` | 6668 |

Patch identity: `8ecc1cb2de5dd57652ba80e24078b2ceb17c4213`, 6680 UTF-8 bytes.

Apply #32125 first, then this patch. Applying this continuation directly to the original canonical API/page is not the documented input. The earlier patch, README and three original MIT notices remain unchanged in this directory. Their attribution, source/instruction-custody qualifications and original notice text continue to apply. No broader repository licensing or authorship determination is made.

The canonical API path history and relocation attribution were recorded in #32125. This continuation does not present an old summary as a newly acquired complete repository tree. No original instruction tree or lost earlier wallet source was reconstructed.

## Verification and overlap

Each newly selected replacement had one match, and reversing the selected replacements restored every original byte. The newly serialized unified diff was parsed for exact file headers, coordinates, context lines and row counts. Forward application reproduced all four intended full postimages, and inverse application restored all four exact preimages. These were source-string operations, not application or test execution.

The preserved API active-contract interface, catch, and successful normalization were outside every new replacement; the completed active panel source is untouched. The page's active-contract fallback and prop remain as published by #32125. Every other byte in all four edited files stays unchanged.

A second seat reviewed the transferred four-file contract without provider calls or execution. It found the failure/empty distinction coherent, called out unavailable precedence and recovery on successful response replacement, and preserved the aggregate-catch and existing-retry limitations. It did not independently inspect JSX placement or hook ordering.

A new dedicated Commons PR search for Soroban, TopContractsTable and unavailable returned zero results. The preceding active-count packet and its scope are explicitly preserved. This bounded search is not proof of global uniqueness or a new ownership claim.

No compiler, fixture, tests, browser, chart calculation, export, application API request, contract call, transaction, workflow or upstream mutation ran. This is an attributed Commons source continuation, not a deployed fix, upstream acceptance, complete dashboard reliability claim, bounty completion or payment entitlement.
