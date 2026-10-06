# CSVUploader: suppress superseded read completions

The mounted CSV uploader starts an independent FileReader for each accepted selection. Its original load handler always parses the returned text, updates the local preview and calls the parent onDataParsed callback. If an earlier read completes after a later selection has created another reader, the old completion can replace that newer selection's result.

This incremental patch after Commons #32009 gives each admitted reader a plain object token. The component remembers the latest token in a ref. The first statement of each load handler compares its closed-over token to that ref and returns for a superseded attempt. It is completion suppression; it does not abort a read.

## Source and exact composition

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`.
Production path: `frontend/src/components/CSVUploader.tsx`.

| Stage | Git blob | UTF-8 bytes |
|---|---|---:|
| Original canonical file | 26b62ac2f50ae4d48d7ce4a416b7841f8a2e742f | 7645 |
| After #32009 drag-over correction | 0d4d54488a8e38eea15aa0656af7f95601c5efdb | 7692 |
| This incremental postimage | 81d91b45eb0ecc0bf51b298340cbd258534a081b | 7880 |

Apply allow-drag-over.patch from #32009 before latest-read-completion.patch. The retained full canonical text and acknowledged prior patch were assembled without source re-fetch or application execution. The complete resulting preimage matches #32009's declared postimage. Its drag-over handler remains exact.

The new patch adds 4 lines and removes 0, in 2 complete hunks/18 rows. Whole serialized forward and reverse application match the complete postimage and preimage. Removing exactly the new declaration, token assignment and guard restores every prior byte.

## Connected producer and consumer

The retained canonical App /employee route renders EmployeeEntry, which renders EmployeeList. EmployeeList's existing control mounts CSVUploader when showCSVUploader is true and passes handleDataParsed as onDataParsed.

CSVUploader's file-picker and drop handlers both select the first supplied file and call handleFileParse. The existing case-sensitive .csv extension check is the admission boundary. After that check, the function sets the displayed filename, creates a reader and starts readAsText. There is no disabled/loading control that prevents a second selection while the first read is pending.

The successful handler calls synchronous parseCSV, setParsedData and the parent callback. That parent maps supplied rows into its local csvData preview; its later add action iterates the preview through onAddEmployee. The observed EmployeeEntry callback logs its argument, so no persisted import or backend mutation is asserted. None of those callbacks, records or files was executed or accessed.

The older-read ordering is an inference from these independent asynchronous readers and unconditional completion handlers, not a captured production incident.

## Token boundary and preserved behavior

The new latestReadTokenRef is declared unconditionally alongside the existing refs. For each admitted file, a new empty object is created immediately after the existing FileReader constructor; the ref is assigned before onload installation and readAsText. Object identity separates attempts without using filenames, timestamps or file contents.

The guard runs before reading the event result, calling parseCSV, updating parsedData or invoking onDataParsed. Once another attempt has assigned its token, an older handler returns without those effects. The current handler follows the exact prior sequence. The ref holds only the small identity token, not the FileReader or its completed text result.

The following limits are intentional:

- A cancelled file picker or a rejected extension never reaches token assignment, so the previously admitted reader remains current.
- The old preview is not cleared when a new filename is selected; the existing pending-display policy remains.
- If the latest reader fails or aborts, no new fallback, error message or retry is added. Earlier superseded completions remain ignored.
- A readAsText throw occurs after token assignment and can supersede the previous token; constructor failure occurs before assignment. Existing exception handling is unchanged.
- No unmount cleanup or cancellation is added. The latest attempt can still reach the existing parent callback after the component is removed.
- The check assumes the existing parse/callback sequence remains synchronous. It does not guard future awaited stages, callback exceptions, or changes to validators/requiredColumns/callback props during a pending read.
- File parsing, quoting, column validation, size/type policy, input resetting, filename text, preview markup and employee-add behavior are unchanged.

This is not a whole upload/import lifecycle correction.

## Primary API support

The [MDN FileReader interface](https://developer.mozilla.org/en-US/docs/Web/API/FileReader) describes asynchronous reading from selected File/Blob objects and a distinct reader object returned by its constructor. The [readAsText reference](https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsText) describes obtaining text on read completion. The [load-event reference](https://developer.mozilla.org/en-US/docs/Web/API/FileReader/load_event) identifies load as the successful-read event. These explain the existing API boundary; they do not supply an observed ordering experiment or application-specific guarantee.

Only those contracts were used. No documentation example, synthetic file, FileReader, CSV parser or event was executed.

## Task, ownership and attribution

This is a narrow source continuation within the already-qualified warm issue194 uploader family. The dated bounded PR194 search returned no entries, and the complete observed issue comment was shobhamerabacha-star's assignment request. Neither establishes exhaustive ownership absence or maintainer acceptance. No new broad search or contributor takeover was performed.

The retained latest path-history attribution is commit 4f5dd01b31a0b7445e50408398b6fbe9b52d8f48, author name Mainnet-ops; it is not an original-author census. Protocol-Guild/PayD's contributors retain credit. The original #32009 guide and full Apache-2.0 LICENSE remain unchanged; license blob 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64 is 11357 bytes. This follow-up adds only a patch and this guide.

All exact held queries and protected related families remain held. The parent seat's lack of a retained exact token-guard completion is bounded custody, not global clearance.

## Verification limits

The completed checks are whole-source byte composition, exact forward/reverse serialized patch application and preservation of all other source bytes. Publication separately checks both complete immutable artifact strings against prepared text, native blobs and independent identities, then checks PR/paths/tree/parents. A separately preselected fresh main-equality alias is used only when it equals the verified merge/readback ref; otherwise both full artifacts are read at one observed immutable main.

No browser, filesystem file, upload, drag/drop/picker event, FileReader, CSV parsing, employee/account data, callback, compiler, test, fixture or upstream operation was executed. There is no persisted-import, full-feature, full-build, accessibility, contributor-acceptance or economic claim.
