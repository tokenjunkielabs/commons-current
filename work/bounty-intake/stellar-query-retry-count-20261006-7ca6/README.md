# Preserve configured query retry counts

The mounted SEP-24 caller passes `retry: 2` through useApiQuery for anchors, capabilities and history. The acquired wrapper declares only a boolean retry option and converts every value except false to true. The existing count therefore becomes the library's indefinite-retry flag. This patch accepts and forwards numeric counts while preserving the wrapper's existing boolean and omitted-option behavior.

## Source and actual caller

Donor: Stellar-Analysis/frontend at `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete acquired input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/lib/react-query/hooks.ts | 5bc662d0ba7d7d9c122a39534a7be65ab1cf77ee | 5664 |
| src/hooks/useSep24.ts | d42e151d1375add1d4be846676af8f9f3e4d1afb | 4726 |
| src/components/Sep24Flow.tsx | 1c11c3c5669b3cb6406d40e474460dc6e695afb1 | 14513 |
| src/app/[locale]/deposit-withdraw/page.tsx | f064a0a1331da46f035b54602f98093b2e0c8c8d | 1357 |

These complete source bodies were already acquired for the connected SEP-24 interface review and were reused without a new source read. The route mounts Sep24Flow through a named dynamic import with SSR disabled. That component calls the three query hooks; each hook passes numeric 2 to useApiQuery. The generic wrapper passes its options into useQuery without another retry transform.

The independent native-blob route identity and the independently derived full-file identities from immutable contents URLs are preserved separately. The contents tool did not return separate native SHA fields for the wrapper, hook or component. The earlier source/spec checkpoint is `56d6b9b9fcc2ab831ed86f45030f7aee83590362`; this continuation does not replay its accepted artifact checks.

Commons [#32133](https://github.com/woahwhattheheck/commons/pull/32133) contains the separate uncompiled SEP-24 binding/order/envelope/form-context proposal. This patch touches only the shared wrapper and can compose with that proposal. Its hook import, component JSX and handler bodies remain protected. Fixing numeric retry forwarding does not remove the other unresolved compiler, context-documentation or integration limitations described there.

## Exact change

The options type becomes `retry?: boolean | number`. The forwarded value becomes `options?.retry ?? true`. This is +2/-2 in two hunks; every other source byte is exact.

| Source | Before | After | After bytes |
| --- | --- | --- | ---: |
| src/lib/react-query/hooks.ts | 5bc662d0ba7d7d9c122a39534a7be65ab1cf77ee | bfbec4e0592af5b24260af9b059f93a64a466a75 | 5671 |

Within the typed option contract, false remains false, true remains true, and an omitted options object or undefined retry still becomes true. Valid numeric counts now reach TanStack unchanged, including zero. The patch deliberately preserves the existing omitted-option choice; it does not switch callers to the library default or introduce a new retry policy. No delay, enabled flag, query key, error, logging, stale-time, refetch or mutation code is changed.

The successful primary useQuery reference at https://tanstack.com/query/v5/docs/framework/react/reference/useQuery (site redirect to current v5 documentation) distinguishes false, true and numeric retry counts: true permits indefinite retry, while a number configures the failure limit. Retained package/lock evidence records TanStack React Query 5.100.5; that is a declared/locked fact, not installed-package execution. No new docs request was made for this continuation.

## Qualification and attribution

Dedicated all-state PR queries for useApiQuery plus retry returned zero in the donor repository and Commons. Bounded current-path history returned the relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888; it does not establish original authorship.

The authorized-channel Slack query returned twenty broad retry-topic results, none with the literal useApiQuery, and supplied a continuation cursor. It does not establish exhaustive overlap absence. Those mixed result bodies were inadvertently projected before screening; they remain held and were not used as source tasks, authority or permission. No retry or alternate recovery of a failed route was made. This guide records that limitation instead of presenting the query as an empty result.

The acquired caller is a concrete numeric configuration, not a hypothetical future API user. This is nevertheless a shared-wrapper change: any existing valid numeric option passed through this wrapper would now be honored. The bounded review did not inventory every application caller or assert repository-wide retry correctness.

## Checks and limits

Pure source-string checks independently hashed the complete preimage/postimage, serialized both unified hunks, and reconstructed the full after/before strings in both directions. Reversing only the two selected replacements restores every original byte. The before/after behavior above is reasoning about the expressions and documented option contract, not a fixture, simulation, runtime or request-count measurement.

Invalid counts such as negative values, fractions, non-finite values and runtime values outside the declared boolean/number/undefined contract are not normalized or validated. Functional retry predicates are not added to the local interface. The patch does not change configured query lifetimes, cancellation, reset semantics, request overlap, cache identity, rate limiting, authorization or availability. The inherited wrapper default remains true and can therefore still retry indefinitely when the option is omitted.

Other acquired wrapper/helper defects and the SEP-24 clearFormData reference remain outside scope. No full compiler, lint, test, browser or application-readiness result is claimed. No endpoint, retry loop, API request, authentication, credential, wallet, account, payment or storage operation was executed.

The retained complete donor tree has no AGENTS/RULES path. docs/CONTRIBUTING.md is EventSource-specific test/npm-release guidance; this session authorizes source-only Commons work and excludes those operations. The differently attributed docs MIT notices do not establish a blanket repository license. Only this minimal patch and guide are added to the Commons tree. The donor repository, contributor attribution, issue ownership and upstream acceptance/payment state are unchanged.
