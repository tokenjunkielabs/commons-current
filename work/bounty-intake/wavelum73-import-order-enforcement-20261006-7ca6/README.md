# Enforce Wavelum's existing import-order rule

This packet supplies two original configuration files and a manual integration plan for [frontend issue 73](https://github.com/stellar-network-builders/wavelum-frontend/issues/73). It is an unexecuted proposal qualified against `stellar-network-builders/wavelum-frontend` commit `39adce49545f0114ef0ae25ad835af39de46f492`. The canonical source already has an import-order rule. Its warning severity, together with the current CI wiring, leaves those violations nonblocking.

The proposal raises only that existing rule's configured severity and supplies the missing staged-file command map. It preserves the existing ordering options and all other inherited rules. No donor source file, context patch, package rewrite, screenshot, dependency update or lockfile is included.

## Files and intended destination

| Artifact | Intended path in a separately reviewed frontend checkout | Purpose |
|---|---|---|
| [eslint.import-order.config.mjs](eslint.import-order.config.mjs) | repository root, beside the existing `eslint.config.mjs` | Import the existing flat-config array, then append a severity-only `import/order` override. |
| [lint-staged.config.mjs](lint-staged.config.mjs) | repository root | Run the same overlay with ESLint autofix for staged JS, MJS, TS and TSX files. |
| [SOURCE_EVIDENCE.json](SOURCE_EVIDENCE.json) | reference only | Public source identities, bounded carrier qualification and verification limits. |

The relative import in the overlay deliberately points at the frontend's existing configuration. This Commons directory does not contain that dependency and is not a runnable copy of the frontend.

## Actual source observations

At the qualified commit, `eslint.config.mjs` imports and registers `eslint-plugin-import`, then configures `import/order` with warning severity. It already defines builtin, external, internal and relative groups, the project's aliases, blank-line spacing and alphabetization. This proposal does not duplicate those options or introduce an alternate sorting policy.

The complete `package.json` has `lint` set to `eslint` and `lint:strict` set to `eslint --max-warnings 0`. It has no `lint:fix` script and no `lint-staged` configuration property. The complete recursive tree has no lint-staged-named configuration file. The current root `.husky/pre-commit` invokes lint-staged, then performs an informational audit. The hook's presence does not establish that Husky is installed or active in any checkout.

The parent task inspected the complete current `.github/workflows/test.yml`. Its `quality` job has no job-level conditional or continue-on-error setting. The normal lint step invokes `npm run lint`. A separate strict lint step is explicitly informational and has `continue-on-error: true`. No actual workflow result was queried or executed for this packet.

The published [ESLint v9 rule configuration contract](https://eslint.org/docs/v9.x/use/configure/rules) says warning severity does not affect the exit code, error severity does, and a later severity-only rule setting retains the earlier rule options. This is the basis for the overlay; it is not an observed lint result. Source comments can still override rule configuration, and ignored files remain subject to the inherited configuration.

## Manual integration against the qualified source

These are review instructions, not commands run by this delivery.

1. Confirm the frontend checkout and the source identities below. Review changes since the qualified commit instead of blindly replacing a newer configuration.
2. Place the two original `.mjs` artifacts at their intended root paths. Preserve the existing `eslint.config.mjs`; do not rename the overlay to that path, which would create a self-import.
3. In the existing `package.json` scripts object, set `lint` to `eslint --config eslint.import-order.config.mjs` and add `lint:fix` with value `eslint --config eslint.import-order.config.mjs --fix`. These are two manual field edits, not a prepared or applied package postimage. Preserve every other script, dependency and field, including any independently integrated issue 71 checker.
4. Keep the existing normal CI `npm run lint` invocation. Once the manual script edit is integrated, that invocation selects the overlay. The separate broad zero-warning step can retain its current policy; raising unrelated warning severities is outside this packet. Required-check or branch-protection settings were not inspected or changed.
5. The staged-file configuration uses a string command, allowing lint-staged to pass admitted filenames as arguments. It does not call `eslint .` from the staged-file command. The four admitted extensions match the file kinds described by the current hook; other extensions and noncode files receive no new staged task from this map.
6. Have the integrator review the actual lint output, dependency resolution, hook activation and any autofix diff in the intended environment before treating this proposal as ready to enforce. No package install, linter, hook, build, workflow or fixture execution occurred here.

The proposed `--fix` command runs every applicable fixable rule in the inherited configuration, not only import ordering. It may require manual changes where rules cannot fix safely. No mass reformat or guarantee of import-only changes is made. The package does not directly declare `eslint-plugin-import` even though the existing configuration imports it; installed or transitive resolution was not examined, and this packet makes no dependency-resolution claim or dependency change.

The [lint-staged project's current configuration documentation](https://github.com/lint-staged/lint-staged#configuration) documents ESM default-export configuration and string tasks that receive matching staged paths. That current documentation was successfully acquired before a separate attempt to read the v16.2.7 README returned an internal error. The exact versioned route is held without retry or alternate recovery. The current documentation is general support, not verification of the installed v16 package, hook or CLI behavior.

## Source identity and acquisition boundaries

| Path | Git blob | UTF-8 bytes | Evidence |
|---|---|---:|---|
| `eslint.config.mjs` | `84d7a2a7b33d8930fed0f4d8671c77a4a574fd46` | 2063 | Complete native text and independent identity match in this seat. |
| `.husky/pre-commit` | `7034c1cd193deba74483bb7dc8a2493c40b58cae` | 421 | Complete native text and independent identity match in this seat. |
| `package.json` | `abd989198d17220cb482e122f8e438fe7669bf6e` | 2984 | Complete parent native source transferred; independently matched here after a disclosed transfer transcription correction. |
| `CONTRIBUTING.md` | `ec1cf887e0908372facf837b929565a3a43b8a65` | 3950 | Complete parent native source transferred and independently matched here. |
| `.github/workflows/test.yml` | `a86e106c5b9b4e5aae41f00c10f0d0132dcf7e8d` | 15253 | Complete source retained and inspected by parent; only the relevant exact lint steps and enclosing job facts transferred here. |

The complete tree is `be8107bb996c94cb0151bf4b95d0493b98aef946`, 293 entries, with `truncated: false`, acquired by the parent. It contains no AGENTS, RULES or license-named file. The repository's license metadata is null. Those observations do not establish legal status or grant donor redistribution authority. This packet therefore contains original configuration text and analysis, public locators and identities; it does not reproduce donor full source or a donor context patch.

The contributor guide requests conventional commits, focused changes, lint/build validation and a normal upstream PR workflow. No upstream PR or acceptance request is made here, and the requested runtime checks are explicitly unperformed within this source-only task.

## Bounded current carrier qualification

Issue 73 was observed OPEN with no native assignee and four public comments, each an assignment request rather than a maintainer assignment or linked implementation. A dedicated all-state title search for `import` returned zero PRs; this is a bounded no-finding, not global absence or permission to claim the issue. An earlier issue-number query returned an unrelated dependency PR and did not establish issue coverage. A distinct dedicated Commons query for Wavelum and import order returned zero bounded results; the fresh donor-main guard still matched the qualified commit.

The issue asks for broader conventions, autofix, a staged hook and blocking CI. This proposal addresses enforcement of the currently configured rule and the staged command map. It does not add a separate styles/types-last policy, prove all imports conform, install the hook, remove pre-existing warnings, validate dependency resolution or complete the whole issue. Reward labels establish no amount, eligibility, acceptance or payout.

## Separate issue 68 disposition

The related visual-regression qualification found an existing screenshot assertion and a 1% pixel-difference threshold, an always-run report upload, and a workflow explicitly kept nonblocking until Linux baselines are committed. The complete current tree has no PNG anywhere; the baseline directory contains only its explanatory placeholder. Prior PR 54 is merged and describes introducing this preparatory setup; another broad CI PR 38 remains open and unmerged. These are current carrier observations, not proof of their runtime claims.

No screenshot was generated, baseline invented, threshold changed or continue-on-error flag removed. Issue 68 remains a separately qualified baseline prerequisite; it is not addressed by the original configuration files here.

## Verification performed and remaining work

Verification here consists of complete-source identity checks, static inspection, exact manual-transfer identity checks, primary documentation review and a retained-description peer check. The peer specifically noted the all-applicable-rules behavior of `--fix`; it did not perform source, provider or runtime validation.

The two new configuration files were not imported or executed. No ESLint, lint-staged, npm, Husky, Playwright, Storybook, build, CI, application, upstream write or account action occurred. Publication verification concerns only these original Commons artifact bytes and Git metadata. Integration into the frontend remains a separate reviewed action.
