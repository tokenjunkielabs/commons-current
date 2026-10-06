# Show the health dashboard's recorded fetch error

HealthDashboard already records an error when its initial anchor request fails, but it never renders that state. Its finally block clears loading, so a rejected request currently falls through to zero-valued summary cards and an empty anchor area. That makes unavailable data look like a successful empty result.

This patch renders the existing error immediately after the existing loading branch, before summary calculations and cards. It adds no request, retry or data policy.

## Actual complete mounted source

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), immutable commit `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/health/page.tsx` | `5bd72d0758c6b99e19c74f79c725dc052ff60f18` | 140 |
| `src/components/health/health-dashboard.tsx` | `d77d90f443f2571f4cbe077bcec82c0bd8a572b0` | 15,761 |
| `src/lib/api/api.ts` | `1af4d71a9127deb5186f016718483dbab088f414` | 7,998 |

The App Router health page directly imports and renders HealthDashboard. The component's mount effect awaits getAnchors(), assigns response.anchors on fulfillment, records the fixed message “Failed to fetch anchor data.” in catch, and clears loading in finally. There is no other setter or render consumer for error in the donor body.

The actual getAnchors builds /anchors with any supplied limit/offset and returns api.get. Its complete fetch wrapper throws ApiError for a non-OK response, awaits JSON for a successful response, and rethrows or wraps caught failures. This getAnchors path has no mock fallback. The unrelated prediction helper in the same module has its own fallback and is untouched.

No request was made to that endpoint. These statements describe the acquired source control flow.

## Nine-line render guard

`render-health-fetch-error.patch` changes **+9/-0 in one hunk**. After the unchanged loading return, a non-null error returns:

* A container with the standard alert role.
* “Health data unavailable” as a heading.
* The existing fixed error message.

Complete source identity:
`d77d90f443f2571f4cbe077bcec82c0bd8a572b0` (15,761 B)
→ `ac0cf6b0eba62f23e86244b758a4b5166b1eec30` (16,060 B).

Loading retains precedence. A successfully fulfilled empty anchors array still reaches the original empty summary/card behavior because no error is set. Every existing source byte remains exact outside the insertion: effect, endpoint, logging, setter ordering, thresholds, state, summary calculations, charts, generators, controls and successful rendering all stay unchanged.

The new view does not add retry, clear errors on later attempts, cancel the fetch, guard unmounts, validate response shape, distinguish failure categories or modify malformed-data handling. It does not prove that an accessible alert is announced in any particular browser or assistive technology. The component's existing English-only copy remains English.

## Validation and unselected boundaries

The complete serialized patch reconstructs the entire postimage; its inverse reconstructs the entire preimage. Independent UTF-8 byte counts and Git blob identities match. No fixture, synthetic rejection, application, API, browser, timer, storage, generator or test was executed.

The separate existing simulated health-history/incident generators, literal trend, settings behavior and success-versus-uptime terminology remain outside this correction. This error view does not certify any health metric, incident or monitoring behavior. Root's completed graph work and the prior dashboard/contact packets are different source paths.

## Attribution and authority

Bounded current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`; earlier contributors retain their rights and no sole-author claim is inferred. Scoped Commons PR and public Slack queries for HealthDashboard/error returned zero, with the Commons incomplete_results flag false. This is bounded overlap evidence, not a global absence claim.

The complete donor tree had no root AGENTS/RULES path. EventSource-specific contribution/release guidance does not override the explicit no-tests/no-runtime/no-upstream scope. Differently attributed documentation MIT notices do not establish whole-frontend licensing; only a minimal patch and this original attributed guide are published.

No upstream branch, PR, comment, maintainer assignment, sponsor acceptance, bounty/payment or whole-issue completion is performed or claimed.
