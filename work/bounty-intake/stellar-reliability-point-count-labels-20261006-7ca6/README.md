# Label reliability selections by point count

The acquired ReliabilityTrend chart labels its controls 7d, 30d, and 90d, but its selector sorts the supplied timestamps and takes the last 7, 30, or 90 array entries. It does not compare a date cutoff or otherwise select elapsed-day intervals.

This patch describes that existing operation directly: the explanatory copy becomes “Latest data points by record count”, and the control text becomes “7 pts”, “30 pts”, and “90 pts”. The internal values, state, timestamp sorting, slicing, chart data, axes, and tooltips remain unchanged. No sampling cadence or new time-window policy is introduced.

## Exact source

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).

Donor commit: `482ee456369418ef82c4056718cb82d3468f762b`.

| Source | Git blob | UTF-8 bytes | Custody |
| --- | --- | ---: | --- |
| `src/components/charts/ReliabilityTrend.tsx`, preimage | `cb63cdf9f5b7dacbfcf212350d8fec849b7c785e` | 3,950 | Complete immutable native source read for this task, independently hashed |
| Same component, postimage | `a2272108fce1321b24cffd93bfad3c8d832c3188` | 3,973 | Two exact presentation edits, +2/-2 |
| Caller `src/app/[locale]/anchors/[address]/page.tsx` | `71fea1bb40c29bcbba0657ba1cb10a65d35fab23` | 7,297 | CI's retained full caller; exact import/data/render excerpts transferred |
| `src/lib/api/types.ts` | `eb5891a5f04e33eb29757cf57c623f9b7d4ab3b5` | 3,140 | CI retained source; exact relevant interface/field transferred |
| `src/lib/api/anchor.ts` | `4c0b6ee29936b17fe97944bc818d460d8ff37c44` | 4,244 | CI retained source; complete getAnchorDetail function transferred |

The native blob read returns content without a separate response SHA. Its request-bound blob and independent Git identity match; no additional native identity field is invented. Caller/type/adapter rows identify the supplying seat's retained source and the transferred excerpts. Those complete modules were not reacquired or independently rehashed in this lane.

The bounded current-path history query at the donor returned only commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888, for repository-root relocation. That returned history is not proof of sole authorship or complete pre-relocation history, and its build claims were not rerun.

## Actual connected behavior

The acquired chart receives `ReliabilityDataPoint[]`. The transferred type is `{ timestamp: string; score: number }`; AnchorDetailData contains `reliability_history: ReliabilityDataPoint[]`. Those declarations establish neither daily spacing nor timestamp grammar, timezone, score units, or a score range.

The actual anchor-detail route imports this chart. After its loading/error branches, it renders `<ReliabilityTrend data={data.reliability_history} />` from the result of getAnchorDetail(address). The transferred adapter returns the selected api.get result without a local cadence transformation. This is source-custody evidence of a mounted consumer, not a backend validation or live API claim.

Inside the complete chart, filteredData copies and sorts the input, maps the selected internal value to 7, 30, or 90, then returns `sortedData.slice(-days)`. Consequently the selector caps the number of returned records; when fewer records are supplied, fewer are shown. No invariant in the acquired component enforces one record per day. The labels should therefore describe point counts without promising a duration the selection code does not calculate.

The display-only replacement is `window.replace("d", " pts")` for the unchanged literal union and control list. It does not evaluate timestamps, alter the stored selection, rename the interface, change the default, or transform scores. The explanatory line supplies the meaning of the abbreviated button unit.

## Boundaries and composition

Both changes are in this component's heading/control presentation. The complete useMemo selection body is byte-exact, as are imports, props, internal 7d/30d/90d values, dependency list, state updates, active styling, dimensions, Date-based ordering/formatting, gradient, series, tooltip, and axis settings.

No elapsed-day cutoff, clock, timezone, aggregation, resampling, interpolation, missing-date policy, score calibration, or additional API request is added. Timestamp validity, backend cadence, rendering at particular widths, accessibility acceptance, and actual chart output were not established by this source-only task.

Root's prior anchor helper/table/card simulated-trend labels concerned a different random makeMiniTrend path. Root and CI retained no exact same-component completion or hold; that is bounded coordination evidence, not a global ownership or completion claim. This packet neither replays those accepted changes nor republishes their source.

## Validation and delivery

The complete child source, actual caller/type/adapter excerpts, and bounded path history were inspected. Exact replacement reversal restores the complete child preimage; exact hunk text checks and Git blob/UTF-8 identities bind the patch and postimage. No component, sort/slice operation, data fixture, API, chart, browser, compiler, typecheck, lint, test, workflow, build, or executor was invoked. There is no whole-build, visual, performance, backend, or runtime acceptance claim.

The deliverable is patch plus guide. A repository-wide license scope has not been established by the differently attributed retained notices, so the full donor component is not republished. Existing attribution remains in [the earlier generator packet](../stellaranalysis-issue-generator-layout-20261006-7ca6/). CI supplied the unexamined child locator and the exact connected caller/type/adapter evidence. No upstream claim, submission, account, payment, or permission action is included.
