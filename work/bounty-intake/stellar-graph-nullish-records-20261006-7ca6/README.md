# Skip absent records before building the network graph

## Actual producer and consumer

The NetworkPage client fetches /api/network-graph, rejects a non-OK response and displays the existing unavailable state. The acquired route fetches backend anchors and corridors, creates anchor/asset nodes and links, validates the resulting graph, and returns JSON. Its outer catch logs the error and returns an empty graph with status 500.

Both input loops first check Array.isArray, but immediately access fields on every element. An array containing null therefore passes the array check and throws at anchor.id or corridor.source_anchor_id. The whole request then follows the error response even when other rows contain useful records. Callback type annotations do not validate the parsed JSON elements.

This failure path is established from complete connected source, not an observed live backend payload or a reproduced runtime incident.

## Complete source identities

Donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/app/api/network-graph/route.ts | d78b81ee03f4f0de3590d18cc26fc028568bc368 | 3858 |
| src/types/network-graph.ts | 2fb2aa949a94ca85ace30146c7b9009cfa78fd5e | 866 |
| src/app/[locale]/network/page.tsx | cfcb9fba468523f2e5069002680a4f4c7c8e4802 | 12424 |

Complete route and type bodies match their native and independently calculated blob identities. The complete caller is retained with the same exact donor identity. Its separate #31997 loader correction does not change the request or response behavior discussed here.

Current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888. This is not sole-authorship evidence. Original attribution and all three acquired MIT notices are preserved.

## Two early returns

The patch adds one statement at the start of each existing forEach callback:

```ts
if (anchor == null) return;
if (corridor == null) return;
```

Each statement belongs to its corresponding callback. A return skips that absent row and allows the existing loop to continue. Rows without the currently required identifiers already contribute nothing through the existing inner conditions; the patch extends this established skip behavior to nullish elements before property access.

