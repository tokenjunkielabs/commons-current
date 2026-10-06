# Match the selected trustline asset by code and issuer

The ranking list uses an asset's code and issuer for its key and detail requests, but its selected-row predicate compares only the code. If two supplied records share a code and have different issuers, selecting either record applies the selected styling to both rows. This patch adds the issuer equality to that predicate.

This is an incremental source correction after Commons #32126. Apply describe-supplied-trustline-metrics.patch first, then match-selected-asset-issuer.patch. The earlier patch, README and three notice files remain unchanged. This guide supersedes only the earlier README's statement that the selected-row predicate remains code-only.

## Actual connected source contract

The complete canonical route and helper were newly acquired at Stellar-Analysis/frontend commit `482ee456369418ef82c4056718cb82d3468f762b` for #32126 and remain in this lane's current source custody. This continuation consumes their retained full text and the exact accepted #32126 postimage; it does not reconstruct lost pre-reset source.

| Source | Git blob | UTF-8 bytes |
|---|---|---:|
| Original src/app/[locale]/trustlines/page.tsx | `fa5bbbd6c2120c8be0e80f0f01b8f351889465bd` | 14748 |
| src/lib/trustline-api.ts, unchanged | `6ff2791be6f5997b5ab3c1b49f666d100e1be414` | 3116 |
| Route after #32126, this patch's preimage | `3c40a527926a1c32f44b54d520cb96fc9b950128` | 14497 |
| Route after this patch | `784ff722087f425f165090bb7760d5ff57fb7fa7` | 14583 |

TrustlineStat declares both asset_code and asset_issuer as strings. The route's ranking button key includes both fields. Clicking the button passes the complete asset record to handleSelectAsset, which sets selectedAsset and supplies both fields to fetchTrustlineHistory and fetchAssetInsights. Each helper includes the encoded code and issuer in its existing request path. The selected detail header also renders both fields.

In contrast, the original isSelected expression compares only selectedAsset.asset_code with the row's code. That boolean drives the existing selected background/border and the chevron color. No other consumer of isSelected appears in the acquired complete route.

The new conjunction compares both existing string fields with strict equality. It adopts the route's current pair identity without adding an issuer parser, normalization, registry lookup or network verification. The illustrative same-code/different-issuer condition is derived from the source contract; it is not a claim that a live response contained such rows.

## Exact edit and validation

match-selected-asset-issuer.patch is 697 UTF-8 bytes with Git blob `5140ba25c40fbfd67d03fed13d0291c9dc668d7c`. It adds three lines and removes one in a single hunk containing ten complete serialized rows.

The actual serialized patch was applied forward to the full retained preimage and inversely to the full postimage. Both complete strings match exactly. All hunk rows are present without truncation. The full prefix before the predicate and suffix after it are separately identical, including every data request, handler, state declaration, render branch, visible label, class expression, key and child prop. The state/request block was also compared separately.

A peer checked only the supplied description of the identity contract and found no concrete concern. That reasoning is not an independent source review, execution result or approval gate. No component, helper, formatter, request or JSX was executed. No runtime, compiler, test, browser or accessibility behavior was observed.

## Behavior and limits

For well-typed records, a row receives the existing selected styling only when both fields equal those of selectedAsset. Rows with the same code but different issuers no longer qualify solely because their codes match. An identical duplicated pair can still match more than one row; no unique-record guarantee, deduplication or key-collision correction is introduced.

All original string comparison semantics remain. There is no case folding, trimming, validation or special native-asset policy. The acquired helper's TypeScript shape is the source contract, not a runtime response validator.

This edit does not associate asynchronous detail results with their originating request. The selection loader still sets the selected record before awaiting its history and insights, retains its existing prior-data/loading behavior and can receive responses out of order. Its existing rejection, logging, cleanup and unmount behavior remains. The initial loading path is unchanged.

This edit does not add an accessible selected-state attribute, a new keyboard pattern or a modal behavior. It retains the current native buttons and their existing styling expressions. No broad accessibility or rendered-layout claim follows.

The earlier supplied-metrics correction remains intact. Active-assets counts still inherit the existing zero fallback, and the helper's zero/empty/null fallback and returned JSON promise behavior are unchanged. A supplied count or issuer string is not a verified live network observation.

## Attribution, custody and publication

Original Stellar-Analysis/frontend contributors retain credit. The exact three notice files already in this directory remain part of the packet; their identities are recorded in the unchanged #32126 README. No broader licensing conclusion is asserted.

A new dedicated Commons PR query for trustline, issuer and selected returned only #32126, whose accepted scope explicitly preserved this predicate. Parent custody was consulted independently. This is bounded overlap evidence, not a global absence finding or ownership transfer.

Publication adds only this guide and the incremental patch to Commons. It does not update the upstream application or make an account, trustline, wallet, payment, deposit, withdrawal, data or API operation. There is no feature acceptance, deployment or issue-completion claim.

Every complete immutable artifact is compared with the prepared string and native/independent Git identity. PR metadata, complete changed paths, commit tree and ordered parents are checked separately. The main-equality alias is predeclared: it is used only if observed main equals the verified merge and immutable readback ref; otherwise both artifacts receive one complete read at the observed immutable main commit without following subsequent movement.

The unrelated unpublished EmployeeList draft remains parked after its source-cache loss. The earlier #32074 final changed-files route remains held and UNKNOWN. Neither is reacquired or replayed for this continuation.
