# Use the GitHub token connection with the existing GitData publisher

[connected_github_token_adapter.cjs](connected_github_token_adapter.cjs)
bridges the existing token connection to the native argument and result
contracts used by `publishGitHubChange` and `continueGitHubMerge`. The
publisher itself is unchanged. The caller explicitly selects this adapter
after discovering the actual token tools and preparing an authorized change.

The adapter has no credentials, network client, checkout, authentication gate,
retry, connection switch or fallback transport. Each wrapper invocation makes
one call through the selected token binding. The existing publisher checks
source and provider identities and decides when its merge step is ready.

## API and explicit use

```javascript
const {publishGitHubChange, continueGitHubMerge} =
  require('./host/connected_github_publish.cjs');
const {createGitHubTokenAdapter} =
  require('./host/connected_github_token_adapter.cjs');

const adapter = createGitHubTokenAdapter(tools, {
  onResponse: async observation => retainTokenResponse(observation),
});

const result = await publishGitHubChange(adapter.tools, preparedChange, {
  bindings: adapter.bindings,
  onProgress: progress => retainOperationProgress(progress),
});
```

Supply the existing connected `tools`, complete prepared source and the
caller's retention functions. Keep ordinary publisher options in the same
third argument. The adapter does not infer source pins, merge intent or a
retained operation from provider state. Connected V8 can load both complete,
identified CommonJS sources through `new Function('module', 'exports', source)`
instead of importing from a filesystem; neither adapter execution nor the
existing publisher requires a checkout.

`createGitHubTokenAdapter(tools, options)` returns `{tools, bindings, calls}`:

| Field | Meaning |
| --- | --- |
| `tools` | A separate surface containing the nine publisher-compatible wrapper functions. The original supplied surface is not modified. |
| `bindings` | Action-to-wrapper-name mapping for the publisher's existing `options.bindings`; values are string keys on `adapter.tools`. |
| `calls` | Live invocation records with `action`, actual `binding`, `method`, relative `path` and `outcome`; actual HTTP status, thrown error and callback error are added when available. |

| Option | Default or contract |
| --- | --- |
| `read_binding` | `mcp__codex_apps__github_token_connection_github_read` |
| `write_binding` | `mcp__codex_apps__github_token_connection_github_repository_write` |
| `onResponse` | Optional awaited function receiving `{action, binding, method, path, response}` for each returned token envelope. |

Both selected bindings must exist as functions at construction, including
when a later operation only reads. A supplied callback must be a function.
Binding overrides select already-observed compatible tools; the adapter does
not discover another account or acquire credentials.

## REST mapping and supported scope

The supported scope is the existing atomic GitData publication and its
explicit merge continuation. Use the adapter's surface and bindings again for
`continueGitHubMerge(tools, change, previousProgress, options)` when that
existing API is appropriate. Preserve the original partial progress and
uncertain outcome; continuation does not mean recreating a commit, branch or
PR.

| Publisher action | Token operation |
| --- | --- |
| `fetch` | GET of the relative path from an explicitly supplied `https://api.github.com/` URL. |
| `fetch_file` | GET `/repos/{owner}/{repo}/contents/{path}` with the supplied `ref`, when present. |
| `fetch_blob` | GET `/repos/{owner}/{repo}/git/blobs/{blob_sha}`. |
| `create_blob` | POST `/git/blobs`, retaining source content and encoding. |
| `create_tree` | POST `/git/trees`, mapping `tree_elements` to `tree` and the optional `base_tree_sha` to `base_tree`. |
| `create_commit` | POST `/git/commits`, mapping `tree_sha` to `tree` and ordered parent SHAs to `parents`. |
| `create_branch` | POST `/git/refs` with `refs/heads/{branch_name}` and the exact supplied commit SHA. |
| `create_pull_request` | POST `/pulls`, retaining supported PR fields and projecting actual returned `head.sha` to `head_sha` and `html_url` to `url`. |
| `merge_pull_request` | PUT `/pulls/{pr_number}/merge`, mapping `expected_head_sha` to REST `sha`. |