The [TypeScript equality-narrowing documentation](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#equality-narrowing) documents that equality with null also matches undefined. Parsed JSON can supply null; the guard additionally handles an undefined element if one reaches this code. No truthiness-based rejection of ordinary non-nullish rows is introduced.

The acquired validateNetworkGraphData function checks that nodes and links are arrays. It is called after construction, so it cannot protect the earlier row property reads. This packet leaves that validator unchanged and makes no stronger graph-schema claim.

## Serialized patch checks

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Complete route preimage | d78b81ee03f4f0de3590d18cc26fc028568bc368 | 3858 |
| Complete route postimage | 99957f284bae1b382811ece47f4699bce725ee4a | 3932 |
| skip-nullish-records.patch | 74480826e71ba69c0f1c0e3cf78dfb71f6c4ce4a | 873 |

The actual serialized patch has two hunks and fourteen rows, with two additions and no deletions. Forward text application exactly reconstructs the postimage, and inverse application exactly restores the preimage. Removing the two inserted guards restores every other route byte.

Fetch URLs/options, Promise.all, HTTP-status checks, JSON parsing, node keys and ordering, required-field conditions, value fallbacks, link construction, validator, logs and response statuses remain unchanged. Existing non-nullish records follow their original paths. Other malformed records, missing linked nodes, throwing accessors and later errors retain their original behavior; this is not full input validation or an all-input recovery guarantee.

Apply skip-nullish-records.patch at the donor repository root to the exact preimage. No route, loop, request, JSON response, compiler, browser, fixture, tests or workflow was executed. Source text checks do not establish backend availability, graph rendering or whole-build success. #31989 guarded separate time-series normalizers in src/lib/network-api.ts; it did not modify this graph route.

## Publication and notices

| Unchanged notice | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| upstream-licence-mclaughlin.md | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| upstream-license-menke-laguna.md | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| upstream-license-de-wet.md | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |

Bounded Commons and Slack queries for this route/nullish scope returned zero rows, with native END for Slack. Internal custody retained no exact same-hunk correction or hold. These observations are not global absence, ownership, acceptance or reward clearance.

This is an attributed Commons source proposal with no upstream mutation or deployment. Publication verification requires all five complete immutable artifact bodies, native plus independent identities and exact final PR/files/merge/main metadata. An exact observed main-equals-merge identity may reuse the immutable reads; otherwise each artifact is read once at the observed main commit. Actual verification is recorded in the release and grouped index.


## Continuation: require admitted anchor endpoints

The original nullish-row proposal above is preserved. This new, incremental `require-anchor-endpoints.patch` starts from its retained route postimage `99957f284bae1b382811ece47f4699bce725ee4a` (3932 UTF-8 bytes). Its earlier missing-linked-nodes limitation is the subject of this continuation; the original patch is neither changed nor replayed.

### Source-established failure path

An anchor becomes a node only when both its identifier and name pass the existing condition. A corridor previously needed only truthy source and destination identifiers, then created its asset node and two links. There was no check that either identifier referred to an admitted anchor. An omitted anchor, or one rejected by the existing name requirement, can therefore leave an emitted link with no matching node. The retained validator checks the two arrays but does not resolve link endpoints.

The complete NetworkGraph component passes this data to ForceGraph2D without overriding the default node or endpoint identifiers. The acquired lockfile pins the dependency chain to react-force-graph-2d 1.29.1, force-graph 1.51.4 and d3-force-3d 3.0.6. These are source and lockfile observations, not installed-runtime measurements.

Pinned primary library source establishes the corresponding consumer contract:

- [force-graph v1.51.4 canvas-force-graph.js](https://github.com/vasturiano/force-graph/blob/v1.51.4/src/canvas-force-graph.js) installs the D3 link force, defaults to the id/source/target properties, and supplies graph nodes followed by links with the configured node identifier accessor.
- [d3-force-3d v3.0.6 link.js](https://github.com/vasturiano/d3-force-3d/blob/v3.0.6/src/link.js) builds a map of nodes by identifier and resolves nonobject link endpoints from it. Its lookup throws when an endpoint is absent.

| Complete retained source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/components/charts/NetworkGraph.tsx | 635255e9533f791528bf1280fcf59016f8ab039b | 7880 |
| pnpm-lock.yaml | 7ecba249d1b7cd41e629e2fff2782ed6805186f5 | 359885 |
| force-graph v1.51.4 src/canvas-force-graph.js | a6f7cdd7ace541f7793f75513daf55f25a96a32c | 22712 |
| d3-force-3d v3.0.6 src/link.js | c99d07b5aba2889b14e9efca739744917b053413 | 3688 |

The route and type identities are listed in the original source table. The separate #32061 component copy correction removes an unconditional badge; it does not alter the graph-data or identifier wiring discussed here.

### Change and behavior

Inside the existing condition requiring both corridor identifiers, the new guard returns from the current callback unless both mapped nodes have type anchor. It precedes asset creation and both link pushes. A skipped corridor contributes neither a new orphan asset nor its two links; an asset already created for another accepted corridor remains intact. Other corridors continue to be processed.

Checking the mapped type matters because this map also accumulates asset nodes. Mere key membership would not establish that an endpoint is an admitted anchor. The lookup uses the existing identifier values and Map equality; it introduces no coercion, fabricated anchor or new asset-key convention.

For corridors whose two endpoints are admitted anchors, the asset construction, insertion order, link data and fallbacks follow the unchanged original statements. Existing nullish guards remain in place. The patch does not define a broader malformed-value, identifier-collision, duplicate-anchor, asset/anchor key-collision, health, width or aggregation policy. It does not prove that every possible backend payload is valid or that no other graph error can occur.

### Exact incremental artifact

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Route input after original nullish proposal | 99957f284bae1b382811ece47f4699bce725ee4a | 3932 |
| Route output after endpoint guard | 60e3ff89b45fe826934c3fe1eaf1d23fe38b4276 | 4118 |
| require-anchor-endpoints.patch | e8de74b9193c1831838f4a49c6a764c31fde0ccd | 734 |

The actual serialized patch contains one hunk and eleven rows, with five additions and no deletions. Forward text application exactly reconstructs the new output; inverse text application restores the retained input. Removing the inserted guard restores every other byte. These checks operate on the new serialized source artifact, without executing the API, either library, fixtures, compiler, tests, browser or workflow.

Apply the original patch to its exact canonical preimage and then this incremental patch to the stated intermediate identity. That is a consumer application instruction; the previous accepted application was not repeated here.

### Scope and publication

A narrow Commons search for the exact source identifiers returned no rows; the same Slack search returned no rows and native END. A broader Slack query returned twenty bounded prefixes and a next cursor, with no END. Its own completed packets, unrelated pagination scopes, terminal work and held topics were left unexpanded. No global absence or ownership inference follows from these bounded observations.

This continuation modifies only this README and adds the incremental patch. The original patch and all three MIT notices remain unchanged. Existing source attribution is retained. The new guard is an attributed Commons source proposal; it is not an upstream change, deployment, observed incident repair, reward claim or successful rendering report.

Ordinary publication checks require both complete immutable artifact bodies, native and independent identities, and exact final PR/path/parent/tree metadata. An equal observed main may use the preplanned immutable-read alias; otherwise both artifacts are read once at the observed main commit. The actual outcome belongs in the release and grouped index.
