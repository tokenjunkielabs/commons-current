# PR131: reopen the circuit after a failed cooldown retry

The current balancer admits a provider once its cooldown expires, but a later failed attempt does not replace its old opening timestamp. That expired timestamp leaves the provider eligible for subsequent requests. The attached patch refreshes the timestamp when a failed outcome reaches the failure threshold and the previous cooldown has expired, while retaining an opening timestamp whose cooldown is still active.

This Commons packet is an attributed correction to liutingqiu's [PR131](https://github.com/mallonepay/pay-per-token-llm-gateway/pull/131). It does not modify the upstream repository or contributor branch, take ownership of issue3, implement the remaining feature requirements, or make a payment claim.

## Current issue, contributor and source contract

- Canonical repository: https://github.com/mallonepay/pay-per-token-llm-gateway
- Issue: https://github.com/mallonepay/pay-per-token-llm-gateway/issues/3
- Issue acceptance: multiple upstream providers for one model; round-robin and least-latency selection; weights; health checking and failover; a failure-triggered circuit breaker; an admin health view; per-provider request and latency analytics.
- At native qualification on 2026-10-06 the issue was OPEN with no native assignee and 32 comments. Several external contributors had expressed interest. The live implementation belongs to liutingqiu.
- PR131 was OPEN, non-draft and unmerged, with 11 changed files, zero PR issue comments and zero inline review comments.
- Exact contributor source: `liutingqiu/pay-per-token-llm-gateway@8e95aeec54c13a869ed1950d2efeacc17c067243`, branch `issue/3-load-balancing`.
- Qualified PR base: `9b259a1be1b4431d270797fcc6707bc08af661a6`.
- The complete contributor-head recursive tree contained 474 entries and returned `truncated:false`. No AGENTS.md was listed. CONTRIBUTING.md and LICENSE were fully acquired.
- CONTRIBUTING.md describes maintainer assignment, upstream review and required test/lint checks. This is a Commons source packet, not a submitted upstream contribution; those upstream checks have not been claimed as completed here.
- LICENSE is MIT, copyright 2025 x402 LLM Gateway Contributors, copied in THIRD_PARTY_NOTICES.md.
- The PR author explicitly omits the admin provider-health view and active health probes, and documents process-local rather than shared balancing state. Those limitations remain.
- A later issue comment asks whether the omitted dashboard could be separately paid. It is a contributor's question, not permission or an award guarantee. No contact, account, payment or transaction action was taken.
- The previously reported exact `tokenjunkielabs/pay-per-token-llm-gateway` fork404 remains held and was not retried or used as a source. All source in this packet came from the identified live contributor head.

The issue label says rewards are contingent on program approval. No cash amount, eligibility, assignment, sponsor response, approval or payment is inferred from the label or issue history. Author-reported test results in the PR are not this packet's verification.

## Observed service behavior and actual consumer

The complete LoadBalancerService contains:
- FAILURES_BEFORE_OPEN=3 and CIRCUIT_COOLDOWN_MS=30000.
- Health state keyed by model and provider.
- isAvailable: an unopened circuit is available; otherwise availability is `now - circuitOpenedAt >= CIRCUIT_COOLDOWN_MS`.
- selectRoute: filters candidates through isAvailable before choosing a weighted or least-latency route.
- record: increments outcome counters; success resets consecutiveFailures and clears circuitOpenedAt; failure increments consecutiveFailures and sets circuitOpenedAt only if it is null.
- status: derives circuitOpen by negating the same isAvailable predicate.

The last condition disagrees with the service's own description that the next failed attempt after cooldown opens the circuit again. After the first cooldown, circuitOpenedAt remains non-null. A failed retry increases the failure count but does not replace that expired timestamp, so isAvailable continues to return true on later selections unless another action changes the state.

This is exercised by an actual source consumer. ProxyController injects LoadBalancerService, obtains candidates from RoutesService, and uses balancer.selectRoute. Its streaming and non-streaming forwarding failure catches call balancer.record with `ok:false`. Its successful paths call record with `ok:true`. ProxyModule imports BalancerModule, which provides and exports the service. No new handler or mounting is invented.

