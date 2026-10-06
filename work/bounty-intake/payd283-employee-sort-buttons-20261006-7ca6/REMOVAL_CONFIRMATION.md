# PayD EmployeeList: identify the existing removal confirmation

The reachable Confirm Removal panel has a visible title and one short confirmation paragraph, but its acquired source exposes only a generic inner div. This incremental patch gives that inner panel the dialog role and associates its name and description with the existing text. It preserves the two action buttons, all callbacks and the actual mounted parent's missing removal callback.

## Source, composition and attribution

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`.
Changed source: `frontend/src/components/EmployeeList.tsx`, mode 100644.

Apply this patch after the saved #32014 native sorting buttons, #32038 active-header aria-sort, #32060 Salary input name and #32079 Edit Salary dialog association. Their artifacts, guides, original authors and Apache-2.0 notice stay unchanged. This is a new association on a different reachable panel; it does not republish or replay those accepted corrections.

| Complete source | Git blob | UTF-8 bytes |
|---|---|---:|
| Canonical EmployeeList.tsx | 277684e5f87cabd72ff5aadd04299a5360fdf3e0 | 20441 |
| Composed preimage after #32079 | f2f789e98cfe9aa9eed815e5672cb900b7605b2e | 21897 |
| Prepared source | ab27936bf8f424751fd38af5fff45952c50a12d3 | 22213 |
| EmployeeEntry.tsx caller | b89a5c832191a19a52c4f7b99201da5ece9acef8 | 11774 |
| App.tsx route | acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c | 6460 |
| frontend/package.json | 33e58d67eca11b200b6988835b1f8450f179d2c2 | 2534 |

These source bodies and the complete canonical tree were already acquired and matched by native and independent Git identities. The saved #32079 postimage supplies the full new preimage. The package declaration, acquired for #32079, declares React/react-dom ^19.2.0 and @types/react ^19.2.14. It is retained declared metadata, not an installed declaration body or a build result. This continuation performs no source-body reacquisition.

A genuinely new bounded all-state Commons pull-request search for PayD / EmployeeList / Confirm Removal, topn 10, returned zero entries through the dedicated github_search_prs tool. This is bounded overlap evidence, not a global ownership census. All earlier external carriers, protected families and exact failed routes stay unchanged.

## Actual mounted and reachable path

App's /employee route renders EmployeeEntry, whose list branch renders EmployeeList. Both the desktop trash-icon control and mobile Remove control unconditionally set showDeleteConfirm to an open state with the selected ID. The conditional panel contains its existing Confirm Removal h2, one short question, Cancel and Remove.

EmployeeEntry does not supply onRemoveEmployee. The existing confirm handler invokes that optional callback only when both its saved ID and callback exist, then closes the panel. That exact handler and the parent's invocation remain unchanged. The mounted confirmation therefore does not gain a removal implementation. No employee, identifier, record, form, callback, account or removal operation was executed.

The Add modal's opening path remains unestablished and excluded. The already named Edit Salary panel and all source outside the two exact replacements are byte-identical.

## Association and its limits

Two unconditional top-level useId calls create distinct title and description identifiers. The existing inner panel receives role="dialog", aria-labelledby referencing the title ID, and aria-describedby referencing the description ID. Its h2 and existing single paragraph receive the corresponding IDs. The action buttons remain descendants, their text/classes/onClick handlers unchanged. Existing visible words and class strings are preserved.

No aria-modal, alertdialog, inert or aria-hidden attribute is introduced. Focus entry, focus return, trapping, Escape, tab order, backdrop behavior and outside-interaction prevention remain existing behavior. The patch provides role/name/description relationships, not a complete modal interaction pattern or an observed screen-reader announcement.

Primary material already acquired in the preceding source qualification is retained and reused without a provider replay:

- W3C APG Dialog (Modal) Pattern: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- React useId reference: https://react.dev/reference/react/useId

The APG associates a dialog with its visible title and permits an optional description for simple explanatory content. Its cautions about complex structures do not apply to this one short paragraph. Modality and focus/keyboard requirements are separate and not implemented here; visual overlay styling alone is not treated as modal behavior. React documents useId for accessibility relationships and unconditional top-level Hook calls. These two IDs are not list or cache keys. No primary example or application component was executed.

## Exact source checks

The serialized patch has two complete hunks and twenty-nine rows, with fourteen insertions and three deletions. Forward application produces the exact 22213-byte prepared source, and inverse application recovers the exact 21897-byte preimage. Reversing the two authored replacements also returns every original byte. The complete delete-confirm handler, complete Edit Salary panel, both opening controls, all existing state/value/callback code and source outside the replacements match.

This verification compares retained text and Git identities only. It does not generate an ID, instantiate a component, compile types, evaluate data, exercise a button, render CSS, run a test or observe assistive technology. Separate roots, hydration, stacked panels, focusability and full accessibility acceptance are outside the claim.

## Artifacts and publication

name-removal-confirmation.patch is the new incremental patch. REMOVAL_CONFIRMATION.md is this guide. Both are new additive files under the existing PayD283 artifact directory; the original Apache-2.0 LICENSE, blob 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64, 11357 bytes, and all earlier source patches remain untouched. Original Protocol-Guild/PayD contributors retain attribution; no complete donor module or caller is republished.

Guarded Commons publication compares both complete immutable readbacks with prepared texts, native blob IDs and independent Git hashes. Final PR, paths, commit/tree/parents and fresh main metadata are separately checked where available, with any failures retained and disclosed. A predeclared main equality alias is used only if observed main equals the verified merge/readback ref; otherwise both complete artifacts are read at one observed immutable main without chasing the branch.

No application, browser, DOM, record, focus, removal, account, wallet, payment, runtime, compiler, test, fixture, upstream or sponsor action is performed. Missing parent callback and incomplete modal interaction behavior remain explicit limitations.
