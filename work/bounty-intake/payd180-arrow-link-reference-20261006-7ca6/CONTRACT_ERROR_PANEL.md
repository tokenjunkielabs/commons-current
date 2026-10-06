# ContractErrorPanel component reference

Reference for the existing PayD presentation component at `171c74b454daba241bfb75f36d10a0a3a77a68e5`. ContractErrorPanel displays a supplied error record. It does not invoke a contract, sign a transaction, parse XDR itself or carry out the suggested action.

## Imports and props

The module frontend/src/components/ContractErrorPanel.tsx exports both the named ContractErrorPanel and the same component as its default export. Its Props interface is local to the module.

| Prop | Type | Required | Behavior |
|---|---|---|---|
| error | ContractErrorDetails or null | Yes | Null returns no panel markup; a supplied record is displayed |
| className | string | No | Defaults to an empty string and is appended to the root CSS-module classes |

The imported ContractErrorDetails interface is exported from frontend/src/utils/contractErrorParser.ts.

| Field | Declared type | Component use |
|---|---|---|
| code | string | Always displayed in the header; two exact codes also select raw details |
| message | string | Displayed in the expanded message paragraph |
| action | string | Displayed under the fixed Suggested Action label |
| rawXdr | optional string | Selects the raw section when truthy and supplies the Copy text |

The component does not validate this record, decode its rawXdr field or map code to message/action. Those are separate producer concerns. The suggested-action field is presented as supplied text; this reference does not endorse a transaction instruction or diagnose a real contract failure.

Only error and className are consumed. There is no children slot, onRetry, onDismiss, controlled expanded prop, title override, copy callback or arbitrary attribute forwarding.

The established caller uses the named export with its existing state:

```tsx
<ContractErrorPanel error={contractError} />
```

This is a source usage shape, not a data fixture or an executed example.

## Rendering and raw-detail selection

The component initializes isExpanded to true before checking error. With a non-null record it renders a root panel, a clickable header, the fixed title Contract Invocation Failed, the supplied code and an up/down chevron. The message and action sections render only while expanded.

Raw details follow this source predicate:

| Error record | Expanded raw section |
|---|---|
| code is UNKNOWN_FORMAT or UNPARSEABLE_XDR, rawXdr truthy | Shown with that raw string |
| One of those two codes, rawXdr missing or empty | Shown with N/A |
| Any other code, rawXdr truthy | Shown with that raw string |
| Any other code, rawXdr missing or empty | Omitted |

Matching is exact and case-sensitive. An empty rawXdr string is falsy; the source does not trim or validate nonempty strings. Collapse hides all content sections, including raw details. The field values are JSX text expressions; the component does not declare an HTML injection surface.

The fixed panel labels are English literals. This module does not call useTranslation. It imports its CSS module and five lucide icons; this reference does not copy the stylesheet or certify its rendered geometry, theme behavior or contrast.

## Expansion state and control semantics

The existing header div toggles local isExpanded state on click. It is not a native button and declares no tabIndex, keydown handler, role or aria-expanded. This is a description of current source, not a keyboard-accessibility guarantee or a source correction.

There is no effect or state update that resets expansion when error changes. Returning null for error does not itself remove this component from its parent's tree. If the same component instance remains mounted, replacing or clearing/reintroducing its error prop does not reinitialize the expansion state. The acquired caller renders the panel at a stable unconditional JSX position.

The [React state-preservation explanation](https://react.dev/learn/preserving-and-resetting-state) associates state with a component's position and identity in the rendered tree. A real unmount or identity change is different from this component returning null. These are conditional source semantics; no route or user interaction was executed, and unknown parent remount behavior is not ruled out universally. The acquired page's v19.3 heading is not a repository dependency-version claim.

## Copy behavior

Inside a displayed raw section, Copy is a native type="button" control. Its handler checks rawXdr again. When the value is truthy, it calls navigator.clipboard.writeText with that exact string; otherwise it does nothing. Thus the button can be present next to N/A for an unknown-format code while having no copy action.

The expression uses void and supplies no local await, rejection callback, try/catch, success message, loading state or availability guard. The documentation does not claim successful copying, permission handling or error recovery. It does not request or perform clipboard access.

## Actual source connection

The complete mounted chain is main → App → the /cross-asset-payment route → CrossAssetPayment → ContractErrorPanel. App wraps that route element in its existing ErrorBoundary; the panel is a separate presentation component, not that boundary.

CrossAssetPayment obtains contractError from useContractError and passes it directly. The hook initially stores null, and clearContractError sets null. Its handler can store parser output for a truthy input string, or a generic record when only a truthy fallback message is supplied. When neither input is truthy, the hook leaves the existing state unchanged. These hook branches establish the field connection, not parser correctness or an observed failure.

No API, wallet, signing, payment, event subscription, decoding routine or transaction handler was invoked. Other actions in the caller and the parser's classification rules are outside this component reference. A bounded code search also returned EmployeePortal and PayrollScheduler paths, but those search hits are not a new full caller audit; the generated tsbuildinfo hit was not expanded.

## Immutable source identities

All paths are relative to Protocol-Guild/PayD at the pinned commit.

| Path | Git blob | UTF-8 bytes |
|---|---|---:|
| frontend/src/components/ContractErrorPanel.tsx | 83a0108c600efcea33562edc242d47519fa71e0b | 2619 |
| frontend/src/utils/contractErrorParser.ts | d9fc1a7b4d3260cdc30252ca79b74e701cae2015 | 6014 |
| frontend/src/hooks/useContractError.ts | 95e99ed6ead9fa3757b10d4bf14b420c2dc094c1 | 952 |
| frontend/src/pages/CrossAssetPayment.tsx | 3763b5e348188b36676cc7fdbbccabce7132ea9a | 18295 |
| frontend/src/App.tsx | acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c | 6460 |
| frontend/src/main.tsx | f84f187971ba135010c48e69fda10f0c0f71ebd9 | 1664 |

Original PayD contributors retain credit. See CONTRACT_ERROR_PANEL_SOURCE.md for provenance, license and validation boundaries. This reference is documentation only; it makes no runtime, recovery, clipboard, contract-diagnosis, accessibility, build or complete issue-acceptance claim.
