# Preserve missing-change meaning in asset share text

TopAssetsTable treats a missing 24-hour change as unavailable in its visible table, but its share text describes the same value as having moved little. Its share button also announces X/Twitter even though the existing handler prefers the native share sheet and uses X only as a fallback.

This patch changes two strings: unavailable change is described as unavailable, and the button is named “Share” plus the asset symbol without promising a particular destination.

## Complete source and mounting

Canonical repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), immutable commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/components/dashboard/TopAssetsTable.tsx` | `efe87b0470969133301d327c646641ec62cd448c` | 7,439 |
| `src/app/[locale]/dashboard/page.tsx` | `cca99335ba0ae1f66a1fb5cea0197f5ead6b2f11` | 13,126 |
| `src/app/api/dashboard/route.ts` | `367fc3807e653a782db0ba94da56a787772ee3e6` | 9,379 |
| `src/lib/top-movers-api.ts` | `4f9af8b2161d4257ec087f4ccf52e75a245f339a` | 4,077 |

The actual client dashboard route renders TopAssetsTable with data.assets when that array is nonempty. Its API maps asset.change_24h_pct from fetchTopMovers into the child's change24h field without replacing a missing baseline with zero. The API client's complete TopMoverAsset definition documents null for absent 24-hour baseline data, and its existing source fallback includes such a value. No fallback generator, fixture or API was executed here.

The table's Asset type likewise permits null, and its visible Change cell already displays an em dash when typeof change24h is not number. The share helper used the same numeric predicate but described the other branch as little movement. Source comments mention upstream backend issue numbers; those are not newly qualified external issue/acceptance claims.

The completed dashboard page patches #32054, #32058 and #32063 preserve the TopAssetsTable import, asset mapping and render call. This child correction is independent of recovery, state ownership and data-provenance disclosure.

## Two-string patch

`describe-share-data-and-action.patch` is **+2/-2 in two hunks**:

* The existing nonnumeric branch now says “has no available 24-hour change data”.
* The existing button aria-label is “Share” plus the same asset symbol.

Source identity:
`efe87b0470969133301d327c646641ec62cd448c` (7,439 B)
→ `21209abca5836a03cebc6155d4a19052b67c8520` (7,445 B).

The complete source shows handleShare first trying navigator.share, returning after fulfillment, and returning without fallback on AbortError. Other native-share failures or absent support reach the existing encoded X/Twitter intent URL. The platform-neutral name therefore fits both existing paths. None of those operations, checks, catches, URLs or calls changes.

All numeric change wording, including the existing zero branch; price formatting; table fields; new-holder display; visual classes; row keys; and click callback remain byte-for-byte unchanged outside the two strings. No new finite-number check, numeric threshold, provider/schema assumption, sharing fallback or cancellation policy is added.

## Validation and limits

The complete serialized patch reconstructs the exact entire postimage, and its inverse reconstructs the exact preimage. Independent UTF-8 byte counts and Git blob hashes match. The patch changes no handler logic.

This is source-only work. No native share sheet, external message, X/Twitter page, clipboard, browser, account, wallet, request, runtime, synthetic fixture or test was invoked. Existing English-only share copy remains English; the dashboard's separate localized data notice is preserved. No full accessibility, localization, browser-support, data freshness or financial-data accuracy claim is made.

Missing baseline is not zero movement. The patch preserves that distinction in this particular output; it does not validate other malformed numeric values, prove live backend provenance or certify a displayed price. The inherited “today”/price wording and all existing sharing behavior remain outside the correction.

## Attribution and authority

Bounded current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`; earlier contributors retain their rights and no sole-author claim is inferred. Scoped Commons/public Slack queries for TopAssetsTable/share returned zero, which is bounded overlap evidence only.

The complete donor tree had no root AGENTS/RULES path. EventSource-specific contribution/release guidance does not override the explicit no-tests/no-runtime/no-upstream scope. Differently attributed documentation MIT notices do not establish repository-wide frontend code licensing, so only a minimal patch and this original attributed guide are published.

No upstream branch, PR, comment, maintainer assignment, sponsor acceptance, bounty/payment or whole-issue completion is performed or claimed.