Writer paths in the table share `/repos/{owner}/{repo}`. Branch creation
requires a complete lowercase 40-character `sha` and rejects `base_ref`;
there is no resolution read or update of an existing branch. This is the
publisher's exact-created-commit subset of the native branch contract.
Contents publication and contribution-ref advancement are outside this
adapter's scope. It adds no Contents writer, deletion primitive or ref-update
binding.

The `fetch` wrapper accepts explicit GitHub REST API URLs only, strips that
exact origin and exposes encoded slash separators as literal slashes for the
current token path parser. It
does not accept repository HTML or raw-file URLs. Contents paths encode each
component separately. The Contents `ref` formatter leaves slash and colon
literal for the current token route, escapes query delimiters and literal `+`,
and retains `%20` for spaces. This limited formatting does not establish
support for arbitrary search routes or query shapes; a rejected route remains
the returned error, without a second attempt.

## Complete content and omitted bodies

A Contents response must identify a file at the exact requested path. The
adapter retains its SHA, size and path and constructs the publisher's
`display_url` using the supplied ref when present. For a returned base64
body, it removes transport whitespace, validates padded base64 syntax and
decodes the entire body. UTF-8 decoding rejects malformed bytes instead of
replacing them and preserves the source's BOM and line endings. Requested
base64 content retains the cleaned complete base64 string.

For UTF-8 bodies, optional positive, ordered `start_line` and `end_line`
select one-based lines while preserving their terminators, including a final
line without a newline. Base64 bodies reject line ranges. The publisher's
one-line preimage request therefore retains the actual returned blob identity
without presenting that slice as complete source.

`encoding: 'none'` or a missing Contents `content` field retains metadata and
omits the adapted content. It never substitutes an empty postimage. The
unchanged publisher can then make its existing optional `fetch_blob` read for
an observed nonempty text blob whose body was omitted. That separate wrapper
requires the returned blob SHA to equal the requested SHA and decodes the
complete base64 blob as UTF-8. The adapter adds no hidden blob request after
a file read and no alternate route after a failed file response.

## Raw response custody and failures

Every returned adapted wrapper has `token_response` containing the exact
original token envelope. Successful projection requires an actual
`structuredContent` wrapper with integer 2xx `status`, `ok === true` and
`data`; each projected publisher payload must be an object. Failed provider
envelopes and invalid response shapes return native-shaped error envelopes
while retaining that original `token_response`.

An actual 404 with provider message `Not Found` becomes the native
`NOT_FOUND` error shape required by the publisher's existing absence check.
Other errors retain their supplied error code when available; unknown HTTP
failures use `GITHUB_HTTP_ERROR`, and projection/shape failures use
`TOKEN_RESPONSE_SHAPE`. Available provider data, status and headers remain in
the adapted error data. The publisher still checks actual returned object
identities, expected source versions, merge acknowledgement and complete
immutable readbacks.

`onResponse` is awaited before decoding and receives successful, failed and
malformed returned envelopes. Its exception is recorded as `callback_error`
on the affected `calls` entry. It does not erase the response, change the
provider result or replay the call. A provider-thrown exception records
`outcome: 'threw'` and propagates the original exception; no returned envelope
or callback observation is invented. Final returned-call outcomes are
`success`, `provider_error` or `response_shape`.

The call records contain metadata rather than full request bodies or source.
Retain the complete prepared packet and raw responses separately when the
operation needs durable custody. A callback failure or malformed write
acknowledgement does not justify repeating a potentially completed write.

## Publishing a prepared packet

Prepare exact previous blob identities and source pins, then use
`publishGitHubChange(adapter.tools, change, {bindings: adapter.bindings,
onProgress})`. Its default pinned-source path creates blobs, one tree and one
commit, creates a new branch and PR, performs the requested merge and reads
the complete published source at the returned immutable commit. The adapter
does not replace any of those checks. A later named-main observation can bind
those immutable source checks to current main. Preserve partial progress and
raw responses when an operation stops so the next action continues or
reconciles the existing provider objects.
