# Keep pool snapshots with their selection attempt

The mounted LiquidityPoolsPage changes its selected pool before awaiting that pool's snapshots. Previously every completion replaced one unkeyed snapshot array, so an earlier request could replace a later selection's chart. A rejected initial request could also leave the whole page loading, while a rejected selection had no error branch.

This patch owns each snapshot attempt and its loading/error state, and gives the initial load an explicit error/cleanup path.

## Complete source and actual caller

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), immutable commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/liquidity-pools/page.tsx` | `b37cf2587695dac374b9c75d577b4b5ec3975434` | 20,164 |
| `src/lib/liquidity-pool-api.ts` | `3db72d8c69173fb8006c59ea240819990b898860` | 8,220 |
| `src/components/charts/PoolPerformanceChart.tsx` | `112d45f786c81c874b7d712a917c21a49150ed34` | 4,944 |

The page is an actual App Router entry. Both its table rows and comparison cards call handleSelectPool. The initial load also selects the first pool. PoolPerformanceChart charts the supplied snapshots directly and does not independently select or validate a pool ID.

The helper catches HTTP/network failures and can return representative pools/stats or randomized sample snapshots. Its direct return of response.json() allows an asynchronously rejected parse promise to propagate to its caller. No helper, request, generator or backend was executed for this assessment.

## Request-state change

`own-pool-request-state.patch` is **+72/-20 in four hunks**, affecting only the page.

* A stable selection callback assigns a fresh object token for every call, including repeated selection of the same pool.
* It immediately selects that pool, clears the previous snapshots, sets snapshot loading and clears the previous snapshot error.
* After the await, only the current token may publish snapshots, an error or the end of snapshot loading.
* The initial effect guards its pools/stats writes with its own active flag, awaits the same selection callback for the first pool, handles rejection, and clears initial loading in finally.
* Cleanup invalidates both the initial effect and any snapshot token.
* The chart area shows loading or a fixed failure message instead of retaining another selection's chart. Selecting the pool again uses the existing controls to retry; initial-load failure has a fixed error view.

Source identity:
`b37cf2587695dac374b9c75d577b4b5ec3975434` (20,164 B)
→ `a62adf63810cb1261e2a0fc006537fa54c5f8c8f` (21,758 B).

The first successful load still selects the first pool and waits for that selection's snapshot attempt before ending the initial page spinner. A snapshot rejection is now represented in the chart area after that spinner, while a pools/stats rejection produces the page error. Successful empty pools retain the existing no-selection behavior. Subsequent selection clears the old chart at the same synchronous point that it changes the selected pool, avoiding reliance on a later effect to hide unrelated data.

The old success/error/finally continuations cannot overwrite a newer token's state, and cleanup invalidates pending continuations. This does not cancel requests or guarantee their settlement. No response schema validation, pool_id filtering, timeout, request deduplication, automatic retry, cache, freshness policy or initial-load retry control is added. A helper response is still accepted according to its existing contract.

All metric values, formatting, sort comparator, pool rows, comparison cards, chart metric buttons, detail display, actual chart implementation and API implementation remain unchanged. Existing pointer-only controls, English-only copy, sample-data policy, literal trend/live labels and financial-data provenance are outside this request-state patch. No pool, wallet, chain, account or payment action is performed.

## Primary contract and static validation

The official [React useRef reference](https://react.dev/reference/react/useRef) documents that the ref object persists across renders, can be mutated in handlers/effects and does not itself trigger rendering. This patch uses it only as an attempt identity; displayed data remains in React state.

The already acquired [React useEffect reference](https://react.dev/reference/react/useEffect) documents cleanup on unmount and before a changed effect's next setup. Its data-fetching example guards asynchronous completion with an inactive flag. The callback is stable with no changing dependencies; the effect names it explicitly. Current documentation is not an installed-runtime test; the retained donor lock identifies React 19.2.7.

The serialized patch reconstructs the full postimage, and its inverse reconstructs the full preimage. Independent Git blob identities and UTF-8 counts match. No application, request, chart, test, fixture, synthetic response, browser or build was executed. No deployment, timing, whole-accessibility or whole-typecheck acceptance is claimed.

## Attribution and bounded overlap

Bounded path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`; earlier contributors retain their rights. The dedicated Commons PR search for LiquidityPoolsPage (all states, topn 20) returned an empty normalized list without a pagination/completeness flag. The public Slack search for that component returned zero and native END. These do not establish global absence or upstream acceptance.

The complete donor tree had no root AGENTS/RULES path. EventSource-specific contribution/release guidance does not override the explicit no-tests/no-runtime/no-upstream scope. Differently attributed documentation license notices do not establish a whole-frontend license. This Commons packet contains a minimal patch and an original attributed guide, not a full-source republishing.

No upstream branch, PR, maintainer assignment, sponsor interpretation, bounty/payment or whole-issue completion is performed or claimed.
