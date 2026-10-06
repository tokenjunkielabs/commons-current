# ThemeToggle component reference

Reference for the existing PayD implementation at `171c74b454daba241bfb75f36d10a0a3a77a68e5`. This documents the current component and its provider; it does not change them.

## Public surface

`frontend/src/components/ThemeToggle.tsx` exports ThemeToggle as its default export. It declares no component props and does not forward arbitrary attributes to its button. There is no component-level className, disabled, icon, onClick, storage-key or initial-theme option.

`frontend/src/hooks/useTheme.ts` exports:

| Export | Source contract |
|---|---|
| Theme | The two literal strings light and dark |
| ThemeContextType | theme: Theme; toggleTheme: () => void |
| ThemeContext | React context whose default value is undefined |
| useTheme | Reads that context with React use and returns its value; throws when no value is available |

`frontend/src/providers/ThemeProvider.tsx` exports the named ThemeProvider component, which accepts children: React.ReactNode. The application's existing root already supplies this provider. Consumers under that root can use the component directly:

```tsx
import ThemeToggle from '../components/ThemeToggle';

export function AppearanceControl() {
  return <ThemeToggle />;
}
```

This is an illustrative source snippet, not a compiled or executed example. The import assumes a sibling-directory layout like a module in frontend/src/pages. It relies on the existing provider above it; it does not create another provider or install a handler.

## State-to-control mapping

| Current context theme | Rendered icon | Button aria-label | Existing activation result |
|---|---|---|---|
| dark | Sun | Switch to light mode | Functional state update selects light |
| light | Moon | Switch to dark mode | Functional state update selects dark |

ThemeToggle passes toggleTheme directly to onClick. The provider callback is created with useCallback and an empty dependency list, and uses a functional state updater. There is no public direct setTheme function or three-state system mode in this API.

The button's label describes its target mode. The label text is currently English and does not call the translation system. No aria-pressed state is declared. Its icon classes are w-4 h-4; the existing component classes supply padding, border, colors, hover styles and transitions. These are source declarations, not measurements or a screen-reader result.

## Initial value and persistence

The provider uses the fixed storage key `payd-theme`. Its lazy initializer reads localStorage synchronously. Exactly light and dark are accepted; a missing or other stored value selects light. The code does not inspect matchMedia or another operating-system preference.

After the theme state is committed, the existing effect sets the document element's data-theme attribute and writes the current value to localStorage. The effect also runs for the initial theme, so a successfully executed first effect writes the selected light/dark value even when the old stored value was missing or invalid.

Neither the initial read nor the effect's write is wrapped in a local try/catch. There is no availability guard for localStorage or document. This reference does not promise behavior when browser storage is denied, unavailable or throws, or in server rendering. It also does not promise that no visual transition occurs before the effect applies data-theme.

No storage event or matchMedia listener is installed by this provider. Another tab changing the key is not a declared synchronization mechanism here. Multiple provider instances would own separate React states while targeting the same global document attribute/storage key; the established application uses the root provider rather than adding a second one for each button.

## Actual application placement

The complete source chain is:

1. frontend/src/main.tsx wraps the application in ThemeProvider and later BrowserRouter.
2. frontend/src/App.tsx installs EmployerLayout as the surrounding route element.
3. frontend/src/components/EmployerLayout.tsx renders DashboardTopBar above its Outlet.
4. frontend/src/components/DashboardTopBar.tsx renders ThemeToggle in its control group.
5. ThemeToggle reads useTheme and invokes the provider callback.

This is source-qualified mounting, not an executed route traversal. Other unrelated provider, account and sidebar behavior in those modules is outside this reference.

The acquired stylesheet contains data-theme='light' and data-theme='dark' variable definitions, including the background, surface and text variables used by the component and layout. The main entry imports that stylesheet. This establishes the intended variable connection; it does not prove that every third-party widget or hard-coded color follows the theme.

## Form and interaction boundary

The current ThemeToggle button does not specify a type attribute and does not accept props that could add one. Its qualified DashboardTopBar placement is not inside a form in the acquired caller chain. Do not describe this unchanged component as universally safe to insert into arbitrary forms: native button behavior can submit an associated form when type is omitted.

The [MDN button reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button) describes native keyboard activation and the significance of an explicit button type. This is an API explanation, not validation of the application's focus styling, keyboard shortcuts, contrast or accessibility as a whole.

The [React use reference](https://react.dev/reference/react/use) describes reading the nearest matching provider's context value. The acquired documentation currently identifies itself as v19.3; that page is not an assertion about the repository's installed package version or compiler output. The concrete local context type, default and missing-provider error above come from the acquired PayD source.

## Source identities

All paths are relative to Protocol-Guild/PayD at the pinned commit.

| Path | Git blob | UTF-8 bytes |
|---|---|---:|
| frontend/src/components/ThemeToggle.tsx | `84f2d166c9c47e0e0c1d45b9ae2f60b31d4f090f` | 607 |
| frontend/src/hooks/useTheme.ts | `de6886fb2b68d3a4ed88566f658310128bf96fa5` | 420 |
| frontend/src/providers/ThemeProvider.tsx | `7263c212046dc5ddfb881d8f7d122c43e1903043` | 827 |
| frontend/src/components/DashboardTopBar.tsx | `617350d5649d30be44a2a01c1776d69870edd840` | 1603 |
| frontend/src/components/EmployerLayout.tsx | `5cd117fcdaf260873f1e9f8655787857a3288ca2` | 3061 |
| frontend/src/main.tsx | `f84f187971ba135010c48e69fda10f0c0f71ebd9` | 1664 |
| frontend/src/App.tsx | `acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c` | 6460 |
| frontend/src/index.css | `91a759763e2d95a56274460685978f2a024c3b53` | 8054 |

Original PayD contributors retain credit. See the accompanying THEME_TOGGLE_SOURCE.md for acquisition, carrier, license and validation limits. No component, storage operation, theme toggle, browser, compiler or test was executed to produce this reference.
