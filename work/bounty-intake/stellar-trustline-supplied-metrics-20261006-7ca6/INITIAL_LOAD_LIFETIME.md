# Bound the initial trustline load to its effect lifetime

The page's initial loadData effect awaits overview/ranking results and then the first asset's details. It previously wrote those results and cleared page loading even after the effect instance had been cleaned up. The row-selection guard added in #32135 explicitly left this initial path untouched.

This patch adds one effect-local active flag, two post-await checks, a guarded loading-finally and cleanup that clears the flag. It bounds the initial effect's asynchronous state writes to that setup's lifetime. The row-click request token, pending/error UI and all presentation remain unchanged.

Apply this patch after #32126, #32131 and #32135 in that order. The prior artifacts and exact notices remain unchanged. This guide supersedes only the earlier caveat that initial loadData has no lifetime guard; other availability, schema and execution limits remain.

## Actual source and caller

The canonical source is Stellar-Analysis/frontend at `482ee456369418ef82c4056718cb82d3468f762b`. The complete route/helper/children were newly acquired for #32126 and their full text remains retained. This continuation uses the exact composed #32135 postimage, with no source recovery or old work replay.

| Source | Preimage / UTF-8 bytes | Proposed postimage / UTF-8 bytes |
|---|---|---|
| src/app/[locale]/trustlines/page.tsx | `1eb0811966f046ebac6c39d4f45477e1ba49ad08` /15754 | `4400d3e9b2023acf6f865d14c82f4c8bc1363415` /15897 |

The unchanged helper is src/lib/trustline-api.ts, Git blob `6ff2791be6f5997b5ab3c1b49f666d100e1be414`,3116 bytes. It supplies the same overview, rankings, history and insight calls. No helper body, endpoint, request option or record shape changes.

The route directly starts loadData in its existing mount effect. The first await group requests metrics and up to50 ranked assets. The effect then writes stats and rankings, chooses the first asset if present, and awaits that asset's history and insights. Its finally clears the page-level loading state.

The new flag belongs to that particular effect setup. A later setup has its own flag. Cleanup of the earlier setup cannot re-enable it or disable the later flag.

## Resulting ordering

| Point in the existing initial loader | Added condition |
|---|---|
| Effect setup | Create active=true for this setup |
| After overview/ranking await | Return before any result writes if inactive |
| After first-asset detail await | Return before history/insights writes if inactive |
| Finally | Clear page loading only while active |
| Effect cleanup | Set this setup's active flag to false |

The first admission check also prevents a cleaned-up initial loader from starting the second detail-request group. If the second group already started, it is allowed to settle but cannot write its results after cleanup. A return from either check still enters finally; the independent finally guard prevents that obsolete completion from clearing the loading state of a newer setup.

The initial synchronous setLoading(true) remains in the setup's loader. The same Promise.all calls, ranking limit, first-row choice, selectedAsset assignment, response writes and catch logging remain in their original order, subject only to the new admission checks. There is no retry timer, abort signal or cancellation implementation.

The existing catch continues to log errors even for an inactive setup. This correction is about component state admission, not suppressing helper or catch side effects. The logger and every request are only inspected as source; they were not invoked.

## Primary lifecycle contract

The previously acquired official [React useEffect reference](https://react.dev/reference/react/useEffect), read successfully during #32135, describes cleanup after component removal and an extra development setup/cleanup cycle. Those documented boundaries support the local flag's purpose. No documentation route was retried for this continuation.

The guarantee begins after this cleanup actually runs. It does not promise that a navigation click instantly cancels outstanding work, prevent synchronous writes before cleanup, or stop underlying requests. The displayed documentation version19.3 is not evidence of this repository's installed dependency version or a compile/runtime result.

## Exact source verification

guard-initial-trustline-load.patch is1134 UTF-8 bytes, Git blob `f9d6f3890fcb4f42d463f6117ec4e528227841df`. It adds seven lines and removes one across three hunks containing36 complete serialized rows.

The actual serialized patch reproduces the full expected postimage in the forward direction and the full preimage in the inverse direction. Every hunk row is included without truncation. Reversing only the five authored replacement regions recovers every other source byte exactly. The complete row-click handler is separately equal, and the formatter plus the entire rendered portion of the route are separately equal.

Consequently the prior supplied active-assets count, removal of unsupported badges, exact code-and-issuer selected predicate, click-attempt guards, pending/error text, chart/insight props and all distribution arithmetic remain as published. The initial effect now has its own local lifetime ownership; the separate click-token cleanup from #32135 remains intact.

No source compiler, fixture, test, component, data helper, chart or formatter was run. These are full-string and static control-flow checks, not simulated requests or observed user behavior.

## Limits, attribution and publication

This does not introduce an initial error view or alter any existing fallback. The helper can still resolve some failures as zero metrics, empty arrays or null insights, and some returned JSON promise failures can still reach the existing catch. An unresolved promise remains unresolved; a stopped state update does not mean a request was cancelled.

The guard does not check returned asset identifiers, validate malformed responses, distinguish an unavailable count from a true zero, change cache/freshness policy or prove backend consistency. It does not make the ranking data current when a later row is selected. The component still uses its retained record and numeric policies.

The effect has an empty dependency list and no new refresh trigger. This is not a general request scheduler or cross-component ordering mechanism. Nothing here establishes account, issuer, protocol, wallet, trustline or financial state.

Original contributors retain credit and the three exact existing notice files remain in the packet. A new dedicated Commons PR query for trustline, initial and cleanup returned only #32135, whose accepted scope explicitly excluded this initial effect. That is bounded overlap evidence, not a global absence or whole-feature completion finding.

Publication adds this guide and the incremental patch only. Complete immutable artifact strings, native and independent identities, PR metadata, changed paths, tree and ordered parents are checked separately. A predeclared observed-main equality alias is used only if main equals the verified merge/readback ref; otherwise both files receive complete reads at one observed immutable main without chasing movement.

No API, account, wallet, payment, trustline, deposit, withdrawal, browser, runtime, build, test, compiler or upstream action was taken. Existing held routes, the #32074 final changed-files UNKNOWN, earlier cache-loss qualifications and unrelated unpublished parked source draft remain protected.
