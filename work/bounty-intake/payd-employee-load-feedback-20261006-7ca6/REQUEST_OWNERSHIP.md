# Keep EmployeeEntry load completions with the latest call

This incremental patch makes the existing employee-list loader use the latest started call as the owner of its result, visible failure flag and loading completion. It follows Commons #32117's failure-feedback patch. It does not start another request or alter the employee-creation handler.

Canonical source: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`, frontend/src/pages/EmployeeEntry.tsx. The exact preimage here is the composed #32117 postimage. The original source and actual App mount are already fully retained; this continuation does not reacquire them.

## Actual call sites and the race

The existing mount effect invokes fetchEmployees. The existing successful creation path also invokes that same callback after resetting its form state. In the normal list view the add-employee header control is outside the loading-versus-list branch, so that source does not impose a wait for the first load before opening the form.

These are two concrete call sites in the complete retained component. No creation or employee request was performed, and no timing incident is claimed. The finding is that the callback accepts concurrent calls without recording which call owns later writes.

Before this continuation, each fulfilled call maps and stores its result, clears the #32117 failure flag and clears loading in finally. Each rejected call sets the failure flag, logs and clears loading. An older completion can therefore overwrite a newer result or its feedback, or stop the spinner while the newer call is still pending.

## Latest-started-call ownership

A top-level useRef starts with null. Each invocation of fetchEmployees creates a distinct object and stores that object in the ref before entering the existing try block and starting the existing request. Objects are compared by identity; there is no numeric counter to wrap.

After the existing await, the callback returns immediately if its captured object is no longer current. That check precedes the existing synchronous response selection, row mapping, setEmployees and successful setLoadError(false). No new await is inserted into that admitted result path.

The catch still logs every caught error exactly as before. Its setLoadError(true) now runs only when the call's token is current. Finally likewise clears loading only for the current token. A return from the stale-success branch still reaches finally, whose own guard prevents it from clearing the newer call's loading state.

| Completion | Result and error state | Loading completion |
|---|---|---|
| Current call succeeds and maps normally | Existing mapped rows are stored; failure flag is cleared | Existing false update is allowed |
| Current call enters catch | Existing rows remain; failure flag is set; original log runs | Existing false update is allowed |
| Older call succeeds after a later call started | Returns before response mapping and state writes | No false update |
| Older call enters catch after a later call started | No failure-flag update; original log still runs | No false update |

This policy deliberately prefers the latest started call even if an older call later succeeds. If the newest call fails, the prior committed rows and the newest failure remain; an older success is not used as a fallback. The patch does not invent a server-order, data-version or successful-response freshness guarantee.

The [React useRef reference](https://react.dev/reference/react/useRef) describes a stable ref object across renders, mutable current storage, and updates that do not themselves render. The token is private per component instance and used from the existing asynchronous callback, not read to render JSX. This current primary reference establishes that general Hook contract; it is not an installed-version compilation or runtime result.

## Exact source composition

Apply show-load-error.patch from #32117 first, then own-latest-employee-load.patch. The older README remains a description of its own published source version; this guide records the distinct concurrent-call continuation.

| Source path | Preimage Git blob / UTF-8 bytes | Postimage Git blob / UTF-8 bytes |
|---|---|---|
| frontend/src/pages/EmployeeEntry.tsx | `02203749c30927c76dfa533e9a89dd84905cf75c` / 12023 | `ae7f8c1a596e4152180d8c215bc2cddb73bd2091` / 12311 |

The patch is 1865 UTF-8 bytes, Git blob `7f116aef37449900a987ec2bb5875ccfc5ebb7fa`. It adds seven lines and removes three across four hunks and thirty-seven complete serialized rows. Forward application reproduces the complete postimage; inverse application restores the complete preimage. Reversing only the five authored replacements leaves every other source byte equal.

The existing request expression, mapping expressions, callback dependencies, both call sites, form state and creation handler, wallet handling, autosave behavior, notifications and every JSX byte are unchanged. The #32117 alert text and position stay exact. Existing logging is deliberately retained outside completion ownership, so an obsolete rejection can still produce that original log.

The complete retained frontend/src/App.tsx body, `acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c` / 6460 bytes, imports and renders EmployeeEntry under its existing ErrorBoundary. That parent relationship was read from source. This continuation changes no route or boundary.

## Scope limits

This token coordinates calls within the current component instance. It is not invalidated by an unmount cleanup, does not abort a request and does not stop network or server work. A current call can still finish after removal. Cleanup ownership is a separate issue; neither the token nor its useRef declaration constitutes an unmount guarantee.

No request timeout, retry policy, cancellation signal or request-count change is introduced. The original setLoading(true) remains at the start of every invocation. The previous failure notice is not cleared at request start. Response validation, the non-array-to-empty fallback and exceptions from synchronous mapping remain the existing behavior.

No creation, account, employee, wallet, persistence, authorization or API-wrapper policy is changed or certified. The logging-only parent CSV import callback and all separately completed EmployeeList/CSV corrections remain untouched. No real response, employee record or account data was acquired.

The state-ownership reasoning assumes the existing synchronous mapping and setter sequence; it is not an atomic transaction across arbitrary user-defined callbacks or future awaits. No full component lifecycle, whole employee-management, runtime, compiler, test or accessibility guarantee is made.

## Attribution and custody

Original Protocol-Guild/PayD contributors retain credit. The complete original Apache-2.0 LICENSE already present in this directory remains unchanged: Git blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`, 11357 bytes. The #32117 patch and README also remain unchanged. This publication adds only the incremental patch and this guide.

A new dedicated Commons PR search for PayD, EmployeeEntry, request and latest returned no entries. Root retained no exact same-hunk request-ownership correction or hold. Those bounded observations are not a global absence proof or whole-issue ownership. The prior #32074 final PR-files metadata route stays UNKNOWN and held; unrelated intake bodies and failed routes remain protected.

A second agent reasoned from the stated contract without fetching source or executing anything. It found no concrete ordering concern with assigning the token before the request and guarding result, error and finally writes independently. That is description-only reasoning, not an independent runtime or source review.

## Validation and publication evidence

Checks are complete retained source reading, concrete mount and post-create call-site qualification, a successful primary React contract read, exact source identities, full serialized forward/inverse application, and every-other-byte preservation. No React component, API request, handler, log, employee or wallet operation, browser, fixture, test or compiler was run.

The two new Commons artifacts are checked as complete immutable texts with native and independently computed Git blob identities, exact changed paths, and final PR/tree/parent metadata. A separately observed main-equality alias is allowed only if main equals the verified merge and readback ref; otherwise both artifacts are read fully at one observed immutable main commit, without chasing later changes. These are artifact-publication checks, not upstream acceptance or deployment.
