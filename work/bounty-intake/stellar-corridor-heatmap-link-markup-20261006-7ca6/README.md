# Use supported Link markup for corridor heatmap cells

## Actual mounted incompatibility

The corridor listing dynamically imports the named CorridorHeatmap export and renders it with filteredCorridors when the heatmap view is selected. Each populated matrix cell renders the project's localized Link with passHref, legacyBehavior and a nested anchor element.

The acquired package declares Next.js 16.2.10. Next.js documentation explicitly says version 16 no longer supports the passHref and legacyBehavior props. The current Link renders the anchor itself, making the nested anchor form inappropriate for that interface. The source therefore retains a legacy link composition on an actually mounted route.

This is a source and documented-interface diagnosis. No component render, browser error, TypeScript error or build failure was executed or observed.

## Complete source custody

Donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete source | Native and independent Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/components/charts/CorridorHeatmap.tsx | 1deb0357b1758f0357ede4dc15dfb7f7f76f4850 | 20640 |
| src/app/[locale]/corridors/page.tsx, canonical caller | a14fe86977c4071ad958ddc3f206b4f07134b072 | 17815 |
| src/i18n/navigation.ts | fd8ba9aa80bb0d0dd56eb76a3891caa0afe0c803 | 182 |
| src/i18n/routing.ts | 7a1c19fa17133fa33179f3381d115f8d2ee542f7 | 175 |
| package.json | 2b1c6ac1f83096666c7fd6d5ba3fd22780e6b8eb | 3119 |

The complete component was acquired for this new task; the caller, navigation wrapper, routing and package reuse retained complete source custody. The package also declares next-intl ^4.13.2. The local navigation module exports Link from createNavigation(routing); its routing configuration lists en, es and zh with localePrefix always and no pathnames map.

The bounded current-path history returns relocation commit 59fad72d9fbef9cfd6f47e215392da44488fcdc4 attributed to christabel888. This is not a complete authorship history or sole-author assertion. Original attribution and the three acquired MIT notices are preserved.

## Primary interface evidence

