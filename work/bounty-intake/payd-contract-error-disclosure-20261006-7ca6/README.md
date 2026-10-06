# Contract error panel disclosure control

The mounted PayD ContractErrorPanel expands and collapses its details through a div with only an onClick handler. This patch gives that existing action a native non-submit button, exposes its current expanded state and declares a focus-visible outline. It changes no error producer, parser, transaction handler or clipboard operation.

## Production scope

Donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`.

| Source path | Before Git blob / bytes | After Git blob / bytes |
|---|---|---|
| frontend/src/components/ContractErrorPanel.tsx | 83a0108c600efcea33562edc242d47519fa71e0b / 2619 | dabe5a24d61ed10ca51f91655ee9e7542d55ad9b / 2709 |
| frontend/src/components/ContractErrorPanel.module.css | a26e6b5cae666c82b572f9afea25364e246435e1 / 3002 | 465474f848b00b235ee06d322f7e978e56e7ee46 / 3196 |

Both source modes remain 100644. The complete patch is +22/-6 across two hunks and 50 explicit rows. The component contributes +11/-6 and CSS +11/-0. Full serialized forward application produces both prepared postimages; inverse application restores both complete preimages. These are string-materialization checks, not component or stylesheet execution.

## Behavior change

The existing header becomes a button with type="button". Its onClick closure is preserved exactly, so activation continues toggling the same isExpanded state. The new aria-expanded uses that same boolean, which also controls whether the content renders. No second key handler or independent expanded state is added.

The header's two existing layout groups become spans while retaining their flex classes and contents. The title, supplied error code and conditional chevrons are unchanged. The Copy control stays outside the disclosure button in the expanded content, so this change does not nest an interactive control inside another.

CSS declares a full-width header, removes a native border/background, inherits color/font/text alignment, and retains the existing flex alignment, padding, cursor, selection and hover declarations. A focus-visible outline uses the existing title color with a negative offset so the declared ring lies inside the header. These declarations support the new native control; they do not prove pixel-identical layout, contrast, cross-browser behavior or the effect of every external style.

The [W3C disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/) describes a button controlling content visibility, Enter/Space activation and an aria-expanded value matching visibility. It treats aria-controls as optional. This patch uses the native button behavior and existing boolean; it does not add a generated ID or claim a complete accessibility audit. No browser, keyboard or assistive-technology session was run.

## Preserved source

The complete component prefix before the header and suffix from the content condition onward are byte-for-byte unchanged. This preserves the required nullable error input, className, initial expansion state, null return, raw-detail predicate, displayed message/action/raw text, Copy handler and every content-section byte.

Every original stylesheet line is retained; only header/button defaults and its focus-visible rule are added. The panel, message, action, raw-content and Copy styles are unchanged.

The patch neither changes the supplied suggested-action text nor carries it out. It does not invoke, authorize, sign, submit, retry or validate a transaction. No parser, error-code map, contract service, wallet, socket, account, application data or real error event is changed or accessed. Existing copy availability/rejection handling and expansion persistence across error-prop changes remain as before.

## Connected source and earlier documentation

The complete acquired CrossAssetPayment source imports ContractErrorPanel and renders it unconditionally with the existing contractError state. The complete retained App source establishes the /cross-asset-payment route; matching retained main mounts App. The acquired hook connects that state to the exported ContractErrorDetails record. This is static mounting evidence, not an executed transaction flow.

The earlier [ContractErrorPanel reference at #32050](https://github.com/woahwhattheheck/commons/blob/788708658cb4ba51eb12e1530f251402959f499d/work/bounty-intake/payd180-arrow-link-reference-20261006-7ca6/CONTRACT_ERROR_PANEL.md) describes the unchanged canonical donor, including its original div header. It remains immutable and unmodified. This separately applicable patch changes only that documented header limitation and associated CSS; the reference's other source contracts are preserved. No combined upstream adoption is asserted.

The source table above uses complete native returned text and independent Git blob identities. The new full CSS acquisition also matches its exact retained canonical-tree entry. Previously acquired component/caller/type/hook/App/main bytes are reused for this new source correction, without repeating their provider reads or invoking their behavior.

## Bounded overlap and attribution

A new bounded Commons PR query for "PayD" "ContractErrorPanel" "disclosure", all states and topn 10, returned no entries. Root retains no exact same expansion-header hunk completion or hold. These are bounded custody observations, not global absence or assignment.

The separate issue185/PR669 whole-body hold remains untouched. No held carrier was expanded, no old accepted patch was reconstructed, and no broader financial/authentication family is superseded. The documentation packet is not presented as upstream feature acceptance.

Original Protocol-Guild/PayD contributors retain credit. The included LICENSE is the unchanged, previously acknowledged Apache-2.0 notice, Git blob 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64, 11,357 UTF-8 bytes. Existing component-reference files and their notice remain unchanged in their own directory. There is no original-author census claim.

## Verification and limits

Static verification covers complete source identities, exact serialized forward/reverse application, all unrelated component bytes, original CSS lines, the actual route/caller relationship and the native-control/expanded-state contract. A peer's retained-description reasoning identified no concrete contract concern; it was not a source, runtime or approval gate.

No application, React, CSS layout engine, browser, DOM event, clipboard, parser, compiler, test, fixture or financial/account operation was executed. There is no whole-build, complete accessibility, geometry, contrast, universal error recovery or upstream acceptance claim.

Publication contains only disclosure-button.patch, this guide and the retained license. The guarded publisher compares complete immutable artifact texts with their prepared/native/independent identities and checks PR/body/paths/tree/parents. A fresh named-main equality alias is preselected only when the observation equals the verified merge/readback ref; otherwise every artifact must be read fully at one observed immutable main commit.
