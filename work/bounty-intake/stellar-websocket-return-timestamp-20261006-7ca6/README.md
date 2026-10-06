# Return the existing WebSocket timestamp state

The acquired `useWebSocket` function explicitly returns `UseWebSocketReturn`. That interface requires `lastMessageTime: number | null`, and the function already declares state with that name, but the returned object omits it.

This patch adds the existing `lastMessageTime` value to that object. It repairs the required return member with one added line. It does not implement timestamp production: the complete acquired module initializes this state to `null` and never invokes its setter, so the newly exposed value remains `null` under the current implementation.

## Source and identity

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).

Donor commit: `482ee456369418ef82c4056718cb82d3468f762b`.

| Input or output | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/hooks/useWebSocket.ts`, acquired preimage | `e34230ffc5e035cc26e5d5715818167d433567c6` | 9,737 |
| Same file, proposed postimage | `b4450f479b44151ed1a375b5128b5018f96d5663` | 9,758 |
| Acquired caller `src/hooks/useRealtimeCorridors.ts` | `e7c2a3e42b08f1c7de1135395712b450d3fb2353` | 6,787 |
| Original mounted route `src/app/[locale]/corridors/[pair]/page.tsx` | `ee5a60a83df1abcd0a5b3c156edb551bba5f83b2` | 18,485 |

The socket source was acquired completely as an immutable native Git blob for the preceding corridor source integration and retained as input to this separate contract correction. Its explicit request-bound SHA and independently computed Git blob identity match. That blob endpoint returns content without a separate response SHA; no additional native identity field is claimed. The realtime hook was transferred completely from root custody and independently hashed; the route was acquired completely and independently hashed during the earlier distinct caller work. No accepted source operation or publication was rerun.

`change.patch` changes only `src/hooks/useWebSocket.ts`, with +1/-0. Both source images have a final newline. Removing exactly the added line restores the complete acquired preimage; all other source bytes are unchanged.

## Explicit contract and connected caller

The interface declares a required property, without an optional-property question mark. The function's return type is explicitly annotated with that interface. The original object contains the other declared members but omits `lastMessageTime`. The local state already has the declared `number | null` type.

TypeScript's primary [Type Compatibility handbook](https://www.typescriptlang.org/docs/handbook/type-compatibility.html) explains that structural compatibility requires the target's members and compatible types; its function-return example likewise rejects a result missing a required member. The [Everyday Types handbook](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html) documents return annotations and the question-mark syntax for optional properties. These contracts support the source-level diagnosis. No compiler diagnostic was produced or invented.

The actual `useRealtimeCorridors` implementation imports and invokes this explicitly typed socket hook. The actual App Router corridor detail page invokes the realtime hook. This establishes a connected source path rather than an unused filename assumption. The acquired realtime caller destructures connection state and socket operations; it does not consume `lastMessageTime`. This packet therefore does not claim a timestamp display, a downstream timestamp calculation, or a demonstrated runtime consumer of the new property.

## Behavior deliberately left unresolved

The existing state initialization is `useState<number | null>(null)`. In the complete original socket source, the timestamp name occurs only in the interface and state declaration; `setLastMessageTime` has no invocation. The patch adds the return occurrence only. It does not turn `null` into an observed message time, choose a clock, infer a last-message arrival, or make freshness reporting complete.

Message parsing, `setLastMessage`, caller invocation, stale-data timers, reconnect decisions, presence fallback, socket cleanup, subscriptions, and the public interface declaration remain byte-exact. Existing unused-state-setter or other compiler/lint issues are not resolved by this one-line change. No whole-build, connection, reliability, freshness, or performance result is claimed.

[Commons #32008](https://github.com/woahwhattheheck/commons/pull/32008) changes the caller's key-array identity, and [Commons #32015](https://github.com/woahwhattheheck/commons/pull/32015) changes the realtime message callback wrapper. Both touch different files and remain separate completed continuations. This patch neither replaces their source nor depends on rerunning their checks.

## Delivery and validation boundary

Validation consists of complete retained source inspection, primary contract review, an exact one-line source transformation, its exact reversal, and Git blob/UTF-8 identities. No hook or message handler was invoked; no compiler, typecheck, lint, application, WebSocket, test, fixture, build, workflow, or executor was run. Integration and runtime acceptance remain unperformed.

The deliverable is a focused patch plus this guide. A repository-wide license scope was not established by the differently attributed notices, so the full donor module is not republished. Existing notice attribution remains in [the prior generator packet](../stellaranalysis-issue-generator-layout-20261006-7ca6/). Source-custody transfers and prior work are credited as evidence, not exclusive ownership or approval gates. There is no upstream submission, claim, account, payment, or permission action in this packet.
