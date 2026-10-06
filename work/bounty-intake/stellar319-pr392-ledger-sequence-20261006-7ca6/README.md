# Validate requested ledger sequences in PR392

PR392's ingestion pipeline requests a specific ledger but trusts the returned FetchedLedger.sequence. The same assumption appears in normal ingestion and rollback-anchor loading. This attributed patch rejects a sequence mismatch at both boundaries before the pipeline mutates its derived-row or checkpoint stores.

## Contributor, assignment and immutable carrier

The source is contributor **ndii-dev**'s **ndii-dev/Stellar-inights** branch **feat/ledger-ingestion-checkpointing**, pinned to **8fbd01316f4264a3a2bbd9bade1d7a04de15c7e9**.

- Issue319: https://github.com/Stellar-Analysis/frontend/issues/319
- Contributor PR392: https://github.com/Stellar-Analysis/frontend/pull/392
- Exact changed source: https://github.com/ndii-dev/Stellar-inights/blob/8fbd01316f4264a3a2bbd9bade1d7a04de15c7e9/backend/src/ingestion/mod.rs

At qualification, issue319 was open and natively assigned to ndii-dev; the bot comment names the same assignee. That assignment remains with the contributor. PR392 was open, non-draft and unmerged, based on d8bae439cbaeb0f6b3a4fb36ffe212993c3af617, with nine changed files and no issue-style PR comments. The dedicated all-state issue-number PR search returned392. This is bounded carrier evidence, not exhaustive semantic-overlap clearance, maintainer acceptance or a payment entitlement.

The contributor's ingestion design, tests and original authorship remain attributed. This packet supplies a narrow review patch rather than taking over the assigned issue or presenting the pipeline as new work here.

## Source-established failure paths

The LedgerSource trait fetches one requested sequence at a time. Its FetchedLedger result has a public sequence field. The acquired HorizonLedgerSource uses the requested sequence in the URL but returns the JSON body's sequence unchanged. Its parsing path does not compare those two values. This makes the unchecked response field a concrete input to the pipeline rather than a hypothetical new API.

In the donor mod.rs:

1. run_once requests next_sequence at line144. Without a current checkpoint, there is no predecessor-hash comparison at all. With one, matching prev_hash still does not compare the sequence fields. The pipeline then passes fetched.sequence into derived.upsert and checkpoint.save.
2. handle_reorg requests rollback_target at line183. It invalidates rows from the requested rollback_target + 1, but saves the returned anchor.sequence and anchor.hash. A mismatched anchor can therefore make the invalidation boundary and saved checkpoint refer to different ledger positions.

These are source-level consequences of a mismatched response, not observations of a live Horizon failure or an executed exploit. No live ledger request was made.

## Exact correction and consumer

The patch adds **20 lines in two hunks**, changing only backend/src/ingestion/mod.rs. Immediately after each successful Some fetch, it compares the returned sequence with the requested value. On mismatch, it returns the existing IngestionError::Fetch with:

- sequence set to the requested next_sequence or rollback_target;
- a message containing the actual returned sequence and expected sequence.

The normal-ingestion guard precedes the predecessor-hash comparison, so an unrelated ledger response cannot trigger the pipeline's reorg handler merely because its prev_hash differs. It also precedes upsert and checkpoint save. The rollback-anchor guard follows the existing missing-anchor error conversion and precedes invalidate_from and checkpoint save.

Both guards are after the source fetch has returned; they make no assertion that an arbitrary LedgerSource implementation has no internal side effects. The guarantee is narrowly about the pipeline's own derived-row and checkpoint mutation calls after a detected sequence mismatch.

Correct-sequence responses continue through the existing code unchanged, including real predecessor-hash mismatch handling. Normal Ok(None) still returns Idle. An absent rollback anchor still produces ReorgRollbackTargetUnavailable. Existing source errors still propagate. No public signature, error variant, adapter, dependency or test is changed.

