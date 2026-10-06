# Source evidence for the Wavelum translation gate

## Current issue and bounded carrier qualification

The requested consumer is [Wavelum frontend issue #71](https://github.com/stellar-network-builders/wavelum-frontend/issues/71), “Add CI validation for i18n translation completeness.” The native issue was observed open, unlocked and unassigned on 2026-10-06, with two comments. Both acquired comments request assignment; no maintainer assignment or pull-request link appears in those two comments. This observation does not confer ownership or permission to submit upstream.

The requirements call for matching locale key sets, detection of missing and unused translations, a minimum coverage level, an `i18n:check` npm command and a blocking `i18n-check` CI job. Warnings are requested for unused keys. Reward labels were observed, but this packet makes no award, eligibility, amount or payment claim.

A dedicated upstream all-state query for `"71" "i18n"` returned zero. A separate semantic `i18n` query returned PRs #41, #44, #32 and #34, whose returned descriptions concern JSDoc, testing infrastructure and the existing internationalization implementation. Their search rows supplied no native current author/status fields; they were not treated as verified carrier states. A scoped Commons query for `"wavelum" "71" "i18n"` returned zero. These bounded search results are not a global exclusivity guarantee.

## Immutable source binding

Repository: `stellar-network-builders/wavelum-frontend`.

Canonical commit: `39adce49545f0114ef0ae25ad835af39de46f492`.

Complete recursive tree: `be8107bb996c94cb0151bf4b95d0493b98aef946`, 293 entries, native `truncated: false`.

Every complete source body in the following table independently matched its native Git blob identity. The table records evidence; donor file bodies are not included in this publication.

| Source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| [CONTRIBUTING.md](https://github.com/stellar-network-builders/wavelum-frontend/blob/39adce49545f0114ef0ae25ad835af39de46f492/CONTRIBUTING.md) | `ec1cf887e0908372facf837b929565a3a43b8a65` | 3950 |
| [package.json](https://github.com/stellar-network-builders/wavelum-frontend/blob/39adce49545f0114ef0ae25ad835af39de46f492/package.json) | `abd989198d17220cb482e122f8e438fe7669bf6e` | 2984 |
| [.github/workflows/test.yml](https://github.com/stellar-network-builders/wavelum-frontend/blob/39adce49545f0114ef0ae25ad835af39de46f492/.github/workflows/test.yml) | `a86e106c5b9b4e5aae41f00c10f0d0132dcf7e8d` | 15253 |
| [i18n/routing.ts](https://github.com/stellar-network-builders/wavelum-frontend/blob/39adce49545f0114ef0ae25ad835af39de46f492/i18n/routing.ts) | `e312ea8c659001cdf362c8c766f4242f4607d529` | 181 |
| [messages/en.json](https://github.com/stellar-network-builders/wavelum-frontend/blob/39adce49545f0114ef0ae25ad835af39de46f492/messages/en.json) | `a6ce4fcc609596a72366fdb3d23c0f1143cc9e53` | 2644 |
| [messages/ja.json](https://github.com/stellar-network-builders/wavelum-frontend/blob/39adce49545f0114ef0ae25ad835af39de46f492/messages/ja.json) | `0c38f80c08e9f3227de29bd90b1daa2c17c65e24` | 3492 |
| [messages/ko.json](https://github.com/stellar-network-builders/wavelum-frontend/blob/39adce49545f0114ef0ae25ad835af39de46f492/messages/ko.json) | `6e974a85526010d3a81ddb491293a53f05c41910` | 3095 |
| [messages/zh.json](https://github.com/stellar-network-builders/wavelum-frontend/blob/39adce49545f0114ef0ae25ad835af39de46f492/messages/zh.json) | `82cdd66ba145914c36592e36eac1f4d911e83b45` | 2434 |
| [src/hooks/useLocale.ts](https://github.com/stellar-network-builders/wavelum-frontend/blob/39adce49545f0114ef0ae25ad835af39de46f492/src/hooks/useLocale.ts) | `11dcff16a563e34d093eddb927a61fe7cc60d2ab` | 967 |
| [i18n/request.ts](https://github.com/stellar-network-builders/wavelum-frontend/blob/39adce49545f0114ef0ae25ad835af39de46f492/i18n/request.ts) | `b27ec7e14b006a282adb9ba8151294579bd34bc3` | 445 |
| [app/[locale]/page.tsx](https://github.com/stellar-network-builders/wavelum-frontend/blob/39adce49545f0114ef0ae25ad835af39de46f492/app/%5Blocale%5D/page.tsx) | `682c3f1dcfc391f7ede37326429cf71384691bfc` | 2170 |
| [src/components/ui/LocaleSwitcher.tsx](https://github.com/stellar-network-builders/wavelum-frontend/blob/39adce49545f0114ef0ae25ad835af39de46f492/src/components/ui/LocaleSwitcher.tsx) | `bfe4eda30a04c63ae1a4f73520e683912c9d249b` | 2061 |
| [src/hooks/useErrorToast.ts](https://github.com/stellar-network-builders/wavelum-frontend/blob/39adce49545f0114ef0ae25ad835af39de46f492/src/hooks/useErrorToast.ts) | `6abde543ad31f7c7b998b941654248945e7a726a` | 5434 |

The complete tree contains no AGENTS.md or RULES.md path and no license/notice filename matching the acquisition screen. Repository license metadata is null. That is the observed metadata, not a legal conclusion about the repository. This publication contains original new artifacts and integration instructions, without a full donor file, copied source patch or asserted upstream license grant.

## What the actual source establishes

- The package declares Node >=20.9.0 and an existing TypeScript ^5 development dependency. Its complete scripts object has no `i18n:check` command.
- The existing complete CI workflow has no translation validation job. It already uses Node 22, checkout v4 and setup-node v4; the proposed separate workflow follows those observed tool versions without changing that workflow.
- Routing declares four locales: en, ja, ko and zh, with en as the default. The request loader imports the corresponding locale JSON file.
- All four acquired catalogues contain 46 string leaf keys. Their key sets match, every value is nonempty after trimming, and there are 46 keys in the union. This is an analysis of retained catalogue data, not an execution result from the new checker.
- The `LocaleSwitcher.locale` message is identical across all four files and contains a multilingual ICU select. Equality to English is therefore not a valid untranslated-value test for this consumer.
- The acquired home-page and locale-switcher consumers use literal translation keys with a literal namespace. The acquired `useLocale` wrapper exposes an unscoped translator. The unused-key scan deliberately reports only conservative static candidates; it does not claim whole-program reachability.

## Validation boundary

The new Node program, dependency installation, npm command, TypeScript compiler, application build, tests, browser and GitHub workflow were not executed. No upstream branch, issue comment, claim, pull request or merge was created. Original artifact identities and publication readbacks are recorded separately from the source observations above.

The complete tree and retained source bodies support the proposed integration paths. They do not establish that the original source remained current after the pinned observation, that the new gate has passed in Node, that ICU messages are linguistically correct, or that warning candidates can be safely deleted.

## Primary API references

- [TypeScript compiler API guide](https://github.com/microsoft/TypeScript/wiki/Using-the-Compiler-API): source-file parsing and AST traversal.
- [Node file-system API source documentation](https://github.com/nodejs/node/blob/main/doc/api/fs.md): reading UTF-8 files and traversing directory entries.

These references support the chosen APIs. They are not substitute runtime results.
