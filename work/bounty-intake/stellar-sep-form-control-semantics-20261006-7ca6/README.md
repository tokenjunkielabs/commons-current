# SEP preset-control names and selected flow state

Both acquired SEP forms display a Preset anchors label beside a native select, but neither label is associated with that select. SEP-24's Deposit and Withdraw buttons also expose the selected flow only through visual classes. This incremental source proposal adds those relationships while preserving the existing form behavior.

## Exact composition and mounted callers

Canonical donor: Stellar-Analysis/frontend at `482ee456369418ef82c4056718cb82d3468f762b`.

The complete acquired `src/app/[locale]/deposit-withdraw/page.tsx` (blob `f064a0a1331da46f035b54602f98093b2e0c8c8d`, 1357 UTF-8 bytes) dynamically imports the named Sep24Flow with SSR disabled and renders it without props. The complete acquired `src/app/[locale]/send-payment/page.tsx` (blob `390ab4f17dd7a0461e26c3e77e8a310b962bc658`, 1201 bytes) similarly mounts Sep31PaymentFlow. Their native pins and independent full-file identities were matched during the original source qualification; no route was reacquired for this continuation.

Apply this patch after the source proposals in Commons [#32133](https://github.com/woahwhattheheck/commons/pull/32133) for SEP-24 and [#32128](https://github.com/woahwhattheheck/commons/pull/32128) for SEP-31. It is not a direct patch against the unmodified canonical component files. The exact composed inputs were retained in source custody, not reconstructed from a description.

| Changed component | Required preimage | Before bytes | Postimage | After bytes |
| --- | --- | ---: | --- | ---: |
| src/components/Sep24Flow.tsx | fd50330e97b1238581560ac460a3eaac19ba2103 | 14981 | a437c8fb9b2c06cbac4800ecedf5e7e94dedd39c | 15182 |
| src/components/Sep31PaymentFlow.tsx | 1e1caa1995d9b54d74848ad5d7b72d7e10dc9781 | 16780 | 41581c85b3331ec5f43ba009c6b3da6dfffd47ae | 16880 |

Canonical full component identities remain SEP-24 `1c11c3c5669b3cb6406d40e474460dc6e695afb1` / 14513 bytes and SEP-31 `52907a4ab7e7577f74d792d5375cf3cb2c9b73c5` / 16658 bytes. These identities were independently computed from complete source responses at immutable contents URLs; those responses did not supply separate native SHA fields.

## Change and source rationale

Each component imports useId and invokes it once, unconditionally at component top level. The existing preset label receives htmlFor and its existing native select receives the matching id. No DOM wrapper, new control, name attribute, list key, form registration or selection callback is introduced.

The two existing SEP-24 type=button controls receive aria-pressed from the same flowKind comparisons that already determine their visual classes. Deposit and Withdraw retain their fixed labels, existing click callbacks and exclusive state transitions. This does not implement a radio-group pattern or alter keyboard navigation.

React's successful current primary useId reference documents top-level hook use for accessibility relationships and demonstrates matching htmlFor/id pairs: https://react.dev/reference/react/useId. The successful W3C APG button pattern documents aria-pressed for a toggle button and keeping its label stable: https://www.w3.org/WAI/ARIA/apg/patterns/button/. These contracts support the proposed source attributes; they are not evidence of a rendered accessibility tree or assistive-technology announcement.

Retained donor manifest/lock evidence records React 19.2.7 and React types 19.3.0. The currently served React documentation is not a claim about installed packages, compilation or this application's runtime behavior.

## Preservation and qualification

The incremental patch is +10/-4 across 8 hunks and two files. Removing only the new IDs/attributes/hooks and import members restores each complete required preimage byte for byte. The previously completed provider and query-wiring proposals remain intact.

All field values, styles, labels, selected-anchor logic, query hooks, loading/error guards, validation, dirty-state gating, mutation and payment handlers, parameters, popup logic and status classification are unchanged. No shared FormField code or query wrapper is edited. Commons #32137's independent retry-count correction and the separate logging qualification are outside these paths.

Dedicated all-state donor PR queries for Sep24Flow plus label and Sep31PaymentFlow plus label returned zero; the bounded Commons SEP/preset/label query also returned zero. These observations do not prove global absence of work or original ownership. Earlier retained current-path histories identify only christabel888's flattening relocation `59fad72d9fbef9cfd6f47e215392da44488fcdc4`; the relocation is not original-author evidence. No new issue claim, assignment, upstream submission, acceptance or payment conclusion is made.

## Checks and limits

Pure retained-source checks independently computed full preimage/postimage identities and reconstructed both directions from every serialized unified hunk. All hunks and rows were included. Separate checks established exact preservation of all bytes outside the selected additions and unconditional useId calls. No application source, tests, fixture, compiler, browser, form control, API, wallet, credential, account or payment operation was executed.

The earlier provider proposals remain explicitly uncompiled and preserve their React Hook Form documentation holds. The SEP-24 unused clearFormData helper reference, broader integration defects and the prior source limits are not settled by adding labels or pressed states. This packet makes no whole-form, whole-accessibility, WCAG conformance, assistive-technology, focus, hydration or operational-readiness guarantee.

The retained complete donor tree has no AGENTS/RULES path. Its EventSource-specific contribution/release guidance does not authorize executing tests or npm release workflows in this source-only session. The three distinct docs MIT notices do not establish a blanket license for these components. The Commons tree therefore receives only this minimal patch and guide; donor code and contributor ownership remain unchanged.
