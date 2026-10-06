# Retain the provider's default QueryClient across renders

The mounted ReactQueryProvider currently evaluates `client || createQueryClient()` inside its render body. Its own factory returns a new QueryClient. With no supplied client, another invocation of the component therefore selects a newly constructed client. This patch stores the internal default through a lazy React state initializer and keeps the supplied-client expression's precedence.

This is a source-level identity correction. It is not a cache-loss reproduction, a benchmark, a fetched TanStack recommendation, a deployment, or a claim of whole-application correctness.

## Source and exact change

Donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), commit `482ee456369418ef82c4056718cb82d3468f762b`. Path: [src/lib/react-query/provider.tsx](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/lib/react-query/provider.tsx).

| Item | Git blob SHA | UTF-8 bytes |
| --- | --- | ---: |
| Complete canonical provider | e82f8d817df30c321b96c599bf117005a432346e | 2150 |
| Complete candidate provider | 5d7f0bbec251f067f7f68b391c92249a4a52c680 | 2205 |
| change.patch | b022faef6b0acb31d3c481c565b47058c7c22580 | 493 |

A new native directory read identified the provider path/blob/size. One native immutable blob request returned its complete string, without a separate returned SHA field. Independent Git-blob identity calculation matched the requested SHA and size. The one-hunk patch changes +2/-1:

```tsx
const [defaultClient] = React.useState(createQueryClient);
const queryClient = client || defaultClient;
```

React is already imported. The initializer is supplied as a function, rather than called as an argument. The full candidate was constructed by one unique anchored replacement; reversing that replacement reproduced the complete original string exactly. All other source bytes, including the exported factory and exported singleton, remain unchanged.

## Actual caller and scope

Retained complete StateProvider source `5c5e7d7f021bf5e072278a5161d04b0dcbf257d7` / 3190 bytes imports ReactQueryProvider as CustomReactQueryProvider from `@/lib/react-query/provider`. Its JSX renders that provider around its children without a client prop. The retained locale layout `1f016787657313d58504e79bccbe634a843ce8b5` / 4212 bytes renders StateProvider. These are exact retained source facts from prior acquisition, not a new complete caller acquisition or a runtime render count.

The newly acquired provider defines createQueryClient locally as `new QueryClient` with explicit query and mutation defaults. The candidate keeps one selected internal default in React state for an ordinary retained component instance. It selects the supplied client when the existing truthy precedence expression selects it, including later prop replacements; it falls back to the retained internal default when the prop is absent. Unmount/remount, identity resets and development initializer behavior are not a process-wide singleton guarantee.

The unconditional lazy state initializer also constructs an internal default when an explicit client is supplied, whereas the original short-circuit expression avoided that construction. That default may be unused while the supplied client remains present. This tradeoff is explicit; the packet does not claim identical factory call counts for injected-client callers. The observed mounted caller does not supply a client.

The factory's staleTime, gcTime, networkMode, retry/retryDelay, refetch options, mutation policy and throwOnError values remain byte-exact. Their comments and claimed offline behavior are not independently validated here. No change to query keys, query functions, cache contents, request behavior, invalidation, persistence, hydration or cross-tab behavior is promised. The exported module-level singleton remains separate and unchanged.

## Primary contract and failed-source boundary

The [React useState reference](https://react.dev/reference/react/useState) was successfully acquired. It documents that an initializer function supplies the initial retained state and that the initial-state argument is ignored after initialization. It also documents development Strict Mode's possible double initializer invocation, with one result ignored. The candidate's persistence claim is bounded by that React state contract and the actual factory placement in the source.

The exact page `https://tanstack.com/query/latest/docs/eslint/stable-query-client` returned a 400 timeout during this qualification. That route remains held; it was not retried or recovered through another URL, search result, package or source. This guide does not present that unavailable page as consulted guidance. The correction follows directly from the acquired constructor expression and successful React documentation, with no TanStack-specific cache-loss or runtime integration claim.

## Attribution and protected work

A new bounded native path-history request returned only current-path relocation `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888, titled “refactor: flatten frontend/ into repo root, eliminate parent/child duplication.” That is observed relocation metadata, not sole authorship or complete rename-following history. Root's retained map contained no exact provider scope or hold; absence in custody is not universal absence of other work.

ReactQueryLogger's completed message projection (#32145), the shared wrapper retry forwarding (#32137) and mutation-error metadata correction (#32140), and StateProvider's accepted changes remain untouched. A separately observed duplicate rendering of logger/devtools by StateProvider and this provider is not repaired in this patch. No accepted postimage was reconstructed or replayed.

Retained donor instruction context: an earlier complete 959-entry tree reported truncated:false and no AGENTS.md or RULES.md; its full array was lost in the documented working-store reset. That retained summary is not a fresh tree census. The identified docs/CONTRIBUTING.md `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` /274 bytes has EventSource-specific scope. No tests were run in this explicitly source-only lane.

Three differently attributed MIT notices are retained separately: docs/LICENCE.md `57740b9d4d86aedf5d518f2f363d5cf192c54127`, docs/LICENSE.md `af5411fa243cfcf2b61c79d081dbb6204e956041`, and docs/license.md `4a766e268772888af5df56c3f6c608f68558b789`. Their scope is not inferred to cover the entire repository. This Commons packet includes a minimal patch and original guide; it does not republish the full upstream module or claim its authorship.

## Validation and recovery

Performed: exact source acquisition and independent identity, actual retained caller inspection, successful React contract reading, unique anchored transformation, complete unaffected-byte equality, patch and guide identities, frozen publication specification, and immutable publication/final metadata checks described in the completion receipt.

Not performed: compiler/typecheck, lint, tests, fixtures, runtime, browser, cache inspection, query/mutation execution, request dispatch from the application, dependency installation, upstream modification or deployment. No whole-build, runtime-cache, performance or library-integration success is claimed.

The fresh specification, including both exact artifacts, is banked using the existing public checkpoint helper before publication. Its acknowledged manifest and full-spec locator are included in the completion receipt. Private native journals and upstream full bodies are excluded. Native blob acknowledgement is not a branch/ref, indefinite retention or deployment guarantee.
