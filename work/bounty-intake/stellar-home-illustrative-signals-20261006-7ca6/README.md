# Label the home-page signal figures as illustrative

The locale home route presents settlement velocity, active corridors and liquidity depth as animated signals. In the complete acquired source, those figures and their status words come directly from a fixed local array. There is no request, subscription, external input or timestamp attached to this array, and the rendered signal section has no example qualifier.

This patch adds one visible paragraph immediately before the three figures:

> Illustrative figures shown for demonstration.

The paragraph sits inside the existing grid and spans its three columns at the existing medium breakpoint. The signal array, status words, animation implementation, links and other page content remain byte-exact. The correction identifies the provenance of this presentation; it does not supply measurements.

## Actual entry and input

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).

Pinned donor commit: `482ee456369418ef82c4056718cb82d3468f762b`.

Actual App Router entry: [src/app/[locale]/page.tsx](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/app/%5Blocale%5D/page.tsx). This is the locale home route itself, not an inferred mount from a component filename.

| Identity | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Complete acquired input | `9fa7d4f61067b54862de7ad709581ca657bc2e7c` | 7,917 |
| Exact candidate postimage | `c62741eaf5570b003edfe9370d86313ccd0a58d4` | 8,080 |

The native immutable blob response supplied the complete content but no separate returned SHA field. The request bound that content to the specified blob, and an independent Git blob computation matched the input identity and byte count. Both strings end with one newline.

The bounded path-history request at the donor commit returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888, with message “refactor: flatten frontend/ into repo root, eliminate parent/child duplication.” This is path-history evidence, not proof of sole authorship. Assertions about builds in that historical commit message were not repeated or adopted as validation of this change.

Root and CI reported no exact same-path disclosure completion or hold in their retained custody. That is a bounded coordination observation rather than a global absence claim. This home route is separate from completed dashboard, rankings, health, internal-monitoring and chart provenance packets.

## Source-supported provenance

The complete module directly defines these local tuples:

| Signal label | Fixed value | Fixed status |
| --- | --- | --- |
| SETTLEMENT VELOCITY | 98.4% | STABLE |
| ACTIVE CORRIDORS | 142 | TRACKED |
| LIQUIDITY DEPTH | $2.8B | OBSERVED |

The render maps this array into the three cards. Its local AnimatedStat component parses the supplied string and animates from zero to that fixed numeric target when it enters view; the component's effect returns controls.stop() for its existing animation cleanup. The animation does not acquire a network measurement or substantiate the displayed status.

The added wording makes the section's illustrative nature visible next to its figures. The source establishes fixed examples; no claim is made about the true current settlement percentage, corridor count, liquidity depth, metric definitions, backend availability or actual financial value.

## Exact change and compatibility boundary

The patch is +3 / -0 in this one source file. It inserts a paragraph before the existing signals.map expression. The new paragraph uses the page's existing landing-muted text color and spacing conventions; the existing medium three-column grid receives a medium column span for this paragraph.

All existing bytes before and after the insertion match the acquired input. No array value, status, animation callback, animation cleanup, effect dependency, duration, viewport behavior, link, route, input or network operation is changed. No new dependency, data source, storage policy, timestamp or telemetry producer is introduced.

The page's existing English copy remains the basis for this English addition. This packet does not claim translation completeness or a broader accessibility/layout result. The visible paragraph is authored source; browser rendering, contrast, animation, responsive presentation and assistive-technology behavior were not exercised.

This is an additive Commons patch-plus-guide packet for downstream application to the exact donor. It does not mutate the upstream frontend repository or assert deployment. A downstream maintainer should inspect current composition before applying it if the donor page has since changed.

## Instructions, attribution and validation

Previously retained complete donor tree metadata at the pinned commit has no AGENTS or RULES file. The separately retained docs/CONTRIBUTING.md, blob `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2`, explicitly concerns EventSource and its test/release process; this packet does not change or release EventSource.

The three differently attributed license notices already preserved in [the generator continuation packet](../stellaranalysis-issue-generator-layout-20261006-7ca6/) are retained as notices, without inferring a repository-wide license scope. The packet republishes only the narrow patch and this guide, not the full upstream page. Existing source authorship is preserved.

Validation consisted of reading the complete actual route, inspecting its local producer and render path, exact insertion/reconstruction, unchanged-section comparison and independent UTF-8/Git blob identities. The source was not executed. No shell, compiler, TypeScript check, lint, test, fixture, browser, build, animation, network request, workflow or prior accepted publication was run or replayed for validation. No whole-build or deployment success is claimed.
