# ContractErrorPanel reference: source qualification

This continuation adds CONTRACT_ERROR_PANEL.md and this source note to the existing PayD180 documentation directory. Prior ArrowLink, ThemeToggle and ErrorBoundary references and the original notice remain unchanged. There is no production patch.

## Scope and evidence selection

The retained warm [Protocol-Guild/PayD issue180](https://github.com/Protocol-Guild/PayD/issues/180) concerns reusable component documentation. This entry documents the canonical ContractErrorPanel exports, typed input, null and raw-detail selection, expansion state, current header/copy controls and one actual mounted caller.

The intended documentation subject is the presentation component, not a contract or payment workflow. The guide does not validate, recommend, execute or modify financial actions. The action field is merely caller-supplied display text. No raw transaction result, account information, live error, environment value or application data was collected.

A possible upstream documentation destination is docs/components/ContractErrorPanel.md. The full retained canonical tree has 753 entries and truncated:false; no docs/components/ entry appears. That is a pinned-tree observation only.

A new bounded Commons PR query for "PayD" "ContractErrorPanel" "documentation", all states and topn 10, returned no entries. It does not certify global absence or contributor ownership. Existing financial/authentication families, exact failed routes, and the separately held error-boundary issue185/PR669 remain protected. No held body was expanded to create this reference, and no upstream action is taken.

## Full source custody

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`.

Four full files were newly acquired at that immutable ref: ContractErrorPanel.tsx, contractErrorParser.ts, useContractError.ts and CrossAssetPayment.tsx. The full returned native identities match independently computed Git blob identities and their canonical tree entries. Each uses mode 100644; exact paths, hashes and byte counts appear in the reference.

The parser file was acquired to establish the actual exported ContractErrorDetails interface and the imported producer relationship. Its classification rules, examples and dependencies were not executed or used to diagnose a failure. No parser correction is proposed.

The complete retained App and main bodies match their canonical tree identities. Main's older original acquisition URL belongs to waterWang's cf853ac31818de9400bf558d0e74ef44ff2a3744 carrier; its full bytes match the canonical main tree entry f84f187971ba135010c48e69fda10f0c0f71ebd9. It is reused as matching retained source, not claimed as a fresh provider acquisition. App supplies the exact /cross-asset-payment route, and its newly acquired component imports and renders ContractErrorPanel.

The bounded canonical code search returned five paths with incomplete_results false: the panel, CrossAssetPayment, EmployeePortal, PayrollScheduler and generated tsbuildinfo. Only the newly acquired CrossAssetPayment route is qualified here as a complete caller chain. Search completeness metadata is not a universal consumer or runtime census. The generated artifact was not expanded or treated as build evidence.

## What the reference establishes

The component's local prop interface requires a nullable error record and accepts an optional root className. Its named/default exports are both documented. The input interface consists of three required strings and an optional raw string.

The table of raw-detail branches follows the exact source predicates and short-circuit expressions. No constructed error payload, decoding example or test fixture was evaluated. The usage line passes an already-declared caller state and does not fabricate application data.

The state description distinguishes a still-mounted panel returning null from the parent removing the component. The existing state initializer is above the null guard and there is no error-change reset effect. The React primary source explains state identity only; no React application or documentation example was run.

Current omissions are recorded as limitations: the clickable header is a div without the listed keyboard/state semantics, and the Copy handler has no local completion/error feedback. This reference does not silently repair either behavior, assert successful clipboard access or infer a complete accessibility result.

The actual hook/caller relationship is described without exercising any event, account, contract, socket, signing, payment, parser or clipboard path. No production error or failure incident is claimed.

## Attribution and license

Original Protocol-Guild/PayD contributors retain credit. This note does not assert an exhaustive author census or supersede contributor proposals.

The existing [LICENSE at the original #32001 immutable merge](https://github.com/woahwhattheheck/commons/blob/f4b583c3d4f7940ab5912470ffb8bfeca540bc47/work/bounty-intake/payd180-arrow-link-reference-20261006-7ca6/LICENSE) preserves the full Apache-2.0 notice, Git blob 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64, 11,357 UTF-8 bytes. It is referenced rather than copied again. The immutable locator is an acknowledged original artifact, not a statement about moving main.

## Primary source and validation

[React: Preserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state) supplies the general state-identity explanation. The documentation's observed v19.3 heading is kept separate from the repository's unexecuted dependencies.

Validation is static source/caller reading, full native/independent identity comparison and exact publication readback. No runtime, browser, clipboard, route traversal, test, compiler, package installation, fixture or service operation was performed. There is no parser-correctness, financial diagnosis, copy-success, keyboard, whole-build or complete issue-acceptance claim.

Publication adds only these two UTF-8 documentation paths. The guarded publisher checks their pinned new blob identities and complete immutable readbacks; final PR/body/path/parent/tree metadata are compared separately. A preselected equal-main alias is valid only if a fresh named-main observation equals the verified merge/readback ref. Otherwise both full files must be read at one observed immutable main commit. Publication verification is not application execution or upstream acceptance.
