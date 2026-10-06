# Label the internal monitoring dashboard as a demo

The internal monitoring route describes itself as real-time monitoring, but its only data source is `getMockMonitoringStats()`. The acquired producer generates page-load/error series and returns fixed API, session, and browser values. The page also displays hard-coded comparison percentages.

This patch adds “Demo” to the page heading and changes the description to “Sample data for frontend vitals, API health, system errors, and session metrics.” That visible label qualifies the dashboard as a demonstration. The generator, charts, values, comparisons, loading behavior, and layout remain unchanged.

## Exact source

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).

Donor: `482ee456369418ef82c4056718cb82d3468f762b`.

Changed path: [src/app/[locale]/internal/monitoring/page.tsx](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/app/%5Blocale%5D/internal/monitoring/page.tsx), mode `100644`.

| Identity | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Complete donor page | `c3876654305fe4fbdc5a9f64e158ba6056253d92` | 12063 |
| Prepared postimage | `5bd1fabfbc1604b674e46074917bfe9102495be0` | 12077 |

The adjacent `change.patch` contains one hunk, **3 additions and 3 deletions**. It applies directly to this exact donor. The three changed source lines are visible copy only; every other line remains byte-identical. No prior Commons patch to this route is required or represented.

## Actual caller and producer

The complete page exports `MonitoringDashboard` as the route default. Its mount effect waits through an 800 ms timeout described in the source as simulated API latency, then calls `getMockMonitoringStats()`, stores the result, and clears its loading state. The populated UI renders under `MainLayout` and uses that result for all of its data charts.

The full sibling [layout.tsx](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/app/%5Blocale%5D/internal/monitoring/layout.tsx) was read at blob `64fe49967d2429ec0f6523c46c2f0039735877e6`, **618 bytes**. It returns its route children and retains `dynamic = "force-dynamic"`. Its historical comment describes a static-rendering/provider issue; that comment is not treated as a current runtime result, and this patch does not alter the layout.

The complete imported producer, [src/lib/mock-monitoring.ts](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/lib/mock-monitoring.ts), is blob `2ef06e069a23e98174b2b3405c23d1ed7ca40da7`, **2082 bytes**, mode `100644`. It constructs twenty-four timestamped page-load values and twenty-four error counts with `Math.random()`; API latencies, session totals/duration/bounce rate, and browser/device breakdowns are literal sample values. It performs no data fetch in the acquired body.

This complete page-to-producer path supports the demo wording without assuming an intended backend, inventing an observation, or executing the generator. The route entry is established in source; no navigation-menu link or mounted browser session was observed for this packet.

## Source qualification and attribution

The donor tree metadata supplied the exact page, sibling layout, and producer pins. Each complete native blob response supplied content without a separate returned SHA field; independent Git blob hashing and UTF-8 byte counts matched the request-bound identities above.

A bounded five-entry path-history request at the donor returned one root-path entry: `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, the root relocation attributed to `christabel888`. This root-path result does not claim complete history across the relocation or sole authorship.

The fleet retained no exact same-route writer, completion, or hold. That is a bounded custody observation, not a global ownership claim. The unrelated ambiguous Telemetry 404 hold remains intact and was not retried or recovered. Existing author, source-access, and upstream acceptance constraints remain.

This source continuation is distinct from Commons [#31984](https://github.com/woahwhattheheck/commons/pull/31984), which removes fallback observations on `src/app/[locale]/performance/page.tsx`. This internal dashboard keeps its demo generator and labels the resulting presentation. Neither packet establishes local telemetry persistence, connects a backend, or changes a storage policy.

## Review and limitations

Review was static: complete source acquisition, exact source/byte identities, and a three-line copy change. The producer was inspected as text and never invoked. No app, browser, React effect, timeout, random generator, telemetry operation, storage access, compiler, tests, fixture, build, workflow, or upstream action ran.

No live-monitoring, production-health, accessibility, mounted-runtime, or whole-build success claim is made. Existing loading/timer cleanup, provider boundaries, chart behavior, and any future real-data integration remain outside this change.

The packet is a narrow patch and guide. A repository-wide licence scope was not established, so it does not republish the complete donor modules. The separately attributed MIT notices already retained in Commons under `work/bounty-intake/stellaranalysis-issue-generator-layout-20261006-7ca6/` remain unchanged and are not assigned a repository-wide scope by this packet.
