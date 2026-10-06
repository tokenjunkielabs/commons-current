# Skip nullish rows without discarding the network series

## Connected failure path

The acquired network API module accepts unknown response data. Each of its five normalizers chooses an array from the direct response or its points, series or data property, then maps the rows. Inside each map, it casts the current row to a record-shaped TypeScript type and immediately reads item.date, item.day or item.timestamp.

There is no nullish-row guard before that property access. A null element in an otherwise useful array therefore throws before the normalizer can reach its existing invalid-point filter. The corresponding fetch function calls normalization inside its try block; its catch returns an empty points array. A single such row can discard all otherwise usable observations for that panel.

The Network route calls those five functions and passes their returned points to the five mounted charts. This establishes the connected effect of the failure from complete source. It does not claim that a live backend response containing null was observed or that a browser incident was reproduced.

## Exact complete inputs

Donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/lib/network-api.ts | 1e69005e28fc2187c462b7e68e2db83620a3266a | 12087 |
| src/app/[locale]/network/page.tsx | cfcb9fba468523f2e5069002680a4f4c7c8e4802 | 12424 |

Both complete source bodies are retained. The API module independently matches its native blob. All five connected chart bodies were also acquired for the preceding calendar-label proposal; this packet does not modify or republish them.

Current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888. A relocation is not sole-authorship evidence. The upstream source attribution and complete acquired MIT notices remain preserved.

| Normalizer | Connected fetch function |
| --- | --- |
| normalizePaymentVolumePoints | fetchNetworkPaymentVolume |
| normalizeDailyActiveAccountsPoints | fetchNetworkDailyActiveAccounts |
| normalizeTransactionsPerDayPoints | fetchNetworkTransactionsPerDay |
| normalizeNewAccountsPoints | fetchNetworkNewAccounts |
| normalizeFeeTrendPoints | fetchNetworkFeeTrends |

## Minimal change and supporting contract

At the beginning of each existing row callback, the patch adds:

```ts
if (row == null) return null;
```

The [TypeScript narrowing handbook](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#equality-narrowing) documents that equality with null also matches undefined. This guard selects those two absent values before record access. It does not use truthiness to broaden the rejection condition.

The [TypeScript type-assertion documentation](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) explains that an as assertion is removed during compilation and adds no runtime checking. The existing cast therefore does not protect that property read. The inserted guard supplies the missing runtime condition.

Every normalizer already returns null for unusable points and removes null results with its existing point != null filter. The new early return uses that established path. For ordinary non-nullish rows, the original record access, aliases, numeric checks, output objects, filter and ordering execute unchanged.

| Selected row | Result of this narrow change |
| --- | --- |
| null or undefined | Return null before property access; existing filter omits it |
| Ordinary non-nullish row | Continue through the original callback unchanged |
| Other malformed data or a later throwing operation | Existing behavior and fetch catch remain unchanged |

This table records source reasoning, not an executed fixture suite. The patch does not introduce a full record schema, finite-number validation, date validation, getter/proxy defenses or an all-input success guarantee.

## Serialized source checks

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Complete preimage | 1e69005e28fc2187c462b7e68e2db83620a3266a | 12087 |
| Complete postimage | d49d36486646208f544197465e39f5883c4ca2c2 | 12267 |
| nullish-rows.patch | 73adabac75efd8fdd44775096cbfcaea01a24bc1 | 972 |

The actual serialized unified patch has five hunks and thirty-five rows, with five additions and no deletions. Forward text application exactly produced the complete postimage. Inverse application exactly restored the preimage. Removing the five inserted guards restores every other source byte.

All wrapper-array selection, aliases, numeric checks, date comparison/sorting, endpoint paths, days parameters, response shapes, currency unit, request options, error logging and catch behavior remain unchanged. No new dependency, exported function, shared helper or retry is introduced. The separate #31985 chart-label proposal changes components, not this module.

Apply nullish-rows.patch at the donor repository root to the exact preimage. No normalizer invocation, application fetch, live response acquisition, Date/sort execution, compiler, browser, package installation, fixture, tests or workflow was performed. These checks establish source serialization and guarded control flow, not runtime or whole-build success.

## Notices and publication boundary

| Unchanged notice | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| upstream-licence-mclaughlin.md | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| upstream-license-menke-laguna.md | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| upstream-license-de-wet.md | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |

This is an attributed Commons source proposal, not an upstream change, deployment, acceptance or reward event. Bounded exact-name Commons and Slack queries returned zero rows, with native END for Slack. Internal custody checks retained no same-hunk completion or hold. These results do not establish global absence, source ownership clearance or query fidelity.

Publication requires complete immutable bodies and native plus independent blob identities for all five artifacts, followed by exact final PR/files/merge/main metadata. The preselected main-equals-merge alias can reuse those bodies only if the observed commit is exactly equal. Otherwise each file is read once at the observed immutable main pin. Actual verification is recorded separately in the release and grouped index.
