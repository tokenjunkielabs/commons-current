# Keep refresh countdowns within their effect lifetime

The mounted dashboard uses `useDataRefresh` with a 30-second interval and an asynchronous dashboard request. In the acquired hook, the automatic timeout awaits that request and then calls its captured `startCountdown`. The manual refresh path also restarts the countdown after awaiting its callback.

Effect cleanup clears the timer handles that exist at cleanup. It does not stop an already-running async callback. A pending continuation can therefore create new timers after cleanup. When dependencies changed and a replacement effect already started, the old continuation also calls `clearTimers` against the shared refs before scheduling timers with its old interval/callback closure.

This patch gives each bootstrap-effect setup a fresh private object token. Cleanup invalidates the token and clears the current handles. `startCountdown` rejects a null or superseded token before clearing or creating any timer. Automatic recursion carries its original token; manual refresh captures the current token before awaiting and passes that same token afterward.

## Exact source and caller

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).

Donor: `482ee456369418ef82c4056718cb82d3468f762b`.

| Source | Git blob | UTF-8 bytes | Custody |
| --- | --- | ---: | --- |
| `src/hooks/useDataRefresh.ts`, preimage | `4cb937ecb129bf4bf88893721b8d15a5bbc3e3b0` | 4,565 | CI's complete retained native source, transferred and independently hashed here |
| Same hook, postimage | `52554fe4d086aba9539050eb9553f46722d76329` | 4,904 | Exact bounded source transformation, +14/-6 |
| `src/app/[locale]/dashboard/page.tsx` | `cca99335ba0ae1f66a1fb5cea0197f5ead6b2f11` | 13,126 | CI's retained full mounted client route; exact callback/hook/indicator excerpts transferred |

The hook transfer includes the final LF and independently matches the supplying seat's complete 4,565-byte pin. No second provider acquisition of the hook was made in this lane. The caller's full module was not transferred or independently rehashed here; its exact relevant source excerpts and full-module identity are attributed to CI.

The actual caller's `fetchDashboard` awaits `fetch("/api/dashboard")`, rejects a non-OK response, awaits JSON, and sets dashboard data. It passes that callback as `onRefresh` with `refreshIntervalMs: 30_000`. The route passes `triggerRefresh` to the mounted DataRefreshIndicator along with the hook's timestamp, countdown and busy state. Hook setup occurs before the route's loading/error returns. This establishes both automatic and manual production consumers without invoking either.

The bounded current-path history at the donor returned only `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888, for repository-root relocation. It does not establish sole authorship or complete pre-relocation history. Its build claims were not rerun.

## Lifecycle reasoning

The already-read primary [React useEffect contract](https://react.dev/reference/react/useEffect) describes cleanup with the old values before setup after changed dependencies, and cleanup on unmount. It also describes the development setup/cleanup/setup cycle. The patch uses that effect lifetime as the token boundary.

The token is a fresh local object per setup, stored only in a private ref. Identity comparison does not depend on a clock, counter wraparound, callback result, or provider state. Once cleanup invalidates token A, a continuation carrying A cannot become valid merely because setup B has begun: B has a different token. The guard is before `clearTimers`, so an old continuation cannot clear B's handles through this restart path. It also returns before resetting the countdown state or creating interval/timeout handles.

During an unchanged effect lifetime, the same token remains valid and the existing countdown behavior proceeds. The recursive automatic callback carries the token passed when its countdown was scheduled. The manual callback captures the token before its await, so later completion cannot silently adopt a replacement effect's token.

These are control-flow conclusions from the actual source and documented cleanup boundary, not measured timer behavior or a claim that a specific delayed request occurred in production.

## Deliberate limits

Only timer-restart ownership changes. The public options/return interfaces, interval arithmetic, elapsed-second bookkeeping, clearTimers implementation, fetch callback, refresh-on-mount effect, markUpdated, logger calls, loading/timestamp state writes, catch/finally behavior, and dependencies remain unchanged except for the explicit restart arguments and bootstrap cleanup wrapper.

Pending refresh work is not cancelled or aborted. The supplied callback may still have its own data writes after cleanup; this hook patch does not suppress or roll them back. Existing post-await lastUpdated/isRefreshing writes are not newly guarded. Simultaneous refresh attempts inside one active effect, the existing isRefreshing closure guard, mount-refresh behavior, retry policy, timestamps, transport errors, and data freshness semantics remain separate. No latest-attempt, request-order, network, resource-count, performance, or whole-application guarantee is claimed.

CI's dashboard-only successful-refresh error clearing is a separate page hunk. The earlier corridor listing effect guard, corridor WebSocket work, and chart point-count labels are different sources and are not replayed or composed into this hook. No exact same-hook completion was established in the retained coordination; that is bounded custody, not a global absence claim.

## Validation and packaging

The complete transferred hook, actual mounted caller excerpts, current-path history, and retained primary cleanup contract were inspected. Exact replacement reversal restores the complete preimage, and unified-hunk reconstruction binds both the preimage and postimage. Git blob identities and UTF-8 sizes bind the source, patch and guide. These operations manipulate source text only.

No hook, callback, request, timer, dashboard, component, browser, compiler, typecheck, lint, test, fixture, workflow, build, or executor was invoked. No runtime, visual, accessibility, backend, upstream acceptance, or timing claim is made.

The deliverable is a narrow patch plus this guide. No repository-wide license scope is inferred from the differently attributed retained notices, and the complete hook is not republished. Existing notices remain in [the earlier generator packet](../stellaranalysis-issue-generator-layout-20261006-7ca6/). CI supplied the exact hook and mounted-caller evidence. No upstream submission, account, credential, payment or claim action is included.
