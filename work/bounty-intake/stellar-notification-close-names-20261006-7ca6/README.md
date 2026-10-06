# Name the existing notification close controls

The mounted Notification Center and Notification Preferences panels each expose a close button using only a symbol. The center button contains an X icon; the preferences button contains the multiplication sign. Neither source button declares an action name. This patch supplies explicit names for those two existing actions.

## Source and attribution

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at `482ee456369418ef82c4056718cb82d3468f762b`. A fresh native main-ref guard returned that same commit before publication. This Commons continuation preserves the original contributors, assignments, external acceptance and economic rights. It is a minimal source patch and original guide, not an upstream submission or a complete notification/accessibility implementation.

The actual locale layout `src/app/[locale]/layout.tsx`, blob `1f016787657313d58504e79bccbe634a843ce8b5` (4,212 UTF-8 bytes), mounts the Navbar and notification context. The full acquired Navbar, blob `1d519697311060e2d72c1a8fcaa59d1eb6148277` (6,182 bytes), renders NotificationBell. Its original source blob is `8e17fc08741d51bda9d0b3169a4b563fd528e89b` (2,774 bytes); it owns the open/close state and renders these panels.

The completed [command-target continuation #31961](https://github.com/woahwhattheheck/commons/pull/31961) and [preference draft-lifetime continuation #31965](https://github.com/woahwhattheheck/commons/pull/31965) remain unchanged. In the latter composition, preferences unmount on close and reinitialize on reopening. This naming patch changes neither that lifetime nor the panel callbacks.

| Module | Original donor blob | Patch preimage | Postimage | Postimage bytes |
| --- | --- | --- | --- | ---: |
| `src/components/notifications/NotificationCenter/NotificationCenter.tsx` | `0cd01f490a82263a5961f4567d62931ae3ffd186` | `f9f8f1ccb1d7219d0de6f5141a81ad4355f5cf1a` | `dd307adefe2360465081730aee9675430060678d` | 9045 |
| `src/components/notifications/NotificationPreferences.tsx` | `fd1482e38a34d706b675e6a2038e57101e4a3ffc` | `e0de0893d29d4a546b6e4a103fa7e55abc4b68a7` | `eb9c925042f78ecd2429d3a8a5c5e14ef31f482e` | 16947 |

The center preimage is the complete 8,990-byte postimage of [#31943](https://github.com/woahwhattheheck/commons/pull/31943), retaining its selection membership correction. The preferences preimage is the complete 16,889-byte postimage of [#31941](https://github.com/woahwhattheheck/commons/pull/31941), which already composes the test-sound resource correction from [#31937](https://github.com/woahwhattheheck/commons/pull/31937). Retained complete source strings supplied these inputs; no omitted module or snippet was reconstructed.

## Correction and primary contract

Apply `name-notification-close-buttons.patch` after those stated preimages. It adds only:

- `aria-label="Close notification center"` to the existing center close button.
- `aria-label="Close notification preferences"` to the existing preferences close button.

The primary [W3C ARIA Authoring Practices button pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/) documents that a button has an accessible name and that aria-label can provide it. The existing native button role and action are retained. The labels use the same English language as the acquired panel headings and surrounding action text; this is not a localization system change.

Both existing onClick={onClose} expressions, symbol children, classes, animation wrappers, backdrop callbacks, other controls and all state/persistence logic remain byte-for-byte unchanged. No new button, event listener, focus command, close path, confirmation or permission condition is introduced. The preferences Cancel and Save controls are untouched.

## Integrity and scope

The serialized patch has two hunks, +2/-0. Each complete forward reconstruction matches its stated postimage and each inverse reconstructs the complete preimage. These are text-integrity operations, not executed component tests. The source modules and any browser storage or notification content were not executed or inspected as user data.

The exact public NotificationCenter/close history search returned zero/native END. A bounded Commons PR query returned two closed, unrelated historical proof headers; their bodies were not expanded. These bounded observations do not prove repository-wide absence of another contribution.

The retained complete donor tree exposed no AGENTS/RULES path. Its EventSource-specific `docs/CONTRIBUTING.md` at `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` does not override the current explicit no-tests/no-runtime/no-package-publication scope. Differently attributed MIT notices under docs do not establish a repository-wide licensing scope. Only this minimal diff and original guide are republished.

This packet establishes explicit source-level names for two existing controls. It does not establish screen-reader or browser results, focus trapping/restoration, Escape handling, modal semantics, translated labels, keyboard coverage or whole-feature accessibility conformance. There was no runtime, test, fixture, build, browser, assistive-technology, notification, audio, storage, account/payment, upstream submission, bounty claim or acceptance action.
