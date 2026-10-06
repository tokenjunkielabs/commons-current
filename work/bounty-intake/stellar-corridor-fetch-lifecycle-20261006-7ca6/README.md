# Ignore corridor results after their effect becomes inactive

The mounted corridor listing fetches rows in an effect depending on `timePeriod` and `sortBy`. Its original success path, mock fallback, and final loading update all write component state after the awaited request, without an effect cleanup. If an older request settles after the old effect has been replaced, it can replace rows from a newer request or clear the newer run's loading state.

This patch gives each effect setup its own `inactive` flag, guards the three completion state writes, and marks the flag during cleanup. It does not abort requests, change request arguments, or change the current effect's success/fallback policy.

## Acquired input and exact change

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).

Donor commit: `482ee456369418ef82c4056718cb82d3468f762b`.

Source path: `src/app/[locale]/corridors/page.tsx`.

| Image | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Complete acquired canonical preimage | `a14fe86977c4071ad958ddc3f206b4f07134b072` | 17,815 |
| Canonical source plus this lifecycle hunk | `158ab0f3b4f3a9c70dee980f94c6fe2b3961f0ff` | 17,937 |

The source was read once as a complete immutable native Git blob for this new task. Its explicit request-bound SHA and independently computed Git blob identity match; the blob endpoint returns content without a separate response SHA. This packet does not invent such a response field.

The patch is +9/-3, in one hunk surrounding the first fetch effect. Both images preserve the canonical file's ending. The complete prefix before that effect and suffix after it are byte-exact; exact text reconstruction of the actual patch yields the stated postimage. No runtime transformation of the application was executed.

## Actual caller and lifecycle

This file is the App Router corridor-listing entry. Its default export renders `CorridorsPageContent` inside the existing ErrorBoundary and Suspense. The content component reads `prefs.corridorsTimePeriod` and `prefs.corridorsSortBy`; the two rendered select controls update those preferences. Both values are dependencies of the affected effect and are placed into its existing request filters.

The original nested control flow is retained: loading becomes true synchronously, `getCorridors(filters)` is awaited, success supplies the returned rows, the inner catch supplies `mockCorridors`, the outer catch logs, and finally clears loading. The changes are limited to:

- An effect-local flag initialized to false before the async function starts.
- A flag check before `setCorridors(result)`.
- A flag check before `setCorridors(mockCorridors)`.
- A flag check before `setLoading(false)`.
- A cleanup that sets this run's flag to true.

Each setup owns a distinct lexical binding. Cleanup of an earlier run cannot mark the replacement run inactive, and replacement setup cannot reactivate the earlier run. The initial `setLoading(true)` executes synchronously during that setup before its first await; it remains unchanged.

React's primary [useEffect reference](https://react.dev/reference/react/useEffect) documents that cleanup for old dependency values runs before replacement setup and also runs on unmount. Its data-fetching section shows an effect-local ignore flag to prevent later responses from an obsolete request from writing state. This patch applies that lifecycle pattern to the actual listing's success, fallback, and finally paths. These are static source/contract findings, not observed timings or an executed response-order experiment.

The guarantee begins when cleanup marks this effect inactive. This is not a claim that selecting a preference synchronously cancels all older work before React processes the lifecycle. Requests remain in flight and may complete; existing outer logging can still occur. The patch introduces no abort controller, retry, queue, cache, request deduplication, timeout, or new error policy.

## Preserve the other listing continuations

Root supplied the concrete source lead and reports two completed disjoint continuations on this same canonical file:

- [Commons #32036](https://github.com/woahwhattheheck/commons/pull/32036): heading disclosure for simulated metrics.
- [Commons #32037](https://github.com/woahwhattheheck/commons/pull/32037): three aria-label attributes.

Their reported scopes are later JSX, outside this effect hunk. Those artifacts were not reacquired, reconstructed, or replayed for this packet. The identity table binds the canonical donor plus this patch only; it is not an aggregate postimage claim for those prior continuations.

Integrate the localized lifecycle hunk while retaining the already accepted disclosure and label edits. Do not replace a composed file with the canonical-plus-lifecycle source image. If another source revision changes the fetch effect itself, compare that actual hunk before integration rather than treating the whole-file donor identity as current composed source.

The random live-tick simulation remains byte-exact, including its interval and row updates. The separate insights fetch and mock generation also remain unchanged. This packet does not supply real telemetry, remove simulation, establish storage/persistence, improve insights lifecycle, or claim that every displayed row is a fresh backend observation. Pagination, filtering/sorting formulas, exports, route links, preferences, request filters, logging text, dependency list, and UI rendering are untouched.

## Validation and delivery boundary

The complete source was read; the exact affected effect and the actual preference controls were inspected; the primary lifecycle contract was acquired. Validation is limited to exact source transformation/reversal, actual diff text reconstruction, and Git blob/UTF-8 identities. No application, effect, request, API service, browser, network simulation, compiler, typecheck, lint, test, fixture, build, workflow, or executor was run. No runtime acceptance, measured request savings, or whole-build success is claimed.

Only a focused patch and this guide are published. The differently attributed retained license notices do not establish a repository-wide license scope, so the complete donor module is not republished. Existing attribution remains in [the prior generator packet](../stellaranalysis-issue-generator-layout-20261006-7ca6/). Source/ownership coordination concerns actual hunks and in-flight writes; it is not an added approval gate. No upstream submission, claim, account, payment, credential, or permission action is part of this continuation.
