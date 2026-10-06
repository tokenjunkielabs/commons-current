# Show EmployeeEntry load failures in the list view

This patch gives the existing employee-loading catch path visible feedback. It adds one local boolean, sets it when that catch runs, clears it after a successful mapped result, and conditionally renders a generic alert paragraph in the existing list view. It adds no request or employee operation.

Canonical source: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`, frontend/src/pages/EmployeeEntry.tsx. A fresh main-reference guard matched that donor. The complete source body was already retained from the mounted CSV/parent qualification and is reused without reacquisition.

## Concrete source behavior

The supplied fetchEmployees callback sets loading, awaits its existing api.get call, selects and maps the returned employee rows, and sets employees. Its catch currently logs the failure and does not set any user-visible error state. Its finally clears loading.

The normal list view selects a spinner while loading and otherwise renders EmployeeList with the current employees array. Since that array begins empty, a first load that enters the catch can return to a normal empty-list presentation without explaining that the load failed. A later failed refresh can keep prior rows without a failure message.

This is a static path finding. No employee request was sent, no response or account data was acquired, and no live failure or empty-data incident is claimed. The correction applies whenever the existing catch runs, including failures during mapping; it does not assert that every server or network failure reaches this catch through the unacquired API wrapper.

## Resulting feedback and recovery

loadError begins false. The existing catch sets it true before the unchanged console.error statement. A successful mapped result sets employees exactly as before and then clears loadError. The existing finally still clears loading.

When the existing list view renders with loadError true, it includes a paragraph reading “Unable to load employees.” with role=alert. The paragraph contains no error object, response detail or employee identifier. The existing list and its data are preserved.

A successful empty mapped result clears the error just like any other successful result; the patch does not redefine schema validation or the existing non-array-to-empty fallback. It does not clear prior rows on failure. A later request does not automatically clear the previous failure at its start; the notice remains until a successful result reaches the new clearing statement or this component instance is removed.

The separate add-employee form return branch is unchanged. The new notice belongs to the normal list view, so it is not promised to appear while that form branch is being displayed. No retry button or new refresh request is introduced.

The [W3C Alert Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/alert/) supports a brief important notice that does not move keyboard focus. This patch adds the role without focus code or an automatic dismissal timer. It makes no screen-reader announcement, color contrast, translation or complete accessibility claim. The copy is English, consistent with other literal UI copy in the retained component; broader localization is separate.

## Exact source preservation

| Source path | Original Git blob / UTF-8 bytes | Proposed Git blob / UTF-8 bytes |
|---|---|---|
| frontend/src/pages/EmployeeEntry.tsx | `b89a5c832191a19a52c4f7b99201da5ece9acef8` / 11774 | `02203749c30927c76dfa533e9a89dd84905cf75c` / 12023 |

The complete 1187-byte patch is Git blob `a8aca114c1de428bacbf04f5b69103f274d8a5af`. It adds nine lines, removes none, and has three hunks with twenty-eight complete serialized rows. Forward application reproduces the exact postimage and inverse application reproduces the exact preimage. Removing the new state declaration, two setters and feedback block leaves every original byte equal.

The api call, mapping expressions, callback dependencies, loading state and finally, existing error log, effect that starts fetching, draft restoration, form fields, creation handler, wallet handling and notifications are unchanged. No existing handler was executed. EmployeeList props and its logging-only CSV import callback remain exact, as do all separately published child CSV, sort and dialog corrections.

The complete retained frontend/src/App.tsx body, `acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c` / 6460 bytes, imports EmployeeEntry and renders it under the existing ErrorBoundary. This establishes the actual mounted parent relationship from source. The patch does not change the boundary, its reset behavior or any route.

## Deliberate limits

No request cancellation, latest-request identity or unmount guard is added. Concurrent completions still use the existing arrival order for employees/loading, and the new error boolean follows those completion paths. This is visible failure feedback with success recovery, not a correction of all fetch-lifetime or concurrency behavior.

No API wrapper, endpoint, response schema, authorization, account, payroll or persistence policy is changed or certified. Existing row fields and the creation/wallet-related source remain untouched. The message does not expose the caught error or change existing logging behavior.

No demo-data notice is added. Inspection of the actual source shows that this page starts with an empty employee array and loads through api; a logging-only CSV callback is not evidence that the displayed employee data is fabricated.

## Attribution and task custody

Original Protocol-Guild/PayD contributors retain credit. The complete original Apache-2.0 LICENSE is preserved byte-for-byte in this packet: Git blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`, 11357 UTF-8 bytes, independently matched against the complete retained canonical tree.

A new dedicated Commons PR query for PayD, EmployeeEntry and load error returned the known #31971 Avatar fallback packet. That different source path remains protected. Root retained no exact prior EmployeeEntry load-error display correction. These are bounded custody observations, not a global absence claim, contributor reassignment or whole-issue completion.

Earlier reference documents remain versioned to their original source identities. The exact #32074 final PR-files metadata route remains UNKNOWN and held. Separate privately screened intake bodies, including the unrelated hook-test/pagination carriers, are not expanded or cleared by this source correction.

## Validation and publication

Validation is complete retained source reading, the actual App-to-EmployeeEntry mount, the concrete catch/finally/list branch, exact text identities and serialized forward/inverse plus every-original-byte checks. The W3C alert pattern was read as a primary contract; its example was not executed.

No React component, request, file, account, employee, wallet, callback, log, browser, fixture, test or compiler was run. There is no runtime, upstream, whole-build, full accessibility or complete employee-management acceptance claim.

Publication adds only show-load-error.patch, this guide and the unchanged complete LICENSE to a new Commons directory. All three full immutable texts, native and independent blob identities, exact paths and final PR/tree/parent metadata are checked. A predeclared main-equality alias is used only when a separate observed main equals the verified merge/readback ref; otherwise all three artifacts are read fully at one observed immutable main commit without chasing later changes.
