# Match the theme provider's first render before restoring preferences

The mounted theme button derives its icon, title and accessible label from ThemeContext. The original provider initializes from browser storage during render, but returns `system` on the server. A saved light or dark preference therefore produces different first-render button content during hydration. System color-scheme resolution can also give the initial context a different resolved theme than the server's dark fallback.

This patch keeps the existing server fallback for both initial renders, then restores and applies the supported browser preference in the provider's existing mount effect. It changes only `src/contexts/ThemeContext.tsx`.

## Pinned source and attribution

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), commit `482ee456369418ef82c4056718cb82d3468f762b`. Original contributor ownership, assignments and upstream acceptance remain unchanged. This Commons packet is a minimal attributed source patch with an original guide, not an upstream contribution or full-feature acceptance claim.

| Source | Git blob | Role |
| --- | --- | --- |
| `src/contexts/ThemeContext.tsx` | `2c5d5fd59feb0d24c2d675b9e4ac97e6df6537ea` | Changed initialization and mount effect |
| `src/components/ThemeToggle.tsx` | `15e9de53dccb18ea312282e2e01bcfc77d04e64a` | Direct icon/title/label consumer |
| `src/components/navbar.tsx` | `1d519697311060e2d72c1a8fcaa59d1eb6148277` | Renders ThemeToggle |
| `src/app/[locale]/layout.tsx` | `1f016787657313d58504e79bccbe634a843ce8b5` | Async server layout mounts provider and navbar |
| `src/app/layout.tsx` | `d99613766c48f2be30014720edd01dc156d58696` | Server HTML uses the dark class |

The complete actual mount chain was inspected, including the provider wrappers between the locale layout and Navbar. UserPreferencesContext `1f22b6a9354ebacf502df2472ddeb24e0006a4e6`, KeyboardShortcutsContext `e43badc17f6c0e374e0fac5e08a96a5496b87bd7`, CommandPaletteContext `5ac25e37bdd4edbcd126118747c51168e101548a`, WalletProvider `cb3e12aa4d3b87adc1fd1b67492510abb3361867`, NotificationContext `8a05dbf6fb720af3f876baef6b14f035d02b6c51`, StateProvider `5c5e7d7f021bf5e072278a5161d04b0dcbf257d7` and its ReactQueryProvider `e82f8d817df30c321b96c599bf117005a432346e` return their children without a client-only mounting gate. ErrorBoundary `ec97514a6b8b690aaaddbaae3406d00286f65765` starts without an error and normally returns children. No wallet, storage, network or backend operation was performed while reading this public source.

## Source contract and correction

The original `getSavedPreference` accepts exactly dark, light or system and catches storage errors. On the server it returns system. The original lazy state initializer calls that function during render; the second initializer resolves the preference with matchMedia in a browser or dark on the server. ThemeToggle immediately selects its icon and text from that preference.

The two-hunk patch (+8/-5) makes the initial preference system and the initial resolved theme dark in both environments. The existing mount effect reads `getSavedPreference`, resolves that value, updates both states, and applies the resolved class/data attribute through the existing helper. The old dependency-suppression comment is unnecessary because this effect no longer reads the rendered preference state.

The restoration effect does not call the persistence setter or write the fallback to storage. Validation, storage exception handling, the storage key, the explicit click setter, system-preference listener and cross-tab listener remain exact. ThemeToggle cycle order, labels, icons, animation and markup are untouched. There is no reset/removal policy, cookie, inline script, no-SSR wrapper or new theme schema.

Official [Next.js Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) documents that client components participate in initial HTML prerendering and are hydrated on first load. The ['use client' directive alone](https://nextjs.org/docs/app/getting-started/server-and-client-components) therefore does not make this render-time storage difference safe.

The official [React hydrateRoot reference](https://react.dev/reference/react-dom/client/hydrateRoot) requires matching initial output and describes an effect-based second render for client-dependent content. It also limits suppression to one level; the root layout's html/body suppression does not resolve the deeply nested button discrepancy. These are primary-source contracts, not observed browser results.

## Composition, integrity and limits

Apply `restore-theme-after-hydration.patch` to the pinned context. Original blob `2c5d5fd59feb0d24c2d675b9e4ac97e6df6537ea` is 4142 UTF-8 bytes; postimage `359b7b678d2081938e2520f27eb54b2062734629` is 4235 bytes. Every serialized hunk is included. Forward reconstruction equals the full postimage, and inverse reconstruction equals the original full source, with native and independent blob identities matching. These are source-text checks, not executed component tests.

Completed UserPreferences appearance/customizer work concerns a different context and remains protected. Navbar first-link, sidebar offset, language, notification, PWA and shortcut changes are not modified. The only bounded ThemeContext/hydration history match was Commons #31755 for the distinct Protocol-Guild/PayD repository, explicitly excluding hydration; no accepted source from it was reopened.

This deliberately adds a post-hydration render. A saved choice may become visible after the initial system/dark presentation; eliminating every theme flash is not claimed. The existing browser matchMedia assumption, cross-tab removal handling, other providers' hydration behavior and unrelated compile/runtime issues remain outside scope. The change does not establish complete application hydration success.

The complete donor tree exposed no AGENTS/RULES path. Retained docs/CONTRIBUTING.md `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` is EventSource release guidance; current task restrictions exclude tests/runtime/package publication. Differently attributed MIT notices under docs do not establish a repository-wide license, so this packet does not republish full modules.

No tests, fixtures, browser, saved-preference access, runtime, build, dependency installation, account/device/wallet/payment operation, upstream submission, sponsor acceptance, bounty award or payout was performed.
