# Show the existing empty diagnostics on the Anchor detail route

The actual Anchor detail page already provides “No failure data available” and “No recent failures” messages. Its two conditions use optional-array map results with a logical-OR fallback. An empty array maps to another empty array, so that truthy result bypasses the existing fallback and leaves the diagnostics section blank.

This patch selects the existing populated markup only when the corresponding array has a nonzero length. An absent or empty array selects the existing fallback. No new copy, loading policy, data normalization or backend behavior is introduced.

## Exact source and data contract

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/anchors/[address]/page.tsx` | `71fea1bb40c29bcbba0657ba1cb10a65d35fab23` | 7,297 |
| `src/lib/api/types.ts` | `eb5891a5f04e33eb29757cf57c623f9b7d4ab3b5` | 3,140 |
| `src/lib/api/anchor.ts` | `4c0b6ee29936b17fe97944bc818d460d8ff37c44` | 4,244 |

This is a directly mounted App Router page under the existing address route, reached by the acquired Anchors views' Details links. Its effect calls `getAnchorDetail(address)`, stores the returned `AnchorDetailData`, and renders these diagnostic arrays after the existing loading/error conditions. The adapter returns the existing typed API response; no endpoint was invoked.

The actual type declares `top_failure_reasons?: { reason: string; count: number }[]` and `recent_failed_corridors?: { corridor_id: string; timestamp: string }[]`. Both arrays may be absent or empty under that contract. No nonempty-array guarantee or client filtering excludes the empty case in the acquired path.

## Minimal patch

`show-empty-diagnostics.patch` changes only the two JSX conditions: each optional `map`/OR expression becomes a length-controlled conditional selecting its existing map or existing fallback.

Source identity: `71fea1bb40c29bcbba0657ba1cb10a65d35fab23` (7297 B) → `749e702f2a5085e232847ab55dcd804e1ec747a6` (7367 B), **+4/-4 in four hunks**. The original final newline is preserved.

For populated arrays, every mapped element, key, class, text, field and timestamp formatting expression remains byte-for-byte unchanged. For absent arrays, the same fallback text/classes remain. Explicitly empty arrays now reach that fallback as intended by the existing presentation. Address validation, fetching, logging, loading/error branches, links, header, chart, asset portfolio and all other source bytes remain exact.

The complete serialized patch and inverse reconstruct the full postimage/preimage and their Git blob identities. These are static source-integrity checks, not execution of a fixture, data example, React render or application. The complete route was acquired once for this genuinely new consumer; prior list/helper source corrections were not replayed or changed.

The correction does not strengthen validation of malformed payloads, null elements within populated arrays, negative counts or invalid timestamps. It does not add request cancellation, retry controls, new accessibility semantics or a real-time diagnostics guarantee. It does not claim that any particular live record currently has empty diagnostics.

## Attribution and source boundaries

Original implementation credit and contributor rights remain upstream. Bounded current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`; the relocation is not treated as sole authorship or as runtime validation of this patch. Earlier history was not reconstructed. Exact scoped Commons/public Slack queries for top_failure_reasons and empty supplied no competing carrier; these are bounded results, not global absence.

The retained complete donor tree contains no root AGENTS/RULES path. Acquired docs/CONTRIBUTING.md is EventSource-specific and does not override the explicit current no-tests/no-runtime/no-upstream-publication scope. Differently attributed MIT notices in documentation do not establish a repository-wide code licence. This Commons contribution therefore contains only a minimal patch and this original attributed guide, with immutable source identities.

The five completed Anchors list/search-control concerns remain in their existing packets and are untouched. No application, browser, test, fixture, API request, account/user data, upstream branch/PR/comment, author assignment, sponsor acceptance, bounty award or payment was performed or claimed.
