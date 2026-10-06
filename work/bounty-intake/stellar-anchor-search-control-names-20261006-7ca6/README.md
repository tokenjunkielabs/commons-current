# Explicit names for the mounted Anchors search controls

The actual Anchors page renders `SearchAndControls`. Its search input has a placeholder and search icon, its sort-field select presents the available criteria, and its direction button displays only a trend icon. None has an explicit label or ARIA name in the acquired source.

This patch adds a programmatic name to each of those three existing controls. It does not change their appearance, state, values or behavior.

| Control | Explicit aria-label |
| --- | --- |
| Search input | Search anchors by name or account |
| Sort criterion select | Sort anchors by |
| Direction button while current order is desc | Sort anchors ascending |
| Direction button while current order is asc | Sort anchors descending |

The direction name describes the **next action**, matching the existing handler's transition. It is not an aria-pressed state or a change to the sorting algorithm. The search name preserves the wording of the existing placeholder without its trailing ellipsis. The Export button already contains visible text and is untouched.

## Actual source and mounting

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete retained input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/anchors/page.tsx` | `80899e99b202a254f6688173404b8131e475f752` | 1,339 |
| `src/app/[locale]/anchors/components/AnchorsPageContent.tsx` | `5ba7f36fa3f2cca6f91e2caaad16b2d88a564625` | 8,115 |
| `src/app/[locale]/anchors/components/helpers.tsx` | `ec1f18bb63d62f4a6a99203bb1baf45cfb93fb16` | 5,665 |
| `src/app/[locale]/anchors/components/useAnchorPage.ts` | `07daa182ff8167ac3d9740ff26ab2e893bc2bf4f` | 3,067 |

The App Router page renders `AnchorsPageContent`, which directly imports and renders this helper component, passing its current searchTerm/sortBy/sortOrder and setters. The complete loader initializes sortOrder to desc and provides the existing search/filter/sort behavior. This is an actual connected consumer, not an inference from an unused exported helper.

## Patch and evidence

`name-search-controls.patch` applies to `src/app/[locale]/anchors/components/helpers.tsx` at the pinned donor. Source identity is `ec1f18bb63d62f4a6a99203bb1baf45cfb93fb16` (5665 B) → `feaa2136e246b12dac0893553d82ff4686dc2327` (5860 B), **+3/-0 in three hunks**. It preserves the final newline.

All callbacks, state inputs, native control types, options, placeholder, SVGs, classes, sorting and Export behavior remain exact. All other functions in the helper module, including the generated-history producer, also remain exact. There are no component/hooks/import/ID additions.

The serialized patch and its inverse reconstruct the complete source postimage/preimage exactly. Retained complete source strings are used as inputs to this new correction; previously completed view fixes and pagination behavior were not replayed or changed. The separate [Anchors view packet](https://github.com/woahwhattheheck/commons/pull/32011) remains protected and composes with this helper-only change.

The [W3C WAI labeling guidance](https://www.w3.org/WAI/tutorials/forms/labels/#using-aria-label) supports aria-label for controls whose visual context already communicates their purpose, while noting it does not provide a visible label. Here that context is the search placeholder/icon, criterion options and direction icon. This is an explicit-name correction only, not a claim that the prior placeholder had no browser-specific accessible-name fallback or that every visual user can understand the icons.

## Attribution and limits

Original implementation credit and contributor rights remain upstream. Bounded current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`; it is not treated as proof of sole original authorship or this patch's runtime validation. The source-specific Commons SearchAndControls/label PR query and public Slack query both returned zero, with no global uniqueness claim.

The retained complete donor tree has no root AGENTS/RULES path. Acquired docs/CONTRIBUTING.md is EventSource-specific; the session's explicit no-tests/no-runtime/no-upstream-publication scope remains controlling. Differently attributed MIT documentation notices do not establish a repo-wide code licence here. This Commons contribution includes only the minimal patch and this original guide, with the exact source identities and preserved attribution.

No visible-label redesign, copy translation, live-region announcement, focus change, aria-sort state, responsive-layout acceptance, assistive-technology behavior or full-page accessibility conformance is asserted. No browser, input, sorting, application, test, fixture, backend/API/user data or upstream operation was run. No author assignment, sponsor acceptance, bounty award or payment is claimed.
