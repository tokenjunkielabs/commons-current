# Certificate download resource cleanup

The retained downloadCertificate implementation awaits generation, creates an object URL, builds an anchor, appends and clicks it, then removes the anchor and revokes the URL. The last two operations are reached only on the successful path. An exception after URL acquisition can skip revocation; an exception after anchor acquisition can leave the anchor attached.

This follow-through gives the acquired URL and anchor separate finally scopes. It is source-only resource ownership, not an executed download or a change to certificate generation.

## Exact source and attribution

Donor: Protocol-Guild/PayD@`171c74b454daba241bfb75f36d10a0a3a77a68e5`.

Production path: `frontend/src/services/certificateApi.ts`, mode100644.

| Identity | Git blob | UTF-8 bytes |
|---|---|---:|
| Complete preimage | 5e42ac7898839800116ac20182cea5c02ddaa348 | 4182 |
| Prepared postimage | 5efb11f3ac93735b96cdc04155073bcdabee1b1b | 4246 |

Original contribution: https://github.com/Protocol-Guild/PayD/pull/142 by Abidoyesimze, observed CLOSED/MERGED, head `ca8da0a5a52e89ef0ba06787029e7d92bfb3728b`, merge `1adaab8fe44744554d25020932a9d2f49e069aa3`. Its complete path metadata binds this service to the same blob that remains in the current donor. Preserve that contribution, repository authors and existing notices.

The service, current caller, canonical tree and PR metadata were acquired while preparing the distinct Commons #31987 automatic-lookup correction. Their complete retained strings are reused here; there is no accepted-source reread, request replay or backend/test acquisition. That earlier correction changed CertificateDownloadButton only. This new patch changes certificateApi only and preserves all #31987 artifacts.

The exact preimage above is the current canonical service. Protected #479/#594 API-base work is not silently substituted, reapplied or overwritten, and no combined-module identity with that external contribution is asserted. Protected #31931/PR576 export cleanup is another source scope and is not replayed.

## Connected source chain

The acquired App mounts TransactionHistory at /transactions. Its existing rows with a transaction hash render CertificateDownloadButton. The button's existing explicit handler awaits downloadCertificate after its original guards and information lookup. Its try/catch/finally and notifications remain unchanged.

| Retained caller | Git blob | UTF-8 bytes |
|---|---|---:|
| frontend/src/pages/TransactionHistory.tsx | ffa01e776eb57818efe9d2e4576a0a91aa1ef691 | 10488 |
| Original CertificateDownloadButton.tsx | c463d21593e71db2021850026aaa591bf0f0f5d2 | 4011 |
| Prepared #31987 CertificateDownloadButton.tsx | 20be3f91fda37f145cf5822d1fc7c48e77bd8ac3 | 4218 |
| frontend/src/App.tsx | acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c | 6460 |

The original and #31987 manual handler/JSX suffixes are byte-identical. This establishes the static call chain for this additional service hunk. It does not establish any actual user record, permission, endpoint response, certificate or downloaded file.

## Ownership order

After createObjectURL returns, execution enters the outer try. Its finally calls revokeObjectURL for that local URL whether anchor creation, setup, click or anchor cleanup completes normally or throws.

After createElement returns, execution enters the inner try. Its finally calls remove on that local anchor. The href assignment, filename expression, appendChild and click retain their original values and order. Element.remove is safe for an anchor that was never attached or is already detached; it removes the element from its current parent if present.

The outer finally still executes if the inner cleanup throws. Generation failure or URL-creation failure occurs before the URL cleanup scope, so no unacquired URL is referenced. An anchor-creation failure reaches URL cleanup without referencing an unacquired anchor.

On the successful path, the order remains generation, URL acquisition, anchor setup, append, click, remove, revoke. Cleanup still occurs immediately after click; this patch does not postpone it or claim that the browser has completed delivery of the file.

## Validation and primary contracts

Primary API references were acquired:

- https://developer.mozilla.org/en-US/docs/Web/API/Element/remove
- https://developer.mozilla.org/en-US/docs/Web/API/URL/revokeObjectURL_static

MDN documents that remove detaches an element and is a no-op without a parent, while revokeObjectURL releases a previously created object URL. These contracts support the cleanup operations. Browser-specific download timing, installed environments and actual DOM execution were not validated.

The source patch adds thirteen lines and removes seven across one hunk/26 complete rows. The actual serialized unified patch was independently parsed and applied to the full preimage; its result exactly equals the prepared postimage. Reverse application exactly restores the original source. The full prefix before the modified resource block and the full verification/info suffix remain byte-identical, including the API-base expression, interfaces, generation request and error handling.

A peer checked the supplied ownership sequence without provider calls or runtime and found no concrete ordering concern. That reasoning is supplementary, not an approval or execution claim.

## Limits

Cleanup APIs themselves can throw; a later cleanup error may replace an earlier exception. A process termination or a call that never returns is not covered. The successful-path immediate revocation timing remains the original policy, not a new browser-delivery guarantee.

The patch does not change the request, response type, Blob generation, endpoint configuration, filename, certificate contents, underlying identity selection, authorization, verification, transaction-info lookup, retry admission, disabled/busy policy or notification messages. It does not repair the separate stale-result or identity-synchronization limits documented for #31987.

No browser, DOM event, network/API call, certificate generation/verification/download, employee/organization/user record, account, authorization, wallet, transaction, compiler, runtime, test, fixture, upstream PR, sponsor, acceptance or payment action was performed.

## Additive artifacts and license

This packet adds download-resource-cleanup.patch and DOWNLOAD_RESOURCE_CLEANUP.md to the existing #31987 directory. Its original automatic-lookup-guard.patch, README.md and LICENSE remain unchanged.

The existing LICENSE is the unchanged Apache-2.0 text, exact donor-tree blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`, 11357 bytes. Keep it and the contributor/repository notices with both modifications. This guide identifies the new change; complete donor modules are not republished.
