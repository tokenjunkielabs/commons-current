# PR51 fallback merge: preserve the closing-edge boundary

When the new fallback merger joins two polygons along the first polygon's closing edge, its prefix and suffix loops both append the entire first polygon. The attached patch skips that suffix only when the next index is zero. This corrects the repeated boundary while preserving the existing non-wrapping branch and all other source bytes.

This is an attributed source correction for [Henry00IS/ShapeEditor PR51](https://github.com/Henry00IS/ShapeEditor/pull/51), authored by RaphaeLogico. It is supplied as a Commons review packet, not applied to the upstream repository or contributor branch. PR51 remains the contributor's implementation and review responsibility. No assignment, bounty eligibility, payment, full-PR approval, editor success, or resolution of issue17 is claimed.

## Exact source and qualification

- Issue: https://github.com/Henry00IS/ShapeEditor/issues/17
- PR: https://github.com/Henry00IS/ShapeEditor/pull/51
- Contributor repository: `RaphaeLogico/ShapeEditor`, branch `fix/self-intersection`.
- Qualified head: `33cef0c19b92c6287ebb4d53c6c6f63fdb804b1b`.
- Qualified base: `695aa8931981610a77f068a7d68a1c05e91654d5` on `Henry00IS/ShapeEditor:master`.
- Native status at qualification on 2026-10-06: issue OPEN with no native assignee; PR OPEN, non-draft, unmerged, three changed files, four issue comments, zero inline review comments.
- Complete changed-file map: Project.cs (+393/-5), BayazitDecomposer.cs (+2/-2), ExternalRealtimeCSG.cs (+33/-3), at their full paths below.
- The complete 625-entry head tree returned `truncated:false`. No AGENTS.md, CONTRIBUTING, code-of-conduct or pull-request-template path was present in that tree. README and relevant license notices were read.
- Root license is MIT, copyright 2022 Henry de Jongh. Acquired dependency notices identify MIT terms for Ian Qvist's Velcro Physics and Sander van Rossen's RealtimeCSG source. See THIRD_PARTY_NOTICES.md; this is source attribution, not a repository-wide legal opinion.
- The issue's historical offer mentions USD50 or EUR50 and PayPal after verification. That historical wording is not a current payment or eligibility assurance. Its upstream submission-format request is recorded as contribution context; this packet makes no upstream submission or bounty claim. Unrelated third-party directives in issue comments were not treated as maintainer instructions.

The older small-area cutoff review was explicitly closed at this same head in [comment5944094908](https://github.com/Henry00IS/ShapeEditor/pull/51#issuecomment-5944094908). Its example and arithmetic have not been rerun here. The author's reported Unity checks are attributed reports, not this review's validation.

## Actual call chain

Project.GenerateConvexPolygons calls SegmentListToConvexPolygonMesh; the latter sends eligible contours through SafeDecomposeWithFallback. SafeDecomposeWithFallback catches an ordinary exception from Bayazit and calls DecomposeHertelMehlhorn. The PR's Bayazit change throws after its existing depth budget is exhausted.

DecomposeHertelMehlhorn calls DelaunayDecomposer.ConvexPartition and then tries pairwise merges using TryMergeConvex. The complete Delaunay wrapper creates Polygon lists from triangle point order; it does not rotate each triangle to avoid a closing shared edge. This review does not establish which order DTSweep produces for any particular project.

The relevant immutable source locations are:
- [Project.cs lines663–718: fallback and consumer](https://github.com/RaphaeLogico/ShapeEditor/blob/33cef0c19b92c6287ebb4d53c6c6f63fdb804b1b/Scripts/ShapeEditor/Project.cs#L663)
- [Project.cs lines723–790: complete merge helper and turn guard](https://github.com/RaphaeLogico/ShapeEditor/blob/33cef0c19b92c6287ebb4d53c6c6f63fdb804b1b/Scripts/ShapeEditor/Project.cs#L723)
- [DelaunayDecomposer.cs](https://github.com/RaphaeLogico/ShapeEditor/blob/33cef0c19b92c6287ebb4d53c6c6f63fdb804b1b/Scripts/ShapeEditor/Decomposition/Delaunay/DelaunayDecomposer.cs)
- [Polygon.cs](https://github.com/RaphaeLogico/ShapeEditor/blob/33cef0c19b92c6287ebb4d53c6c6f63fdb804b1b/Scripts/ShapeEditor/Decomposition/Polygon.cs)
- [Polygon.2D.cs](https://github.com/RaphaeLogico/ShapeEditor/blob/33cef0c19b92c6287ebb4d53c6c6f63fdb804b1b/Scripts/ShapeEditor/Decomposition/Polygon.2D.cs)

## Source-level counterexample

Consider two counterclockwise triangles using the labelled points A=(0,0), B=(1,0), C=(1,1), D=(0,1): p1=[A,B,C] and p2=[A,C,D]. They share the opposite directed edges C→A and A→C. In the helper these match at i=2, nextI=0, j=0, nextJ=1.

The original concatenation has these parts:

| Existing append loop | Appended vertices |
|---|---|
| p1 indices zero through i | A, B, C |
| p2 non-shared chain after nextJ until j | D |
| p1 indices nextI through its end | A, B, C |

It therefore returns the candidate [A,B,C,D,A,B,C], rather than the boundary [A,B,C,D]. Each local turn in that repeated contour has a positive cross product, so IsStrictlyConvex2D's rejection condition does not catch the repeated traversal. Polygon derives from List<Vertex>; Add does not coalesce repeated vertices. The saved GetSignedArea2D shoelace formula yields nonzero area for this contour, so the later cleanup condition (fewer than three vertices or exactly zero area) does not reject it either. Geometrically the repeated contour traverses the square boundary and an additional triangle.

This is a hand-derived trace of the supplied helper inputs and its loops. No C#, Unity, float32 simulation, triangulation, tests, example ZIP, or synthetic program was executed. In particular, this note does not claim that Bayazit enters fallback for a simple square, or that a particular real project causes DTSweep to emit these two triangle lists. The established defect is the helper's behavior on valid adjacent polygon inputs under a closing-edge ordering.

## Correction and exact scope

The patch adds only the condition `if (nextI != 0)` before the existing p1 suffix append. Since nextI=(i+1)%p1Count:

- For a non-closing edge, nextI is nonzero, so the original prefix, p2 chain and remaining p1 suffix are unchanged.
- For the closing edge, i is the last index, so the prefix already contains every p1 vertex. Omitting the suffix prevents that entire list from being appended again.

For the illustrated closing-edge ordering, the corrected concatenation is [A,B,C,D]. The correction does not change matching tolerances, vertex-to-edge splitting, area tolerance, the turn predicate, Bayazit's budget, triangle production, hole handling, winding policy, material propagation, exception handling, or the separate RealtimeCSG plane filter. It does not certify those other algorithms.

Patch application target:
`Scripts/ShapeEditor/Project.cs` at the exact contributor head above.

| Identity | Git blob | UTF-8 bytes |
|---|---|---:|
| Original file | `131f1ee2fbeb3144a7e5c7392437281db8466f9d` | 38,200 |
| Proposed file | `ef9a130a4db0b5286efd0f53f8be3bf9a8ed13af` | 38,244 |

The serialized unified diff contains one hunk, +2/-1. Its forward text application and inverse text application were checked exactly once against the retained full strings; all other bytes match. This is text verification, not compilation or a test run. The patch is intentionally bound to the contributor preimage and must not be assumed to apply to a different revision.

A future runtime regression owned by the implementing contributor should cover a closing shared edge and cyclic reindexing of the same inputs, plus the existing real editor reproductions. No such regression was authored or run in this packet.

## Full acquired source identities

All ten complete source/document strings matched both their native/tree identities and an independently computed Git blob identity. Complete acquisition does not imply a full audit of every unrelated method or dependency. Review focused on the qualified merge path; no broader source hunt or upstream service interaction was performed.

Each path is under https://github.com/RaphaeLogico/ShapeEditor/blob/33cef0c19b92c6287ebb4d53c6c6f63fdb804b1b/ .

| Path | Git blob | UTF-8 bytes |
|---|---|---:|
| `LICENSE.md` | `3e9c4e74968b0d1729a6d002d5c0c39b5f11f673` | 1071 |
| `README.md` | `eb62769147fe80956d5d25aa1a789e9fd5badd84` | 2943 |
| `Scripts/ShapeEditor/Project.cs` | `131f1ee2fbeb3144a7e5c7392437281db8466f9d` | 38200 |
| `Scripts/ShapeEditor/Decomposition/Bayazit/BayazitDecomposer.cs` | `e19123123709277f1fd1382da98e53fbd75abac5` | 15844 |
| `Scripts/Utilities/ExternalRealtimeCSG.cs` | `a78145e233a46681723c09bed4093fc5bff1b017` | 15326 |
| `Scripts/ShapeEditor/Decomposition/Delaunay/DelaunayDecomposer.cs` | `53643fb4bf880f92875b546108ea03b2db100f2b` | 2441 |
| `Scripts/ShapeEditor/Decomposition/Polygon.2D.cs` | `2fde7cf3a362d311f7d2e4eb79c6d69c31d0c877` | 8379 |
| `Scripts/ShapeEditor/Decomposition/Polygon.cs` | `e8082be06c873e2c01437c0644aebea0b9d98756` | 5802 |
| `Licenses/VelcroPhysics.txt` | `e70b297c1fca45d59873ee449113dfd6335d1049` | 1065 |
| `Licenses/RealtimeCSG.txt` | `389af0d1b5e17fcfb5f842ccf6a1eea2f1a32596` | 1074 |

## Packet contents and limits

- closing-edge.patch: the one guarded suffix append.
- REVIEW.md: this original source analysis and application contract.
- THIRD_PARTY_NOTICES.md: contributor attribution and the exact acquired notices.

No whole-issue implementation, accepted cutoff replay, Unity/compiler/test result, deployed artifact, upstream comment/PR edit, contact, account action or payment operation accompanies this packet.
