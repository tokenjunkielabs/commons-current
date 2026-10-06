# Preserve calendar-day labels in the network charts

## Connected source issue

The Network route mounts five daily-series panels: payment volume, daily active accounts, transaction count, new accounts and fee trends. The acquired network API client accepts date, day or timestamp fields, retains the selected string as date and sorts the series using that original value. It does not restrict every selected string to one date representation.

Each chart currently constructs Date from point.date and formats a month/day label in the host's default time zone. For a valid four-digit ISO date-only input (YYYY-MM-DD), parsing establishes midnight UTC. A host zone behind UTC can therefore display the preceding calendar day rather than the day named by the input.

The patch adds the same narrow formatting option in each chart: a string of exactly ten characters matching four digits, dash, two digits, dash, two digits uses UTC. Other strings use an undefined timeZone option, retaining the existing host-zone formatting. Full timestamps therefore keep their existing interpretation and presentation policy.

This is a source-level correction for a supported string input shape. No live API payload, backend execution or browser incident was captured.

## Complete source inputs and caller chain

Donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/components/charts/PaymentVolumeChart.tsx | 2a80a9912dc883b1e13a6f033de6536a06ecfac7 | 7020 |
| src/components/charts/DailyActiveAccountsChart.tsx | f1d25f7e9ab61215cbc1fea6106e800652039814 | 7018 |
| src/components/charts/TransactionsPerDayChart.tsx | acfd85ddc17b4b3ccc0953159b54b24d532edb38 | 6420 |
| src/components/charts/NewAccountsChart.tsx | ebfa2e116a27fb7dc8367af18592be9d84a992f2 | 6315 |
| src/components/charts/FeeTrendsChart.tsx | a692a23342b2c9199a35621c676aa810cc1a4891 | 6740 |
| src/app/[locale]/network/page.tsx | cfcb9fba468523f2e5069002680a4f4c7c8e4802 | 12424 |
| src/lib/network-api.ts | 1e69005e28fc2187c462b7e68e2db83620a3266a | 12087 |

The route dynamically imports all five chart components and renders each with its corresponding point array and loading state. Its effects call fetchNetworkPaymentVolume, fetchNetworkDailyActiveAccounts, fetchNetworkTransactionsPerDay, fetchNetworkNewAccounts and fetchNetworkFeeTrends. The acquired client normalizers preserve the original selected date string and sort by its parsed time. These complete inputs establish the connection without inferring a deployed or working backend.

The complete five chart bodies independently match their native Git blob IDs. The original source remains attributed to the upstream repository; no sole-author claim is made. The same three complete acquired upstream MIT notices are preserved.

## Date and formatting contracts

The already acquired [ECMAScript 2025 Date.parse algorithm](https://tc39.es/ecma262/2025/multipage/numbers-and-dates.html#sec-date.parse) specifies UTC interpretation for date-only forms without an offset. Its date-time string format includes YYYY-MM-DD.

The already acquired [ECMA-402 CreateDateTimeFormat algorithm](https://tc39.es/ecma402/#sec-createdatetimeformat) uses the system time zone when the timeZone option is undefined. Supplying UTC selects that zone. Consequently the conditional option preserves the existing zone choice for strings outside the selected date-only shape.

These primary contracts were acquired during the earlier liquidity work and retained complete; no failed specification-page request was retried or recovered through another route for this packet.

| Input representation | Formatting zone after this patch |
| --- | --- |
| Valid, exactly ten-character YYYY-MM-DD | UTC, preserving the supplied calendar day |
| Full timestamp, including a time or explicit offset | Existing system-zone formatting |
| Other string representation | Existing system-zone formatting |

The length condition makes the recognizer exactly ten characters; it does not accept an extra trailing line terminator. It is a shape check, not calendar validation. Invalid months/days, expanded-year forms, arbitrary malformed data and non-string runtime payloads remain outside the claim. The patch neither changes Date construction nor adds validation, re-bucketing, truncation, parsing fallback or date normalization.

Labels remain month/day. Year disambiguation, localization changes and a different timestamp time-zone policy are separate decisions. No timezone or date-value calculation was executed as a fixture or experiment.

## Exact serialized changes

| Complete component postimage | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| PaymentVolumeChart.tsx | a5a979eb80d024791f8ea10754034382a30f2887 | 7152 |
| DailyActiveAccountsChart.tsx | daa1e932cf1b1499694d62ab7c874839ed311894 | 7150 |
| TransactionsPerDayChart.tsx | 712ffe58c4ac58705542d8dadde45bfce1b083a1 | 6552 |
| NewAccountsChart.tsx | 0aa1ecd93dfd75445d4c14b5918b848f14b7937b | 6447 |
| FeeTrendsChart.tsx | 8f153108ce0bdf6b5253392f95d21680d10fca46 | 6872 |

The combined calendar-labels.patch is `57b7fc93d4160292321b1d24c50c3abc7d1b6fc9`, 2678 UTF-8 bytes. It contains five hunks and fifty rows, with twenty added lines and no deleted lines: four formatting-option lines in each component.

Each segment of the actual combined serialized patch was applied textually to its complete original input and exactly produced its postimage. Inverse application exactly restored each original. Removing the inserted option reproduces every other source byte. No application Date, date-recognition regexp, Intl or chart operation was executed for these source checks.

Existing API normalization/sorting, numbers, totals, averages, currency/fee formatting, loading/empty branches, plot data, labels, JSX layout, gradients, tooltips, export controls and styles are unchanged. Separate chart-export corrections (#31944, #31949, #31955), LiquidityChart correction (#31978) and TVL correction (#31980) affect other source definitions and are not repeated or modified.

Apply the patch at the exact donor repository root. No package install, compiler, browser, application API request, fixture, tests, workflow, upstream submission or deployment occurred. The checks establish source serialization and contract reasoning, not runtime or whole-build success.

## Notices and publication boundary

| Unchanged notice | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| upstream-licence-mclaughlin.md | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| upstream-license-menke-laguna.md | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| upstream-license-de-wet.md | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |

This is an attributed Commons source proposal, not an upstream change, deployment, acceptance or reward event. The bounded Commons query returned eleven noisy historical rows, not an absence result. Slack returned two headers for already completed chart-export work and native END; their bodies were not reacquired. Internal custody checks retained no same-hunk date-label completion or hold. None of these observations establishes a global search census or query fidelity.

Publication requires complete immutable bodies, native and independently calculated identities for all five artifacts, plus final PR/files/merge/main metadata. The preselected equality alias may reuse those immutable bodies only when the observed main commit exactly equals the verified merge. Otherwise each artifact is read once at the observed immutable main pin. Actual evidence is recorded separately in the release and grouped index.
