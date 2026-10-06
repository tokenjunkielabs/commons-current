# CountdownTimer component reference

CountdownTimer is a named export from `frontend/src/components/CountdownTimer.tsx` in Protocol-Guild/PayD. It displays days, hours, minutes and seconds derived from a target Date. This reference describes canonical source at `171c74b454daba241bfb75f36d10a0a3a77a68e5` and separately identifies the completed #31966 effect-time update patch.

## Declared API

| Prop | Declared type | Default | Behavior |
|---|---|---|---|
| targetDate | Date or null, required | None | Null returns no rendered output; a supplied Date is used by the effect's countdown calculation. |

The component declares no completion callback, schedule identifier, refresh function, locale, className, interval option, or storage interface. It does not submit or execute a scheduled action. Its Date annotation is not runtime date validation.

The retained caller already uses:

```tsx
<CountdownTimer targetDate={nextRunDate} />
```

No concrete timestamp or runnable timer example is supplied here.

## Connected display consumer

The retained App source mounts PayrollScheduler through its /payroll route. PayrollScheduler imports CountdownTimer, initializes nextRunDate to null, and renders this call below the existing Next Scheduled Run label in its active-schedule presentation.

The caller's acquired fetch path takes schedules[0], creates a Date from that record's nextRunTimestamp and assigns it to nextRunDate. When the returned collection is empty, it sets activeSchedule and nextRunDate to null. This records the actual source connection. The nearby comment calls the selected record the most imminent one, but this reference does not establish backend ordering, timestamp validity, authorization or schedule execution.

No scheduling, fetch, account, wallet, transaction, log or form handler was invoked to qualify the display path. The component's visual countdown is not evidence that any schedule will run or that a backend job completed.

## State and display

The local timeLeft state initializes days, hours, minutes and seconds to zero. A null target returns null from render. The null branch does not explicitly replace the stored timeLeft object; a later supplied target is handled by the existing effect.

For a non-null target the component renders four units separated by colon characters. The labels are the literal English strings Days, Hrs, Min and Sec. Days is rendered directly. Hours, minutes and seconds call toString().padStart(2, '0'). These expressions specify a minimum character width, not an upper limit.

The JSX uses existing flex, font and color utility classes. This reference does not measure layout, compiled styles, localization, contrast or assistive-technology output. There is no aria-live declaration in the acquired component.

## Countdown calculation

Each invoked calculation constructs a current Date, obtains its millisecond value, and computes distance as targetDate.getTime() minus that value. It derives units from that current difference rather than decrementing the previous state.

| Field | Literal arithmetic structure |
|---|---|
| days | floor(distance / (1000 * 60 * 60 * 24)) |
| hours | floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)) |
| minutes | floor((distance % (1000 * 60 * 60)) / (1000 * 60)) |
| seconds | floor((distance % (1000 * 60)) / 1000) |

The expressions use fixed millisecond units, including a 24-hour day. They do not perform calendar-day arithmetic, display a timezone, or validate a date string. The caller constructs the Date before passing it.

The cutoff is strictly distance < 0. That branch clears the interval, replaces all four fields with zero and returns. Exact zero is handled by the ordinary arithmetic branch rather than that strict-negative branch. No finite-value or valid-Date guard is present. These are source observations; no date, arithmetic fixture or timer callback was evaluated for this document.

## Canonical setup and cleanup

The effect declares [targetDate] as its dependency array. It returns early for a null target. Otherwise the canonical source registers the calculation as an interval callback with a requested delay of 1000 milliseconds. Its returned cleanup clears that same interval.

The canonical source has no explicit calculation during setup. The initial zero state, or a retained prior display on a target replacement, is not replaced by this effect until its callback runs. The requested delay is not a measured wall-clock guarantee. The existing dependence on the supplied Date object is distinct from a policy for mutating that same object in place.

Null targets, invalid Dates, clock changes, callback exceptions, browser throttling and wider lifecycle behavior are not repaired by this reference. No change to the component or the caller is included.

## Separate #31966 composition

The completed correction is:
https://github.com/woahwhattheheck/commons/pull/31966

Its existing patch names the original interval body updateTimeLeft without changing the arithmetic, cutoff or state writes. It creates the interval with that function, calls the function once after the interval identifier initializes, and retains the same cleanup:

```typescript
const interval = setInterval(updateTimeLeft, 1000);
updateTimeLeft();

return () => clearInterval(interval);
```

This is the already-published sequence, not a new implementation. Defining the callback earlier is separate from invoking it; its explicit invocation follows interval initialization. The original negative-distance path can therefore refer to the initialized identifier during that call.

The patch changes effect-time setup behavior. It does not change the state initializer, run during render, promise a correct first paint, or eliminate every visible transient. It does not add expiry callbacks, schedule execution, polling, persistence, request cancellation or invalid-date handling. The original guide retains its browser-delay and target-object limitations.

## Exact version identities

| Complete text | Git blob | UTF-8 bytes |
|---|---|---:|
| Canonical CountdownTimer.tsx | 061e64322c837d3a3331bcb25fa66cb4e000f766 | 2382 |
| CountdownTimer.tsx with #31966 | 24604c0a436a4fd555726ca8d4138a1d8bbd23ca | 2448 |
| PayrollScheduler.tsx caller | e394d547dafe88da7d3ce9683666fd47e8a63bce | 28934 |
| App.tsx route | acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c | 6460 |

The composed component identity is reproduced only by applying the saved patch to retained text; inverse application returns the exact canonical source. No React, Date, interval, browser or application behavior is executed. See COUNTDOWN_TIMER_SOURCE.md for custody and attribution.
