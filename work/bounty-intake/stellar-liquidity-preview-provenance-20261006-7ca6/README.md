# Identify the liquidity terminal as a demonstration

The mounted liquidity page labels its loading step as measurement, displays a high-accuracy-stream badge, and says automated capital rebalancing is active. Its complete acquired module instead contains an 800 ms presentation timer, fixed overview values and trends, empty arrays passed to both chart children, and no request, subscription or rebalancing invocation in the page itself.

This parent-only patch gives that presentation a coherent preview label. It changes the loading copy to “Loading Liquidity Preview... // 303-D”, adds “Illustrative liquidity overview with fixed example figures.” below the title, changes the badge to DEMONSTRATION, and describes the provisioning section as a preview. It preserves the timer, figures, trends, chart props and children.

## Exact source and mounted boundary

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).

Pinned donor: `482ee456369418ef82c4056718cb82d3468f762b`.

Actual entry: [src/app/[locale]/liquidity/page.tsx](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/app/%5Blocale%5D/liquidity/page.tsx). This module exports the locale liquidity App Router page. No separate caller was inferred from its name.

| Identity | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Complete acquired input | `5b0d98d58f3277a540d79ef6d7128483a2c144c8` | 5,061 |
| Exact candidate postimage | `5faf308140cd9533134edf72949b9472a3201837` | 5,217 |

The immutable native blob route returned full content without a separate SHA field. The request-bound blob and independent Git blob computation matched exactly. The input and postimage retain their final newline.

A bounded path-history request at this donor returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888, with the root-flattening commit message. Relocation does not establish sole authorship. Historical build assertions in that message were not run or used as validation here.

Root retained no exact same-route provenance completion. CI confirmed that its completed #32088/#32089 work targets the separate `src/app/[locale]/liquidity-pools/page.tsx` path. These are bounded coordination facts, not a global ownership or absence proof.

## Actual local producer and presentation

The only effect in the complete page creates a timeout that sets loading=false after 800 ms and clears that timeout on cleanup. It does not measure liquidity. This timer and cleanup remain exact.

The overview directly supplies these fixed props:

| Card | Value | Existing trend |
| --- | --- | --- |
| Total Liquidity Depth | $124.5M | 12.4, up |
| Slippage Index | 0.04% | -0.01, down |
| Reserve Ratio | 1.42x | No trend prop |

The page directly passes an empty data array to charts/LiquidityChart and an empty corridors array to LiquidityHeatmap. Its time-period callback for the latter is empty. The provisioning paragraph is literal text; the page does not invoke or confirm capital rebalancing. Its existing Capital Allocation Map button has no handler or link in this module.

These facts support a parent-level demonstration label. They do not prove anything about external backend activity, actual liquidity, market conditions, capital movement elsewhere, or the internal behavior of a chart child. The original $ amounts, ratios and trend props are retained as example presentation, not certified observations.

## Scope and preserved work

The patch is +6 / -3 in three hunks, all in the parent page. Four exact replacements account for the entire change: three text substitutions and one three-line explanatory paragraph.

The source's effect, cleanup, metrics, trend props, chart calls, empty arrays, callback, imports, button and existing layout remain unchanged. No request, subscription, backend operation, data validation, storage, telemetry, metric policy, time-period behavior, allocation action or replacement data source is introduced.

The existing child paths `src/components/charts/LiquidityChart.tsx` and `src/components/charts/LiquidityHeatmap.tsx` remain outside this patch. In particular, the previously completed charts/LiquidityChart continuation #31978 is preserved. This packet does not re-acquire, replay or certify those child implementations, and does not silently substitute a new chart policy. The distinct dashboard/LiquidityChart path is also untouched.

The inert allocation button remains a separate limitation; changing its behavior is not part of this provenance correction. No claim is made that the page now carries out allocation or is complete as a liquidity product. Existing English copy supplies the language for these replacements; translation completeness, rendering and broader accessibility remain unverified.

## Attribution, instructions and evidence limits

The retained complete canonical tree at the donor has 959 entries, truncated=false, no backend root and no AGENTS or RULES file. Its separately retained branch metadata identifies tree `44703ba39198f99b6541450c740db0d1c3c0f7b8`; the recursive response's SHA echoed the requested commit. No independent full-tree reconstruction is claimed.

The retained `docs/CONTRIBUTING.md`, blob `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` (274 bytes), explicitly concerns EventSource testing and release. This packet does not modify or release EventSource. Three differently attributed license notices remain preserved in [the earlier generator packet](../stellaranalysis-issue-generator-layout-20261006-7ca6/) without inferring a repository-wide license scope. This packet contains only a narrow patch and this guide, preserving source authorship.

Evidence consists of complete page inspection, exact source identities, bounded history, exact transformation/reconstruction and unchanged-section comparisons. The complete overview-and-charts source region and loading effect remain byte-exact. No source execution, shell, compiler, lint, test, fixture, browser, timer, chart rendering, API request, socket, capital operation, workflow or prior accepted check was run or replayed.

This is a Commons source continuation, not an upstream application or deployment. It makes no financial, current-measurement, runtime, whole-build, whole-issue or payout claim.
