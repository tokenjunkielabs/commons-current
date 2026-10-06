# EmployeeList: name the Edit Salary input

The existing Edit Salary overlay contains an unnamed number input. Its heading supplies visual context, but the input has no explicit label association or accessible-name attribute. This incremental patch adds `aria-label="Salary"` to that one input. It changes no visible content, form value, callback, submission or persistence behavior.

## Source and exact composition

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`.
Production path: `frontend/src/components/EmployeeList.tsx`.

| Stage | Git blob | UTF-8 bytes |
|---|---|---:|
| Original canonical module | 277684e5f87cabd72ff5aadd04299a5360fdf3e0 | 20441 |
| After #32014 native sort buttons | 29fee53b3a74b52032d07700f91e6afc2b891f21 | 21006 |
| After #32038 active aria-sort | 9c62f3d3208cac07d47189e201fd9e6370627390 | 21671 |
| New input-name postimage | 6be2d27fdc4c280b3db09ad2b36192eeef6f2e4e | 21705 |

Apply the existing sort-header-buttons.patch, then expose-active-sort.patch, then name-edit-salary-input.patch. This packet reuses the complete retained source and already acknowledged postimage; it does not repeat accepted source acquisition or execute those changes. The new patch is +1/-0 in one full hunk of seven rows. Exact forward application produces the stated postimage, reverse application restores the complete preimage, and deleting only the added attribute restores every prior byte.

The fresh donor-main metadata guard still identifies the same canonical commit. These are source artifact identities, not deployed application identities.

## Reachable control and limits of the caller

The complete retained App routes /employee to EmployeeEntry. The retained EmployeeEntry renders EmployeeList with employees, onEmployeeClick and onAddEmployee. It supplies NO onEditEmployee callback. The original list nevertheless has unconditional desktop and mobile edit buttons that initialize editSalary and open showEditModal with the selected employee. The modal condition requires both open and an employee; its controlled input is therefore reachable from those existing controls in the acquired source.

| Retained caller source | Git blob | UTF-8 bytes |
|---|---|---:|
| frontend/src/App.tsx | acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c | 6460 |
| frontend/src/pages/EmployeeEntry.tsx | b89a5c832191a19a52c4f7b99201da5ece9acef8 | 11774 |

The salary-value buttons are additionally conditional on onEditEmployee, but the separate edit buttons are not. This qualification does not infer that the mounted caller can persist edits. handleEditModalSubmit invokes the optional callback only when supplied and then closes the modal. With the acquired EmployeeEntry caller, saving closes without invoking an edit callback. That existing missing wiring is explicitly unresolved.

The patch preserves type=number, value={editSalary}, Number(e.target.value), the original change handler, classes, opening controls, modal condition, Cancel and Save callbacks, all employee data handling, sort buttons and aria-sort. It adds no validation, minimum, maximum, currency, unit, amount formatting or financial behavior. It neither opens the modal nor reads or changes any employee record.

The separately declared Add modal was not selected: its opening path was not established. Its inputs and every other control remain outside this correction.

## Naming contract

[W3C Technique ARIA14](https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA14) describes aria-label as an accessible-name mechanism when clear visible label text is unavailable through the design, and includes number-input examples. The label should describe the control's purpose. This source change uses the existing Salary terminology without claiming a visible label, label-click focus behavior or a complete dialog implementation.

The primary explanation was read; its example code was not copied or run. No exact spoken phrase, announcement timing, assistive-technology support matrix, full WCAG conformance, keyboard trap, focus return or complete modal accessibility is claimed. Existing English visible copy and the new English name remain unlocalized.

## Scope, ownership and attribution

A fresh bounded Commons query for PayD / EmployeeList / salary / label returned no entries in its top-ten scope. That is not an exhaustive ownership census. Root's retained custody contains no exact same-hunk completion or hold; that is likewise not global absence or a review gate.

Existing issue283 attribution and contributor boundaries from the earlier packet remain. PR581 was retained as OPEN/unmerged waterWang head `82ce1281b0a8f7a014d8835df237f7ccd34d00e1`; its complete retained eight-path map excludes EmployeeList. That is an earlier bounded observation, not a new PR status read. Test-titled PR588/589 and all held/protected families remain unexpanded. No contributor acceptance, assignment, sponsor approval, upstream authority or reward is inferred.

Original PayD contributors retain credit. The existing full Apache-2.0 LICENSE, blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`, 11357 bytes, remains in this packet directory unchanged. Existing patches and guides remain exact; this publication adds only this note and the incremental patch.

## Verification boundary

Verification consists of complete retained source/caller reading, primary naming semantics, independent UTF-8 Git blob identities, full serialized forward/reverse checks and preservation of every other source byte. Both new artifacts are read completely at the immutable publication ref and checked against prepared text and independent identities; final PR, path, tree and parent metadata are checked. A separately declared same-repository main equality can alias those immutable checks only when main equals merge and readback ref. Otherwise both complete artifacts are read at one observed immutable main.

No application render, DOM, browser, screen reader, salary edit, record, network request, database, wallet, account, payment, compiler, installation, fixture or test is executed. This source packet does not establish functional salary editing, issue completion, a complete build or upstream acceptance.
