# Restore Asset detail modal state on cleanup

This packet contains two incremental corrections to the mounted AssetDetailModal: restore the prior inline overflow value and return focus to the previously focused connected HTML element. Each patch preserves the existing opening, Escape, Tab-loop and callback behavior.

## Immutable source and actual caller

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/components/anchors/AssetDetailModal.tsx` | `dcab1bf692c77dbf8eec93682612d8e364ceb9a4` | 9,160 |
| `src/components/anchors/AssetPortfolio.tsx` | `1801c67028bb96c8b69c8c6d23f47ba45ad0a920` | 6,015 |
| `src/components/anchors/IssuedAssetsTable.tsx` | `1c650ade062e90d3a0e2dda834f5a396659fe5db` | 4,885 |
| `src/app/[locale]/anchors/[address]/page.tsx` | `71fea1bb40c29bcbba0657ba1cb10a65d35fab23` | 7,297 |

The actual detail App Router page renders AssetPortfolio. The portfolio passes setSelectedAsset to IssuedAssetsTable and renders AssetDetailModal with that selection plus a callback which clears it. Clearing the selection leaves the table mounted and makes the modal return null.

The modal effect returns early without an asset. Otherwise it finds its first/last focusable elements, moves focus to the first control, installs its existing keyboard listener and applies the body scroll lock. Its existing dependency list is asset and onClose.

[Commons #32045](https://github.com/woahwhattheheck/commons/pull/32045) separately adds a native asset-name button to the table; its source postimage is `821eca456b8cc09ca9f96963cd100bf9be519be1` (5,498 B). Keyboard activation therefore establishes a concrete focused opener for this modal. That table patch remains separate, and the modal does not depend on a particular opener ID or table implementation.

The [detail diagnostics #32032](https://github.com/woahwhattheheck/commons/pull/32032) and [portfolio export-anchor #32039](https://github.com/woahwhattheheck/commons/pull/32039) corrections preserve this caller chain.

## Apply the incremental patches in order

1. `restore-modal-overflow.patch`, completed in [Commons #32042](https://github.com/woahwhattheheck/commons/pull/32042), captures the body inline overflow string immediately before hidden and restores it instead of assigning literal unset. **+2/-1**, source `dcab1bf692c77dbf8eec93682612d8e364ceb9a4` (9,160 B) → `1a0749b9dd958c3cee76346d48991a97253d24fa` (9,228 B).
2. `restore-opener-focus.patch` applies to that exact postimage. It captures document.activeElement immediately before the existing initial focus call. After removing the key listener and restoring overflow in the existing cleanup, it calls focus only when the saved element is an HTMLElement and remains connected. **+7/-0 in two hunks**, source `1a0749b9dd958c3cee76346d48991a97253d24fa` (9,228 B) → `01088959d0952b489b5378e71efdb3a061350983` (9,464 B).

The second patch uses the retained complete first postimage as input to a new source correction. It does not rerun the first change or replace its artifact. Listener setup/removal, overflow capture/restoration, keyboard logic, initial focus, dependencies and all JSX remain exact outside the new focus capture/return lines.

Each setup captures its own target for the associated cleanup. Cleanup can also run when the existing dependencies cause setup replacement or on unmount; the new check skips disconnected targets. It does not select an alternate destination when the opener disappeared.

## Primary behavior contracts

[MDN's HTMLElement.style reference](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) documents inline property values and empty-string reset. The overflow patch therefore restores a previously absent inline declaration without leaving unset behind.

The [W3C APG button pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/) describes moving focus into an opened dialog and typically returning it to the invoking button when closed. [MDN's Node.isConnected reference](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected) defines the connection check used before attempting return. These support the source correction; no actual focus or DOM operation was performed.

The previous focus target need not be the opener for every pointer/browser interaction. The patch restores only the captured, connected HTML target. Being connected does not guarantee that an element remains enabled, visible or focusable. No fallback target, cross-document target, nested/stacked-modal ownership, exit-animation policy or whole-dialog accessibility guarantee is added. Cleanup focus may still be affected by other components or browser policy.

The overflow correction remains property-value restoration only: no global lock manager, concurrent external-write arbitration, arbitrary declaration-priority/longhand preservation or replacement-body handling is claimed. Existing fixed IDs, rate badges and other modal behavior remain separate.

## Validation and attribution

Serialized forward and inverse reconstruction of the new patch match its complete composed preimage/postimage and independently calculated Git blob identities. No React render, browser/keyboard operation, synthetic event, fixture, test or build was executed.

Bounded current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`; original contributors retain credit and rights, with no sole-author inference. Original overflow overlap queries returned zero. The subsequent exact AssetDetailModal/focus Commons and public Slack queries returned only the already-known #32042 overflow packet, which expressly left focus unchanged. No completed source/proof was revalidated.

The retained complete donor tree has no root AGENTS/RULES path. EventSource-specific CONTRIBUTING guidance does not override the explicit session no-tests/no-runtime/no-upstream scope. Differently attributed documentation MIT notices do not establish repository-wide code licensing, so the packet contains only minimal patches and this original attributed guide.

No live asset/account data, API request, upstream branch/PR/comment, author assignment, sponsor acceptance, bounty/payment or whole-issue completion was performed or claimed.
