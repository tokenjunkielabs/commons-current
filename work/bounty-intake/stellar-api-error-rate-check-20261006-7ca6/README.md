# Label the API error-rate check by its actual input

The mounted API-usage dashboard labels one card “System Health” and displays HEALTHY or DEGRADED using only the expression `data.error_rate < 5`. That one threshold does not establish the condition of the rest of the system. The child accepts no independent health status, dependency availability or broader diagnostic result for that card.

This narrow presentation patch labels it “Error Rate Check”. The unchanged true branch displays “BELOW 5%”; the unchanged false branch displays “CHECK VALUE”. The latter is deliberately neutral: the supplied number type and fetch helper do not establish a finite-number or runtime-schema guarantee, so the false result is not promoted to a verified “at least 5%” observation.

## Exact source and correction

| Field | Identity |
| --- | --- |
| Repository | Stellar-Analysis/frontend |
| Immutable donor commit | `482ee456369418ef82c4056718cb82d3468f762b` |
| Changed path | `src/components/analytics/ApiUsageDashboard.tsx` |
| Complete input blob | `cb7fbe36720ca0381dcaefd0ebf3b14cb21767d2` |
| Input UTF-8 bytes | 8,575 |
| Complete candidate blob | `2e02d4f40c28681c833761088982c0e2fbac7b18` |
| Candidate UTF-8 bytes | 8,582 |
| Diff | +2 / -2, one hunk |

The native immutable blob read returned complete content, without a separate returned SHA field. Its request-bound SHA and independently computed Git blob identity agree. Applying the exact patch to that complete input reconstructs the candidate; reversing the two presentation lines reconstructs the input exactly.

Only the card label and its two display strings change. The `< 5` expression, error-rate value, adjacent Error Rate card and its percentage formatting, remaining cards, endpoint/status charts, latency table, icons, styles and component interface stay byte-exact. The patch does not introduce a new threshold, validation rule, request, health score or fallback policy.

## Actual mounted caller and data contract

CI transferred import/render evidence from its acquired complete App Router entry `src/app/[locale]/analytics/api/page.tsx`, blob `c54b19e2753fba98266c2d05db0c4212092fe134`, as caller evidence. It imports the named ApiUsageDashboard and renders `<ApiUsageDashboard data={data} />` after non-error/noninitial-loading accepted data. This is delegated source custody; this seat did not re-fetch or independently hash that caller body.

The separate completed Commons #32108 continuation changes the page's request ownership, fallback disclosure and Last Refresh wording. This child patch targets a different file and does not repeat or replace those changes.

CI also transferred the exact relevant interface and functions from root's complete `src/lib/analytics-api.ts` custody, blob `d3daf672cc780815418e3c7518ab4d2334c21796` (23,025 bytes). The selected ApiUsageOverview interface contains total_requests, avg_response_time_ms, error_rate, top_endpoints and status_distribution. It does not contain a system-health verdict. The selected helper requests `/api/admin/analytics/overview`, returns response.json(), and on its caught failures returns a representative object with error_rate 1.2. Its millisecond field names specify units for latency, but the selected contract supplies no aggregation window, source timestamp or finite-number validation guarantee.

The helper's unawaited response.json() also means a later JSON rejection is not claimed to be caught by that function. No helper behavior is changed here. Successful page data can be representative fallback data, and no claim of measured service health or live backend telemetry is inferred from the card.

## Attribution and scope

The bounded immutable path-history response contains commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888, which relocates the frontend into the repository root. That relocation is not sole-authorship evidence. The original component remains attributed to its repository contributors; this packet supplies a narrow source continuation as patch plus guide only.

The retained same-commit recursive-tree observation contains 959 entries with truncated=false and no AGENTS/RULES. Its response echoed the requested commit; no independent full-tree reconstruction is asserted. The separately retained branch tree is `44703ba39198f99b6541450c740db0d1c3c0f7b8`.

The retained docs/CONTRIBUTING.md `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` (274 bytes) explicitly concerns EventSource tests and release commands; this patch does not modify or release EventSource. Three differently attributed license notices remain preserved in [the generator continuation packet](../stellaranalysis-issue-generator-layout-20261006-7ca6/) without assigning one repository-wide scope. This packet republishes neither the complete component nor the unrelated modules.

## Validation and limits

Validation is complete immutable child-source inspection, independent UTF-8/Git blob identity, actual delegated caller/helper inspection, bounded path history, and exact patch/reverse reconstruction. The observable claim is limited to source wording: the card now describes its existing API error-rate check instead of declaring whole-system health.

No compiler, renderer, browser, screenshot, test, fixture, application request, API server, telemetry measurement or executor ran. This is not a runtime, accessibility, localization, schema-validity, service-health, whole-build, integration or performance guarantee. No numeric formatting or data policy is invented, and invalid values or other existing component behavior remain outside the correction.
