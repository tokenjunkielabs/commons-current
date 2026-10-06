# Distinguish failed and generated health-dashboard data

This packet contains two composable source corrections for the mounted HealthDashboard:

1. Render its already-recorded initial fetch error instead of falling through to zero-valued summary cards.
2. Label its generated reliability histories and incidents as examples, and remove the Stable card's literal comparison.

Neither patch changes requests, metric computation, thresholds, generators or alert settings.

## Actual source and mounting

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), immutable commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input acquired in this lane | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/health/page.tsx` | `5bd72d0758c6b99e19c74f79c725dc052ff60f18` | 140 |
| `src/components/health/health-dashboard.tsx` | `d77d90f443f2571f4cbe077bcec82c0bd8a572b0` | 15,761 |
| `src/lib/api/api.ts` | `1af4d71a9127deb5186f016718483dbab088f414` | 7,998 |

The App Router health page directly imports and renders HealthDashboard. Its mount effect awaits getAnchors(), assigns response.anchors on fulfillment, records “Failed to fetch anchor data.” in catch, and clears loading in finally. The actual getAnchors returns api.get for /anchors; its fetch wrapper throws or wraps non-OK, parsing and other caught failures. This path has no mock fallback. No endpoint was called.

Root separately retained the complete shared `src/components/dashboard/MetricCard.tsx`, blob `0be01cd20b73e9cd85b74e17f94398ae7f69e7f0`, 2,043 B, and transferred its relevant optional-prop/render contract. That is attributed retained-source evidence, not another source acquisition or runtime check here. The component displays the absolute trend percentage and “vs prev window” only when trend is defined. trendDirection also controls a positive icon glow outside that conditional.

## Composition order and identities

Apply these patches in order to the donor HealthDashboard:

| Stage | Source Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Donor | `d77d90f443f2571f4cbe077bcec82c0bd8a572b0` | 15,761 |
| After `render-health-fetch-error.patch` (#32078) | `ac0cf6b0eba62f23e86244b758a4b5166b1eec30` | 16,060 |
| After `describe-generated-health-data.patch` | `881fc7b7823d1813114a0ce7bc572d145b7a8c68` | 16,155 |

The previously published error patch remains byte-for-byte unchanged: Git blob `570594b1633e51e7faab1ac49a8aaa5b61888f91`, 637 B. This continuation adds one new patch and updates this original guide.

## Recorded fetch error

The accepted first patch is **+9/-0 in one hunk**. After the unchanged loading return, an existing non-null error displays an alert container, a “Health data unavailable” heading and the component's fixed error message. Loading retains precedence; a successful empty anchors array retains its original empty summary/card behavior.

No retry, request cancellation, error clearing, unmount guard, response validation or failure-category policy is added. The new continuation preserves that entire error guard.

## Generated histories, incidents and literal comparison

The complete HealthDashboard itself is the producer for the two displayed datasets. generateHistoricalData builds 30 dated values by applying random variation to the current reliability score. generateRecentFailures selects random timestamps, reasons and corridor names. Both are called inside the per-anchor render path; neither reads a historical telemetry or incident source.

The original headings called these “30-Day Reliability Telemetry” and “Incident Log”, and its empty-incident branch said “No anomalies detected”. The Stable summary also passed literal trend={100} and trendDirection="up" into the shared MetricCard. No earlier observation or comparison calculation supports those props.

The new patch is **+7/-5 in five hunks**:

* Add a plain explanation that reliability histories and incident logs below are generated examples.
* Name the chart “Simulated 30-Day Reliability”.
* Name the list “Sample Incident Log” and its existing empty branch “No sample incidents”.
* Remove both literal Stable-card comparison props. This hides the comparison and removes its positive glow; the loaded Stable count and its threshold remain unchanged.

This is one coherent provenance correction. It does not replace or execute the generators, certify the loaded data, invent an earlier comparison window or change the summary classifications. Every request, setter, loaded anchor field, chart series/tooltip, generator, date calculation, list item, style and control stays unchanged outside the explicit paragraph/label/prop hunks. Existing English-only copy remains English.

## Validation and remaining boundaries

The complete serialized new patch reconstructs the entire postimage, and its inverse reconstructs the entire #32078 postimage. Independent UTF-8 byte counts and Git blob identities match. Retained-string checks confirm complete generator and settings blocks remain exact; the existing error patch is preserved.

No application, API, browser, storage, timer, random generator, fixture, synthetic response or test was executed. No whole build, accessibility, announcement, localization, health-data accuracy or operational-monitoring acceptance is claimed.

Unused settings behavior, success-versus-uptime terminology, missing observations, response shape, live data integration and thresholds remain unselected. The guide does not describe this as a complete health system. Root's analytics comparison correction used another caller; root graph work and prior dashboard/contact packets are separate source paths.

## Attribution and authority

Bounded current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`; earlier contributors retain their rights, with no sole-author inference. Separate scoped Commons/public Slack queries for the error and generated-provenance scopes returned zero; the Commons incomplete_results flags were false. These are bounded overlap observations only. Root supplied the retained MetricCard contract and suggested combining the related provenance observations; it was not a review or permission gate.

The complete donor tree had no root AGENTS/RULES path. EventSource-specific contribution/release guidance does not override the explicit no-tests/no-runtime/no-upstream scope. Differently attributed documentation MIT notices do not establish whole-frontend licensing. Only minimal patches and this original attributed guide are published.

No upstream branch, PR, comment, maintainer assignment, sponsor acceptance, bounty/payment or whole-issue completion is performed or claimed.
