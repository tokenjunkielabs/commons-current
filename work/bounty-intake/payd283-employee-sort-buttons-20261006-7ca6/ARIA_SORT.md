# EmployeeList: expose the active sort direction

The mounted desktop employee table already sorts its rows and displays a direction arrow. After the native-button correction in Commons #32014, its table headers still do not expose that state through aria-sort. This incremental source packet adds the attribute to the currently selected column header and leaves it absent on the other headers.

## Exact source and composition

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`.
Production path: `frontend/src/components/EmployeeList.tsx`.

| Stage | Git blob | UTF-8 bytes |
|---|---|---:|
| Original canonical source | 277684e5f87cabd72ff5aadd04299a5360fdf3e0 | 20441 |
| After acknowledged #32014 native buttons | 29fee53b3a74b52032d07700f91e6afc2b891f21 | 21006 |
| This incremental postimage | 9c62f3d3208cac07d47189e201fd9e6370627390 | 21671 |

Apply sort-header-buttons.patch from #32014 before expose-active-sort.patch. The retained original full source and acknowledged prior serialized patch were assembled locally; the resulting complete preimage matches #32014's declared postimage exactly. That composition is byte materialization, not a repeat of source acquisition, application execution or an old test. The old patch, README and license are unchanged.

The new serialized patch has 5 complete hunks and 55 rows, +20/-5. Its semantic additions are five attributes; the other changed lines split the existing one-line th tags into readable JSX. Whole forward application produces the exact postimage, whole reverse application restores the exact composed preimage, and removing only those new attributes/formatting restores every original byte.

## State contract

The retained module initializes sortKey to name and sortAsc to true. Activating the selected sort key reverses sortAsc. Selecting a different key changes sortKey and selects ascending order. The existing comparator reads these same state values for its numeric or string comparisons. No comparator, normalization, default, state setter or event handler is changed.

| Header | Existing key | New attribute when selected |
|---|---|---|
| Name | name | ascending or descending from sortAsc |
| Role | position | ascending or descending from sortAsc |
| Wallet | wallet | ascending or descending from sortAsc |
| Salary | salary | ascending or descending from sortAsc |
| Status | status | ascending or descending from sortAsc |

For each header the expression is sortKey === itsKey ? (sortAsc ? 'ascending' : 'descending') : undefined. Thus the selected header exposes the current direction; inactive headers do not receive an aria-sort value. Actions is not sortable and receives no new attribute. This is source reasoning over the actual state and render declarations, not a rendered accessibility-tree observation.

The [W3C APG sortable table explanation](https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/) places aria-sort on the active column's th, using ascending/descending and moving the attribute when the selected column changes. Its example retains native header buttons and warns that assistive-technology support needs actual validation. This packet uses only that semantic explanation; it does not copy or execute the example or claim its other caption/icon/focus features.

The existing directional glyph remains in the button's content and is not newly hidden from the accessibility tree. Button labels, focus styling and geometry remain those of #32014. No claim is made about an exact spoken phrase, announcement timing, an entire accessible table or WCAG conformance.

## Connected caller and contributor custody

The complete retained canonical App /employee route renders EmployeeEntry, which renders EmployeeList with its employee state and existing callbacks. The original source, full caller chain and exact tree entries were already acquired for the distinct native-button packet; they are reused here without another source fetch. No employee row, account or real user data was acquired or exercised.

The recent bounded issue283 metadata and comments remain only task context. Its one contributor comment was ranjeet150's assignment request, not a grant. The retained PR283 query had no returned entries within its stated bound; that is not a global ownership census or a fresh absence claim.

A fresh PR581 metadata read still shows OPEN/unmerged waterWang head `82ce1281b0a8f7a014d8835df237f7ccd34d00e1`. The retained complete eight-path map at that unchanged head excludes EmployeeList. That mobile/layout carrier is preserved; its unrelated source is not imported. Test-titled PR588/589 source and bodies remain unexpanded. No contributor acceptance, sponsor approval, reward or upstream authority is inferred.

All other held routes and protected families stay held. The root seat retains no exact aria-sort completion in its own bounded custody; that absence is not an exhaustive search result or permission gate.

## Attribution and artifacts

Original PayD contributors retain credit. This packet supplies only expose-active-sort.patch and this note in the existing Commons packet directory. The full retained Apache-2.0 notice remains in the existing LICENSE file with Git blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`, 11357 bytes. It is not replaced or duplicated.

The established #32014 button geometry limits still apply: global 44px button minimums may affect layout, and header padding outside each button no longer invokes sorting. This follow-up changes neither CSS nor click target extent.

## Verification and limits

Validation consists of retained complete source reading, static state/caller/primary-contract reasoning, independent Git blob identities and exact serialized forward/reverse source composition. Both new artifacts are fully read at the immutable publication ref, then checked with final PR/path/tree/parent metadata. A fresh same-repository main equality may serve only as a separately declared alias to those complete immutable checks; otherwise both files are read completely at one observed main commit.

No React render, DOM, browser, keyboard, screen reader, comparator, employee/account action, compiler, package installation, fixture or test was run. There is no mobile sorting, sorting-algorithm correctness for every possible value, universal announcement, complete accessibility, issue acceptance or upstream change claim.
