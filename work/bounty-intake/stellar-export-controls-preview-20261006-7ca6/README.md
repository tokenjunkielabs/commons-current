# Keep export metric choices focusable and report the actual preview count

The mounted analytics export page uses MetricSelector to choose columns and ExportPreview to show up to five generated rows. Each metric's native checkbox was styled with display:none, and the preview footer always said “Showing 5” even when its data slice contained fewer rows.

This source-only continuation changes those two child components together. Metric checkboxes remain native controlled inputs, visually hidden with sr-only, and their existing visual boxes receive a focus-within ring. ExportPreview derives one five-row slice for both its row mapping and displayed count.

## Source custody and attribution

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).
Immutable donor: `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete acquired source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/analytics/export/components/MetricSelector.tsx` | `7c2b2159a78423f1f85f4e0ebc84b734e38488f3` | 2,142 |
| `src/app/[locale]/analytics/export/components/ExportPreview.tsx` | `e3b8687c81f4db939ff21fe3d7fa2f9bdff7ba97` | 3,534 |
| `src/app/[locale]/analytics/export/components/DateRangeSelector.tsx` | `ebcf27a8797f46be0005155bcaec6d21c7dd0eb5` | 474 |
| `src/components/ui/TimeRangeSelector.tsx` | `2fba3d99670a0ae35cdb80cc97478a903352ca13` | 3,863 |
| `src/app/[locale]/analytics/export/page.tsx` | `e60172711db5a9f5cc5cf71ae924ab24da15c989` | 7,849 |

The full page source is retained from the preceding substantive page correction, [Commons #32115](https://github.com/woahwhattheheck/commons/pull/32115). That packet changes only demo-data/email presentation and leaves these child imports, props, generator and handlers exact. Its page postimage is `e99e9053fb420e73dd3884ecae4865247d76ac3c` / 7,984 bytes. This patch touches only the two child modules and preserves that completed page packet.

The two current native child path-history pages each returned christabel888's relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`. This attributes observed history, not original authorship of every line. Dedicated upstream PR searches for MetricSelector and ExportPreview each returned zero; dedicated Commons searches for MetricSelector plus checkbox and ExportPreview plus rows returned zero, as did the public Slack analytics/export/components query. These are bounded results, not exhaustive absence claims. No external assignment, source PR, eligibility or upstream acceptance is asserted.

## Actual caller and row contract

ExportPage owns the metrics array and passes handleMetricChange to MetricSelector. That handler updates the requested metric's checked value through the existing state updater. Each child checkbox already receives its controlled checked value and calls the supplied onChange with its metric ID and native checked state; its enclosing label provides the existing text association.

The complete DateRangeSelector forwards nullable start/end dates and onChange to TimeRangeSelector. Custom date inputs can pass null when cleared, and users can choose short ranges. The retained parent generator returns [] when either endpoint is absent and otherwise constructs a dense array of dated sample rows. Thus fewer than five preview rows, including zero, are supported by this actual caller chain. No date control, generator, storage, export helper or browser was invoked to establish that source relationship.

## Exact correction

`focus-metrics-and-count-preview.patch` is **+6/-5 across six hunks in two production files**.

| Source | Before blob / bytes | After blob / bytes |
| --- | --- | --- |
| MetricSelector.tsx | `7c2b2159a78423f1f85f4e0ebc84b734e38488f3` / 2,142 | `53a3c059fe7203e3ae1e38cb4c4b5636ab518a51` / 2,190 |
| ExportPreview.tsx | `e3b8687c81f4db939ff21fe3d7fa2f9bdff7ba97` / 3,534 | `99490ae5dc1bc773737a5bb24e727e58fcbd934b` / 3,588 |

MetricSelector changes hidden to sr-only on the native checkbox and adds focus-within:ring-2 plus focus-within:ring-blue-500 on its existing visual container. It introduces no custom keyboard handler, ARIA checkbox emulation, tab index or new selection state. The label, checked binding, onChange, Select All callback, icons, ordering and all other classes remain exact.

ExportPreview sets previewRows = data.slice(0, 5), maps that same variable, and displays previewRows.length in the footer. Its caption now says “Up to 5 rows of export.” The data order, five-row cap, selected columns, cell formatting, units, existing keys and no-metrics early return remain unchanged. The source claim concerns the acquired dense parent data, not arbitrary sparse arrays or malformed row schemas.

## Primary utility contract and dependency limits

The successfully read primary [Tailwind display documentation](https://tailwindcss.com/docs/display) defines hidden as display:none and documents sr-only as visual hiding without removing content from screen readers. The successfully read [Tailwind state documentation](https://tailwindcss.com/docs/hover-focus-and-other-states) documents focus-within styling when the element or one of its descendants has focus. The patch uses those utilities on the existing native control and visual container.

Root transferred retained manifest/lock facts: package `2b1c6ac1f83096666c7fd6d5ba3fd22780e6b8eb` / 3,119 bytes declares tailwindcss 4.1.18 and @tailwindcss/postcss ^4. Lock `7ecba249d1b7cd41e629e2fff2782ed6805186f5` / 359,885 bytes resolves direct tailwindcss 4.1.18 and @tailwindcss/postcss 4.3.3, which also brings tailwindcss 4.3.3 transitively. These are declared/locked facts, not installed dependency or generated-CSS evidence. The primary pages are current documentation, not a version-pinned build result.

## Validation and scope

Full acquired source identities and UTF-8 counts matched independently. The serialized patch reconstructs both complete postimages; its inverse reconstructs both complete preimages. Exact source comparisons preserve each controlled checkbox callback and the preview's complete cell-formatting block. No application code, date generator, fixture, test, build, browser, screen reader, export, download, clipboard, print, email, network request or user data was exercised.

This proposes focusable native controls and corresponding focus styling; it does not certify generated CSS, color contrast, device behavior, every label structure or whole-page accessibility. Date parsing, timezone/DST behavior, preset inference, range validation, export failures and output metadata remain unchanged. Parent demo-data/email disclosure stays intact; this patch does not implement live reporting.

The complete donor tree has no AGENTS/RULES paths. Its known contributing document is EventSource-specific test/npm release guidance; this authorized source-only continuation does not execute that workflow. Three differently attributed documentation MIT notices do not establish repository-wide licensing. This Commons packet contains only the minimal attributed patch and this original guide. Existing ownership, completed work and exact failed-route holds remain preserved; no upstream action is taken.
