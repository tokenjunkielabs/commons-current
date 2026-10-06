# Own row-selection detail requests

A ranking click changes the selected asset before its history and insights arrive. Previously the old details remained visible beneath the new asset heading, and any completed row-click request could replace the details or clear the loading flag for a later click. A rejected Promise.all also left the handler without its own failure or completion branch.

This incremental patch assigns a fresh identity to each row-click attempt, clears its prior detail data, and displays a pending or failure message. Only the current attempt can write its resulting history, insights, error and completion state. A cleanup invalidates pending row-click identities. The existing initial page-loading effect is deliberately separate and unchanged; this is not a whole-page request-lifecycle guarantee.

Apply the existing #32126 supplied-metrics patch, then #32131 selected-issuer patch, then own-selected-asset-details.patch. Earlier artifacts and notices remain unchanged. This guide supersedes their unchanged-row-click-loader caveat only within the scope described here.

## Source and actual caller

Canonical source is Stellar-Analysis/frontend at `482ee456369418ef82c4056718cb82d3468f762b`. The complete route, helper and both connected detail children were acquired for #32126 and remain in current custody. The exact composed #32131 postimage is the preimage here. No accepted source was reconstructed after the earlier unrelated cache loss.

| Source | Git blob | UTF-8 bytes |
|---|---|---:|
| src/app/[locale]/trustlines/page.tsx, after #32131 | `784ff722087f425f165090bb7760d5ff57fb7fa7` | 14583 |
| Proposed route postimage | `1eb0811966f046ebac6c39d4f45477e1ba49ad08` | 15754 |
| src/lib/trustline-api.ts, unchanged | `6ff2791be6f5997b5ab3c1b49f666d100e1be414` | 3116 |
| src/components/charts/TrustlineGrowthChart.tsx, unchanged | `77aba5b486e459f7fe1c73954eae0b5553e3c4db` | 7260 |
| src/components/trustlines/AssetInsights.tsx, unchanged | `4197442b800e0a247c4d42a0e950f4237a56c5b4` | 2945 |

The actual ranking button invokes handleSelectAsset with its row's TrustlineStat. Both existing detail calls receive that row's asset_code and asset_issuer. The selected heading and distribution are based on selectedAsset, while the chart and insight child receive separate history and insights state. That separation makes retaining earlier details under a newly selected heading a concrete source-level mismatch.

The ordinary initial render shows a page-level loading screen until the existing loadData effect completes. It separately writes stats, rankings, selectedAsset, history and insights. This patch leaves that whole effect byte-exact. It is not governed by the new row-click token.

## Request and presentation sequence

The handler creates a new object and installs it in a component-local ref before changing state or invoking either existing helper. It then updates selectedAsset, clears history and insights, clears the prior selection-error flag, and sets the existing detail loading flag.

The same two helper calls remain inside Promise.all with the same asset arguments. After both resolve, the handler compares its captured object with the current ref before writing either result. A later click replaces the ref immediately, making older row-click results ineligible.

A rejection from the current attempt sets selectionError and logs through the already imported logger with a fixed message. An obsolete attempt's catch returns without writing state or logging that new handler-level message. Its finally still runs, and performs its own identity check before clearing loading. Thus an obsolete completion cannot end the newer row-click pending state. Existing logging inside the unchanged helpers is outside that admission check.

The new effect cleanup sets the ref to null. Row-click continuations arriving after that cleanup fail the identity check. This does not cancel a request, interrupt a continuation that already passed its check, or establish the instant of a navigation click as the cleanup boundary.

The detail area renders one of three branches:

| Detail state | Presentation |
|---|---|
| Current row-click attempt pending | Loading selected asset details... |
| Current row-click attempt rejected | Unable to load details for this asset. Select it again to retry. |
| No pending or selection-error flag | Existing chart and insight markup with their existing props |

