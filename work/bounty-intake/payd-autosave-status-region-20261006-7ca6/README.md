# Autosave status semantics

The current AutosaveIndicator renders translated saving, saved-time and never-saved feedback as ordinary div content. Its existing form callers pass the autosave hook's saving and lastSaved values. This patch adds role="status" to the existing outer div in each of the three branches, giving that feedback status-region semantics without changing the form, hook or persistence behavior.

## Exact source and attribution

Repository: https://github.com/Protocol-Guild/PayD
Immutable donor: `171c74b454daba241bfb75f36d10a0a3a77a68e5`.
Production path: `frontend/src/components/AutosaveIndicator.tsx`, mode 100644.

| Identity | Git blob | UTF-8 bytes |
|---|---|---:|
| Complete donor preimage | af97c737484c46015b852664a227f53a652af425 | 1826 |
| Prepared postimage | 350306db9bce5acedb272284843aa75d84830543 | 1868 |

The complete retained donor tree has 753 entries and reports no truncation. It binds the source path, callers, entrypoint and license. The complete source text matches its returned provider blob and an independent Git blob calculation. A fresh named-main guard still returned the donor commit before publication.

This is an attributed follow-through on current repository source, not an external contributor branch mutation or a claim that an entire issue is complete. The bounded path history, limited to one commit at the exact donor, returned `4f5dd01b31a0b7445e50408398b6fbe9b52d8f48`, dated 2026-09-27, with author name “Mainnet-ops” and subject “feat(ui): adopt workpay-inspired design language”. That is the observed latest path-touch attribution, not an original-authorship census. Preserve the repository contributors and existing notices. No absence of another owner or carrier is asserted.

## Actual connected source

The acquired App source imports and renders EmployeeEntry at /employee and PayrollScheduler at /payroll under its existing route wrappers. Both complete page sources import AutosaveIndicator, destructure saving and lastSaved from useAutosave, and render the component with those two props.

| Retained source | Git blob | UTF-8 bytes |
|---|---|---:|
| frontend/src/pages/EmployeeEntry.tsx | b89a5c832191a19a52c4f7b99201da5ece9acef8 | 11774 |
| frontend/src/pages/PayrollScheduler.tsx | e394d547dafe88da7d3ce9683666fd47e8a63bce | 28934 |
| frontend/src/App.tsx | acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c | 6460 |
| frontend/src/main.tsx | f84f187971ba135010c48e69fda10f0c0f71ebd9 | 1664 |

The main.tsx full text had already been acquired from a separate immutable donor; its independently calculated blob is exactly the same blob bound to this canonical donor tree. Its render of App is therefore reused by byte identity, without inventing a new source read. The page and App sources were acquired directly at the canonical donor. This establishes source wiring only, not an actual signed-in form session or observed employee, payroll or storage record.

An earlier independent observation about useAutosave.clearSavedData remains NO PATCH: neither of these acquired frontend callers destructures or invokes that clear method. This status change does not resume that unconnected candidate or alter the hook.

## Focused modification

Each existing outer div receives the same role. All three branches retain their original div element, class names, children and return conditions. The translated saving/saved/neverSaved keys, localized time formatting, spinner and decorative dots are unchanged. No prop, import, hook order, state, callback, debounce, storage, form submission, financial policy or route changes.

The three replacements total +3/-3 across three hunks and 24 complete diff rows. The patch is against the complete original current-main component and needs no earlier delivery patch applied to this file.

## Primary semantics and validation

Primary documents acquired for this change:

- MDN status role: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/status_role
- W3C status messages explanation: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html

The status role supplies advisory live-region semantics with implicit polite announcements and atomic content. Its use does not require moving focus. This supports the source-level role choice; it is not an observation of assistive-technology output in this application. The W3C guidance explains the need for status changes to be programmatically identified without taking focus, but this patch is not a WCAG audit or a conformity claim.

The actual serialized unified patch was independently parsed and applied to the full preimage. The result exactly matches the prepared postimage; reverse application exactly restores the preimage. Hunk counts, full row coverage and all unchanged source ranges were checked. This is source-string validation, not execution of the component or a synthetic interaction.

A peer reviewed the supplied source contract without provider reads or execution and reported no concrete semantic concern. That reasoning is supplementary, not a gate or runtime verification.

## Limits

Conditional branch rendering and an ARIA role alone do not establish that any particular browser/screen reader will announce a transition. Initial content, timing, coalescing, rapid saves, language changes and the actual accessibility tree were not exercised. No focus move, guaranteed delivery of every announcement, new error state, invalid-Date handling, saved-time persistence, initial-read recovery or broader accessibility result is claimed.

The already-existing hook controls what the displayed status means. This patch neither proves that persistence succeeded nor changes failure classification. Multiple mounted instances and their independent messages remain the existing application design.

No browser, DOM, assistive technology, compiler, runtime, tests, fixtures, storage, employee/payroll data, account, wallet, transaction, API, upstream PR, sponsor contact, acceptance or payment action was performed.

## Artifact and license scope

Only status-region.patch, this guide and the unchanged LICENSE are published. Complete donor application modules are not republished. The retained Apache-2.0 license text is the exact donor-tree blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`, 11357 bytes. Keep it and the repository notices with the patch; this guide identifies the modification.
