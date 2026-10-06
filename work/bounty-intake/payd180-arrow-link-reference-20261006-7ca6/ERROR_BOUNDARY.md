# ErrorBoundary and ErrorFallback reference

This describes the existing PayD components at `171c74b454daba241bfb75f36d10a0a3a77a68e5`. The boundary decides when to replace its children; the fallback renders the message and optional action. Their reset behavior is separate.

## Public component surfaces

Both components are default exports from frontend/src/components.

| Component | Prop | Type | Required | Existing behavior |
|---|---|---|---|---|
| ErrorBoundary | children | React.ReactNode | Yes | Rendered while hasError is false |
| ErrorBoundary | fallback | React.ReactNode | Yes | Rendered after the boundary records an error |
| ErrorFallback | title | string | No | Overrides the translated default title |
| ErrorFallback | description | string | No | Overrides the translated default description |
| ErrorFallback | onReset | () => void | No | When supplied, renders the retry button and is passed directly to its onClick |

The prop types are local declarations, not named exports. Neither component forwards arbitrary props to its markup. ErrorBoundary does not accept a render-function fallback, error callback, reset key, reset handler, className or a public reset method. ErrorFallback does not receive an error object or component stack from ErrorBoundary.

ErrorFallback resolves title and description with nullish coalescing. An omitted value selects its translation key; an explicitly supplied empty string is retained. The source keys are errorFallback.defaultTitle, errorFallback.defaultDescription, errorFallback.tryAgain and errorFallback.goHome. This entry identifies the keys used by the component, without asserting their current resource text in any language.

## Boundary state and reporting

The class initializes hasError to false. Its static getDerivedStateFromError returns hasError: true. Render then selects the supplied fallback instead of children. There is no code in this class that changes hasError back to false.

componentDidCatch calls Sentry.captureException with the caught value and extra.componentStack from React's error information. That source call is the extent of the reporting statement here. It is not evidence that a report was sent, accepted, persisted or scrubbed, or that a deployed reporting service is configured.

The [React Component reference](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary) explains descendant rendering errors, fallback state and componentDidCatch. It excludes event-handler errors, server rendering, errors in the boundary itself and ordinary asynchronous callbacks; its documented transition-function exception is separate. This is a scope explanation, not a claim that the local boundary catches every application failure. The acquired page identifies itself as v19.3, which is not a repository dependency-version assertion.

## Fallback presentation and actions

ErrorFallback renders an AlertTriangle icon, an h2, a description paragraph and its action group. The existing source uses the project's card, glass, noise and theme classes. These declarations do not establish measured appearance, contrast or assistive-technology behavior.

When onReset is provided, the retry control is a native button with explicit type="button". It invokes exactly the supplied callback. ErrorFallback does not reset the boundary, remount children, clear an error, reload the document or make a request on its own.

The Home control is always a React Router Link with to="/". It requires an appropriate router context. A change of route is not wired to a boundary-state reset in these components. If the existing boundary instance still has hasError true, its render method continues selecting fallback.

The component uses useTranslation and the design-system icon import. Its actual application entry already imports the i18n initialization and places BrowserRouter above the boundary. This reference does not install a router, translation provider, icon package or stylesheet.

## Current application wiring

The acquired frontend/src/main.tsx places ErrorBoundary immediately around App, inside BrowserRouter. QueryClientProvider, ThemeProvider, NotificationProvider, SocketProvider and WalletProvider are also ancestors of that boundary. The placement establishes the covered descendant tree; it does not put those ancestor providers inside this boundary.

The current fallback prop is an ErrorFallback element with an empty onReset callback. Consequently the retry button is present, but the supplied callback does nothing. The class also has no reset API. Do not describe the current root wiring as a working retry or recovery mechanism. This reference documents that existing behavior without replacing the callback or adding a reset design.

The Home Link remains available because BrowserRouter is above the fallback. Navigation alone has no declared reset operation on this boundary. There is no promise here that selecting Home restores App after an error.

A minimal usage form inside the application's existing router and initialization is:

```tsx
import ErrorBoundary from '../components/ErrorBoundary';
import ErrorFallback from '../components/ErrorFallback';

<ErrorBoundary fallback={<ErrorFallback />}>
  <section>Content</section>
</ErrorBoundary>
```

This newly authored, unexecuted snippet illustrates the required children/fallback relationship and intentionally omits the optional retry callback. It is not an error-generating demonstration, recovery implementation or instruction to wrap the already-wrapped root again. The relative imports assume a module one directory below frontend/src.

## Source identity and limits

All paths are relative to Protocol-Guild/PayD at the pinned commit.

| Path | Git blob | UTF-8 bytes |
|---|---|---:|
| frontend/src/components/ErrorBoundary.tsx | c57a9ff7bf87afea45f8d6a5ed54f407a9236725 | 759 |
| frontend/src/components/ErrorFallback.tsx | 9af8bd18a15ae00176ed8e62d00e80dd07cf1b44 | 1699 |
| frontend/src/main.tsx | f84f187971ba135010c48e69fda10f0c0f71ebd9 | 1664 |

Original PayD contributors retain credit. See ERROR_BOUNDARY_SOURCE.md for the source, license and contributor-scope record.

No component, error, callback, logging operation, browser, router, package installation, build or test was executed for this reference. It does not establish recovery success, reporting delivery, an error census, accessibility compliance, framework compatibility across versions or complete issue acceptance. In particular, errors in fallback rendering or its event callback are not shown to recover through this same boundary.
