# Restore the Asset detail modal's prior inline overflow value

The mounted AssetDetailModal temporarily assigns the body's inline overflow to hidden. Its cleanup currently assigns the literal CSS value unset, regardless of the value it replaced. Closing the modal can therefore overwrite a previous inline setting; even a previously absent declaration becomes an explicit inline declaration.

This patch captures the existing inline overflow string immediately before the modal changes it, then restores that same captured string in the existing effect cleanup. It does not introduce a global scroll-lock manager or change the modal's opening, closing or focus behavior.

## Complete source and actual caller

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), immutable commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/components/anchors/AssetDetailModal.tsx` | `dcab1bf692c77dbf8eec93682612d8e364ceb9a4` | 9,160 |
| `src/components/anchors/AssetPortfolio.tsx` | `1801c67028bb96c8b69c8c6d23f47ba45ad0a920` | 6,015 |
| `src/app/[locale]/anchors/[address]/page.tsx` | `71fea1bb40c29bcbba0657ba1cb10a65d35fab23` | 7,297 |

The actual detail App Router page renders AssetPortfolio with its issued assets. AssetPortfolio owns selectedAsset state and renders AssetDetailModal with that selected asset plus an onClose callback which clears it. The modal's effect returns early without an asset; otherwise it installs its existing key listener, applies the scroll lock and supplies cleanup. The effect depends on asset and onClose.

The captured string belongs to each effect setup and its cleanup. The same restoration therefore applies to cleanup when the modal closes, unmounts or the existing dependency list causes setup replacement. No dependency or callback identity is changed.

The earlier [detail diagnostics packet #32032](https://github.com/woahwhattheheck/commons/pull/32032) and [portfolio export-anchor packet #32039](https://github.com/woahwhattheheck/commons/pull/32039) preserve this caller chain and are not included or replayed here.

## Source correction and contract

`restore-modal-overflow.patch` changes only the effect's capture/cleanup in `src/components/anchors/AssetDetailModal.tsx`: **+2/-1 in one hunk**.

Full source identity:
`dcab1bf692c77dbf8eec93682612d8e364ceb9a4` (9,160 B)
→ `1a0749b9dd958c3cee76346d48991a97253d24fa` (9,228 B).

[MDN's HTMLElement.style reference](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) documents that this live object reflects inline declarations, absent declarations read as an empty string, and assigning an empty string resets a declaration. Consequently restoring the captured empty string removes this effect's inline override instead of leaving unset behind. This is a property-value restoration claim, not evidence of any particular live page style.

The entire key handler, Escape close behavior, Tab loop, initial focus operation, listener lifecycle, effect dependencies, all modal markup and displayed values remain byte-for-byte unchanged. The hidden value is still applied at the same location, and cleanup still removes the key listener before restoring overflow.

No document-wide CSS snapshot is taken. The change does not coordinate multiple simultaneous modal owners, preserve arbitrary declaration priority/longhand configurations, resolve concurrent external style writes, capture a replacement body element or guarantee cleanup after custom throwing DOM setters. It does not add focus return, unique IDs, status thresholds or alter the existing rate badges. Those are separate questions, not implied by this patch.

## Validation, attribution and limits

Full serialized forward and inverse reconstruction match the complete immutable preimage/postimage and independently computed Git blob identities. No React render, DOM/style mutation, browser, fixture, test or application build was executed.

Bounded current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`; original contributor rights are preserved and relocation is not treated as sole authorship. Exact scoped Commons/public Slack queries for AssetDetailModal and overflow returned zero, which is bounded evidence rather than a global absence claim.

The retained complete donor tree has no root AGENTS/RULES file. EventSource-specific CONTRIBUTING instructions do not override the explicit session no-tests/no-runtime/no-upstream scope. Differently attributed MIT notices in documentation do not establish a repository-wide code licence. This Commons contribution therefore contains only a minimal patch and this original attributed guide.

No live API or account data, upstream branch/PR/comment, author assignment, sponsor acceptance, bounty/payment or whole-issue completion was performed or claimed.
