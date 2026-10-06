# CSVUploader reference: source qualification

This PayD180 continuation adds CSV_UPLOADER.md and this qualification note to the existing component-reference packet. Earlier references, source patches and license remain unchanged. No production patch or new parsing policy is included.

## Distinct documentation scope

The retained warm issue180 concerns reusable-component documentation. This entry covers CSVUploader's three props, exported CSVRow shape, local file admission/read path, literal parser/validation behavior, preview/callback boundary and actual EmployeeList consumer. The three completed #32009/#32041/#32062 corrections remain separate accepted work.

A new bounded Commons query for PayD / CSVUploader / documentation, all states and topn10, returned no entries. Root retains no exact reference-documentation completion or hold. This is not a global ownership census or permission to replay protected work. Existing issue194 and issue283 boundaries stay intact.

The complete retained canonical tree has 753 entries and truncated:false, with no docs/components/ entry. A possible upstream destination is docs/components/CSVUploader.md. This packet creates only the two new Commons documents and performs no upstream action.

## Full retained source custody

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`.

| Path | Native and independent Git blob | UTF-8 bytes | Mode |
|---|---|---:|---|
| frontend/src/components/CSVUploader.tsx | 26b62ac2f50ae4d48d7ce4a416b7841f8a2e742f | 7645 | 100644 |
| frontend/src/components/EmployeeList.tsx | 277684e5f87cabd72ff5aadd04299a5360fdf3e0 | 20441 | 100644 |
| frontend/src/pages/EmployeeEntry.tsx | b89a5c832191a19a52c4f7b99201da5ece9acef8 | 11774 | 100644 |
| frontend/src/App.tsx | acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c | 6460 | 100644 |

No application source was newly fetched. All four complete retained bodies independently hash to their native returned SHA and their exact path/mode/size entries in the retained complete tree.

The source chain is App's /employee route, EmployeeEntry's list branch, EmployeeList's Import CSV control and mounted CSVUploader call. The callback path is followed through staging to onAddEmployee and the actual parent-provided logging callback. Neither row.isValid filtering nor a persisted parent update is inferred where the source does not provide it.

The retained latest EmployeeList postimage after #32014/#32038/#32060 is 6be2d27fdc4c280b3db09ad2b36192eeef6f2e4e, 21705 bytes. The complete handleDataParsed/handleAddEmployees source ranges and uploader JSX call match the canonical list exactly. Sorting, accessibility labels, edit controls and row actions are not changed.

## Preserved patch chain

All files below are retained under work/bounty-intake/payd194-csv-drag-over-20261006-7ca6/:

| Completed packet | Patch | Git blob | UTF-8 bytes | Verified merge |
|---|---|---|---:|---|
| #32009 | allow-drag-over.patch | 316183274f505c948430f33037b2ab12d1c9ba71 | 510 | 2c84eeb0a62d6cd56f45c4ed7477c92e9702711e |
| #32041 | latest-read-completion.patch | b1db3f8ed1d5e9dad7f0828b93ce8a669aae17fc | 922 | dfacf49151df1e72d731083e4b6c827d2b1b220b |
| #32062 | text-preview-status.patch | 69a9878cb5047e06e2422f5eb3725f99cbf382c0 | 1122 | b1c487d2c61a3df3a50191cf4ea40d94192f1ab5 |

Their full original guides and Apache-2.0 notice remain untouched. Byte-only sequential application gives the three component identities in CSV_UPLOADER.md; each inverse returns its exact preceding complete version. The final 8039-byte text equals the retained #32062 postimage. The complete internal parseCSV function is byte-identical between canonical and final composed source.

These checks use only text and Git identity operations. They do not instantiate FileReader, parse content, validate records, dispatch drag/drop events, run React, evaluate Number/Date/random expressions, invoke callbacks or reopen accepted source publications.

## Documentation reasoning

The reference separates three layers: the parser's returned error flags, the uploader's preview/callback policy, and the actual parent's import behavior. Validity indicators are not treated as admission enforcement. The mounted parent supplies no custom validators and stages all returned rows; its supplied add callback logs instead of persisting. This is an unresolved source boundary, not an observed production incident or a new correction.

The source records literal comma/newline splitting and exact header-name checks. No CSV standard conformance, quoted-field support, duplicate-header policy, data schema, financial validation or safe-input guarantee is asserted. No test records, personal values or parser examples are generated.

The selected file name is assigned before read completion while prior rows are retained. The token guard acts once before synchronous parsing and its subsequent writes. Invalid/cancelled selections retain the prior admitted token. No abort, unmount, asynchronous-validator, read-error or callback-exception behavior is claimed beyond what the source contains.

The text-status and drag-over patches keep their bounded original purposes. None is represented as completing issue194, fixing persistence or delivering whole-component accessibility.

## Attribution and publication boundary

Protocol-Guild/PayD's original contributors retain credit. Existing external carriers and exact held/protected families remain protected. The containing reference directory retains the original full Apache-2.0 LICENSE, blob 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64, 11357 bytes. No full donor module, employee record, input file or license text is republished here.

Both new documents are independently hashed and fully read at the immutable publication ref against prepared text and native blob identities. Final PR body, changed paths, tree and parents are checked. A fresh same-repository main observation can be a separately predeclared alias only when it equals the verified merge/readback ref; otherwise both full files are read at one observed immutable main without branch chasing.

No application, browser, file, upload, parser, validator, fixture, compiler, test, storage, log, account, wallet, payment or upstream action is performed. The result is a scoped reference with source-qualified limitations, not runtime, import, sponsor or whole-issue acceptance.
