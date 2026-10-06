# PayD PR611 AnimatedModal: return focus during cleanup

The acquired AnimatedModal moves focus to its first selected control when opening. Its effect cleanup removes the Tab listener but does not restore the element focused before that move. This source patch captures that element immediately before the existing focus call and attempts to restore it during the same effect's cleanup, provided it is still a connected HTMLElement.

## Contributor carrier and exact source

Canonical contribution: https://github.com/Protocol-Guild/PayD/pull/611
Observed state: open, unmerged; author Levi-Ojukwu.
Donor repository: `Levi-Ojukwu/PayD`.
Donor branch: `feat/design-system-modal-animation-responsive`.
Pinned head: `35bc44885d37eb34b11f55fd2f37ac4fbd922d03`.
Changed source: `frontend/src/components/AnimatedModal.tsx`.

This packet preserves the original contributor's branch, authorship and broader design-system work. It does not claim ownership or upstream completion. Current canonical PR metadata reports eight changed paths, zero issue comments and zero review comments. The complete changed-path metadata and complete, untruncated 758-entry donor tree were acquired. This is bounded observed metadata, not a repository-wide absence claim.

The original module is `16bba4549d5275de5b7fdad68c68e9dc87789d2e`, 5,979 UTF-8 bytes. The prepared module is `9f487c996a3545280e14751781b56fe73c59fa3b`, 6,178 bytes. The patch adds seven lines and removes one in two hunks/twenty complete rows. No complete donor module is republished.

## Connected source chain

The actual donor branch's main entry renders App. Its `/admin` route renders AdminPanel. The panel's contracts tab renders ContractUpgradeTab. That component conditionally renders UpgradeConfirmModal when its existing selection/address condition is satisfied; its existing onClose clears the selection. UpgradeConfirmModal renders AnimatedModal with isOpen=true and passes its existing close/processing props.

This establishes a conditional source connection. It does not establish that any current account is authorized, that a real contract or selected row exists, or that the flow has been exercised. No business handler, admin-address condition, authorization, simulation, transaction, upgrade or account operation is changed or invoked. The separate current-main label and clipboard packets #31938 and #31942 remain separate from this contributor head.

| Complete input path | Git blob | UTF-8 bytes |
|---|---|---:|
| frontend/src/components/AnimatedModal.tsx | `16bba4549d5275de5b7fdad68c68e9dc87789d2e` | 5979 |
| frontend/src/components/UpgradeConfirmModal.tsx | `db30ed09c33e9e7888016b436d505085fd2bd85c` | 35097 |
| frontend/src/components/ContractUpgradeTab.tsx | `b9f89b99fc6915515f0a49c750afacc31679834c` | 14472 |
| frontend/src/pages/AdminPanel.tsx | `f006db147bc281b66ac6bc7993a6430830cd9220` | 45073 |
| frontend/src/App.tsx | `acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c` | 6460 |
| frontend/package.json | `33e58d67eca11b200b6988835b1f8450f179d2c2` | 2534 |
| frontend/src/main.tsx | `f84f187971ba135010c48e69fda10f0c0f71ebd9` | 1664 |
| LICENSE | `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64` | 11357 |

The six newly acquired full source/manifest strings matched their returned native identities, independently measured Git identities and exact donor-tree paths. The previously retained full main and Apache license texts independently match this donor tree; those transfers are not new content reads. The original immutable license response had no returned SHA field, so its prior identity is request-bound plus independently measured.

## Ordering and boundaries

The existing effect first rejects a closed modal, a missing content ref, or an empty selected-control list. These early returns remain unchanged. After selecting the same first and last controls, it captures document.activeElement, then runs the same first-control focus and installs the same Tab listener.

Cleanup removes that listener first. It then checks the captured element with instanceof HTMLElement and isConnected before calling focus. The dependency remains [isOpen]. React's documented effect lifecycle runs cleanup when dependencies change and on component removal; the development setup/cleanup cycle is not excluded by this change.

The prior active element is a captured reference, not an inferred selector or a new query at close time. It can differ from the visual invoking control, for example when pointer focus behavior or another focus operation selected a different element. Connected does not guarantee focusable, enabled, visible or successful focus. The code makes an attempt and does not report a successful keyboard interaction.

The zero-selected-control path still does no focus move or restoration. The existing selector, disabled/hidden control handling, static first/last snapshot, Escape/backdrop behavior, processing admission, close callbacks, animations, reduced-motion logic and rendered dialog remain unchanged.

## Primary contracts

- WAI-ARIA APG modal pattern: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- React effect lifecycle: https://react.dev/reference/react/useEffect

APG describes returning focus when a dialog closes, with exceptions for a removed invoker or a different logical next step. This patch provides only a connected-element restoration attempt and does not implement an alternate workflow target. React describes cleanup before a changed-dependency setup and after removal, plus an additional development setup/cleanup cycle. These primary contracts were acquired; neither is runtime evidence for this branch.

The donor package manifest declares React ^19.2.0 and framer-motion ^12.34.3. No installed dependency tree, lockfile resolution, types tarball, animation implementation or compiled output was inspected for this patch, and no version-specific compatibility or deployment acceptance is claimed.

## Verification and limits

Independent application of the actual serialized patch to the original full string reproduces the prepared full string. Reversing that serialized patch recovers the original. All unchanged ranges match exactly. This is source-string/patch validation, not a synthetic interaction test.

Cleanup is tied to the existing effect and isOpen/component removal, not animation completion. No focus stack, nested-modal arbitration, external-focus preservation policy, alternate return target, scroll suppression, first-paint guarantee or stale-event handling is added. Removing the original target simply skips this restoration attempt. Parent/child teardown order, delayed animation removal, a target that becomes disabled/hidden and custom focus methods remain unvalidated.

No claim is made that the existing dialog is fully accessible: focus-trap selector coverage, a dialog name, background inertness, dynamic control changes and other modal concerns remain outside this hunk. No DOM/browser/keyboard/assistive-technology execution, screenshot, compiler, test, fixture, account access, record read, network action, upgrade/simulation/transaction, upstream submission, sponsor contact or payment was performed.

## Artifacts and license

`restore-focus.patch` targets only AnimatedModal at the pinned contributor head. This guide records the change and its source limits. `LICENSE` is the full unchanged Apache-2.0 text from the donor tree. Retain the original contributor and repository notices. No unrelated donor module or business-handler source is republished.
