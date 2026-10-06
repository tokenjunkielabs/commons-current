# Wavelum frontend: translation completeness gate

This is an original implementation packet for [Wavelum frontend #71](https://github.com/stellar-network-builders/wavelum-frontend/issues/71). It contains a Node checker, a separate GitHub Actions workflow and exact integration instructions for the inspected source revision. The checker and workflow have not been executed or installed in the upstream repository. Publication in Commons does not claim issue completion, an upstream submission or a reward.

## Files and target paths

| Packet file | Target path in Wavelum frontend | Purpose |
| --- | --- | --- |
| [check-i18n.mjs](check-i18n.mjs) | `scripts/check-i18n.mjs` | Validate declared catalogues and report static unused-key candidates |
| [i18n-check.yml](i18n-check.yml) | `.github/workflows/i18n-check.yml` | Run the checker on main-branch pushes and pull requests |
| [SOURCE_EVIDENCE.md](SOURCE_EVIDENCE.md) | Reference only | Immutable source pins, actual catalogue findings and qualification limits |

The two target files are new at the inspected complete tree. The workflow is stored as an inert packet artifact under `work/` in Commons; this publication does not install or dispatch it as a Commons workflow.

## Integration

The source binding is commit `39adce49545f0114ef0ae25ad835af39de46f492` in `stellar-network-builders/wavelum-frontend`, tree `be8107bb996c94cb0151bf4b95d0493b98aef946`. Before any later integration, compare the actual current routing/catalogue layout and package dependencies to [the recorded evidence](SOURCE_EVIDENCE.md). Do not overwrite a target file or an existing script added after this observation.

1. Place the original checker at `scripts/check-i18n.mjs`.
2. Add this one member to the existing `scripts` object in `package.json`, preserving its other entries:

   ```json
   "i18n:check": "node scripts/check-i18n.mjs"
   ```

3. Place the original workflow at `.github/workflows/i18n-check.yml`.
4. In an authorized execution environment, install the existing dependencies and run `npm run i18n:check`. Follow the upstream contribution guide for lint/build checks before requesting review. Those commands have not been run for this packet.

The recorded package already contains TypeScript ^5 and declares Node >=20.9.0. No new package or lockfile change is proposed. The workflow uses Node 22, consistent with the inspected existing workflow. Its `npm ci --ignore-scripts` step installs the declared parser dependency without running application lifecycle scripts; the checker only reads routing, catalogues and source text.

The new job is named `i18n-check`, has read-only contents permission and a five-minute timeout, and has no `continue-on-error`. A nonzero checker exit fails that job. Whether a failing job blocks merging additionally depends on repository branch rules; no branch rule was read, configured or claimed here. Main-branch push and pull-request triggers have no path filter, so changes to routing, catalogues, source, package scripts and the checker all reach the proposed check.

## Blocking checks

The checker derives the repository root from its own module URL. It parses `i18n/routing.ts` as TypeScript text and reads the exported `routing = defineRouting({...})` declaration; it never imports or evaluates application configuration.

The expected routing format is deliberately narrow: a directly exported variable, one `defineRouting` call with an explicit object, a nonempty literal locale array and a literal default locale belonging to that array. Parentheses and ordinary TypeScript assertion wrappers are accepted. Spreads, shorthand, computed properties, dynamic locale expressions and invalid filename identifiers fail with a diagnostic. A future routing refactor requires an explicit checker update instead of silently checking a guessed set of languages.

For every declared locale, the checker requires a corresponding regular `messages/<locale>.json` file. Additional JSON filenames are errors. It reads JSON objects recursively and rejects empty catalogues, empty property names, empty nested objects, arrays, nulls, non-string leaves and strings containing only whitespace. Ambiguous flattened dotted-key collisions also fail. JSON parsing uses normal `JSON.parse` semantics; this is not a separate duplicate-property linter or an ICU-message compiler.

Key parity is checked against the union of keys from every declared catalogue. This detects a missing key even if it was introduced first in a non-default locale. Each locale reports nonempty string leaves divided by that union. Required structural coverage is 100%, which is stricter than the issue's illustrative 90% minimum and consistent with its requirement that all locales have identical complete key sets.

Coverage describes present, nonempty message strings. It does not measure translation quality, language correctness or whether a string differs from English. Identical valid messages are permitted. That decision follows the actual `LocaleSwitcher.locale` ICU select, which is identical across all four current catalogues.

## Warning-only unused-key candidates

The checker statically parses regular TS/JS source files in existing `app` and `src` directories. It skips dependency/build directories, test/story patterns and TypeScript declaration files, and does not follow symbolic-link entries. It collects ordinary string literals and template literals without substitutions.

A catalogue key becomes a warning candidate only when neither its complete dotted name nor its final leaf name occurs in the collected literals. This conservatively accommodates the observed namespace-based calls and the unscoped translator wrapper without executing application code.

This is a bounded heuristic, not a proof of unused messages. A common leaf string appearing in unrelated code can conceal a truly unused key. Dynamic keys, indirect data flow and uses outside the scanned roots can produce warning candidates for messages that are actually used. Review the calling code before removing any candidate. The program never deletes or edits a catalogue.

Candidate warnings do not fail the job. An unreadable or syntactically unparseable source file is fatal, because a silently incomplete scan would be misleading. If neither root yields a source file, the program reports that limitation and suppresses candidate output; catalogue validation still applies.

## Evidence and verification limits

The retained actual catalogues each contain the same 46 nonempty leaf keys. All four have 100% structural coverage against the retained union. This finding was computed from those acquired source JSON files; it is not a reported run of the authored checker.

The original checker was inspected as source. The proposed workflow's trigger, permissions, command, timeout and failure propagation were checked against the integration instructions. The complete acquired source bodies independently match the native blob identities listed in [SOURCE_EVIDENCE.md](SOURCE_EVIDENCE.md).

No new program, npm install, compiler, lint command, build, test, browser or workflow was executed. There is therefore no runtime pass, CI pass, accepted test result or validated upstream behavior to report. Remaining execution verification includes checking that the actual installed TypeScript version parses the repository's source and that the job reaches the new package command after integration.

The packet contains original code and documentation. It does not publish full donor files or a context-bearing donor patch. It does not alter existing translations, routing, application components, existing workflows or upstream ownership. Publication custody and exact artifact readbacks are recorded in the Commons completion receipt.
