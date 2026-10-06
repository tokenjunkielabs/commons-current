# Use the refresh button's localized visible name

The mounted DataRefreshIndicator already renders localized button text: `t("refresh")` when idle and `t("refreshing")` while refreshing. Its decorative SVG is hidden from the accessibility tree. A separate hardcoded `aria-label="Manually refresh data"` overrides that visible text with an English name.

This one-line removal lets the native button derive its accessible name from the existing visible content. The title remains `t("refreshNow")`; no new translation key, string, dependency, state, or callback is introduced.

## Source identities and actual caller

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).

Donor: `482ee456369418ef82c4056718cb82d3468f762b`.

| Source | Git blob | UTF-8 bytes | Custody |
| --- | --- | ---: | --- |
| `src/components/DataRefreshIndicator.tsx`, preimage | `f57e4cdba8fddc335677f9de3aacbca7785d3990` | 5,191 | Complete immutable native content for this task, independently hashed |
| Same component, postimage | `e667764e518ec7c62785ebeff84aa0b3bef6e695` | 5,148 | Exact +0/-1 transformation |
| `src/app/[locale]/dashboard/page.tsx` | `cca99335ba0ae1f66a1fb5cea0197f5ead6b2f11` | 13,126 | CI retained full mounted route; exact indicator invocation transferred |
| `messages/en.json` | `d714ba710db0e7287bf81d3ebfd00cbe8292ef88` | 7,724 | CI retained full resource; exact relevant dashboard values transferred |
| `messages/es.json` | `eeeb6e815a966037e0c7bbac524438bf423f8aa8` | 6,988 | Same attributed custody |
| `messages/zh.json` | `f37d511ba8aa41c7d6e1f17129856aa92537d8c4` | 5,885 | Same attributed custody |

The native blob response supplies content without a separate SHA field; the request-bound identity and independently computed identity match. Caller and resource rows are exact attributed transfers, not new full-module acquisitions or independent whole-file hashes in this lane.

The actual dashboard passes lastUpdated, secondsUntilRefresh, a 30-second interval, isRefreshing, and triggerRefresh to this component. The values and callback originate from useDataRefresh. The acquired child uses `useTranslations("dashboard")`, a native button with `disabled={isRefreshing}`, and the two existing visible state strings.

| Locale | Existing idle text | Existing busy text | Existing title |
| --- | --- | --- | --- |
| en | Refresh | Refreshing… | Refresh now |
| es | Actualizar | Actualizando | Actualizar ahora |
| zh | 刷新 | 刷新中 | 立即刷新 |

These exact values were transferred from CI's full resources. CI's separate dashboard notice preparation adds dataNotice keys and preserves these values. No locale resource is changed by this packet.

The bounded current-path history at the donor returned only `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888, for repository-root relocation. This does not establish sole authorship or complete earlier history. Embedded build claims were not rerun.

## Primary contract and narrow inference

The [W3C ARIA Authoring Practices naming guidance](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/) identifies buttons as elements named by their descendant content by default. It explains that aria-label replaces that content-derived name, recommends visible text for naming, and calls for translating aria-label values in multilingual interfaces.

Applied to the complete acquired button, the removed English attribute was the explicit override. The visible localized text already supplies the intended action or busy-state name, and the SVG remains aria-hidden. This is source and standards reasoning; browser or assistive-technology output was not observed, and no live announcement behavior is promised.

## Exact scope and validation

Only the hardcoded button aria-label line is removed. The complete remainder of the component is byte-exact: props, imports, translations, visible text, title, onClick binding, disabled behavior, SVG attributes, class names, countdown arithmetic, timestamp formatting, surrounding labels, and return structure.

The completed useDataRefresh timer-lifetime packet is a different file and is not rerun or reconstructed. CI's dashboard error recovery, nested KPI update, and provenance notice scopes are separate. Root and CI retained no exact same-child label completion or hold; this is bounded coordination evidence, not a global absence claim.

Full child-source inspection, actual caller/resource transfers, the primary naming contract, bounded history, exact line/hunk checks, and Git blob/UTF-8 identity computation were performed. No component, hook, timer, callback, request, translation runtime, browser, assistive technology, compiler, typecheck, lint, test, fixture, workflow, build, or executor was invoked. No whole-page accessibility, language, runtime, visual, performance, or upstream acceptance claim is made.

The deliverable is patch plus guide. A repository-wide license scope is not inferred from the differently attributed retained notices; the complete donor module is not republished. Existing notices remain in [the earlier generator packet](../stellaranalysis-issue-generator-layout-20261006-7ca6/). No upstream submission, account, payment, contact, or claim action is included.
