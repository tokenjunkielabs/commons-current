# Expose the current Trustlines asset

The Top Assets list already highlights the asset whose exact code and issuer match selectedAsset. Its native command buttons do not expose that current-item state. This incremental patch adds aria-current={isSelected ? "true" : undefined} to the existing button, using the same predicate as the visual highlight.

Activating a button still selects and reloads that asset. Activating the current asset still reloads it. This change adds no toggle, tab, radio, listbox, keyboard-navigation or deselection behavior.

## Source and composition

Canonical donor: Stellar-Analysis/frontend at `482ee456369418ef82c4056718cb82d3468f762b`. Complete route and API source were acquired for #32126 and remain retained. The route's subsequent accepted compositions are #32131, #32135, #32138, #32141 and #32144. This patch applies to that exact retained route postimage, without reacquiring or reconstructing accepted source.

| Production source | Preimage / UTF-8 bytes | Proposed postimage / UTF-8 bytes |
|---|---|---|
| src/app/[locale]/trustlines/page.tsx | `5739dace8e22e0671039c8b6e88d017cb91dcb95` / 16370 | `47f44d7d322abc336ea8037ac37d4a0d7c600010` / 16435 |

The actual mounted route maps rankings to native buttons keyed by asset_code and asset_issuer. isSelected compares both fields against selectedAsset, as established by #32131. The same boolean controls the row highlight and chevron color. The new attribute is true on that existing current-item branch and omitted otherwise.

handleSelectAsset creates the current request token, writes selectedAsset synchronously, clears the old detail data and starts the existing history/insights requests. Its success, error and finally guards from #32135 remain exact. The initial-load lifetime checks from #32138, zero-total presentation from #32141 and overview availability metadata/display from #32144 are unchanged. The independent #32146 chart baseline correction is unaffected.

The marker describes the route's current asset selection, including while its details are pending or fail. It does not assert that the history or insights request succeeded, or that a returned placeholder is fresh data.

## Primary semantics and narrow choice

The successfully acquired [WAI-ARIA 1.2 Recommendation, aria-current](https://www.w3.org/TR/wai-aria/#aria-current) defines this state for the current item in a related set, including a visually indicated current item. It supports base markup and has a generic true value. An absent or undefined value has no exposed current state. The Recommendation advises one current item per set.

The same Recommendation's aria-pressed section describes a toggle whose next activation changes it back to false. The [APG button pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/) likewise distinguishes toggle buttons from command buttons. The current handler does not implement that deselection contract, so this patch uses current-item semantics while preserving the native command button. This is an application of the acquired primary contract to the retained source, not an observed assistive-technology result.

The page retains its existing data assumptions. Duplicate returned rows with the same exact code and issuer can produce multiple matching buttons, just as they already produce duplicate keys and visual highlights. A selected asset absent from the current rankings can leave no row marked current. This patch does not normalize those responses or change asset identity policy.

## Exact verification

expose-current-asset.patch is 616 UTF-8 bytes, Git blob `4d5de1f88e81cc1c902b1f6ca74666868e50bb9d`. It adds one line and removes none, in one hunk with seven complete serialized rows.

Forward application of the actual serialized patch reproduced the complete expected postimage. Inverse application reproduced the exact preimage. Removing the one authored attribute reconstructed every other source byte. The existing identity predicate, native button, key, callback, complete handler, effect state, visible content, class names and all other source bytes remain unchanged.

CI supplied a nongating retained-description check of this contract: the current-item attribute fits the unchanged command behavior and stays aligned with the visual predicate. This was not a source, provider or runtime review and was not an approval gate.

No component, click, request, Date, formatter, chart, account, credential, wallet, trustline or other application operation was executed. No compiler, build, test, fixture, browser, keyboard or assistive-technology observation is claimed. The attribute is not a full accessibility, unique-row, data-quality or successful-detail guarantee.

## Qualification, attribution and publication

A genuinely new dedicated Commons PR query for Trustlines selection state returned an empty bounded result. This is not a global absence, acceptance or ownership claim. The previously accepted Trustlines corrections remain protected.

This packet adds only the new patch and this guide inside the existing attributed Trustlines directory. Its original guide, patches and exact upstream notices are unchanged. Original contributor ownership is preserved; no upstream repository is modified.

The newly authored complete publication spec and proposed full postimage are checkpointed before branch publication. Complete immutable artifact text and native/independent Git identities are checked against the prepared files. Separate final metadata reads verify the PR, exact changed paths, merge tree and ordered parents. A predeclared equality alias can apply only if observed main equals the verified merge/readback ref; otherwise both files receive one complete read at the observed immutable main, without chasing later commits.

Earlier whole-body/provider holds, #32074's unavailable final changed-files check, #32122/#32123 custody-loss qualifications and the unrelated unpublished EmployeeList draft remain unchanged. This is a source-only proposed correction, not upstream acceptance, deployment or bounty completion.
