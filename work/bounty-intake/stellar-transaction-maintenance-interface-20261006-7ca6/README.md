# Align the transaction route with its current maintenance components

The current transaction-builder route imports a Signature type that its child module does not export and supplies workflow props to two components that accept no props. Both complete child modules now render maintenance placeholders. The route still contains a transaction/signature/submission flow that those children cannot invoke and describes the workflow as operational.

This source-only correction makes the page match its current components: it renders the existing TransactionBuilder placeholder without unsupported props, removes the unreachable workflow wiring and explains that building, signature collection and submission are unavailable during maintenance. It does not implement or invoke any transaction operation.

## Actual source and attribution

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).
Immutable donor: `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete acquired module | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/transactions/builder/page.tsx` | `57f1d925c06fa88173441fea2e8c7e8886a3e381` | 4,098 |
| `src/components/transactions/TransactionBuilder.tsx` | `92e0264e2bd2eeea8280a4bcc0f8a5c6214b8e3d` | 378 |
| `src/components/transactions/SignatureCollector.tsx` | `2cda77abfae6a88217c7c1659474c5d7b831c36a` | 417 |
| `src/components/transactions/index.ts` | `6427586346f0e229c5487d1503b51c3d823e3e74` | 496 |

The actual App Router page imports the two child modules directly. TransactionBuilder and SignatureCollector are each zero-argument exported functions whose full bodies contain only maintenance text and layout. Neither accepts, reads or invokes a supplied callback. SignatureCollector exports no Signature binding. This complete local import/export/caller evidence is the basis of the correction; no guessed SDK, backend or hypothetical caller contract is used.

Native current path history for the route and SignatureCollector returned christabel888's relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`. That is observed history, not an assertion of original authorship for every line.

A dedicated upstream PR search found [PR #203](https://github.com/Stellar-Analysis/frontend/pull/203), by miss-yusrah, currently closed and merged. Its observed head is `6d1736aae0934f019dec23cb5c019a4609bd9557`. The complete five-file changed-path response covers three locale resources, Sidebar and the transactions index under the historical frontend/ prefix; it does not change this page or either child body. Its classification places this route in Explorer rather than an insight dashboard. The retained current index preserves that same classification. This patch changes no navigation path, index export or group placement.

Dedicated Commons SignatureCollector plus maintenance and public Slack equivalent queries returned zero. These are bounded overlap results, not exhaustive absence claims. No new external assignment, reward eligibility, whole-PR acceptance or upstream permission is inferred.

## Why the removed flow is unreachable through this page

transactionId starts as null, so the page initially renders TransactionBuilder. Its only setter is in handleXdrGenerated, which is passed as onXdrGenerated to the zero-argument placeholder. The full placeholder has no event control or callback invocation. Consequently this acquired child provides no path into the parent callback or its pending-transaction POST, and no path that selects the SignatureCollector branch.

The collector is itself a maintenance placeholder with no signature or submit controls. Its proposed onSignatureAdded and onSubmitTransaction props are not part of that current implementation. The page's Signature import also has no matching export in the complete directly imported module.

This is a bounded source reachability/interface statement about these acquired modules. It does not assert that backend endpoints are absent, that no other route can submit transactions, or that the entire project currently builds. No network, wallet, signer, XDR, account or transaction data was acquired or used.

## Exact source correction

`align-transaction-maintenance-page.patch` is **+5/-89 across two hunks in one production file**.

| Source identity | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Before | `57f1d925c06fa88173441fea2e8c7e8886a3e381` | 4,098 |
| After | `1de4c07f4d43cf83f0ed5e5781d50df24b89718f` | 1,304 |

The patch removes useState/logger/SignatureCollector/Signature imports that only supported the disconnected flow; removes transactionId/xdr/requiredSignatures/loading state and the three unreachable request callbacks; replaces the conditional builder/collector branch with the existing TransactionBuilder without props; and replaces the operational promise with the current maintenance status. The nearby JSX comment is updated to describe that state.

The client directive, default page export, route path, React/TransactionBuilder/Hexagon imports, heading, icon, visible initial child and surrounding layout/class strings remain unchanged. Both child modules and the transactions index are byte-for-byte untouched by the patch. No new API request, signature collection, transaction construction, account validation, authorization, retry, recovery or backend behavior is added.

This deliberately aligns with today's maintenance interface. If these children later regain operational implementations, their real typed interfaces and source-account contract must be acquired and deliberately wired. The removed DUMMY_ACCOUNT placeholder is not replaced with a fabricated account or an asserted valid transaction source. Future functionality is not silently restored by this patch.

## Source validation and limits

All four complete source bodies matched their immutable Git blob identities and UTF-8 byte counts independently. The serialized patch reconstructs the whole postimage, and its inverse reconstructs the whole preimage. Pure source comparisons preserve the header/layout wrappers and retain the actual initial maintenance child. The result removes the identified local import/prop mismatch at source level; no compiler, typecheck, build, fixture, test or application runtime was invoked.

No transaction was built, signed, posted or submitted. No wallet/account/key operation, browser, clipboard, export, API request, user data or backend execution occurred. The patch does not certify financial correctness, security, network configuration, transaction lifecycle, recoverability or any whole-project readiness. Current English copy is preserved as the page's existing language convention; localization is not added.

The complete retained donor tree has no AGENTS/RULES paths. Known contributing guidance concerns EventSource tests/npm release workflow, outside the authorized source-only work. Three differently attributed documentation MIT notices do not establish repository-wide licensing. This Commons packet publishes only the minimal attributed patch and this original guide, preserves the external navigation contribution and all exact held routes, and makes no upstream submission.
