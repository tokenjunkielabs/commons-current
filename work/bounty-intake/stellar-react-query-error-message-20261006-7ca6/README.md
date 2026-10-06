# Preserve React Query warning messages through metadata redaction

The mounted ReactQueryLogger warns about cached queries whose status is error. It currently places each query's error object inside logger.warn metadata. The shared logger recursively copies Object.entries when redacting metadata, so the usual non-enumerable Error.message is omitted. This patch projects a recognized Error to its message string at that one caller. The string then passes through the existing redaction rules.

This is an attributed, source-only continuation for Stellar-Analysis/frontend. It does not change the donor repository, install dependencies, execute the application, or establish that a warning occurred in a deployed environment.

## Exact source boundary

| Input or output | Git blob SHA | UTF-8 bytes |
| --- | --- | ---: |
| Canonical src/lib/react-query/logger.tsx | 9fe329c0fdd763c977c572da550e94a16aa80552 | 3578 |
| Candidate src/lib/react-query/logger.tsx | 0187a0a131b386b094df6dc104c3c6aea7918727 | 3635 |
| Unchanged src/lib/logger.ts | 7c99dbe969798e1b1b7a8a80a18c6c26110c4682 | 11575 |
| change.patch | a7dbffc1541d5c02174e653eeb63ce3a9c85d5f2 | 453 |

Donor repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend). Immutable donor commit: `482ee456369418ef82c4056718cb82d3468f762b`. Source path: [src/lib/react-query/logger.tsx at the donor](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/lib/react-query/logger.tsx).

The directory metadata identified the file and its blob. The native blob request returned the complete source string; it did not return a separate SHA field. An independent Git-blob calculation over that full string matched the requested blob and 3578-byte size. The shared logger was acquired and independently matched as a real dependency during the preceding mutation-metadata task, and its retained complete bytes were read for this new caller analysis.

The patch contains one hunk, +1/-1. It changes only the error field in the existing warning projection:

```tsx
error: q.state.error instanceof Error ? q.state.error.message : q.state.error,
```

The complete postimage was constructed from the exact source by one unique anchored replacement. Reversing that one replacement reproduced the full preimage exactly. No logger, query-wrapper, StateProvider, route, timer, package, test, or workflow file is changed.

## Actual mounted consumer

Retained complete-source provenance establishes the caller chain. StateProvider, canonical blob `5c5e7d7f021bf5e072278a5161d04b0dcbf257d7` / 3190 bytes, imports ReactQueryLogger from `@/lib/react-query/logger` and renders it beneath CustomReactQueryProvider. The locale layout, blob `1f016787657313d58504e79bccbe634a843ce8b5` / 4212 bytes, renders StateProvider. These are retained previously acquired source facts, not new whole-file acquisitions for this packet or a runtime mount observation.

The newly acquired logger component gets the query cache every 30000 milliseconds, selects query states whose status equals error, and sends count plus per-query metadata to logger.warn. Its cleanup clears the interval. That complete control flow, its dependencies and query-key expression remain byte-exact.

The shared logger's warn method accepts metadata as its second argument. When logging is enabled by its existing environment policy, the method sends that metadata through redactSensitiveData before console.warn. The redactor recursively handles arrays and copies object properties through Object.entries. Therefore a normal Error with no enumerable custom properties becomes an empty object along this source path, omitting its standard message. This is a source-and-language-contract inference, not captured production output.

## Language contract and behavior

The [ECMAScript Error constructor](https://tc39.es/ecma262/multipage/fundamental-objects.html#sec-error-constructor) creates its supplied message as a non-enumerable property. [Object.entries](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries) returns an object's own enumerable string-keyed properties. Both primary documentation pages were opened successfully for this qualification; no application or logger execution was used.

For a value recognized by the existing-realm `instanceof Error` check, the candidate emits its message string as the error metadata value. That string traverses the unchanged recursive redactor and its existing string rules. A non-Error value follows the original branch unchanged. The correction does not add stack, cause, name, or custom Error properties to the warning, and it does not promise cross-realm Error recognition. Custom enumerable properties on an Error are no longer the representation chosen at this caller; its message is the intended bounded diagnostic.

The existing warning level, environment enablement, query-key handling, error-status predicate, interval, cleanup, count, other exported hooks and cache operations stay unchanged. The redactor remains heuristic; this packet makes no universal privacy, sanitization, logger reliability, delivery, deduplication or telemetry guarantee. There were no actual credential values, query execution, authentication, wallet, browser, account, request, log emission or monitoring operations.

## History, attribution and protected work

A bounded native path-history request at the donor returned one current-path entry: `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888, titled “refactor: flatten frontend/ into repo root, eliminate parent/child duplication.” This establishes the observed relocation history only, not sole authorship or followed rename history. A dedicated all-state donor PR search for `"ReactQueryLogger"`, top 20, returned no rows. That is a bounded query result, not proof that no other work exists. Root's retained ownership record had no exact same-path hold or completion; custody gaps were not treated as universal clearance.

The shared wrapper's completed retry forwarding (#32137) and mutation logger.error metadata correction (#32140), StateProvider's completed duplicate-export and QueryCache corrections (#31962/#31968), and all held source/documentation routes remain outside this diff. No accepted patch was reconstructed or revalidated.

The earlier complete donor tree record contained 959 entries with truncated:false and no AGENTS.md or RULES.md. The full tree array was lost in the documented working-store reset, so this is retained instruction context, not a new census or reconstructed tree. The retained docs/CONTRIBUTING.md identity is `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` / 274 bytes; that document's EventSource-specific scope does not establish a new logger implementation policy. Its test requests do not imply that tests ran here; this lane is explicitly source-only.

Three differently attributed MIT notices are retained at docs/LICENCE.md `57740b9d4d86aedf5d518f2f363d5cf192c54127`, docs/LICENSE.md `af5411fa243cfcf2b61c79d081dbb6204e956041`, and docs/license.md `4a766e268772888af5df56c3f6c608f68558b789`. Their separate scopes are not inferred to license the entire repository. The Commons deliverable is a small patch and this original guide, not a republished donor module. Original authorship remains with the upstream contributors.

## Validation and recovery boundaries

Performed: complete immutable source acquisition, independent source/blob identities, actual caller and shared logger inspection from identified custody, language-contract reading, unique anchored source transformation, exact unaffected-byte comparison, patch identity, frozen artifact specification, and native publication/readback checks as recorded in the completion receipt.

Not performed: source conversion execution, application execution, dependency installation, compiler/typecheck, lint, unit/integration/runtime tests, fixtures, browser or monitoring operation, upstream modification, or deployed correctness verification. The packet claims the one source correction only, not whole-build success.

The new frozen publication specification is banked with the existing public checkpoint helper before branch publication. It contains this patch and guide; private native journals and upstream full bodies are excluded. The checkpoint manifest's acknowledged immutable locator is reported with the completion receipt. An acknowledged unreferenced blob is not a branch/ref, deployment, or indefinite-retention guarantee. The original immutable donor blob plus this exact patch defines the candidate; no accepted work needs replay for this packet's recovery.
