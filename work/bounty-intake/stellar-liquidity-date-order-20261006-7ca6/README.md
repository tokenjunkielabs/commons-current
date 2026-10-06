# Order liquidity buckets before formatting their labels

## Connected source defect

The acquired Analytics route renders LiquidityChart with metrics.liquidity_history when metrics exists. The chart groups values by the existing date prefix obtained from point.timestamp.split('T')[0]. It then formats each bucket to an en-US month/day label, discarding its year, before reparsing those labels to sort the series.

That sequence makes chronological ordering depend on a yearless display string. It cannot retain the original year information. Formatting the date-only bucket without an explicit time zone also uses the host zone, which can display an earlier calendar day than the bucket key.

This patch sorts the original date keys first and formats those date-only keys with timeZone: 'UTC'. The existing buckets, sums and rounded values remain unchanged. This is a source-level correction supported by the acquired caller and language contracts; no live API response or browser incident was captured.

## Exact complete inputs

Donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/components/charts/LiquidityChart.tsx | 081fd5fc0829f7e8e98b17e483b19552b8c6e85a | 4332 |
| src/app/[locale]/analytics/page.tsx | 210bb00fd103fa1ca9a02ae7dedb14f4182aa9bf | 8438 |
| src/lib/analytics-api.ts | d3daf672cc780815418e3c7518ab4d2334c21796 | 23025 |

The complete route and API module were already retained as connected caller/type evidence. The complete chart was newly acquired at the donor pin and matched independently to its native blob.

Current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888. A relocation is not evidence of sole original authorship. The source attribution and three acquired upstream MIT notices remain preserved.

## Contract and scope

The [ECMAScript 2025 Date.parse specification](https://262.ecma-international.org/16.0/#sec-date.parse) defines ISO date-only forms without an offset as UTC. It permits implementation-specific handling for strings outside its specified date-time format and does not guarantee a portable round trip through a locale-formatted date label.

The [ECMA-402 DateTimeFormat initialization algorithm](https://tc39.es/ecma402/#sec-initializedatetimeformat) uses the system time zone when the timeZone option is absent and uses the requested valid zone when one is supplied.

These contracts support two changes in the same chart-data expression:

1. Sort the full original bucket keys with the existing Date/getTime numeric comparison before mapping to display objects. For valid ISO date-only keys this preserves chronological year information.
2. Specify UTC when formatting each date-only key. The visible month/day then describes that key's calendar day independently of the host's local time zone.

The original grouping still takes the textual prefix before T. This patch does not convert arbitrary timestamp offsets to global UTC days or redefine the aggregation's calendar policy. The label remains month/day, so different years can still have identical visible labels. The patch corrects ordering, not year-label disambiguation.

Malformed timestamps, nonfinite numeric inputs, invalid-date ordering and a broader ingestion schema remain outside this source change. No all-input behavior claim is made beyond the intended valid ISO date keys.

## Serialized change and preservation

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Component preimage | 081fd5fc0829f7e8e98b17e483b19552b8c6e85a | 4332 |
| Component postimage | 3d5ff3b3eed0dd8186c89871802452524c97b6e8 | 4341 |
| date-order.patch | 6b5d0956c3fa4af8a1f2f90e1bda5a170828c0fa | 793 |

The actual serialized unified patch contains one hunk and seventeen rows, with three additions and two deletions. Forward text application produced the complete postimage exactly; inverse application restored the complete preimage exactly. Restoring the changed chart-data expression reproduces every other source byte.

The full aggregation prefix, the complete currency-formatting function and all JSX remain byte-for-byte unchanged. Data grouping, corridor handling, summation, rounding, chart styling, tooltip configuration, export controls and imports retain their existing behavior. Commons #31964, #31967 and #31972 concern other source files and are not repeated or modified here.

Apply date-order.patch at the donor repository root to the exact preimage above. No Date expression, chart rendering, compiler, package installation, browser, API application request, fixture, test or workflow was executed. The checks establish source serialization and contract reasoning, not runtime or whole-build success.

## Notices and publication boundary

| Unchanged notice | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| upstream-licence-mclaughlin.md | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| upstream-license-menke-laguna.md | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| upstream-license-de-wet.md | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |

This is an attributed Commons source proposal. It is not an upstream change, deployment, acceptance or reward event. Bounded exact-name Commons and Slack queries returned no rows, with native END for Slack; internal custody checks found no retained same-hunk completion. Those observations do not establish global absence of other work.

Publication verification requires complete immutable bodies and native plus independently computed blob identities for all five artifacts, followed by final PR/files/merge/main metadata. If the observed main commit exactly equals the verified merge, the preselected equality alias can reuse the immutable bodies. Otherwise each artifact is read once at the observed immutable main commit. Actual publication evidence is recorded separately in the release and grouped completion index.
