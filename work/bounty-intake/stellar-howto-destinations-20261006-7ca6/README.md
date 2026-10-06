# Match Terminal and Health guide descriptions to their screens

The mounted getting-started route directs readers to Terminal and Network Health, but describes ledger-close/throughput/fee-pressure widgets and validator-quorum/ledger-variance/live-anomaly monitoring. The complete destination source instead renders payment/corridor/liquidity/settlement summaries and anchor health with generated examples.

This correction changes the two destination descriptions and the hero's blanket real-time promise. It does not change navigation or destination behavior.

## Source custody

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at immutable commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Actual complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/how-to-use/page.tsx` | `30e9e18baa9c892e68d619d1766d0e09ea443b4b` | 5,348 |
| `src/app/[locale]/dashboard/page.tsx` original | `cca99335ba0ae1f66a1fb5cea0197f5ead6b2f11` | 13,126 |
| `src/app/api/dashboard/route.ts` | `367fc3807e653a782db0ba94da56a787772ee3e6` | 9,379 |
| `src/app/[locale]/health/page.tsx` | `5bd72d0758c6b99e19c74f79c725dc052ff60f18` | 140 |
| `src/components/health/health-dashboard.tsx` original | `d77d90f443f2571f4cbe077bcec82c0bd8a572b0` | 15,761 |

The newly acquired guide is an actual App Router page. Its existing steps link to /dashboard and /health through the already localized Link. Full destination and producer bodies were retained from earlier distinct work and are used here as input to a new description correction, without revalidation or execution.

The dashboard renders payment-success rate, corridor count, liquidity depth and settlement-speed KPI cards, plus assets, corridors and liquidity/settlement histories. Its retained producer generates chart histories, and the page has simulated updates. The health route mounts HealthDashboard, which derives summaries from anchors and generates history and incident examples. These are bounded findings from those complete modules, not a claim about all application routes or backend services.

Existing Commons continuations remain separate: the dashboard disclosure from #32063 has page postimage `31d966464f3fa7e66d960be53a02f56a1707a500` (13,356 B), and health provenance #32082 has component postimage `881fc7b7823d1813114a0ce7bc572d145b7a8c68` (16,155 B). Their source artifacts are not rewritten. The new descriptions agree with both the original data-producing behavior and those disclosed compositions.

## Narrow copy correction

`describe-actual-guide-destinations.patch` is **+4/-4 in three hunks**, affecting only the how-to route:

* Terminal points readers toward its actual four summary categories and acknowledges simulated histories/updates.
* Network Health describes anchor reliability, simulated history and sample incident entries.
* The hero describes exploring screens and notes that some views include representative or simulated values.

Source identity:
`30e9e18baa9c892e68d619d1766d0e09ea443b4b` (5,348 B)
→ `6153b36d6f1e968f5fe2624d6bdee1dedf58d901` (5,326 B).

Links, hrefs, labels, step order, icons, layout, metadata and every other instruction remain exact. The existing wallet, corridor, liquidity, analytics and notification-tip claims are unselected; this packet does not certify the whole guide. It does not add a route, transport, analytics feature, financial policy, account operation, notification permission or instrumentation.

The source strings remain English as before. No response-specific provenance flag or whole-app localization claim is added.

## Validation, attribution and limits

The full serialized patch reconstructs the postimage, and its inverse reconstructs the preimage. Independent UTF-8 counts and Git blob identities match. This is retained-source reasoning and literal source validation only: no app, endpoint, fallback generator, simulated update, test, fixture, browser, wallet, account, notification or backend operation was executed.

A bounded five-entry path-history request returned the relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`; no sole-author inference is made. Existing contributors retain their attribution and rights.

New dedicated Commons PR and public Slack searches for how-to-use plus dashboard returned zero. The PR tool supplied no completeness/pagination flag; these are bounded overlap observations, not proof of global absence. No held or failed route was retried.

The donor's complete tree had no root AGENTS/RULES path. EventSource-specific guidance does not override explicit no-runtime/no-tests/no-upstream instructions. Differently attributed documentation license notices do not establish a whole-frontend license, so this Commons publication contains a minimal patch and original attributed guide only. No upstream PR, maintainer acceptance, sponsor/bounty/payment or whole-issue completion is claimed.
