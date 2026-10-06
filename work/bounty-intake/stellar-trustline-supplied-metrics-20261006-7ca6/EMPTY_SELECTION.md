# Trustlines empty-selection message

The Trustlines route can finish loading with no ranking rows and no selected asset. Its retained placeholder still asks the reader to select an asset from the leaderboard, even though that rendered leaderboard has no buttons. This incremental proposal changes that placeholder to “No assets are available to select.” when the current rankings array is empty.

The existing two-line instruction remains for a nonempty rankings array and a null selection. A selected asset still takes the existing details branch. The page's earlier loading return remains unchanged. This is a description of the local list's available selection action, not a statement that the network has no assets or that a request succeeded.

## Exact source and composition

The canonical donor is [Stellar-Analysis/frontend at 482ee456369418ef82c4056718cb82d3468f762b](https://github.com/Stellar-Analysis/frontend/tree/482ee456369418ef82c4056718cb82d3468f762b). The production path is `src/app/[locale]/trustlines/page.tsx`.

This patch starts from the complete proposed route retained after [Commons #32162](https://github.com/woahwhattheheck/commons/pull/32162). It does not start from the canonical route. The preceding route chain is #32126 → #32131 → #32135 → #32138 → #32141 → #32144 → #32162. The helper and chart are separate files with the dependencies recorded in [APPLICATION_ORDER.md](APPLICATION_ORDER.md).

| Identity | Git blob | UTF-8 bytes |
|---|---|---:|
| Required route preimage after #32162 | `47f44d7d322abc336ea8037ac37d4a0d7c600010` | 16435 |
| Proposed route postimage | `e28e557814ba7a0d7e62f95ed5eb8445959d30dc` | 16627 |
| [show-empty-asset-selection.patch](show-empty-asset-selection.patch) | `078afcf5c7e6a81a684b4c4269b7bc0e0ffe71a9` | 1007 |

The serialized unified patch contains one hunk, 18 rows, +9/−3. The line increase mostly wraps the old instruction in a conditional fragment. All bytes outside that one placeholder's contents remain exact.

## Why the empty state is reachable

The complete retained page initializes rankings to an empty array and selectedAsset to null. Its initial effect obtains stats and rankings with the existing Promise.all, stores the returned rankings, and selects the first asset only when rankingsData.length is greater than zero. Its finally block clears loading only while that effect remains active.

The complete retained `src/lib/trustline-api.ts` has a rankings helper that returns parsed JSON for an OK response and returns [] from its catch. Thus both a successful empty rankings array and an existing caught HTTP/network failure can leave no buttons to select. A rejected initial Promise.all can also leave the original empty local state. The proposal does not diagnose which path occurred.

Once loading is false, the route's rankings.map renders one button per retained row. Its selectedAsset conditional independently chooses the details view or placeholder. Only the placeholder is edited: rankings.length > 0 retains the existing instruction, otherwise the message describes the absence of selectable rows.

## Preserved behavior and limits

No fetch call, URL, request argument, Promise.all, helper, catch, logger, state setter, effect dependency, cleanup, selection token or handler changes. Code-plus-issuer identity and the current-item marker remain exactly as delivered. The selected asset details, pending/error views, overview counts, chart, insights, distribution and all surrounding classes/icons remain unchanged.

The instruction's visible words and line break are unchanged for the nonempty-list branch; they are indented inside a fragment. No retry control, reload action, loading announcement, error-specific message, focus change or new control is added. The neutral sentence appears only in the existing null-selection placeholder after the original loading return.

This does not distinguish a genuinely empty successful response from an unavailable response, validate response schemas, infer live network state, or repair the helper's fallback policy. In particular, the existing history helper's [] and insights helper's null fallbacks, and their unawaited JSON-rejection boundaries, remain as previously documented. The independent date-only and detail-availability no-patch dispositions are unchanged.

Malformed non-array rankings already fall outside the declared TrustlineStat[] contract and retain their prior behavior. No new claim is made about duplicate identities, list ordering, availability of an asset absent from the returned list, or correctness of backend data. The source analysis is not an observed user session.

## Review and verification

The complete current route, helper and earlier receipt maps were already retained. This work consumed those bytes directly; it did not reacquire accepted donor sources, reapply earlier patches, rebuild accepted postimages or rerun accepted checks. The fresh donor main metadata remained at the pinned canonical commit. One dedicated native Commons PR query for “Trustlines empty selection” returned no results within its bounded search; that is not global absence proof. Root retained no exact same-hunk completion or hold.

The new patch was checked as serialized text: forward reconstruction exactly equals the new proposed source; inverse reconstruction exactly equals its required preimage; replacing only the new conditional block with the retained old block restores every original byte. No JSX expression, application, request, account, trustline, wallet, payment, browser, compiler, build, test or fixture was executed.

This packet also updates the existing APPLICATION_ORDER.md, guarded by its exact #32164 blob `b5c0bc13a4a266129618230e2434a53f11656e1f` /13769 B. The guide now includes this ninth patch, the new route transition and final pin; its earlier artifact identities are copied from retained completed receipts. No accepted patch is modified.

Publication checks cover complete immutable prepared/native/independent artifact identity and the Commons PR, path set, tree and ordered parents. A predeclared main-equality alias is used only if the observed main equals the verified immutable merge/readback; otherwise the three new or updated artifacts receive full reads at one observed immutable main. These checks do not establish application integration or runtime behavior.

## Attribution

The original source contributors retain attribution and ownership. This is an incremental source proposal and original explanatory documentation, not an upstream change or whole-issue completion. Keep the existing directory's [McLaughlin notice](upstream-licence-mclaughlin.md), [Menke/Laguna notice](upstream-license-menke-laguna.md) and [de Wet notice](upstream-license-de-wet.md) with the source-derived patch. Their exact bytes are unchanged; this is not a repository-wide licensing conclusion.

Earlier provider and body holds, #32074's final changed-files UNKNOWN, and #32122/#32123's custody-loss qualifications remain. The unrelated EmployeeList draft remains unpublished. The current Trustlines source and this new packet's full bytes are retained independently of those older losses.
