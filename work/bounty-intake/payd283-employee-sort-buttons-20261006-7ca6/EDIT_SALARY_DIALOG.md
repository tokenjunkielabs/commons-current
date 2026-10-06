# PayD EmployeeList: associate the Edit Salary panel with its title

The reachable Edit Salary panel has an existing visible h2 and its input/Cancel/Save controls, but the acquired source represents the panel as an unnamed generic div. This incremental patch gives the inner panel the dialog role and connects its accessible name to that same heading. It preserves the completed Salary input label and all existing actions.

## Source and composition

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`.
Changed production path: `frontend/src/components/EmployeeList.tsx`, mode100644.

This patch applies after the existing #32014 sort buttons, #32038 aria-sort and #32060 Salary input-name patches. Their artifacts, guides, attribution and license remain untouched. The complete retained composed preimage is the prior #32060 result; no accepted correction or source publication is replayed.

| Complete source | Git blob | UTF-8 bytes |
|---|---|---:|
| Canonical EmployeeList.tsx | 277684e5f87cabd72ff5aadd04299a5360fdf3e0 | 20441 |
| Composed preimage after #32060 | 6be2d27fdc4c280b3db09ad2b36192eeef6f2e4e | 21705 |
| Prepared source | f2f789e98cfe9aa9eed815e5672cb900b7605b2e | 21897 |
| EmployeeEntry.tsx caller | b89a5c832191a19a52c4f7b99201da5ece9acef8 | 11774 |
| App.tsx route | acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c | 6460 |
| frontend/package.json | 33e58d67eca11b200b6988835b1f8450f179d2c2 | 2534 |

The canonical component and retained caller bodies have full native and independent identity matches against the complete canonical tree. The dependency declaration was acquired once for this new hook consumer at the same immutable donor commit, with full returned SHA, independent Git identity and tree path/mode/size agreement. It declares react and react-dom ^19.2.0, and @types/react ^19.2.14. This establishes declarations, not installed dependency contents, a build or a hydration result.

A new bounded Commons all-state query for PayD / EmployeeList / dialog, topn10, returned only the existing #32060 input-label packet. That accepted input hunk is preserved. Root retains no exact same role/name hunk completion or hold. This is a bounded overlap disposition rather than a global ownership census. Earlier external carriers and all exact held/protected families remain unchanged.

## Actual reachable display path

App renders EmployeeEntry at /employee. Its list branch renders EmployeeList. Desktop and mobile pencil controls in the acquired list open showEditModal with the selected employee, regardless of whether onEditEmployee was supplied. The conditional panel contains the existing Edit Salary heading, employee context, the Salary-labelled number input, Cancel and Save.

The actual EmployeeEntry invocation does not supply onEditEmployee. The existing submit handler invokes that optional callback only when available and closes the panel afterwards. This patch neither supplies a callback nor changes persistence, authorization, salary conversion or business behavior. The mounted Save action therefore remains unable to update through an absent callback. No employee value, salary record, open/save/cancel action or financial operation was executed.

The declared Add modal has no established opening call in this retained path and is excluded. The Delete confirmation and every other wrapper, control, handler and caller remain byte-identical.

## Narrow association

One unconditional top-level useId call creates editSalaryTitleId. The existing inner panel receives role="dialog" and aria-labelledby referencing that identifier. The persistent h2 receives the matching id. The existing visible heading words and class strings are retained. The input, Cancel and Save remain descendants of the named panel.

No aria-modal, aria-hidden or inert attribute is added. There is no focus entry, return-focus, trap, Escape handler, autofocus, tab-order or backdrop behavior change. This names the dialog container; it does not complete the modal-dialog interaction pattern.

Primary semantics acquired for this change:

- W3C APG Dialog (Modal) Pattern: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- React useId reference: https://react.dev/reference/react/useId

The APG identifies the dialog container role and association to a visible title as naming semantics. It separately requires actual outside-interaction prevention before marking a dialog modal, and describes focus/keyboard behavior that this patch does not implement. The existing overlay's visual appearance alone is not treated as proof of modality.

React documents useId for accessibility IDs and requires top-level Hook calls. The new call is unconditional in the synchronous component and is used for the heading relationship, not list or cache keys. No React example, browser widget or screen-reader demonstration was run; no wider accessibility, unique-across-independent-roots or hydration guarantee is claimed.

## Source verification

The actual serialized patch has three hunks, twenty-eight complete rows, ten insertions and three deletions. Forward application produces the exact 21897-byte prepared source; inverse application returns the exact 21705-byte preimage. Reversing the three exact authored replacements also recovers every original byte. The existing edit/submit handler source and all regions outside those changes match.

These are string, patch and Git identity checks. They do not instantiate a component, generate a runtime ID, open a dialog, enter a value, trigger a callback, compile types, execute a test or observe assistive technology.

## Artifacts, attribution and publication

name-edit-salary-dialog.patch is the new incremental source change. EDIT_SALARY_DIALOG.md is this guide. Both are additive files in the existing PayD283 packet. The original Apache-2.0 LICENSE, blob 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64, 11357 bytes, remains unchanged. Original Protocol-Guild/PayD contributors retain attribution; no full donor module or caller is republished.

The guarded Commons publication reads both new artifacts completely at its immutable readback ref and compares prepared text, native SHA and independent identity. Final PR, paths, tree and parents are checked where available; any failure is preserved and disclosed. A fresh same-repository main equality can provide a separate predeclared alias only when it equals the verified merge/readback ref; otherwise both full files are read at one observed immutable main without branch chasing.

No application, browser, DOM, focus action, employee data, account, wallet, payment, compiler, runtime, test, fixture, upstream submission, sponsor or acceptance action is performed. Existing focus/modal usability and the missing mounted edit callback remain explicit limitations.
