# EmployeeList reference

This reference describes the acquired PayD EmployeeList component and its actual EmployeeEntry caller. It separates the canonical source from the already-published Commons accessibility patches. It is a source reference; none of the displayed or described actions were run.

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`, `frontend/src/components/EmployeeList.tsx`.

## Public shape

The component is a named export. Its local Employee interface declares the following fields:

| Field | Declared type | Required |
|---|---|---|
| id | string | yes |
| name | string | yes |
| email | string | yes |
| position | string | yes |
| imageUrl | string | no |
| wallet | string | no |
| salary | number | no |
| status | 'Active' or 'Inactive' | no |

The source does not export that interface. A consumer must provide a structurally compatible value through its own types; this reference adds no public type export or runtime validator.

| Prop | Declared contract | Actual use in this component |
|---|---|---|
| employees | Employee[]; required | Supplies the sorted desktop rows and mobile cards. |
| onAddEmployee | (employee: Employee) => void; required | Called for each staged CSV row by the import action; also referenced by the declared Add modal handler. |
| onEmployeeClick | (employee: Employee) => void; optional | Declared but not destructured or invoked; no row-click callback is implemented. |
| onEditEmployee | (employee: Employee) => void; optional | Enables an additional inline salary button and is guarded inside the Edit Salary submit handler. |
| onRemoveEmployee | (id: string) => void; optional | Guarded inside the removal-confirmation handler. |

The optional callbacks are not promises in the declared interface and the component does not await callback completion. It introduces no error recovery, pending state or persistence guarantee for a callback implementation.

## Actual mounted caller

App's /employee route renders EmployeeEntry. Its list branch renders EmployeeList with employees, a logging onEmployeeClick prop, and a logging onAddEmployee prop. It does not pass onEditEmployee or onRemoveEmployee.

The effects of that exact invocation are limited:

- The supplied click callback is unused by EmployeeList.
- CSV import invokes the supplied logging callback for each staged item, then clears the local staging state. It does not persist those additions through that callback.
- The desktop/mobile pencil controls still open Edit Salary because their handlers are unconditional. Save has no supplied edit callback to invoke, then closes the panel.
- The desktop/mobile Remove controls still open Confirm Removal. Confirmation has no supplied removal callback to invoke, then closes the panel.

EmployeeEntry's separate employee-entry form and its own submit path are not the EmployeeList callbacks. Their business behavior is outside this reference. This distinction is based on the literal mounted invocation, not an observed record or an account operation.

## Sorting and responsive display

The initial sort key is name, ascending. Choosing the same key flips direction; choosing a different key selects it and restores ascending order. The five offered keys are name, position, wallet, salary and status. The source copies the incoming array before sorting. It reads the original employee objects rather than making replacement records.

For a selected key, a nullish value becomes an empty string. When both compared values are numbers, the comparator subtracts in the selected direction. Otherwise it converts both to strings and calls localeCompare in that direction. This is the actual mixed-value policy, not a claim of a globally normalized order, a fixed collation locale or complete validation of caller data. No comparator or collation was evaluated while preparing this reference.

The desktop branch uses a table inside hidden/md:block classes. The mobile branch uses md:hidden cards. Both render the same sortedEmployees array and have their own empty-state markup. CSS classes establish the intended responsive split; no viewport or computed style was observed.

Desktop shows Name, Role, Wallet, Salary, Status and Actions. Mobile shows the identity/position header and status, then wallet and salary with Edit/Remove controls. Avatar receives email, name, optional imageUrl and size="sm" in both branches. Its existing reference and fallback patch remain separate.

The wallet helper returns an empty string for a falsy wallet; otherwise it uses the literal first-four/ellipsis/last-four expression. It performs no account lookup. Salary uses nullish fallback zero. Status uses the source's Active-versus-other class branch and a visible fallback dash. Those expressions are documented without evaluating an employee record or altering their policies.

## CSV staging and local lifetime

Import from CSV shows the child CSVUploader. EmployeeList supplies requiredColumns in this exact order: name, email, wallet, position, salary, status.

The callback maps every returned CSVRow into the local Employee shape. It does not filter by row.isValid. It maps fields from row.data, uses the literal Number(salary) || 0 expression, defaults a falsy status to Active through a type assertion, and generates an ID with the existing Date.now/Math.random expression. A TypeScript assertion does not add a runtime status check. These are source descriptions; no conversion, ID generation, random value, parser or file read was performed.

Add Employees from CSV is disabled only when the staged array is empty. Otherwise the handler calls onAddEmployee for each staged item, then clears the array and hides the uploader. If a callback throws, the source has no surrounding catch/finally to guarantee those later statements. Cancel hides the uploader and clears the staged array. These component actions do not prove that the parent persisted any item.

The CSV_UPLOADER.md reference covers the child parser, preview and file-attempt boundaries; this document adds the parent's staging/dispatch contract. The separate #32009 drag-over, #32041 latest-read identity and #32062 text-status corrections remain preserved, with no additional parsing or validation change.

## Existing panels and versioned accessibility

The source declares Add, Edit Salary and Confirm Removal panels. Add has a false initial state and no established setShowAddModal(true) call in the acquired module. EmployeeEntry's separate Add Employee button switches its own page branch, not this local state. This reference does not describe the declared Add modal as a mounted opening path.

Edit Salary stores an employee and a local numeric value; both unconditional pencil actions seed those values and open it. Its optional inline salary button exists only when onEditEmployee is supplied. Cancel closes it. Save conditionally invokes the edit callback, then closes it. Confirm Removal stores an ID; confirmation conditionally invokes the removal callback, then closes it. No callback, conversion, open/close action or record mutation was exercised.

The canonical source and saved correction chain must not be confused:

| Version | Scoped change already published |
|---|---|
| Canonical donor | Sorting uses clickable headers; Salary input and the two reachable generic panel containers lack the later associations. |
| #32014 | Native buttons carry the five sort actions. |
| #32038 | Only the active table header exposes aria-sort from the same key/direction. |
| #32060 | Edit Salary number input receives its name. |
| #32079 | Inner Edit Salary role=dialog panel is named by its existing heading using useId. |
| #32083 | Inner Confirm Removal role=dialog panel is named and described by its existing heading/question using useId. |

The fully composed saved source is ab27936bf8f424751fd38af5fff45952c50a12d3, 22213 UTF-8 bytes. The original donor remains 277684e5f87cabd72ff5aadd04299a5360fdf3e0, 20441 bytes. These patches do not implement aria-modal, outside-interaction prevention, focus entry/return/trapping or Escape behavior. They are not a whole-component accessibility acceptance or a runtime observation.

## What this reference establishes

The module's declared props, literal callback/control flow, comparator and display expressions, the actual caller and the saved source versions are supported by complete retained source identities. It does not establish employee persistence, route authorization, account state, successful parsing/import, action completion, callback ordering across external asynchronous work, runtime styling, hydration, a compiled build or a full accessibility result.

Original Protocol-Guild/PayD contributors retain attribution. The unchanged Apache-2.0 LICENSE in this reference directory applies as recorded in EMPLOYEE_LIST_SOURCE.md. No complete upstream component or caller is republished.
