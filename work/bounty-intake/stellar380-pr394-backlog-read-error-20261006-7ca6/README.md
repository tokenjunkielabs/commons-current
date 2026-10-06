# Propagate a failed PR394 retry-backlog read

This review packet changes one error path in contributor PR394 for Stellar-Analysis/frontend issue380. If the fresh-period query succeeds but loading pending retries fails, the donor currently logs the error and substitutes an empty backlog. With clean or empty fresh work, run_once returns a successful report and the daemon can reset its consecutive-failure counter even though the pending backlog was never read. The patch returns the existing ReconciliationError instead, allowing the existing daemon tick-error handling to report and back off on that failure.

## Contributor and source identity

The contributor implementation is by **s6pa1rta3n-lab** in **s6pa1rta3n-lab/Stellar-inights**, branch **fix-issue-380**, immutable head **de6a5b36097acabf97f4c10f3ef64e1676cb0560**. This packet is a small attributed follow-up; it does not present the contributor's broader reconciliation implementation as original work here.

- Issue: https://github.com/Stellar-Analysis/frontend/issues/380
- Current contributor PR: https://github.com/Stellar-Analysis/frontend/pull/394
- Exact donor source: https://github.com/s6pa1rta3n-lab/Stellar-inights/blob/de6a5b36097acabf97f4c10f3ef64e1676cb0560/backend/src/reconciliation/compare.rs
- Superseded PR: https://github.com/Stellar-Analysis/frontend/pull/388
- Explicit supersession comment: https://github.com/Stellar-Analysis/frontend/pull/388#issuecomment-5494440848

At qualification, issue380 was open with no native assignees; its three comments requested assignment. PR394 was open and unmerged, based on upstream commit d8bae439cbaeb0f6b3a4fb36ffe212993c3af617. PR388 was closed and unmerged, with the author directing readers to fix-issue-380. Both seven-file metadata lists exposed the same blob identities. A dedicated all-state issue-number PR search returned394,388 and the adjacent ingestion PR392. That bounded search is not an exhaustive semantic-overlap or ownership clearance. No assignment, reward, sponsor approval, payment eligibility or upstream acceptance is asserted.

## Exact source contract and correction

The complete immutable source bodies were acquired and independently hashed as Git UTF-8 blobs:

| Source path | Bytes | Blob SHA |
| --- | ---: | --- |
| backend/src/reconciliation/compare.rs | 20,125 | b090291ed8bcb5427fff339e1360e278640b34f4 |
| backend/src/reconciliation/mod.rs | 2,136 | 0f677bdaa25ea212d2176f192b7babf69f076f04 |
| backend/tests/reconciliation_fault_tolerance_test.rs | 14,613 | b98af6fbf044b75a7d39e0be9a7b4fe11008b232 |

In the donor compare.rs, the ReconciliationStateStore trait at lines55–67 returns Result<Vec<u64>, ReconciliationError> from load_pending_retries. The match at lines304–310 turns Err into Vec::new(). That is observably different from a successfully loaded empty backlog.

The patch replaces that match with:

```rust
// 3. A failed backlog read is a tick failure, not an empty backlog.
let pending_retries = self.state_store.load_pending_retries().await?;
```

The original error value is propagated without introducing a new enum variant, signature or dependency. A successful read follows exactly the existing merge/deduplication and per-period paths. If the read fails, run_once returns before constructing the merged comparison batch, so it does not manufacture a report declaring that batch clean.

The actual consumer already exists in run_until_shutdown: donor lines475–534 match on run_once. Its Err arm increments RECONCILIATION_TICK_ERRORS_TOTAL, increments the consecutive failure count, computes the existing backoff, logs the failure, attempts a ReconciliationTickFailed alert, then performs the existing backoff wait. It continues through the existing loop and shutdown rules. The patch adds no retry loop. Direct run_once callers receive the existing error instead of the previous successful partial report. Alert delivery is attempted by the existing code; successful delivery is not guaranteed by this change.

## Side effects and deliberate boundaries

The optional MissingSubmissionHandler phase at donor lines277–298 executes before the fresh-period and backlog reads. It may already have produced external effects when the backlog read fails. This patch does not undo those effects, provide transactional semantics or make repeated resubmissions idempotent. The daemon may invoke that phase again on a later tick through its existing behavior.

Per-period comparison has not started at the failing backlog-read point. Returning here therefore does not discard completed sibling comparison outcomes from this batch. It deliberately defers fresh comparisons until the pending-work list can be loaded, matching the existing treatment of a failed fresh-period enumeration.

This packet does not implement a durable state-store adapter, claim crash/restart persistence for the in-memory default, repair ignored record_failed_period or record_reconciled_period errors, deduplicate alerts, change max-batch fairness, validate backoff settings, change resubmission behavior, or resolve the whole issue380. It changes only the treatment of a failed pending-retry read.

The previously completed Commons31839 shutdown-watch correction is protected and is not reimplemented, reapplied or reviewed here. This patch has no shutdown/watch hunk. Its exact donor hunk was not recovered during this assessment; composition with that separate packet remains a downstream integration task. No in-flight cancellation guarantee is inferred. The earlier held Commons ReconciliationJob search was not retried or replaced with another query.

## Patch and static validation

Apply pr394-backlog-read-error.patch to the exact contributor head above. It changes only backend/src/reconciliation/compare.rs, in one hunk: **+2/-8**, including the explanatory comment. The computed postimage is **19,952 UTF-8 bytes**, Git blob **bf560cd3c9063c6aef8fd273112d73a7ef39f6ad**. That postimage identity is a local comparison value, not a claim that the contributor repository was modified or that its full postimage was separately uploaded.

Validation actually performed:

- Complete acquired source text matched native and independent blob identities.
- The replacement preimage occurred exactly once.
- Every context and removal line in the generated unified hunk matched the retained preimage.
- Applying that hunk in memory reconstructed the entire intended postimage exactly.
- The source branch from backlog error to the existing daemon error arm was inspected.
- The supplied fault-tolerance test source was inspected; it does not inject an error from load_pending_retries.

No shell executor, compiler, Cargo command, test, daemon, database, RPC call or other runtime was executed. Tests and all other donor files remain unchanged. This is source reasoning and exact patch construction, not a runtime pass or an end-to-end fault-tolerance result.

## Notices

At the exact PR394 head, the docs directory metadata binds these three existing notices:

| Donor notice | Packet notice | Bytes | Blob SHA |
| --- | --- | ---: | --- |
| docs/LICENCE.md | NOTICE-MCLAUGHLIN-MIT.txt | 1,104 | 57740b9d4d86aedf5d518f2f363d5cf192c54127 |
| docs/LICENSE.md | NOTICE-MENKE-LAGUNA-MIT.txt | 1,111 | af5411fa243cfcf2b61c79d081dbb6204e956041 |
| docs/license.md | NOTICE-DE-WET-MIT.txt | 1,080 | 4a766e268772888af5df56c3f6c608f68558b789 |

Their complete already-retained bodies are copied without alteration, including original line endings. They name Michael Mclaughlin; Romain Menke and Antonio Laguna; and Declan de Wet, respectively. These differently attributed notices coexist under docs; this packet does not infer a repository-wide license scope or attribute the reconciliation implementation to those notice holders. Contributor attribution and the pinned original source remain explicit.

## Publication scope

The Commons packet contains the source patch, this guide and the three notices. Publication modifies Commons only. No contributor/upstream branch, issue or PR is edited; no external acceptance, assignment or payment claim is made. Publication checks establish artifact identity and repository state at their observation, not runtime correctness.
