# Error components: source qualification

This documentation-only continuation adds ERROR_BOUNDARY.md and this qualification note beside the existing PayD180 ArrowLink and ThemeToggle references. It changes no production component, root wiring, reporting call, translation resource, route, dependency or configuration.

## Task and bounded overlap evidence

The retained warm [Protocol-Guild/PayD issue180](https://github.com/Protocol-Guild/PayD/issues/180) asks for reusable component documentation. The prior ArrowLink #32001 and ThemeToggle #32033 packets are protected, distinct entries. This entry covers the current ErrorBoundary/ErrorFallback surfaces and their actual root relationship.

A possible upstream documentation destination is docs/components/ErrorBoundary.md. The complete retained canonical tree has 753 entries, truncated:false, and no docs/components/ entries. That observation establishes only this pinned tree's contents; it does not establish absence of external drafts or documentation.

A new bounded Commons PR query for "PayD" "ErrorBoundary" "documentation", all states and topn 10, returned no entries. This is an exact query result, not an exhaustive ownership or completion certificate. Root retains no exact same documentation hunk. Neither observation authorizes an upstream change or supersedes contributors.

The held issue185/PR669 carrier body remains unexpanded. No assertion about that carrier's source, readiness, reset implementation or acceptance is made. This packet deliberately documents canonical public components; it does not attempt to reconstruct, duplicate or correct a held proposal. Other failed exact routes and protected families remain unchanged.

## Canonical source and mounting

Donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`. A new named-main guard returned that same commit before freezing this packet.

Two full component files were acquired at that immutable ref: frontend/src/components/ErrorBoundary.tsx and frontend/src/components/ErrorFallback.tsx. Each complete text matches its native returned SHA, independently computed Git blob identity and exact entry in the retained canonical tree. Both use mode 100644.

The complete 1,664-byte main entry is reused from retained custody. Its original acquisition URL identifies waterWang's older cf853ac31818de9400bf558d0e74ef44ff2a3744 carrier; the full body and independent identity f84f187971ba135010c48e69fda10f0c0f71ebd9 also match the canonical frontend/src/main.tsx tree entry. It is therefore reused as matching bytes, not presented as a new canonical provider acquisition. No older unmatched AppLayout body is used.

That entry imports both components, imports i18n initialization, wraps App in the boundary and places BrowserRouter and the other named providers outside it. It also supplies the empty reset callback. The reference's wiring statements come from that full source. No route was traversed or error deliberately raised.

The component's reporting call and the root's conditional reporting initialization are public source declarations. No environment value, credential, error event, log, session or service account was acquired or accessed. The documentation does not claim reporting is configured or delivered.

## Documentation decisions

The state machine is described exactly: initial children, then supplied fallback, with no reset back to children implemented in the class. ErrorFallback's optional callback is not promoted to a boundary reset API. The root's no-op callback is described explicitly without providing an unqualified recovery patch.

Prop tables preserve required ReactNode inputs, optional strings/callback, nullish default selection and the absence of arbitrary prop forwarding. Translation keys are listed without inventing their resource values. The always-present Home Link and optional button are distinguished by the source, not by an interactive test.

No new provider, error class, reset token, retry action, remount policy or logging scheme is proposed. The small illustrative usage snippet was newly authored and not compiled or executed. It does not import example application data or force an error.

## Primary explanation and evidence limits

The newly acquired [React Component documentation](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary) supplies the general boundary and excluded-error explanation. Its actual returned catching-errors section includes the transition-function exception, so the reference does not claim that every asynchronous error is excluded. The page's current v19.3 heading is kept separate from the unexecuted repository's dependency state.

The specific props, state, fallback, empty root callback and reporting call are derived from the acquired PayD files, not attributed to generic React examples. No framework example or repository code was executed, and no React test, browser, runtime, build, package install or application effect was invoked.

Validation consists of full-source identities, static caller and state inspection, documentation review and subsequent exact publication readback. It does not certify whole-application crash coverage, recovery, telemetry, navigation success, accessibility, SSR, hydration or compatibility.

## Attribution and license

Original Protocol-Guild/PayD contributors retain credit; this note does not claim a complete author census. The new prose and illustrative snippet supplement their implementation.

The existing [LICENSE at the original #32001 immutable merge](https://github.com/woahwhattheheck/commons/blob/f4b583c3d4f7940ab5912470ffb8bfeca540bc47/work/bounty-intake/payd180-arrow-link-reference-20261006-7ca6/LICENSE) preserves the full retained Apache-2.0 notice, blob 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64, 11,357 UTF-8 bytes. This packet reuses that acknowledged notice without another license file or a moving-main identity claim.

The earlier ARROW_LINK.md, THEME_TOGGLE.md, their source notes, original README.md and LICENSE remain unchanged. Only these two new documentation paths are published.

## Publication verification plan

The guarded Commons publisher will add the two prepared UTF-8 files, retain their exact expected new Git blob identities and read both complete artifacts at the immutable merge. PR, path, parent and tree metadata are checked separately.

A fresh named-main observation is recorded after publication. The preselected equality alias is valid only if it equals the verified merge/readback ref; otherwise both complete artifacts must be read at one observed immutable main commit. This plan does not equate publication verification with application execution or upstream acceptance.
