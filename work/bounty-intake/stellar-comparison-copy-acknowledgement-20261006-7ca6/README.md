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
