# Clear an old analytics error after a successful manual refresh

## Source defect and correction

The actual Analytics route keeps an error state for loadMetrics. Its Re-Scan button invokes handleRefresh, and LiquidityHeatmap also receives that same callback. A rejected loadMetrics attempt can set a non-null error. A later successful manual refresh replaces metrics and lastUpdated but leaves that old error unchanged, so the error banner remains visible alongside newly accepted data until another path clears it.

The patch adds setError(null) immediately after the successful await in handleRefresh. It clears a stale failure when this attempt has obtained data. If the awaited request rejects, this new statement is not reached; the existing catch logging and finally loading reset remain intact. Every other source byte is unchanged.

This is source-level control-flow reasoning. No failed or successful live response, rendered banner, browser interaction, React execution or endpoint was exercised.

## Exact acquired source

All donor inputs were acquired from [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/app/[locale]/analytics/page.tsx | 210bb00fd103fa1ca9a02ae7dedb14f4182aa9bf | 8438 |
| src/lib/analytics-api.ts | d3daf672cc780815418e3c7518ab4d2334c21796 | 23025 |

Both complete bodies were retained from earlier source qualification and independently hashed for this new edit. No source was reconstructed and no duplicate source read was needed. The complete route imports fetchAnalyticsMetrics from the acquired API module, awaits it in both loading paths, renders the error banner under the error condition, and binds its own manual callback to the button and heatmap. This is an actual connected caller, not an unmounted utility hypothesis.

The current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed by GitHub to christabel888. That relocation does not establish sole authorship of the older page. Original source ownership and notices are preserved.

## Why the error path is reachable in the acquired source

The API client's try block awaits fetch and checks response.ok, then returns response.json() without awaiting that body's promise inside its try block. Its existing catch supplies mock data for errors it catches. A later rejection of the returned body promise is adopted by the async function's result and can reach the page's awaited call.

The [WHATWG Fetch Standard, Body mixin](https://fetch.spec.whatwg.org/#body-mixin) specifies a promise for JSON body consumption, rejects it when conversion fails, and identifies a possible SyntaxError from json(). This gives a concrete standards-defined rejection path in the acquired code. It is not evidence that the deployed backend has returned malformed JSON. The [ECMAScript Await semantics](https://tc39.es/ecma262/2024/multipage/control-abstraction-objects.html#await) describe rejection resuming the suspended operation with a throw completion.

For a sequential failed load followed by a successful manual refresh, the old implementation never updates error in the latter callback. The new statement directly repairs that missing state transition. No API catch policy is changed. In particular, the existing API mock fallback still counts as resolved data; this patch does not distinguish live data from mocks or prove backend availability.

## Patch and ordinary source checks

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Page preimage | 210bb00fd103fa1ca9a02ae7dedb14f4182aa9bf | 8438 |
| Page postimage | 965c6e9ca12f99dfdef41ee9fc86ad302a57e827 | 8460 |
| clear-refresh-error.patch | 18e9454cb357fabb8ff97bbec6e2c85e72d22ad5 | 380 |

The actual serialized unified patch contains one hunk and seven rows: one inserted line, no deletions. Forward application exactly produces the complete postimage; inverse application exactly recovers the complete preimage. Removing the one added statement reproduces every original byte. All imports, JSX, error text, API calls, mock generators, loading effects, interval cleanup, logging and data assignments remain as acquired.

Apply the patch at the repository root to the exact preimage above. No compiler, package installation, browser, HTTP request to the application, fixtures, tests or workflow was run. These checks establish the serialized source change, not runtime or whole-build success.

This does not add an error state to a failed manual refresh, revise the banner's existing wording, validate the response schema, disable repeated clicks, cancel an in-flight request, or establish ordering among concurrent automatic and manual requests. A later independent request can still alter the same state. Those behaviors require separate source requirements and are outside this one-line correction.

## Attribution and publication boundary

The directory carries three unchanged upstream MIT notices, copied byte-for-byte from the acquired repository notices:

| Notice | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| upstream-licence-mclaughlin.md | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| upstream-license-menke-laguna.md | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| upstream-license-de-wet.md | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |

The patch is an attributed Commons source proposal. It is not an upstream change, deployment, acceptance or reward event. The narrow Commons phrase search returned zero entries; the first bounded Slack search page contained unrelated, completed or held topics and retained a continuation cursor. Neither result proves global absence of other work. Internal coordination identified no retained same-hunk overlap.

Publication requires the full immutable text plus native and independent blob identities for all five files, and final PR/files/merge/main metadata. Named-main equality may reuse the already verified immutable merge contents only when the observed main SHA equals that merge; otherwise each file is read once at the observed main pin. Actual publication evidence is recorded separately in the release and completion index.
