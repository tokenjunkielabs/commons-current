# Remove the unsupported live badge from the settlement chart

The mounted SettlementSpeedChart unconditionally displays REAL_TIME. Its actual dashboard producer generates the settlement-history series in both its backend-success and mock-fallback branches, and the page then applies random steps to its last value. The child has no provenance or freshness flag with which to justify that badge.

This patch removes the badge and its unused import. It leaves the chart and all data behavior unchanged.

## Complete actual source chain

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), immutable commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/components/dashboard/SettlementSpeedChart.tsx` | `cad2d9146c7b8f2661428a8598ba1c4139cb4586` | 3,400 |
| `src/app/[locale]/dashboard/page.tsx` | `cca99335ba0ae1f66a1fb5cea0197f5ead6b2f11` | 13,126 |
| `src/app/api/dashboard/route.ts` | `367fc3807e653a782db0ba94da56a787772ee3e6` | 9,379 |

The client dashboard imports this exact child and renders it with data.settlement when that array is nonempty. The producer's successful branch creates six time-labelled speed values by scaling its current average, rather than obtaining a historical time series. Its fallback also generates six values around a mock average. The page's existing 2,800 ms effect randomly adjusts the final speed value.

The chart accepts only time/speed records and renders its badge regardless of their origin, age or any actual connection state. Neither this data shape nor the acquired caller supplies a real-time provenance flag. Removing that unconditional claim is supported without inventing a new mode, contract or measured source.

The complete page/producer bodies were retained from new dashboard investigations and reused as inputs to this distinct child correction. Existing #32054 recovery, #32058 state ownership and #32063 localized data disclosure preserve this render chain and remain unchanged. Root's #32002 SettlementLatencyChart is a different source path.

## Minimal patch

`remove-unqualified-live-badge.patch` changes **+0/-7 in two hunks**:

* Remove the unused Badge import.
* Remove the six-line unconditional REAL_TIME badge.

Source identity:
`cad2d9146c7b8f2661428a8598ba1c4139cb4586` (3,400 B)
→ `3778ec15c069cc7c0d167d254e6092d676478f1e` (3,212 B).

The header container and existing heading/subtitle remain; no replacement provenance claim is introduced. BarChart data, time-axis mapping, seconds formatting, tooltip, color thresholds, bar animation, responsive sizing, imports used by the chart and all other source bytes stay exact.

The seconds units already agree with the actual producer's conversion from milliseconds and its fallback averages. No unit repair is made. Existing chart/title terminology, missing/invalid-record policies and color thresholds are not certified by this badge removal. The separate page-level disclosure still explains the generated data.

## Validation and boundaries

The complete serialized patch reconstructs the entire postimage, and its inverse reconstructs the entire preimage. Independent UTF-8 byte counts and Git blob identities match. No chart rendering, API request, WebSocket, timer, random generator, browser, fixture, test or application was executed.

The patch removes an unsupported label; it does not connect telemetry, replace synthetic values, classify the current response or establish live freshness. Removing the badge naturally changes that header's visible content; no pixel/layout or accessibility acceptance is claimed.

Bounded current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`. Original contributor rights remain, with no sole-author inference. Scoped Commons/public Slack queries for SettlementSpeedChart and its real-time claim returned zero, which is bounded overlap evidence only.

The complete donor tree had no root AGENTS/RULES paths. EventSource-specific contribution/release guidance does not override the explicit no-tests/no-runtime/no-upstream scope. Differently attributed documentation MIT notices do not establish repository-wide frontend code licensing. Only this minimal patch and original attributed guide are published.

No upstream branch/PR/comment, maintainer assignment, sponsor acceptance, bounty/payment or whole-issue completion is performed or claimed.
