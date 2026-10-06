# Preserve zero latency and represent an unavailable average

## Two connected presentation defects

The acquired Analytics route imports and renders TopCorridors with metrics.top_corridors whenever metrics exists. It does not require that array to be nonempty. CorridorAnalytics declares avg_settlement_latency_ms as an optional number; zero is a supplied measurement, not an absent value.

The component currently puts that number on the left of a JSX logical AND. At zero, the expression produces zero itself, so the labelled Lat span is not selected. The patch uses a boolean nullish-presence check. A finite supplied zero therefore uses the same labelled millisecond presentation as other supplied finite numbers. Missing undefined or null values remain omitted.

The average-success summary currently divides an initial-zero sum by the array length without an empty-list branch. With no corridors, that is zero divided by zero; the formatted output becomes NaN followed by a percent sign. The patch displays N/A for that case and evaluates the existing average expression only when the list is nonempty. It does not present an absence of observations as a zero-percent result.

These are source-level deductions from the acquired rendering path and permitted input shapes. They are not reports of a captured live API response or a reproduced browser incident.

## Exact complete inputs

The donor is [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/components/charts/TopCorridors.tsx | 84b27cbc6fd0e51db6b60eaafa8fd825280a6bc1 | 5954 |
| src/app/[locale]/analytics/page.tsx | 210bb00fd103fa1ca9a02ae7dedb14f4182aa9bf | 8438 |
| src/lib/analytics-api.ts | d3daf672cc780815418e3c7518ab4d2334c21796 | 23025 |

The complete route and API module were already retained and are used as connected caller/type evidence. The complete TopCorridors body was newly acquired and independently matched to its native blob. No prior artifact, calculation or application input was replayed.

The current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888. That relocation does not establish sole authorship of the original component. Source ownership and all acquired notices remain preserved.

## Rendering contract and chosen behavior

[React's conditional-rendering documentation](https://react.dev/learn/conditional-rendering#logical-and-operator-) explicitly identifies numeric zero on the left of logical AND as a rendering pitfall: the expression retains zero rather than selecting or omitting the intended JSX branch. A boolean guard addresses that exact issue. Here a positive-only condition would incorrectly hide a valid zero, so the condition checks absence instead.

The empty-average decision follows the arithmetic meaning of the summary: no observations provide no average. N/A appears without a percent sign. For a nonempty list, the same sum, divisor and toFixed(1) expression remain, with the same percent suffix. The change does not reweight success rates, validate API data, sort differently or infer any financial result.

| Input condition | Corrected presentation |
| --- | --- |
| Finite latency supplied, including zero | Existing Lat label, value and ms unit |
| Latency null or undefined | No latency span |
| Corridor array empty | Average-success value N/A |
| Corridor array nonempty | Existing average computation and one-decimal percent |

This table is source reasoning, not an executed fixture suite. Malformed or nonfinite input is not validated by this patch; no all-input equivalence claim is made for data outside the intended typed finite-number shape.

## Serialized change

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Component preimage | 84b27cbc6fd0e51db6b60eaafa8fd825280a6bc1 | 5954 |
| Component postimage | 086c19eeac723e10e72fdcf58454d42e86115d05 | 6034 |
| numeric-display.patch | 0db923115afa4ee454543e7ea79dfb9f35fde668 | 1481 |

The actual serialized unified patch has two hunks and eighteen rows, with four added lines and two removed lines. Forward text application exactly produces the complete postimage. Inverse application exactly restores the preimage. Restoring the two changed expressions reproduces every other source byte.

All sort/order/top-five behavior, totals, currency formatting, labels, CSS, imports, array copying and data inputs remain unchanged. Existing Commons #31964 and #31967 corrections affect separate Analytics/Heatmap files and are neither changed nor repeated here.

Apply numeric-display.patch at the donor repository root to the exact preimage above. No package install, compiler, browser, render engine, API application request, fixture, tests, workflow or upstream submission was executed. These checks establish source serialization and contract reasoning, not runtime or whole-build success.

## Notices and publication boundary

Three complete acquired upstream MIT notices accompany the patch unchanged:

| Notice | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| upstream-licence-mclaughlin.md | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| upstream-license-menke-laguna.md | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| upstream-license-de-wet.md | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |

This is an attributed Commons source proposal, not an upstream change, deployment, acceptance or reward event. Bounded exact-name Commons and Slack queries returned zero rows, with native END reported for Slack. Internal coordination found no retained same-hunk completion or hold. Those limited results do not establish global absence of other work.

The publication requires complete immutable bodies, native and independent blob identities for all five artifacts, and final PR/files/merge/main metadata. If observed main exactly equals the verified merge, the preselected equality alias may reuse those immutable bodies; otherwise each file is read once at the observed immutable main pin. Actual evidence is recorded separately in the release and completion index.
