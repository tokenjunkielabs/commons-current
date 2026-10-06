# Close the command palette with Escape from either control

The mounted command palette displays an “Esc close” hint, but its only Escape branch is attached to the search input. Its separate native close button is also focusable and is outside that handler's event ancestry. Moving focus to that button leaves Escape without the promised dismissal behavior.

This patch moves Escape handling to the existing dialog wrapper. The search input and close button are its descendants, so their bubbling Escape events call the existing `close` function. The Escape branch prevents the default action and stops further propagation; it does not let that same event continue to the document-level shortcut dispatcher. Arrow keys and Enter remain owned by the search input.

## Exact source and caller chain

Canonical source is [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Role | Path | Git blob | UTF-8 bytes |
| --- | --- | --- | ---: |
| Before | `src/components/CommandPalette.tsx` | `7e853ba2d07a62202feaee6f29f10ef86631ffad` | 8,547 |
| After | `src/components/CommandPalette.tsx` | `87834bf4cb260ec24495c8df021d3289c4a6de62` | 8,643 |
| Mounted caller | `src/app/[locale]/layout.tsx` | `1f016787657313d58504e79bccbe634a843ce8b5` | 4,212 |
| State owner | `src/contexts/CommandPaletteContext.tsx` | `5ac25e37bdd4edbcd126118747c51168e101548a` | 999 |
| Global shortcut dispatcher | `src/contexts/KeyboardShortcutsContext.tsx` | `e43badc17f6c0e374e0fac5e08a96a5496b87bd7` | 6,274 |
| Default registered actions | `src/lib/keyboard-shortcuts/default-shortcuts.ts` | `a90973724eab2e2c8d735f2abd17b4b4ddc0511f` | 4,739 |

The complete locale layout renders `CommandPalette` inside its actual provider. The complete provider implements `close` as `setIsOpen(false)` and has no key listener. The retained shortcut dispatcher listens on `document`; the complete default actions define no Escape binding. This patch owns Escape locally while the palette is rendered, without changing the dispatcher or assuming a policy for arbitrary custom bindings, earlier capture listeners or separate concurrently opened overlays.

## Change and composition

Apply `dialog-escape.patch` to the pinned donor. The complete patch is **+8/-3 in two hunks**: remove the input-only Escape branch and its now-unused callback dependency, then add the Escape-only handler to the existing `role="dialog"` wrapper. The existing input handler remains attached to the input, so close-button Enter retains its native click behavior and cannot select a command.

Command definitions, navigation destinations, query filtering, selection, open-state reset, delayed initial focus, mouse actions, click-close controls and JSX classes remain byte-for-byte unchanged. The completed notification-target packet #31961 changed the bell target in another component and is unaffected. No shortcut-customizer, theme, help-overlay, chart-export or route-matcher change is included.

The patch supplies this specific dismissal path. It does not implement a focus trap, return-focus policy, new combobox naming, initial-focus timer cleanup, stacked-overlay coordination, complete modal accessibility, browser compatibility or runtime acceptance.

## Primary contracts

- [W3C APG modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) documents Escape dismissal and separately describes focus containment and return focus. This continuation addresses only the dismissal behavior.
- [React: Responding to Events](https://react.dev/learn/responding-to-events), Event propagation and Stopping propagation, explains that handlers receive events from descendants and that `stopPropagation` prevents further propagation. No event example or browser operation was executed.

The existing component and provider, rather than a fabricated interaction response, establish the connected controls and close action.

## Integrity, attribution and limits

Complete retained module and caller inputs were used for this new correction; the newly needed complete provider body independently matched its pinned blob. A full line comparison and serialized forward/inverse reconstruction preserve the exact before/after identities. These are retained-text artifact checks, not application tests. Bounded Commons PR and public Slack searches for CommandPalette/Escape returned zero; this is not a global absence assertion. A fresh native donor main-ref check before publication returned the same pinned commit.

Existing implementation credit remains with the Stellar-Analysis/frontend contributors. This Commons continuation contributes only the scoped patch and original explanation. The complete donor tree has no AGENTS or RULES path. Its retained EventSource-specific contributing note and differently attributed MIT notices do not establish a repository-wide licence for this module; the packet therefore does not redistribute the full module. Current session constraints exclude runtime/tests and publication upstream.

No browser, keyboard, storage, account, telemetry, test, fixture, build or dependency execution occurred. No upstream branch or issue was changed. No contributor assignment, maintainer acceptance, bounty or payment is asserted.
