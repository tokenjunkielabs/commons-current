# Notification commands and preference draft lifetime

The mounted command palette and registered notification shortcut both look up `[data-notification-button]` and click the matching button. The actual NotificationBell button has the handler that opens NotificationCenter, but lacks that attribute. This patch adds the existing selector's target to that button.

## Source and attribution

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), commit `482ee456369418ef82c4056718cb82d3468f762b`. Original authors, assignments, upstream acceptance and economic rights are unchanged. This is an attributed Commons source continuation, not an upstream submission or a whole-feature acceptance claim.

| Path | Original Git blob | Role |
| --- | --- | --- |
| `src/components/notifications/NotificationBell.tsx` | `8e17fc08741d51bda9d0b3169a4b563fd528e89b` | Changed target button |
| `src/components/CommandPalette.tsx` | `7e853ba2d07a62202feaee6f29f10ef86631ffad` | Open Notifications command |
| `src/components/keyboard-shortcuts/ShortcutsInitializer.tsx` | `105911230a83d5a480a2601a124956a8d34c1dfe` | Registers the notification callback |
| `src/lib/keyboard-shortcuts/default-shortcuts.ts` | `a90973724eab2e2c8d735f2abd17b4b4ddc0511f` | Connects the default key binding to that callback |
| `src/contexts/KeyboardShortcutsContext.tsx` | `e43badc17f6c0e374e0fac5e08a96a5496b87bd7` | Registration and key handler |
| `src/components/navbar.tsx` | `1d519697311060e2d72c1a8fcaa59d1eb6148277` | Renders NotificationBell |
| `src/app/[locale]/layout.tsx` | `1f016787657313d58504e79bccbe634a843ce8b5` | Mounts the palette, initializer and navbar under the providers |

These complete source files were inspected. The palette closes before calling its command action. The initializer supplies the notification callback to createDefaultShortcuts and registers the returned shortcuts; the default notification shortcut uses that callback. NotificationBell opens its existing NotificationCenter through showHistory. The shared locale layout establishes these as connected application components.

## Correction

The sole hunk adds `data-notification-button=""` to the main notification bell button. Its existing onClick, accessible label, unread badge, visual classes, showHistory state, settings button and both modal props remain byte-for-byte unchanged. Neither caller nor any key binding is changed.

The [MDN querySelector reference](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) specifies first-match lookup and null when no match exists. Its [attribute selector reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors) specifies that a presence selector matches an explicitly present attribute. The empty string therefore supplies the exact existing selector contract. This is source reasoning; no document, button or keyboard event was executed.

## Application and checks

Apply `notification-command-target.patch` to the pinned NotificationBell. Original blob `8e17fc08741d51bda9d0b3169a4b563fd528e89b` is 2774 UTF-8 bytes; postimage `83466559bfd5732401ada835e2ee2f23e6780c00` is 2812 bytes. The patch has one hunk, +1/-0. Its complete serialized forward reconstruction matches the full postimage, and its inverse reconstructs the original native blob exactly. These are text-integrity checks, not component or browser tests.

A bounded exact public Slack phrase search and a Commons repository PR phrase query for data-notification-button returned zero results; the latter reported incomplete_results:false. That is bounded overlap evidence, not a global absence claim. Completed notification selection, read timestamps, CSV, preferences and sound changes remain protected in their separate packets.

The existing document-wide first-match convention is retained. Multiple mounted bell instances, custom key conflicts, browser-reserved shortcuts, palette focus behavior, modal accessibility and unrelated compile/runtime defects are outside this patch. The mounted StateProvider's separately observed duplicate export was addressed in [Commons #31962](https://github.com/woahwhattheheck/commons/pull/31962); these Bell changes do not establish whole-application build success.

The complete donor tree contained no AGENTS/RULES path. Retained docs/CONTRIBUTING.md `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` describes EventSource testing/release steps; current instructions exclude runtime/tests/package publication. Differently attributed MIT notices under docs do not establish repository-wide licensing, so this packet contains only a minimal patch and this original guide.

No runtime, tests, fixtures, browser, keyboard/device action, user data, account, wallet/payment operation, upstream submission, sponsor acceptance, award or payout was performed.

## Additive continuation: discard the cancelled preference draft

NotificationBell originally rendered NotificationPreferences at all times, passing false while closed. The complete panel at `src/components/notifications/NotificationPreferences.tsx`, native blob `fd1482e38a34d706b675e6a2038e57101e4a3ffc`, initializes localPreferences from provider preferences and hasChanges to false. Returning null for isOpen=false does not remove that component from the parent's tree. Cancel, the close control and backdrop call only onClose. Consequently an unsaved draft remains after Cancel, and provider changes while the panel is hidden do not reinitialize that draft.

The actual Reset Changes handler copies current provider preferences into the draft; Save Changes writes that draft and clears hasChanges without closing. These separate explicit controls establish the saved-versus-draft contract. The provider can also update preferences when notification permission is denied or through the retained storage hook's cross-tab event. No permission, storage or browser action was performed to inspect this source.

The additional patch makes Bell render the existing panel only while showPreferences is true. All panel props and close callbacks remain the same. Closing removes the component and discards its local draft; reopening creates it from then-current provider preferences with hasChanges=false. Saving stays open exactly as before. It does not add an effect that would overwrite a draft while the user is editing.

The primary [React preserving and resetting state guide](https://react.dev/learn/preserving-and-resetting-state) documents that state belongs to a component's position in the tree: retaining that component preserves state, removing it discards state, and adding it again initializes state anew. This source-level mounting correction uses that documented lifecycle.

Apply `reset-preferences-on-reopen.patch` after `notification-command-target.patch`:

| Composed state | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Completed command-target postimage | `83466559bfd5732401ada835e2ee2f23e6780c00` | 2812 |
| Additional conditional panel mount | `0e03799201779f68a4e87ef1f70f98e7a1cae1d4` | 2857 |

This one-hunk continuation is +6/-4, including JSX indentation. Both serialized directions reconstruct their complete expected source strings. The command target and NotificationCenter mounting stay exact. The original command patch artifact is unchanged.

The panel's completed Test Sound cleanup (#31937) and accessible switches (#31941) are in a different file and remain untouched. Their composed full panel postimage is `e0de0893d29d4a546b6e4a103fa7e55abc4b68a7`. Its initialization and close/save/reset handlers remain the source contract above, and it has no required hidden-panel effect. An already-started test tone still owns its existing ended cleanup; closing the panel is not audio cancellation or rollback.

A precise public showPreferences search returned zero/native END, and a bounded Commons PR query for NotificationPreferences plus draft returned zero/incomplete_results:false. A broader public Slack query returned twenty header previews and a continuation; it was not exhausted and is not claimed complete. Known own packets and unrelated external publication/contract topics were excluded without body expansion.

Cross-tab/provider changes while the panel is already open, persistence failure semantics, focus restoration, transition timing and modal accessibility remain outside this correction. No runtime, tests, component rendering, browser, permission prompt, audio, account action or upstream acceptance is claimed.
