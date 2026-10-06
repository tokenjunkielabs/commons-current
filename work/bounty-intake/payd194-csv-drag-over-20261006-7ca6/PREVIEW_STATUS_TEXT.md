# CSVUploader: text for each preview status

The existing Preview table's Status cell contains only a check or warning icon. This incremental patch keeps those icons and adds visible Valid or Invalid text from the same row.isValid boolean. A surrounding aria-hidden span marks the now-redundant icon branch as presentation; the new text is outside that span.

## Exact source and composition

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`.
Production path: `frontend/src/components/CSVUploader.tsx`.

| Stage | Git blob | UTF-8 bytes |
|---|---|---:|
| Original canonical module | 26b62ac2f50ae4d48d7ce4a416b7841f8a2e742f | 7645 |
| After #32009 drag-over correction | 0d4d54488a8e38eea15aa0656af7f95601c5efdb | 7692 |
| After #32041 latest-read completion | 81d91b45eb0ecc0bf51b298340cbd258534a081b | 7880 |
| This text-status postimage | c3e7ef2b49d275cab07762ce9896ae1264fdd36f | 8039 |

Apply allow-drag-over.patch, then latest-read-completion.patch, then text-preview-status.patch. The complete retained prior postimage was used directly; no accepted source or old calculation was reacquired or replayed. A fresh donor-main metadata guard still matches the canonical commit.

The new serialized change is +8/-5 in one complete hunk of 19 rows. Most changed lines indent the unchanged icon conditional inside its new span. Whole forward application produces the exact postimage; reverse application restores the exact preimage. Replacing only this one Status cell with its original text restores every other module byte. Icon choice and icon class strings are unchanged.

## Connected display and producer

The complete retained App /employee route renders EmployeeEntry, which renders EmployeeList. EmployeeList's Import from CSV button sets showCSVUploader true; the resulting CSVUploader receives requiredColumns and handleDataParsed. The existing successful read path fills parsedData and calls the parent. The Preview table renders only when parsedData.length is positive, and each parsedData row supplies this Status cell.

Retained complete caller identities are App `acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c` (6460 B), EmployeeEntry `b89a5c832191a19a52c4f7b99201da5ece9acef8` (11774 B), and original EmployeeList `277684e5f87cabd72ff5aadd04299a5360fdf3e0` (20441 B). Later EmployeeList sort buttons, aria-sort and salary-input naming are protected, separate source changes; this patch does not alter EmployeeList or assert a new combined identity for it.

The parser records errors for absent required fields and applicable supplied validators, then sets isValid from errors.length === 0. The actual EmployeeList caller passes name, email, wallet, position, salary and status as required columns, with no custom validators. The labels therefore describe only that existing local validation result. They do not certify CSV quoting, address syntax, salary correctness, account existence or business eligibility.

EmployeeList currently maps every returned row without filtering isValid. This display correction does not block, admit or persist any import, and does not resolve that separate policy. The existing parent callbacks, errors list, valid/invalid summary counts, file name, parsed values and Add action remain exact.

## Text and presentation contract

The [W3C explanation of non-text content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html) describes equivalent text as a way to convey information otherwise carried by visual content, and says purely decorative content should be ignorable by assistive technology. This change supplies the row's existing two-state meaning as actual text and keeps the redundant icons inside an aria-hidden ancestor.

Only the row-status icons receive that ancestor; the text and cell remain outside it. No role, tab stop, live region, event handler, input name or validation rule is introduced. There is no dependency on a new icon-component property or hidden-text CSS class. The icons retain their existing size/color classes.

Visible words may change cell width, wrapping or row height. The patch does not promise unchanged geometry, particular contrast, a spoken phrase, announcement timing, universal assistive-technology behavior or complete table/WCAG conformance. The new English labels match the existing English preview terminology; localization is not added.

## Ownership and attribution

A fresh bounded Commons query for PayD / CSVUploader / status / text returned no entries within its top-ten scope. That does not certify exhaustive ownership absence. Root's retained custody has no exact same-cell completion or hold; this is a bounded custody statement, not a permission gate.

The earlier qualified issue194 context remains: its dated bounded PR search returned no entries, and the observed contributor comment was shobhamerabacha-star's assignment request, not an assignment grant. The retained latest path-history attribution is commit `4f5dd01b31a0b7445e50408398b6fbe9b52d8f48`, author name Mainnet-ops, not an original-author census. All PayD contributors retain credit.

This publication adds only the patch and this note. The #32009/#32041 patches and guides remain untouched, as does the full Apache-2.0 LICENSE `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`, 11357 bytes. All exact held routes and protected related families remain held. No issue acceptance, sponsor approval, reward or upstream authority is inferred.

## Verification and limits

Verification is static complete-source/caller reading, primary text-alternative reasoning, independent UTF-8 Git blob identities, exact serialized forward/reverse materialization and preservation of every byte outside the chosen cell. Both new published artifacts receive complete immutable text/native/independent checks and final PR/path/tree/parent checks. A predeclared fresh same-repository main equality can separately alias those checks only when it equals merge and readback ref; otherwise both complete artifacts are read at one observed immutable main.

No file, file picker, upload, drop event, FileReader, CSV parser, validator, callback, employee record, account/payment action, browser, screen reader, compiler, test or fixture is executed. Existing invalid-selection, pending-read, unmount, parser and import-policy limitations remain. This is a source presentation correction, not a complete upload/import or runtime accessibility claim.
