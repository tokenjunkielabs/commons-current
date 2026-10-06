# Limit Soroban panel state writes to the current load

## Actual source finding

SorobanPage starts its load function from the mount effect and from the rendered Refresh button. Each invocation awaits one Promise.all over five fixed panel requests, then writes five response states. Its catch writes five failure fallbacks, and its finally clears both loading and refreshing.

The original mount effect returns no cleanup. None of those asynchronous state-write groups checks whether its invocation is still current. A completion from an effect that has been cleaned up therefore still attempts all corresponding writes. If two loads overlap, an older completion can also overwrite a newer invocation's data or clear its loading indicators. These are source-level control-flow possibilities, not a claim that a deployed stale-response incident was reproduced.

The Refresh button is already disabled while loading or refreshing, and this patch preserves that condition. Ordinary rendered button availability reduces overlapping user requests; it does not give the asynchronous continuation an effect-lifetime or ownership check. The source has no selectable request parameter; this change does not invent a time-range or account-switch race.

## Narrow correction

A component-local ref holds the current load's unique object. Each actual load installs a fresh owner object before beginning the unchanged loading-state setup and five requests.

After Promise.all resolves, the invocation checks that it still owns the ref before writing any panel state. The catch retains the original logger call and then makes the same ownership check before changing the fallback states. The finally clears loading and refreshing only while the invocation still owns the ref. The mount effect's cleanup clears the ref, invalidating every outstanding invocation from that component lifetime.

An older completion cannot acquire ownership merely by finishing later; only a new load start installs an owner. Object identity avoids a numeric generation counter or wraparound policy. The owner is bookkeeping only, contains no response data and is not rendered.

The original error logging still occurs for a rejected stale load. This preserves that observability behavior while preventing the stale catch from replacing current panels. The finally uses a guarded block, not a return that could replace an error or return value.

## Preserved behavior and limitations

All five API calls, their order and parameters, Promise.all behavior, response assignments, fallback values and request helpers remain exact. The two synchronous loading starts are unchanged. The complete returned JSX suffix is byte-for-byte identical, including the Refresh button, its disabled state, all panel props and the previous availability/notices work.

This does not abort, deduplicate, cancel or retry any request. Superseded requests and their helper-side logging can still run and settle; only this page's later state writes are gated. One current rejected Promise.all still follows the original all-panel fallback policy. The helper functions' existing distinctions between resolved failure fallbacks and thrown rejections remain unchanged.

The ref is cleared during effect cleanup, not by adding a route listener, timer, global registry or dependency. The existing effect dependency policy and suppression comment remain unchanged. This is not a caching migration, API redesign, concurrency limit, backend coverage fix or full hook-lint cleanup.

The [React useEffect reference](https://react.dev/reference/react/useEffect) documents cleanup on removal and before a subsequent setup, and illustrates ignoring stale fetch results. It also describes an extra setup/cleanup cycle in development when Strict Mode is enabled. Those contracts support the ownership boundary above; this packet does not assert that Strict Mode is enabled in a particular deployed configuration or that a development cycle was executed here.

## Exact retained input and output

The immediate input is the complete retained Soroban page postimage from [#32134](https://github.com/woahwhattheheck/commons/pull/32134), including the earlier [#32125](https://github.com/woahwhattheheck/commons/pull/32125) and [#32129](https://github.com/woahwhattheheck/commons/pull/32129) page changes. It was not reconstructed from a patch, summary or lost source.

| Source path | Preimage | UTF-8 bytes | Proposed postimage | UTF-8 bytes |
| --- | --- | ---: | --- | ---: |
| src/app/[locale]/soroban/page.tsx | 80ba478b5aa34d8af463ea4a5c6f969eeca114fa | 6254 | 4719b2c3b6ed7bddc8f3c1c282b601e622f58c68 | 6569 |

The complete retained current API source is src/lib/soroban-api.ts, a3ba6bc1f13ec89d31191d18550e8bb0b584b407 / 9226 UTF-8 bytes. It establishes the actual five Promise-returning helpers; it is evidence only and unchanged.

The canonical donor remains [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at 482ee456369418ef82c4056718cb82d3468f762b in the fresh main metadata read. No donor source body was reacquired for this task. The earlier refined checkpoint 63518084a46841ab670add0aa3f5d34ad99975c6 points to predecessor 0a7e7e4150015e6498ab6545ff53f4f6e7513452, which retains the page/API inputs. Its superseded initial deployment-list draft is not used.

The new patch identity is 25ab778356d455cfff3ab252ddd6c64f69d9c758, 2022 UTF-8 bytes: +13/-3 across five hunks and fifty-two rows. Apply it to the stated #32134 page postimage. [APPLICATION_ORDER.md](APPLICATION_ORDER.md) places this change after that page state and records the final eight-file chain alongside the other Soroban packets.

## Qualification, attribution and unissued preparation

A dedicated native Commons PR search for Soroban and lifetime returned total_count 0, incomplete_results false and no items. That bounded result is not global proof of uniqueness or an exclusive ownership claim. Another existing seat had no exact SorobanPage lifetime correction or hold in its retained completion map; its prior request-ownership changes were on other routes. No accepted patch was replayed to check overlap.

This packet adds guard-soroban-load-lifetime.patch, this guide and APPLICATION_ORDER.md beside the unchanged fifteen earlier artifacts. All three original MIT notices remain unchanged and retain their attribution. No upstream license is replaced or expanded.

Before this new source finding was selected, a documentation-only six-packet application-order draft was frozen and acknowledged at checkpoint 35daebd74fd9be1005bd0f8de13d44ee0c3103ff, with spec aff2da84c67eefc441af22b633eb817c3946f3d5. No advisory or branch publication was dispatched for that draft. It is superseded by this combined source-and-documentation packet; its original spec must not be published as if it were current.

## Verification and publication boundary

Each selected replacement anchor was unique in the complete input, and the exact inverse restored the input. The newly serialized unified diff was parsed for file headers, hunk coordinates, context and row counts. Applying that new text patch to the actual complete preimage reproduced the intended postimage; inverse application restored the full preimage. Every other source byte, including the entire rendered JSX suffix, remained exact.

These were text checks of the new candidate. No load function, ownership comparison, React renderer, compiler, test, fixture, browser, workflow, endpoint or donor runtime was executed. Preparing the accompanying order guide compares prior recorded identities and artifact names; it does not rerun earlier accepted patches. No upstream submission, deployment, account, contract, bounty claim or payment action occurred. Commons publication makes the candidate reviewable and does not establish runtime, build, upstream-acceptance or payment success.
