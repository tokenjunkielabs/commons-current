# CSVUploader component reference

CSVUploader is a named export from `frontend/src/components/CSVUploader.tsx` in Protocol-Guild/PayD. It reads the first selected local file, builds rows with validation messages, displays a preview and calls a supplied callback. This reference describes canonical source at `171c74b454daba241bfb75f36d10a0a3a77a68e5`, followed by the separately completed #32009, #32041 and #32062 compositions.

The preview's validity flags do not filter callback output. The acquired mounted EmployeeList consumer also stages every returned row, and its actual EmployeeEntry parent supplies a logging-only add callback. This reference does not describe a persisted import.

## Declared props

| Prop | Declared type | Default | Contract in the source |
|---|---|---|---|
| requiredColumns | string array, required | None | Exact trimmed header names required by the parser; also checked for a truthy row value. |
| onDataParsed | function taking CSVRow array and returning void, required | None | Called with the complete returned rows after onload parsing and setParsedData. |
| validators | string-keyed functions taking a string and returning a string or null, optional | Empty object | Each function runs only when its field's row value is truthy; a truthy returned message joins the errors array. |

There is no endpoint, upload-progress callback, file-size option, delimiter option, validity-filter option, or abort handle in these props. The component does not await onDataParsed or a custom validator. This describes the declared synchronous contract, not support for asynchronous parsing or callback reentrancy.

The named exported CSVRow interface has:

| Field | Declared type | Meaning |
|---|---|---|
| rowNumber | number | The loop's line index plus one, after trimming and splitting the input string. |
| data | string-keyed string record | Values assigned by the parsed header list. |
| errors | string array | Missing-field and custom-validator messages collected for that row. |
| isValid | boolean | Whether errors.length equals zero. |

parseCSV is an internal component function, not a separate exported parser API.

## File admission and state

The hidden file input declares accept=".csv". Both selection and drop handlers take only the first available File. The file-processing function separately requires file.name.endsWith('.csv'); a mismatch shows the existing alert and returns before changing the file name or starting a read.

The source checks a literal suffix. It does not inspect MIME type, contents, encoding or size as an admission policy. The reference does not claim that the file-picker hint validates a file.

For an admitted File, the code sets fileName, constructs FileReader, installs its load handler and calls readAsText. The load handler casts the event result to string, calls parseCSV, stores the returned rows, then calls onDataParsed with the same rows. The cast is not a runtime type check.

The source does not clear the previous parsedData when an accepted selection begins, and it has no dedicated pending-read display. Therefore the source permits the new file caption and the prior preview state to coexist before completion. A cancelled selection or rejected suffix does not explicitly clear prior state.

No reader error or abort handler, unmount cleanup, size limit, decoding selection or file-operation exception recovery is added by this reference. No FileReader, file or upload is actually used to produce this document.

## Literal parser and validation behavior

The parser trims the whole content string and splits it on the newline character. Fewer than two resulting lines returns an empty array. It splits the first line on commas and trims each header. Missing required header names cause the existing alert and an empty-array return.

For each later line, the parser splits on commas and trims each value. It iterates headers, assigning the corresponding value or an empty string to row.data. Surplus values have no header assignment in that loop. There is no explicit duplicate-header or exact-row-width validation.

The parser records a missing-field message when a required field's assigned string is falsy. Custom validators then run for truthy values in their respective fields. An empty non-required field is not sent to its validator. The row is appended regardless of whether errors were found; isValid is calculated from the resulting errors array.

This is literal string splitting, not an implementation of quoted CSV fields, escaped delimiters or embedded quoted newlines. No sample CSV, parser fixture, schema, validator or row was evaluated. The reference supplies no replacement parser and no claim of CSV-standard compliance.

An empty parser result still reaches setParsedData and onDataParsed when the admitted file's load handler completes. A header-error alert does not by itself bypass those subsequent statements in that handler.

## Preview and callback boundary

Summary counts filter the stored rows by isValid solely for display. A preview table is rendered when parsedData is nonempty. Its columns come from the first row's data keys; all stored rows are displayed, with errors listed separately and OK displayed for an empty errors array.

The callback receives all returned CSVRow objects, including invalid ones. The component has no independent Import confirmation button or remote submission call. Its file chooser button and drop handlers initiate the same local read path.

The acquired App renders EmployeeEntry at /employee. In its list branch, EmployeeEntry renders EmployeeList. That list has an Import CSV control and mounts this existing uploader call:

```tsx
<CSVUploader
  requiredColumns={['name', 'email', 'wallet', 'position', 'salary', 'status']}
  onDataParsed={handleDataParsed}
/>
```

No custom validators are passed there. EmployeeList's handleDataParsed maps every returned row into its local staging array without filtering row.isValid. Its separate confirmation handler calls onAddEmployee for each staged item, clears staging and closes the uploader.

The acquired EmployeeEntry passes an onAddEmployee callback that logs the item. That callback does not update its employee state or issue a persistence request. This source chain establishes the display/callback connection and its current limitation; it does not establish a successful import. No record, numeric field conversion, generated identifier, confirmation button or logging callback was exercised here.

## Separately completed source compositions

| Version | Complete component Git blob | UTF-8 bytes | Distinct change |
|---|---|---:|---|
| Canonical | 26b62ac2f50ae4d48d7ce4a416b7841f8a2e742f | 7645 | Original component. |
| After #32009 | 0d4d54488a8e38eea15aa0656af7f95601c5efdb | 7692 | Adds the drag-over default-prevention handler to the existing zone. |
| After #32041 | 81d91b45eb0ecc0bf51b298340cbd258534a081b | 7880 | Guards onload against an older admitted read's token. |
| After #32062 | c3e7ef2b49d275cab07762ce9896ae1264fdd36f | 8039 | Adds visible Valid/Invalid text and hides the decorative status icon from naming. |

These are existing Commons patches, not changes introduced by this reference:
https://github.com/woahwhattheheck/commons/pull/32009
https://github.com/woahwhattheheck/commons/pull/32041
https://github.com/woahwhattheheck/commons/pull/32062

The token correction creates a fresh object for each admitted read and assigns it before readAsText. At the start of onload, identity mismatch returns before parsing, setParsedData and onDataParsed. It does not abort an older reader. A cancelled or rejected selection does not replace the token; constructor/read errors, unmount, asynchronous validators and wider callback behavior remain outside that correction.

The textual status correction uses the same row.isValid value as the original icon. It changes neither validation nor the callback's all-row policy. It also does not repair the parent's logging-only import path.

All three saved patches compose and invert exactly as strings. The complete parseCSV function, EmployeeList staging/confirmation functions and uploader JSX call are unchanged through those qualified compositions. The reference does not rerun a parser or replay an accepted correction.

## Evidence limits

No file, browser, drag event, parser, validator, record, callback, log sink, runtime, compiler, test, account or upstream operation was executed. Error handling, validation policy, import persistence, localization and wider accessibility remain the source's existing limits. See CSV_UPLOADER_SOURCE.md for exact custody and attribution.
