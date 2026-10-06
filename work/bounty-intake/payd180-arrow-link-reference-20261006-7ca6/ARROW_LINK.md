# ArrowLink component reference

Source: `frontend/src/components/ArrowLink.tsx` at Protocol-Guild/PayD commit `171c74b454daba241bfb75f36d10a0a3a77a68e5`. This reference describes that exact source version. It covers one existing component, not the entire design system.

ArrowLink is a secondary call to action with caller-supplied content and a trailing right-arrow icon. Its public API chooses between a React Router link, a native anchor, and a native button.

## Props

| Prop | Source type | Meaning |
| --- | --- | --- |
| children | React.ReactNode, required | Content rendered before the decorative arrow. Supply meaningful visible text. |
| className | string, optional | Appended to the existing link-arrow class; defaults to the empty string. |
| to | string, mutually exclusive branch | Destination passed to React Router Link when nonempty. |
| href | string, mutually exclusive branch | Destination passed to an anchor when nonempty. |
| onClick | () => void, mutually exclusive branch | Callback attached to the native button branch. |

The union uses optional `never` properties to exclude the other two mode props in each typed branch. It is not a runtime validator. The actual branch order is a truthy `to`, then a truthy `href`, then a button. In particular, an empty destination string falls through instead of producing a link; supply a nonempty destination.

The component does not extend general anchor or button props. It does not forward arbitrary attributes from the rest object. There is no supported disabled, loading, target, download, aria-label, tabIndex, ref, or router replace prop in this API. If a caller needs those behaviors, a separate component change is required; passing extra JSX props should not be treated as a supported workaround.

## Rendered branches

| Mode | Element selected by source | Details |
| --- | --- | --- |
| Nonempty to | Imported React Router Link | Receives only to, className and children. Use within the application's router context. |
| Nonempty href | Native a | Receives href, className and children. Strings matching the exact case-sensitive /^https?:\\/\\// expression also receive target="_blank" and rel="noopener noreferrer". |
| onClick branch | Native button | Has type="button", the callback, className and children. It is not a submit button. |

The external-link check is only the literal prefix test shown above. Protocol-relative links, other schemes and differently cased prefixes do not receive those extra target/rel attributes from this component. There is no URL validation, allowlist, destination check, or navigation-success guarantee. Treat destinations as caller-controlled input requiring the caller's own policy.

The action callback is typed with no required event argument. The source passes it directly to the button; it does not await a result, catch exceptions, add a pending state, or prevent repeated activation.

## Existing mounted usage

The acquired `frontend/src/pages/Home.tsx` imports ArrowLink. Its existing hero secondary action is:

```tsx
<ArrowLink to="/employee">{t('home.ctaViewEmployees')}</ArrowLink>
```

The feature cards use the same component with an additional class string:

```tsx
<ArrowLink to={f.to} className="text-sm self-start">
  {t('home.learnMore')}
</ArrowLink>
```

The actual feature destinations in that source are /payroll, /employee and /transactions. The complete App source mounts Home at /. The retained entry source places App inside BrowserRouter and imports index.css. These are source relationships, not results from visiting those routes.

Only the to mode is established in the acquired production caller. The href and onClick modes are exported source capabilities, not separately established mounted uses. The following snippets illustrate those existing branches; they were not executed:

```tsx
<ArrowLink href="https://example.org/guide">
  Read the guide (opens in a new tab)
</ArrowLink>

<ArrowLink onClick={openDetails}>View details</ArrowLink>
```

In the second snippet, openDetails is a callback supplied by the consuming component. The snippet does not add an implementation for it. Import ArrowLink using the relative path appropriate to that caller.

## Styling and accessibility considerations

The class list is the trimmed concatenation of link-arrow and the optional className. The acquired index.css defines inline-flex alignment, a 0.375rem gap, weight 600 and the --link text color. Hover changes color and translates the SVG by 3px; dark-theme hover uses a separate text token. There is no size or visual-variant prop. Additional class behavior still depends on the stylesheet and cascade.

The arrow is rendered with aria-hidden="true" and is decorative. Meaningful visible children should describe the destination or action; do not rely on the arrow alone to name the control. Use navigation modes for destinations and the button mode for an action. A link that opens another tab should say so in its content when that information is needed. The wrapper does not add that notice itself.

MDN's native button and anchor references support those basic element distinctions. They do not establish this application's measured focus behavior, contrast, layout, assistive-technology output, router version behavior, or accessibility compliance:
- https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button
- https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a

No browser, keyboard, screen reader, router navigation, click handler, build, compiler or test was run for this reference. The examples are documentation, not verified runtime demonstrations. No component code or styles are changed.
