# AlertsPage logger binding and selected-rule form identity

The mounted alerts route calls `logger.error` in seven catch blocks but neither imports nor declares `logger`. The donor's existing logger module exports the named object and the `error(message, error?, metadata?)` method those calls expect. This patch adds that one named import. It changes no alert operation or logging implementation.

This directory also contains the separate selected-rule form continuation described at the end. Apply the logger import first, then the form-identity patch; each patch has its own immutable preimage. The original logger explanation below remains scoped to its one-import patch.

## Exact source and connection

Canonical repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend). All source inputs below are pinned to commit `482ee456369418ef82c4056718cb82d3468f762b`; a fresh native main-ref guard returned that same commit before publication.

| Role | Actual path | Git blob | UTF-8 bytes |
| --- | --- | --- | ---: |
| Before | `src/app/[locale]/alerts/page.tsx` | `b2b301ad85b01d6faa327119248cba5fe957fcd5` | 16,333 |
| After this patch | `src/app/[locale]/alerts/page.tsx` | `e57d52687aec99a522235a52c1d173ca7eacdbe5` | 16,372 |
| Existing dependency, unchanged | `src/lib/logger.ts` | `7c99dbe969798e1b1b7a8a80a18c6c26110c4682` | 11,575 |

The complete route is an actual App Router `page.tsx` with a default `AlertsPage` export. Its initial effect calls `loadData`; its existing create, update, delete, active-toggle, history-dismissal and snooze handlers supply the other six catch paths. The complete logger source exports `logger` and even documents the same `@/lib/logger` named import. These are actual source connections, not a claim that any alert request or exception was executed.

## Change and application

Apply `import-alerts-logger.patch` to the exact donor commit or compose it with independently reviewed changes to the same import block. It contains one hunk, **+1/-0**, adding:

```ts
import { logger } from "@/lib/logger";
```

Every original handler, catch call, loading transition, API call, form, confirmation, rule threshold, JSX node and class remains byte-for-byte unchanged. The logger module is an input only; its environment gates, redaction, tracking and fallback behavior are not modified.

The correction supplies the missing lexical binding used by the existing catch blocks. It does not establish a successful backend operation, full typecheck or build, comprehensive error recovery, telemetry delivery, logging configuration, redaction adequacy or user-visible failure feedback. A logging call may still have the existing logger's behavior. No alert, account, storage or tracking data was acquired or acted on.

## Source integrity and scope

Both complete immutable inputs were read once for this new task and independently matched to their Git blob identities. The complete line comparison has one inserted line and no deletions. The serialized patch reconstructs the exact postimage and its inverse reconstructs the exact preimage using pure retained-text operations. Those checks are artifact integrity checks, not application tests or execution.

Before authoring, bounded public Slack exact-path/logger history and repository-specific Commons and donor PR queries returned zero results; the GitHub results reported `incomplete_results: false`. This does not claim a global absence of other work. No held route was retried or recovered. No source from protected earlier packets was changed.

No application, browser, test, fixture, workflow, dependency installation, native device, alert API or logger runtime was invoked. There is no upstream submission, author assignment, maintainer acceptance, bounty award or payment claim.

## Attribution and instructions

The page, handlers and logger are existing work of the Stellar-Analysis/frontend contributors. This Commons continuation contributes only the missing import and this explanatory guide; it does not claim the upstream implementation or replace any contributor's rights or acceptance conditions.

The acquired complete donor tree contained no AGENTS or RULES path. Its retained `docs/CONTRIBUTING.md` at blob `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` is headed “Contributing to EventSource” and contains test/release guidance. This session explicitly excludes runtime, tests and package publication. Differently attributed MIT notices in the donor do not establish a repository-wide licence for these modules. Accordingly this packet contains a minimal patch and an original guide, not copies of either complete module.

## Separate continuation: initialize the draft for the selected rule

The complete `AlertRuleForm` initializes metric, condition, threshold, corridor and three notification choices from `initialData` with local state. The actual alerts page leaves the form mounted while its list remains interactive. Every rule's Edit button can replace `editingRule` and set the already-true `isFormOpen` again. The form then receives a different `initialData`, while the page's submit callback targets that new rule ID.

Without a changed component identity, the fields can retain the previous draft under the new save target. The same mismatch is possible when an open create form is switched to an existing rule via that list. This is a source-established caller path; no actual rule or account was read or changed.

The follow-on `reset-selected-rule-form.patch` adds exactly one key:

```tsx
key={editingRule ? `edit:${editingRule.id}` : "create"}
```

The namespaced edit key is distinct from the create key even when a legitimate string ID itself equals `create`. Selecting a different rule or switching from create to edit remounts the form and uses that selection's existing initializers. Re-renders with the same rule ID preserve its draft. Switching away discards that local draft; this does not create per-rule saved drafts or a confirmation policy.

| Input or output | Actual path | Git blob | UTF-8 bytes |
| --- | --- | --- | ---: |
| Page after #31986, before this continuation | `src/app/[locale]/alerts/page.tsx` | `e57d52687aec99a522235a52c1d173ca7eacdbe5` | 16,372 |
| Page after both patches | `src/app/[locale]/alerts/page.tsx` | `11b1de1fcea8b21919f61c04152bbfd008571fa5` | 16,452 |
| Unchanged complete form input | `src/components/AlertRuleForm.tsx` | `97d01198bc9855e3d5e5c8463a4f8012644fda0a` | 8,311 |
| Unchanged rule type and API contract | `src/lib/alerts-api.ts` | `9542be40db7573e988344f812b1115833b58149d` | 2,107 |

All inputs belong to the same donor commit above. The type declares `AlertRule.id: string` and the existing update adapter uses that ID in the rule URL. No API implementation, request data, threshold policy, form field, initializer, onSubmit/onCancel handler, loading state or completed logger import is modified. The incremental source diff is **+1/-0 in one hunk**.

[React's primary state-preservation documentation](https://react.dev/learn/preserving-and-resetting-state), “Resetting state with a key” and “Resetting a form with a key,” explains that a changed key creates distinct component state and recreates the subtree. That contract supports the selected-rule reset; no documentation examples were executed. A fresh donor guard remained at the pinned commit, and bounded Commons/public Slack overlap searches returned zero without asserting global absence.

The serialized incremental patch and inverse reconstruct the complete recorded postimage and preimage. The original `import-alerts-logger.patch` remains unchanged. This is an attributed in-place continuation of [Commons #31986](https://github.com/woahwhattheheck/commons/pull/31986), preserving the original authors and earlier limits.

This change does not address an already-started request finishing after another selection, duplicate submissions, same-ID data refresh, malformed/duplicate IDs, backend ownership, atomic writes, focus restoration after remount, persistence or full form accessibility. No browser, runtime, tests, requests, account operation, upstream action, acceptance or payment claim is made.
