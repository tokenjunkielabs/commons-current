# Release the StateDevTools global only when the effect still owns it

The mounted StateDevTools development effect assigns an object containing store and query-client callbacks to `window.__stateDevtools`. It currently returns no cleanup. The assigned global can therefore continue to hold that effect's object after its cleanup boundary. This patch names the exact object locally and removes the global during cleanup only if it still refers to that object.

The comparison protects a replacement installed by a newer effect or another owner: an older cleanup does not delete a different current object. This is source-level lifecycle reasoning; no window, browser, logging, query or cache operation was executed.

## Exact source boundary

Donor repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), immutable commit `482ee456369418ef82c4056718cb82d3468f762b`. Production path: [src/components/StateProvider.tsx](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/components/StateProvider.tsx).

| Input or artifact | Git blob SHA | UTF-8 bytes |
| --- | --- | ---: |
| Complete canonical StateProvider | 5c5e7d7f021bf5e072278a5161d04b0dcbf257d7 | 3190 |
| Retained #32161 postimage: immediate input | e8b2a043edd35ad8ddfa677fb5cabad715f39922 | 2982 |
| Cleanup after retained #32161 | 1f0f4495ed064d7ce4277109e6ec3d68da4776ca | 3172 |
| change.patch | 3c709cdf721a26db3e20b97359feaaef3f66a861 | 920 |

The complete canonical string was acquired and independently matched for the preceding distinct instrumentation-owner task. This task directly loads that task's retained complete #32161 postimage as its immediate input; it does not reapply the accepted patch or request source again. The earlier canonical acquisition returned content bound to the exact requested blob without a separate returned SHA field. The #32161 postimage is a locally retained derived source identity, not a claim that this blob is deployed in the donor repository.

The patch has two hunks, +8/-1. It replaces the direct object assignment with `const debugTools = {`, preserving the complete object contents, assigns that object to the existing global, and returns cleanup:

```tsx
(window as any).__stateDevtools = debugTools;

return () => {
  if ((window as any).__stateDevtools === debugTools) {
    delete (window as any).__stateDevtools;
  }
};
```

Both source anchors were unique. Reversing the two replacements reproduced the entire retained #32161 input exactly. The complete object-member region and the entire suffix beginning with the original effect dependency line remain byte-identical.

## Actual consumer and lifetime

StateProvider renders StateDevTools within CustomReactQueryProvider. The retained locale layout, canonical `1f016787657313d58504e79bccbe634a843ce8b5` /4212 bytes, renders StateProvider around route content. The layout relationship is retained source provenance rather than a fresh whole-layout acquisition or a runtime mount observation.

StateDevTools reads the store and query client, then its effect assigns the public debugging object only in development. The object exposes the store, reset/log operations and query-client diagnostics. The effect depends on store and queryClient. Its existing assignment can replace an earlier global, but its former absence of cleanup does not remove the last assigned object when that effect is cleaned up.

The [React useEffect reference](https://react.dev/reference/react/useEffect), successfully acquired for earlier actual lifecycle work and reused as retained primary guidance, documents cleanup before a changed-dependency setup and when the component is removed. It also describes development Strict Mode's additional setup/cleanup cycle. The new identity comparison is synchronous: cleanup reads the current global and deletes only a matching object.

This correction does not roll back the previous global value or restore another owner. It does not invalidate independently retained references, cancel an already invoked debug callback, make debug actions safe, or establish that all possible writers follow the same ownership convention. It makes no whole-window teardown or memory benchmark claim. When the current global is a different object, this cleanup leaves it alone. When the effect is outside development, its existing branch behavior remains unchanged.

No object member, query method, logger invocation, StateDevTools return value, useDebugTools hook, effect dependency or production enablement condition is changed. In particular, this packet does not repair or reinterpret the separately held store API suspicion or the existing performance metric calculations.

## Composition and superseded preparation

The immediate input is the actual complete retained postimage from [Commons #32161](https://github.com/woahwhattheheck/commons/pull/32161), which removed separate ReactQueryLogger/ReactQueryDevtools imports and direct JSX mounts. This cleanup is authored directly on that retained string. The entire import/render portion remains byte-identical to #32161; its instrumentation removal is preserved without reapplying that accepted change.

The earlier accepted #31962 export correction and #31968 QueryCache correction remain protected. Their complete postimages were lost in the shared working-store reset and have not been reconstructed. Accordingly, the new candidate is composed after the retained #32161 candidate, but is not represented as fully composed with #31962/#31968. This packet publishes a narrow effect cleanup diff, not a full replacement module. An integrator must preserve those separate protected export/QueryCache changes.

Before any branch publication, an initial canonical-only cleanup preparation was superseded in favor of the retained #32161 input. Its public checkpoint manifest was `34c8464550b3681f57a12f57aa1b4b7cab6a866d`, full specification `cb1dffb7a482223e43d19521f908351ad7852bf0` /10402 bytes, and candidate `09d5096b8a0640ae7f4a31382ffcbcdf1cf4a782` /3380 bytes. These are preserved historical preparation records, not an earlier publication attempt. No branch, PR or merge was dispatched from that specification. The revised checkpoint links that previous manifest, and the existing activity message is amended instead of resent.

The private source directory retains both the direct #32161 input and the superseded preparation. This guide does not upgrade old pre-reset pin/excerpt custody to surviving full accepted #31962/#31968 postimages.

## Attribution and instruction context

The retained native path-history response acquired for #32161 returned only current-path relocation `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888 and titled “refactor: flatten frontend/ into repo root, eliminate parent/child duplication.” It is reused without another history request. That is relocation metadata, not sole authorship or complete rename-following history.

Root's retained completion map had no exact owner-checked __stateDevtools cleanup. That bounded absence is not global proof of no other work. All previous source, documentation and ownership holds remain intact, including the failed Zustand and stable-query-client documentation routes.

An earlier complete donor tree reported 959 entries, truncated:false and no AGENTS.md/RULES.md. Its full array was lost in the documented reset, so only the retained instruction summary is used. Identified docs/CONTRIBUTING.md `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` /274 bytes has EventSource-specific scope. This authorized lane remains source-only; no test execution is implied.

The three differently attributed MIT notices remain separately identified: docs/LICENCE.md `57740b9d4d86aedf5d518f2f363d5cf192c54127`, docs/LICENSE.md `af5411fa243cfcf2b61c79d081dbb6204e956041`, docs/license.md `4a766e268772888af5df56c3f6c608f68558b789`. No repository-wide scope is inferred. The deliverable is an attributed small patch and original guide, with no full upstream module republication.

## Validation and recovery

Performed: retained complete-source inspection, independent candidate/patch/guide identities, unique anchored transformation, exact reverse comparison, unchanged object-members and suffix checks, frozen artifact specification, and the native publication/readback checks recorded in the completion receipt.

Not performed: compiler/typecheck, lint, tests, fixtures, application/browser/window execution, query/log/cache/API/account action, dependency installation, upstream modification or deployment. There is no runtime proof, whole-build claim, measured memory reduction or global cleanup guarantee.

The new frozen artifact specification is banked through the existing public checkpoint helper before branch publication. Its acknowledged manifest and full-spec identities are reported in the completion receipt. Private native journals and complete upstream modules are not included. An acknowledged unreferenced blob does not establish a branch/ref, indefinite retention or deployment.
