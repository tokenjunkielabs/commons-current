# Acknowledge comparison-link copying after the write succeeds

## Actual mounted path

The corridor comparison App Router page renders ComparisonContent inside its existing layout and Suspense boundary. Its Share button calls handleShare and displays Copied! when the local copied state is true.

The original handler obtains window.location.href, calls navigator.clipboard.writeText(url), immediately sets copied to true, and schedules the existing two-second reset. It neither awaits nor catches the returned promise. A rejected clipboard write can therefore leave a success message for an operation that did not complete and an unhandled promise rejection.

This is a source-level promise-handling failure. No user clipboard was accessed and no denied write or browser incident was reproduced.

## Complete source

Donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Source | Native and independent Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/app/[locale]/corridors/compare/page.tsx | 4b16f9f7680222ff0230d8e50ae6c2b38c4a10e6 | 11814 |

The complete page body is retained and independently matches its native identity. It includes the event handler, Share button, copied-state display and the actual default App Router export, so no hypothetical caller is required. The logger import is already present and the existing fetch catch uses the same two-argument error-logging form.

Current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888. Relocation does not establish sole authorship. Original attribution and all three complete acquired MIT notices are preserved.

## Promise contract and minimal correction

The [Clipboard.writeText documentation](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard/writeText) specifies a promise that resolves after clipboard contents have been updated and documents rejection when writing is not allowed. The operation is subject to browser security requirements; a click handler cannot guarantee permission or availability.

The patch makes the existing handler async and awaits that same write inside try/catch. Only after fulfillment does it set copied to true and start the unchanged two-second reset. The catch sets copied to false and logs a bounded failure message with the existing logger.

| Outcome of the single attempted write | Handler behavior |
| --- | --- |
| Promise fulfills | Show existing Copied! state and schedule the same two-second reset |
| Promise rejects | Clear copied state and log the failure |
| Synchronous access/call failure inside try | Use the same catch path |

The same current URL is captured once and passed to the same API. No clipboard read, retry, fallback copy mechanism, permission request, new dependency or extra network request is introduced. The literal URL is not added to the log message.

This table records source control flow, not executed browser cases. Multiple overlapping share attempts, old timer overlap, unmount cancellation and a dedicated error announcement are outside this correction. The old timer mechanism is retained; there is no request-serialization or all-errors guarantee.

## Serialized patch checks

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Complete preimage | 4b16f9f7680222ff0230d8e50ae6c2b38c4a10e6 | 11814 |
| Complete postimage | 62d653b5b125e244a8354191f40dd0e97826efdf | 11951 |
| await-copy-acknowledgement.patch | cf2c86f24339fbb97f2cc4d022e4d1f874be8e29 | 771 |

The actual unified patch has one hunk and twenty rows, with nine additions and four deletions. Serialized forward application exactly reconstructs the postimage; inverse application exactly restores the preimage. Restoring the original handler restores every other page byte.

Selected corridor state, URL navigation, backend/mock loading, CSV export, charts, comparison table, recommendations, add dialog, Share button label/icon and styling remain unchanged. The separate corridor-detail #32004 score patch affects another route.

Apply await-copy-acknowledgement.patch at the donor repository root to the exact page preimage. No handler, promise, clipboard, timer, logger, browser, compiler, fixture, tests or workflow was executed. Source checks establish promise sequencing and serialization, not actual browser permission, runtime rendering or whole-build success.

## Notices and publication boundary

| Unchanged notice | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| upstream-licence-mclaughlin.md | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| upstream-license-menke-laguna.md | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| upstream-license-de-wet.md | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |

Bounded exact-route/clipboard Commons and Slack queries returned zero results, with native END for Slack. Internal custody retained no same-handler completion or hold. These bounded observations are not global absence, ownership or acceptance clearance.

This is an attributed Commons source proposal, with no upstream mutation or deployment. Publication verification requires all five complete immutable artifact bodies with native plus independent identities, followed by exact PR/files/merge/main metadata. An exact observed main-equals-merge identity may reuse those bodies; otherwise every artifact is read once at the observed immutable main commit. The actual publication result belongs in its separate release and grouped index.

## Continuation: explicit names for three comparison controls

The sections above document the initial #32007 clipboard packet. This continuation consumes its retained source postimage and leaves that handler correction intact.

The same complete mounted page contains an icon-only Back link, an icon-only remove button for each selected corridor and a text input identified visually through its corridor-ID placeholder. The new patch supplies an explicit accessible name to each selected control without changing its destination, behavior or visual layout.

| Existing control | Added accessible name |
| --- | --- |
| Header Back link | Back to corridors |
| Selected corridor remove button | Remove followed by the current corridor ID and from comparison |
| Add-dialog text input | Corridor ID |

The remove label uses the same id already passed to handleRemoveCorridor, making each repeated button distinguishable. The existing input placeholder and its example remain intact. The existing English copy is retained; this is not a translation or visible-label redesign.

[W3C technique ARIA14](https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA14) documents aria-label for naming controls whose purpose is conveyed visually without clear visible label text, including symbol buttons and native inputs. This supports the explicit names here; the technique is not a complete accessibility assessment.

