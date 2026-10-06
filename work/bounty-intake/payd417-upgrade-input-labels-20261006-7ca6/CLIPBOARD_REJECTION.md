# Upgrade transaction-hash copy: rejected Promise feedback

The current upgrade modal's two transaction-hash Copy controls call a helper that attaches only a fulfillment callback to `navigator.clipboard.writeText(text)`. If the returned Promise rejects, the existing success message does not run, but no failure notification is attached. This source continuation adds the existing error notification as the Promise's rejection callback.

## Source and composition

Original source belongs to Protocol-Guild/PayD and its contributors at commit `171c74b454daba241bfb75f36d10a0a3a77a68e5`, path `frontend/src/components/UpgradeConfirmModal.tsx`, original blob `5478483e6ef82ea383b249326b5febc9f106f0f6`. The preceding [Commons #31938](https://github.com/woahwhattheheck/commons/pull/31938) packet supplies only two input-label associations. This packet is a separate small behavior correction found while qualifying that same actual modal, not a claim to complete the broader [issue #417](https://github.com/Protocol-Guild/PayD/issues/417).

Apply the existing `input-labels.patch` first, then this new `clipboard-rejection.patch`:

| Exact path | Composed preimage Git blob | Prepared postimage Git blob | UTF-8 bytes before / after |
|---|---|---|---:|
| `frontend/src/components/UpgradeConfirmModal.tsx` | `e0c8ea028df87b389a7c8256cd17869ac019399c` | `666391673af485089a36692fc049b563d8f40dac` | 35709 / 35824 |

The new source difference is +8/−3 in one complete 17-row hunk. Patch blob `d9f16e43416165b9e3c68dfe01756e038d2382b7`, 925 bytes. The actual serialized patch materializes the exact postimage and reverses to the exact composed preimage. Both previous label associations and every byte outside this copy-helper hunk stay exact.

The [original packet guide](README.md) retains contributor attribution, the current issue's unassigned/request-only discussion, bounded carrier-query limits, complete caller pins and React manifest evidence. This additive packet changes none of those artifacts. The unchanged Apache License 2.0 text remains in [LICENSE](LICENSE), blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64` (11,357 bytes). No complete donor module or actual copied value is published here.

## Actual caller and failure boundary

The already-acquired same-ref caller chain is `frontend/src/App.tsx` at `/admin` → `AdminPanel` contracts tab → `ContractUpgradeTab` → this modal. The component's executing and done branches each call `copyToClipboard` with their transaction hash. Neither passes the password field. This is a source relationship, not evidence of any deployed account, transaction, clipboard value, or permission state.

The success callback keeps `notifySuccess('Copied', 'Copied to clipboard.')`. A second argument to `then` now calls `notifyError('Copy failed', 'Could not copy the transaction hash.')` when the returned write Promise rejects. The fixed message contains no hash, rejection message or other dynamic value.

The [W3C Clipboard API and events working draft, §7.3.4](https://www.w3.org/TR/clipboard-apis/#dom-clipboard-writetext), dated 24 June 2026 in the acquired version, specifies a returned Promise and a rejection path. It is a working draft, not browser execution evidence. No permissions request or clipboard operation was performed while consulting it.

This handler is intentionally limited to the returned Promise's rejection. Missing `navigator.clipboard`, synchronous invocation exceptions, nonconforming implementations, errors thrown by either notification callback, never-settling writes, repeated-click ordering and component lifetime remain outside the result. There is no legacy clipboard fallback or change to copy timing. Fulfillment only selects the existing success callback; this packet does not independently verify operating-system clipboard contents.

## Validation and scope

The new patch uses retained complete source bytes and already-qualified actual callers. Validation is source-contract reasoning, one exact text edit, serialized forward/reverse materialization and independent Git blob identities. No previous accepted patch was executed or revalidated through a browser. No fixtures, simulated Promise sequence, lint, compilation, tests, browser, clipboard, account, credential, contract, signing, upgrade, simulation, API, permission, upstream submission or reward action occurred.

Source state transitions, input values, authorization, contract execution, cancellation policy, polling, transaction-hash display and the prior labels remain unchanged. This packet is not a credential-security review, general error-handling repair, accessibility audit, runtime result or whole-issue acceptance.
