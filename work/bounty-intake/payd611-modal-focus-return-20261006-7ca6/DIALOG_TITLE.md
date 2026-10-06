# PR611 dialog name from its visible heading

The acquired contributor branch renders AnimatedModal with role="dialog" and aria-modal="true", but without an aria-label or aria-labelledby. Its mounted UpgradeConfirmModal already renders a persistent visible "Upgrade Contract" h2. This follow-through connects that heading to the dialog through a per-instance ID.

## Carrier, application order and attribution

Existing canonical contribution: https://github.com/Protocol-Guild/PayD/pull/611.
Donor: `Levi-Ojukwu/PayD@35bc44885d37eb34b11f55fd2f37ac4fbd922d03`, branch `feat/design-system-modal-animation-responsive`, original author Levi-Ojukwu. The canonical PR was observed open/unmerged with zero issue/review comments. This source-only follow-through leaves the contributor branch and its ownership unchanged.

Apply the earlier `restore-focus.patch` from Commons #31974 first, then `dialog-title.patch`. The generic-wrapper preimage is exactly that prepared focus-return result. UpgradeConfirmModal's preimage is still the original complete PR611 source. The prior focus patch, README and unchanged Apache LICENSE remain in this directory; this addition neither replaces nor republishes those artifacts.

| Source | Before Git blob | Before bytes | After Git blob | After bytes |
|---|---|---:|---|---:|
| frontend/src/components/AnimatedModal.tsx, after31974 | `9f487c996a3545280e14751781b56fe73c59fa3b` | 6178 | `094204ecb3d031e514b478bbd8c8da7675bf00e2` | 6307 |
| frontend/src/components/UpgradeConfirmModal.tsx | `db30ed09c33e9e7888016b436d505085fd2bd85c` | 35097 | `33ddcc3390492242d38cc68ebc558c41a1192a0d` | 35175 |

The complete donor strings and branch-specific input map remain retained from the immediately preceding new source qualification. The original wrapper at that head was `16bba4549d5275de5b7fdad68c68e9dc87789d2e` (5979 bytes). No new provider read of accepted source or replay of earlier source checks was needed to prepare this distinct hunk.

## Actual connected caller

The acquired donor main entry renders App, whose /admin route renders AdminPanel. Its contracts tab renders ContractUpgradeTab; that component conditionally mounts UpgradeConfirmModal under its existing selected-contract/address condition. UpgradeConfirmModal renders AnimatedModal with isOpen=true. Its visible h2 is outside the conditional step bodies, so the named heading is supplied across those existing rendered steps.

This is conditional source wiring, not a claim about any actual account, permission, selected record or executed flow. Current-main Commons #31938 labels and #31942 clipboard rejection concern a different source head and are not silently substituted or reapplied here. The original contributor and repository attribution remain.

## Small additive interface

AnimatedModal gains one optional string prop, ariaLabelledBy, and forwards it to aria-labelledby on the existing motion.div dialog element. Callers that omit it retain their prior behavior; no label is invented for them.

UpgradeConfirmModal imports useId and calls it unconditionally at the start of the component. The resulting titleId is passed to the wrapper and assigned to the existing h2. The heading's text and class remain exactly the same. The ID is an accessibility relationship, not a data key or a list key.

The prior focus-return change remains intact. No effect, selection state, notification, close callback, processing admission, input, simulation, upgrade, authorization, polling, transaction, storage or account handler changes. The source patch adds eight lines and removes two across seven hunks/fifty-two complete rows.

## Primary contracts and validation

- WAI-ARIA APG modal-dialog naming: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- React useId: https://react.dev/reference/react/useId

APG specifies a name for a dialog through a visible-title reference or a label. React documents a top-level useId call for per-instance accessibility IDs. The corresponding docs were acquired, while the APG source already read for #31974 was reused. These are source-design contracts; they are not observations of this application's rendered accessibility tree.

The actual serialized two-file patch was independently parsed and applied to each complete preimage. The exact prepared postimages resulted; reversing it recovered both preimages. Complete unchanged ranges are identical. This validation uses source strings and patch structure, without a browser, compiler or synthetic interaction.

The donor manifest declares React ^19.2.0 and framer-motion ^12.34.3. Installed resolution, dependency internals, built output and actual motion/DOM attribute forwarding were not executed or inspected. No version-pinned runtime, server/client tree equality, multiple-root configuration or installed-types claim follows.

## Limits and license

This supplies one source-level dialog-name relationship for the connected UpgradeConfirmModal caller. Other AnimatedModal users may still omit a name. It does not supply descriptions, change focus handling, fix the existing trap selector, guarantee contrast, introduce inertness, rename controls, or establish full modal accessibility. It does not claim screen-reader output, key-event behavior, first-paint behavior, animation timing or whole-build acceptance.

No user/contract record, account, image, browser/DOM, assistive technology, runtime, compiler, test, fixture, API call, upgrade/simulation/transaction, upstream PR, sponsor contact or payment action was performed.

The existing `LICENSE` is the unchanged Apache-2.0 text with Git blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`, 11357 bytes, from the exact donor tree. Keep it and the contributor/repository notices with both patches. This guide records the additional modification. Only the focused patch and this guide are new artifacts; complete donor modules are not republished.
