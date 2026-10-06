# Store the dead-letter entry before invoking the alert sink

This source-only patch moves one existing call in the contributor's job-runner proposal: DeadLetterQueue::quarantine inserts its cloned entry into the in-memory queue before invoking AlertSink::alert. The queue mutex guard is released at the end of the insertion statement, before external sink code runs.

## Donor and scope

Carrier: [Stellar-Analysis/frontend PR403](https://github.com/Stellar-Analysis/frontend/pull/403), by daniel6yi8-gif, covering issues333,334 and335. Transferred current metadata records it OPEN, unmerged and non-draft, with the author assigned. This packet addresses only one local ordering seam relevant to issue335; it does not take ownership of the combined contributor task.

The exact source donor is `daniel6yi8-gif/frontend@3566cbbd307c5fc1316477b3ef83c57b83af3eb9`, branch drips/333-334-335, against base482ee456369418ef82c4056718cb82d3468f762b. This is a contributor PR head, not a deployed backend or canonical main implementation.

Root transferred the complete native eleven-added-path map and issue335's bounded current metadata. Four full job-module bodies were then acquired directly at that immutable fork head. Their returned native blobs, transferred file-map pins and independent UTF-8 Git identities match. The external PR body and test file were not used as execution evidence.

The source change is only backend/jobs/dead_letter.rs. The backup333 and IP-allowlist334 modules, scheduler policy, error taxonomy, tests and public method signatures are unchanged.

## Concrete before and after

The existing method constructs a DeadLetter containing job_name, payload, history and reason. Before the patch, it calls sink.alert(&entry) before locking the entries vector and pushing entry.clone(). If that callback panics instead of returning, ordinary execution does not reach the subsequent insertion. This is a control-flow finding from the acquired method, not a reproduced incident.

After the patch, the sequence is:

1. Construct the same DeadLetter.
2. Acquire the existing queue mutex and push the same entry.clone().
3. End the insertion statement, dropping its temporary guard.
4. Invoke the same sink.alert(&entry).
5. Return the same entry if the alert returns normally.

No catch_unwind, alternate sink, retry, new allocation, additional clone, fallback error or duplicate call is added. There remains exactly one alert invocation.

When insertion completes, later external alert work no longer precedes storage of that record. A sink that reads this queue can now see the inserted entry before its own call completes. Other readers can also see the entry while the alert is in progress. That observable ordering change is intentional.

The lock is not held across the external callback. The existing chained lock/expect/push expression ends with a semicolon, and the alert remains a separate following statement. No named guard is introduced or retained.

## Connected local call path

The complete acquired scheduler.rs declares Job::run and Scheduler::run. Scheduler::run records failure attempts and calls its own quarantine helper for a terminal error or after exhausting the retry ceiling. That helper invokes DeadLetterQueue::quarantine with the job name, payload, accumulated history, reason and its configured AlertSink. The patch therefore changes the queue method actually referenced by this supplied scheduler.

The acquired error.rs defines the retryable/terminal classification used there. The acquired jobs/mod.rs exports Scheduler, the queue and the alert interfaces. The DeadLetterQueue and RecordingAlertSink both use in-memory Mutex<Vec<DeadLetter>> storage; neither supplies durable persistence.

This is a connected call path within the supplied modules. The complete transferred PR diff contains no Cargo manifest or module-registration change, and the retained base inventory had no backend root. jobs/mod.rs declares a backfill module that is not among the eleven added paths. These integration gaps are not repaired or hidden by this patch. No application mounting, compiler success, production job execution or complete runnable backend is asserted.

## Primary language contract

The [Rust Reference's temporary-scope rules](https://doc.rust-lang.org/reference/destructors.html#temporary-scopes) place the temporary guard in this ordinary expression statement's scope. The [standard Mutex documentation](https://doc.rust-lang.org/std/sync/struct.Mutex.html#method.lock) explains scoped unlocking when its guard is dropped; its examples also distinguish an unnamed statement temporary from a longer-lived named guard. These contracts support the inference that this method's queue guard has ended before the following alert call. Documentation examples were not executed.

No Rust compiler version or Cargo configuration is established by those current documentation pages. Mutex poisoning remains the existing expect failure behavior; it is not treated as a general soundness or panic-containment guarantee.

## Limits and changed failure ordering

An alert panic still propagates. In that case neither quarantine nor Scheduler::run is promised to return normally, and this patch does not manufacture Outcome::Quarantined after a panic. The limited retention claim requires successful insertion and a live, retained queue; process abort, restart, destruction or loss of memory is outside it.

If lock acquisition/expect or cloning/insertion fails first, the alert is now not reached. This is the corresponding failure-order change. No allocation, poisoned-lock or out-of-memory recovery is added.

The queue remains volatile and unbounded. Duplicate calls still add duplicate entries; job idempotency is not enforced by this vector. Alert completion/order across concurrent jobs is not serialized by the queue lock. No delivery acknowledgment, external alert reliability, durable replay, exactly-once processing, shutdown policy, retry-configuration validation or whole335 acceptance is claimed.

## Exact source identities

All paths are relative to the immutable contributor fork head above.

| Path | Full preimage Git blob | UTF-8 bytes | Use |
|---|---|---:|---|
| backend/jobs/dead_letter.rs | `beb0aa6dfac9eb45588db4c5c8ec324697bea623` | 2995 | Changed queue method and existing sink implementation |
| backend/jobs/scheduler.rs | `dedcd602a8fab9aa32884a01b11f1223d57a50ec` | 2974 | Direct local caller and outcome/retry boundary |
| backend/jobs/error.rs | `a789af804fd178241024edaaf774f8d5d9aedb60` | 1865 | Failure classification |
| backend/jobs/mod.rs | `49e24f156ffc7a70953f258297908404fd50fad7` | 619 | Module/export relationship |

The sole proposed postimage is backend/jobs/dead_letter.rs, Git blob `bebf0e1f2ac23357a0ba56ff6810ed01713c7075`,2995 UTF-8 bytes. The serialized patch is one hunk/twelve complete rows,+1/-1,445 bytes. It applies forward to that exact postimage and inversely to the exact preimage. Removing the single moved alert line from both strings leaves every other byte equal. This is text verification, not code execution.

## Attribution and preserved notices

The contributor daniel6yi8-gif and original Stellar-Analysis authors retain credit. This packet is a follow-on artifact and does not impersonate, replace, submit or merge the external contributor's PR.

Three complete previously acquired MIT notices are included unchanged: upstream-licence-mclaughlin.md (57740b9d4d86aedf5d518f2f363d5cf192c54127,1104 bytes,CRLF), upstream-license-menke-laguna.md (af5411fa243cfcf2b61c79d081dbb6204e956041,1111 bytes), and upstream-license-de-wet.md (4a766e268772888af5df56c3f6c608f68558b789,1080 bytes). Root transferred their exact JSON-escaped strings; Delivery independently verified bytes and Git hashes without provider rereads or line-ending normalization. Preserving these notices is not a conclusion that every proposed backend file shares a particular license.

## Verification and publication

A new bounded dedicated Commons PR query for PR403 plus dead_letter returned no entries. Root retained no exact prior same-hunk ordering correction. Neither observation certifies global absence or reassignment; all held routes and unrelated source families remain protected.

Validation is complete static source inspection, the local call relationship, primary Rust scope/locking contracts, serialized forward/inverse patch application, every-other-byte preservation and exact artifact identity. No job, scheduler, callback, panic, thread, mutex operation, fixture, test, compiler, module, server or backend was executed.

Publication adds only this patch, guide and three preserved notices to Commons. Five complete immutable artifact texts/native blobs/independent identities, exact changed paths and merged PR/tree/parent metadata are checked. A separately planned main-equality alias is used only when the fresh observed main equals the verified merge/readback ref; otherwise all five artifacts are read completely at one observed immutable main commit, without chasing later changes. Publication checks do not establish runtime correctness, upstream acceptance or a security/availability guarantee.
