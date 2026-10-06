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

## Continuation: align graph descriptions with supplied data

This continuation preserves #31997 and batches two related presentation corrections in the actual mounted network page and its graph child. The page postimage, complete graph component and complete API route are retained; no graph or data acquisition was executed.

The page's old help text described larger nodes as high-volume or multi-trustline objects, corridor edges as asset-to-asset links with liquidity-depth width, and hover details as performance metrics for any element. The actual source supports a narrower description:

| Visible subject | Actual retained implementation | New page wording |
| --- | --- | --- |
| Nodes | Custom paintNode draws a fixed 12-by-12 rounded square for anchors and radius-4 circle for assets. It does not use node.val for geometry. | Rounded squares represent anchors. Circles represent assets. |
| Connections and width | The API emits source-anchor to asset issuance links, then asset to destination-anchor corridor links. Corridor value comes from volume_usd; the graph passes corridor value to linkWidth. Issuance width stays 1. | Links connect anchors and assets. Corridor line width reflects reported USD volume. |
| Corridor color | API health comes from success_rate; the color accessor uses that value when defined, with unchanged thresholds and fallback. liquidity is not used by that accessor. | Color reflects the available success rate. |
| Hover details | onNodeHover controls a panel containing name, type, and available address or fullName. | Hover over a node to see its name and available identifying details. |

The first card heading becomes "Nodes". Existing drag and wheel instructions remain exact. The correction does not introduce a time window, a measured geometry result or a new scaling policy.

The asset hover panel also always rendered a green dot and "Trading Active", without checking any field. The API's asset-node constructor supplies id, name, type, val, fullName and issuer; it supplies no trading-activity field. Node.status is optional but the badge did not consult it. The patch removes this six-line constant badge. The asset name/fullName and anchor address display remain unchanged. No inactive status is substituted and no trading or account operation is performed.

