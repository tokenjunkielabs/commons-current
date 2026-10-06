# Keep API Usage refresh state with its current request

The mounted API Usage page invokes loadData immediately, every 30 seconds, and from its Refresh and Retry controls. Each invocation awaits fetchApiUsageOverview. Previously every completion could replace data, lastUpdated, error and loading state even after a later request started or the page effect cleaned up.

This continuation gives each admitted request a unique object token. Only the token still owned by the page may commit a success, error or loading completion. It also explains the actual sample-data fallback and calls the client completion timestamp “Last Refresh.”

## Canonical source and ownership

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).
Immutable commit: `482ee456369418ef82c4056718cb82d3468f762b`.

| Input | Git blob | UTF-8 bytes | Custody |
| --- | --- | ---: | --- |
| `src/app/[locale]/analytics/api/page.tsx` | `c54b19e2753fba98266c2d05db0c4212092fe134` | 4,390 | Complete native body, independently matched |
| `src/lib/analytics-api.ts` | `d3daf672cc780815418e3c7518ab4d2334c21796` | 23,025 | Root's previously acquired complete body; exact selected type/helper/fallback excerpt transferred for this task |

The route is an actual App Router entry. Its full source imports fetchApiUsageOverview, awaits it in loadData, and passes the accepted data to ApiUsageDashboard. The patch is confined to this route; it does not modify that child or the helper.

Current native path history returned christabel888's relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`. This is attribution for the observed history, not proof of original authorship of every line. Dedicated Commons PR search for ApiAnalyticsPage plus request, upstream PR search for ApiAnalyticsPage plus refresh, and public Slack search for ApiAnalyticsPage plus request returned zero. These bounded queries do not establish global absence. No external carrier, issue assignment or upstream acceptance is claimed.

## Exact request ownership

A top-level useRef holds the current request token. Each loadData call creates and assigns its own token before the existing synchronous loading/error reset. Successful completion checks token identity before both data and lastUpdated writes. The catch branch checks before changing error. The finally branch independently checks before clearing loading, so a stale return or rejection cannot clear a newer request's loading state.

Effect cleanup still clears the same interval and now also invalidates the current token. An already pending continuation then fails its identity check. A later effect setup creates a fresh request token; old work cannot inherit that identity.

The mount call, 30-second interval, manual callbacks, error text, data values, timestamp creation and initial resets retain their existing policies. The method does not abort fetches or serialize requests. Overlap remains possible, and the rule is latest admitted request, not latest server observation. Under sustained slow responses, a newer interval request can supersede an older request before it completes; this packet introduces no deadline, cache, retry or guaranteed update latency. It also makes no claim about state committed before cleanup occurs.

The primary [React useRef reference](https://react.dev/reference/react/useRef), acquired earlier in this source lane, documents retention of a mutable ref object across renders. The previously acquired [React useEffect reference](https://react.dev/reference/react/useEffect) documents cleanup on effect replacement and unmount. This patch uses those existing contracts and does not revisit held useState/StrictMode documentation routes.

## Result provenance and timestamp wording

The transferred exact helper fetches `/api/admin/analytics/overview`. A non-OK response throws into its catch; that branch returns getMockApiUsageOverview after its existing logging policy. The mock function returns fixed request counts, latency, error rate, endpoint rows and status counts. Consequently a fulfilled page request is not proof of live telemetry.

The helper returns response.json() without awaiting it inside the try. A later JSON rejection can therefore escape that helper catch and reach the page's awaited catch. The new token guard covers that completion without changing the helper's error or fallback policy.

The page's lastUpdated is new Date() after a result arrives; it is not a server measurement timestamp or network scan. The source patch renames only “Last Scan” to “Last Refresh” and adds a short paragraph explaining possible built-in sample metrics and the client-completion meaning. It does not classify an individual result as live or simulated. No per-result provenance field or server timestamp is invented.

## Patch and source identities

`own-api-usage-refresh-state.patch` is **+17/-4 across three hunks in one production file**.

| Source identity | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Before | `c54b19e2753fba98266c2d05db0c4212092fe134` | 4,390 |
| After | `2f5723bf514d154e7bd6163f86971ed4367882a6` | 5,019 |

The request-only part is +12/-3. The remaining changes are the four-line explanatory paragraph and the timestamp label. Removing those selected copy edits yields the independently retained request-only postimage, whose entire JSX suffix matches the original. The interval expression and all handler bindings remain exact.

The serialized full patch reconstructs the complete postimage, and its inverse reconstructs the complete preimage. Independent Git blob identities and UTF-8 counts are recorded. Infra's reasoning check covered the supplied token design only, emphasizing the independent finally guard; it was not an independent source acquisition, runtime review or approval gate.

## Boundaries

No browser, request, API key, account, telemetry collection, storage, fixture, test, build or application code was executed. The analytics helper excerpt is attributed to root's retained complete source rather than described as a new independent full-file read. This source-only packet does not validate response schemas, numeric metrics, the rendered dashboard, service availability, installed dependencies or whole-repository lint/type correctness. Existing effect dependency structure and fetch behavior remain unchanged.

The retained complete donor tree has no AGENTS/RULES paths. The known contribution document addresses EventSource test/npm release workflow, which is outside the authorized no-runtime scope. Three differently attributed documentation MIT notices do not establish a repository-wide licensing scope. Only the minimal attributed patch and this original guide are published in Commons. All prior source completions, author ownership and exact route holds remain intact; this is not an upstream contribution or acceptance claim.
