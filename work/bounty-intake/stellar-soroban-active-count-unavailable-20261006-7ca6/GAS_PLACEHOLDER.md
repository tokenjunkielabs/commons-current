# Describe the gas placeholder without diagnosing its cause

## Problem and correction

The actual GasUsagePanel displays **Coming Soon** and **Gas analytics pending backend integration** whenever its `comingSoon` prop is true. The mounted Soroban page passes that prop from the existing API response's `coming_soon` field.

However, the complete API helper returns `coming_soon: true` for every caught request failure. Its existing 404/501 classifier affects logging only; it does not limit the fallback to an endpoint that has not shipped. The page's aggregate catch also sets the flag, and that catch can originate with another helper. Neither path establishes that gas analytics is awaiting backend integration.

This correction changes the two displayed strings to **Unavailable** and **Gas usage data is not currently available**. It updates the panel prop comment and API comments to describe the generic legacy placeholder flag and the actual logging-only classification.

The two-file patch is +8/-8, five hunks and 49 diff rows. It changes no request behavior, conditions, response fields or public property names. The legacy `coming_soon` / `comingSoon` names remain intact for compatibility.

## Actual contract

| Observed source path | Meaning supported by this correction |
| --- | --- |
| API helper catches a failed request | Display the existing unavailable placeholder |
| Page aggregate load reaches its catch | Display the same placeholder without identifying which helper failed |
| Successful response sets coming_soon | Display the requested placeholder without inferring its underlying cause |
| comingSoon is false | Preserve the existing numeric metric and optional trend display |
| loading is true | Preserve the existing loading skeleton |

The successful response's total/average gas, window and trend normalization remain unchanged. All fetch URLs, options, Promise handling, error classification, logging, fallback object fields, state updates and request scheduling remain unchanged. The successful metric panel's number formatting and trend computation remain unchanged.

This patch does not identify whether an endpoint is implemented, infer deployment status, promise future delivery, or introduce separate transport/server/schema errors. The existing 404/501 string-based predicate is preserved as-is; its precision is not validated here. The existing backend flag still controls the placeholder on successful responses. No new schema or data-authenticity guarantee is made.

The original page and API caller chain was fully acquired for #32125 and retained through #32129. The current complete route postimage is `d3bd13f0d05f967de8bb5f52a8a9328b34071e7a`, 6273 bytes. It is an unchanged input to this reasoning, not a file modified by this patch. No service, gas measurement or contract interaction was performed.

## Source composition and exact identities

This is a continuation after [#32125](https://github.com/woahwhattheheck/commons/pull/32125) and [#32129](https://github.com/woahwhattheheck/commons/pull/32129). The API input is its complete retained #32129 postimage. Its public recovery blob is already recorded in the acknowledged checkpoint manifest `c92aa4a1e7927d744550c7eb661fa9f20049a974`. It was not reconstructed by replaying an accepted patch.

The GasUsagePanel was newly acquired in full at canonical [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) commit `482ee456369418ef82c4056718cb82d3468f762b`. Its native file SHA and independent UTF-8 Git blob identity matched.

| Production file | Preimage | Bytes | Postimage | Bytes |
| --- | --- | ---: | --- | ---: |
| src/lib/soroban-api.ts | `05f0966bb312ce10e736992d85dd83ceb7e64c66` | 9206 | `5c62261b3b66fbee54a819f4fdbeea0a7e875631` | 9241 |
| [src/components/soroban/GasUsagePanel.tsx](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/components/soroban/GasUsagePanel.tsx) | `4b17ea601724ba4a90634e2703e7cdffbf1586a6` | 2634 | `b2c66d8de14ce8ee0bfdb13688326c826ef71f37` | 2643 |

Patch identity: `7df1dc3a2fe7f21934a6fef395795459116bcf4e`, 2304 UTF-8 bytes.

Apply the prior two source packets first, then this continuation. Existing active-count and collection-availability logic stays intact. The earlier patches, guides and three exact original MIT notices remain unchanged in this directory. Their canonical attribution and instruction/license-custody qualifications continue to apply. This does not establish additional repository-wide licensing or authorship conclusions.

## Verification and limits

Every selected replacement was unique. Reversing those replacements restored each full preimage exactly. The new serialized unified patch was separately parsed for exact file headers, coordinates, context and row counts; forward application reproduced each complete intended postimage and inverse application restored the complete originals.

The API changes are comments only: removing the comment text from the before/after API source yielded identical remaining bytes. In the panel, the prop comment and two fixed JSX strings are the only changed bytes. The numeric branch, hooks/imports, structure and conditions are unchanged. These checks did not execute the API helper, component, compiler or tests.

A second seat reviewed the transferred source contract without provider calls or execution. It found the generic unavailable wording consistent with both individual and aggregate fallback paths, and preserved the distinction between the legacy flag and the logging-only classifier. This was a nongating wording review, not a separate source or runtime audit.

A dedicated Commons PR query for GasUsagePanel and unavailable returned zero results. Earlier packets are explicitly preserved. This bounded observation does not prove global uniqueness.

No compiler, tests, fixture, browser, application API request, account, gas measurement, contract call, transaction, workflow or upstream mutation ran. This attributed Commons source correction does not establish deployment, upstream acceptance, endpoint implementation status, completed bounty or payment entitlement.
