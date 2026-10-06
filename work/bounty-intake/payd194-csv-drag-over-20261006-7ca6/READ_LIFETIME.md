# Ignore CSV read completions after uploader cleanup

This incremental patch invalidates CSVUploader's existing latest-read token when its effect is cleaned up. The already present onload guard then returns before content access, parsing, local preview writes or the parent callback when an old completion reaches that guard after cleanup.

The correction owns only that completion boundary. It does not abort FileReader, add error handling, interrupt a callback already running or promise cancellation at the instant a button is clicked.

## Actual connected source and failure order

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`. The complete retained frontend/src/components/CSVUploader.tsx is composed after #32009 drag-over, #32041 latest admitted-read token, #32062 textual preview status and #32105 filename/preview association.

The retained EmployeeList mounts CSVUploader only inside its showCSVUploader condition. Its Cancel handler sets that condition false and clears csvData. The parent's handleDataParsed callback maps received rows into csvData. Before this correction, a pending reader still holds the current token after the child is removed; a later onload can pass its existing token guard and call that retained parent callback.

Consequently, a completion after the component's lifetime can repopulate parent CSV data after the explicit cancellation path cleared it. This is a static ownership finding from the complete child/parent source, not an executed file read, observed incident or persisted import.

The same source contains other removal paths. This patch does not redefine them, and it does not infer a persisted employee operation: the actual mounted EmployeeEntry onAddEmployee callback logs only. No upload, account, employee, callback or logging operation was performed while producing this packet.

## Exact change

The patch adds useEffect to the existing React import and installs one unconditional effect after the existing refs:

```tsx
useEffect(() => {
  return () => {
    latestReadTokenRef.current = null;
  };
}, []);
```

The setup creates no reader and changes no state. Cleanup clears only the existing token ref. Each admitted read still installs its own fresh object token before readAsText. Its existing first onload statement compares that captured object with latestReadTokenRef.current and returns on mismatch.

After cleanup, null cannot equal an admitted read's object token. Such a completion therefore returns before parseCSV, filename/preview writes and onDataParsed. A later component instance owns a separate ref. Mounted picker cancellation, rejected extensions and the latest-admitted-read policy remain unchanged.

The [React useEffect reference](https://react.dev/reference/react/useEffect) documents cleanup after component removal. That contract was transferred from CI's earlier successful primary-source qualification; no new page retrieval or reconstructed quotation is claimed here. The full passage's local locator was not retained in that transfer. The concrete after-cleanup result follows from the unchanged token comparison and the new null assignment in the supplied source.

## Timing and behavior limits

This is an after-cleanup guard. It does not promise to prevent a callback between the Cancel click and effect cleanup, or to interrupt a callback that has already passed its guard. The parser and callback remain synchronous in the supplied flow; arbitrary future asynchronous parsing or callback internals are outside this claim.

FileReader continues its underlying work. No abort call, event-handler detachment, onerror/onabort handler, unmount notification, resource cancellation, timer or pending-state display is added. The existing failure behavior and read-result conversion remain exact.

While the component stays mounted, admitted replacements still use #32041's token policy. #32105 still keeps the previous filename and preview together until the current read's parser returns; empty or invalid-row results retain existing behavior. This patch adds no row validation/filtering, parent data policy or import persistence. Existing callbacks can still throw, and no catch is added.

## Exact identities and composition

| Source state | Git blob | UTF-8 bytes |
|---|---|---:|
| Composed preimage after #32105 | `93f7ff9f7efed569bede593022ee869be8516471` | 8041 |
| Proposed postimage | `a016932912ae0dc5022d9f2871c0949415f0f56d` | 8150 |

The source patch is +7/-1 across two hunks and seventeen complete serialized rows. The complete 815-byte patch has Git blob `425c3576d2339612765678d66a86fd42007a518a`. Forward application produces the exact postimage; inverse application reproduces the exact preimage. Removing the new effect and restoring the original import leaves every other source byte equal.

The existing latest-token check, read admission, parser, setParsedData, onDataParsed, filename commit, drag-over handling and preview-status markup are unchanged. No prior patch calculation or application behavior is replayed.

| Retained connected source | Git blob | UTF-8 bytes |
|---|---|---:|
| frontend/src/components/EmployeeList.tsx after #32083 | `ab27936bf8f424751fd38af5fff45952c50a12d3` | 22213 |
| frontend/src/pages/EmployeeEntry.tsx | `b89a5c832191a19a52c4f7b99201da5ece9acef8` | 11774 |
| frontend/src/App.tsx | `acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c` | 6460 |

These complete bodies were retained from their earlier source qualifications. Their actual conditional child, cancellation and callback relationship establishes the local scope. No new source body or user data was acquired for this continuation.

## Custody, attribution and validation

A new dedicated Commons PR query for PayD, CSVUploader and unmount returned the already completed #32041 and #32105 packets. Both retained scopes explicitly left unmount handling unchanged. Root retained no exact prior cleanup-token correction. These are bounded ownership observations, not a global absence claim or permission to replay the previous work.

Original Protocol-Guild/PayD contributors retain credit. The earlier four patches, their guides and the complete Apache-2.0 LICENSE remain unchanged. The existing licence identity is `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`, 11357 bytes. The versioned #32074 reference and its exact final-files metadata UNKNOWN remain historical evidence with that limitation intact.

Validation consists of complete retained source reading, the concrete parent lifetime relationship, the transferred React cleanup contract, static token ordering, exact text identities and serialized forward/inverse plus every-other-byte checks. No React/FileReader/parser/event/file/callback/log/runtime operation, test, fixture, browser or compiler was executed.

Publication adds only invalidate-read-token-on-cleanup.patch and READ_LIFETIME.md to the existing Commons packet. Full immutable artifact strings, native and independent Git identities, exact added paths and final PR/tree/parent metadata are checked. A predeclared alias is used only if a separately observed main equals the verified merge/readback ref; otherwise both artifacts are read completely at one observed immutable main, without chasing subsequent changes.

No upstream action, abort guarantee, whole CSV-format/import acceptance, persistence, accessibility or general lifecycle correctness is claimed.
