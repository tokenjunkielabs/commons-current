# CSV upload zone drag-over admission

The current PayD CSV upload zone installs drag-enter, drag-leave and drop handlers, but does not cancel drag-over. This patch adds one onDragOver callback to that same wrapper so the native drag operation can admit the existing drop handler. It changes one JSX line and leaves the complete parsing, file-selection and downstream data paths byte-for-byte unchanged.

This is a source-only continuation prompted by [Protocol-Guild/PayD issue 194](https://github.com/Protocol-Guild/PayD/issues/194). It is a partial correction to the existing implementation, not delivery of the issue's requested react-dropzone migration, file-size validation, or an end-to-end bulk-import feature.

## Immutable source and patch

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`.

| Source path | Before Git blob | Before UTF-8 bytes | After Git blob | After UTF-8 bytes |
|---|---|---:|---|---:|
| frontend/src/components/CSVUploader.tsx | `26b62ac2f50ae4d48d7ce4a416b7841f8a2e742f` | 7645 | `0d4d54488a8e38eea15aa0656af7f95601c5efdb` | 7692 |

The source mode is 100644 in the complete pinned repository tree. `allow-drag-over.patch` has one hunk, seven complete rows, and +1/-0 source lines. It inserts `onDragOver={(e) => e.preventDefault()}` between the existing drag-enter and drag-leave props. Serialized forward application yields the whole postimage; serialized reverse application yields the whole original source. Removing the single inserted line reproduces every original byte. These are text checks, not execution of the component or a drag operation.

## Actual connected caller

The complete acquired and retained modules establish this chain:

1. `frontend/src/main.tsx` supplies the application's BrowserRouter.
2. `frontend/src/App.tsx` renders EmployeeEntry on the existing `/employee` route.
3. `frontend/src/pages/EmployeeEntry.tsx` renders EmployeeList after its existing loading branch.
4. EmployeeList's existing Import from CSV button sets its local uploader visibility. The conditional CSVUploader receives its existing required columns and handleDataParsed callback.
5. CSVUploader's drop handler selects the first dropped File and calls the same handleFileParse function used by the browse input.

| Unchanged caller | Git blob | UTF-8 bytes |
|---|---|---:|
| frontend/src/main.tsx | `f84f187971ba135010c48e69fda10f0c0f71ebd9` | 1664 |
| frontend/src/App.tsx | `acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c` | 6460 |
| frontend/src/pages/EmployeeEntry.tsx | `b89a5c832191a19a52c4f7b99201da5ece9acef8` | 11774 |
| frontend/src/components/EmployeeList.tsx | `277684e5f87cabd72ff5aadd04299a5360fdf3e0` | 20441 |

Main/App bytes were reused from existing complete custody and qualified against the canonical tree, not reacquired or described as fresh file reads. CSVUploader, EmployeeEntry and EmployeeList were acquired completely at the pinned donor ref; returned native identities and independent full-content Git blob identities match.

The current EmployeeEntry callback supplied as onAddEmployee only logs its argument. Consequently, this mounted UI chain does not establish a persisted employee import. No employee records, files, accounts or submission handlers were accessed or invoked. The patch does not change that callback or make a production-write claim.

## Browser contract and precise behavior

[MDN's HTMLElement dragover event documentation](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragover_event), acquired 2026-10-06, describes cancellation of drag-over on the target as the step that permits receiving drop. It also identifies the event as cancelable and able to bubble. That primary API contract supports the source correction; it is not a browser test or a guarantee that every platform, surrounding listener or user gesture succeeds.

The existing drag-enter callback already prevents its default, the drop callback already prevents its default, and the new callback supplies the missing drag-over cancellation. It does not parse or submit data, set new state, change propagation, choose a drop effect, or introduce a dependency. It does not install a global document/window handler.

The correction does not filter drag-over by MIME type. Acceptance still reaches the existing file handling, including the case-sensitive .csv suffix check and first-file selection. Dropping non-file data still finds no first File in the unchanged drop path. Drag leave/highlight behavior remains unchanged.

## Current carrier and attribution

A bounded current PR search for issue number 194 in Protocol-Guild/PayD, state all and top 20, returned no entries. This is not an exhaustive ownership search or a claim that no contributor work exists. The observed issue is open with no assignees and one comment. That complete comment is shobhamerabacha-star's request to be assigned, not a maintainer assignment, acceptance or permission. Its promised implementation and test plan were not treated as observed code.

The bounded latest path history reports commit `4f5dd01b31a0b7445e50408398b6fbe9b52d8f48`, author name “Mainnet-ops”, with a design-adoption subject. That is a latest observed path attribution, not identification of the original component author or a full authorship census. The source remains credited to Protocol-Guild/PayD's contributors.

A bounded code search for CSVUploader returned the component, EmployeeList and a generated build-info file with incomplete_results false. Only the two source modules were used; generated build-info was not expanded or accepted as compilation evidence. No upstream branch, PR, issue, assignment or contributor artifact was changed.

The accompanying LICENSE preserves the retained complete donor Apache-2.0 license text, Git blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`, 11,357 UTF-8 bytes. Existing source attribution is retained. This packet contains a minimal patch and guide, not a re-publication of every acquired caller.

## Limits and validation

No browser, drag event, FileReader, file upload, CSV parsing, synthetic file, fixture, test, compiler, package manager, service, wallet or account operation was run. No full-build, accessibility-wide, issue-acceptance or economic claim follows.

The pre-existing simple comma/newline parser, header and value handling, validator behavior, row admission, file size/type policy, asynchronous read ordering, error handling, highlight lifetime, same-file reselection and browse-button semantics remain outside this change. The patch does not claim CSV standard conformance, react-dropzone adoption, successful persisted imports or reliable processing of every input.

Publication verification is recorded separately using exact prepared artifacts, immutable native full-content readbacks, independent Git blob identities and PR/path/tree/parent metadata. A later main equality observation may be recorded as a separate qualified alias; otherwise every artifact must be read completely at one observed immutable main commit. No runtime verification is implied by either path.
