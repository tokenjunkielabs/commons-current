# useNotification and NotificationProvider reference

Reference for Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`. This describes the existing notification context and wrapper API. It adds no notification behavior.

## Public exports

`frontend/src/hooks/useNotification.ts` exports the interface NotificationContextType, the NotificationContext object, and the useNotification function. The context is created with an undefined default. The hook reads it with React use; if the returned value is falsey, it throws the literal error "useNotification must be used within NotificationProvider". Otherwise it returns the context value.

`frontend/src/providers/NotificationProvider.tsx` exports the named NotificationProvider component. Its only declared prop is children: React.ReactNode. It wraps those children in NotificationContext with the four functions below. There is no default export in either acquired module.

| Context method | Declared arguments | Declared result | Existing provider call |
|---|---|---|---|
| notify | message: string | void | toast(message) |
| notifySuccess | message: string, description?: string | void | toast.success(message, { description }) |
| notifyError | message: string, description?: string | void | toast.error(message, { description }) |
| notifyWarning | message: string, description?: string | void | toast.warning(message, { description }) |

The first argument is named message in this API. A separate title field, structured message object or options object is not declared. notify accepts only one declared argument. The three typed variants pass an object containing description even when the optional argument is omitted.

Each provider function is created with useCallback and an empty dependency list. The source imports toast from sonner, casts it to any, invokes the corresponding member, and does not return that invocation's result. This wrapper therefore does not expose a toast identifier, Promise, completion acknowledgment or cancellation handle. Its declared void result must not be interpreted as successful display or delivery.

The provider constructs a new context-value object in its render expression; the source does not memoize that object. This observation does not establish a performance problem or a render-count measurement.

## Using the API

A consumer reads the context during its component render and invokes one of its functions from its existing event or application flow:

```tsx
import { useNotification } from '../hooks/useNotification';

export function ExampleNoticeButton() {
  const { notifyWarning } = useNotification();

  return (
    <button
      type="button"
      onClick={() => notifyWarning('Example notice', 'Optional explanatory text')}
    >
      Show example notice
    </button>
  );
}
```

This is a newly authored, unexecuted illustration. The import assumes a component one directory below frontend/src. It requires an appropriate NotificationContext value above the component. The standard provider supplies that value:

```tsx
import { NotificationProvider } from '../providers/NotificationProvider';

export function ExampleNoticeScope() {
  return (
    <NotificationProvider>
      <ExampleNoticeButton />
    </NotificationProvider>
  );
}
```

The two snippets are conceptual neighbors in the same module; the second refers to the first component. They do not install a Sonner display host. Do not add another provider around every existing application consumer based on this example.

The acquired provider renders only its context wrapper and children. It does not itself render a Toaster or another notification display component. The location, configuration and behavior of any display host are outside the two-module acquisition. A context provider and a visible notification host serve different source roles.

## Actual retained consumers

These examples describe existing code paths. No form, account, certificate, network request, notification or download was invoked to produce this reference.

| Consumer | Source use of the context | Relevant boundary |
|---|---|---|
| frontend/src/pages/EmployeeEntry.tsx | Reads notifySuccess once through useNotification; its existing submission path calls it after an awaited request completes | This is call ordering in source, not proof of a request, data update or successful toast display |
| frontend/src/components/CertificateDownloadButton.tsx | Reads notifySuccess and notifyError; existing validation/download paths choose a message and optional description | The wrappers do not validate a certificate, authorize a request or acknowledge download completion |

The complete retained App source imports and renders EmployeeEntry under the existing employer layout. Its full retained caller body establishes that this is application source, rather than an isolated demonstration. The earlier ThemeToggle reference in Commons #32033 separately qualified the canonical main entry's root mounting. Only that prior qualification and the entry's path/blob/byte identity survive in this continuation; the full main body was not reacquired or reconstructed here. This reference does not present a fresh verification of main's provider order or notification-host configuration.

The CertificateDownloadButton body used here is the complete canonical preimage. Later protected #31987 and #31991 work addressed automatic lookup admission and resource cleanup respectively; this reference neither reconstructs their callers nor changes or revalidates those patches. The certificate component's complete parent locator is not retained here, so it is not asserted as a newly established mounted route.

EmployeeEntry also has a separate local notification state. That local state is not part of NotificationContextType. Reading this hook does not expose that state or any list/history of notifications.

## Error, lifetime and configuration boundaries

The hook's explicit guard covers the absence of a usable context value. The provider itself has no try/catch around toast calls. If an invoked toast function throws synchronously, this wrapper does not swallow it. Existing consumer-level catches remain their own behavior; this reference adds no recovery.

No wrapper accepts duration, position, rich content, action buttons, identifiers, deduplication keys, persistence, priority or dismissal callbacks. There is no context-level clear, dismiss, update or history method in the acquired interface. This is a statement about this wrapper surface, not a claim that Sonner lacks such features.

The source neither schedules a timer nor awaits a notification result in these methods. It also has no transport, permission request, email, browser Notification API or operating-system notification call in either acquired module. The method names success, error and warning select Sonner members; they are not independent verification of the underlying operation.

The source casts the Sonner import to any and suppresses unsafe-call/member lint rules. This reference reports those existing lines without changing them or treating the casts as evidence of dependency compatibility. No installed Sonner source, types, browser renderer or build was acquired or executed for this entry. Visual style, announcements, focus, duration, stacking, dismissal, host placement and persistence are deliberately unverified.

## Source identities and prior qualification

All complete source bodies below are relative to the pinned Protocol-Guild/PayD commit. The two notification modules are newly acquired for this entry. The other complete bodies were already retained and reused; their independent text hashes match their canonical tree entries.

| Path | Git blob | UTF-8 bytes | Custody |
|---|---|---:|---|
| frontend/src/hooks/useNotification.ts | `782cf022cfa13d25961555d27ddb9b98509f75c8` | 620 | New full immutable acquisition |
| frontend/src/providers/NotificationProvider.tsx | `ae41db777ed5dd4a0ffbb4e88a7c1ee2bde0ad19` | 1480 | New full immutable acquisition |
| frontend/src/pages/EmployeeEntry.tsx | `b89a5c832191a19a52c4f7b99201da5ece9acef8` | 11774 | Complete retained consumer |
| frontend/src/components/CertificateDownloadButton.tsx | `c463d21593e71db2021850026aaa591bf0f0f5d2` | 4011 | Complete retained canonical consumer; parent locator not retained |
| frontend/src/App.tsx | `acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c` | 6460 | Complete retained route source |

The distinct prior entry qualification is frontend/src/main.tsx, Git blob `f84f187971ba135010c48e69fda10f0c0f71ebd9`, 1664 UTF-8 bytes, documented in [the immutable #32033 reference](https://github.com/woahwhattheheck/commons/blob/e0eecfe3fee128376458b8e2e86f43f9ac6eab18/work/bounty-intake/payd180-arrow-link-reference-20261006-7ca6/THEME_TOGGLE_SOURCE.md). It is not included in the newly checked full-body table.

Original PayD contributors retain credit. See NOTIFICATION_SOURCE.md for the task, protected work, license and publication limits. No production source, notification, renderer, dependency, runtime or upstream state was changed.