Relevant immutable source:
- [load-balancer.service.ts](https://github.com/liutingqiu/pay-per-token-llm-gateway/blob/8e95aeec54c13a869ed1950d2efeacc17c067243/apps/gateway/src/modules/balancer/load-balancer.service.ts)
- [proxy.controller.ts](https://github.com/liutingqiu/pay-per-token-llm-gateway/blob/8e95aeec54c13a869ed1950d2efeacc17c067243/apps/gateway/src/modules/proxy/proxy.controller.ts)
- [proxy.module.ts](https://github.com/liutingqiu/pay-per-token-llm-gateway/blob/8e95aeec54c13a869ed1950d2efeacc17c067243/apps/gateway/src/modules/proxy/proxy.module.ts)
- [balancer.module.ts](https://github.com/liutingqiu/pay-per-token-llm-gateway/blob/8e95aeec54c13a869ed1950d2efeacc17c067243/apps/gateway/src/modules/balancer/balancer.module.ts)
- [routes.service.ts](https://github.com/liutingqiu/pay-per-token-llm-gateway/blob/8e95aeec54c13a869ed1950d2efeacc17c067243/apps/gateway/src/modules/routes/routes.service.ts)

The controller's request/payment/forwarding code is review context only. This packet does not call an upstream provider, API, ledger, wallet or payment path.

## Exact change

Only the failed-outcome branch of record changes. It captures one current wall-clock value. When consecutiveFailures is at or above the existing threshold, it writes that value if either the circuit has never opened or the stored cooldown has expired. The condition uses the same inclusive cooldown boundary as isAvailable.

| Failed-outcome state | Corrected timestamp behavior |
|---|---|
| Consecutive count below threshold | No opening timestamp is set by this branch |
| Threshold reached and circuitOpenedAt is null | Open using the captured current time |
| Threshold reached and stored cooldown is still active | Keep the original opening timestamp |
| Threshold reached and stored cooldown has expired | Replace the stale timestamp and restart the existing cooldown |

Success handling remains byte-for-byte unchanged. For a still-active cooldown, a late failure from a previously started request does not extend the original window. A failed attempt after the window expires starts a new window. The request count, failure count, threshold, cooldown duration, selectors, weights, latency accumulation, status shape and reset method remain unchanged.

The source reasoning follows the predicates above. No timed scenario, synthetic fixture, load test, Jest run or runtime simulation was created or executed.

## Limits

This is a correction to one existing transition, not a complete half-open concurrency policy. It does not reserve a single recovery probe, prevent concurrent retries after cooldown, attach attempt generations, discard stale success completions, or create distributed state. It continues to use Date.now and inherits wall-clock changes. It does not distinguish additional upstream error categories or change the controller's existing outcome-reporting decisions.

It also leaves request routing, response codes, payment and ledger behavior, provider-health UI, active probes, analytics persistence and all other issue3 requirements unchanged. No runtime health outcome, failover guarantee, complete load-balancing implementation or whole-PR approval is claimed.

## Exact application and text verification

Target `apps/gateway/src/modules/balancer/load-balancer.service.ts` at the contributor head above.

| File state | Git blob | UTF-8 bytes |
|---|---|---:|
| Original | `f0398379eda7e1232d83a1b7d547f9efae21f099` | 8,976 |
| Proposed | `763fe5dba8cce2e37bb551ef3b5b14d1600a5dd1` | 9,061 |

The serialized unified diff has one hunk, +4/-2. Forward and inverse text applications were each checked once against the complete retained source strings. Every other byte remains exact. No compile, lint, test, deployment or donor execution was performed. The author's reported test suite results do not validate this new patch.

A future upstream implementation review should verify the failed post-cooldown transition and preservation of an already-open window under its actual test environment. That is a validation requirement for a later upstream submission, not a result claimed here.

## Complete acquired source identities

All seven full source/document strings independently matched their native/tree Git identities. Complete acquisition is not a claim to have audited every unrelated method in the large proxy controller. Review used the actual selection and recording paths described above.

All paths below are under https://github.com/liutingqiu/pay-per-token-llm-gateway/blob/8e95aeec54c13a869ed1950d2efeacc17c067243/ .

| Path | Git blob | UTF-8 bytes |
|---|---|---:|
| `CONTRIBUTING.md` | `76b1207db2ca146dfb1059bdd7c589c42d42138a` | 13572 |
| `LICENSE` | `6174c9bc692908e5d46c4581570317f4c69617e9` | 1086 |
| `apps/gateway/src/modules/balancer/load-balancer.service.ts` | `f0398379eda7e1232d83a1b7d547f9efae21f099` | 8976 |
| `apps/gateway/src/modules/balancer/balancer.module.ts` | `e0581314787d769766e574b99f951ef6c237f7fe` | 570 |
| `apps/gateway/src/modules/proxy/proxy.controller.ts` | `9eb44c068403dc28393e787202fa9a30c1003273` | 39826 |
| `apps/gateway/src/modules/proxy/proxy.module.ts` | `21b031be492552cc7ed7a03d1e82ab27e5586a3b` | 981 |
| `apps/gateway/src/modules/routes/routes.service.ts` | `bec8cb4d00ecbb4e52d1b5069a746349f17b0a47` | 10029 |

## Contents

- circuit-reopen.patch — the bounded service correction.
- REVIEW.md — original defect, consumer, transition and scope analysis.
- THIRD_PARTY_NOTICES.md — contributor attribution and the exact source license notice.

No full donor source file, private provider journal, payment address or credential is included.
