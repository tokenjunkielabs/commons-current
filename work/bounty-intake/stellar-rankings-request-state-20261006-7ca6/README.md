# Keep ranking requests within their active sort effect

The mounted RankingsPage lets the user switch between holder and volume order while its prior request is still pending. Its original effect writes results and clears loading after every completion, including a completion from a cleaned-up sort mode. It also has no rejection branch, so a rejected result can leave loading active.

This correction owns result, error and loading writes within each effect lifetime. It renders a fixed error when an active request rejects and explains the API helper's existing representative-data fallback.

## Actual complete source

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), immutable commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/rankings/page.tsx` | `63d9d0fcd9e1603a3c10334fbc5f12706da3eb7d` | 5,503 |
| `src/lib/rankings-api.ts` | `8f757beb2ff8b3f963ee3fc32f89321434bf16ec` | 2,909 |

The page is an actual App Router entry. Its existing native buttons set sortBy to holders or volume, and its effect depends on that value. The imported helper includes the selected sort mode in the request query.

The complete helper returns representative sorted assets after caught HTTP or network failures. It returns response.json() directly from its try block; an asynchronously rejected JSON promise can therefore escape that catch and reach the page's await. This patch does not change that helper or choose a new fallback policy.

## Coherent request-state correction

`own-ranking-request-state.patch` is **+16/-3 in two hunks**, affecting only the page.

* Add a nullable error state.
* Give each effect a local active flag, invalidated by its cleanup.
* Preserve the initial loading update, clear the prior error, and guard all post-await result/error/loading writes with that flag.
* Catch active-request rejection and display “Failed to load asset rankings.” after the loading branch.
* Explain that representative rankings may be shown when a backend request fails.

Source identity:
`63d9d0fcd9e1603a3c10334fbc5f12706da3eb7d` (5,503 B)
→ `56ef5d66212629113e0cf292d4c910736032af11` (6,091 B).

A completion belonging to a cleaned-up effect cannot replace the newer effect's results or clear its loading state. The same cleanup also suppresses these writes after unmount. This is a state-ownership guard, not request cancellation.

The helper, endpoint, query parameters, fallback records, sorting, number formatting, mode controls, table, row keys, visible data values and dependency array remain byte-for-byte unchanged. The existing array is retained while another request loads, so the header asset count can still show the prior array length during loading or an error. This correction does not claim a no-flash render boundary between selecting a new mode and its effect cleanup/setup.

The new note describes possible fallback use, not the provenance of a particular response. No response flag, cache, timeout, retry button, schema validation, cancellation, financial-data validation or localization policy is added. Original English-only copy and existing tab semantics remain; no full accessibility acceptance is claimed.

## Primary contract and source validation

The official [React useEffect reference](https://react.dev/reference/react/useEffect) documents cleanup before setup when dependencies change and cleanup on unmount. Its fetching-data example guards completion with a flag set during cleanup because responses may arrive out of order. The page's async form follows that lifecycle contract, guarding success, catch and finally.

The complete serialized patch reconstructs the entire postimage, and its inverse reconstructs the entire preimage. Independent UTF-8 byte counts and Git blob identities match. Retained-string guards confirm exact mode-control and table blocks, preserved dependencies and guarded result/loading writes.

No component, request, fallback generator, browser, timer, synthetic response, fixture, test or build was executed. No installed-runtime, endpoint availability, backend acceptance or actual visible-error behavior is asserted from execution.

## Attribution and overlap limits

Bounded path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`. Earlier contributors retain their rights; no sole-author inference is made.

The dedicated github_search_prs tool was used with repository_full_name woahwhattheheck/commons, query RankingsPage, state all and topn 20. It returned an empty normalized list; no pagination/completeness flag was supplied, so none is claimed. The public Slack RankingsPage search returned zero. These are bounded overlap observations, not a repository-wide absence claim. No held issue-search route was retried or recovered.

The complete donor tree had no root AGENTS/RULES path. EventSource-specific contribution/release guidance does not override the explicit no-tests/no-runtime/no-upstream scope. Differently attributed documentation MIT notices do not establish whole-frontend licensing; this packet publishes only a minimal patch and original attributed guide.

No upstream branch, PR, comment, maintainer assignment, sponsor acceptance, bounty/payment or whole-issue completion is performed or claimed.
