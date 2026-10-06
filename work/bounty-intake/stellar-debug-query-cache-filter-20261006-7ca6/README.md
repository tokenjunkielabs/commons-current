# Use the query-cache filter contract in the mounted debug action

The development-only `window.__stateDevtools.getQueryData(queryKey)` action passes a bare predicate function to TanStack Query's `QueryCache.find`. The actual dependency is TanStack React Query 5.100.5, whose v5 API uses a filter object. This patch supplies `{ queryKey, exact: true }`, preserving the action's existing `string[]` parameter and `query?.state.data` return.

This is a separate source-level API correction to the existing mounted developer tool. No query cache, application, browser, compiler, test, fixture, build, workflow, or network query was executed to exercise it. No observed runtime result or whole-build success is claimed.

## Source and composition

Repository: https://github.com/Stellar-Analysis/frontend

Pinned upstream donor: `482ee456369418ef82c4056718cb82d3468f762b`.

| Role | Path | Git blob SHA | UTF-8 bytes |
| --- | --- | --- | ---: |
| Complete upstream module | `src/components/StateProvider.tsx` | `5c5e7d7f021bf5e072278a5161d04b0dcbf257d7` | 3190 |
| Required composed preimage from Commons #31962 | same path | `0e1dcc03a89c254787636dbed3afe933abbcf5da` | 3175 |
| Candidate postimage | same path | `b2c88faf1454af6d44373662b209a04a724a1b82` | 3141 |
| Retained actual mounted caller | `src/app/[locale]/layout.tsx` | `1f016787657313d58504e79bccbe634a843ce8b5` | 4212 |

Apply this continuation after [Commons #31962](https://github.com/woahwhattheheck/commons/pull/31962), whose [patch](../stellar-stateprovider-single-export-20261006-7ca6/change.patch) removes the repeated final hook export. The upstream donor has not been claimed to contain either Commons patch. The candidate retains that prior export correction exactly.

The complete upstream module was transferred from CI's retained native source and independently hashed after its exact transcription correction; the earlier transfer discrepancies remain privately preserved. The composed preimage is the already retained candidate from #31962, not a reacquired accepted artifact or replayed application check.

The locale layout directly imports and renders StateProvider around the application content. StateProvider renders StateDevTools inside CustomReactQueryProvider. In development mode its effect attaches the actual `getQueryData` callback to `window.__stateDevtools`. This establishes a connected source consumer; it does not claim the browser callback was invoked during this task.

## Exact dependency evidence

Root's retained complete donor `package.json`, blob `2b1c6ac1f83096666c7fd6d5ba3fd22780e6b8eb`, declares `@tanstack/react-query` as exactly `5.100.5`. The retained complete `pnpm-lock.yaml`, blob `7ecba249d1b7cd41e629e2fff2782ed6805186f5`, records importer specifier `5.100.5` and resolution `5.100.5(react@19.2.7)`. Devtools is also 5.100.5 with React Query 5.100.5. These facts were transferred from actual retained source; no dependency installation or replacement resolution was performed.

## Contract and change

The primary [TanStack v5 migration guide](https://tanstack.com/query/latest/docs/framework/react/guides/migrating-to-v5) shows the `queryCache.find` filter-object signature introduced in v5. The official [QueryCache reference](https://tanstack.com/query/latest/docs/framework/react/reference/classes/QueryCache#find) takes filters containing a query key and returns the matching query or undefined. The official [query-filter guide](https://tanstack.com/query/latest/docs/framework/react/guides/filters) distinguishes an exact query-key match from inclusive key matching and places optional predicates inside the filter object.

The original code instead supplies an Array.find-style function:

```tsx
queryClient.getQueryCache().find(({ queryKey: key }) =>
  JSON.stringify(key) === JSON.stringify(queryKey)
)
```

The new argument supplies the action's existing key through the library's documented exact-key filter. It keeps the synchronous cache lookup and optional return behavior. It does not fetch, create, refetch, invalidate, remove, or rewrite any query. No claim is made about which entry an unsupported predicate argument happened to return in a running application.

The patch has four additions and three deletions. It changes only this lookup's argument. The debug-tool availability condition, effect dependencies, public callback name, `string[]` input, result expression, other actions, logger calls, query metrics, state access, and prior named-export repair remain unchanged.

## Attribution and boundaries

The already acquired bounded path history identifies [christabel888's root relocation 59fad72d](https://github.com/Stellar-Analysis/frontend/commit/59fad72d9fbef9cfd6f47e215392da44488fcdc4). [yosemite01's merged PR #116](https://github.com/Stellar-Analysis/frontend/pull/116) changed the StateProvider logging calls and supplied the same upstream module blob; those contributions are retained. This continuation does not repeat the earlier source/history/provider reads solely to validate accepted work.

The distinct `logState` / Zustand API suspicion remains unmodified. Its primary documentation route failed, and neither this TanStack lookup nor this publication clears or recovers that held contract. Other debug-tool metrics and lifecycle questions remain outside this patch.

The donor has no established repository-wide license from the available differently attributed MIT notices, so this packet publishes a narrow patch and guide rather than the complete module. The verbatim notices remain in the [prior generator packet](../stellaranalysis-issue-generator-layout-20261006-7ca6/): McLaughlin `57740b9d4d86aedf5d518f2f363d5cf192c54127`, Menke/Laguna `af5411fa243cfcf2b61c79d081dbb6204e956041`, and de Wet `4a766e268772888af5df56c3f6c608f68558b789`; their individual scope is not broadened.

This is a Commons source continuation only. No upstream claim, assignment, pull request, deployment, award, or acceptance action is made. Native artifact readbacks and independent identities establish publication of these bytes, not runtime correctness or an all-green build.
