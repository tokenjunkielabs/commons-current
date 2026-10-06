# Label the Anchors illustrations as simulated

The mounted Anchors table and cards display randomly generated sparklines as “30-Day Trend” and “30-day trend.” This patch changes both visible captions to **“Simulated trend”**. The source already generates illustrative data; the correction makes that limitation visible to the person using the page.

## Source and mounted caller

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), commit `482ee456369418ef82c4056718cb82d3468f762b`.

The actual App Router `src/app/[locale]/anchors/page.tsx` renders `AnchorsPageContent`. That component passes the same `paginatedAnchors` to `AnchorList` from `AnchorTable.tsx` and to `AnchorCards`. Existing responsive classes select the table on large screens and the cards on smaller screens.

| Complete source input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/anchors/page.tsx` | `80899e99b202a254f6688173404b8131e475f752` | 1,339 |
| `src/app/[locale]/anchors/components/AnchorsPageContent.tsx` | `5ba7f36fa3f2cca6f91e2caaad16b2d88a564625` | 8,115 |
| `src/app/[locale]/anchors/components/AnchorTable.tsx` | `58a190ccc4689b2fd097d456437047a4d8852da0` | 10,079 |
| `src/app/[locale]/anchors/components/AnchorCards.tsx` | `d28c319c43ada775ba7320c87759f83840becc1b` | 6,157 |
| `src/app/[locale]/anchors/components/helpers.tsx` | `ec1f18bb63d62f4a6a99203bb1baf45cfb93fb16` | 5,665 |
| `src/lib/api/anchor.ts` | `4c0b6ee29936b17fe97944bc818d460d8ff37c44` | 4,244 |

Both complete views call `generateMockHistoricalData(anchor.reliability_score)` during rendering. The fully acquired helper creates 31 values using `Math.random()`, bounds the scores to 0–100, and assigns dates from the current clock. Both views pass `historicalData.slice(-7)` to their line chart. Thus these plots are generated illustrations around the current score, not acquired historical measurements. The API module was read as data-contract context; it does not change the directly observed producer used by these two plots.

## Exact change

Apply `label-simulated-trends.patch` to the pinned donor. It changes **two lines in two hunks (+2/-2)** and preserves both source files' existing lack of a final newline.

| Production path | Before blob | After blob | After bytes |
| --- | --- | --- | ---: |
| `src/app/[locale]/anchors/components/AnchorTable.tsx` | `58a190ccc4689b2fd097d456437047a4d8852da0` | `f34f8fd1ffbfa8074be53d2fdf1a001efc44ef63` | 10,082 |
| `src/app/[locale]/anchors/components/AnchorCards.tsx` | `d28c319c43ada775ba7320c87759f83840becc1b` | `480458025426c4bf454141b25f1b38ae4eea0ec1` | 6,160 |

All chart inputs, random generation, date generation, seven-sample slicing, scores, colors, dimensions, links, row handlers, sort controls, transaction calculations, pagination and API behavior remain exact. The caption deliberately makes no measured 30-day or seven-day coverage claim. Replacing the generated series with backend history would require a separate actual data contract and is not implemented here.

The serialized patch and inverse reconstruct the full recorded postimages and preimages exactly. Complete native source bytes were independently checked against Git blob identities. These are source-integrity checks; no application, generator, example, fixture, build, browser, test, API request or user data was executed or accessed.

## Attribution and boundaries

Original implementation credit and all original contributor rights remain with the upstream authors. Bounded current-path history returned the repository-flattening commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888` for both modules. That move is not claimed as sole authorship, and its historical validation statement is not adopted as validation of this patch. Earlier pre-relocation authorship was not reconstructed.

The exact Commons PR overlap query for anchors/simulated/trend returned zero with incomplete_results=false; that is a bounded lexical result, not a global absence claim. The public Slack query returned one unrelated historical recovery/proof-topic result, which supplied no Anchors source carrier and was not followed. Existing privacy, account, runtime and failed-route holds remain.

The retained complete donor tree had no root AGENTS/RULES path. Its acquired docs/CONTRIBUTING.md is EventSource-specific and includes test/release instructions; the explicit current no-runtime/no-tests/no-publication-to-upstream scope remains controlling. Differently attributed MIT notices in documentation do not establish a repository-wide source licence here. This Commons contribution therefore contains only the minimal patch and this original guide, with pinned attribution rather than a copied production module.

This is a source-only presentation correction in Commons. It does not establish real trend data, data accuracy, hydration determinism, localization, zero-denominator behavior, nested-control keyboard behavior, rendering quality, accessibility acceptance, backend integration or whole-issue readiness. No upstream branch/PR/comment, author assignment, sponsor acceptance, bounty award or payment is asserted.

## Separate continuation: keep nested link keys out of the parent handler

The complete table and cards also contain a source-backed event-ownership defect. Each focusable row/card has an Enter/Space handler that calls `preventDefault()` and `router.push()`. Each also contains a Details Link whose existing click handler stops click propagation. A keyboard event from that nested Link still reaches the parent key handler; the click-only stop does not guard that event.

`preserve-nested-link-keys.patch` adds the same early return in both parent key handlers when `event.target !== event.currentTarget`. Events originating on a descendant now reach this handler without it cancelling the default or invoking its router action. Events originating on the row/card itself retain the original Enter/Space behavior.

| Production path | After #32003 / before this patch | After this patch | Bytes before → after |
| --- | --- | --- | --- |
| `src/app/[locale]/anchors/components/AnchorTable.tsx` | `f34f8fd1ffbfa8074be53d2fdf1a001efc44ef63` | `30aa2abab512ed808301fd9d91a892289722292a` | 10082 → 10192 |
| `src/app/[locale]/anchors/components/AnchorCards.tsx` | `480458025426c4bf454141b25f1b38ae4eea0ec1` | `ac3648cb3d41d7c88cccc3747097015d8447b866` | 6160 → 6258 |

Apply this incremental patch **after** `label-simulated-trends.patch` from [Commons #32003](https://github.com/woahwhattheheck/commons/pull/32003). It adds six lines in two hunks (+6/-0). Both simulated captions, chart/producer logic, hrefs, router destinations, parent click handlers, nested click stopPropagation, roles, tabIndex values and all other source bytes remain exact. The original no-final-newline convention is preserved.

The [primary React event-object reference](https://react.dev/reference/react-dom/components/common#react-event-object) defines currentTarget as the node owning the current React handler and target as the originating node, which may be a descendant. It also distinguishes default cancellation from stopping propagation. React's [event propagation guidance](https://react.dev/learn/responding-to-events#event-propagation) supplies the bubbling contract. These support the guard without a native event or browser execution.

The complete retained preimages were inputs to this new correction, not replayed accepted-source validation. Serialized forward/inverse application reconstructs both complete identities. A fresh Commons lexical AnchorTable/keyboard PR query returned zero; public Slack returned only this packet's own earlier release header. Neither is a global absence claim. Original source attribution and instructions above remain.

This correction concerns only these parents' key handling. It does not redesign nested interactive markup, establish table/card or whole-page accessibility, implement localized routes, change modified-key handling on the parent itself, add focus management, control other ancestor handlers, or guarantee browser/assistive-technology behavior. No runtime, keyboard simulation, test, browser, navigation request, API, upstream action, author assignment, acceptance or payment claim is made.
