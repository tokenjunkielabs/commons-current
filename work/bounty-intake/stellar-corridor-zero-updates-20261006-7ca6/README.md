# Preserve zero scores in corridor detail updates

## Connected failure

CorridorDetailPage passes an onCorridorUpdate callback to useRealtimeCorridors. For an existing matching corridor, the callback copies the current data and updates success_rate and health_score using incomingValue || previousValue. Numeric zero therefore leaves the previous score in place instead of updating the displayed value.

The page renders the resulting success rate, health score and health color. This is a source-level stale-value path for a matching zero-valued update, not a claim that a live socket delivered such a message.

The complete hook uses isCorridorUpdate before storing and forwarding a message to this callback. The acquired parser requires success_rate to have JavaScript number type, which includes zero. The hook's CorridorUpdate interface additionally declares health_score?: number; the underlying parser does not validate that optional extra field. This distinction limits the scope of any validation claim.

## Exact complete sources

Donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/app/[locale]/corridors/[pair]/page.tsx | ee5a60a83df1abcd0a5b3c156edb551bba5f83b2 | 18485 |
| src/hooks/useRealtimeCorridors.ts | e7c2a3e42b08f1c7de1135395712b450d3fb2353 | 6787 |
| src/lib/websocket-message-parser.ts | cb85ffafb4f1856736cef6b534208433ba99655a | 6757 |

All three complete source bodies match their native and independently calculated Git blob identities. The page is an existing App Router corridor-detail entry and is also the destination of the already-acquired liquidity heatmap corridor links.

Current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888. That relocation does not establish sole authorship. Original source attribution and three complete acquired MIT notices are preserved.

## Deliberately narrow value selection

For each of the two numeric fields, the patch adds an explicit zero branch around the original fallback:

```ts
update.success_rate === 0
  ? update.success_rate
  : update.success_rate || updatedData.corridor.success_rate
```

The health_score expression has the same structure. For ordinary record values, incoming numeric zero is retained; every other value continues through the original logical-OR expression.

The [official TypeScript 3.7 documentation](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html#nullish-coalescing) explains the zero-value pitfall of logical-OR defaults and the broader distinction between falsy and nullish values. This patch selects zero explicitly, preserving the existing treatment of other falsy values rather than changing that separate input behavior.

| Incoming value for the selected field | Result |
| --- | --- |
| Numeric zero, including negative zero | Use the incoming numeric zero |
| Other truthy value | Use the incoming value, as before |
| Other falsy value, including absent/null or NaN | Use the existing score, as before |

This table describes source control flow for ordinary data values, not an executed fixture suite. Existing malformed truthy values remain outside any guarantee; the patch adds no range checks or schema validation. Accessor/proxy side effects are not a promised equivalence domain.

## Exact patch checks

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Complete preimage | ee5a60a83df1abcd0a5b3c156edb551bba5f83b2 | 18485 |
| Complete postimage | 45724baef4ac084737cc578088f0273356411ff7 | 18641 |
| preserve-zero-scores.patch | 3abad28a38e5d168a1828f622634ee197889f70c | 890 |

The actual unified patch has one hunk and fifteen rows, with six additions and two deletions. Serialized forward application exactly reconstructs the postimage; inverse application exactly restores the preimage. Reversing the two expression replacements restores every other page byte.

The existing matching-corridor guard, state copy, timestamp fallback, last-update scheduling, WebSocket subscription behavior, API/mock fallback, history arrays, payment stream, alerts, navigation and UI markup remain unchanged. The hook and message parser are not modified. No historical percentages or payment counts are recomputed.

Apply preserve-zero-scores.patch at the donor repository root to the exact page preimage. No callback, state update, WebSocket, API request, parser, compiler, browser, fixture, tests or workflow was executed. Text checks establish the source selection and serialization, not live delivery, runtime rendering, message ordering or whole-build success.

## Notices and publication boundary

| Unchanged notice | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| upstream-licence-mclaughlin.md | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| upstream-license-menke-laguna.md | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| upstream-license-de-wet.md | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |

Bounded exact-component/zero-scope Commons and Slack queries returned zero results, with native END for Slack. Internal custody retained no exact same-hunk correction or hold. These observations are not global absence, ownership, acceptance or reward clearance.

This is an attributed Commons source proposal with no upstream mutation or deployment. Publication verification requires five complete immutable artifact bodies, native plus independent identities and final PR/files/merge/main metadata. Only an exact observed main-equals-merge identity permits reusing the immutable reads; otherwise every artifact is read once at the observed immutable main pin. Actual publication checks are recorded separately in the release and grouped index.
