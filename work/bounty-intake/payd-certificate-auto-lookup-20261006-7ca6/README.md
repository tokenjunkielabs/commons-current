# Bound automatic certificate-info lookup

CertificateDownloadButton starts an automatic transaction-info lookup when the transaction hash is present, both IDs are missing, and isLoadingInfo is false. The effect depends on isLoadingInfo. Its finally callback restores false even if the lookup returns null or rejects. With both IDs still missing, that state transition makes the same automatic request eligible again.

The acquired service explicitly returns null for a response without data and for HTTP 404, and propagates other request failures. The actual TransactionHistory caller supplies only transactionHash, so the missing-ID branch is connected in source. This is a static state-flow finding; no application request or failure was reproduced.

## Source and original contribution

Canonical donor: Protocol-Guild/PayD@`171c74b454daba241bfb75f36d10a0a3a77a68e5`.

Production path: `frontend/src/components/CertificateDownloadButton.tsx`, mode100644.

| Identity | Git blob | UTF-8 bytes |
|---|---|---:|
| Full source preimage | c463d21593e71db2021850026aaa591bf0f0f5d2 | 4011 |
| Prepared postimage | 20be3f91fda37f145cf5822d1fc7c48e77bd8ac3 | 4218 |

Original feature: https://github.com/Protocol-Guild/PayD/pull/142 by Abidoyesimze, observed CLOSED and MERGED. Its head is `ca8da0a5a52e89ef0ba06787029e7d92bfb3728b`, merge `1adaab8fe44744554d25020932a9d2f49e069aa3`. The current PR metadata reports one issue comment and zero review comments; that comment body was not expanded. The complete eleven-path PR metadata binds the added button and certificateApi module to the exact same blobs still present in the acquired current donor. This is lineage metadata, not a replay or review of the accepted feature's backend, tests or original implementation.

The bounded current certificate PR query also returned #594 and #382. Their bodies/source were not expanded. The previously protected #479/#594 API-base work remains separate and unchanged, as do backend auditing and isolation scopes. The three returned rows are not a global owner or overlap absence claim. No external contribution is modified.

## Actual connected caller and service

| Retained source | Git blob | UTF-8 bytes |
|---|---|---:|
| frontend/src/pages/TransactionHistory.tsx | ffa01e776eb57818efe9d2e4576a0a91aa1ef691 | 10488 |
| frontend/src/services/certificateApi.ts | 5e42ac7898839800116ac20182cea5c02ddaa348 | 4182 |
| frontend/src/App.tsx | acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c | 6460 |
| frontend/src/main.tsx | f84f187971ba135010c48e69fda10f0c0f71ebd9 | 1664 |

App renders TransactionHistory at /transactions. The history page maps its existing rows keyed by item.id and, when item.txHash is present, renders CertificateDownloadButton with only transactionHash. It does not pass the two optional IDs. These are source expressions, not acquired user records or a claim that a particular record exercises the failure.

The complete service's getTransactionInfo reads response.data.data or null. Its 404 path also returns null, while other errors reject. This establishes the two missing-result outcomes needed for the component finding without reading or executing the backend.

The retained main.tsx full string came from another immutable donor; its independently computed blob equals the exact blob in this canonical donor's complete tree. It renders App and is reused by byte identity, without claiming a new provider read. The page, service, component and App identities match the canonical tree and independently calculated full contents.

## Narrow admission guard

A top-level useRef<string | null>(null) remembers the latest hash for which this component instance began an automatic lookup. The existing effect guard additionally requires that remembered hash to differ from transactionHash. Inside that guard, the hash is recorded synchronously before setIsLoadingInfo(true) and the existing service call.

When the same request later settles without IDs, finally still clears the loading flag. The effect may run again because its dependencies are unchanged, but the remembered hash blocks another automatic attempt for that same value. The existing explicit click path still performs its own lookup when IDs are missing, so the user-triggered retry remains available under the original disabled/busy policy.

Only the latest automatically attempted hash is remembered. A different eligible hash can replace it, and returning to an older hash can then permit another automatic lookup. A fresh component instance has its own empty ref. This is not a global request cache, permanent blacklist, per-account cache or one-attempt-per-hash history.

The existing truthiness guards, dependency list, promise callbacks, state setters and error handling remain unchanged. The entire handleDownload function and rendered JSX suffix are byte-identical. No ID validation, association, prop synchronization, certificate generation/verification, authorization, API-base policy, download, notification or route is modified. The source patch is +10/-2 across two hunks and 24 complete diff rows.

## Validation and primary contract

React's useRef reference was acquired: https://react.dev/reference/react/useRef . It documents retaining a mutable value between renders without causing a render, and reading/writing it in an effect. That contract supports this instance-local admission record; no installed React execution or version-specific scheduler behavior is claimed.

The actual serialized patch was independently parsed and applied to the complete preimage, producing the exact postimage. Reverse application recovered the complete preimage. The unchanged manual-handler/JSX suffix was also compared directly. Full source strings match provider identities and independent Git blob hashes. These are source and patch checks, not runtime tests or a synthetic failure loop.

A peer reviewed the supplied effect/service/caller contract without provider reads or execution and found no concrete ordering flaw in this scope. Its explicit qualification is retained: the ref records only the latest attempted hash and does not identify or cancel in-flight results.

## Limits

This correction stops the automatic loading-state feedback loop for the same remembered hash. It does not cancel a request, add a timeout, suppress a late result, clear IDs when transactionHash changes, synchronize changed optional ID props, serialize manual and automatic attempts across instances, or guarantee one request across remounts. Existing stale-result/identity and unmount behavior remain outside this patch.

The original manual click may still fail or return missing information. The original truthiness treatment of IDs, displayed error text and service behavior remain. No successful certificate, correct underlying identity association, complete workflow, backend readiness, storage safety or production incident is established.

No browser, UI interaction, timer, Axios/network request, API endpoint, backend, compiler, runtime, test, fixture, download, user/employee/organization record, account, certificate, wallet, transaction, upstream PR, sponsor, acceptance or payment action was performed.

## Artifacts and license

Only automatic-lookup-guard.patch, this guide and the unchanged Apache-2.0 LICENSE are published. The license is exact donor-tree blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`, 11357 bytes. Preserve the original Abidoyesimze contribution, repository authors and notices; this guide identifies the added modification. Complete donor application modules and backend sources are not republished.
