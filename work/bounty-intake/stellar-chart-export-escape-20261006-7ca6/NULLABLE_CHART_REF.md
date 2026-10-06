# Accept the actual caller's nullable chart ref

## One-line compatibility correction

The mounted PaymentVolumeChart creates `useRef<HTMLDivElement>(null)` and passes that object as ChartExportButton's chartRef. The button currently declares `React.RefObject<HTMLDivElement>`, which excludes null from its current value under the documented React 19 type contract.

This patch changes that prop to `React.RefObject<HTMLDivElement | null>`. It preserves HTMLDivElement as the element type and changes no runtime expression. The existing `if (!chartRef.current || isExporting) return;` guard remains intact. The entire exported component function—including the prior Escape handler and positional export arguments—is byte-identical.

## Pinned evidence

All donor inputs refer to Stellar-Analysis/frontend commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Evidence | Git blob | Bytes |
| --- | --- | ---: |
| src/components/charts/PaymentVolumeChart.tsx | 2a80a9912dc883b1e13a6f033de6536a06ecfac7 | 7020 |
| src/app/[locale]/network/page.tsx | cfcb9fba468523f2e5069002680a4f4c7c8e4802 | 12424 |
| tsconfig.json | 16eae33a28d532523720d66061cf9ac4b85c69a7 | 1000 |
| package.json | 2b1c6ac1f83096666c7fd6d5ba3fd22780e6b8eb | 3119 |
| pnpm-lock.yaml | 7ecba249d1b7cd41e629e2fff2782ed6805186f5 | 359885 |

The Network route dynamically imports and renders PaymentVolumeChart. Its nonloading, nonempty render supplies the nullable ref to ChartExportButton. This is the acquired source caller, not an inferred use of the separate exported chart hook.

The complete compiler configuration explicitly enables strict and strictNullChecks, includes TS/TSX source, and enables noEmit and skipLibCheck. The complete manifest selects React19.2.7, @types/react ^19 and TypeScript5.9.3; the retained pnpm lock resolves @types/react19.3.0. The installed package tarball was not inspected.

The configuration body had been unavailable in one seat's old custody. That seat acquired the exact immutable blob once for this new type-boundary assessment, then transferred all 1000 bytes, including the final LF. The returned native blob envelope carried content but no separate SHA field. Identity is therefore recorded as the requested immutable pin plus independent hash, not an invented returned native SHA. Root independently hashed the transferred complete text to the same blob; it made no duplicate provider read.

## Primary type contract

The [React 19 upgrade guide](https://react.dev/blog/2024/04/25/react-19-upgrade-guide#useref-requires-an-argument) defines RefObject's current value in terms of its generic parameter and documents the null-initializer overload as returning a nullable generic value. The [TypeScript strictNullChecks reference](https://www.typescriptlang.org/tsconfig/strictNullChecks.html) explains that null remains a distinct type when that option is enabled.

Combining these documented contracts with the acquired caller and explicit compiler settings identifies the prop mismatch: the supplied current value may be null, while the original prop excludes it. Adding null to the prop's existing element type fixes this specific mismatch. This is source and contract reasoning, not an observed compiler diagnostic or a claim that every installed declaration was read.

## Composition and exact patch

Apply this incremental patch after the existing `escape-dismissal.patch` from Commons31944 and `export-arguments.patch` from Commons31949. Those accepted patches are not recomputed or changed.

| Item | Git blob | Bytes |
| --- | --- | ---: |
| ChartExportButton.tsx after31949 | 94a4ffa0cda9b96a0e8dc35ec5c548c09647d54e | 3591 |
| ChartExportButton.tsx after this patch | aca513eb96065923ca8c7b5f0f92170ec37cbf9f | 3598 |
| nullable-chart-ref.patch | 7547dd3a4ea94e5e68833fb25f31c1a8f8da49fd | 444 |

The actual serialized one-hunk patch contains eight complete rows, adds one line and removes one line. Forward text application exactly produces the postimage; inverse application exactly recovers the preimage. Restoring the old type line reproduces every other source byte. The complete exported function body is identical.

No compiler, package install, codemod, browser, DOM, chart export, download, runtime, fixture or test was executed. This addresses the previously explicit nullable-prop boundary only. It does not establish a clean whole build, repair other component typings, or complete menu keyboard behavior.

Two new artifacts are added to the existing packet directory. The preceding guides and three unchanged upstream MIT notices remain preserved; original authorship and exact license identities are documented in README.md. This is an attributed Commons source proposal, not an upstream publication, deployment, acceptance or reward event.

Publication requires full immutable text/native/independent identities for both new artifacts and final PR/files/merge/main metadata. A named-main equality alias is allowed only when that observation equals the verified merge; otherwise both files are read once at the observed main pin. The release and completion index record the actual publication evidence.
