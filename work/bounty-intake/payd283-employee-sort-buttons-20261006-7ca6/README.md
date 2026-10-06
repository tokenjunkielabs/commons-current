# Employee table sort buttons

The mounted EmployeeList desktop table currently attaches its five sort actions directly to table-header cells. Those cells contain visible labels and directional glyphs but no native interactive control. This patch places each existing action and its existing label/glyph inside a native button, while retaining the surrounding th as a table header. It makes the current sorting action available through the button's native interaction contract.

This is a narrow source continuation prompted by the warm [PayD issue 283 accessibility row](https://github.com/Protocol-Guild/PayD/issues/283). Its body is generic UI language; this packet does not claim an accessibility audit, full issue completion, or implementation of an unobserved acceptance checklist.

## Exact source and patch

Donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`.

| Source | Before blob | Before UTF-8 bytes | After blob | After UTF-8 bytes |
|---|---|---:|---|---:|
| frontend/src/components/EmployeeList.tsx | `277684e5f87cabd72ff5aadd04299a5360fdf3e0` | 20441 | `29fee53b3a74b52032d07700f91e6afc2b891f21` | 21006 |

Mode 100644. The minimal serialized patch changes the five adjacent headers in one hunk, 75 complete rows, +40/-25 lines. Forward application reproduces the entire prepared postimage and reverse application reproduces the entire acquired source. All source outside that hunk is preserved exactly. No component, comparator or user event was executed for this verification.

The five existing callbacks remain exactly onClick={() => handleSort(key)}, with one callback for each original key and no duplicate handler retained on the parent. The visible label and arrow expression are preserved.

| Visible heading | Existing sort key |
|---|---|
| Name | name |
| Role | position |
| Wallet | wallet |
| Salary | salary |
| Status | status |

Each button explicitly has type="button". The cursor affordance moves from th to the button, and text-left is explicit. Header text-size, weight, uppercase, tracking, color and padding classes remain on the original th. The existing handleSort function, sortKey/sortAsc state, comparator, sortedEmployees array, row rendering and mobile cards are unchanged.

## Connected source evidence

The complete retained App module routes /employee to EmployeeEntry. Its existing loading branch eventually renders EmployeeList. EmployeeList renders these headers in its existing hidden md:block desktop table. The table already consumes the sortedEmployees array, so this is an action entry point for an existing connected sorter, not an invented page or a new data operation.

| Unchanged retained module | Git blob | UTF-8 bytes |
|---|---|---:|
| frontend/src/main.tsx | `f84f187971ba135010c48e69fda10f0c0f71ebd9` | 1664 |
| frontend/src/App.tsx | `acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c` | 6460 |
| frontend/src/pages/EmployeeEntry.tsx | `b89a5c832191a19a52c4f7b99201da5ece9acef8` | 11774 |
| frontend/src/index.css | `91a759763e2d95a56274460685978f2a024c3b53` | 8054 |

EmployeeList and EmployeeEntry were acquired completely at the pinned donor while qualifying the separate #32009 CSV-zone patch. They are reused here without a provider reread. Main, App and stylesheet are also reused from full retained custody; their canonical tree identities match. Reuse does not make them fresh acquisitions. The CSVUploader source change in #32009 is a different file and remains untouched.

The parent supplies callbacks that log for some employee interactions. No persisted operation, employee data, payroll information or account action is needed or performed here. Sort state is still local display state; the patch neither adds nor invokes submission, editing or deletion handlers.

## Native control contract and limits

The primary [MDN button element documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button), acquired 2026-10-06, identifies button as an interactive element with native keyboard activation and explains that type="button" avoids the default submit role. This supports the choice of control. It is not a browser or assistive-technology test.

Keeping the th preserves the table-header element. The moved callback is attached only once, to its child button, so this patch does not deliberately add a parent/child double action. No custom keydown emulation, positive tabindex or role override is introduced. The five existing visible headings provide button content; their existing arrow glyphs remain present. aria-sort and broader announcement of sorting state are outside this change.

Clicking header padding outside the button no longer invokes sorting. This is an explicit change to the clickable area. The complete retained stylesheet applies a 44px minimum width and height to buttons, and native button styling also participates. These rules can change header geometry. No identical-pixel layout, unchanged hit area, computed-style, focus-visibility or universal accessibility claim is made. The surrounding responsive table/mobile split is preserved.

## Current carrier and attribution

The bounded all-state PR query for issue 283, top 20, returned no entries. The observed issue is open, unassigned and has one comment. Its complete comment is ranjeet150's assignment request, not a maintainer grant, acceptance or established implementation. This is a bounded observation, not a global ownership clearance.

A separate bounded EmployeeList PR query returned test-titled PRs 588/589 and the mobile-layout PR581. No test body, fixture or test source was expanded or run. PR581's current metadata is OPEN/unmerged, author waterWang, head `82ce1281b0a8f7a014d8835df237f7ccd34d00e1` in waterWang/PayD. Its complete eight-path metadata includes EmployeeEntry but not EmployeeList. Its branch, pages and handlers remain untouched; metadata is not a review of its full source or readiness. No claim of a complete contributor census follows.

Protocol-Guild/PayD contributors retain source credit. This packet makes no original-authorship assertion. The included LICENSE is the retained complete donor Apache-2.0 text, blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`, 11,357 UTF-8 bytes. The packet republishes a minimal patch, this guide and that notice, not all acquired caller modules.

## Verification scope

Validation is complete source/text custody: pinned before/after identities, exact serialized forward/reverse application, preserved callbacks and unchanged source outside the header hunk. Publication verification is recorded separately with full immutable artifacts, native and independent Git blob identities, PR/path/tree/parent metadata, and a preselected main-equality alias only if a fresh same-repository observation actually matches; otherwise full artifacts are read at one observed immutable main.

No browser, keyboard, screen reader, DOM, styling engine, comparator, employee record, account, build, compiler, runtime, synthetic fixture, test or upstream action was executed. This is not a whole-table accessibility result, mobile sorting addition, aria-sort enhancement, global keyboard-shortcut guarantee, issue acceptance or payment claim.
