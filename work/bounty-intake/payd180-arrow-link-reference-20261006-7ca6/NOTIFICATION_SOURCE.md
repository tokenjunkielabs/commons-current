# Notification reference: source qualification

This adds two new documentation artifacts, NOTIFICATION.md and NOTIFICATION_SOURCE.md, to the existing PayD180 reference packet. It changes no production file or earlier documentation entry.

## Task and distinct scope

The retained warm issue Protocol-Guild/PayD #180 asks for reusable component documentation. This entry documents the local useNotification context API and NotificationProvider implementation, including the actual argument mapping, void return boundary, consumer ordering and explicitly unverified display host. It is distinct from the existing ArrowLink, ThemeToggle, ErrorBoundary, ContractErrorPanel, autosave, Avatar, CountdownTimer, CSVUploader and EmployeeList references.

A possible upstream destination is docs/components/Notification.md; that exact path is absent from the complete retained canonical tree. This inventory observation is not a universal claim about external documentation or contributor work. No upstream destination is written by this packet.

The new dedicated Commons PR search for "PayD" "useNotification" "reference" returned no entries. That is only the bounded query result, not proof of globally unowned work. Root custody was consulted for exact documentation conflicts; no absence certification is inferred from a missing retained conflict.

Protected PayD478 / carriers720 and428 cover earlier toast implementation work. Their sources, bodies, handlers and disposition are not reopened or replayed. This packet documents the current canonical API and makes no toast-source correction or whole-issue completion claim. The source and artifact compositions in other PayD packets remain untouched.

## Acquired evidence

Canonical donor is Protocol-Guild/PayD at 171c74b454daba241bfb75f36d10a0a3a77a68e5. Two narrow full-file reads acquired useNotification.ts and NotificationProvider.tsx. Each returned native blob matches the complete canonical tree entry and an independent Git blob identity over the returned UTF-8 text.

Complete retained EmployeeEntry.tsx, CertificateDownloadButton.tsx and App.tsx were reused only to document concrete consumers and the EmployeeEntry route connection. Their texts are independently hashed against the pinned tree. No form submission, network request, wallet generation, certificate lookup, download, clipboard operation or notification was performed.

The earlier #32033 reference retains a source-qualified main-entry mounting narrative and the exact main.tsx path/blob/byte identity. Its full-body private locator does not survive in this continuation; root also retains only that metadata. The entry is explicitly attributed as prior qualification, not reconstructed, reacquired or counted as a new full-body check. Notification host placement and provider order are not freshly asserted.

The retained certificate consumer's complete parent path/blob locator is also absent. Only the already acquired component body is used. This limitation is not resolved by guessing a TransactionHistory path or reacquiring accepted sources.

## What the source establishes

The interface has four methods returning void. The provider wraps Sonner calls in four useCallback functions with empty dependency lists, without returning their invocation results. The three typed variants pass description as an option; the basic notify variant does not. The hook's missing-context guard and literal error message come directly from its source.

No display host is rendered by the acquired provider. No renderer, installed Sonner implementation, toast identifier, timing, announcement, persistence or delivery guarantee is inferred from these wrappers. The any casts and lint suppressions are reported as existing source, not validated dependency contracts.

The reference's illustrative snippets are newly authored and have not been compiled or executed. They demonstrate the local public surface only; no fixture, application module, hook or event handler is evaluated.

## Attribution and license

Protocol-Guild/PayD's original contributors retain credit. This continuation preserves the existing complete Apache-2.0 LICENSE at the original #32001 merge: https://github.com/woahwhattheheck/commons/blob/f4b583c3d4f7940ab5912470ffb8bfeca540bc47/work/bounty-intake/payd180-arrow-link-reference-20261006-7ca6/LICENSE . Its independently retained identity is 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64, 11357 UTF-8 bytes. No duplicate license or changed notice is introduced.

The root-entry attribution uses the already published #32033 guide. No fresh provider recovery or held-route substitution is performed. Earlier exact source, search, carrier-body and metadata holds remain in force, including the unrelated #32074 final PR-files metadata gap.

## Verification and publication boundary

Validation consists of complete source reading, static caller relationships, UTF-8/Git identity checks, and complete immutable artifact readback. The packet includes no source patch. It does not include React execution, notification display, browser or screen-reader interaction, Sonner invocation, storage, network, forms, account actions, build, compiler, tests or upstream writes.

Before publication, both artifacts are frozen with their independent expected Git blobs. The publisher must create only these two new mode100644 files from a fresh Commons base. Full immutable text/native/independent identities, merged PR metadata, exact paths and parent/tree relationships are checked. A separate named-main observation can alias the verified merge only if main, merge and readback_ref are identical; otherwise both complete artifacts are read at one observed immutable main commit. No later moving-main chase is intended.

Publication verifies the documentation artifacts, not application behavior, ownership, external contributor acceptance or the complete PayD180 task.
