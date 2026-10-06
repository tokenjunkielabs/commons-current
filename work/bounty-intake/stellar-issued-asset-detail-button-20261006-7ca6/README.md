# Add a native details button to issued asset rows

The mounted IssuedAssetsTable opens asset details through a table-row click handler. The asset code itself is a span, and the row has no keyboard activation behavior. The actual portfolio supplies that handler to select the asset shown by its existing details modal.

This patch renders a native button in the asset-name cell when the optional selection callback exists. Its click handler stops propagation before calling that callback, preserving one selection call per activation instead of also triggering the existing row handler. Without a callback, the exact original span remains.

## Actual source and caller chain

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), immutable commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/components/anchors/IssuedAssetsTable.tsx` | `1c650ade062e90d3a0e2dda834f5a396659fe5db` | 4,885 |
| `src/components/anchors/AssetPortfolio.tsx` | `1801c67028bb96c8b69c8c6d23f47ba45ad0a920` | 6,015 |
| `src/components/anchors/AssetDetailModal.tsx` | `dcab1bf692c77dbf8eec93682612d8e364ceb9a4` | 9,160 |
| `src/app/[locale]/anchors/[address]/page.tsx` | `71fea1bb40c29bcbba0657ba1cb10a65d35fab23` | 7,297 |

The App Router detail page renders AssetPortfolio with `data.issued_assets`. The portfolio renders IssuedAssetsTable with its filtered/sorted assets and `onAssetClick={setSelectedAsset}`; it also renders AssetDetailModal with that selection. No navigation or transaction operation occurs in this action.

The modal already moves focus to its first control when opened and supplies its own Escape/Tab handlers. Those complete source bytes are retained as caller context, not changed or revalidated here. The prior #32032 diagnostics, #32039 export-anchor and #32042 overflow patches preserve this chain.

## Minimal source correction

`open-asset-details-button.patch` changes only the asset-name span region: **+15/-1 in one hunk**.

Source identity:
`1c650ade062e90d3a0e2dda834f5a396659fe5db` (4,885 B)
→ `821eca456b8cc09ca9f96963cd100bf9be519be1` (5,498 B).

When onAssetClick is present, the native type=button displays the same asset code and has an explicit View-code-details accessible name. A small class list retains left alignment and provides underline cues on hover/focus. The original table row and its pointer callback remain intact, so clicks elsewhere in the row retain their existing behavior. The button stops its own bubbling click before invoking the same callback with the same row object. It does not prevent default keyboard activation or introduce synthetic key handlers.

Without onAssetClick, the original span is used and no inert action control is added. Table headers, row keys, icons, numeric formatting, pagination calls, slicing, sorting/filtering in the parent and every other table source byte remain exact. No role is changed on the table row.

The [W3C APG button pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/) identifies dialog opening as an action and describes Enter/Space activation for focused buttons. [React's event reference](https://react.dev/reference/react-dom/components/common#react-event-object) documents stopPropagation as stopping propagation through the React tree. These primary contracts support the native action and prevent the retained ancestor row from receiving the same click.

## Source-only validation and limits

The complete serialized patch reconstructs the full postimage, and its inverse reconstructs the full preimage with exact independently computed Git blob identities. No synthetic event, React render, browser, keyboard, device, application, fixture or test was executed.

This adds a keyboard-reachable activation control under native browser semantics; it is not a whole-dialog or whole-table accessibility verdict. Existing modal focus return, stacked-modal behavior, fixed IDs and rate badges remain separate. Browser/global button styles may affect geometry; no pixel identity or device rendering result is claimed. The supplied action callback remains responsible for its original state behavior and any failures.

Bounded current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`; original authorship rights are retained, with no sole-author inference. Scoped Commons/public Slack queries for IssuedAssetsTable and keyboard returned zero; this is bounded overlap evidence.

The complete donor tree had no root AGENTS/RULES path. EventSource-specific CONTRIBUTING instructions do not override the explicit no-tests/no-runtime/no-upstream scope. Differently attributed documentation MIT notices do not establish repository-wide code licensing. Only this minimal patch and original attributed guide are published.

No actual asset/account data, live API call, upstream branch/PR/comment, assignment, sponsor acceptance, bounty/payment or full issue completion is performed or claimed.
