# Match notification Select All to visible ID membership

The mounted notification center keeps selected IDs while its search, read-status, type and priority filters change. Its row checkboxes use selected-ID membership, but its Select All checkbox and handler compare only the number of selected IDs with the number of filtered notifications. Equal counts do not establish that the visible IDs are selected.

This patch makes the checkbox and its handler use the same visible-ID membership condition. It is a two-line production correction, +2/-2, with no change to filter or batch-action policy.

## Exact original source

Repository: https://github.com/Stellar-Analysis/frontend

Donor: `482ee456369418ef82c4056718cb82d3468f762b`.

| Production source | Preimage | Postimage | UTF-8 bytes before / after |
| --- | --- | --- | ---: |
| `src/components/notifications/NotificationCenter/NotificationCenter.tsx` | `0cd01f490a82263a5961f4567d62931ae3ffd186` | `f9f8f1ccb1d7219d0de6f5141a81ad4355f5cf1a` | 8,984 / 8,990 |
| `src/components/notifications/NotificationCenter/NotificationsTab.tsx` | `56e2737f7b4cb1825f0e3f711c9e51ce1f28206b` | `53ed7b261d907d3f2e463cace2fdce5a22e98c37` | 14,479 / 14,485 |

Both complete modules were acquired once as new inputs to this task. Both source files keep mode 100644 and their exact original newline endings.

The actual mounted caller is the Navbar `1d519697311060e2d72c1a8fcaa59d1eb6148277`, through notification barrel `812d23234012d75770a798e7ad4f6c7be77b1e58` and NotificationBell `8e17fc08741d51bda9d0b3169a4b563fd528e89b`. The bell sets showHistory and renders NotificationCenter. Center passes its filtered list, selected Set and unchanged handlers to NotificationsTab. The tab's search and filter controls update the parent filter without resetting selection; each row already checks `selectedNotifications.has(notification.id)`.

Original Stellar-Analysis contributors retain credit and ownership. No new upstream issue, PR, assignment, approval or accepted feature is claimed. An exact bounded public search for NotificationCenter plus Select returned zero; the earlier bounded repository notification-title PR search was empty. Neither is a claim of global absence or maintainer selection.

## Correction and preserved policy

`select-all-membership.patch` changes only:

1. The handler's all-selected condition becomes `filteredNotifications.every(n => selectedNotifications.has(n.id))`.
2. The Select All checkbox uses that membership condition, retaining its existing nonempty-list guard.

When filtered results have equal count but different IDs, the header no longer reports a false complete selection or takes the clear branch solely because counts match. When all visible IDs are selected alongside other retained IDs, the header reflects that all visible rows are selected.

The existing branches remain exact: the all-selected branch clears the entire selected Set; the other branch replaces it with the current filtered IDs. This intentionally retains the existing whole-Set action policy rather than adding scoped deselection or merging hidden IDs. The empty-list checkbox stays unchecked. The handler still yields an empty Set for an empty filtered list, regardless of which original branch would have produced it.

Batch Mark as Read/Delete continue to operate on the selected Set as before. The selected-count banner, per-row handlers, filtering, search, export/download functions, provider data, notification ordering, timestamps and content are unchanged. This does not add indeterminate-state rendering, stale-ID pruning, hidden-selection warnings, duplicate-ID validation or concurrent-operation guarantees.

## Integration and source-only checks

Apply the exact patch to the donor pair, and inspect newer source before composing rather than overwriting later changes. Completed Auto Hide, Test Sound cleanup, preference switch semantics, shared audio hook and root export utilities are separate source paths. This patch does not modify NotificationCenter's own export/download handler.

Complete literal and serialized unified-patch forward/inverse reconstruction matches the stated full source identities. Those operations inspect retained strings only. No notification records were read from a live account or generated as fixtures; no selection, deletion, export, browser, runtime, test, compiler or device operation was executed. No whole-notification-center, accessibility, sponsor, bounty or payment completion is claimed.

The retained complete donor tree has no AGENTS.md or RULES.md. The observed `docs/CONTRIBUTING.md` (`f66db3b0eece27eb6fa888948c31ee8c7eabcfd2`) is EventSource-specific release guidance. Session no-execution/no-tests/no-upstream instructions control this source-only work.

Differently attributed MIT notices in donor documentation do not establish a repository-wide licence for these production modules. Only the focused patch and this original guide are distributed in Commons; original source contributor rights and external acceptance requirements are preserved.
