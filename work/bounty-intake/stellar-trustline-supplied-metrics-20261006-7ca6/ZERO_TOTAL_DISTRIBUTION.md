# Display a zero-total trustline distribution explicitly

The selected asset's distribution computes authorized and unauthorized bar widths by dividing each count by total_trustlines. Its caption examines only whether unauthorized_trustlines is positive. For an asset whose reported total is zero, those width expressions still divide by zero and the zero-unauthorized branch says all trustlines are fully authorized.

This patch gives exactly zero total its own display policy: both bars receive zero percent width, and the caption reads No trustlines reported for this asset. The raw count labels remain visible. Both original nonzero formulas and the original nonzero caption branches remain intact.

Apply after the existing #32126, #32131, #32135 and #32138 patches in this directory. Earlier artifacts and notices remain unchanged. This correction is separate from supplied-metric provenance, asset identity, row-click request ownership and initial-effect cleanup.

## Actual source evidence

Canonical donor: Stellar-Analysis/frontend at `482ee456369418ef82c4056718cb82d3468f762b`. The complete route, API helper and connected detail children were newly acquired for #32126 and remain retained. This continuation uses the exact composed #32138 source postimage, with no accepted-source reconstruction.

| Source | Preimage / UTF-8 bytes | Proposed postimage / UTF-8 bytes |
|---|---|---|
| src/app/[locale]/trustlines/page.tsx | `4400d3e9b2023acf6f865d14c82f4c8bc1363415` /15897 | `1ceba2ed046441f3e01dd5cddbba84bd072c0b5a` /16112 |

The unchanged src/lib/trustline-api.ts is Git blob `6ff2791be6f5997b5ab3c1b49f666d100e1be414`,3116 bytes. Its TrustlineStat shape declares total_trustlines, authorized_trustlines and unauthorized_trustlines as numbers. The actual route stores a supplied ranking record in selectedAsset and renders these fields directly in its distribution. The acquired helper has no runtime nonzero-total validator.

The selected-asset branch already displays the authorized and unauthorized raw counts. Immediately below, two style.width expressions compute each count divided by selectedAsset.total_trustlines, multiplied by100. The caption then uses unauthorized_trustlines>0 to choose between the pending/revoked wording and the fully-authorized wording. No total check currently protects either expression or caption.

The zero case is qualified from these acquired types and expressions, not from an observed live record. No network count, issuer, account or backend response was acquired for this correction.

## Exact policy

| Supplied total | Bar widths | Caption |
|---|---|---|
| Exactly numeric zero | Zero percent for both bars | No trustlines reported for this asset |
| Any nonzero value | Existing authorized/total and unauthorized/total formulas | Existing unauthorized-positive or fully-authorized branch |

Each width uses a conditional expression whose zero branch is the literal0 and whose other branch is the complete original arithmetic expression. The zero branch therefore avoids that division. The caption first checks exactly total_trustlines===0, then retains the original condition and both original strings for the other branch.

This is an explicit presentation choice. It does not infer that authorization succeeded, that a live network has no trustlines, or that the input counts are internally consistent. The term reported describes the supplied total, not independently verified network state.

## Source verification

show-zero-total-distribution.patch is1829 UTF-8 bytes, Git blob `1267dc6660c54014d91801af7f773a2ec9cefeb0`. It adds seven lines and removes five in one hunk containing28 complete serialized rows.

Full forward application of the actual serialized patch reproduces the expected postimage, and inverse application reproduces the preimage. Every hunk row is included without truncation. Reversing only the three authored replacement regions reconstructs every other byte exactly. The complete request/state block is separately equal, and the original arithmetic expressions are retained verbatim as the nonzero branches.

The raw count labels, distribution container and color classes, selected heading, charts, insights, number formatter, overview metrics, ranking controls, selected issuer comparison, request ownership and cleanup remain unchanged. No helper or child file is edited.

These are static source and full-text checks. No JavaScript width expression, component, formatter, API helper, data request, compiler, test, fixture or browser was executed. No rendered CSS or layout behavior was observed.

## Limits and publication

The policy handles exactly zero only. Negative, missing, nonnumeric, nonfinite or inconsistent fields are not validated or normalized. A record with zero total and nonzero component counts still displays those original raw count labels while the bars use zero width; this patch does not reconcile the contradiction. Existing nonzero arithmetic and caption behavior are deliberately preserved.

Existing helper fallback, error, empty-data and freshness policies remain. Prior request-lifetime changes do not certify a response's schema or truth. This patch adds no accessible progressbar semantics, announcement, localization layer or whole-accessibility guarantee.

A new dedicated Commons PR query for trustline, zero and distribution returned no entries. That is bounded search evidence, not a global absence proof, contributor reassignment or whole-feature completion finding. Original contributors retain credit, and the exact existing three notice files remain part of the directory.

Publication adds the patch and this guide only. Each complete immutable artifact is checked against its prepared string and native/independent Git identity; final PR, changed paths, tree and ordered parents are checked separately. A predeclared observed-main equality alias is used only if main equals the verified merge/readback ref. Otherwise both files receive complete reads at one observed immutable main without chasing later movement.

No API, account, wallet, trustline, payment, deposit, withdrawal, runtime, build, test, browser or upstream action was performed. Existing held routes, #32074 final changed-files UNKNOWN, earlier cache-loss qualifications and the unrelated unpublished parked source draft remain protected.
