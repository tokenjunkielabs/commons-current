# Associate the CSV filename with the committed preview

This incremental patch moves the existing setFileName(file.name) call into the latest-read onload handler, after parseCSV returns and before the existing preview writes. It changes no parser, acceptance rule, callback payload or data persistence.

## Source-backed problem

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`. The source path is frontend/src/components/CSVUploader.tsx, composed after the protected Commons #32009 drag-over, #32041 latest-read token and #32062 preview-status patches.

The existing handler accepts a file whose name ends in .csv, immediately calls setFileName(file.name), and then starts a FileReader. Its parsedData state and parent onDataParsed callback are updated only later from onload. The JSX displays File: with that filename above the row counts and preview derived from parsedData.

Consequently, after a previously parsed file, an admitted replacement can put its new name above the previous file's rows while the new read is pending. If no current onload reaches the parse/write sequence, those old rows can remain under the new name. This is a static event-order finding, not an executed upload or observed data incident.

## Resulting behavior

The patch removes the immediate filename setter and adds the same setter inside the existing guarded onload sequence:

1. Return if this reader's token is no longer current.
2. Obtain the content and call the unchanged synchronous parseCSV.
3. Set this file's name.
4. Set the same parsed rows and call onDataParsed with those rows.

The filename therefore represents the result accepted by that completion handler, rather than an uncompleted file selection. On first admission the filename panel is not newly shown until the handler reaches this setter. During a replacement read, the prior filename and preview remain displayed. No progress or pending-file label is added.

A successful file read is not the same as valid rows: parseCSV may return an empty array after its existing missing-header alert or for too little input. If it returns normally, including an empty array or rows with validation errors, the filename still advances with that returned result. If parsing throws, the moved setter is not reached. There is no new catch, validator behavior or valid-row filter.

The same latest-read token now also gates this filename write. Rejected extensions and a cancelled picker retain their existing policy: they do not admit a new read or reset the token. The patch adds no abort, onerror, onabort, unmount guard, parser scheduling, timeout or asynchronous callback support.

The [MDN FileReader error-event reference](https://developer.mozilla.org/en-US/docs/Web/API/FileReader/error_event) identifies the read-failure event. This component still installs only its existing onload handler; the patch does not report or recover from read errors. The page's example was not executed.

## Actual parent relationship

The complete retained EmployeeList.tsx mounts CSVUploader when showCSVUploader is true. It passes handleDataParsed, which maps every received row into its local csvData. Its Add Employees from CSV button is disabled only when that array is empty and loops over it when activated. No isValid filtering is added by this patch.

The complete retained EmployeeEntry.tsx supplies the mounted EmployeeList onAddEmployee callback that logs each item. This is not a persisted import implementation. No parent operation, callback, file, log, employee/account action or request was invoked while producing this artifact.

This correction does not clear previous parent rows on a newly selected file and does not disable their existing import control while a replacement is pending. It instead keeps the visible filename associated with the previous completed preview until the next accepted completion. It does not promise atomicity with arbitrary external callback work or recovery if onDataParsed throws.

## Exact composition and identities

All earlier source corrections and their Commons artifacts remain unchanged. This patch must follow the stated preimage; it is not a replacement for the original contributor implementation.

| Source state | Git blob | UTF-8 bytes |
|---|---|---:|
| Current composed preimage after #32009/#32041/#32062 | `c3e7ef2b49d275cab07762ce9896ae1264fdd36f` | 8039 |
| Proposed postimage | `93f7ff9f7efed569bede593022ee869be8516471` | 8041 |

The only source edit is the one moved setter with its new indentation: +1/-1 across two hunks and fourteen complete serialized rows. The complete 631-byte patch applies forward to the exact postimage and inversely to the exact preimage. Removing the old/new setter lines leaves every other byte equal. The token check, parsing, setParsedData, onDataParsed, drag-over and status text are exact.

| Retained supporting file | Git blob | UTF-8 bytes | Role |
|---|---|---:|---|
| frontend/src/pages/EmployeeEntry.tsx | `b89a5c832191a19a52c4f7b99201da5ece9acef8` | 11774 | Actual mounted parent callback |
| frontend/src/App.tsx | `acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c` | 6460 | Actual EmployeeEntry route |
| frontend/src/components/EmployeeList.tsx, canonical | `277684e5f87cabd72ff5aadd04299a5360fdf3e0` | 20441 | Original CSV mapping/render connection |

The supporting complete bodies were retained, not reacquired for this continuation. EmployeeList's later sort/dialog corrections are separate; their composed source preserves the relevant CSV callback and control regions. No old patch calculation or old application behavior was replayed.

## Task custody and attribution

This is a distinct source continuation of the PayD194 CSV upload-control lane. The newly issued dedicated Commons PR query for PayD, CSVUploader and filename returned the already completed #32041 token packet. Its retained scope explicitly left filename policy unchanged. That result is related ownership evidence, not a global absence certification or permission to repeat the old token patch.

Original Protocol-Guild/PayD contributors retain credit. Existing allow-drag-over.patch, latest-read-completion.patch, text-preview-status.patch and their guides remain exact. The original complete Apache-2.0 LICENSE remains at the packet prefix, Git blob261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64 /11357 bytes. No duplicate notice or upstream edit is introduced.

The earlier #32074 reference describes the earlier versioned source and retains its exact unresolved final PR-files metadata read. This new source patch does not silently rewrite that reference, repeat its failed route, or clear its limitation. Other exact holds remain unchanged.

## Validation and publication limits

Validation is retained source reading, the concrete child/parent relationship, full-text identities, primary failure-event semantics, and serialized forward/inverse plus every-other-byte checks. CI supplied a nongating retained-description ordering check only; it did not inspect sources or execute the UI.

No FileReader, parser, React component, event, file, browser, upload, callback, log, test, fixture or compiler was executed. No runtime, full CSV-format, import persistence, validation, accessibility or whole194 acceptance claim is made.

Publication adds only the new incremental patch and this guide to the existing Commons packet. Complete immutable artifact texts/native and independent hashes, merged PR/exact paths/tree/parents and a separate fresh main observation are checked. A predeclared equality alias is used only if main equals verified merge/readback ref; otherwise both artifacts are read completely at one observed immutable main commit, without a moving-branch chase.
