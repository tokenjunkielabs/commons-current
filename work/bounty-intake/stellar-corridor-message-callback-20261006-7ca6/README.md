# Stable corridor WebSocket message callback

The mounted corridor detail route passes three inline callbacks to `useRealtimeCorridors`. The hook currently makes `handleMessage` depend on those callback identities. The acquired `useWebSocket` makes its connection callback depend on `onMessage`, and its connection effect invokes `disconnect()` during cleanup when that dependency changes. The existing connection-entry guards do not prevent this cleanup from closing the held socket.

This patch uses the already-imported `useStableCallback` for `handleMessage` and removes the now-inapplicable dependency-array argument. The complete message handler body remains byte-exact. This addresses the callback-identity cleanup trigger without changing the socket implementation or subscription protocol.

## Exact acquired source

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).

Donor commit: `482ee456369418ef82c4056718cb82d3468f762b`.

| Source | Git blob | UTF-8 bytes | Provenance |
| --- | --- | ---: | --- |
| `src/hooks/useRealtimeCorridors.ts`, patch preimage | `e7c2a3e42b08f1c7de1135395712b450d3fb2353` | 6,787 | Complete retained root transfer, independently hashed in this lane |
| Same hook, new postimage | `e63c937a5ace270ac131b50ec27c09d90f3a3043` | 6,719 | Two exact edits, +1/-2 |
| `src/hooks/useStableCallback.ts` | `1d76106d3973298b7ac66959a70a5db54bfa372e` | 809 | Previously acquired complete native blob, retained identity and full source used as this new implementation input |
| `src/hooks/useWebSocket.ts` | `e34230ffc5e035cc26e5d5715818167d433567c6` | 9,737 | Complete immutable native source from the directly preceding caller qualification, with native and independent identity |
| `src/app/[locale]/corridors/[pair]/page.tsx`, original donor caller | `ee5a60a83df1abcd0a5b3c156edb551bba5f83b2` | 18,485 | Complete native blob acquired for the preceding distinct caller patch |
| Same caller after Commons #32004 and #32008 | `1517325bfad37ae5b7abc112a713870a4ed2b956` | 18,719 | Retained exact source composition; all three inline callbacks remain |

Native blob acquisition supplies content without a separate returned SHA; those inputs are identified by their explicit request-bound blob and independent Git identity. This packet does not invent a returned identity field.

Only `src/hooks/useRealtimeCorridors.ts` is changed by `change.patch`. Both its preimage and postimage retain their final newline. The existing `useCallback` import remains needed by the separate subscribe, unsubscribe, and alert-clear callbacks. The existing `useStableCallback` import is reused, so no import, dependency, lockfile, or helper change is required.

## Concrete effect path

The actual route supplies new `onCorridorUpdate`, `onHealthAlert`, and `onNewPayment` function objects during render. Before this patch:

1. The realtime hook's `handleMessage` is recreated when those functions change.
2. That function is passed as `onMessage` to the acquired socket hook.
3. The socket hook's `connect` callback includes `onMessage` in its dependencies.
4. Its effect depends on `connect` and `disconnect`; a changed `connect` causes the previous effect cleanup.
5. `disconnect()` clears the retry timeout and, when a socket reference exists, calls `close()` and clears the reference.

The presence-state guard in `disconnect` occurs after the close/null operations. It changes whether UI connection state is reset; it does not prevent socket teardown. The early connected/connecting guards are inside `connect`, not around effect cleanup.

React's primary [useEffect reference](https://react.dev/reference/react/useEffect) documents dependency comparison using `Object.is` and cleanup followed by setup after a commit with changed dependencies. This supports the static identity-path finding. No browser, socket, or network measurement was used.

## Existing stable-callback contract

The acquired utility keeps the supplied function in a ref, assigns that ref during each render, and returns an empty-dependency `useCallback` wrapper that forwards its arguments and return value to the ref's current function. It is already used in this realtime hook for socket open, close, error, and stale-data callbacks.

The new wrapper therefore delegates to the latest-rendered message-handler closure under that existing utility's behavior. The message parameter union, map/list state updates, list bounds, optional caller callbacks, payment-stream condition, subscription-confirmation logging, ping handling, and unknown-message logging remain byte-exact. A change to a handler input can be read through the updated ref without making that input alone a connection-effect identity dependency.

This is deliberately a latest-rendered description. The utility writes its ref during render; this packet does not change that design, claim latest-committed semantics, or establish a concurrent-render guarantee. Ordinary hook-cache retention is not a universal never-changing identity promise.

## Relationship to prior work and limits

[Commons #32004](https://github.com/woahwhattheheck/commons/pull/32004) preserves explicit zero values in two score updates. [Commons #32008](https://github.com/woahwhattheheck/commons/pull/32008) memoizes the caller's key array. Those completed changes are retained, distinct source inputs; their accepted checks and publication were not replayed. The present patch targets a different file and does not require replacing the caller or reapplying its changes.

No subscription-set deduplication, reconnect policy, disconnect implementation, retry guard, URL selection, presence fallback, state reporting, or callback utility is rewritten. Manual reconnects, genuine URL/dependency changes, unmounts, development setup cycles, and other lifecycle causes remain. Enabling the payment stream still affects the existing subscription callbacks through their own dependencies.

The source establishes an avoidable callback-identity cleanup path, not a successful reconnection count per render. A new connection still depends on the existing guards, lifecycle timing, events, and backend availability. There is no claim about measured connection counts, server effects, traffic volume, latency, general socket reliability, or whole-application performance.

## Validation and attribution

The full retained caller, realtime hook, socket hook, and stable-callback implementation were read for this new source integration. Exact replacement reversal verifies that only the wrapper name and one dependency line change; a separate exact comparison verifies the full message-handler body is unchanged. Git blob identities and UTF-8 byte counts bind the actual preimage, postimage, and artifacts.

No application, callback invocation, WebSocket, subscription, benchmark, compiler, lint, test, fixture, build, workflow, or executor was run. Runtime acceptance and upstream integration remain unperformed.

Root supplied the acquired realtime-hook text and the new mounted-caller finding. CI supplied the socket locator during the preceding qualification. Those are source-custody contributions, not new ownership or approval gates. No repository-wide license scope was established by the differently attributed notices; this deliverable is patch plus guide rather than complete donor-module republication. Existing notice attribution remains in [the prior generator packet](../stellaranalysis-issue-generator-layout-20261006-7ca6/). No upstream claim, payment, account, or permission action is part of this packet.
