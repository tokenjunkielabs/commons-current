# Clear the dashboard error after a successful refresh

The dashboard's initial request catches failures into a page-wide error state. Its separate refresh hook stays mounted and continues the thirty-second countdown, including while the page renders that error. A later successful refresh stores new data but leaves the error set, so the page keeps rendering the old failure instead of its recovered data.

This patch clears that error only after the existing fetch and JSON decoding succeed and the result is stored.

## Complete source and caller evidence

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/dashboard/page.tsx` | `cca99335ba0ae1f66a1fb5cea0197f5ead6b2f11` | 13,126 |
| `src/hooks/useDataRefresh.ts` | `4cb937ecb129bf4bf88893721b8d15a5bbc3e3b0` | 4,565 |

DashboardPage is an actual client App Router entry. Its fetchDashboard callback fetches /api/dashboard, rejects non-OK responses, awaits response.json and calls setData. The initial effect awaits that same callback; failure sets error, and finally sets loading=false.

Before any loading/error render return, the page calls useDataRefresh with onRefresh=fetchDashboard and refreshIntervalMs=30,000. The complete hook starts its countdown in an effect and calls onRefresh from its timeout. It catches refresh failures and schedules the next countdown. The successful page render also passes triggerRefresh into DataRefreshIndicator, but this correction does not require that control to be visible during the error state: the existing timer is already connected.

The page checks loading, then error, then data. That ordering makes the stale error a concrete blocker after successful automatic recovery. No route mount, external API, browser or timer was executed to establish this source call graph.

## One-line source change

`clear-recovered-dashboard-error.patch` adds **one line in one hunk**:

`setError(null);` follows the existing `setData(result);` in fetchDashboard.

Full source identity:
`cca99335ba0ae1f66a1fb5cea0197f5ead6b2f11` (13,126 B)
→ `0748c045e1edaf7a7adba4198980134376146025` (13,146 B).

The error is not cleared when a request starts or when HTTP/JSON failure occurs. Existing initial-load error classification/logging, hook retry/countdown policy, manual refresh, loading state, lastUpdated behavior, translation dependency, data schema and render branches stay exact. WebSocket callbacks, simulated ticks and all dashboard child props are untouched. The distinct analytics-page #31964 correction is a separate source path and is not replayed here.

The complete serialized patch reconstructs the entire postimage and its inverse reconstructs the preimage, with independent Git blob identities. No application, request, timer, synthetic fixture, test, browser, storage or device execution was used.

## Boundaries and attribution

This is a successful-result error reset, not a request-generation or cancellation implementation. Overlapping initial/refresh results, stale callbacks, unmount ownership and the hook's lifecycle behavior remain outside this patch. Successful JSON decoding does not validate DashboardData; the existing response shape assumption remains. Existing simulated telemetry is not converted into measured production data or endorsed by this recovery fix.

Current exact-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`. Original contributor rights remain; relocation is not proof of sole authorship. Scoped Commons and public Slack queries for fetchDashboard/error returned zero, which is bounded overlap evidence only.

The complete donor tree had no root AGENTS/RULES path. Its EventSource-specific contributing/release guidance does not override the explicit no-tests/no-runtime/no-upstream scope. Differently attributed documentation MIT notices do not establish repository-wide frontend licensing. Only this minimal patch and original attributed guide are published.

No upstream branch, PR, comment, assignment, sponsor acceptance, bounty/payment, whole-issue completion, deployed recovery or full build claim is made.
