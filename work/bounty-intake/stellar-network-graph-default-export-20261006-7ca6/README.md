# Match the NetworkGraph loader to its default export

## Connected source mismatch

The Network route declares a client-side dynamic NetworkGraph loader. Its import promise returns a module-shaped object whose default member is selected from m.NetworkGraph. The complete imported component instead declares a local NetworkGraph constant and ends with export default NetworkGraph; it supplies no named NetworkGraph export.

Consequently, the caller selects a member that this source module does not export. The route later renders the dynamically loaded component with its existing graph data. This is a direct caller/export mismatch established from both complete source bodies; no live browser failure or successful graph render was observed.

## Complete source identities

Donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/app/[locale]/network/page.tsx | cfcb9fba468523f2e5069002680a4f4c7c8e4802 | 12424 |
| src/components/charts/NetworkGraph.tsx | 635255e9533f791528bf1280fcf59016f8ab039b | 7880 |

The complete source bodies match their native and independently calculated Git blob identities. Current-path history for the caller returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888. Relocation history does not establish sole authorship. Original source attribution and the three acquired MIT notices are preserved.

## One-line correction

The patch changes only the selected member inside the existing adapter:

```diff
-      default: m.NetworkGraph,
+      default: m.default,
```

The import path, promise adapter shape and ssr: false option remain intact. The existing default member now receives the component that the imported module actually exports.

The [official Next.js lazy-loading guide](https://nextjs.org/docs/app/guides/lazy-loading) documents next/dynamic default component imports and separately shows selecting named exports from the resolved module. Its distinction supports selecting the module's actual export. The acquired documentation describes Next.js 16.3.8, while the donor manifest/lock specify Next.js 16.2.10. This is supporting API documentation, not an execution result against the installed donor version.

The five other chart loaders in NetworkPage deliberately select named exports. Their complete acquired component sources do provide those named exports; this patch does not change those adapters. There is no blanket conversion of chart imports.

## Exact patch and scope

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Complete caller preimage | cfcb9fba468523f2e5069002680a4f4c7c8e4802 | 12424 |
| Complete caller postimage | c3086b28a2d054fba51840150e13d2d585c7d227 | 12419 |
| default-export.patch | 4223f38285aca5fc5bc812c892dc20933429c531 | 376 |

The actual serialized unified patch has one hunk and eight rows, with one addition and one deletion. Forward application exactly reconstructs the complete postimage; inverse application exactly restores the preimage. Replacing the one edited member restores every other caller byte.

All fetch functions, endpoint choices, loading and error state, graph data construction, five series panels, UI text and graph-rendering implementation remain unchanged. The imported graph's existing resize-listener cleanup is already present and needs no change in this packet. Earlier Commons #31985 chart calendar labels and #31989 nullish network rows affect separate source files.

Apply default-export.patch at the donor repository root to the exact caller preimage. The adapter correction does not establish live graph data availability, rendering, force-graph compatibility or whole-build success. No dynamic import, application request, compiler, browser, package installation, fixture, tests or workflow was executed.

## Notices and publication boundary

| Unchanged notice | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| upstream-licence-mclaughlin.md | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| upstream-license-menke-laguna.md | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| upstream-license-de-wet.md | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |

This is an attributed Commons source proposal. It does not modify upstream, deploy a site or establish acceptance, ownership or reward eligibility. Bounded exact-name Commons and Slack overlap queries returned zero results, with native END for Slack. Internal custody supplied no exact export-link completion or hold; these bounded observations do not certify global absence.

Publication requires complete immutable artifact bodies and native plus independent blob identities, followed by final PR, changed-file, merge and main metadata. The preselected main-equals-merge shortcut applies only when the observed main commit exactly equals the merge. Otherwise every artifact is read once at the observed immutable main pin. The actual publication outcome belongs in its separate release and grouped index.
