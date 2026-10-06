# Show successful zero trends as neutral in MetricCard

## Actual defect and correction

The shared MetricCard renders a trend whenever its numeric trend prop is defined. Its original color is positive only when trendDirection matches the favorable direction; every other case receives the negative red class. Its arrow likewise defaults to the downward icon whenever the direction is not "up".

Two actual mounted Soroban callers supply a direction only for positive or negative changes. ActiveContractsPanel and GasUsagePanel pass the absolute trend value to this card; a successful numeric zero therefore reaches it as trend 0 with no direction. That original combination displays a red downward arrow beside 0%. This is a source-based finding from complete retained components and their API/page path, not a fabricated fixture or observed deployed request.

The correction recognizes trend === 0. The existing 0% text remains visible, the trend uses the existing text-muted-foreground class, the directional arrow is omitted, and the card does not receive the success glow for that neutral case. No icon, dependency, data field or caller change is added. An explicitly supplied direction cannot make a zero value directional.

## Exact behavior and limits

Nonzero trends keep the original direction, color and inverse policy. The isPositive expression is unchanged. A missing trend continues to suppress the entire trend block, and its existing Activity-icon behavior remains unchanged. The value, label, sublabel, comparison caption, typography and surrounding card markup are unchanged. Math.abs remains the original displayed magnitude calculation.

Zero includes negative zero under the equality used here. This patch does not infer a direction from a nonzero value, change percentage precision, introduce rounding, reject nonfinite numbers, validate malformed API payloads or repair inconsistent nonzero direction props. A small nonzero value remains nonzero; this change does not apply a threshold. Caller availability gates, loading states and successful-empty policies are unchanged.

These source facts establish a narrow presentation correction. They do not establish live endpoint coverage, an integration result, a whole build result or upstream acceptance.

## Complete source and caller evidence

The complete changed file was acquired once through the native GitHub file API at [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) commit 482ee456369418ef82c4056718cb82d3468f762b. The returned blob identity matched an independent Git-blob identity over the complete UTF-8 content. A fresh donor-main metadata read returned that same commit.

| Changed file | Preimage | Bytes | Proposed postimage | Bytes |
| --- | --- | ---: | --- | ---: |
| src/components/dashboard/MetricCard.tsx | 0be01cd20b73e9cd85b74e17f94398ae7f69e7f0 | 2043 | 4e4d9ca76aafe84d0411756e0e2ff85544645de6 | 2144 |

The unchanged caller evidence is the complete current retained postimages from the earlier attributed Soroban packets:

| Evidence file | Current blob | UTF-8 bytes | Relevant contract |
| --- | --- | ---: | --- |
| src/components/soroban/ActiveContractsPanel.tsx | 56f76087005e608b23853edfd650bc34ee867f37 | 1414 | Positive/negative direction only; defined successful trend passed as absolute magnitude. |
| src/components/soroban/GasUsagePanel.tsx | b2c66d8de14ce8ee0bfdb13688326c826ef71f37 | 2643 | Positive/negative direction only; defined trend passed as absolute magnitude. |
| src/lib/soroban-api.ts | a3ba6bc1f13ec89d31191d18550e8bb0b584b407 | 9226 | Both relevant successful responses preserve numeric data.trend, including zero. |
| src/app/[locale]/soroban/page.tsx | 80ba478b5aa34d8af463ea4a5c6f969eeca114fa | 6254 | Mounts both panels and passes their corresponding trend values. |

These are intact source strings, not reconstructed accepted patches or summary-only inputs. Their producing packets include [#32125](https://github.com/woahwhattheheck/commons/pull/32125), [#32132](https://github.com/woahwhattheheck/commons/pull/32132) and [#32134](https://github.com/woahwhattheheck/commons/pull/32134). None of those files is modified here. The new MetricCard patch applies directly to the stated canonical MetricCard preimage; it does not require applying those caller patches to interpret the diff.

The acknowledged public caller checkpoint chain includes c6799624308a7875bc42add05bc845345d9bb772, fe857136099c218b42c779c2fd9024a713f1815b, and 63518084a46841ab670add0aa3f5d34ad99975c6 with its predecessor 0a7e7e4150015e6498ab6545ff53f4f6e7513452. The older deployment-list draft in that predecessor remains superseded. Blob acknowledgments are recovery locators and do not promise indefinite retention.

## Patch, attribution and overlap

The patch is +5/-4 across two hunks and twenty-two rows. Its identity is d943783922a12400e9469111f7ca10dbb2fa2ec8, 1425 UTF-8 bytes. Every source byte outside the two exact replacements is preserved.

This continuation adds only show-neutral-zero-trends.patch and this guide beside the existing packets and their three unchanged original MIT notices: upstream-licence-mclaughlin.md, upstream-license-menke-laguna.md and upstream-license-de-wet.md. The original attribution and custody qualifications continue to apply. No license notice is replaced or discarded.

The native GitHub issue-search endpoint returned total_count 0, incomplete_results false and an empty item list for the bounded Commons PR query containing "MetricCard" and "zero". This is not proof of global uniqueness or an ownership reservation. Existing seats reported no exact zero-trend correction in their retained completion maps. Earlier HealthDashboard work removed fabricated trend props from a caller; it did not modify this shared card. Earlier chart-empty/baseline and calendar-label corrections affect different source paths. No accepted application or calculation was replayed for this qualification.

## Verification and publication boundary

The two replacement anchors were unique in the complete actual source, and their inverse restored every original byte. The newly serialized unified diff was independently parsed for file headers, hunk coordinates, context and line counts. Forward application reproduced the intended full postimage, and inverse application restored the full preimage.

Those were text-only checks of this new patch. No card or caller expression, React renderer, compiler, test, fixture, browser, workflow, endpoint or donor runtime was executed. No upstream submission, deployment, account, contract, bounty claim or payment action occurred. Publication in Commons makes this attributed candidate reviewable; it does not claim deployed behavior or payment entitlement.
