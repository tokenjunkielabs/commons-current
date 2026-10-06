# Make the registered theme shortcut toggle light and dark

The registered toggle-theme action describes switching between light and dark. Its initializer reads the resolved theme, whose type has only those two values, but routes the light branch to the system preference. When the system resolves to light, that action need not change the visible theme and can continue selecting system. The initializer's three-mode comment conflicts with the actual registered shortcut description and cannot make the resolved theme report system.

This patch implements the registered binary shortcut contract. It changes the branch to dark when the current resolved theme is light, and corrects the adjacent comment. The separate three-mode ThemeToggle remains available and unchanged.

## Exact source and attribution

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at `482ee456369418ef82c4056718cb82d3468f762b`. Fresh main-ref qualification returned that same commit. Original authors, assignments, acceptance and economic rights are preserved; this is a minimal Commons continuation without an upstream submission or a complete theming claim.

| Actual source | Git blob | Role |
| --- | --- | --- |
| `src/components/keyboard-shortcuts/ShortcutsInitializer.tsx` | `105911230a83d5a480a2601a124956a8d34c1dfe` | Registered handler, 2,485 bytes |
| `src/lib/keyboard-shortcuts/default-shortcuts.ts` | `a90973724eab2e2c8d735f2abd17b4b4ddc0511f` | toggle-theme description and binding |
| `src/contexts/KeyboardShortcutsContext.tsx` | `e43badc17f6c0e374e0fac5e08a96a5496b87bd7` | Actual matching and action dispatch |
| `src/contexts/ThemeContext.tsx` | `2c5d5fd59feb0d24c2d675b9e4ac97e6df6537ea` | Resolved Theme and separate ThemePreference contract |
| `src/components/ThemeToggle.tsx` | `15e9de53dccb18ea312282e2e01bcfc77d04e64a` | Separate system/light/dark preference control |
| `src/app/[locale]/layout.tsx` | `1f016787657313d58504e79bccbe634a843ce8b5` | Mounts ThemeProvider, KeyboardShortcutsProvider and initializer |

Complete acquired/retained modules supply the contract. No runtime state or operating-system preference was sampled. The default registry's description says “Switch between light and dark theme”; the initializer's old comment instead claims a dark/light/system cycle. The patch resolves that inconsistency in favor of the registered action contract. It does not change the three-mode button's distinct ordering.

The provider distinguishes Theme ('dark' or 'light') from ThemePreference ('dark', 'light' or 'system'). Its setter persists the selected preference and resolves/applies the theme. The completed [theme hydration packet #31957](https://github.com/woahwhattheheck/commons/pull/31957), provider postimage `359b7b678d2081938e2520f27eb54b2062734629` (4,235 bytes), preserves those APIs and remains unchanged.

## Patch and composition

Apply `toggle-resolved-theme.patch` to the initializer preimage above. Its complete postimage is `14c78a8be9811c80ee6ac521a040ec6a3e1e4a7a`, 2,465 bytes. The single source hunk is +2/-2, including one comment line.

The handler now selects light for resolved dark and dark otherwise under the existing two-value Theme contract, then calls the same setter. Selecting an explicit mode through this shortcut leaves system-following mode, as expected for its binary action. Users can still select system using the untouched ThemeToggle control.

Every shortcut binding, action ID/name/description, platform override, enabled check, input-focus exclusion, preventDefault behavior, registration, effect dependency, navigation/sidebar/notification/refresh handler and provider persistence implementation remains exact. ShortcutCustomizer's completed reset/binding edits and notification command-target correction remain protected. No shortcut registry or theme provider mutation is included.

The serialized patch reconstructs the complete postimage and reverses to the complete preimage. These are source text-integrity operations, not keyboard events or component tests. Exact public ShortcutsInitializer/theme history returned zero/native END; the bounded Commons PR query returned zero/incomplete_results:false. Those observations are not global absence claims.

The retained complete donor tree has no AGENTS/RULES path. Its EventSource-specific docs/CONTRIBUTING.md `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` does not override the current no-tests/no-runtime/no-package-publication boundary. Differently attributed docs notices do not establish a repository-wide license; only this minimal diff and original guide are republished.

## Limits

The system-light case is a consequence of the acquired type and branch logic, not an observed OS/browser result. No keyboard, browser, media query, storage, saved preference, user data, runtime, build, test, fixture, device, account/payment or upstream operation was performed. No rapid-repeat scheduling, operating-system shortcut conflict, malformed preference, full hydration or whole-build/accessibility guarantee is asserted.
