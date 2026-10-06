# Corridor detail subscription-key memoization

The mounted corridor detail route constructs a fresh one-element `corridorKeys` array on every render. The acquired realtime hook includes that array in its subscription effect dependencies. Its acquired WebSocket consumer does not compare channel selections: each subscription call reaches its send path. This patch memoizes the route's key array by `corridorPair`, reducing effect retriggers attributable only to a newly allocated array while React retains the memo.

This is a source-only continuation. It supplies a narrow patch and this guide; it does not deploy the application or assert measured network, rendering, or server behavior.

## Exact source and composition

Canonical repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).

Pinned donor commit: `482ee456369418ef82c4056718cb82d3468f762b`.

| Source | Git blob | UTF-8 bytes | Custody |
| --- | --- | ---: | --- |
| `src/app/[locale]/corridors/[pair]/page.tsx`, original donor | `ee5a60a83df1abcd0a5b3c156edb551bba5f83b2` | 18,485 | Full native blob read for this new caller change, independently hashed |
| Same page after inherited Commons #32004 | `45724baef4ac084737cc578088f0273356411ff7` | 18,641 | Exact composition of the original page with the two accepted score-selection changes |
| Same page after this patch | `1517325bfad37ae5b7abc112a713870a4ed2b956` | 18,719 | New source postimage |
| `src/hooks/useRealtimeCorridors.ts` | `e7c2a3e42b08f1c7de1135395712b450d3fb2353` | 6,787 | Complete retained source transfer from root, independently hashed in this lane |
| `src/hooks/useWebSocket.ts` | `e34230ffc5e035cc26e5d5715818167d433567c6` | 9,737 | Complete native file read at the pinned donor; returned and independently computed identities agree |

The native blob response for the original page supplies content without a separate returned SHA. Its identity is bound to the explicit requested blob and the independently computed Git blob hash; a returned SHA is not invented.

Apply `change.patch` to the page with the exact #32004 postimage above. The inherited [Commons #32004](https://github.com/woahwhattheheck/commons/pull/32004) changes only the `success_rate` and `health_score` fallback selections so an explicit zero is retained. Those two changes were composed as source input and their combined postimage matched exactly. They are not repeated in this new diff and their accepted execution or verification was not replayed. The upstream page at the donor pin remains the original source, so this packet does not claim #32004 is deployed upstream.

Both the inherited and new complete page retain the original absence of a final newline. The unified patch changes only three locations: the React import, one top-level memo declaration, and the `corridorKeys` option. Its source delta is **+6/-2**.

## Acquired caller and consumer

The actual App Router entry is the page named above. It derives `corridorPair` from `useParams()` and invokes `useRealtimeCorridors` with payment streaming enabled. This patch preserves the existing singleton-or-empty array values and the existing route-parameter assumption.

The realtime hook's subscription effect depends on `isConnected`, `corridorKeys`, and `subscribeToCorridors`. For a nonempty selection while connected, the callback stores the supplied keys for reconnect handling, constructs the corridor channel list plus payment channels, and calls `subscribe`.

The acquired WebSocket hook's `subscribe` callback passes a subscribe message to its stable `send` callback. When the underlying socket is open, that callback serializes and sends the message; otherwise it issues its existing warning. No channel-list equality check or subscription-set deduplication is present on this path.

The new declaration uses `useMemo(() => (corridorPair ? [corridorPair] : []), [corridorPair])`. With the same pair and a retained memo, unrelated committed rerenders do not change this dependency merely by allocating another array. A changed pair still produces the corresponding new selection.

## React contract and boundaries

Primary references read for this source assessment:

- [React useEffect](https://react.dev/reference/react/useEffect): changed dependencies are compared with `Object.is` and cause the effect to run after a commit.
- [React useMemo](https://react.dev/reference/react/useMemo): an unchanged dependency can reuse the cached calculation result. The cache is a performance optimization and can be discarded; it is not a semantic guarantee.

No socket-level deduplication is introduced. Reconnect subscriptions, manual subscribe/unsubscribe behavior, channel ordering, payment-channel inclusion, message parsing, and stable socket callbacks keep their existing implementation.

The page also supplies inline update, alert, and payment callbacks. The realtime hook's message handler depends on them, and the WebSocket connection callback depends on that message handler. This existing callback-identity path is unchanged. This packet therefore does not claim to eliminate socket reconnects, all resubscriptions, Strict Mode setup work, or cache-discard effects. It addresses the array-identity trigger only.

The WebSocket hook's existing presence fallback, connection-state reporting, warning behavior, and missing-backend policy remain outside scope. Server-side subscription idempotence and production traffic were not observed. There is no measured latency, bandwidth, request-count, or whole-application performance claim.

## Attribution and validation scope

Root supplied the current complete realtime-hook input, the accepted #32004 composition contract, and the bounded page-history observation. That history returned the relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, authored by `christabel888`, with the message about flattening the frontend into the repository root. This is relocation attribution, not proof of sole authorship or an exhaustive history. CI supplied the retained WebSocket tree locator; its source was then acquired once for this new assessment.

Validation consists of full source reading, exact source composition, Git blob/UTF-8 identity comparisons, and preservation of bytes outside the three new edits. No application, WebSocket, network subscription, API request from the application, benchmark, compiler, lint, test, fixture, browser, build, or workflow was executed. Hosted acceptance and upstream integration remain unperformed.

The repository-wide license scope is not established by the separately observed MIT notices. The Commons deliverable is patch plus guide, without republication of complete donor modules. Existing notice attribution remains in [the prior generator packet](../stellaranalysis-issue-generator-layout-20261006-7ca6/). No upstream claim, submission, payment, account, or permission action is part of this continuation.
