# Preserve the StateProvider hook export once

The mounted StateProvider module exports `useDebugTools` at its function declaration and repeats the same exported name in its final export list. This patch removes only the repeated list entry. `useDebugTools` remains a named export through its unchanged declaration, and `StateDevTools` remains exported through the final list.

This is a source-level module compatibility correction. No compiler, bundler, application, browser, dependency installation, lint, test, fixture, or workflow was run, and no whole-build success is claimed.

## Exact source and caller

Repository: https://github.com/Stellar-Analysis/frontend

Pinned donor: `482ee456369418ef82c4056718cb82d3468f762b`. A fresh named-main observation on 2026-10-06 at approximately 07:52 UTC returned that commit. This is a bounded observation, not a provider snapshot or a deployment claim.

| Role | Path | Git blob SHA | UTF-8 bytes |
| --- | --- | --- | ---: |
| Complete original source | `src/components/StateProvider.tsx` | `5c5e7d7f021bf5e072278a5161d04b0dcbf257d7` | 3190 |
| Candidate postimage | same path | `0e1dcc03a89c254787636dbed3afe933abbcf5da` | 3175 |
| Retained mounted caller | `src/app/[locale]/layout.tsx` | `1f016787657313d58504e79bccbe634a843ce8b5` | 4212 |

The actual locale layout imports `StateProvider` from `@/components/StateProvider` and wraps its sidebar, navbar, route children, and other UI in that provider. The module is therefore connected to the application source. This does not assert that any route was rendered during this work.

The complete source came from CI's retained native acquisition. Two intermediate transfer transcriptions failed or could not support the expected identity: the corrected actual `activeQueries` expression is `q.getObserversCount() > 0`. After that exact retained correction, all 3,190 source bytes independently matched the native blob pin. Both earlier transfer mistakes were preserved privately; neither was treated as a source preimage. No guessed-byte repair or provider source replay was used.

## Why this is a concrete module defect

[ECMAScript 2026, §16.2.1.1](https://tc39.es/ecma262/2026/multipage/ecmascript-language-scripts-and-modules.html#sec-module-semantics-static-semantics-early-errors) rejects duplicate entries in a module's ExportedNames. Its [ExportedNames rules in §16.2.3.3](https://tc39.es/ecma262/2026/multipage/ecmascript-language-scripts-and-modules.html#sec-exports-static-semantics-exportednames) include a declaration's bound names and the names supplied by export specifiers, combining them across module items. The [TypeScript module reference](https://www.typescriptlang.org/docs/handbook/modules/reference.html) documents its use of standard ECMAScript module syntax.

Here the existing `export function useDebugTools()` contributes `useDebugTools`, and the final `export { StateDevTools, useDebugTools }` contributes it again. The patch removes the second occurrence. This is a static source-and-contract conclusion, not a recorded compiler diagnostic or a reproduced runtime failure.

## One-line scope

`change.patch` has one addition and one deletion. The final line changes from:

```tsx
export { StateDevTools, useDebugTools };
```

to:

```tsx
export { StateDevTools };
```

The function declaration, its return value, effect and interval behavior, StateProvider tree, StateDevTools implementation, logger calls, imports, and all other bytes are preserved. This patch does not evaluate or correct other debug-tool behavior, query metrics, store typing, lifecycle policy, or application-wide type/build issues.

## Bounded chronology and attribution

A five-entry current-path commit-history request returned one row: [christabel888's relocation commit 59fad72d](https://github.com/Stellar-Analysis/frontend/commit/59fad72d9fbef9cfd6f47e215392da44488fcdc4). The lookup was for the present path and does not reconstruct older renamed-path history.

The exact StateProvider PR search returned [yosemite01's PR #116](https://github.com/Stellar-Analysis/frontend/pull/116). Separate native PR metadata confirmed it closed and merged on 2026-06-18, head `9b5c720293f5e85b1dcd7e2ed1057f2e64623752`. Its complete 13-file metadata response includes the same StateProvider blob `5c5e7d7f021bf5e072278a5161d04b0dcbf257d7`; the displayed patch replaces console calls with logger calls and leaves this export suffix unchanged. That contribution is preserved. Historical test/build statements in upstream messages are their authors' reports and were not rerun or adopted as validation of this patch.

A bounded first page of public activity search was screened as headers and short prefixes, with private and held topics withheld. It did not establish another current writer of this line; the returned continuation was retained. Query fidelity, all-history completeness, and absence of other owners are not inferred. CI's current ThemeContext work is a different file.

## Packaging and limits

The transferred complete donor tree has no root AGENTS or RULES file; its CONTRIBUTING material is specific to EventSource work. Existing MIT notices have differing named attributions and do not by themselves establish a repository-wide license. This Commons packet therefore contains a narrow patch and this guide, not a full copy of the upstream module.

The already preserved notices remain available under [the prior generator packet](../stellaranalysis-issue-generator-layout-20261006-7ca6/): `upstream-licence-mclaughlin.md` (`57740b9d4d86aedf5d518f2f363d5cf192c54127`), `upstream-license-menke-laguna.md` (`af5411fa243cfcf2b61c79d081dbb6204e956041`), and `upstream-license-de-wet.md` (`4a766e268772888af5df56c3f6c608f68558b789`). Their individual wording and scope remain unchanged.

This is a Commons source continuation only. No upstream claim, assignment, submission, pull request, merge, deployment, award, or acceptance action is made. Upstream maintainers retain their review and acceptance requirements. Exact packet identity and publication readbacks establish delivery of these artifacts; they do not establish application execution.
