# Reset the wallet view for each resolved address

## What changes

The existing address page owns fetched data, loading, validation errors and an empty-state flag in one component. That component resolves its address from the route parameters. Its request callback changes with the address, but its local state has no corresponding reset: validation and empty flags can remain set, and an older pending request retains setters for the same component instance if that instance is reused.

This patch establishes an explicit local-state boundary. A small module-scope wrapper resolves the address and renders `WalletAddressContent key={address} address={address}`. The address-specific component owns the existing state, request callback and effect. When a different resolved address commits, React creates a different keyed subtree with its own initial local state. Old callbacks retain the old instance's setters.

Two related text corrections explain the actual data contract:

- A paragraph below the address header discloses that API failures can return generated samples and that panels may mix API responses with samples.
- The empty-state text describes the three empty collections actually checked. It no longer claims that the account is known to exist on the network.

The one-file patch has +12/-5 lines, four hunks and 48 diff rows. The entire existing local-state hook, request callback and effect block is byte-for-byte unchanged. The lookup page, analytics helpers, request parameters, validation function, chart props, clipboard handler, shared wallet context and outer Suspense boundary are unchanged.

## Why the copy needs correction

The page calls five existing helpers in one `Promise.all`: portfolio, allocation, activity, transfers and balance history. Each helper independently catches its own fetch/non-OK failure and returns a generated fallback. Thus one dashboard can combine API responses and sample values. None of these helper return contracts supplies panel-level provenance.

The helpers return `response.json()` without awaiting it inside their local `try`. A later JSON parsing rejection can escape that catch and reach the page error path. The disclosure therefore says failures **can** return samples; it does not claim every failure falls back.

The retained generators produce synthetic portfolio values, three asset allocations, activity entries, transfers and balance-history points. No generator was invoked and no sample counterparty literal is reproduced in this packet.

The empty-state branch checks only balance history, allocation and transfer arrays. It does not prove network account existence and does not inspect portfolio or activity for emptiness. The new heading, “No History or Transfers,” and paragraph follow those observed conditions. A populated dashboard similarly cannot establish that the displayed holdings or transactions belong to the requested address.

This is a disclosure, not data authentication. It neither removes the sample fallback nor marks individual panels as live or synthetic.

## State behavior and limits

| Situation | Source-level consequence |
| --- | --- |
| A different resolved address commits | A new keyed address subtree initializes its own local state |
| A request from the discarded instance completes | Its closure still holds that discarded instance's state setters |
| Two requests for the same mounted address overlap | Existing ordering behavior remains; no request token was added |
| Route parameters remain pending under Suspense | Existing Suspense and transition behavior remains |
| Shared wallet context or external state changes | The new key does not reset or audit that state |
| Existing request remains in flight after unmount | It is not cancelled by this patch |

The claim is about explicit component identity. No observation of deployed Next.js route reuse is implied. Reset occurs when the newly resolved address subtree commits; this is not a guarantee about the display during a pending transition.

React's [Preserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state) documents that different keys create different component identities and reset state within their subtrees. The component definitions stay at module scope, and the address is passed explicitly because React's key is not an ordinary component prop. The successfully acquired documentation currently identifies React 19.3; the retained package and lock declare React/React DOM 19.2.7 and Next.js 16.2.10. This is a general documented identity contract, not a runtime check against an installed version.

## Exact source and attribution

Canonical repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).
Immutable donor: `482ee456369418ef82c4056718cb82d3468f762b`.
The latest acquired main metadata still pointed to that commit at 2026-10-06 14:45:55 UTC.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| [Address page](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/app/%5Blocale%5D/wallet/%5Baddress%5D/page.tsx) | `2311cc3eb7c9f074ad3b17581583411c232ecc29` | 18902 |
| [Lookup page](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/app/%5Blocale%5D/wallet/page.tsx) | `8c0fc9fa948c954f3650fff793d1244195d219be` | 3452 |
| [Analytics helpers](https://github.com/Stellar-Analysis/frontend/blob/482ee456369418ef82c4056718cb82d3468f762b/src/lib/analytics-api.ts) | `d3daf672cc780815418e3c7518ab4d2334c21796` | 23025 |

The two pages were completely acquired at the donor and matched native and independently computed Git blob identities. The complete analytics module was already retained at that same donor; this packet used those exact existing bytes without reacquisition.

Address-page postimage: `2d040a191b2e4f2284ec00af96f5d19bcff10300`, 19342 bytes.
Serialized patch: `4d0963759ff05b8f41d53156715c50eb357b00aa`, 2729 bytes.

The bounded native path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, authored by **christabel888**. Selected wallet carriers were also inspected as metadata: PR277, PR278 and PR279 by **ndii-dev**, and PR211 by **benedict-cmd**, were closed and merged. Their bodies and old source revisions were not expanded or used as this patch's input. These observations credit existing work; they do not assert that the selected history exhausts authorship.

The retained canonical-base instruction summary reported 959 entries, not truncated, with no AGENTS/RULES paths. Its complete array locator is no longer available, so that historical summary is not presented as a new full-tree acquisition or independently reconstructed tree identity. Retained CONTRIBUTING metadata is `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2`, 274 bytes, summarized as an EventSource test/npm release guide; its full native body is not in this packet's custody. No such process was run.

Three original MIT notices are preserved byte-for-byte, including line endings and separate attributions. They are not a repository-wide licensing determination.

| Included notice | Original path | Git blob | Bytes |
| --- | --- | --- | ---: |
| upstream-licence-mclaughlin.md | docs/LICENCE.md | `57740b9d4d86aedf5d518f2f363d5cf192c54127` | 1104 |
| upstream-license-menke-laguna.md | docs/LICENSE.md | `af5411fa243cfcf2b61c79d081dbb6204e956041` | 1111 |
| upstream-license-de-wet.md | docs/license.md | `4a766e268772888af5df56c3f6c608f68558b789` | 1080 |

## Verification and publication boundary

The newly serialized unified diff was parsed for exact file headers, hunk coordinates, context lines and counts. Forward application reproduced the full intended postimage; inverse application reproduced the original. Reversing the six chosen replacements also reproduced the original exactly, and the existing state/request/effect block matched byte-for-byte. These are text checks, not executed application tests.

A second seat reviewed the transferred wrapper and caller structure without additional provider calls or execution. It confirmed the separate local-state identity reasoning and the limits concerning cancellation, same-address ordering, external context and pending Suspense. Root reviewed the disclosure directly against the complete page and retained helper implementations. No child-component rendering audit is claimed.

A dedicated Commons search for wallet/address/state returned zero PRs. A public Slack search for WalletPageContent and address returned zero results and native end. The upstream wallet/dashboard search returned ten carrier titles; four selected existing carriers received metadata qualification. This is bounded overlap coverage, not proof of global uniqueness.

No compiler, tests, browser, wallet lookup, generator, clipboard action, transaction, service, workflow or upstream mutation was run. Commons publication supplies an attributed source proposal. It does not establish upstream acceptance, a deployed correction, verified account data, completed bounty or payment entitlement.
