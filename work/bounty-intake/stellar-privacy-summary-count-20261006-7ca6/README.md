# Keep an unavailable privacy activity count distinct from zero

The mounted Privacy Settings page starts with summary = null. When its summary request rejects, the page records an error and clears loading. Its overview then still says that zero data-processing activities were recorded because the count expression falls back from the missing summary to 0.

This source-only correction renders an unavailable-count message when the summary is absent. With a summary present, the entire existing count expression and wording remain unchanged, including a legitimate zero count. It changes no privacy action or legal text.

## Actual source and identity

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).
Immutable donor: `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete acquired source | Git blob identity | UTF-8 bytes | Identity qualification |
| --- | --- | ---: | --- |
| `src/app/[locale]/settings/gdpr/page.tsx` | `d5bae9d2e8e87c85edccb87078b47cf8ded22bb9` | 13,924 | Retained tree pin, native blob acquisition and independent hash matched |
| `src/lib/gdpr-api.ts` | `3fa487228abb4cd668c1f8680ea4296e780c1f0a` | 6,492 | Complete source from immutable contents URL; independently derived hash, no separate native blob-SHA field |

The API source was acquired once at [the immutable contents URL](https://api.github.com/repos/Stellar-Analysis/frontend/contents/src/lib/gdpr-api.ts?ref=482ee456369418ef82c4056718cb82d3468f762b). That successful response returned source text directly rather than the expected JSON metadata. The local parsing exception was retained, and the already-returned complete source was used without another provider call or alternate acquisition. No application request or private data was accessed.

The native page path-history result contains christabel888's relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`. This attributes observed history without asserting original authorship of every line. Dedicated upstream GdprSettingsPage PR search, dedicated Commons GdprSettingsPage plus count search, and public Slack GdprSettingsPage search returned zero. Those bounded results are not exhaustive absence claims. No external assignment, reward entitlement, maintainer acceptance or upstream action is asserted.

## Complete caller contract

This source is an actual App Router page exporting GdprSettingsPage. Its mount effect calls loadSummary. The function sets loading and clears error before awaiting getGdprSummary; success sets summary, catch sets error, and finally clears loading. The loading branch returns a spinner. Once loading is false, the initial overview is rendered even when the summary is still null.

GdprSummary declares data_processing_activities_count as a number. The acquired helper awaits fetchWithAuth for the summary endpoint and returns response.json(). fetchWithAuth propagates failure, including non-OK responses; it contains no mock summary or zero-count fallback. The page's own await also observes a rejected returned JSON promise. A failed request therefore does not establish a recorded count of zero.

This is source analysis of public code. No access token, local storage value, user identifier, consent, export/deletion record or processing log was read. No helper or fetch was invoked.

## Exact correction

`distinguish-unavailable-activity-count.patch` is **+13/-7 in one hunk and one production file**.

| Source identity | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Before | `d5bae9d2e8e87c85edccb87078b47cf8ded22bb9` | 13,924 |
| After | `86412bcef4f0ebd8e1585d7855845dc491d2c26a` | 14,133 |

The existing activity paragraph is rendered when summary is present. Otherwise, the same paragraph styling displays “Data processing activity count is unavailable.” The successful branch keeps the original summary?.data_processing_activities_count || 0 expression, its span styling and its text. Valid zero remains zero; positive values retain their prior formatting. No numeric normalization, schema validation or fallback policy is introduced for malformed non-null summaries.

Everything before and after this one paragraph replacement is byte-for-byte exact: mount/load logic, loading and error handling, consent and request counts, tab buttons, ConsentManager/DataExport/DataDeletion render bindings, rights information and all other copy. The API helper is context only and is not modified. No consent, export, deletion, authentication, retry, cancellation or lifecycle behavior changes.

## Validation and limits

The acquired page's full native and independent identities matched. The helper's independent source identity is explicitly distinguished from a separately returned provider SHA. The serialized one-hunk patch reconstructs the full postimage and its inverse reconstructs the full preimage. Pure source comparisons preserve the complete prefix/suffix outside the changed paragraph.

No fixture, test, application runtime, typecheck, build, browser, API call, storage operation, account action, privacy request, data export or deletion was performed. The source result is an honest missing-observation display, not proof of live data freshness, correct server counts, request recovery, privacy compliance, legal advice or whole-page accessibility. Existing error text, missing retry UI, request lifetime, summary schema assumptions and child behavior remain outside the patch.

The retained complete donor tree has no AGENTS/RULES paths. Its known contributing document concerns EventSource tests/npm release workflow, not this authorized source-only continuation. Three differently attributed documentation MIT notices do not establish repository-wide licensing. This Commons packet contains only the minimal attributed patch and this original guide. Completed work, external ownership and exact failed-route holds remain intact; no upstream submission occurs.
