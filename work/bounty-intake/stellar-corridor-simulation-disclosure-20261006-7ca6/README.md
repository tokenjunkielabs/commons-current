# Disclose simulated live updates on the corridor listing

## Why the visible notice is needed

The mounted corridor listing fetches rows from getCorridors and stores the successful result. A separate effect runs for the lifetime of the component and, every 3,200 milliseconds, maps over the current rows using Math.random. It changes success_rate, health_score and liquidity_volume_24h_usd. The interval is unconditional: it also applies to rows loaded successfully from the backend, rather than only the mock fallback.

The cards show these mutable values as success rate, Health Score and 24h Vol, and the same current rows feed the health-map view. The acquired listing does not visibly disclose the simulated updates. A reader therefore lacks source context for numbers that can change between backend requests.

This is a source-level observation about the mounted component. No live backend response, simulation tick, user data or browser display was observed.

## Complete source and actual caller

Donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at `482ee456369418ef82c4056718cb82d3468f762b`.

The complete source is [src/app/[locale]/corridors/page.tsx](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/app/%5Blocale%5D/corridors/page.tsx). Its default App Router export renders CorridorsPageContent inside the existing ErrorBoundary and Suspense. The acquired file includes the real data assignment, simulation effect, two view branches and heading that receives the notice. No hypothetical consumer or reconstructed file is used.

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Complete donor source, native and independent identity | a14fe86977c4071ad958ddc3f206b4f07134b072 | 17815 |
| Prepared complete postimage | d68d3579560bb4f5fe4c1046233334d8e461b2ef | 17953 |
| disclose-simulated-updates.patch | b78c11d66ecb3374261d8de54956864e304b5aa4 | 525 |

The bounded current-path history returned commit 482ee456, attributed to Ndifreke000, and relocation commit 59fad72d9fbef9cfd6f47e215392da44488fcdc4, attributed to christabel888. These entries are not a complete authorship history or a claim of sole authorship. All original source attribution and the three complete acquired MIT notices are preserved.

## Minimal visible correction

The patch inserts one paragraph immediately below the Payment Corridors heading:

> Displayed metrics include simulated live updates.

The existing text-sm and text-muted-foreground utility classes style the paragraph; mt-2 separates it from the heading. Its scope is the displayed metrics in both listing views. It does not label every value as simulated or claim that all source data are mocks.

The paragraph is present while loading and after loading because simulation is a configured behavior of this mounted page. It is descriptive text, not a live-region announcement and not an observed tick count. This does not provide row-level provenance, a last-update time, a simulation toggle or a measured freshness guarantee.

## Preserved source behavior

Every pre-existing byte remains exact. The patch does not change the random-walk formula, bounds, three updated fields, 3,200 ms interval or its cleanup. Backend loading, mock fallback, insights, filtering, sorting, pagination, user preferences, navigation, grid/heatmap selection and export dialog remain unchanged.

This notice does not assert that the underlying displayed values are suitable for operational decisions. It discloses the existing simulation without selecting a new data policy. Other completed pagination or export proposals are not reapplied, reconstructed or reverified; this new hunk only inserts the heading paragraph at the complete canonical source.

The existing application copy is English, and this correction follows that source. No translation or broad accessibility assessment is claimed.

## Exact text verification

The serialized patch contains 1 hunk and 9 rows, with 3 additions and 0 deletions. Forward application of the actual serialized hunk reconstructs the complete postimage, and inverse application restores the complete preimage. Removing the inserted paragraph restores every other page byte.

These are source and serialization checks. No React component, interval, Math.random call, metric calculation, API request, browser, compiler, lint command, fixture, test, build or workflow was executed. The notice has not been visually validated in a browser.

## Bounded overlap and publication

The exact-path/simulated Commons search returned only the existing #31453 grouped index header. Retained completed maps distinguish the separate Anchors trend labels and /performance and /internal/monitoring packets from this listing paragraph. The own index body and comments were not reread. The paired Slack search returned zero rows with native END. This bounded evidence is not a global absence, ownership or acceptance clearance.

Publication is an attributed Commons source proposal, with no upstream mutation or deployment. The prepared packet contains this patch, this guide and these unchanged original notices:

| Notice | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| upstream-licence-mclaughlin.md | 57740b9d4d86aedf5d518f2f363d5cf192c54127 | 1104 |
| upstream-license-menke-laguna.md | af5411fa243cfcf2b61c79d081dbb6204e956041 | 1111 |
| upstream-license-de-wet.md | 4a766e268772888af5df56c3f6c608f68558b789 | 1080 |

All five complete immutable artifact bodies require native plus independent identity matches, followed by exact PR/files/head/merge/parents/tree/main metadata. If fresh named main exactly equals the verified merge, the receipt may explicitly reuse those complete bodies. Otherwise each artifact is read once at the observed immutable main commit. Actual publication identities belong in the separate release and grouped index.
