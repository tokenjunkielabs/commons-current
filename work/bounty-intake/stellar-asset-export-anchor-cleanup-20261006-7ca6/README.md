# Remove the AssetPortfolio export anchor on failure

The mounted AssetPortfolio export handler currently removes its temporary download anchor only after all attribute setup, insertion and click operations return successfully. If an operation throws after insertion, that attempt can leave the anchor attached to the document.

This patch places the existing attribute/append/click sequence in a try block and calls the acquired anchor's remove method in finally. Successful removal still happens immediately after click returns. No CSV contents, filename, filtering, sorting or asset selection behavior is changed.

## Actual mounted source

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), immutable commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/components/anchors/AssetPortfolio.tsx` | `1801c67028bb96c8b69c8c6d23f47ba45ad0a920` | 6,015 |
| `src/app/[locale]/anchors/[address]/page.tsx` | `71fea1bb40c29bcbba0657ba1cb10a65d35fab23` | 7,297 |
| `src/lib/api/types.ts` | `eb5891a5f04e33eb29757cf57c623f9b7d4ab3b5` | 3,140 |

The actual App Router detail page imports AssetPortfolio and renders it with `data.issued_assets` after its existing loading/error branches. AssetPortfolio renders its Export CSV button with `onClick={handleExport}`. This is a connected production handler, not an unused helper. The acquired source uses a fresh local anchor for each invocation; no shared node is removed.

The page's separate diagnostics correction in [Commons #32032](https://github.com/woahwhattheheck/commons/pull/32032) preserves this import/render chain. That accepted change is neither replayed nor included here.

## Narrow source change

`remove-export-anchor.patch` changes only `src/components/anchors/AssetPortfolio.tsx`: **+11/-8 in one hunk**.

Full source identity:
`1801c67028bb96c8b69c8c6d23f47ba45ad0a920` (6,015 B)
→ `14bdc6d5dddd533b403e69f071be2ffe5d5e6a71` (6,045 B).

The try block begins only after the anchor is acquired. Its href, download name, append and click statements retain their order and arguments. Finally calls `link.remove()`, which removes that node from its current parent and is a no-op if unattached, as documented by [MDN's Element.remove reference](https://developer.mozilla.org/en-US/docs/Web/API/Element/remove). No custom DOM implementation or throwing-cleanup guarantee is asserted.

Blob creation, object-URL creation, CSV/header/row formatting, export ordering, date-based filename, all control state and every JSX byte remain exact. Exceptions continue to propagate; no success acknowledgement, catch policy or retry flow is added. A cleanup exception can replace an earlier exception.

## Explicit remaining boundary

The original handler also never revokes its object URL. This packet deliberately leaves that existing behavior unchanged. Successfully retained prior URL documentation says to revoke after finished use, but it does not establish download completion or safe immediate post-click timing for this caller. No new URL lifetime schedule is invented.

The later exact MDN revokeObjectURL lookup failure remains held; it was not retried or acquired by an alternate route. A teammate transferred only already-successful primary documentation from its earlier independent task, without a new provider request. That retained contract is not treated as evidence that this download has completed.

No browser, clipboard, download, Blob construction, live asset data, network endpoint or application handler was executed. Serialized forward and inverse patch reconstruction match the complete preimage and postimage with independently calculated Git blob identities. These are source-integrity checks, not runtime behavior or a whole-build result.

## Attribution and publication scope

Original contributor rights remain upstream. Bounded current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`; relocation is not treated as sole authorship. Exact bounded Commons and public Slack queries for AssetPortfolio and cleanup returned no competing carrier, not a global absence guarantee.

The retained complete donor tree has no root AGENTS/RULES path. EventSource-specific CONTRIBUTING guidance does not override this session's explicit no-tests/no-runtime/no-upstream scope. Differently attributed MIT documentation notices do not establish repository-wide code licensing, so only this minimal patch and original attributed guide are published.

All prior Anchor list, detail and control packets remain unchanged. No upstream branch, pull request, comment, author assignment, sponsor acceptance, award, payment or full issue completion is claimed.
