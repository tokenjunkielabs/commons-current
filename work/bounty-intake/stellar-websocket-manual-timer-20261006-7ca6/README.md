# Cancel a pending manual WebSocket reconnect during disconnect

The dashboard exposes a Reconnect action through its realtime hooks. The acquired `useWebSocket` implementation delays a manual connection attempt by 100 ms but does not retain that timeout's identifier. Its disconnect cleanup can clear the automatic retry timer, while this separate manual timeout remains scheduled. If cleanup runs before that timeout executes, its callback can still call `connect()` afterwards.

This packet retains the manual timeout in its own ref. The existing `disconnect()` path cancels and clears it; the delayed callback clears its ref before starting the connection. A subsequent manual reconnect already calls `disconnect(true)`, so that action also replaces an earlier pending manual timer. The 100 ms delay and connection function remain unchanged.

## Artifacts

- `change.patch`: three source hunks, +10/-1, for `src/hooks/useWebSocket.ts`.
- This guide: actual caller, source identities, limits, attribution and validation record.

This is a Commons source continuation. No upstream source branch, issue claim, account, socket, service, browser, workflow or runtime operation was performed.

## Exact source and caller

Repository: `Stellar-Analysis/frontend`  
Donor commit: `482ee456369418ef82c4056718cb82d3468f762b`

| Role | Path | Git blob | UTF-8 bytes |
| --- | --- | --- | ---: |
| Canonical source | `src/hooks/useWebSocket.ts` | `e34230ffc5e035cc26e5d5715818167d433567c6` | 9,737 |
| Standalone candidate on that canonical source | same path | `810fb14d5e10baaaa99abd8c4fbb6c9e4f4c3624` | 10,082 |
| Actual realtime caller | `src/hooks/useRealtimeAnchors.ts` | `dd2eabb63e3ef68096502ea968325cef18911ef5` | 4,199 |
| Actual dashboard entry | `src/app/[locale]/dashboard/page.tsx` | `cca99335ba0ae1f66a1fb5cea0197f5ead6b2f11` | 13,126 |

The native hooks-directory response at the donor commit established the hook paths, blob identities and byte counts. Complete source strings were then acquired by those exact blob requests and independently hashed. The native blob tool returns content without a separate response SHA field; the provenance is the exact requested immutable locator plus the independent Git blob identity. Dashboard source was acquired by its previously retained immutable locator and independently matched as well.

The dashboard literally imports `useRealtimeAnchors`. Its `WebSocketStatus` reconnect callback calls both `reconnectCorridors()` and `reconnectAnchors()`. The complete anchor hook calls `useWebSocket(wsUrl, ...)` and returns the latter's `reconnect` function. The dashboard and anchor hook are unchanged here.

The source finding is independent from callback identity: this dashboard already memoizes `onAnchorUpdate` using `useCallback([markUpdated])`, and its acquired anchor-hook invocation supplies no `anchorIds`. That separate question was disposed without a patch.

## Demonstrated control flow and correction

1. Existing `reconnect()` invokes `disconnect(true)`, re-enables reconnection, resets the attempt counter, and schedules `connect()` after 100 ms.
2. The original manual `setTimeout` result is discarded. It is distinct from `reconnectTimeoutRef`, which is assigned by the automatic close-handler retry.
3. The main connection effect returns cleanup that invokes `disconnect()`. That function originally clears the automatic retry ref and closes the current socket, but has no handle for the pending manual timer.
4. `connect()` checks its connecting flag and current socket state; it does not inspect `shouldReconnectRef`. Consequently a manual timer that is still pending when cleanup runs can later reach a new connection attempt when the existing guards do not block it.
5. The new `manualReconnectTimeoutRef` stores that timer. `disconnect()` checks it against null, calls `clearTimeout`, and resets it to null. The scheduled callback resets its own ref before calling the unchanged connection function.

