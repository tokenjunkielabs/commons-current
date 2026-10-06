# Route failed-mutation variables through the existing logger redaction

The shared mutation wrapper passes its failure context as the second argument to `logger.error`. In the acquired logger, that position is the error payload, while structured metadata belongs in the third position. The actual SEP-24 form includes an optional `jwt` field in mutation variables. A failed mutation therefore sends that object through the error-payload path instead of the logger's existing recursive metadata redaction.

This packet adds `undefined` as the second argument of that one failure log call. The unchanged context object becomes the third argument. The existing redactor then handles nested `variables.jwt`, and the tracking error payload becomes the fixed message `Mutation failed`. The original caught error is still rethrown to the query library. No mutation, authentication, logging, service or account operation was executed.

## Artifacts and composition

- `change.patch`: one hunk, +1/-1, in `src/lib/react-query/hooks.ts`.
- This guide: the actual caller chain, logger contract, exact identities and limits.

The patch is composed **after** the accepted Commons #32137 retry-count correction. Its full supplied postimage was independently matched before this new change. The numeric retry type and nullish fallback remain exact. This packet does not replay or revalidate the earlier runtime behavior.

| Source stage | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Canonical wrapper at frontend donor | `5bc662d0ba7d7d9c122a39534a7be65ab1cf77ee` | 5,664 |
| Exact inherited #32137 wrapper postimage | `bfbec4e0592af5b24260af9b059f93a64a466a75` | 5,671 |
| New composed wrapper postimage | `7b87d6d41b7858620bdcce6f2133ac78a24ff5c0` | 5,682 |
| Actual logger, unchanged | `7c99dbe969798e1b1b7a8a80a18c6c26110c4682` | 11,575 |

Repository: `Stellar-Analysis/frontend`  
Canonical donor: `482ee456369418ef82c4056718cb82d3468f762b`  
Changed path: `src/lib/react-query/hooks.ts`  
Logger path: `src/lib/logger.ts`

The complete canonical wrapper and exact two #32137 replacement ranges were transferred directly from the CI seat's retained source. This seat independently matched the canonical wrapper and inherited postimage identities. The accepted replacements are the retry option type `boolean | number` and the existing-default expression `options?.retry ?? true`. They are not part of the new patch.

The complete logger was acquired from its exact immutable blob request and independently matched. The native blob tool returns content without a separate returned SHA field, so this is request-bound native content plus an independent Git blob identity, not a fabricated native SHA response.

## Actual mounted consumer

The CI seat supplied exact selected caller excerpts and immutable identities from its acquired source, without provider rereads. This seat does not claim a new complete native acquisition of those caller files.

| Role | Path or entry | Canonical blob | Bytes |
| --- | --- | --- | ---: |
| Route rendering the flow | `src/app/[locale]/deposit-withdraw/page.tsx` | `f064a0a1331da46f035b54602f98093b2e0c8c8d` | 1,357 |
| Form component | `src/components/Sep24Flow.tsx` | `1c11c3c5669b3cb6406d40e474460dc6e695afb1` | 14,513 |
| Domain hooks | `src/hooks/useSep24.ts` | `d42e151d1375add1d4be846676af8f9f3e4d1afb` | 4,726 |
| Service schema | `src/services/sep24.ts` | `a318c18c66ddd619fd80775e40acccaca3bd63c3` | 5,345 |

The route dynamically imports named `Sep24Flow` with `ssr: false` and renders it. In the form's retained `startFlow` body, the selected deposit or withdrawal mutation receives a params object containing `jwt: data.jwt || undefined` via `mutation.mutate(params)`.

The domain hook literally imports `useApiMutation` from `@/lib/react-query/hooks`. Both start-flow hooks pass variables containing `transferServer` and optional string fields including `jwt` to that generic wrapper, then to the service. The service's deposit and withdrawal parameter interfaces each declare `jwt?: string`.

