# ThemeToggle reference: source qualification

This two-file documentation continuation adds THEME_TOGGLE.md and this qualification note to the existing PayD180 component-reference packet. The earlier ARROW_LINK.md, README.md and LICENSE remain unchanged. No production source, dependency, CSS, storage value, route, theme setting or upstream repository is changed.

## Scope and intended destination

The warm issue [Protocol-Guild/PayD #180](https://github.com/Protocol-Guild/PayD/issues/180) asks for reusable component documentation. The earlier #32001 packet documents ArrowLink only; this is a distinct component entry, not a repeat of that reference. A potential upstream destination would be docs/components/ThemeToggle.md. That exact path is absent from the complete retained 753-entry canonical tree inventory. This does not establish that no external documentation or contributor draft exists.

The reference documents current ThemeToggle props/exports, the two-state context mapping, the fixed payd-theme key, initial/default/effect behavior, actual mounting, styling connection and explicit unsupported behavior. It does not claim a source fix, new feature, design-system completion or whole issue acceptance.

## Source custody and mounting

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`.

Five full files were newly acquired at that exact ref: ThemeToggle.tsx, useTheme.ts, ThemeProvider.tsx, DashboardTopBar.tsx and EmployerLayout.tsx. Each complete returned native blob matches an independently computed Git blob identity over the full text. Their complete path/hash/byte table is in the reference.

Main, App and index.css are full retained source reused for this genuinely new documentation task. Each matches its canonical tree entry. They were not described as new provider acquisitions. App's actual route wrapper is EmployerLayout; its DashboardTopBar is the qualified ThemeToggle caller.

A separately retained AppLayout body belongs to waterWang's older cf853ac3 carrier and has blob 452565460f1bdad2df2162d8191e37e32320d823, which differs from the canonical AppLayout tree entry f2fb2a09415e55a7a53bccba1d54a027681fb9cf. It was not substituted for the current caller and was not used as mounting evidence. No accepted sidebar correction was reconstructed or replayed while reading EmployerLayout for this independent caller relationship.

The bounded canonical code search for ThemeToggle returned the component, AppLayout, DashboardTopBar and a generated tsbuildinfo path with incomplete_results false. The generated file was not expanded or treated as build evidence. That search is not a universal consumer census.

## Related contributor work and holds

Earlier retained issue180 metadata and comments were used only as a dated task lead. The prior bounded PR180 query returned no entries; that old observation is not a fresh exhaustive ownership check. The contributor requests were not interpreted as assignments or permission.

A distinct current PR [Protocol-Guild/PayD #643](https://github.com/Protocol-Guild/PayD/pull/643), for issue285, is OPEN/unmerged by SrvFernandes, head `62238188669482cfd6c742984b0cbb74ff3c065d` in SrvFernandes/PayD. Its complete four-path metadata adds root src/App.jsx, src/components/ThemeToggle.jsx, src/context/ThemeContext.jsx and src/index.css. The current production entry imported by main remains frontend/src/App.tsx. Integration of those root additions was not established. No carrier body or source was used for this reference, and no alternative entry point was invented. Its whole PR body remains held after screening; the author and branch remain untouched.

This reference describes the existing canonical frontend/src implementation. It neither claims that #643 is accepted, rejects its intended design, nor upgrades its readiness. Other exact held routes and protected source families remain unchanged.

## Attribution and license

Protocol-Guild/PayD's original contributors retain credit; no original-author census is asserted. The minimal illustrative usage snippet is newly authored and unexecuted.

The existing [LICENSE at the original #32001 immutable merge](https://github.com/woahwhattheheck/commons/blob/f4b583c3d4f7940ab5912470ffb8bfeca540bc47/work/bounty-intake/payd180-arrow-link-reference-20261006-7ca6/LICENSE) preserves the full retained Apache-2.0 notice, Git blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`, 11,357 UTF-8 bytes. This continuation adds no duplicate license file and does not change the existing notice. The immutable link identifies the acknowledged original artifact, not a new assertion about moving main.

## Primary explanations and verification limits

The newly acquired React use page supplies only the context-reading explanation used in the reference. Its current v19.3 heading is kept separate from the unexecuted repository's dependency state. The previously acquired current MDN button page supplies the native-control/form explanation; no examples or tests from that page were executed.

Validation is source reading, full-content/native/independent identity comparison, static caller inspection and exact publication readback. It does not include running React, accessing localStorage, changing data-theme, browser rendering, focus, theme toggling, server rendering, package installation, compilation, tests, fixtures, account or upstream actions. No persistence-success, cross-tab, system-theme, contrast, full accessibility, no-flash, hydration or build guarantee is made.

Publication is limited to these two new documentation artifacts. Complete immutable artifacts, their native and independent identities, PR/path/tree/parent metadata and a separate fresh main observation are checked. The preselected equality alias is allowed only if that observation equals the verified merge/readback ref; otherwise both files must be read completely at one observed immutable main commit. Publication metadata is not runtime evidence or contributor acceptance.