The same enabled ranking button provides retry. The asset heading, supply and distribution remain visible from the selected ranking record. The chart and insight subtree is conditionally absent while pending or failed, and mounts again in the normal branch; no preservation of transient child/widget state is claimed. English copy follows the current route's existing literal-copy style. No live-region, screen-reader announcement, layout or full-accessibility behavior was tested or asserted.

## Primary lifecycle contract

The official [React useRef reference](https://react.dev/reference/react/useRef) says that the same ref object persists across renders, its current value can change without rendering, and event handlers or effects can read/write it. The patch keeps the request identity in that ref and visible pending/failure/data values in state.

The official [React useEffect reference](https://react.dev/reference/react/useEffect) describes cleanup after component removal and the extra development setup/cleanup cycle. The guarantee here starts after the added cleanup executes. It does not claim that all asynchronous work on this page stops.

Both official pages were successfully read during this qualification. Their displayed documentation version is19.3; that is not a claim about this repository's installed React version, compiler output or runtime. The current source uses ordinary top-level hooks, with the new ref accessed in the handler and cleanup rather than render.

## Exact patch checks

own-selected-asset-details.patch is3445 UTF-8 bytes, Git blob `27fc82787f5f8cd1a90ff67ab709a644e1e13a96`. It adds50 and removes15 lines in four hunks containing92 complete serialized rows.

The actual serialized patch was applied forward and inversely to the full retained strings; both exact expected images were reproduced. All rows are included without truncation. Reversing only the four authored replacement regions reconstructs every other byte exactly. The original loadData effect is separately identical. The normal-branch chart and insight markup matches the earlier markup after its four-space indentation change, with the same props. The #32131 code-and-issuer predicate is intact.

An unpublished first draft omitted the closing JSX expression brace in the new conditional. Static inspection caught and corrected that local transcription before the final patch, spec, checkpoint or publication; no application execution or provider replay was involved. The retained final diff contains the closing brace.

A peer reasoned only from the supplied token/catch/finally/cleanup description and found no concrete ordering concern within that bounded scope. It did not review the source or execute it, and was not an approval gate.

## Explicit limits and attribution

The unchanged initial loadData effect can still update shared selectedAsset/history/insights state independently, including from overlapping development effect instances or after unmount. The new token governs only row-click requests. It does not prove that every possible writer on the page obeys the selected identity. A whole-page lifecycle correction would require a separately qualified change to that initial path.

The unchanged helper resolves some failures as empty history or null insights. Such outcomes are fulfilled results and reach the normal child empty-data behavior, not the new rejection branch. Because its JSON promise is returned without awaiting inside the helper's try, some parse failures can propagate to this new catch. No endpoint, return schema, fallback policy or partial-success policy changes.

Promise.all remains all-or-nothing at this handler. If one operation rejects, the other may continue; no network cancellation, abort signal or partial result is introduced. A helper that never settles still leaves the current attempt pending. If logging itself throws, finally still performs its guard, but no universal successful-handler-return guarantee is made.

The patch does not validate returned asset identities or data fields, change ranking order, improve distribution arithmetic, certify freshness, or establish a live issuer/account state. It does not change either earlier presentation correction. Original contributors retain credit, and the existing three exact notice files remain part of this directory.

A new dedicated Commons PR search for trustline, selected and request returned only #32126 and #32131, whose scopes explicitly left this loader unchanged. Parent retained no exact same-hunk completion or hold. These are bounded overlap observations, not a global absence proof or contributor reassignment.

Publication adds this guide and the patch only. Complete immutable strings, native and independently computed identities, final PR/paths/tree/ordered parents are checked. A predeclared main-equality alias is used only when observed main equals the verified merge/readback; otherwise both complete artifacts are read at one observed immutable main without chasing.

No application, helper, chart, formatter, API, account, wallet, trustline, payment, deposit, withdrawal, browser, compiler, fixture or test was executed. No upstream file, deployment or live data was changed. The held #32074 final-files route, earlier source losses and unpublished parked EmployeeList draft remain protected.
