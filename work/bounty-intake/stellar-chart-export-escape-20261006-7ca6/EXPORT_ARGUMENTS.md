# Pass chart export filename and format as positional arguments

## Change

The local helper in `src/lib/chart-export.ts` declares `exportChart(chartElement: HTMLElement, filename: string, format: ExportFormat = 'png')`. Both the chart export button and exported hook instead pass `{ filename, format }` as its second argument and omit its third argument.

This patch changes those two calls to `exportChart(chartRef.current, filename, format)`. It adds and removes one line in each caller, for +2/−2 overall. The helper and every other caller byte are unchanged.

The mismatch is directly visible in the acquired source. Its second argument is incompatible with the helper's declared string parameter. If the old source is emitted and executed, the omitted third argument selects the PNG default even when the control supplied SVG to its own handler, and the object reaches the helper's filename template. Those consequences are source-level deductions, not observed browser downloads or a recorded compiler run. The corrected call passes the computed name and selected format into their declared positions.

## Inputs and composition

All donor files are pinned to [Stellar-Analysis/frontend at 482ee456369418ef82c4056718cb82d3468f762b](https://github.com/Stellar-Analysis/frontend/tree/482ee456369418ef82c4056718cb82d3468f762b).

| Input | Git blob | Bytes |
| --- | --- | ---: |
| src/lib/chart-export.ts (unchanged helper) | f95cf7581b2f68abfd9ea2a4a853f025b6ab5af7 | 1327 |
| src/hooks/useChartExport.ts (donor) | f418fd627969ac49a731801d1a4a7ebc6b94f732 | 1011 |
| src/components/charts/ChartExportButton.tsx (donor) | 9e3cf18fd486344169da57ce11b76df517afbde9 | 3135 |
| ChartExportButton.tsx after the preceding Escape packet | dc91bd10b8d59ca5f39709b0995e286e4274e28c | 3595 |

Apply the existing `escape-dismissal.patch` from [Commons #31944](https://github.com/woahwhattheheck/commons/pull/31944) first, then this `export-arguments.patch`. The button change is an incremental continuation over that exact postimage. The hook is changed directly from its acquired donor preimage. Nothing in #31944 is recomputed or republished.

| Output | Git blob | Bytes |
| --- | --- | ---: |
| ChartExportButton.tsx after both patches | 94a4ffa0cda9b96a0e8dc35ec5c548c09647d54e | 3591 |
| useChartExport.ts after this patch | ab3c0b07875afc471b44c627ec8bac302758fb7b | 1007 |
| export-arguments.patch | 225ddc9bde2e6b74814886d56a3b0895dc0e2e83 | 1140 |

The acquired Network route (`src/app/[locale]/network/page.tsx`, blob `cfcb9fba468523f2e5069002680a4f4c7c8e4802`, 12424 bytes) imports and renders PaymentVolumeChart. That component (`src/components/charts/PaymentVolumeChart.tsx`, blob `2a80a9912dc883b1e13a6f033de6536a06ecfac7`, 7020 bytes) renders ChartExportButton for its nonloading, nonempty series. This establishes the mounted source consumer. It does not establish current live data or an observed user export.

The hook directly imports and calls the same helper; a mounted useChartExport hook consumer has not been established. Correcting its identical declared-argument mismatch preserves the exported hook interface without claiming an additional mounted route.

## Verification and limits

Each complete source input matched its native identity and independent Git blob identity. The two actual serialized unified hunks contain 16 complete rows. Forward text application exactly produces each postimage, and inverse application exactly recovers each preimage. Replacing the new call text with the old call text reproduces every other source byte exactly.

Existing filename normalization, date suffix, ref/loading guards, exporting state, await, error behavior, finally cleanup, hook dependency array and the button's JSX—including its new Escape handling—are unchanged. The helper still implements PNG/JPEG/SVG branches, styles, generated data URLs, link creation and click behavior as before.

No TypeScript compiler, application, hook, DOM, keyboard, image library, browser download, fixture or test was executed. This does not establish a clean build or whole export workflow. In particular, the existing nullable chart-reference prop typing and remaining menu keyboard behavior noted in the prior guide are outside this call-argument correction.

Two new files are added to the existing packet directory. The preceding README and all three unchanged upstream MIT notices remain the attribution/license basis; their exact hashes and source history are documented in `README.md`. This is an attributed Commons source proposal, not upstream publication, deployment, acceptance or a reward claim.

Bounded exact Commons PR and public Slack searches for exportChart plus filename returned no matches before this continuation was frozen. Slack reported native pagination end. These observations do not establish exclusive ownership or complete history coverage.

The preselected publication checks require complete immutable text/native/independent identities for both added artifacts and final PR/files/merge/main metadata. Named-main equality may alias verified immutable reads only when it equals the verified merge; otherwise each new artifact is read once at the observed main pin. The release and completion index record the actual result.
