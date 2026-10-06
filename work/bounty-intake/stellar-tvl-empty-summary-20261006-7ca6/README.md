# Represent an empty TVL history explicitly

## Connected presentation gap

The acquired Analytics route renders TVLChart with metrics.tvl_history whenever metrics exists. It does not require the history array to be nonempty. The acquired AnalyticsMetrics interface declares TVLDataPoint[] with timestamp and tvl_usd fields on each point; it does not impose a minimum array length.

TVLChart maps that array and displays Current, Average and Volatility summaries. Current falls back to a numeric zero when no last point exists. Average and Volatility pass their aggregate expressions directly to the currency formatter with no empty-history presentation. An empty history supplies neither a current observed value nor a meaningful observed average or range.

This patch gives all three existing summary value slots an explicit empty state: N/A. Each slot first checks whether chartData.length is zero. With any points present, its original formatter expression is retained exactly, including the existing current-value fallback and the existing definitions of average and volatility.

This is a source-level presentation decision for a permitted input shape. It is not a report of a captured live API response or a rendered browser incident.

## Exact complete source inputs

Donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/components/charts/TVLChart.tsx | b161a6f75434ec726f385a673ce0bf744a6716ba | 4673 |
| src/app/[locale]/analytics/page.tsx | 210bb00fd103fa1ca9a02ae7dedb14f4182aa9bf | 8438 |
| src/lib/analytics-api.ts | d3daf672cc780815418e3c7518ab4d2334c21796 | 23025 |

The complete chart, route and API bodies are retained. The chart's complete UTF-8 body independently matches its native blob. The route contains metrics && <TVLChart data={metrics.tvl_history} />, establishing the connected caller without assuming a live response.

Current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888. This does not establish sole original authorship. Three complete upstream MIT notices accompany the patch unchanged.

## Deliberately limited change

| History state | Summary presentation |
| --- | --- |
| Empty mapped array | N/A for Current, Average and Volatility |
| One or more mapped points | Each original formatter expression, unchanged |
| Supplied zero-valued observations | Nonempty branch remains selected; zero is not treated as absence |

The patch changes only the three JSX value expressions. It does not add an early return or alter the chart layout, data mapping, ordering, date labels, rounding, colors, tooltip, export control, imports or props.

The existing maxTVL, minTVL and avgTVL computations remain unchanged and still execute before render. This patch controls their empty-state display; it does not claim all intermediate values are finite, introduce data validation, redefine Volatility, change aggregation arithmetic or reduce computation costs. Nonfinite/malformed values in a nonempty array remain subject to the original behavior. The empty plot itself is also unchanged.

N/A follows the absence-of-observations distinction already used in the separate Top Corridors proposal (#31972). It avoids presenting an absent current observation as measured zero. No financial interpretation or estimate is introduced.

## Serialized patch and ordinary source checks

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Component preimage | b161a6f75434ec726f385a673ce0bf744a6716ba | 4673 |
| Component postimage | 78c5133614009693d1390b3c45e8345d3bd31728 | 4772 |
| empty-summary.patch | d15cad950836cd8d222e5db95acdc9e461dc65b5 | 1295 |

The actual serialized unified patch has three hunks and twenty-four rows, with three additions and three deletions. Forward text application exactly produced the postimage; inverse application exactly restored the preimage. Reversing the three replacements restores every other source byte. The complete nonempty branches and aggregate computations are unchanged.

Apply empty-summary.patch at the donor repository root to the exact preimage above. No aggregate/chart execution, compiler, package installation, browser, API application request, fixture, tests or workflow was run. These checks establish source serialization and branch preservation, not runtime or whole-build success.

A supplemental primary Math.max/Math.min lookup failed because the provider could not retrieve the oversized specification page. Those exact requests remain held and were not retried or acquired through another route. No contract from that failed lookup is claimed as evidence. The empty-state decision above is supported directly by the complete source's connected array shape and its three display branches.

## Related guide correction

The same publication corrects one field name in the earlier LiquidityChart guide from #31978: metrics.liquidity becomes metrics.liquidity_history, matching the acquired Analytics caller. Only that prose token changes; the liquidity patch, component identities and prior publication verification remain unchanged.

| Existing guide | Before blob | After blob | Bytes |
| --- | --- | --- | ---: |
| ../stellar-liquidity-date-order-20261006-7ca6/README.md | ee176b8a527484577c7fd699c03b57f8d622fdcf | 952ebcb9188c28bf2a6aeb41cc26777e6ada859d | 6014 → 6022 |

## Notices and publication boundary

| Unchanged notice | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| upstream-licence-mclaughlin.md | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| upstream-license-menke-laguna.md | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| upstream-license-de-wet.md | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |

This is an attributed Commons source proposal, not an upstream change, deployment, acceptance or reward event. Bounded exact-name Commons and Slack searches returned zero rows, with native END for Slack. Internal custody checks retained no same-hunk completion or hold. These results do not establish global absence of other work.

All six published artifacts require full immutable body comparison, native and independently computed identities and final PR/files/merge/main metadata. The preselected main-equals-merge alias may reuse verified immutable bodies only if the observed commit is exactly equal; otherwise all six bodies are read once at the observed immutable main pin. Publication evidence is recorded separately in the release and grouped index.
