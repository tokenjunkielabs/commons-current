# Supplied Library read headers

`connected_library_read_headers.cjs` provides a bounded view of a supplied native
Library read response. It copies literal file and version identifiers, size and
pagination metadata, and counts rendered content blocks without returning their
text. It performs no I/O and leaves the complete supplied response available to
its caller.

```js
const {projectLibraryReadHeaders} = require('./connected_library_read_headers.cjs');
const view = projectLibraryReadHeaders(retainedNativeRead, {
  start_index: 0,
  max_items: 1,
  max_metadata_units: 1024,
  max_string_units: 256,
  max_content_blocks: 1
});
```

The accepted envelope is the observed native tool result with
`structuredContent.results` as an array. The helper does not parse JSON text,
search arbitrary wrappers, fetch another page, or certify that a supplied object
came from Library. An explicitly supplied `isError: true` is `UNSUPPORTED`.
Missing or invalid shapes have an explicit unsupported reason. The supplied
error flag's state is retained separately; absence is not success evidence.

## Bounds and literal values

The default limits are 20 items, 4,096 UTF-16 units across copied string metadata,
512 units per string, and 16 scanned content blocks per selected item. Item and
content scan limits have independent ceilings of 100 and 1,024. A nonnegative
`start_index` selects a window in the supplied results array. The caller can set
any budget to zero. Invalid options throw before projection.

Each selected item's `source_path` and `source_index` identify the location in
the supplied envelope. Array holes and invalid records remain explicit entries.
`retained_results` is the supplied array length; `remaining_results` is only the
unselected suffix of that array. Neither indicates how many Library files or
provider pages exist. An empty window does not establish absence elsewhere.

String metadata is copied whole and unchanged, or omitted with
`budget_omitted`. No identifier or filename is shortened. Numeric metadata must
be a nonnegative safe integer; boolean metadata must be a boolean. A field's
`missing`, `null`, `invalid`, `budget_omitted`, or `observed` state distinguishes
unknown values from a literal zero or false. Null version metadata is retained
as null; it is not a concrete version guard for replacement.

The copied fields include Library and backing file IDs, read reference, version
ID, filename, MIME/provider/artifact type, timestamps, mode, line/page bounds,
size metadata, and the declared `has_more`/text/image flags. Warning text is not
copied; only its observed array count is reported. URLs, transfer headers,
xattrs, signed materialization descriptors, and arbitrary fields are excluded.

## Rendered text is separate from file bytes

`content_summary` reports the observed content-array length and the bounded
number of scanned blocks. For scanned string blocks it sums JavaScript string
lengths as `scanned_text_utf16_units`; no text or excerpts are returned. Other
block types and holes have separate counts. `scan_complete` describes only that
bounded traversal of the supplied array. It does not certify complete text,
provider content, a download, or raw byte equality. The helper never converts
`has_more: false`, line counts, or a size field into such a claim.

The actual retained read of the worker's 7,699-byte recovery checkpoint supplies
one string block, all 54 declared lines, and `has_more: false`. That rendered
string omits the source's final LF. A subsequent exact materialization recovered
the complete original 7,699 bytes including that LF. This is why rendered text
length and provider size metadata stay separate. A byte-equality receipt needs
complete materialized bytes and an independent exact comparison.

The original retained native response was consumed once with a one-item,
one-block window. Its literal file IDs, null version, size, 54-line declaration,
and false `has_more` remained exact; the string block's 7,690 UTF-16 units were
counted with zero body output. Complete input serialization and the original
result/content references remained unchanged. Syntax inspection passed. No
Library read, transfer, account/mail action, network, DOM or provider mutation
was performed during that consumption. This observed activation is not a claim
about unobserved modes or envelopes.
