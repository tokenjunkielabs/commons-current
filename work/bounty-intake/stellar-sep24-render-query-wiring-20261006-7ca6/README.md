# SEP-24 render and query wiring — uncompiled source proposal

The mounted deposit/withdraw page dynamically loads Sep24Flow. The current component evaluates query arguments before its watched variables are initialized, references undeclared bindings, consumes response envelopes as arrays, and renders shared fields without passing its local form instance through their context. This patch aligns that connected render path with the acquired service and hook interfaces. It is a source proposal, not evidence that deposits, withdrawals, authentication, history requests, or the application build work.

## Donor and custody

Donor: Stellar-Analysis/frontend at immutable commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete acquired source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/app/[locale]/deposit-withdraw/page.tsx | f064a0a1331da46f035b54602f98093b2e0c8c8d | 1357 |
| src/components/Sep24Flow.tsx | 1c11c3c5669b3cb6406d40e474460dc6e695afb1 | 14513 |
| src/hooks/useSep24.ts | d42e151d1375add1d4be846676af8f9f3e4d1afb | 4726 |
| src/services/sep24.ts | a318c18c66ddd619fd80775e40acccaca3bd63c3 | 5345 |
| src/lib/react-query/hooks.ts | 5bc662d0ba7d7d9c122a39534a7be65ab1cf77ee | 5664 |
| src/lib/schemas.ts | e2a396eac77810eaeda5ed3a228653f9facbdb5f | 4342 |
| src/components/ui/FormField.tsx | b33a9c042b16d6284019a34a1225bed4947a8756 | 7473 |

The route, schema and shared-field pins were independently matched to their native blob locators. Flow, hook, service and query-wrapper identities were independently computed from complete source returned by immutable contents URLs; those responses did not include separate native SHA fields. Delivery had already acquired the route and flow when CI's two reads crossed the custody notice. That duplicate acquisition is recorded, not hidden. Delivery then explicitly transferred the complete static interface/initialization qualification to CI and made no patch to these files. No further route, flow or shared-field read was used.

Bounded current-path history for both changed files returned only the repository-flattening commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888. That relocation is not evidence of original authorship. Dedicated all-state PR searches for Sep24Flow and useSep24 in both donor and Commons returned zero; the bounded authorized-channel Sep24Flow search also returned zero. These are bounded overlap observations, not global absence, issue ownership, eligibility, acceptance or payment conclusions.

## Actual source contract and change

- The route imports the named Sep24Flow export with SSR disabled and renders it without props.
- The schema exports Sep24FlowForm. The service exports Sep24AnchorInfo and Sep24Transaction. The component now imports the already-used React useState and service types, and uses SubmitHandler<Sep24FlowForm> instead of its undeclared Sep24Form name.
- The component keeps one useForm call and its exact resolver, mode and defaultValues. Its complete result is retained as methods, with the prior destructured bindings preserved. The existing JSX is assigned to a local value and returned under FormProvider with that instance. Shared FormField and FormSelect call useFormContext and register their names; their code is unchanged.
- All three query hooks now run unconditionally after the watched transferServer and jwt declarations, before effects or rendering consume their results. No conditional hook or early-return path is introduced.
- getSep24Anchors returns Sep24AnchorsResponse with an anchors array; getSep24Transactions returns Sep24TransactionsResponse with a transactions array. The generic useApiQuery returns useQuery without changing the response shape or supplying initialData. The component selects those array members and uses an empty array while the response/member is absent. This is not runtime schema validation or proof that a failed request succeeded with an empty result.
- The existing Load history button now resolves to a zero-argument callback that invokes the current query's refetch. It does not pass the React click event as query options. Its JSX, visibility, loading flag, text and endpoint/parameters are unchanged.
- Both mounted mutation hooks already call useQueryClient. The only hook-file change adds that missing named import from the package already used by the acquired generic mutation wrapper. The complete remainder of that file stays exact.

The source patch is +26/-15 across 10 hunks and two files.

