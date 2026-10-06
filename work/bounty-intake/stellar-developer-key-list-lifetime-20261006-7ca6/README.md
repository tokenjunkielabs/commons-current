# Developer key-list request lifetime

The existing developer keys route can start a list request when the wallet-dependent effect runs and again after its existing create, rotate or revoke callback completes. Every old list completion currently updates keys, error and loading without checking whether another list request or effect lifetime has superseded it. This source continuation gives those list-state writes explicit ownership.

Only the public source patch and this guide are published. No wallet, key, account, API endpoint, browser or application was operated.

## Source and actual caller

Repository: Stellar-Analysis/frontend  
Pinned donor: 482ee456369418ef82c4056718cb82d3468f762b

| Input | Git blob | UTF-8 bytes | Acquisition |
| --- | --- | ---: | --- |
| src/app/[locale]/developer/keys/page.tsx | 3e8ff66a20cd4224a6db7c9c3485263f93b9d811 | 10091 | Complete native immutable blob response; request-bound locator plus independent Git blob hash |
| src/lib/api-keys.ts | 53e3f5f842ac58cbacceddd8b594807a249ea69e | 2357 | Complete native file response at the pinned donor; returned and independent blob identities matched |
| Proposed page postimage | f705854fdb95ebf8a965a5400ba01b2ed3013d7f | 10614 | Derived from the complete pinned page; private source custody |

The page is an actual App Router route. It obtains isConnected and address from useWallet, calls the imported listApiKeys(address) in fetchKeys, and starts fetchKeys from the effect with dependencies isConnected, address and fetchKeys. The existing mutation handlers also await fetchKeys after their own action.

The acquired adapter implements listApiKeys as a GET through fetchWithWallet and returns parsed response data. It has no shared request identity, cancellation or component-lifetime mechanism. Its source was inspected, not invoked. Type declarations identify the returned keys array but do not establish runtime validation or backend authorization.

A bounded path-history read at the exact donor returned relocation commit 59fad72d9fbef9cfd6f47e215392da44488fcdc4 by christabel888. The relocation records provenance and does not establish sole authorship. Retained same-path custody checks from root and CI found no exact completion or hold; that limited knowledge is not a global absence claim.

## Change

change.patch changes only the page: +21/-5 in two hunks.

- Add one useRef containing the active effect's address and latest list-request token.
- Establish a fresh scope before the connected-address effect starts its list request.
- Admit fetchKeys only when an active scope exists and its address matches the callback's captured address.
- Give each admitted list its own object token. Success, error and finally writes require both the same active scope and the same latest request token.
- Invalidate the scope during effect cleanup.

The complete source from handleCreate through the end of the file is byte-identical. All create, rotate and revoke implementations, actionLoading writes, modal/reveal behavior, labels, controls, table rows, disconnected rendering, API arguments and error strings remain unchanged. The adapter is not edited.

This prevents a superseded list's completion from replacing the newer list's state and prevents a cleaned-up effect's pending list from writing later. It does not cancel requests, deduplicate network traffic, retry, or change backend behavior.

## Primary contract

React's official useEffect reference states that cleanup for changed dependencies runs before the new setup and that cleanup also runs when the component is removed. Its data-fetching example ignores responses after cleanup because response order can differ from request order.

https://react.dev/reference/react/useEffect#parameters  
https://react.dev/reference/react/useEffect#fetching-data-with-effects

That lifecycle contract supports invalidating the captured scope. The per-request identity additionally handles multiple list requests admitted within one active effect. This is source reasoning, not an observed runtime sequence.

## Limits

The guarantee begins when the relevant effect cleanup or newer list admission occurs. There is no claim about a render or paint before passive-effect cleanup, a cache, a server transaction, or response-schema correctness.

Previously displayed keys are not proactively cleared by this patch. A later list failure may leave existing displayed data with the existing error state. The empty-state policy remains unchanged.

The create, rotate and revoke handlers can still complete their own modal/error/actionLoading writes; their lifetimes are outside this patch. A delayed handler whose captured address differs from the active list scope cannot start that old-address list. A later callback for the same address can request a fresh list in the current lifetime. This is not a complete cross-account isolation, credential lifecycle or security remediation claim.

No request is aborted, and an already-issued key operation is neither cancelled nor rolled back. No backend, wallet or authentication guarantee follows from these local guards.

## Validation and packaging

Complete input strings were acquired and independently pinned. The source was changed with unique exact anchors. Source-text reconstruction matches the original and proposed files, and the action/render suffix is exact. These are inspection and text-identity checks only.

No compiler, lint, test, fixture, browser, network API request, key generation, rotation, revocation, wallet connection or application execution was performed. No whole-build or device acceptance claim is made. Upstream integration and runtime behavior remain unverified.

Retained canonical tree evidence at this donor was 959 entries with truncated:false, no AGENTS/RULES and no backend root. The complete array is not re-created here. Its recursive response echoed the requested commit; a separately observed branch tree was 44703ba39198f99b6541450c740db0d1c3c0f7b8. No independent whole-tree reconstruction is claimed.

The retained docs/CONTRIBUTING.md is the EventSource-specific 274-byte file f66db3b0eece27eb6fa888948c31ee8c7eabcfd2, including its instruction to add tests when adding or fixing something. This Commons source-only lane explicitly excludes test/runtime execution and publishes no upstream-ready acceptance claim.

Three differently attributed MIT notices are retained from earlier canonical qualification: docs/LICENCE.md 57740b9d4d86aedf5d518f2f363d5cf192c54127, docs/LICENSE.md af5411fa243cfcf2b61c79d081dbb6204e956041, and docs/license.md 4a766e268772888af5df56c3f6c608f68558b789. They do not establish repository-wide licensing scope. Packaging is a narrow patch plus guide, not full-module republication.

## Continuity

A private source custody directory was created before acquisition. It explicitly names the request, native response, complete source, independent identity, adapter, history, postimage, patch, guide and publication-spec records. The full source and postimage remain private working records. This packet contains no private tool journal, Slack/mail body, account value or credential material, and does not re-bank an accepted packet.