Accepted #32133 changed the form's query/provider wiring and added the domain hook's query-client import. Its supplied form postimage is `fd50330e97b1238581560ac460a3eaac19ba2103` / 14,981 bytes, and hook postimage is `5e29480896eb73109b71a574eb2b866bf6818da4` / 4,742 bytes. CI explicitly confirmed the parameter construction and mutation bodies above remain exact. No caller file is changed or reconstructed here.

This is public schema and source evidence. No JWT, credential value, request, wallet, account or session was acquired or operated.

## Logger contract and why argument position matters

The acquired logger defines:

`error(message: string, error?: Error | unknown, metadata?: LogMetadata)`

Its metadata object is passed through `redactSensitiveData`. That function recursively visits arrays and objects, and replaces values whose field names match a case-insensitive pattern including `jwt`, `token`, `auth` and other credential-related terms.

The error-payload argument takes a different path. In development it is passed directly to `console.error`. In production, an object payload is normalized using `JSON.stringify` into an Error message, then routed to error tracking. Metadata redaction does not transform that original second-argument object.

The original failure call supplies `{ variables, error: ... }` in that second position. The new call supplies `undefined` there and passes the same object in the metadata position. Because the error payload is absent, the logger uses its fixed first argument as the tracking payload. The extracted error-message field remains available as metadata, subject to the logger's existing redaction rules.

The success call already uses `logger.info(message, metadata)`, whose second argument is redacted metadata. It remains byte-exact. This distinction is established by the complete first-party source, not by running the logger or inventing a credential fixture.

## Scope and limitations

Only the failure log call's argument routing changes. The metadata object, mutation function, success logging, query invalidation, custom callbacks, original error propagation and accepted retry correction remain exact. The logger implementation is unchanged.

This does not establish complete redaction for arbitrary data, messages or other log call sites. The separate `Query failed` call, generic logger payload behavior, unsupported object forms, logging configuration, transport failures and historical records are outside this patch. The existing callbacks still receive their intended original values; this change only directs this log context through the already-defined metadata path.

No credentials were generated, read, posted or tested. No external tracking request, backend request, browser, build, compiler, test, fixture, runtime or workflow was executed. There is no claim that a leak occurred in a running environment or that the entire application is secure.

## Validation and public checkpoint

Pure source checks established:

- The complete transferred canonical wrapper and exact inherited #32137 postimage identities.
- The complete newly acquired logger identity and its actual argument/redaction branches.
- One unique changed failure call, one unified-diff hunk, +1/-1.
- Forward patch application yields the exact composed postimage; reverse application restores the inherited postimage.
- Removing the new argument reproduces the inherited file byte-for-byte. Both accepted retry lines and the success log call remain exact.

The source packet contains only the narrow patch and this guide. A genuinely new frozen publication spec is checkpointed through the existing public-blob helper before publication, with the acknowledged manifest locator retained in the completion receipt. Full upstream modules, credentials and private native journals are not selected for that checkpoint. An acknowledged blob is not a branch/ref or an indefinite retention guarantee.

## Attribution and instruction custody

CI transferred the bounded native current-path history result from #32137: one row, commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, author/committer christabel888, describing relocation of the frontend into the repository root. This is current-path relocation metadata, not sole authorship or followed history. The earlier retry-specific searches do not establish absence of other logging work and are not reused as such.

Retained complete-tree instruction context at the canonical donor found no root AGENTS or RULES file. The original complete array was lost in the shared working-cache incident; no new census is claimed here. The retained EventSource-specific `docs/CONTRIBUTING.md` is `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` / 274 bytes and requests tests for changes. Upstream acceptance steps remain unperformed in this source-only lane.

The separate MIT notices are `docs/LICENCE.md` (`57740b9d4d86aedf5d518f2f363d5cf192c54127`, 1,104 bytes), `docs/LICENSE.md` (`af5411fa243cfcf2b61c79d081dbb6204e956041`, 1,111 bytes), and `docs/license.md` (`4a766e268772888af5df56c3f6c608f68558b789`, 1,080 bytes). Their differing attribution does not establish one repository-wide licence scope. This Commons continuation publishes patch hunks and explanation, not full upstream modules.
