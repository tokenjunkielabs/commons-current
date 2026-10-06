# Associate custom dates and expose the selected time preset

The analytics export route mounts DateRangeSelector, which forwards its props to TimeRangeSelector. That component renders custom Start Date and End Date labels beside their inputs without an explicit association. Its four native preset buttons communicate the selected preset through CSS alone.

This source-only continuation associates both custom date labels with their controls and exposes the existing selected preset through aria-pressed. Date calculations, effect inference, controlled values and callbacks remain unchanged.

## Source and actual mounting

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).
Immutable donor: `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete retained source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/components/ui/TimeRangeSelector.tsx` | `2fba3d99670a0ae35cdb80cc97478a903352ca13` | 3,863 |
| `src/app/[locale]/analytics/export/components/DateRangeSelector.tsx` | `ebcf27a8797f46be0005155bcaec6d21c7dd0eb5` | 474 |
| `src/app/[locale]/analytics/export/page.tsx` | `e60172711db5a9f5cc5cf71ae924ab24da15c989` | 7,849 |

The acquired page renders DateRangeSelector with its startDate, endDate and state-setting onChange. The adapter forwards exactly those three props to TimeRangeSelector. This establishes a concrete mounted consumer, not an inferred unused utility. The page's completed [#32115 demo/email presentation](https://github.com/woahwhattheheck/commons/pull/32115) and its separate [#32118 metric focus/preview count](https://github.com/woahwhattheheck/commons/pull/32118) packet remain unchanged. No source verification of those completed packets was repeated.

Current native path history returned christabel888's relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`; that is observed history rather than a claim about original authorship of all code. A dedicated upstream TimeRangeSelector PR query, a dedicated Commons TimeRangeSelector plus label PR query, and a public Slack TimeRangeSelector query returned zero. These bounded checks do not prove global absence. No external issue assignment, maintainer approval, reward eligibility or upstream acceptance is asserted.

## Exact source contract

Preset is the existing union of 24h, 7d, 30d and custom. The component initializes preset to 30d. Its existing effect re-infers a preset from incoming dates; applyPreset computes or preserves dates, sets preset, then calls onChange. Each button already uses preset === p for its selected styling and keeps its visible label unchanged.

The new aria-pressed expression uses that same comparison. It describes this existing local selection state, including its current effect timing and inference behavior. It is not an assertion that the selected label exactly validates both date endpoints, and it does not change clicking the already-selected preset, which can recompute relative dates. No radio-group role, roving focus or new keyboard model is introduced.

Custom Start Date and End Date inputs are rendered only when preset is custom. Two unconditional top-level useId calls precede the existing state hook. Each generated ID is shared between the corresponding label's htmlFor and input's id. No IDs are derived from user values or used as list keys.

## Patch and primary contract

`associate-time-range-controls.patch` is **+8/-3 across five hunks in one production file**.

| Source identity | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Before | `2fba3d99670a0ae35cdb80cc97478a903352ca13` | 3,863 |
| After | `7e627c586a3a47dcef1b2c6e76765ec29ced4054` | 4,072 |

The patch imports useId, declares two IDs, adds two htmlFor/id pairs and adds aria-pressed to the existing preset button mapping. All dates, labels, classes, handlers, ordering, controlled values and conditional rendering remain exact.

The successfully read primary [React useId documentation](https://react.dev/reference/react/useId) documents top-level calls for accessibility associations and includes matching htmlFor/id examples. The successfully read primary [W3C APG button pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/) describes aria-pressed for button state and retaining a stable label. These support the selected source associations/state attributes, not a complete interactive-widget certification.

Retained root dependency facts identify canonical package `2b1c6ac1f83096666c7fd6d5ba3fd22780e6b8eb` / 3,119 bytes and lock `7ecba249d1b7cd41e629e2fff2782ed6805186f5` / 359,885 bytes: React 19.2.7, @types/react locked 19.3.0, Next 16.2.10 and TypeScript 5.9.3. These are declared/locked facts, not installed packages or a successful build.

## Validation and limits

The full acquired preimage independently matched its immutable Git blob and byte count. The serialized patch reconstructs the complete postimage, and its inverse reconstructs the complete preimage. A pure source comparison preserves the entire original preset state/effect/applyPreset block. Both date input onChange bodies, value expressions and the preset onClick remain byte-for-byte exact.

No application, date conversion, browser, assistive technology, export, API, account, storage, fixture, test or build was run. This is a source association/state-semantics correction, not measured speech output, contrast, whole-page accessibility, hydration or date correctness. Existing range validation, UTC/local date parsing, DST behavior, preset inference, the general Time Range label and other consumers' layouts remain outside the claim.

The retained complete donor tree has no AGENTS/RULES paths. Its known contribution guidance concerns EventSource tests/npm releases; the authorized source-only scope does not execute that workflow. Three differently attributed documentation MIT notices do not establish whole-repository licensing. This Commons packet publishes only the minimal attributed patch and this original guide, preserving all completed work, ownership and exact failed-route holds. No upstream submission occurs.
