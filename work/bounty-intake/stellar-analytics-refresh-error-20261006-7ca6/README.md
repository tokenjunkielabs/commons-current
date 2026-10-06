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

## Continuation: remove an unsupported fixed comparison

This continuation follows #31964 and consumes its complete retained analytics-route postimage. The refresh recovery correction is preserved.

The actual Success Probability MetricCard receives the fetched avg_success_rate as its value, but also receives the constants trend={1.2} and trendDirection="up". The complete mounted child in src/components/dashboard/MetricCard.tsx (0be01cd20b73e9cd85b74e17f94398ae7f69e7f0, 2043 UTF-8 bytes) renders Math.abs(trend) percent followed by "vs prev window" whenever trend is not undefined. Thus the comparison is always 1.2% upward, independent of both current and previous measurements. The declared AnalyticsMetrics type includes avg_success_rate and no previous-window success rate or comparison-delta field. No local calculation derives the fixed trend from history.

The patch removes only those two constant props. The shared MetricCard already makes trend optional and conditionally renders the comparison row; omitting it suppresses that unsupported row. Omitting the fixed direction also removes this card's direction-driven glow-success class from its decorative Activity icon. No zero, unchanged, improved or worsened comparison is substituted. This intentionally leaves the comparison unavailable until a real data contract and calculation support it.

The current value expression, percentage formatting, card label, other cards, shared MetricCard source, metrics request/fallback paths and every other route byte remain exact. The change does not repair or assert the truth of broader analytics data, sample fallback metrics, historical windows or other components' trends.

| Comparison continuation item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Analytics route after #31964 | 965c6e9ca12f99dfdef41ee9fc86ad302a57e827 | 8460 |
| Route with fixed comparison props removed | d0dc3903ea602257ce7780fdf94c1a530549a757 | 8404 |
| remove-fixed-success-trend.patch | 87614d82b1de42c8182965db6d8acd8cca218dcc | 472 |

The incremental serialized patch contains one hunk and eight rows, with zero additions and two deletions. Complete forward and inverse reconstruction matched the source identities. Removing precisely the two unique prop lines produces the full postimage; every other byte is unchanged.

Source qualification uses the complete retained route and analytics API from the preceding packet, and one newly acquired complete MetricCard body with native and independent Git blob equality at the same immutable donor. The analytics API source is d3daf672cc780815418e3c7518ab4d2334c21796, 23025 UTF-8 bytes. Only the public type and actual caller relationship are described here. Bounded analytics/trend/1.2 Commons and AnalyticsPage/trend Slack queries returned zero rows, with native END for Slack; they do not establish global absence.

Apply clear-refresh-error.patch first, then remove-fixed-success-trend.patch. Only the new patch and this exact-preimage-guarded README continuation are written. Original patch and all three MIT notices remain unchanged, preserving attribution.

No application, metric calculation, browser, compiler, fixture, tests, workflow or upstream action was executed. Runtime layout and complete page behavior were not observed. Publication requires both complete newly written immutable bodies to match text, native and independent identities, followed by exact PR/files/head/merge/parents/tree/main metadata. Fresh observed main equality can reuse those verified immutable bodies through an explicit alias; otherwise both changed artifacts are read once at that observed immutable main commit.
