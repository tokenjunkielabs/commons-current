# Chart export menu: Escape dismissal

## Result and scope

This source-only packet adds Escape dismissal to the existing chart export menu. When that menu is open and keyboard focus is on its trigger, PNG button, or SVG button, Escape closes it and returns focus to the Export trigger. The handler consumes that handled Escape event so it does not continue bubbling to an ancestor. When the menu is closed, and for every other key, the handler returns without changing state or consuming the event.

The patch adds 14 lines and removes none in `src/components/charts/ChartExportButton.tsx`. It preserves the export function, filename construction, format arguments, guard, loading flag, logger/error path and finally block exactly. Existing click handlers, button disabled state, visual classes, menu roles, labels and outside-click overlay are unchanged. The already imported `useRef` supplies one component-local trigger reference. Keyboard listeners are attached only to the three existing native buttons, not to the noninteractive wrapper.

This is one dismissal repair. It does not implement the rest of the menu keyboard pattern: opening focus, arrow navigation, Home/End, Tab exit, menu naming or post-action focus. It does not change the existing chart-reference prop type or claim that the whole component type-checks. No browser, DOM, keyboard, accessibility, chart capture, download, application runtime, test, fixture or upstream action was executed.

## Exact upstream source

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).

All source reads in this packet are fixed at commit `482ee456369418ef82c4056718cb82d3468f762b`, using complete UTF-8 content and comparing the native file SHA with an independently computed Git blob identity.

| Path | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/components/charts/ChartExportButton.tsx | 9e3cf18fd486344169da57ce11b76df517afbde9 | 3135 |
| src/components/charts/PaymentVolumeChart.tsx | 2a80a9912dc883b1e13a6f033de6536a06ecfac7 | 7020 |
| src/app/[locale]/network/page.tsx | cfcb9fba468523f2e5069002680a4f4c7c8e4802 | 12424 |

The network route dynamically imports PaymentVolumeChart and renders it with its payment-volume points and loading flag. PaymentVolumeChart directly imports ChartExportButton and renders it with its chart reference and the Payment Volume name when the loading and empty-data early returns do not apply. This is an actual source-connected route, not a claim that a live network request returned nonempty data or that a user encountered the defect.

The button currently exposes an expanded menu containing the two format buttons, but none of its controls handles Escape. Its menu can be closed by clicking its trigger, activating an export, or clicking the outside overlay. The new handler supplies the missing cancellation action while focus remains on these controls. It does not add a document-wide shortcut.

The separately read analytics route is not cited as a PaymentVolumeChart caller. A default-branch code search returned no ChartExportButton results; that result was not treated as evidence of absence. The exact source chain above was acquired from retained tree metadata and full pinned files.

## Source postimage and patch

| Item | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Upstream ChartExportButton.tsx | 9e3cf18fd486344169da57ce11b76df517afbde9 | 3135 |
| Patched ChartExportButton.tsx | dc91bd10b8d59ca5f39709b0995e286e4274e28c | 3595 |
| escape-dismissal.patch | 4ca7783982286e3c8669297f6cfe7363e5317c36 | 1660 |

The serialized unified patch has four hunks and 39 complete projected rows. Applying those actual serialized rows to the retained upstream text produces the postimage exactly; applying their inverse to the postimage reproduces the upstream text exactly. No application code is evaluated by those text checks. The complete export-handler block is byte-identical, and the complete JSX return block is identical after removing the four newly added ref/key-handler bindings.

An earlier unpublished local draft attached the handler to the wrapper. It was replaced before any publication with the native-button binding above, avoiding an unnecessary new interaction on a noninteractive element. Only the final patch described in this document is a deliverable.

To inspect or apply the source patch in a separately authorized upstream checkout at the pinned preimage:

```sh
git apply --check escape-dismissal.patch
git apply escape-dismissal.patch
```

These commands are instructions for a future authorized environment, not commands executed for this packet.

## Primary behavior reference

The [W3C APG Menu and Menubar pattern](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/) describes closing a focused menu with Escape and returning focus to the invoking control. The [Menu Button pattern](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/) separately describes opening and focus behavior. This patch addresses only the Escape dismissal boundary and leaves the remaining pattern work explicit. APG guidance does not establish browser or assistive-technology validation for these source bytes.

## Attribution and license

The latest path-specific upstream history entry is `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888, which relocates the frontend into the repository root. This is a history observation, not a claim that the relocating author wrote the entire component.

The three complete upstream MIT notices retained with the previous source acquisition are copied unchanged into this packet, including the original CRLF bytes in the McLaughlin notice. Their native and independent identities are:

- `upstream-licence-mclaughlin.md`: `57740b9d4d86aedf5d518f2f363d5cf192c54127`, 1104 bytes.
- `upstream-license-menke-laguna.md`: `af5411fa243cfcf2b61c79d081dbb6204e956041`, 1111 bytes.
- `upstream-license-de-wet.md`: `4a766e268772888af5df56c3f6c608f68558b789`, 1080 bytes.

Original project authorship and license rights remain with their respective holders. This Commons packet is an attributed downstream source proposal, not an upstream contribution claim, deployed repair, accepted bounty or payment event.

## Coordination and publication evidence

Before freezing the patch, a bounded Commons PR query for ChartExportButton and Escape returned no matching entries, and an exact public Slack query with those terms returned zero rendered results with native pagination end. These are bounded observations, not proof of exclusive ownership or universal history coverage.

The publication plan is to add this patch, this guide and the three unchanged notices under the unique packet directory, verify each complete immutable artifact and its native/independent identity, then read the final PR/files/merge/main metadata. A named-main equality alias may reuse a verified immutable read only if the observed main commit equals the verified merge; otherwise the plan calls for one full read of every packet file at that observed main pin. The final merge, release and index receipts carry the actual publication observations. No re-execution of an accepted source task or old calculation is part of that process.
