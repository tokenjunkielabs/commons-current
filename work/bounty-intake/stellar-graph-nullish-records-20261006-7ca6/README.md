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
