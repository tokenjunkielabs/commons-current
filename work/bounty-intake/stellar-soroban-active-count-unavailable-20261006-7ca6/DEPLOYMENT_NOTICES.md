# Describe deployment coverage without diagnosing event ingestion

## Problem and correction

The Soroban API helper and page each have an existing failure fallback that returns an empty deployment list with `partial: true` and a fixed notice. That notice attributes unavailable data to deployment/init events not being fully ingested. The actual list component's default partial banner and partial-empty description likewise identify missing contract events or pending contracts-repository work as the cause.

These same paths are used after ordinary request failures and the page's aggregate failure. The acquired frontend does not determine that event ingestion caused each such failure. Its nonpartial empty text also asserts that no new deployments occurred, while the directly observed input is an empty returned list.

This three-file correction changes only fixed strings and comments:

| Location | Corrected statement |
| --- | --- |
| API helper and page fallback notice | Deployment data is unavailable or incomplete. This list may not include all deployments. |
| List default partial banner | Deployment coverage is partial or unconfirmed. This list may be incomplete. |
| Partial empty list | No deployments are available to display; coverage may be incomplete. |
| Nonpartial empty list | No deployments were returned for this view. |
| Response/prop comments | Coverage is incomplete or unconfirmed. |

The patch has +7/-7 lines, six hunks and fifty diff rows. All runtime flags, expressions, conditions, request parameters, normalized values, list rows and date formatting stay unchanged. Backend-supplied notice text continues to take precedence through the existing trim/default expression.

This gives users the information supported by the current view without promising that ingestion work will resolve every missing result. It adds no availability mechanism, schema validation, retry, request or loading behavior.

## Actual caller and limits

The complete retained API calls `fetchJson` and returns deployment data through `fetchSorobanNewDeployments`. Its catch returns the existing `partial: true`, empty list and notice. The complete retained page also sets that fallback in its aggregate catch. It passes the response's partial flag, notice, deployments and loading state to the newly acquired NewDeploymentsList.

The list shows its banner when `partial || Boolean(notice)`, selects `notice?.trim() || DEFAULT_PARTIAL_NOTICE`, and uses the partial flag to choose its empty description. Those exact expressions are unchanged. The page aggregate catch may originate in a sibling request and does not identify the deployment endpoint as the source of every failure.

Existing normalization remains a limitation. The helper still uses `Boolean(data.partial)`, so a successful response with an absent or falsy partial field is not newly marked uncertain. A non-array deployment field is still normalized to an empty array. No stronger interpretation of those successful malformed inputs is introduced. The optional child prop's default false is also unchanged.

The normal populated list still displays each returned contract, date, optional ledger and optional deployer. No transaction, account, contract, deployment process or actual ingestion system was inspected or operated. The number of returned records remains a display of input length, not proof of complete network coverage.

## Exact source composition

This continuation follows [#32125](https://github.com/woahwhattheheck/commons/pull/32125), [#32129](https://github.com/woahwhattheheck/commons/pull/32129) and [#32132](https://github.com/woahwhattheheck/commons/pull/32132). The API preimage is the complete retained #32132 postimage; the route preimage is the complete retained #32129 postimage. Neither was reconstructed by applying an accepted patch again.

Their acknowledged public checkpoint chain ends at `fe857136099c218b42c779c2fd9024a713f1815b`, linked to `c92aa4a1e7927d744550c7eb661fa9f20049a974`. Those manifests identify the exact public source blobs used here. The new list source was fetched in full at canonical [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) commit `482ee456369418ef82c4056718cb82d3468f762b`; native file SHA and independently computed UTF-8 Git identity matched.

| Production file | Preimage | Bytes | Postimage | Bytes |
| --- | --- | ---: | --- | ---: |
| src/lib/soroban-api.ts | `5c62261b3b66fbee54a819f4fdbeea0a7e875631` | 9241 | `a3ba6bc1f13ec89d31191d18550e8bb0b584b407` | 9226 |
| src/app/[locale]/soroban/page.tsx | `d3bd13f0d05f967de8bb5f52a8a9328b34071e7a` | 6273 | `80ba478b5aa34d8af463ea4a5c6f969eeca114fa` | 6254 |
| [src/components/soroban/NewDeploymentsList.tsx](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/components/soroban/NewDeploymentsList.tsx) | `6cb57ff2a5cfc8aa70bf602297264b7bb7f2c55c` | 5326 | `3a6bdbcac7e120d8e01515569da43dfe874a0ead` | 5237 |

Patch identity: `96e0bdaf6d8a0214c79d38b6e2a8bd32b54caa82`, 2766 UTF-8 bytes.

Apply the three earlier source corrections before this patch. The earlier active-count and collection availability logic, gas wording, source packets, guides and three original MIT notices remain unchanged except for the explicitly listed new replacements in shared source. Their canonical attribution, notice text and historical instruction/source-custody limits continue to apply; no additional repository-wide licensing or authorship claim is made.

## Verification and publication boundary

Every selected string/comment replacement was unique, and reversing the selections reproduced all original bytes. The new serialized unified diff was independently parsed for exact file headers, coordinates, context and counts. Forward application reproduced all three complete intended postimages, and inverse application restored all three complete preimages. Every unselected byte stayed unchanged.

These were text checks. No request handler, list renderer, date formatter, compiler, tests, browser or workflow was executed. Earlier accepted application work was not replayed to establish these new inputs.

A second seat reviewed the transferred wording contract without provider calls or execution. Its suggested partial-empty refinement was incorporated: data may be unavailable to display even when no API response was received. The normal nonpartial-empty wording remains limited to returned data, with the normalization caveat above. This was a nongating wording review, not a separate full-source audit.

A new dedicated Commons PR search for NewDeploymentsList and unconfirmed returned zero results. This is bounded overlap evidence, not proof of global uniqueness or ownership. The earlier source corrections are explicitly retained as prerequisites.

No API, account, contract, deployment, ingestion, transaction or upstream action ran. The Commons packet is an attributed wording correction. It does not establish a deployed fix, complete coverage, a diagnosed ingestion defect, upstream acceptance, bounty completion or payment entitlement.
