# AutosaveIndicator and its existing producer

This reference describes the reusable AutosaveIndicator presentation component in the pinned PayD source and the useAutosave hook that its acquired page callers use. It does not add or modify storage behavior.

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`.

## Component API

Production module: `frontend/src/components/AutosaveIndicator.tsx`. It exports the named AutosaveIndicator component. Its local props interface has two required fields:

| Prop | Type | Meaning in this component |
|---|---|---|
| saving | boolean | Selects the first display branch when true |
| lastSaved | Date or null | Supplies the saved-time display when saving is false and this value is truthy |

The component calls useTranslation unconditionally. It accepts no className, children, save callback, storage key or reset callback. It does not itself read or write storage.

The actual EmployeeEntry usage is:

```tsx
<AutosaveIndicator saving={saving} lastSaved={lastSaved} />
```

Here saving and lastSaved are already obtained by that page from its existing hook call. The snippet does not construct data or start an additional save.

## Display precedence

| First matching condition | Display |
|---|---|
| saving is true | Spinner plus t('autosave.saving') |
| saving is false and lastSaved is truthy | Status dot plus t('autosave.saved') and formatted time |
| Otherwise | Muted dot plus t('autosave.neverSaved') |

Saving wins even if lastSaved contains an earlier Date. The saved branch calls lastSaved.toLocaleTimeString with an empty locale list and hour/minute set to two digits. It does not pass the active translation language as the formatting locale, show a calendar date, or add a relative-time timer. A timestamp from a different day can therefore still be presented as only a time. The declared Date type is not runtime validation; no invalid-Date or string-input handling is added.

The original canonical component has ordinary div wrappers. The separately completed Commons #31982 patch adds role=status to all three wrappers without changing their text, props or selection. Its exact composed postimage is listed below. That source addition is not proof of a particular screen-reader announcement, especially when a branch is inserted conditionally. This reference neither reapplies nor replaces that patch.

## Producer API: useAutosave

The named generic hook is exported from `frontend/src/hooks/useAutosave.ts`.

| Parameter | Declaration | Source role |
|---|---|---|
| key | string | localStorage item key |
| data | T | Value passed to JSON.stringify for a scheduled write |
| delay | number, default 1000 | Delay passed to setTimeout |

Its returned object contains saving, lastSaved, loadSavedData and clearSavedData. It starts with saving=false and lastSaved=null. The generic T is a compile-time annotation; the hook supplies no runtime schema validation.

The effect depends on key, data and delay. It sets saving true, schedules the existing timeout and returns cleanup that clears that timeout. At timeout completion it calls localStorage.setItem(key, JSON.stringify(data)); only after that call succeeds does it set lastSaved to a new Date and saving false. Its catch logs and sets saving false, leaving any earlier lastSaved value intact.

Thus saving includes the pending debounce interval. A saved timestamp describes a successful local call in that hook instance, not a server acknowledgement, database commit or completed employee/payroll operation. An earlier timestamp may remain after a later failure. The hook does not return an error object or failure reason to AutosaveIndicator.

loadSavedData reads the item and parses nonempty stored text, returning the parsed value cast to T. Missing/empty items or caught read/parse errors return null. The function does not update saving or lastSaved. Finding a saved draft therefore does not by itself establish a lastSaved timestamp in this newly mounted hook.

clearSavedData directly removes the storage item and then sets lastSaved null. Its removeItem call is not wrapped by this function's own catch. It does not cancel a pending timeout or set saving false; a pending write can still run later. These are declarations of the retained source, not a reproduced timing experiment or a proposed persistence correction.

The hook stores no timestamp alongside the data and has no cross-tab listener, encryption, server synchronization, conflict resolution or data-shape validation in this module. It does not automatically load the draft into the caller's state; callers must choose how to use loadSavedData.

## Acquired mounted callers

The complete retained App routes /employee to EmployeeEntry and /payroll to PayrollScheduler under their existing wrappers. Both pages import useAutosave and AutosaveIndicator, obtain saving/lastSaved/loadSavedData, and pass saving and lastSaved to the component. Each has an effect that calls loadSavedData and applies a truthy returned value to its own form state.

Neither acquired caller destructures or invokes clearSavedData. The earlier clearSavedData investigation remains NO PATCH because a mounted invocation was not established. This reference describes the hook's declared API without asserting that the clear path is exercised by those pages, or changing caller behavior.

Only this local draft/display connection is qualified. Submission, scheduling, account, wallet, signing, payment and backend handlers are not explained as operational instructions or executed. No real stored draft or employee data was acquired.

## Exact source map

| Source | Git blob | UTF-8 bytes |
|---|---|---:|
| frontend/src/components/AutosaveIndicator.tsx, canonical | af97c737484c46015b852664a227f53a652af425 | 1826 |
| Same component after separate #31982 patch | 350306db9bce5acedb272284843aa75d84830543 | 1868 |
| frontend/src/hooks/useAutosave.ts | 44615916010e71288bd3880c80be4a0bd01147d8 | 1868 |
| frontend/src/pages/EmployeeEntry.tsx | b89a5c832191a19a52c4f7b99201da5ece9acef8 | 11774 |
| frontend/src/pages/PayrollScheduler.tsx | e394d547dafe88da7d3ce9683666fd47e8a63bce | 28934 |
| frontend/src/App.tsx | acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c | 6460 |

All five original complete files match their returned native identities, independent Git blob calculations and the retained canonical tree entries. The separate #31982 postimage was materialized from its acknowledged patch and matched its declared identity; no component or hook was run.

## Limits and attribution

This is source documentation, not runtime, storage, announcement, browser, build, complete accessibility or persisted-work verification. Translation resource completeness, missing-key fallback, locale appearance, error logging outcomes and multi-tab behavior were not tested. Original PayD contributors retain credit and the repository's Apache-2.0 notice remains in the containing Commons documentation packet. See AUTOSAVE_SOURCE.md for custody and publication scope.