The [react-force-graph API reference](https://github.com/vasturiano/react-force-graph/blob/master/README.md) documents nodeCanvasObject as the custom painter, its default replacement mode, and linkWidth as a numeric/accessor width. The declared dependency is react-force-graph-2d 1.29.1; the consulted reference is current master, not an inspection of an installed runtime. The visible-copy correction is grounded in the complete application source and these API contracts; browser rendering was not observed.

| Input or output | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Network page after #31997 | c3086b28a2d054fba51840150e13d2d585c7d227 | 12419 |
| Network page with corrected help text | 0bcb0b952bb70725d604f515f8a69f3f0d054b09 | 12288 |
| Original graph child | 635255e9533f791528bf1280fcf59016f8ab039b | 7880 |
| Graph child without constant activity badge | 5adf1a0dc8a7bc2a91259c173f47c21b64bc2bf9 | 7589 |
| Canonical API route, source qualification only | d78b81ee03f4f0de3590d18cc26fc028568bc368 | 3858 |
| Retained API route after independent #32000 nullish guards | 99957f284bae1b382811ece47f4699bce725ee4a | 3932 |
| align-graph-descriptions.patch | feb7af4e40e112972a2ad5e9ba1a05961a7921d4 | 2611 |

The source packet changes two files: page +5/-8 across three hunks, graph child +0/-6 in one hunk. The final combined serialized patch has four hunks and 46 rows, +5/-14 overall. Complete forward and inverse reconstruction matched both file identities. The page's four exact text replacements and the graph's exact badge removal account for every changed byte. The earlier page-only draft was superseded before publication.

The graph data, node painter, link accessors, dimensions, hover state/handlers, controls, styles outside the removed badge, API route, fetchers and chart panels are unchanged. Width normalization, unknown data, graph accessibility, the truth of upstream records and broader chart claims remain outside this change.

Apply default-export.patch first, then align-graph-descriptions.patch. #32000 is a separate API-file correction and its qualification is inherited without replay. A bounded NetworkGraph/caption Commons query returned only the existing grouped index and Slack returned zero rows with native END. Separate NetworkGraph/"Trading Active" queries returned zero Commons and Slack rows, with native END for Slack. These are bounded overlap checks, not global absence claims.

Only the new patch and this exact-preimage-guarded README update are written. Original default-export patch and three MIT notices remain unchanged. No graph, component, canvas, browser, compiler, fixture, tests, workflow or upstream action was executed. Both complete newly written immutable artifacts require native/text/independent identities plus exact PR/files/head/merge/parents/tree/main metadata. An explicit main alias requires fresh exact commit equality; otherwise both changed artifacts are read once at the observed immutable main commit.


## Continuation: bound volume-based corridor line widths

This incremental `bound-volume-link-width.patch` starts from the two retained #32061 postimages below. The original loader patch and the description/badge correction remain intact. Their completed applications are not replayed.

### Actual source and renderer contract

The graph route supplies each corridor link's value from its reported USD volume, with the existing fallback to zero. NetworkGraph previously returned that number directly from its line-width accessor. This mixes a monetary magnitude with a drawing width and provides no upper limit. The issue follows from the producer/accessor/renderer chain; no live oversized payload or rendering incident was observed.

The pinned [force-graph v1.51.4 renderer](https://github.com/vasturiano/force-graph/blob/v1.51.4/src/canvas-force-graph.js), complete blob `a6f7cdd7ace541f7793f75513daf55f25a96a32c` (22712 UTF-8 bytes), groups links by the returned width and assigns the width divided by global scale to the canvas context for ordinary drawing. It adds separate padding for its shadow canvas. The retained lockfile `7ecba249d1b7cd41e629e2fff2782ed6805186f5` pins this version through react-force-graph-2d 1.29.1.

[MDN's canvas lineWidth documentation](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/lineWidth) describes a width in coordinate-space units and states that nonpositive and nonfinite assignments are ignored. Therefore a zero or invalid accessor value must not be described as a reliable way to hide an edge. The new fallback deliberately supplies a valid baseline width.

The current route source is retained at canonical donor `482ee456369418ef82c4056718cb82d3468f762b`, blob `d78b81ee03f4f0de3590d18cc26fc028568bc368`, with the separate #32000 and #32068 graph-record proposals. Neither changes the USD-value producer used for this analysis. This continuation does not modify the API.

### Chosen visual scale

For ordinary non-corridor links, the accessor returns its existing width of 1 without reading the volume property. For corridor links, it uses the existing local Link type instead of an any assertion and selects:

- Baseline width 1 for zero, negative or nonfinite values, including runtime values that are not numbers.
- For a finite positive volume v, width min(6, 1 + log10(1 + v)).

The baseline and cap are explicit presentation choices for readability, not financial thresholds or changes to the reported value. The positive branch is nondecreasing and bounded between 1 and 6 accessor units; very large volumes share the cap. Floating-point rounding may also make nearby values share a width. The logarithm compresses magnitude rather than promising proportional dollar-to-width ratios. No numerical case runner, formula execution or renderer measurement was used to make this source proposal.

The graph-page explanation now identifies the capped logarithmic volume scale, so readers are not invited to interpret width as a linear dollar scale. The existing color explanation remains based on available success rate.

This changes visual width selection, including the baseline handling of nonpositive or invalid corridor values. It does not normalize, rewrite, filter or validate the source data, infer activity or liquidity from width, or claim accurate volume ranking above the cap. Other node/link fields, positions, painter code, hover state, controls, geometry settings, colors, requests and source fallbacks are unchanged.

### Complete incremental identities

| Source | Retained input blob / bytes | New output blob / bytes |
| --- | --- | --- |
| src/components/charts/NetworkGraph.tsx | 5adf1a0dc8a7bc2a91259c173f47c21b64bc2bf9 / 7589 | 1d3d89e31095231f4f1c4868deb480b1941f2aed / 7751 |
| src/app/[locale]/network/page.tsx | 0bcb0b952bb70725d604f515f8a69f3f0d054b09 / 12288 | 94e2979c47e93e9724a47fb511401e87c13beaa1 / 12323 |

The serialized patch is `a457d5c2d5edea09d05c3ac557dd6b5614dba25d`, 1530 UTF-8 bytes. It contains two hunks and twenty-six rows, with nine additions and five deletions. The complete serialized multi-file patch applies forward to both stated outputs and inversely restores both retained inputs. Reversing the exact two selected replacements restores every other source byte.

Consumer application order is the original default-export correction, the description/badge correction, then this new incremental patch, each against its stated input. This instruction is not evidence of repeating an accepted application or executing the application.

### Publication scope

The bounded Commons PR and public Slack queries for NetworkGraph plus linkWidth returned zero rows; Slack reported native END. These observations do not prove global absence, ownership or upstream acceptance. The retained earlier root packets cover other exact hunks and remain protected.

This continuation writes only the new patch and this exact-preimage README continuation. Original patches, source attribution and all three MIT notices remain unchanged. Complete immutable artifact identities and final PR/path/parent/tree observations are required by the publication plan. If an observed main equals the immutable merge readback, the preplanned alias can be used; otherwise both complete files are checked once at that observed main commit.

No application, canvas, graph layout, browser, fixture, compiler, tests, workflow, benchmark or upstream operation was performed. This is a Commons source proposal with a documented visual-scale decision, not a claim of measured throughput, rendered usability, deployment or reward.