The [Next.js passHref notice](https://nextjs.org/docs/messages/link-passhref) states the removal of passHref and legacyBehavior starting in version 16. Its lower legacy example is not the applicable guidance for the declared version here.

The [Next.js invalid-child explanation](https://nextjs.org/docs/messages/invalid-new-link-with-extra-anchor) describes removing the extra anchor and moving its attributes onto Link. The [current Link reference](https://nextjs.org/docs/app/api-reference/components/link) confirms that anchor attributes such as className belong directly on Link.

The [next-intl navigation reference](https://next-intl.dev/docs/routing/navigation) identifies its Link as a wrapper around next/link that applies locale handling. The existing project wrapper is retained, so the patch follows the same localization path.

The retrieved documentation surface identifies Next.js 16.3.8; the version-16 removal notice applies to the project's declared 16.2.10. These documentation statements do not establish a particular installed runtime, successful build or browser result.

## Narrow markup correction

The patch removes passHref and legacyBehavior and removes the child anchor's opening and closing tags. It moves the existing className expression onto the same localized Link and retains the same metric span as its child.

The href expression remains exactly `/corridors/${cell.corridorData.id}`. The existing class string, color and opacity function calls, metric display call, span class and all content are preserved, with only the former anchor body dedented by two spaces. No new route encoding, navigation handler, locale override, target, prefetch or scroll setting is introduced.

The surrounding cell wrapper and its mouse/touch handlers remain exact. Matrix construction, metric selectors, responsive sizes, colors, tooltip state, timers, formatting and empty-cell markup remain unchanged. Existing tooltip accessibility, mobile touch behavior, route-ID normalization and complete heatmap accessibility are not resolved or claimed by this correction.

The separate listing source proposals #32036 and #32037 affect later heading/control JSX in the caller. They are not reapplied or reverified here. The listing request-lifecycle proposal also concerns the caller, not this component.

## Serialized source checks

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Complete preimage | 1deb0357b1758f0357ede4dc15dfb7f7f76f4850 | 20640 |
| Complete prepared postimage | f532cc2e9149d0569faf014cad188c2f31a0bd69 | 20450 |
| supported-link-markup.patch | a872a04111354d1eaca30403bb31f4b6c4f59d47 | 2139 |

The actual unified patch contains 1 hunk and 28 rows, with 8 additions and 13 deletions. Complete serialized forward application reconstructs the postimage and inverse application restores the preimage. Restoring the selected link block restores every other component byte. The href line is exact, and the former anchor body matches after its two-space dedent.

Apply supported-link-markup.patch at the donor repository root to the exact component preimage. No Link, React component, navigation, locale cookie, tooltip, timer, browser, compiler, lint command, fixture, test, build, workflow or upstream action was executed. No package or lockfile is changed.

## Overlap, notices and publication

Bounded exact-component/legacyBehavior queries returned zero Commons rows and zero Slack rows with native Slack END. Internal custody retained no exact same-component legacy-link completion or hold. This is bounded overlap evidence, not global absence, ownership or upstream acceptance clearance. Unrelated search results from one documentation query were retained but not adopted as evidence.

| Unchanged notice | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| upstream-licence-mclaughlin.md | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| upstream-license-menke-laguna.md | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| upstream-license-de-wet.md | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |

This is an attributed Commons source proposal. Publication requires all five complete immutable artifact bodies with native plus independent identities, followed by exact PR/files/head/merge/parents/tree/main metadata. A fresh main commit exactly equal to the verified merge may reuse those bodies under an explicit alias receipt. Otherwise each artifact is read once at the observed immutable main pin. Actual publication identities belong in the separate release and grouped index.

## Continuation: metric-control names and active state

The preceding sections document #32043. This continuation consumes its retained complete component postimage and preserves the supported localized Link markup.

The mounted heatmap has four native buttons that set activeMetric to health, success_rate, volume or latency. The same state controls both metric rendering and the selected button's styling. Each button's text is inside a span with hidden sm:inline; there is no explicit button name independent of that responsive visibility, and no programmatic pressed-state attribute.

The new patch adds a stable aria-label matching each existing text label and an aria-pressed boolean using the same comparison already used for selected styling:

| Existing metric state | Explicit name | Pressed state |
| --- | --- | --- |
| health | Health | activeMetric equals health |
| success_rate | Success | activeMetric equals success_rate |
| volume | Volume | activeMetric equals volume |
| latency | Latency | activeMetric equals latency |

The existing initial state selects health. Each existing handler sets one member of the same four-value union, so the corresponding button exposes true while the others expose false under that source state model. Labels remain stable when selection changes. Re-selecting the current metric retains the existing state; the patch does not add a no-selection mode.

The [W3C APG button pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/) supports explicit button names through aria-label and communicates a button's pressed state through aria-pressed with stable labels. This supports the added semantics. It does not establish full accessibility conformance or a tested assistive-technology announcement.

Only eight attributes are added. Native button roles, handlers, keyboard behavior, focus, visual labels, icons, class expressions, state initialization, metric calculations and every other source byte remain exact. No tab/radio roles, arrow-key navigation, live region, new callback or changed selection policy is introduced. The surrounding chart and tooltip accessibility are unchanged.

| Metric-control continuation item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Source after #32043, before attributes | f532cc2e9149d0569faf014cad188c2f31a0bd69 | 20450 |
| Source after metric attributes | ebdadd15b4f027e2cddc256447f3934f117fe8e8 | 20799 |
| name-and-expose-metric-controls.patch | 82122104bd29409b2cbb34a9333e04ea1e3fa5c1 | 2258 |

The serialized incremental patch contains 4 hunks and 32 rows, with 8 additions and no deletions. Complete forward and inverse reconstruction matched the source identities. Removing the eight attributes restores every prior byte, including the corrected cell links.

Apply supported-link-markup.patch first, then name-and-expose-metric-controls.patch. No button event, metric computation, component, browser, assistive technology, compiler, fixture, tests or workflow was executed. Responsive visual behavior and spoken output were not observed.

Separate bounded component/aria-pressed and component/aria-label overlap queries returned zero Commons rows and zero Slack rows with native END. These queries do not establish global absence or upstream acceptance.

This continuation writes only the new patch and an exact-preimage-guarded guide update. The existing Link patch and three MIT notices stay unchanged, with accepted checks inherited without replay. Both complete newly written immutable bodies require native and independent identity matches, followed by exact final PR/files/head/merge/parents/tree/main metadata. An explicit main alias requires fresh exact commit equality; otherwise both changed artifacts are read once at the observed immutable main pin.
