# Show unavailable settlement summaries when there are no observations

## Connected display problem

SettlementLatencyChart receives SettlementLatencyDataPoint[]. It chooses the final element as latestPoint and renders Median, P95 and P99 summaries using optional property access followed by an existing zero fallback. With an empty input array, the component therefore presents three zero-millisecond summaries although no latest observation exists.

The Analytics route mounts this component with metrics.settlement_latency_history and has no nonempty-array condition around that render. The API module declares that field as an ordinary array, which permits zero elements. This establishes a reachable source-level display case; it does not claim an empty live response was captured.

A measured zero remains meaningful input. This proposal uses the absence of observations, not the numeric value of an existing observation, to select the unavailable label.

## Complete input identities

Donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/components/charts/SettlementLatencyChart.tsx | 61cb5b29563c99a3aa165e8528764fed2a609591 | 5199 |
| src/app/[locale]/analytics/page.tsx | 210bb00fd103fa1ca9a02ae7dedb14f4182aa9bf | 8438 |
| src/lib/analytics-api.ts | d3daf672cc780815418e3c7518ab4d2334c21796 | 23025 |

The [complete chart source](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/components/charts/SettlementLatencyChart.tsx), caller and API type definitions are retained. The chart independently matches its native blob identity. Current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888; relocation is not sole-authorship evidence. All acquired source attribution and three unchanged MIT notices are preserved.

## Exact change

Each of the three existing JSX summary expressions receives the same outer selection:

```tsx
data.length === 0 ? 'N/A' : originalSummaryExpression
```

The patch retains each original nonempty expression byte-for-byte, including the optional access, existing zero fallback, rounding and millisecond formatter. It does not reinterpret a measured zero as missing.

| Input case | Summary behavior |
| --- | --- |
| Empty array | Median, P95 and P99 display N/A |
| Nonempty valid array | Original summary expressions use the same final element |
| Nonempty malformed array or non-finite fields | Existing behavior is unchanged |

This table is source reasoning, not an executed fixture suite. The chartData mapping and latestPoint assignment still run before the JSX selection. The patch neither sorts observations nor establishes that the final element is chronologically latest. It does not add finite-number checks, schema validation or a live-data guarantee.

## Serialized source checks

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Complete preimage | 61cb5b29563c99a3aa165e8528764fed2a609591 | 5199 |
| Complete postimage | 5eae4cf80d7e56c436f42a85907bfe04eb712c7c | 5283 |
| empty-summary.patch | ab2b019f48e888807bba0e451b39614327802aba | 1452 |

The actual unified patch has three hunks and twenty-four rows, with three additions and three deletions. Serialized forward application exactly produces the postimage; inverse application exactly restores the preimage. Removing the three outer empty-array selections restores every other source byte.

Date conversion, input order, median/percentile rounding, formatter, chart series, axes, tooltip, export button, headings and classes remain unchanged. The preceding #31980 empty TVL summary and #31972 corridor display packets affect separate components.

Apply empty-summary.patch at the donor repository root to the exact chart preimage. No component, data mapping, Date operation, Math.round, formatter, browser, compiler, fixture, tests or workflow was executed. Text checks establish the selected display branch and source integrity, not runtime behavior or whole-build success.

## Notices and publication boundary

| Unchanged notice | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| upstream-licence-mclaughlin.md | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| upstream-license-menke-laguna.md | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| upstream-license-de-wet.md | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |

Bounded exact-component/empty-scope Commons and Slack queries returned zero results, with native END for Slack. These observations do not establish global absence or acceptance.

This is an attributed Commons source proposal, with no upstream change or deployment. Publication verification requires all five complete immutable artifact bodies with native plus independent identities, followed by exact PR/files/merge/main metadata. An exact observed main-equals-merge identity may reuse those bodies; otherwise every artifact is read once at the observed immutable main pin. The actual result is recorded in the release and grouped index.
