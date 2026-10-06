# Align trustline overview claims with supplied metrics

This patch replaces an unsupported, always-positive network growth claim with the active-assets count already supplied to the page. It also removes issuer-verification wording and check-mark badges that are selected by rank position or rendered unconditionally. Requests, asset selection, returned values, chart inputs and insight inputs are preserved.

Source: Stellar-Analysis/frontend at `482ee456369418ef82c4056718cb82d3468f762b`, src/app/[locale]/trustlines/page.tsx. The actual route, API helper and connected chart/insight components were newly acquired as complete source bodies. This is a static source correction; no trustline or account operation was performed.

## Concrete mismatch

The third overview card currently displays the literal word Positive and says it is based on a rolling thirty-day average. Neither expression reads a statistic or computes a comparison. The actual TrustlineMetrics interface declares total_assets_tracked, total_trustlines_across_network and active_assets; it declares no aggregate growth comparison.

The second card says it monitors verified issuers. The actual TrustlineStat interface contains asset code, issuer and counts, but no verification field. The rankings list places a BadgeCheck beside each of its first ten rows solely because index is less than ten. The selected-asset heading always places another BadgeCheck beside the code. Those conditions do not establish an issuer-verification result.

This does not assert that a real issuer is unverified or that a backend could never have additional fields. It identifies what the acquired page actually uses to produce those claims. The patch makes no live-network or issuer-status finding.

## Resulting presentation

| Existing presentation | Proposed presentation |
|---|---|
| Growth Trend; literal Positive; rolling thirty-day average explanation | Active Assets; compactly formatted stats.active_assets using the existing zero fallback; Reported by data source |
| Monitoring verified issuers below the tracked-assets count | Assets in the supplied dataset |
| Check-mark icon for the first ten ranking rows | Asset code remains, without that icon |
| Check-mark icon beside every selected-asset heading | Asset code remains, without that icon |

The existing Activity icon replaces the removed upward-trend icon in the active-assets card. The two now-unused icon imports are removed. No other imports or icon instances change.

The active-assets count comes from the same existing fetchTrustlineStats result. The source helper already declares that numeric field and includes it in its error-fallback object. The patch adds no new request, formula, derived growth series or interpretation of what the server considers active. The other two overview values and the shared formatter are byte-for-byte unchanged.

The selected-asset chart and generated insight sentences remain separate source paths. Removing the unsupported global card does not remove a selected asset's existing history or insight computations. Their input props are untouched.

## Connected source evidence

| Acquired source path | Git blob | UTF-8 bytes |
|---|---|---:|
| src/app/[locale]/trustlines/page.tsx | `fa5bbbd6c2120c8be0e80f0f01b8f351889465bd` | 14748 |
| src/lib/trustline-api.ts | `6ff2791be6f5997b5ab3c1b49f666d100e1be414` | 3116 |
| src/components/trustlines/AssetInsights.tsx | `4197442b800e0a247c4d42a0e950f4237a56c5b4` | 2945 |
| src/components/charts/TrustlineGrowthChart.tsx | `77aba5b486e459f7fe1c73954eae0b5553e3c4db` | 7260 |

The page directly imports the acquired helper and both acquired children. The helper includes the exact public metric and asset record shapes, fetch calls and zero/empty/null fallbacks that bound this correction. Native source blob identities and independently computed Git identities match for all four complete bodies.

No browser route, data helper, request, chart, formatter or component was executed. No response, issuer record or account data was fetched.

## Exact patch

| Source path | Preimage / UTF-8 bytes | Postimage / UTF-8 bytes |
|---|---|---|
| src/app/[locale]/trustlines/page.tsx | `fa5bbbd6c2120c8be0e80f0f01b8f351889465bd` / 14748 | `3c40a527926a1c32f44b54d520cb96fc9b950128` / 14497 |

describe-supplied-trustline-metrics.patch is 2960 bytes, Git blob `aed9ea7b9a1fa34120474d42a7a2f78fb6ead5f9`. It adds five lines and removes eleven across five hunks and fifty-eight complete serialized rows.

Full forward application of the actual serialized patch reproduces the exact postimage. Full inverse application reproduces the exact preimage. Every hunk row is included without truncation. The complete state/request/selection block and the formatter block are separately equal, and the only diff rows are the nine intended replacements/removals. The helper and child files are not edited.

## Deliberate limits

The existing data-availability policy remains. The API helper converts some failures to zero metrics, empty arrays or null insights; its returned JSON promises can also propagate rejection. The page still uses its existing numeric fallback and does not distinguish a real zero from an unavailable metric. The new active-assets display inherits that limit; it does not certify current network activity, freshness or successful retrieval.

No backend definition of active, endpoint implementation, schema validation, provenance flag, rank ordering or issuer verification mechanism is added or certified. The replacement caption identifies a supplied count, not a measurement independently established by this patch.

The selected-row predicate still compares only asset code, and the selection loader still has its existing asynchronous ordering/error behavior. Those are separate source findings and are not silently changed here. The original empty, pending, error and unmount behavior remains, as do number formatting, history ordering, distribution arithmetic and all data-handler bodies.

Existing layout classes remain except for removing the unsupported icon elements and replacing the trend icon with Activity. There is no rendered layout, contrast, localization or whole-accessibility claim. English copy follows the retained page's current literal-copy style.

## Attribution and bounded custody

Original Stellar-Analysis/frontend contributors retain credit. Three exact notice files are preserved in this packet:

| Notice | Git blob | UTF-8 bytes |
|---|---|---:|
| upstream-licence-mclaughlin.md | `57740b9d4d86aedf5d518f2f363d5cf192c54127` | 1104 |
| upstream-license-menke-laguna.md | `af5411fa243cfcf2b61c79d081dbb6204e956041` | 1111 |
| upstream-license-de-wet.md | `4a766e268772888af5df56c3f6c608f68558b789` | 1080 |

Their full bytes came from the parent's earlier exact message transfer, including the first notice's CRLF line endings, and match all retained identities. This preserves the supplied notices without asserting a broader licensing conclusion.

A new dedicated Commons PR search for Stellar, trustline, growth and verified returned no entries. Root and CI retained no exact same-path prior hold/completion in their summaries. These are bounded observations, not a global absence proof, contributor reassignment or whole-task completion.

A cache loss earlier in this lane parked an unrelated unpublished PayD button-availability draft because its complete accepted preimage was gone. That draft was not reconstructed or published. This packet uses newly acquired, previously unacquired source bodies. Existing accepted deliveries, held routes and the #32074 final-files UNKNOWN remain protected.

## Validation and publication

Validation consists of the newly acquired complete source/caller/helper relationships, native plus independent identities, exact source diff and serialized forward/inverse text checks. No application, API, account, trustline, deposit, withdrawal, financial, browser, fixture, runtime, test or compiler action was taken. There is no upstream mutation, deployment or whole-feature acceptance claim.

Publication adds five new Commons artifacts: the patch, this guide and the three exact notices. Every complete immutable file is compared with its prepared text and native/independent blob identity. Final PR/path/tree/parent metadata is checked separately. A predeclared observed-main equality alias is used only when main equals the verified merge and readback ref; otherwise all five files are read fully at one observed immutable main commit, without chasing later commits.
