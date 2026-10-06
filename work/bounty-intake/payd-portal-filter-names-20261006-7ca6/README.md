# Explicit names for the Employee Portal filters

This source-only continuation adds explicit accessible names to the existing transaction search, status filter, and type filter in the mounted Employee Portal. The search retains its exact visible placeholder wording. The two selects receive names describing the dimension they filter. This packet contains a minimal patch and the unchanged upstream Apache-2.0 licence; it does not operate an account, fetch employee records, or deploy the application.

## Exact production source and caller

| Item | Immutable identity |
| --- | --- |
| Canonical repository | Protocol-Guild/PayD |
| Donor commit | 171c74b454daba241bfb75f36d10a0a3a77a68e5 |
| Source path | frontend/src/pages/EmployeePortal.tsx |
| Preimage blob / UTF-8 bytes | abd4b9974970dbf29f76188fec94a21de9f02438 / 29,426 |
| Proposed postimage blob / UTF-8 bytes | 132d1a2abbfb44d4a4205f43073837c29796c1e1 / 29,565 |
| Source mode | 100644 |
| App caller | frontend/src/App.tsx, acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c, 6,460 bytes |
| Entry source | frontend/src/main.tsx, f84f187971ba135010c48e69fda10f0c0f71ebd9, 1,664 bytes |
| Root licence | LICENSE, 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64, 11,357 bytes |

The complete retained canonical tree has 753 entries and reports no truncation. It binds these source and caller paths to the donor commit. The full App source imports EmployeePortal and renders it under the existing ErrorBoundary at /portal. The entry source imports and renders App; its complete bytes were already retained from a separately pinned donor acquisition and are reused only because the canonical tree identifies the exact same blob. No current-main entry-file read is claimed. The fresh canonical main ref still equalled the donor during preparation.

The full current portal source was acquired by immutable ref and its native blob was independently recomputed. Only source definitions were inspected. Neither the component nor its hooks, data requests, filters, withdrawal flow, or account controls were invoked.

## Three inserted attributes

| Existing control | Added aria-label |
| --- | --- |
| Transaction search input | Search tx hash, memo… |
| Status select | Filter by status |
| Type select | Filter by type |

The acquired JSX has no associated label, aria-label, or aria-labelledby for these three controls. The search has a placeholder; this note does not claim that every browser or assistive technology previously exposed no name, because placeholder fallback behavior is a separate platform concern. The patch supplies an explicit source-level name. Select option text describes the available choice and remains unchanged.

The selected controls have no separate visible captions to reference. The search name uses the existing placeholder exactly, including its ellipsis. MDN's aria-label reference describes the attribute as a way to name eligible interactive elements when an appropriate associated visible label is unavailable, while preferring a visible label association when one exists. This is a narrow application of that naming contract, not a screen-reader result or a broader accessibility verdict.

Primary reference acquired during preparation:
https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label

Only the three attribute lines are inserted. Values, ChangeEvent annotations, state setters, option strings, placeholder, CSS classes, filtering and pagination calculations, TypeBadge, data-loading behavior, and every other source byte remain unchanged. The separate Local Currency control is outside this patch. No translation resource or user-visible layout is changed; the new names follow this page's existing English copy. Complete localization remains outside scope.

## Attribution and existing contributor work

Credit belongs to the original Protocol-Guild/PayD contributors for the complete surrounding portal implementation. A bounded one-row path-history request at the donor returned commit 4f5dd01b31a0b7445e50408398b6fbe9b52d8f48, dated 2026-09-27, with author name “Mainnet-ops” and subject “feat(ui): adopt workpay-inspired design language”. That records the latest returned path-history row, not a complete original-authorship census.

The warm lead was existing upstream PR568 by waterWang, head 41cc9da36a7aaea867ef02802ef76673a2b068c9 on fix/544-typebadge-icons in waterWang/PayD. Its current metadata reports OPEN/unmerged, two changed paths, zero issue comments and zero review comments. The full two head files show that its TypeBadge already places Lucide icon children and type text in an inline-flex badge with centered alignment and a gap. That badge scope was recorded NO PATCH. Its whole PR body was held before expansion by the intake content screen; this packet does not rely on that body or infer ownership absence.

This continuation instead uses the separately acquired canonical current portal source for a distinct filter-name residual. It neither rewrites that contributor branch nor claims to complete issue544, issue475, the Employee Portal feature, or any other whole issue. No upstream approval, assignment, acceptance, merge, or reward is claimed. Prior held routes, protected source scopes, and completed packets remain untouched.

The supplied LICENSE is the complete retained Apache-2.0 file with exact donor blob identity and line endings. Source attribution is preserved by the minimal patch; no whole-repository licence inference beyond this actual file is required.

## Patch and verification boundary

filter-names.patch is a real unified patch for the exact preimage above: +3/-0 in three complete hunks and 21 context/change rows. Its serialized form was independently parsed and applied forward to the complete preimage and backward to the complete proposed postimage. Both resulting full strings matched exactly. Removing only the three added attribute lines recovers the original string. Complete source and artifact Git blob identities were independently computed from their UTF-8 bytes.

Those checks validate source construction and byte custody. No compiler, installed dependency, browser, DOM, keyboard, accessibility tree, screen reader, network, data, application runtime, or tests were executed. The work makes no claim about every assistive technology, live announcements, wider page accessibility, filtering correctness, financial behavior, backend authorization, or deployment.

The Commons publication contains only this guide, filter-names.patch, and the exact licence. Full immutable content comparisons and a separate final main observation are performed during publication; their outcome belongs to the completion receipt rather than a prediction in this guide. Upstream application files are not modified.
