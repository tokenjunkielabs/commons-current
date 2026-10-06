# Name notification preference switches and expose their draft state

The mounted Notification Preferences panel renders on/off controls as native buttons containing only empty visual track spans. Their nearby visible labels are separate elements with no association, and the buttons have no accessible name or checked-state property. This incremental source correction adds those semantics while keeping the existing click handlers and save flow.

## Composition and source ownership

Original repository and donor: https://github.com/Stellar-Analysis/frontend at `482ee456369418ef82c4056718cb82d3468f762b`.

Apply this packet's existing `close-test-sound-context.patch` from [Commons #31937](https://github.com/woahwhattheheck/commons/pull/31937) first, then `named-preference-switches.patch`. The second patch intentionally uses the complete retained postimage of the first as input; no completed audio behavior was re-executed or revalidated. The audio cleanup bytes are preserved by this new patch.

| Source stage | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Upstream NotificationPreferences.tsx | `fd1482e38a34d706b675e6a2038e57101e4a3ffc` | 15,996 |
| After #31937; this patch's preimage | `083079fe5bf4cb532dd614b6ae9a95594ae21af6` | 16,207 |
| After named-preference-switches.patch | `e0de0893d29d4a546b6e4a103fa7e55abc4b68a7` | 16,889 |

Production path: `src/components/notifications/NotificationPreferences.tsx`, mode 100644; the original absence of a final newline is preserved.

Original Stellar-Analysis contributors retain credit and ownership. This is a separate narrow Commons continuation, not an upstream submission, accepted accessibility audit, assigned bounty completion or payment claim. A new bounded public search for NotificationPreferences plus aria returned zero; the retained repository notification-title search was also empty. Those are limited chronology observations, not global absence guarantees.

## Actual mounted control contract

The source path is mounted through the already acquired Navbar `1d519697311060e2d72c1a8fcaa59d1eb6148277`, notification barrel `812d23234012d75770a798e7ad4f6c7be77b1e58`, and NotificationBell `8e17fc08741d51bda9d0b3169a4b563fd528e89b`. The full panel supplies the visible labels, draft booleans, toggle handlers and Save Changes callback. The retained locale layout mounts that Navbar and provider.

| Existing visible control | Added accessible name | aria-checked value |
| --- | --- | --- |
| Enable Notifications | Enable Notifications | `localPreferences.enabled` |
| Desktop Notifications | Desktop Notifications | `localPreferences.showOnDesktop` |
| Auto Hide | Auto Hide | `localPreferences.autoHide` |
| Enable Sound | Enable Sound | `localPreferences.sound.enabled` |
| Each mapped category | Existing `category` label string | Existing mapped `enabled` boolean |

All five JSX sites gain `role="switch"`, `aria-label` and `aria-checked`, +15/-0 across five hunks. The current four category keys produce four category switches. Their accessible names use the same category strings as their visible text; capitalization remains presentation styling.

The role/state reflect the current editable draft, not a false claim that an unsaved preference is already persisted. Existing handlers update the same draft values, and the existing Save Changes control remains responsible for committing them. Labels remain stable when their values change.

## Primary contract

The [W3C WAI-ARIA Authoring Practices switch pattern](https://www.w3.org/WAI/ARIA/apg/patterns/switch/) describes binary on/off controls with a stable accessible label, switch role and boolean aria-checked state. It explicitly permits aria-label and includes a native-button switch example. This change retains native buttons and their existing click handlers; it does not add custom keyboard interception.

This supplies individual control names and states only. Group labels/descriptions, range/select associations, modal focus/escape behavior, the close button, broader keyboard handling, contrast and screen-reader/browser compatibility have not been completed or tested by this patch. No whole-page or whole-modal accessibility compliance claim is made.

## Integrity and operational limits

The complete source input and output, each literal insertion and its inverse, and every serialized unified hunk reconstruct the stated identities. These are string/source integrity checks. No application/component execution, synthetic fixture, compiler/lint/test run, browser, screen reader, notification permission, sound, storage or account operation was performed.

Toggle handlers, state setters, Save/Reset/Cancel behavior, permission decisions, styling, test-sound cleanup, notification renderer and shared sound hook remain byte-exact outside the inserted properties. Compose with newer source instead of replacing a newer file.

The existing packet's README retains the original source/API/ownership context. Its donor instruction assessment still applies: no AGENTS.md or RULES.md in the retained complete tree; the observed EventSource-specific contributing document is not this workflow. Current session forbids runtime/tests/upstream publication. Documentation MIT notices with different attribution do not establish repo-wide licensing for this production component, so only this focused patch and original guide are distributed here.
