# Match the corridor card labels to its supplied data

The mounted CorridorHealth child calls a supplied success-rate percentage “UP” and always shows ACTIVE_MONITORING. The acquired producer explicitly maps success_rate into the legacy uptime field, while its fallback generates representative values. The child receives no monitoring-state or freshness flag.

This patch names that supplied percentage “SUCCESS” and removes the unconditional monitoring badge and its unused import. It changes no data or status behavior.

## Actual complete source chain

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), immutable commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/components/dashboard/CorridorHealth.tsx` | `a1ecf8732017a60ed56abd46184d9c73c8dab2ef` | 3,845 |
| `src/app/[locale]/dashboard/page.tsx` | `cca99335ba0ae1f66a1fb5cea0197f5ead6b2f11` | 13,126 |
| `src/app/api/dashboard/route.ts` | `367fc3807e653a782db0ba94da56a787772ee3e6` | 9,379 |

The App Router dashboard imports CorridorHealth and renders it with data.corridors when that array is nonempty. The producer's backend-success branch maps each corridor's success_rate directly to uptime, with an explicit source comment describing that proxy. Its status instead derives from health_score; this patch preserves that distinction. The fallback generates the same-shaped corridor records and uses their uptime values in its aggregate success-rate calculation.

CorridorHealth accepts id, name, status, volume24h and uptime. It receives no connection, measurement-age, provenance or monitoring-enable field. Its original ACTIVE_MONITORING badge therefore does not depend on the actual data or monitoring state.

The complete page and producer were retained as inputs from the earlier dashboard investigations. Completed page patches #32054, #32058 and #32063 preserve this caller and remain unchanged. The localized #32063 notice continues to disclose simulated comparisons, histories and live ticks, with possible fallback data. SettlementSpeedChart #32070 is a separate child and is untouched.

## Minimal presentation correction

`describe-corridor-data.patch` is **+1/-3 in three hunks**:

* Remove the unused Badge import.
* Remove the unconditional ACTIVE_MONITORING badge.
* Replace the literal UP after the existing percentage with SUCCESS.

Complete source identity:
`a1ecf8732017a60ed56abd46184d9c73c8dab2ef` (3,845 B)
→ `28b8f6b38eaa254670a645ee413c6e113a9c7177` (3,695 B).

The legacy uptime property, its percentage suffix, numeric value and bar width remain exact. No unit conversion, renamed API property, backend request, derived metric, status threshold, icon, color, volume formatting, row key, condition or event handler changes. A missing or malformed metric is not newly normalized. Existing English-only child copy remains English.

“SUCCESS” describes the supplied field's meaning in this source chain; it does not certify that the response is measured, current, complete or non-mock. Removing the badge does not disable monitoring or add a replacement connection-state claim.

## Validation and limits

The complete serialized patch reconstructs the entire postimage, and its inverse reconstructs the entire preimage. Independent UTF-8 byte counts and Git blob identities match. Every other source byte is unchanged.

No application, request, WebSocket, timer, random generator, browser, user storage, fixture or test was executed. No full UI/layout, accessibility, translation, financial-data accuracy, uptime measurement or live-monitoring acceptance is claimed.

## Attribution and qualification

Bounded current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`. Earlier contributors retain their rights; this is not a sole-author inference. The exact public Slack CorridorHealth search returned zero.

The attempted Commons overlap query returned HTTP 422 INVALID_ARGUMENT because its request lacked the required issue/PR qualifier. The exact request and error are retained and held without retry or alternate acquisition. It provides no search-result or absence evidence. Root retains no exact same-hunk completion, which is bounded custody rather than a global claim.

The complete donor tree had no root AGENTS/RULES path. EventSource-specific contribution/release guidance does not override the explicit no-tests/no-runtime/no-upstream scope. Differently attributed documentation MIT notices do not establish repository-wide frontend licensing; this packet contains only a minimal patch and original attributed guide.

No upstream branch, PR, comment, maintainer assignment, sponsor acceptance, bounty/payment or whole-issue completion is performed or claimed.