There is an actual source consumer: backend/src/lib.rs exports ingestion, and backend/tests/ingestion_reorg_test.rs constructs IngestionPipeline and calls run_once in its run_to_idle helper. The pipeline's existing run_forever catches an error, logs it and retries on a later tick. This patch uses that existing path; it does not add a scheduler, service mount or application startup wiring.

## Scope and remaining limits

Sequence equality does not authenticate the ledger or validate its hash, predecessor linkage, derived rows or row-level ledger_sequence values. It does not prove that a returned rollback anchor is stable. The donor explicitly treats confirmation depth as an assumption and can only partially correct a deeper reorg; that limit remains.

No atomic transaction is introduced across derived-row changes and checkpoint changes. Crash consistency, concurrent callers, durable adapters, eventual consistency, source freshness, checked sequence arithmetic, API mounting and exactly-once delivery remain outside this correction. The in-memory reference stores remain in-memory. This packet does not resolve all of issue319 or establish reorg recovery on a real network.

The assigned contributor's tests were read as source context, not replayed. The existing response-shape test supplies a matching request/body sequence; it is not evidence of mismatch rejection. No new test is added, and no compiler, Cargo command, daemon, RPC, database, shell executor or other runtime is executed here.

## Immutable inputs and text validation

All six full source files were acquired at the exact head and matched native plus independently computed Git blob identities:

| Path | UTF-8 bytes | Blob SHA |
| --- | ---: | --- |
| backend/src/ingestion/mod.rs | 14,569 | 6c70e179c12e8ab2965a968237b5ae39280297e3 |
| backend/src/ingestion/watermark.rs | 4,180 | be5637409dbd235a9bb75315b083bfb2063b37bf |
| backend/src/ingestion/upsert.rs | 6,961 | e5ab6fadf30e22f46ce71e8e25f78d73960ae470 |
| backend/src/ingestion/fetch.rs | 12,270 | 7aceeddecfb4d8b1c1a92a18261b9eecdffe8a77 |
| backend/src/lib.rs | 454 | e0a3f4798a113e450035b31dc13489db85e10d37 |
| backend/tests/ingestion_reorg_test.rs | 4,268 | 71f24be37613a6e2776b6308c62790514db24f17 |

The source replacement anchors were unique. Both generated unified hunks were applied in memory to the retained preimage; the full result matched the intended postimage. The existing mod.rs test section remained byte-identical. The computed postimage is **15,249 bytes**, Git blob **24a7e0cd6754a397221ffb8133228c8ed8a4c03c**. This is a comparison identity for the reconstructed donor file, not an upstream mutation or a separate native acknowledgement of that full postimage.

Apply pr392-ledger-sequence.patch only against the qualified preimage, or compose against a separately qualified changed head. These exact text/source checks do not establish runtime or test success.

## Notice provenance

The exact contributor head's docs metadata binds these three notices. Their complete already-retained bodies are reused without rereading or changing the accepted notice bytes:

| Donor path | Packet file | Bytes | Blob SHA |
| --- | --- | ---: | --- |
| docs/LICENCE.md | NOTICE-MCLAUGHLIN-MIT.txt | 1,104 | 57740b9d4d86aedf5d518f2f363d5cf192c54127 |
| docs/LICENSE.md | NOTICE-MENKE-LAGUNA-MIT.txt | 1,111 | af5411fa243cfcf2b61c79d081dbb6204e956041 |
| docs/license.md | NOTICE-DE-WET-MIT.txt | 1,080 | 4a766e268772888af5df56c3f6c608f68558b789 |

They retain the names Michael Mclaughlin; Romain Menke and Antonio Laguna; and Declan de Wet, and their original line endings. Their coexistence under docs does not establish a repository-wide license or attribute this ingestion implementation to those notice holders. The pinned contributor attribution remains separate and explicit.

## Publication boundary

Only the review artifacts are published to Commons: the unified patch, this guide and the three unchanged notices. No upstream source, issue, PR, assignment or comment is changed. No sponsor contact, payment, security certification, whole-issue completion or exactly-once guarantee is asserted. Artifact readbacks establish exact publication identity at their recorded observations.
