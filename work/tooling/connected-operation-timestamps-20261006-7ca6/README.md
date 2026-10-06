# Optional caller timestamps in the connected operation recorder

The connected operation recorder now accepts `observe_timestamps: true`. This records the caller's wall-clock observation immediately before invoking a binding or local callback and as the first continuation when its awaited result returns or throws. It closes a concrete reporting gap: a recent main-alias check could only be located within a broader independently observed interval because the existing recorder had no per-call time fields.

The option defaults to false. Existing callers receive the same metadata shape unless they opt in. This change updates the existing recorder; it adds no transport, retry, routing, scheduling, authorization, duration calculation, or additional provider operation.

## Source and attribution

The existing implementation is `host/connected_operation_recorder.cjs` in `woahwhattheheck/commons`, originally published in [PR #31824](https://github.com/woahwhattheheck/commons/pull/31824). Its retained complete input is Git blob `bf0e3e56eae2bbc5da87ea8d92bd3fb04dd34a11`, 15,360 UTF-8 bytes. No old source or accepted changes were reconstructed.

For this change, native main metadata bound commit `fbf8e062c8de000f9c1b05f4872a7968188e2d3d` to root tree `e435ca9972f7e6b99c90db5ccd4763cbc5edfc2d`. Its complete nonrecursive root tree bound `host` to tree `9db3e96cb01dd9f00537667da394236d40905f89`. The complete 985-entry host tree returned the exact retained recorder blob, size, and mode 100644. The recorder source was not fetched again.

The postimage is `7785fd1cc9d23ad9a18c0a208ea4760eddb460d0`, 16,514 UTF-8 bytes, with 30 added lines and one removed line. The companion `change.patch` describes that exact transition. This guide is a new original document under a task-specific tooling path; it does not reconstruct or replace the earlier recorder guide.

A bounded all-state Commons PR search for `"connected_operation_recorder" "timestamps"` returned zero results. This is only the observed search result, not a global ownership claim.

Current root instructions were acquired once for this new edit, read completely, and independently matched: `AGENTS.md` blob `746d9dabb2acbf6211997fa7640fefe898e3d3be` / 34,889 bytes and `RULES.md` blob `9941e220d7bd3efaf999ea8d739595aebf1bdd1c` / 12,406 bytes. No nested host AGENTS, RULES, or CONTRIBUTING entry appeared in the complete host tree. The standing offline execution and private-data limits govern this work.

## Enable it on a new real operation

Keep the existing operation identity, private retain callback, native bindings, and normal invocation flow. Add only the new boolean when creating the recorder:

```javascript
const recorder = createConnectedOperationRecorder({
  operation_id,
  entry_prefix,
  retain,
  max_calls: 64,
  serializable_errors: true,
  observe_timestamps: true,
});

const recordedBindings = recorder.wrapBindings(nativeBindings);
```

Use `recordedBindings` for the actual intended calls, or the existing `recorder.run(descriptor, invoke)` interface for a local boundary. Capture `recorder.snapshot()` after the intended work settles. Enabling serializable errors remains a separate existing choice; timestamp observation does not require it.

The planned first consumer is the next genuine intake clock/channel-read operation. No earlier provider request, main-alias check, accepted release, or failed route should be repeated merely to obtain timestamps.

## Metadata contract

Only opted-in call metadata contains a `timestamps` object:

| Field | Meaning |
| --- | --- |
| `basis` | Always `caller_wall_clock_not_provider_native`. |
| `format` | Always `ISO_8601_UTC`. Successful values come from `new Date().toISOString()`. |
| `invocation_at` | ISO UTC string when observation succeeds; otherwise null. |
| `invocation_status` | `not_observed`, `observed`, or `unavailable`. |
| `settlement_at` | ISO UTC string when observation succeeds; otherwise null. |
| `settlement_status` | `not_observed`, `observed`, or `unavailable`. |

Each metadata projection copies this flat object. It appears in saved call-entry metadata, snapshots, and the existing error diagnostic's `call` metadata. The private raw result and the existing error-description slot keep their original shapes.

Both observations start at null / `not_observed`. Directory, request, and invocation-intent persistence happen before the invocation observation. A saved intent still has `invocation_started: null`; its timestamp fields do not claim that a callback or provider ran. Validation, snapshot, or retention failure before invocation leaves the observations unattempted.

The invocation observation occurs synchronously just before the existing single `invoke(request)` expression. Return and throw observations occur before asynchronous result/error retention. Consequently they do not include the later retain-callback acknowledgement time.

These are observations in the caller's execution context. For an awaited promise, settlement is observed when its continuation runs. It is not the remote provider's internal completion time. A binding may reject locally before any provider dispatch; `invocation_started` means the callback was invoked, and `provider_outcome` remains deliberately unassessed. An MCP error envelope returned normally remains an unchanged returned value.

The host wall clock can jump, be adjusted, or disagree with another clock. The fields do not establish elapsed duration, monotonic ordering, remote processing time, health, authentication, acceptance, or source freshness. Do not subtract them and report a verified performance measurement. Concurrent call IDs still express assignment order, not completion order.

## Clock and custody failures

A synchronous clock exception is caught inside the observation function. That observation becomes null / `unavailable`; it does not prevent invocation, add a call, retry, or replace the original returned/thrown outcome.

Default thrown-value identity remains unchanged. When `serializable_errors` is enabled, the existing wrapper still exposes a serializable diagnostic and keeps the original error privately. Timestamp data reaches that diagnostic through the call metadata; it is not attached to or substituted for the original thrown value.

The existing retention queue and custody-error behavior are unchanged. A failure to retain a result still throws a custody error with the original result privately available; it never returns success silently or invokes again. Where that diagnostic has call metadata, the observed timestamps are included. A process loss between invocation and completed final-entry retention can still lose the observations: this feature does not provide a write-ahead remote timestamp or stronger durability than the retain callback.

Timestamp observations do not make private requests, results, error messages, or snapshots suitable for public publication. Keep those records private and publish only the narrow metadata needed for the actual work report.

## Validation scope

The complete retained preimage independently matches its expected Git blob identity. Six exact source replacements account for the change; reversing them reproduces every original byte. A pure text application of the generated patch checks every old context line, both hunk counts, and the exact full postimage.

Focused static comparisons preserve the request-snapshot function, error-description function, retention function, rethrow function, thrown-completion function, and binding/export suffix byte-for-byte. There remains exactly one `value = await invoke(request)` expression. The inserted return/throw observations precede their existing asynchronous retention paths; the initial saved intent precedes both observations.

The modified module has not been executed during preparation. No fixture, test suite, compiler, executor, workflow, provider replay, benchmark, clock-failure injection, or retention-failure injection was used. First adoption and any exercised branch must be reported separately from these static checks.
