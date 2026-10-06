# Report the outcome of copying an anchor address

The mounted AnchorHeader calls clipboard.writeText directly from its copy button. A rejected Promise has no handler and neither success nor failure produces feedback. This patch waits for the actual result and renders a small local status message for the address involved in that click.

## Actual source and mounting

Canonical source: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), immutable commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/components/anchors/AnchorHeader.tsx` | `2eaa169a9454fa1e1574661258350ed34eee3943` | 4,311 |
| `src/app/[locale]/anchors/[address]/page.tsx` | `71fea1bb40c29bcbba0657ba1cb10a65d35fab23` | 7,297 |
| `src/lib/api/types.ts` | `eb5891a5f04e33eb29757cf57c623f9b7d4ab3b5` | 3,140 |

The client App Router detail page renders AnchorHeader with `anchor={data.anchor}` after its loading and error branches. The declared stellar_account field is a string. The header already handles button events within that client boundary. The previous detail diagnostics patch #32032 changes only optional diagnostic-array rendering and preserves this caller.

The separately retained NotificationContext persists notifications and can play audio or display desktop notifications. This correction intentionally uses component-local state, adding none of those side effects.

## Narrow correction

`report-copy-outcome.patch` changes only this header: **+38/-1 in four hunks**.

Source identity:
`2eaa169a9454fa1e1574661258350ed34eee3943` (4,311 B)
→ `fe8f43aba536dd8a9d3b06e1f6e8752bb7f8a844` (5,488 B).

Each click captures the current address, installs a fresh plain-object request token and clears prior feedback. The existing clipboard call is awaited inside try/catch. A successful fulfillment produces “Address copied.”; a caught access/call failure or rejection produces fixed retry guidance without exposing a raw error or address in the message.

Only the latest click's token may update feedback. Each result also carries its captured address and is rendered only while that address equals the current header address. The ref retains a token, not a clipboard result or external resource. A local paragraph uses role=status; there is no success timer or new fallback clipboard implementation.

[MDN's Clipboard.writeText reference](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard/writeText) states that the returned Promise resolves after the system clipboard is updated, and documents rejection when writing is not allowed. This supports acknowledgement after fulfillment and a handled failure path. No clipboard access or permission prompt was performed during this work.

All address text, the existing copy button's name/title/classes, the external explorer URL and link attributes, status icon/color selection, reliability score and asset coverage remain unchanged. Clicks remain available while a prior request is pending. No address validation, network selection or retry policy is introduced.

## Validation and boundaries

The complete serialized patch reconstructs the full postimage exactly, and its inverse reconstructs the full original source. Independent UTF-8 byte counts and Git blob hashes identify both. This is static source work: no application execution, synthetic event, browser, actual clipboard, permission request, device, fixture or test was used.

The token controls local feedback ordering; it does not cancel or serialize clipboard writes or prove what the clipboard contains after overlapping writes. The address check is an equality guard, not a generation model: same-address ABA, unmount behavior and external clipboard changes remain outside the claim. There is no broader lifecycle, browser compatibility, assistive-technology announcement or whole-accessibility guarantee. Dynamically inserting a status paragraph does not itself establish an observed announcement.

No error notification service or raw clipboard error is published. Browser permission, secure-context availability and the original user-triggered operation remain browser responsibilities. No real account or private/user data was acquired.

## Attribution and publication scope

The bounded current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`. That relocation preserves earlier history; it does not establish sole authorship. Original contributor rights and attribution remain intact.

Scoped current Commons/public Slack queries for AnchorHeader and clipboard returned zero. This is bounded overlap evidence, not a repository-wide completion claim. Root's comparison-page clipboard packet is a distinct component and is preserved.

The complete donor tree had no root AGENTS/RULES paths. Its EventSource-specific contribution/release guidance does not override the session's explicit no-tests/no-runtime/no-upstream scope. Differently attributed documentation MIT notices do not establish repository-wide frontend code licensing; this continuation publishes only a minimal patch and this original attributed guide.

No upstream branch/PR/comment, maintainer assignment, sponsor acceptance, bounty/payment, full issue completion or deployed behavior is claimed.
