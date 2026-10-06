# Native localized corridor links in the liquidity heatmap

## Change and actual caller

The acquired Analytics route dynamically imports LiquidityHeatmap and renders it with metrics.top_corridors. In that mounted component, the populated matrix cells navigate through an onClick handler on a motion.div. There is no native destination or keyboard activation binding. The displayed compact amount also does not identify the destination corridor.

The patch makes the populated inner cell an existing locale-aware Link. Its href uses the same encoded corridor key. Its accessible name includes the source asset, destination asset and visible formatted liquidity. Empty cells remain unchanged and noninteractive. The unused useRouter binding, imperative helper and outer click handler are removed.

This uses link semantics for navigation, including keyboard Enter and browser link actions. No button or custom key handler is introduced. The link explicitly sets prefetch={false}, so this change does not opt into viewport or hover route prefetch under the documented App Router contract.

## Pinned complete source

Every donor input refers to [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/components/charts/LiquidityHeatmap.tsx | cc15d61c3cf1415a78ae191b2377a12a6f1c9d01 | 15264 |
| src/app/[locale]/analytics/page.tsx | 210bb00fd103fa1ca9a02ae7dedb14f4182aa9bf | 8438 |
| src/i18n/navigation.ts | fd8ba9aa80bb0d0dd56eb76a3891caa0afe0c803 | 182 |
| src/i18n/routing.ts | 7a1c19fa17133fa33179f3381d115f8d2ee542f7 | 175 |
| package.json | 2b1c6ac1f83096666c7fd6d5ba3fd22780e6b8eb | 3119 |

The complete navigation module exports Link and useRouter from the same createNavigation(routing) call. The complete routing configuration declares en/es/zh, default en and always-prefixed locales, with no pathnames map. The patch therefore keeps a final string destination and the existing locale-aware API family. The manifest declares Next16.2.10 and next-intl^4.13.2; no installed dependency implementation was executed.

The full route is supporting caller evidence, not a copied artifact. Commons31964 separately fixes its refresh error state; this heatmap patch is independent and does not edit or replay that correction.

Current-path history returned christabel888's relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`. A relocation record is not sole-authorship evidence; original notices and source ownership are preserved.

## Primary contracts

The [W3C APG Link Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/link/) recommends native href-bearing links for navigation and describes Enter activation. A clickable generic container does not acquire native link behavior merely from its click listener.

The [next-intl navigation reference](https://next-intl.dev/docs/routing/navigation) documents its shared locale-aware wrappers, Link's use of next/link and final string hrefs when no pathnames map is configured. The acquired configuration matches that case.

The [Next.js App Router Link reference](https://nextjs.org/docs/app/api-reference/components/link) describes the underlying anchor and forwarding of anchor attributes. Its prefetch=false contract disables viewport and hover prefetch. This is why the patch includes that explicit prop instead of inheriting a new prefetch default.

These are source and documented-contract deductions, not an observed browser, assistive-technology or network result for the installed application.

## Serialized source result

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Heatmap preimage | cc15d61c3cf1415a78ae191b2377a12a6f1c9d01 | 15264 |
| Heatmap postimage | 73ec135a3b93203a671a7a3d138becebfc45c975 | 15226 |
| corridor-links.patch | 4e914fddf6dbfbd259f34f5681c4bef226a8293f | 2699 |

The actual serialized patch contains five hunks and 48 rows, adds six lines and removes twelve. Forward application exactly produces the complete postimage; inverse application exactly recovers the complete preimage. Native and independent identities match the complete acquired source and two navigation modules. The same corridor-key encoding expression now supplies href.

The matrix calculations, currency text, inner cell classes, outer animation, mouse hover bindings and complete tooltip handler remain unchanged. The empty-cell branch is byte-identical. The linked pointer target is the colored inner cell: the outer wrapper padding no longer routes, while its hover region remains. Native context-menu and modified-click behaviors are intentionally available. The accessible label follows the existing English UI.

A preliminary unpublished Link draft lacked explicit prefetch=false and is retained separately. A later ordinary identity assertion caught an authored guide's mistaken navigation-module byte count before artifacts or publication; the correct count is 182. No source was fabricated, provider call replayed or application executed to resolve that local error.

## Limits and attribution

No package install, typecheck, compiler, browser, focus rendering, application navigation, route request, fixture, tests or workflow was run. This is not whole-build or WCAG-conformance evidence. Hover-only tooltip details, grid arrow keys, visible focus styling across application CSS, asset-code aggregation, route existence, period filtering and translations remain outside the correction.

The following acquired upstream MIT notices are carried byte-for-byte:

| Notice | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| upstream-licence-mclaughlin.md | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| upstream-license-menke-laguna.md | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| upstream-license-de-wet.md | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |

This attributed Commons proposal is not an upstream change, deployment, acceptance or reward. Bounded exact-name Commons and Slack queries returned zero rows; Slack reported native END. Internal coordination reported no retained same-hunk overlap. These results do not prove global absence of other work.

Publication requires complete immutable file bodies and native/independent identities for all five artifacts, plus final PR/files/merge/main metadata. Named-main equality may reuse the verified immutable merge bodies only when the observed main SHA equals that merge; otherwise every file is read once at the observed main pin. Actual evidence is recorded in the release and completion index.