The checks and cancellation concern an established timer that has not executed. They do not abort an already started connection, roll back an executed callback, or make a stale externally retained `reconnect` function safe to invoke after unmount.

## Primary contract

[MDN: Window.clearTimeout](https://developer.mozilla.org/en-US/docs/Web/API/Window/clearTimeout) documents cancellation using the identifier returned by `setTimeout`. [React: useEffect](https://react.dev/reference/react/useEffect) documents cleanup before setup with changed dependencies and after removal from the DOM. Both primary documentation pages were read for this new source question. The inferred path above follows the acquired code and these contracts; no browser or React lifecycle was executed.

## Composition boundary

A prior accepted Commons continuation exposes the existing `lastMessageTime` return value in this same module. Its complete postimage did not survive the shared working-cache loss. This packet does not reconstruct that accepted change or claim that the canonical donor contains it.

The published artifact is an independent patch, with hunks confined to the ref declarations, disconnect cleanup and manual reconnect callback. Its contexts do not reach the return object. The candidate identity above describes only this patch applied to the canonical donor. It is **not** a composed-current-module identity. An adopter must retain the accepted return exposure and any other independently accepted changes when applying these isolated hunks.

Completed corridor callback/memoization work, dashboard provenance/deep-copy work and data-refresh lifecycle work are also outside this source scope. No accepted packet or runtime result was replayed.

## Preserved behavior and limits

The connection function and all open/close/error/message handler bytes are unchanged. Send, subscribe, unsubscribe, automatic retry timer ownership, effect bodies, presence fallback, connection status policy and the return suffix are unchanged. The original event handlers, retry-limit behavior, connecting flags, stale-data behavior and the fallback's connection assertions were not assessed as corrected by this patch.

This is cancellation of the pending manual timer through the existing cleanup path. It does not establish global socket teardown, absence of stale socket events, a measured reduction in network requests, backend availability, successful reconnection, authentication, data freshness, or a whole-build/typecheck result.

## Validation and custody

Pure source operations established:

- The complete canonical source, complete caller inputs and standalone candidate identities shown above.
- Exactly three unique replacement sites and three unified-diff hunks, +10/-1.
- Forward application of the actual unified patch exactly reproduces the standalone candidate; reverse application exactly restores the canonical source.
- Connection/handler, send/subscription, effect and return regions remain byte-exact.
- Only this patch and guide are selected for publication. Full upstream modules and private native request/result journals are not included.

No compiler, test suite, fixture, benchmark, shell, app, timer, socket, request endpoint or workflow was run. These are source checks and a bounded control-flow inference, not runtime acceptance.

The new frozen public publication spec is checkpointed with the existing acknowledged-public-blob helper before publication. That checkpoint selects only these two artifacts and public source metadata. Its manifest locator is retained separately in the completion receipt. A blob acknowledgement is not a repository ref or a promise of indefinite object retention.

## Attribution and source instructions

A bounded donor path-history read returned `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, authored by christabel888, describing relocation of the frontend into the repository root. That does not establish sole authorship of the hook.

Retained complete-tree instruction context at this donor found no root AGENTS or RULES file. The original complete array was lost during the shared cache incident, so no new complete-tree census is claimed. The retained `docs/CONTRIBUTING.md` identity is `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` (274 bytes); it is EventSource-specific and requests tests for changes. Upstream acceptance steps remain unperformed in this source-only lane.

Three differently attributed MIT notices are retained separately: `docs/LICENCE.md` (`57740b9d4d86aedf5d518f2f363d5cf192c54127`, 1,104 bytes), `docs/LICENSE.md` (`af5411fa243cfcf2b61c79d081dbb6204e956041`, 1,111 bytes), and `docs/license.md` (`4a766e268772888af5df56c3f6c608f68558b789`, 1,080 bytes). They do not establish one repository-wide licence scope. This packet therefore publishes a narrow patch and explanatory guide rather than complete upstream modules.
