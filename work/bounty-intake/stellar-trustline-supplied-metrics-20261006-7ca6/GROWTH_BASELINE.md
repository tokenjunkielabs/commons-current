# Avoid reporting a fallback percentage as trustline growth

TrustlineGrowthChart calculates a relative percentage only when its earliest historical count is positive. Otherwise growthPercent is set to zero, but the current markup still displays that fallback as a signed percentage with a growth-direction color.

This patch uses the same existing earliestTotal > 0 prerequisite for the percentage display. When the prerequisite fails, the growth value reads Unavailable in a neutral text class. When it passes, the existing sign, one-decimal percentage and direction color are preserved. Sorting, date labels, current count, chart data and arithmetic are unchanged.

Apply this incremental patch alongside the existing Trustlines source packet. It is the first change here to TrustlineGrowthChart; the route's #32126, #32131, #32135, #32138, #32141 and #32144 composition remains untouched.

## Acquired source and mounted caller

Canonical donor: Stellar-Analysis/frontend at `482ee456369418ef82c4056718cb82d3468f762b`. The complete chart, API helper and route were acquired for #32126 and remain retained. Current route and helper postimages are retained after #32144. No accepted source was reconstructed or reread.

| Production path | Preimage / UTF-8 bytes | Proposed postimage / UTF-8 bytes |
|---|---|---|
| src/components/charts/TrustlineGrowthChart.tsx | `77aba5b486e459f7fe1c73954eae0b5553e3c4db` / 7260 | `dfd20a698d14c4940abb8d826fa52218c12bc637` / 7509 |

The actual src/app/[locale]/trustlines/page.tsx imports this named chart and supplies data={history} with latestTotal={selectedAsset.total_trustlines}. Its current #32144 postimage is `5739dace8e22e0671039c8b6e88d017cb91dcb95`,16370 bytes. The helper's current postimage is `315f8082701f12df466c8fd5b76d7c81afd7137a`,3166 bytes; its TrustlineSnapshot and TrustlineStat declare the supplied count fields as numbers. The page and helper are not edited by this patch.

The chart first returns its existing no-historical-data panel if data is absent or empty. For nonempty data it copies and sorts the snapshots by snapshot_at, maps each total_trustlines field to total, and selects chartData[0]?.total || 0 as earliestTotal. It then calculates growth=latestTotal-earliestTotal and growthPercent=earliestTotal>0?(growth/earliestTotal)*100:0.

Thus zero is an implementation fallback when the existing ratio prerequisite fails. It does not by itself establish an observed zero relative change. The current display also chooses a sign and color from growth even on that fallback path.

## Bounded display policy

| Existing source condition | Result |
|---|---|
| Empty or absent history | Existing early empty panel, unchanged |
| earliestTotal > 0 | Original positive-baseline sign, toFixed(1) percentage and direction color |
| earliestTotal > 0 is false | Unavailable, with text-muted-foreground |

The percentage markup is wrapped in a conditional fragment. Its two original expressions are retained exactly apart from indentation. The class selection wraps the original growth >= 0 color expression in the same prerequisite, with a neutral class for the unavailable branch.

The original numeric calculations remain present and unchanged. This is a presentation correction rather than a new formula or data-cleaning rule. Current latestTotal display, chart points, axes, tooltips, legends, chart export control, layout classes and empty-history copy remain byte-for-byte unchanged outside the two edited regions.

The condition covers zero and negative earliestTotal values and any value already reduced to zero by the existing || 0 expression. It is not finite-number or runtime schema validation. A positive but nonfinite baseline or malformed latestTotal can still produce the existing invalid output. No new ordering, freshness, history-window or synchrony relationship between the ranking count and historical snapshots is established.

## Full-text verification

show-unavailable-growth-baseline.patch is1042 UTF-8 bytes, Git blob `4fb52c2569ae492b34411d4bd0e7c2e8594e45f3`. The patch adds11 lines and removes3 in one hunk with22 complete serialized rows.

Forward application of the actual serialized patch reproduces the full expected postimage, and inverse application reproduces the full preimage. Every hunk row is included without truncation. Reversing only the two authored replacement regions reconstructs every other byte. The complete sorting/mapping/formatting/arithmetic block is independently equal, and the original positive-baseline percentage markup is equal after its mechanical indentation change.

CI supplied a nongating retained-description check: reusing the same prerequisite for the text and neutral class is coherent, with positive-baseline behavior preserved. This was not a source, compiler or runtime review.

No chart, date parser, formatter, arithmetic expression, component, API request, browser, compiler, test, fixture or export operation was executed. No visual, assistive technology, layout or measured data claim follows from the static checks.

## Qualification and publication boundary

A new dedicated Commons PR query for TrustlineGrowthChart and baseline returned no entries. Root retained no exact same-hunk completion or hold; its #32142 date correction targets ContractCallsChart and older #31985 targets five other network charts. These are bounded custody and search findings, not a global absence or ownership claim. Earlier accepted corrections are preserved.

The existing directory's original contributor attribution and three exact notices remain. Publication adds only this guide and the new incremental patch, without changing prior artifacts or the upstream donor.

Both complete immutable artifacts are compared with prepared strings and native/independent Git identities. Separate final reads check PR identity, exact changed paths, merge tree and ordered parents. The predeclared main-equality alias applies only when observed main equals the verified merge/readback ref; otherwise both full files are read once at the observed immutable main, with no chasing.

No runtime, build, test, account, wallet, trustline, payment, deposit, withdrawal, API, export, clipboard, credential or upstream operation was performed. Existing whole-body/provider holds, #32074 final changed-files UNKNOWN, earlier cache-loss qualifications and the unrelated unpublished parked draft remain protected.
