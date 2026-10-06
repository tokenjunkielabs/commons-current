# Preserve date-only labels in the Soroban daily-event chart

## User-visible defect and correction

The mounted Soroban ContractCallsChart converts each supplied point.date with new Date(point.date) and formats its label through toLocaleDateString("en-US", { month: "short", day: "numeric" }). The API accepts date, day and timestamp aliases and preserves the selected date value. The chart describes the series as daily event counts.

For valid four-digit ISO date-only strings, parsing uses UTC midnight. Formatting that instant in a host zone behind UTC can display the preceding calendar day. The daily bucket's visible label then disagrees with its supplied date. This is a source-based inference from the actual caller and documented date contracts; no application date value or formatter was executed.

The six-line insertion adds timeZone: "UTC" only when the supplied value is a string, has exactly ten characters, and has the YYYY-MM-DD digit/hyphen shape. Other values use timeZone: undefined, retaining the default-zone behavior. Full timestamps therefore keep the existing interpretation and presentation.

The existing English locale, short month and numeric day remain unchanged. No helper, dependency, date parser or new data field is introduced.

## Exact scope and limits

This patch changes one formatting option in one actual component. The original date and count fields in chartData remain exact. API aliases, filtering and sorting are unchanged. Period total, peak, latest count, chart configuration, event-versus-transaction wording, export binding and all rendered markup remain exact.

The prior #32129 unavailable-data prop and branch remain intact. A failed request still renders its unavailable message rather than a successful-empty statement. Loading and empty branches are unchanged.

The recognition expression is a shape check, not calendar validation. It does not validate month/day ranges, repair impossible dates or normalize arbitrary timestamp strings. It deliberately excludes expanded years, incomplete dates, whitespace and full timestamp strings. Their previous formatting behavior remains outside this correction. It does not establish backend completeness, date ordering, valid counts or a runtime integration result.

## Actual source and custody

The complete chart preimage is the retained postimage from [#32129](https://github.com/woahwhattheheck/commons/pull/32129), not a reconstruction from its patch or summary. Its original canonical source was acquired at [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) commit 482ee456369418ef82c4056718cb82d3468f762b.

| Source | Preimage | Bytes | Postimage | Bytes |
| --- | --- | ---: | --- | ---: |
| src/components/charts/ContractCallsChart.tsx | d36e06e5ff150e852e5f982f309ae86a5856861e | 6668 | ceb784684589b3d10787d5035bd8ae080405f7fd | 6850 |

The complete retained current API source is a3ba6bc1f13ec89d31191d18550e8bb0b584b407, 9226 UTF-8 bytes; it selects item.date ?? item.day ?? item.timestamp and returns that date in each accepted point. The complete retained current Soroban page is 80ba478b5aa34d8af463ea4a5c6f969eeca114fa, 6254 bytes; it imports this chart dynamically and passes contractCalls?.points ?? [] plus the availability and loading props. Those two sources are evidence only and are not modified.

The chart's acknowledged public source checkpoint is c92aa4a1e7927d744550c7eb661fa9f20049a974. The later API/page postimages are recoverable through checkpoint 63518084a46841ab670add0aa3f5d34ad99975c6 and its previous manifest 0a7e7e4150015e6498ab6545ff53f4f6e7513452. The initial deployment-list draft in that older manifest remains superseded; it is not an input here. These native blob acknowledgments are custody locators, not a promise of indefinite retention.

A fresh native donor-main metadata read still returned 482ee456369418ef82c4056718cb82d3468f762b. No upstream source was reacquired for this change.

Patch identity: 561ecd870670d8f494b0e60ded1046a5a85ca891, 580 UTF-8 bytes. The patch is +6/-0, one hunk and twelve rows. Apply it to the stated #32129 chart postimage. All earlier packets, guides and the three original MIT notices in this prefix remain unchanged; their attribution and source-custody limits continue to apply.

## Primary contract and overlap qualification

The successful [MDN Date.parse reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse) documents UTC interpretation of date-only input and distinguishes date-time input without an offset. The successful [MDN Intl.DateTimeFormat constructor reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat) documents the runtime's zone as the default and UTC as an explicit option. The correction applies those contracts to the actual source above; it is not an executed timezone comparison.

Earlier [#31985](https://github.com/woahwhattheheck/commons/pull/31985) handled the same class of defect in five different network charts: PaymentVolumeChart, DailyActiveAccountsChart, TransactionsPerDayChart, NewAccountsChart and FeeTrendsChart. One native PR metadata read and one files read resolved this concrete overlap question. Its source paths do not include ContractCallsChart. No accepted hunk, calculation or application verification was replayed.

A new dedicated Commons query for ContractCallsChart and calendar returned the known aggregate issue #31453 despite an is:pr qualifier. Query filtering is therefore not independently established. That result is not treated as a clean zero, proof of uniqueness, an implementation lead or an ownership reservation. Current seat coordination identified no same-file writer.

A second seat reviewed the transferred narrow contract without source, documentation or execution calls. It found no concrete concern and reiterated that the expression does not validate calendar dates. This was nongating reasoning, not an independent full-source audit.

## Verification and publication boundary

The unique insertion anchor and its exact inverse preserve every unselected source byte. The newly serialized unified diff was parsed for file headers, hunk coordinates, context and row counts; applying it to the actual complete preimage reproduced the complete intended postimage, and inverse application restored the preimage. Those are text-only checks of this new patch.

No Date constructor, date-recognition expression, chart renderer, compiler, tests, fixture, browser, workflow or API request was run. Earlier accepted work was not replayed. No account, contract, deployment, upstream submission, bounty claim or payment action occurred. This attributed Commons source packet does not establish deployed behavior, whole-build success, upstream acceptance or payment entitlement.
