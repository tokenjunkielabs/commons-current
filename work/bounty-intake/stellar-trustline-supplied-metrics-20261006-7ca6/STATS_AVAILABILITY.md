# Distinguish unavailable Trustlines overview metrics from zero

The current stats helper catches request failures and returns three zero counts. The mounted Trustlines route displays those values as ordinary metrics; it also displays zero when its stats state is absent after an initial load rejection. Neither path proves a reported count of zero.

This patch adds an optional unavailable marker to the existing helper fallback and displays Unavailable in the three overview count positions when stats are absent or explicitly marked unavailable. Successful results keep their existing count expressions, including actual zero values. The request URLs, fetch options, loading state and all current request-lifetime guards remain unchanged.

Apply after the existing #32126, #32131, #32135, #32138 and #32141 source patches in this directory. It edits the previously unchanged API helper and the exact composed #32141 route postimage. Existing artifacts and the three notices remain unchanged.

## Complete retained source and caller

Canonical donor: Stellar-Analysis/frontend at `482ee456369418ef82c4056718cb82d3468f762b`. The complete helper and route were acquired for #32126 and remain in current custody. The route's later postimages are retained from the published composition, with no accepted-source reconstruction or provider reread.

| Production path | Preimage / UTF-8 bytes | Proposed postimage / UTF-8 bytes |
|---|---|---|
| src/lib/trustline-api.ts | `6ff2791be6f5997b5ab3c1b49f666d100e1be414` / 3116 | `315f8082701f12df466c8fd5b76d7c81afd7137a` / 3166 |
| src/app/[locale]/trustlines/page.tsx | `1ceba2ed046441f3e01dd5cddbba84bd072c0b5a` / 16112 | `5739dace8e22e0671039c8b6e88d017cb91dcb95` / 16370 |

The acquired TrustlineMetrics interface declares total_assets_tracked, total_trustlines_across_network and active_assets as numeric fields. fetchTrustlineStats fetches the existing stats endpoint, rejects a non-OK status inside its try, and returns res.json() on its success path. Its catch logs the error and returns all three counts as zero.

The actual route initializes stats to null and loading to true. Its first Promise.all requests stats and rankings, then its active effect stores both results. It may subsequently load the first ranking's details. Its finally clears loading only while the effect is active. The loading branch suppresses the overview until then. Each overview count currently applies formatNumber to stats?.field || 0.

The request/caller relationship is established from complete source. No live response, count, account, trustline, endpoint or log event was inspected or generated.

## Exact producer and display contract

TrustlineMetrics gains optional unavailable?: boolean. Only the existing caught-error fallback gains unavailable: true; its three existing zero fields remain byte-for-byte unchanged. The successful return expression remains return res.json(), with no result normalization, schema validation, wrapper envelope or retry change.

Each overview count now checks that stats exists and stats.unavailable is not exactly true. If so, the complete original formatNumber(stats?.field || 0) expression is used. Otherwise the fixed text Unavailable is displayed in the same count container.

| Source state | Display in the three overview count positions |
|---|---|
| Existing helper catch returns its marked fallback | Unavailable |
| Route has no stats object after its initial load rejects | Unavailable |
| Successful stats object without the marker, or with marker false | Original expression for each count, including zero |
| Supplied object explicitly carrying marker true | Unavailable |

The optional marker is an additive source contract. Existing consumers can still access the original numeric fields; no claim is made that uninspected consumers interpret the new marker. The endpoint's successful JSON is still trusted by the existing code. A server-supplied marker true is therefore honored; this patch does not authenticate provenance or establish a reserved wire-schema field.

This is a display distinction. It does not manufacture replacement metrics, certify a successful response, prove freshness or change which request errors are swallowed.

## Loading, absence and lifetime boundaries

The route's full code preceding its main content return is unchanged, including imports, state, both effects, row selection, catches, finally guards and formatter. Initial loading still precedes the overview. #32138's effect cleanup ownership and #32135's row-click request ownership remain as published.

If the first Promise.all rejects, no successful tuple is committed and stats may remain null even if its independent stats request resolved. The unavailable display then reflects this route's lack of committed stats; it does not identify which request failed. If stats were already committed before a later detail request rejected, the available overview retains those committed counts.

The helper returns the JSON promise without awaiting it inside the try. A later JSON rejection can bypass that catch and reach the route's existing catch. That behavior remains unchanged and is not described as a marked fallback. Logging failures, malformed JSON shapes, null JSON and other unexpected values remain outside a general success guarantee. Existing numeric truthiness fallback and formatting behavior remain for unmarked objects.

No new state, request, timer, selection token, cleanup, cancellation or error handler is introduced. Rankings/history/insights empty and failure policies are outside this correction. Overview captions, styles, icons and labels remain unchanged; the patch changes only the three count values.

## Verification of the authored patch

mark-trustline-stats-unavailable.patch is 2392 UTF-8 bytes, Git blob `c9ad16069e746eebdd7c510534aea4cff97eecc9`. Combined source change: +11/-3 across five hunks with 44 complete serialized rows.

The actual combined serialized patch applies forward to both full expected postimages and inversely to both full preimages. All hunk rows are included without truncation. Reversing just the five authored replacement regions reconstructs every other byte exactly. The full route request/state/loading block is independently equal, and all three original successful count expressions remain literal in the new branches.

These are text and Git identity checks. No application helper, formatter, expression, request, browser, renderer, compiler, test or fixture was executed. Visual fit, localization, assistive technology output and whole-page behavior were not measured.

A new dedicated Commons PR query for trustline, stats and unavailable returned no entries. Root retained no exact same-hunk completion or hold. Both are bounded custody/search statements, not global absence, issue ownership or whole-feature acceptance.

## Attribution and publication boundary

Original contributors retain credit. The existing exact upstream notice files remain in this directory. Publication adds this guide and the incremental patch only, with no mutation to the donor repository or prior Commons artifacts.

Both complete immutable files are compared with their prepared strings and native/independent Git identities. Separate final reads check the PR, exact changed paths, merge tree and ordered parents. Observed-main equality is a predeclared alias only when main equals the verified merge/readback ref; otherwise both files are read completely at one observed immutable main without chasing later changes.

No API, account, wallet, trustline, deposit, withdrawal, payment, runtime, build, test, browser, credential or upstream operation was performed. Existing held routes, #32074 final changed-files UNKNOWN, prior cache-loss qualifications and the unrelated unpublished parked source draft remain protected.