| Continuation item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Source after #32007, before names | 62d653b5b125e244a8354191f40dd0e97826efdf | 11951 |
| Source after control names | 5ad3af8111e8782eb1df3bb70b0e4620bcfee3b3 | 12093 |
| name-comparison-controls.patch | f725531a7021cb724a86237df6e529571c3d8476 | 1356 |

The actual incremental patch has three hunks and twenty-one rows, with three additions and no deletions. Serialized forward and inverse text application matched the complete source identities. Removing the three added attributes restores every other byte, including the accepted clipboard handler.

Apply the original await-copy-acknowledgement.patch first, then name-comparison-controls.patch. No event handler, navigation, clipboard, browser, assistive technology, compiler, fixture, tests or workflow was executed. The dialog's role, focus behavior, keyboard handling, announcements and full WCAG conformance are not claimed.

The current continuation publishes only this new patch and an exact-preimage-guarded update to this guide. The original clipboard patch and three MIT notices remain unchanged; their earlier publication checks are inherited without replay. Both newly written complete immutable bodies and final PR/files/merge/main identities must match. Main reuse still requires exact commit equality; otherwise each changed artifact is read once at the observed immutable main pin. Bounded route/label overlap queries returned zero rows with native Slack END, without any global-absence claim.

## Continuation: release comparison download resources on exceptional exits

The sections above document #32007 and #32012. This third incremental patch consumes their retained complete source postimage and preserves both corrections.

The same mounted page's Export CSV button invokes handleExportCSV. After assembling the existing CSV, that handler creates a Blob, acquires an object URL, creates/configures an anchor, appends it, clicks it, removes it and revokes the URL. In the original straight-line sequence, an exception between acquisition and either cleanup statement skips that cleanup. This is a control-flow gap in the acquired source; no download failure was reproduced.

The patch places an outer try/finally immediately after successful URL acquisition. It places an inner try/finally immediately after successful anchor creation. The inner cleanup calls a.remove(); the outer cleanup reaches the same existing URL.revokeObjectURL(url) operation.

| Source path | Cleanup reached |
| --- | --- |
| Anchor creation throws after URL acquisition | Outer URL revocation |
| Anchor configuration, append or click throws after anchor creation | Anchor removal, then URL revocation |
| Anchor removal itself throws | Outer URL revocation is still reached |
| All existing operations return normally | Anchor removal, then URL revocation at the same immediate post-click point |

These are source-level control-flow cases, not executed test cases. If Blob construction or URL acquisition throws, no acquired URL is available for this cleanup. If anchor creation throws, no returned anchor is available to remove. The patch adds no catch, retry, error swallowing or download-success announcement. A cleanup exception can replace an earlier exception; preservation of exception precedence is not claimed.

[MDN's Element.remove reference](https://developer.mozilla.org/en-US/docs/Web/API/Element/remove) states that removal uses the element's parent and is a no-op when it has no parent. This supports using the same cleanup for an anchor whose append did not complete or which was already detached. The existing immediate revocation timing is retained; this patch does not establish browser download completion, delayed revocation compatibility or successful file saving.

| Cleanup continuation item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Source after #32012, before cleanup | 5ad3af8111e8782eb1df3bb70b0e4620bcfee3b3 | 12093 |
| Source after cleanup | 576f30a3df21a9f9856e192c38e403f81c8d1d20 | 12169 |
| download-resource-cleanup.patch | 815cd0930ba1afba7c9725174d90ba6bd388b945 | 1015 |

The actual incremental patch has 1 hunk and 26 rows, with 13 additions and 7 deletions. Complete serialized forward application reconstructs the postimage and inverse application restores the preimage. Replacing only the cleanup block restores every other page byte. CSV headers, row selection, numeric formatting, separators, Blob type, filename and date expression remain exact. The copied-state correction, control names, navigation, data loading and other handlers also remain exact.

Apply await-copy-acknowledgement.patch, then name-comparison-controls.patch, then download-resource-cleanup.patch at the donor root. No application handler, Blob, object URL, anchor, DOM, click, Date expression, clipboard, browser, compiler, fixture, test or workflow was executed.

The bounded route/cleanup overlap query returned only the existing Commons #31453 grouped index header, which was disposed using retained completion maps rather than rereading its issue body or comments. Those maps record #32007 clipboard and #32012 names on this page, plus separate download cleanup paths. The paired Slack query returned zero rows with native END. These observations are bounded custody evidence, not a global absence, ownership or upstream acceptance claim.

The current publication contains only download-resource-cleanup.patch and this exact-preimage-guarded guide update. The two preceding patches and three original MIT notices are unchanged and their accepted checks are inherited without replay. Both newly written complete immutable bodies require native and independent identity matches, followed by exact PR/files/merge/main metadata. Exact observed main-equals-merge equality permits reuse of those bodies; otherwise both changed artifacts are read once at the observed immutable main commit. The separate release and grouped index hold the resulting publication identities.
