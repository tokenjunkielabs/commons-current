# Preserve empty monitoring data on the Performance page

The existing Performance route substitutes random values when its stored monitoring arrays are empty. Those values are displayed beneath “Real User Monitoring — Web Vitals, API latency, and error rates” without a mock-data label. The Web Vitals generator deliberately stays in the “good” band, while the API and error generators also create observations that were never read from storage.

This packet removes those fallbacks. Empty Web Vitals and API summaries stay empty; an empty stored error list yields an empty timeline and a recorded count of zero. The page already has empty-state JSX for all three sections, so those messages remain visible instead of being replaced by generated charts.

## Exact source and patch

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).

Donor commit: `482ee456369418ef82c4056718cb82d3468f762b`.

Changed path: [src/app/[locale]/performance/page.tsx](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/app/%5Blocale%5D/performance/page.tsx), mode `100644`.

| Identity | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Complete donor file | `c121b1d6509a91a6242f744c7a5a89e60b94166a` | 9014 |
| Prepared postimage | `b776ae57e7a5f1f832e08af087e8dcfddfcd67fe` | 7090 |

The adjacent `change.patch` has four hunks, **4 additions and 54 deletions**. It applies directly to the exact donor file. No prior Commons patch to this route is required or represented.

The patch removes `generateMockVitals`, `generateMockApiLatencies`, and `generateMockErrorTimeline`. It replaces the two conditional fallback setters with `setVitals(vitalsSummary)` and `setApiLatencies(latencies)`, and always sets the error count/timeline from the parsed stored error array.

All existing aggregation, metric thresholds, rating logic, chart rendering, labels, local-storage keys, storage reads, and effect timing are unchanged. In particular, this patch does not generate example measurements, invoke a random generator, replay a collected measurement, or introduce a replacement data source.

## Connected entry and data boundary

The acquired file is the actual App Router page at `src/app/[locale]/performance/page.tsx`, exporting `PerformancePage` as its default. This establishes a route entry in the current source. No browser navigation, mounted runtime, or particular navigation-menu link was observed for this packet.

The effect reads `mon_metrics` and `mon_errors` from local storage and parses absent values as `[]`. It derives the three display datasets from those arrays. The source itself establishes the empty-data path that previously called the random generators; no constructed input or app execution was needed to identify it.

The complete related [src/lib/monitoring.ts](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/lib/monitoring.ts) was acquired as source context at blob `fdf6678ad469ae6e375a8fd7f31ff28defd8ced2`, **4120 UTF-8 bytes**. It exports the `Metric` and `AppError` interfaces used by the page. Its monitoring singleton buffers observations and sends them to `/api/metrics/frontend`; that complete module does not write the two local-storage keys read by this page.

Consequently, this packet does not establish or repair a live producer-to-storage connection. A zero stored error count means that the parsed stored list is empty. It is not a claim that the backend, all sessions, or the application as a whole experienced no errors.

## Current source qualification and attribution

A fresh native `branches/main` read returned the donor commit above. A bounded five-entry path-history request at that commit returned one root-path entry: `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, the root relocation attributed to `christabel888`. That bounded root-path history does not identify every earlier author or establish complete history across the relocation.

A bounded all-state repository PR search for `performance` returned eleven connector headers. The search envelope supplied null state/date fields and no pagination evidence, so the result is not treated as an exhaustive carrier search. The related telemetry [PR #118](https://github.com/Stellar-Analysis/frontend/pull/118) was separately observed closed and merged, attributed to `favourawaku`, at head `3b3080b3ef1ce23f44318a6ab5cc4ebc66e7881d`; its complete returned twelve-file list does not include this route. Its work remains credited and unchanged.

The fleet reported no exact retained owner, completion, or hold for this route. That is a bounded custody statement, not proof of globally absent ownership. The unrelated ambiguous Telemetry 404 hold was preserved and was not retried or recovered through another route. Existing private, source-access, and upstream-author constraints remain intact.

This Commons continuation supplies a source patch and explanation. It makes no upstream assignment, submission, merge, deployment, acceptance, or payment claim.

## Review and limits

The complete donor page and monitoring utility were read once for this new source task using native blob requests. Those responses supplied content without a separate returned SHA field. Each complete UTF-8 text was independently hashed and matched its exact request-bound Git blob and byte count.

The postimage was prepared by removing the specific generator block and replacing the three unique fallback sites. The diff and exact pre/post identities above describe the resulting source. The JSX empty states and the observed-data aggregation remain byte-preserved.

No frontend code, React effect, browser, storage operation, metric producer, random generator, build, compiler, linter, tests, fixture, workflow, server, or upload was run. There is no runtime or whole-build success claim.

Existing concerns remain outside this change: malformed or inaccessible storage, record validation, metric-name normalization, unsupported metric ratings, timing/refresh behavior, the error-timeline comment versus its actual bucketing/filtering, and the producer/persistence gap. No new policy for these areas is implied by preserving empty arrays.

## Packaging

The packet contains only the narrow patch and this guide. No repository-wide licence scope was established for the acquired frontend tree, so the complete donor module is not republished.

The separately attributed MIT notices already retained in Commons under `work/bounty-intake/stellaranalysis-issue-generator-layout-20261006-7ca6/` remain unchanged:
- `upstream-licence-mclaughlin.md`: `57740b9d4d86aedf5d518f2f363d5cf192c54127`
- `upstream-license-menke-laguna.md`: `af5411fa243cfcf2b61c79d081dbb6204e956041`
- `upstream-license-de-wet.md`: `4a766e268772888af5df56c3f6c608f68558b789`

Those notices are not assigned a repository-wide scope by this packet.