| Changed source | Before | After | After bytes |
| --- | --- | --- | ---: |
| src/components/Sep24Flow.tsx | 1c11c3c5669b3cb6406d40e474460dc6e695afb1 | fd50330e97b1238581560ac460a3eaac19ba2103 | 14981 |
| src/hooks/useSep24.ts | d42e151d1375add1d4be846676af8f9f3e4d1afb | 5e29480896eb73109b71a574eb2b866bf6818da4 | 4742 |

## Evidence boundaries

The successful TanStack useQuery primary page, requested at https://tanstack.com/query/v5/docs/framework/react/reference/useQuery and redirected by the site to its current v5 reference, states that data may be undefined and exposes refetch as a manual query function returning a Promise. The successful primary search result at https://old.tanstack.com/query/latest/docs/framework/react/reference/useQueryClient identifies the named package import and current-client contract. The newly attempted exact https://tanstack.com/query/v5/docs/framework/react/reference/useQueryClient open returned Internal Error and remains held; it was not retried or recovered through another route. The earlier successful result and the acquired local wrapper import are separate evidence.

The earlier exact React Hook Form FormProvider and useFormContext documentation URLs returned 403 and remain held, without retry or alternate recovery. This context wiring is an explicitly uncompiled proposal based on the complete local field/form contracts and retained declared/locked React Hook Form 7.79.0, resolver 5.2.2 and Zod 4.4.3. Retained dependency evidence also records React 19.2.7, Next 16.2.10, TypeScript 5.9.3 and TanStack React Query 5.100.5. These are manifest/lock facts, not an installed-package or runtime check.

## Preservation and remaining defects

The entire original JSX block remains byte-for-byte exact inside its new provider return. The original effects, startFlow body, mutation choice/parameters, dirty/valid gate, anchor selection, status-color classifier and error/history markup remain exact; only the declared submit-handler type changes. The hook's query keys, enabled/stale/retry options, mutation bodies, notifications, popup behavior and invalidations are unchanged.

This is deliberately not a whole-module compilation or operational-readiness claim. The acquired shared wrapper declares retry as boolean while this hook still supplies numeric 2, and forwards retry as a boolean comparison; that existing mismatch/policy remains. The hook's unused clearFormDataValue closure still references clearFormData without binding it. Other unused imports/bindings and shared-wrapper helper defects are not repaired. No new caller of that closure is introduced.

The transaction query key still omits jwt. Existing cached-data identity, request overlap/cancellation, error display, authorization, amount/asset policy, preset dirty-state behavior, polling/retry policy, popup handling and interactiveUrl feedback are not validated or expanded. The local interactiveUrl state is still only cleared by this component; the acquired mutation hooks own their existing popup path. The history callback does not add a new error presentation policy or prove successful retrieval. A malformed non-array response member remains outside the typed service premise. Any eventual application of this proposal must separately address remaining compiler and integration defects before claiming a working feature.

## Source checks and publication boundary

Pure retained-string checks independently hashed all complete inputs and both postimages, generated the unified diff, and reconstructed each postimage and preimage from its serialized hunks in both directions. Preservation checks established exact JSX, exact existing handler/effect bodies except the named type, one useForm call with unchanged options, and exact hook content after its first import line. An initial local projection used the helper's default eight-hunk display limit; the coverage assertion rejected it before storing a candidate. The corrected projection included all ten hunks and passed reconstruction. No application code, compiler, fixtures, tests or runtime were executed.

The retained complete donor tree had no AGENTS/RULES path. Its docs/CONTRIBUTING.md is EventSource-specific test/npm-release guidance; this session authorizes source-only Commons proposals and excludes those operations. The three differently attributed docs MIT notices do not establish a repository-wide license grant for this component. Accordingly this packet contains a minimal patch and this guide, not a redistributed source snapshot in the repository tree.

No browser, form interaction, storage, credentials, auth, wallet, account, payment, network API, signing, popup, clipboard, device or upstream submission occurred. All request-shaped text reviewed here is public source. The Commons publication does not modify the donor repository, claim upstream acceptance, or establish a completed bounty.
