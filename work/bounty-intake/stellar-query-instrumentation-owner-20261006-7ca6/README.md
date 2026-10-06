# Keep React Query instrumentation at its provider

StateProvider directly renders ReactQueryLogger and ReactQueryDevtools inside CustomReactQueryProvider. The actual implementation of CustomReactQueryProvider renders its children and then another ReactQueryDevtools and ReactQueryLogger. This patch removes only StateProvider's two redundant component imports and two direct JSX mounts. The provider remains the owner of one logger and one devtools instance in this acquired composition.

The correction is supported by the complete caller and provider source. It does not claim an observed production warning rate, a measured performance gain, runtime execution or deployed behavior.

## Exact source and patch scope

Donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at `482ee456369418ef82c4056718cb82d3468f762b`.

| Source or artifact | Git blob SHA | UTF-8 bytes |
| --- | --- | ---: |
| src/components/StateProvider.tsx canonical | 5c5e7d7f021bf5e072278a5161d04b0dcbf257d7 | 3190 |
| StateProvider standalone canonical candidate | e8b2a043edd35ad8ddfa677fb5cabad715f39922 | 2982 |
| src/lib/react-query/provider.tsx canonical dependency | e82f8d817df30c321b96c599bf117005a432346e | 2150 |
| src/lib/react-query/logger.tsx canonical dependency | 9fe329c0fdd763c977c572da550e94a16aa80552 | 3578 |
| change.patch | a83eeab2935c9d1156ad00c268134ba134c0e5f7 | 839 |

[Canonical StateProvider](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/components/StateProvider.tsx) was acquired once as new input to this duplicate-mount task. Its full string independently matched the exact request-bound native blob and size. The native blob response did not expose a separate SHA field. The provider and logger dependency strings were already fully acquired, read and independently matched during the immediately preceding genuine source tasks, so their retained bytes were reused.

The patch is two import/render hunks, +0/-4. It removes the ReactQueryDevtools and ReactQueryLogger imports from StateProvider, plus its direct `<ReactQueryLogger />` and `<ReactQueryDevtools initialIsOpen={false} />` elements. StateProvider continues to render CustomReactQueryProvider, all supplied children and StateDevTools in their original order. The remaining StateDevTools/useDebugTools source suffix is byte-exact against the canonical input.

## Custody and composition limit

Earlier work had acquired complete StateProvider source, but its full string and the accepted #31962/#31968 postimages were lost in the shared working-store reset. Before this new read, active custody held its exact pin, import/render excerpts and prior acquisition provenance, not a surviving full canonical string. The preceding #32145/#32148 guides relied on those retained caller facts and did not claim a fresh full-file caller read.

This new task acquired the canonical module for a separate top-level JSX/import question. The candidate identity in the table is a standalone transformation of that canonical blob. It is explicitly not the fully composed result after the earlier duplicate-export (#31962) and QueryCache-filter (#31968) corrections. Those accepted bytes were not reconstructed, replayed or replaced. The deliverable is a narrow diff; applying a full standalone candidate over accepted work would be inappropriate.

The patch's import/render hunks do not select the final useDebugTools export or the QueryCache find implementation. Those completed scopes remain protected. No accepted-source verification was performed. The held Zustand contract and the separate shared-store suspicion remain untouched.

## Actual component ownership

The exact StateProvider import aliases ReactQueryProvider from `@/lib/react-query/provider` to CustomReactQueryProvider. Its JSX places the two direct instruments beneath that component. The newly acquired dependency, canonical e82f8d81, returns a QueryClientProvider containing children, ReactQueryDevtools and ReactQueryLogger. Therefore the acquired composition contains two instances of each instrument before this patch.

The retained locale layout, blob `1f016787657313d58504e79bccbe634a843ce8b5` /4212 bytes, imports and renders StateProvider around its route content. This is retained source provenance, not a new whole-layout acquisition or browser observation.

The logger module's effect establishes a 30000 ms interval, reads the query cache, filters error-status queries and conditionally logs warning metadata; cleanup clears the interval. Two rendered logger instances each own that effect. Removing the redundant direct instance removes its source-level periodic scan while retaining the provider's logger. Warnings still depend on cached errors and the shared logger's existing enablement policy. No fixed reduction in output, observed timing, workload benchmark or complete absence of other logger mounts is claimed.

The already completed #32145 message projection changes the logger's error metadata representation only, and #32148 changes the provider's retained internal client only. Both preserve the component ownership/interval behavior relevant here. Their accepted patches are not reapplied or modified by this packet. The ReactQueryDevtools package itself was not executed or inspected for internal behavior; the demonstrated change is removal of its redundant JSX instance in this particular composition.

The [React useEffect reference](https://react.dev/reference/react/useEffect), successfully acquired earlier for actual lifecycle work and reused as retained primary guidance here, describes setup when a component is added and cleanup when it is removed, including development Strict Mode's extra setup/cleanup cycle. This packet does not equate source instance counts with measured production event counts.

## History, instructions and attribution

A new bounded current-path history request returned one relocation entry, `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888, titled “refactor: flatten frontend/ into repo root, eliminate parent/child duplication.” That is relocation metadata, not sole authorship or complete rename-following history. Root had no newly known exact same-hunk duplicate correction; retained custody gaps were not treated as universal absence of other work.

The earlier complete donor tree reported 959 entries, truncated:false and no AGENTS.md/RULES.md. The complete array was lost in the documented reset, so this is a retained instruction summary rather than a new census. Identified docs/CONTRIBUTING.md `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` /274 bytes concerns EventSource-specific work. No tests were run in this explicitly source-only lane.

Three differently attributed MIT notices remain separately scoped: docs/LICENCE.md `57740b9d4d86aedf5d518f2f363d5cf192c54127`, docs/LICENSE.md `af5411fa243cfcf2b61c79d081dbb6204e956041`, and docs/license.md `4a766e268772888af5df56c3f6c608f68558b789`. No repository-wide license scope is inferred. The Commons artifacts are this original guide and a small attributed diff, not a republished upstream module.

## Validation and recovery

Performed: new complete immutable caller acquisition, independent blob identity, retained complete dependency inspection, exact four-line removal with unique anchors, unchanged remaining suffix, patch/guide identities, frozen publication spec and the native immutable/final checks recorded in the completion receipt.

Not performed: compiler/typecheck, lint, tests, fixtures, application/browser execution, logging, query/cache/API/account operations, dependency installation, upstream modification or deployment. The source still has separately protected and unselected concerns; this packet does not claim whole-build or global instrumentation correctness.

The fresh complete artifact spec is banked using the existing public checkpoint helper before branch publication. Its acknowledged manifest and spec identities are reported with the completion receipt. Private raw responses, journals and complete upstream modules are excluded. An acknowledged blob is not a branch/ref, indefinite retention or deployed acceptance guarantee.
