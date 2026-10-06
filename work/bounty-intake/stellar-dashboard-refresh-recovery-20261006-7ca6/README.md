# Restore dashboard results and preserve prior state

The mounted dashboard had two distinct state boundaries: successful automatic refreshes left an old page-wide error visible, and a live corridor update changed an object still shared with the prior React state. The two ordered patches below correct those source paths while preserving the existing data and refresh policies.

## Complete source and caller evidence

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/dashboard/page.tsx` | `cca99335ba0ae1f66a1fb5cea0197f5ead6b2f11` | 13,126 |
| `src/hooks/useDataRefresh.ts` | `4cb937ecb129bf4bf88893721b8d15a5bbc3e3b0` | 4,565 |

DashboardPage is an actual client App Router entry. It holds DashboardData in React state, passes fetchDashboard to useDataRefresh, and passes onCorridorUpdate to useRealtimeCorridors. Its local data type declares a nested kpi.successRate object with value, trend and trendDirection fields.

The original complete page and hook inputs were acquired for the new recovery investigation. The recovery postimage is reused as the input to the independent nested-state correction, not revalidated through another donor read. Hook lifecycle work is a separate continuation owned by the infrastructure lane.

## Apply the two patches in order

| Patch | Source preimage | Source postimage | Change |
| --- | --- | --- | --- |
| `clear-recovered-dashboard-error.patch` | `cca99335ba0ae1f66a1fb5cea0197f5ead6b2f11`, 13,126 B | `0748c045e1edaf7a7adba4198980134376146025`, 13,146 B | +1/-0 |
| `copy-dashboard-success-rate.patch` | `0748c045e1edaf7a7adba4198980134376146025`, 13,146 B | `f1944160ad5c8e97958dc44153b0b826a514ee8a`, 13,266 B | +7/-1 |

Both patches target only `src/app/[locale]/dashboard/page.tsx`. Apply the recovery patch first, then the nested-state patch. The first patch's artifact is unchanged from [Commons #32054](https://github.com/woahwhattheheck/commons/pull/32054).

## Successful refresh recovery — completed #32054

fetchDashboard fetches /api/dashboard, rejects non-OK responses, awaits response.json and stores the result. The initial effect catches failures into error and finally sets loading=false. The page checks loading, then error, then data.

Before these render returns, useDataRefresh starts its countdown. Its timeout invokes the same fetchDashboard even while the error view is rendered. The original successful refresh updated data without clearing error, leaving the failure view in place. The first patch adds setError(null) after the successful data update. It does not clear error at request start or on failure.

Initial error classification/logging, retry/countdown policy, loading state, lastUpdated, manual refresh, response assumptions and translation dependencies remain unchanged. The separate analytics-page #31964 correction is a different path.

## Nested live-state replacement — new continuation

The existing onCorridorUpdate callback returns early for absent data, creates `updatedData = { ...prevData }`, and checks `update.success_rate !== undefined`. Its original assignment through updatedData.kpi.successRate.value writes into the same nested successRate object referenced by prevData.

The second patch replaces only that assignment. It installs a new kpi object on the already-new outer object and a new successRate object inside kpi. Both spreads preserve the other existing fields; only value receives the same incoming success_rate. The previous state's nested objects are not written.

[React's primary guide on updating objects in state](https://react.dev/learn/updating-objects-in-state) explains that object spread is shallow and that an update to a nested value requires new objects at the changed levels. It also distinguishes mutating a newly created local object from changing an object already held in state. That contract supports assigning the new kpi object to the fresh outer copy.

The existing undefined guard is exact, so a provided zero still follows the update branch. With no success_rate, the original outer-copy behavior remains. Other KPI objects and the corridors/liquidity/assets/settlement references are preserved. A retained exact hook excerpt from the infrastructure lane confirms that useRealtimeCorridors invokes onCorridorUpdate after its existing isCorridorUpdate check. The original hook pin is e7c2a3e42b08f1c7de1135395712b450d3fb2353; its completed #32015 wrapper change preserves that handler body. No new parser or payload-schema guarantee is inferred from the type cast.

Logging, markUpdated, callback dependencies, hook options and all later source bytes stay unchanged. There is no new validation, aggregation, rate policy, timestamp interpretation or subscription behavior.

## Source-only validation and limits

For each patch, the complete serialized diff reconstructs the exact full postimage, and its inverse reconstructs the exact preimage. Independent UTF-8 byte counts and Git blob identities match. The second correction retains #32054's error-clear line exactly.

No application, request, WebSocket, timer, browser, synthetic fixture, test, storage or device operation was executed. No claim of full compilation, installed-library execution or deployed recovery is made.

The recovery change does not implement request generations, cancellation, stale-result handling or hook lifecycle ownership. The nested update assumes the existing DashboardData structure; it does not validate malformed response objects or event values. It preserves the original choice to place a corridor update's success rate into the dashboard KPI, without asserting that this is the correct aggregate metric. Simulated ticks are unchanged and are not reclassified as measured telemetry. No end-to-end concurrency or transaction guarantee is claimed.

## Attribution and scope

The retained bounded current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`. Earlier contributors retain their rights; relocation does not establish sole authorship. Scoped Commons/public Slack queries for fetchDashboard/error and separately DashboardPage/immutable returned zero. These are bounded overlap findings, not global completeness claims.

The complete donor tree had no root AGENTS/RULES paths. EventSource-specific contributing/release guidance does not override the explicit no-tests/no-runtime/no-upstream scope. Differently attributed documentation MIT notices do not establish repository-wide frontend licensing. Only minimal patches and this original attributed guide are published.

No upstream branch, PR, comment, assignment, sponsor acceptance, bounty/payment or whole-issue completion is performed or claimed.
