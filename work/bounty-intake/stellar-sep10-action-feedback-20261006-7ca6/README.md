# Show connection and authentication action failures in the SEP-10 demo

The SEP-10 demo passes connectWallet and authenticateWithSep10 directly to its two action buttons. The actual imported wallet context logs failures and rethrows them, while the page only puts authenticated-endpoint test results into its visible result area. A connection or authentication rejection therefore has no page-level path to visible error feedback.

This narrow page continuation awaits each existing action inside a local catch and displays fixed failure copy in the existing Error result. It makes no change to the wallet context, authentication service or protocol.

## Exact public inputs

Canonical repository: Stellar-Analysis/frontend  
Pinned donor: 482ee456369418ef82c4056718cb82d3468f762b

| Source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| src/app/[locale]/sep10-demo/page.tsx | 771aca398f8355d7a4a6550522e016aa71ad1b49 | 10988 |
| src/components/lib/wallet-context.tsx | cb3e12aa4d3b87adc1fd1b67492510abb3361867 | 6586 |
| Proposed demo page postimage | e186e4ed92768b70184d54d33bb1314648968b15 | 11476 |

The page is an actual App Router entry. Its literal import is useWallet from @/components/lib/wallet-context. A native directory read at the pinned commit established the exact context file path and blob before its complete source was acquired. Both full source strings were returned by immutable blob reads and independently matched their Git identities and byte counts. These fetch-blob responses expose content only; the native provenance is the exact requested locator plus independent identity, not an invented returned SHA field.

The context's WalletContextType declares both selected actions as () => Promise<void>. The complete connectWallet implementation catches and logs its failure, then throws it again. authenticateWithSep10 throws when no address exists and rethrows service or storage failures after logging. No action was invoked during qualification.

The page already owns testResult with success/message fields and renders its failure form as Error. The endpoint-testing callback has its own try/catch; it is unrelated to the missing action handlers and stays unchanged.

A bounded path-history read at the donor returned relocation commit 59fad72d9fbef9cfd6f47e215392da44488fcdc4 by christabel888. That is relocation provenance, not sole-authorship evidence. Retained root and CI scope checks supplied no conflicting page writer; bounded custody does not prove repository-wide absence.

## Source change

change.patch is +21/-2 in three hunks:

1. Add handleWalletAction(action, errorMessage). It clears the previous result for this attempt, invokes the supplied action once inside try, awaits its promise and maps a throw or rejection to the existing failure result.
2. Route Connect Wallet through that helper with fixed copy: Failed to connect wallet. Please try again.
3. Route Authenticate with SEP-10 through it with fixed copy: Authentication failed. Please try again.

The helper calls the existing action synchronously before its first await suspends. It does not schedule, retry or replace the wallet operation. It writes no success claim; successful connection/authentication continues to be represented by the existing context status.

The complete authenticated-endpoint callback, request URL/header construction, logout button/handler, token/address presentation, explanatory copy and all styling are byte-exact. The context and service are not edited. Original rejection details are not copied into the new visible error strings.

## Language contract

MDN's JavaScript await reference states that awaiting a rejected promise throws its rejection reason and demonstrates handling it with try/catch. Calling and awaiting the action within the try also catches a synchronous throw from invocation.

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#exceptions  
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#handling_rejected_promises

This contract and the acquired Promise<void> declarations support the local rejection handler. No browser or wallet error was induced to exercise it.

## Limits

This is visible page-level failure handling, not authentication correctness, credential protection or account isolation. The context and service remain responsible for their own state and side effects; a rejected action can already have performed partial work. Nothing is cancelled or rolled back.

The patch adds no single-flight guard, disabled/pending policy, timeout, retry mechanism, logout error handling or request ordering. Repeated clicks and late completions retain their existing lifetime/concurrency limits. Clearing the prior result when starting either selected action is intentional. A failed action shows generic copy rather than its low-level cause.

The literal protected-endpoint route, supported wallet set, storage policy, token lifecycle, SEP-10 implementation and security/benefit statements are not validated by this packet. There is no successful authentication, connectivity, protocol, browser, device or whole-build claim.

## Source checks and packaging

Unique exact replacements produced the new page. Applying and reversing the final narrow patch reconstructs the pinned original and proposed postimage exactly. The two selected button expressions and the added helper are the only changes. Complete public source inputs, native responses, independent identities, history, postimage, patch, guide and spec have explicit private custody keys.

No compiler, lint, tests, fixtures, wallet connection, signature, authentication, token/secret access, endpoint request, account operation or application execution was performed. The Commons packet is source-only, with no upstream-ready acceptance claim.

Retained canonical tree evidence at this donor has 959 entries, truncated:false, no AGENTS/RULES and no backend root; its full old array was lost in the reported volatile-store incident and is not reconstructed here. The recursive response echoed the requested commit; the separately observed branch tree is 44703ba39198f99b6541450c740db0d1c3c0f7b8, without an independent whole-tree claim.

The retained docs/CONTRIBUTING.md f66db3b0eece27eb6fa888948c31ee8c7eabcfd2 is the 274-byte EventSource-specific guide, including its request for tests when adding or fixing something. The authorized source-only lane excludes execution and preserves that upstream acceptance requirement as unperformed.

Earlier source qualification preserved three differently attributed MIT notices: docs/LICENCE.md 57740b9d4d86aedf5d518f2f363d5cf192c54127, docs/LICENSE.md af5411fa243cfcf2b61c79d081dbb6204e956041 and docs/license.md 4a766e268772888af5df56c3f6c608f68558b789. Their scope is not promoted to a repository-wide license. Only this guide and the narrow patch are published.

The complete frozen publication spec, containing only these two public artifacts and publication metadata, is eligible for the existing public checkpoint helper before publication. Full source modules, credential values and private request/raw journals are excluded from that checkpoint. A blob acknowledgement is an immutable recovery locator, not an indefinite retention or branch reachability guarantee.
