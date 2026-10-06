# PayD countdown: calculate when the effect starts

The mounted countdown initializes its display fields to zero and previously calculated a target only from a one-second interval callback. A newly supplied target therefore waited for the first interval tick; replacing a target could leave the previous display until that tick. This source correction invokes the existing calculation once after the effect creates its interval.

## Exact source and attribution

Donor repository: `Protocol-Guild/PayD`  
Observed main commit: `171c74b454daba241bfb75f36d10a0a3a77a68e5`  
Changed source path: `frontend/src/components/CountdownTimer.tsx`

This is a current-main residual, not a modification to another contributor's branch. Preserve the repository's original authors. A bounded all-state PR search for the literal component name returned only PR440, an existing testing contribution; its source and tests were not acquired or run. This is not a whole-repository ownership census or a claim that no related contribution exists.

| Source text | Git blob | UTF-8 bytes |
|---|---|---:|
| Original CountdownTimer.tsx | `061e64322c837d3a3331bcb25fa66cb4e000f766` | 2382 |
| Prepared CountdownTimer.tsx | `24604c0a436a4fd555726ca8d4138a1d8bbd23ca` | 2448 |
| frontend/src/pages/PayrollScheduler.tsx | `e394d547dafe88da7d3ce9683666fd47e8a63bce` | 28934 |
| frontend/src/App.tsx | `acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c` | 6460 |
| frontend/src/main.tsx | `f84f187971ba135010c48e69fda10f0c0f71ebd9` | 1664 |
| LICENSE | `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64` | 11357 |

The newly acquired component, caller and App full strings matched their native identities and independent Git blob hashes. Retained complete main-entry and license text also matched independent hashes and the complete current-main tree's exact path/blob entries; these were source-byte transfers for this new consumer, not new provider file reads. The immutable license fetch originally returned content without a native SHA field, so its identity is request-bound plus independently measured. No returned native field is invented.

## Actual caller connection

The main entry renders App. The acquired App renders PayrollScheduler through its `/payroll` route. The caller imports CountdownTimer and renders it with its `nextRunDate` state. Its existing fetch path assigns a new Date from the selected schedule's timestamp and clears that state when there is no schedule. This identifies a connected display consumer; it does not validate the schedule's timestamp, sort order, backend behavior or authorization wrappers.

Only the countdown component is modified. No fetch, scheduling, transaction, wallet, account, form or other caller handler changes. No schedule, employee, browser storage or other user data was read.

## Focused ordering change

The patch names the previous interval body `updateTimeLeft`, preserving its complete calculation, cutoff and state update. The effect then does:

```typescript
    const interval = setInterval(updateTimeLeft, 1000);
    updateTimeLeft();

    return () => clearInterval(interval);
```

The callback closes over the interval identifier. Its explicit first call occurs after that identifier has been initialized. Native interval callbacks are deferred, so defining the closure earlier does not itself read an uninitialized value. An already expired target can therefore use the existing clearInterval path during the explicit call. The returned cleanup still clears the same interval.

The acquired browser API documentation states that the first interval callback occurs after the requested delay, and that the returned interval identifier can be used to cancel it: https://developer.mozilla.org/en-US/docs/Web/API/Window/setInterval . It also notes that actual delays can be longer. This documentation supports the timer-order contract; no browser timing was measured.

This is an effect-time initial update. It does not change the useState initializer and does not promise a correct first render, zero flash or synchronous screen paint. A target replacement causes the existing effect dependency to set up the next interval and invoke its calculation; mutating the same Date object without changing its reference is outside that relationship.

## Verification and limits

The actual serialized unified patch has two hunks, nineteen complete rows, five insertions and two deletions. Independent forward materialization reproduces the exact 2,448-byte prepared component and inverse materialization reproduces the exact 2,382-byte original. The callback's arithmetic, strict negative-distance cutoff, zero fields, one-second interval period, cleanup, target dependency, null return and complete rendered JSX remain unchanged. No component, timer or date example was executed.

The existing behavior for null or invalid dates, clock changes, exact zero distance, browser throttling and callback exceptions remains outside this correction. It adds no request generation, cancellation of in-flight backend work, polling policy, persistence or schedule execution behavior. It does not establish installed dependency compatibility, whole-build success or backend data correctness.

No React/browser/DOM/timer execution, compiler, installation, test, synthetic date sequence, fixture, product API request, schedule action, wallet/payment/account action, upstream submission, sponsor acceptance or reward action occurred. This packet demonstrates a source-level display-order correction only.

## Artifacts and license

`first-effect-update.patch` is the focused modification against the exact current-main component. This guide records the source connection and limits. `LICENSE` preserves the complete Apache-2.0 text. Retain the original repository authors and existing notices. The full donor component and caller modules are not republished.
