# Own the notification hook's audio teardown

The mounted notification provider uses `playSound` but never invokes the sound
hook's exported cleanup callback. This continuation makes the hook register its
own teardown and keeps its critical-tone timeouts attached to that same
ownership boundary. It composes over the earlier resume-rejection patch without
replaying or replacing that completed work.

## Source lineage and composition

Upstream repository: `Stellar-Analysis/frontend`.

Observed upstream main and immutable input:
`482ee456369418ef82c4056718cb82d3468f762b`.

Affected path: `src/hooks/useNotificationSound.ts`.

| Source stage | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Original complete upstream hook | `5fc9fe895921224065cfd0f3ea4441d0d824fc9e` | 3,919 |
| Prior Commons #31935 postimage / this patch's preimage | `2dd1c2f3701ed85dfc9195b545a0aab8bc106974` | 4,022 |
| This composed postimage | `1184701859cd6e6e29aa243fb483261b1de0c3bf` | 4,565 |

Apply this patch after the attributed resume-rejection patch from
[Commons #31935](https://github.com/woahwhattheheck/commons/pull/31935),
merge `375f01c0fd5f66db78e9e79cd96e54a9c8fbcbac`, under
`work/bounty-intake/stellar-notification-resume-rejection-20261006-7ca6/`.
That prior patch blob is `589d06f94776f00f7ac576aeecfff157257f9bd5`.
The original upstream hook remains unchanged there; a Commons source packet
does not establish deployment or upstream integration.

The current patch is +18/-5 relative to the prior postimage. The earlier resume
catch is byte-preserved. No caller, notification preference, Test Sound button,
toast component, dependency, or configuration source is changed.

The connected `src/contexts/NotificationContext.tsx` blob
`8a05dbf6fb720af3f876baef6b14f035d02b6c51` was already acquired fully by CI.
Its exact retained source contract is `const { playSound } = useNotificationSound();`.
The complete module contains no cleanup invocation. Its transferred complete
`showToast` function calls `playSound` for enabled sound, then returns the toast
ID synchronously. CI's separate NotificationPreferences Test Sound context
cleanup concerns a different independently created context and file.

The original hook and the prior postimage remain in retained custody. Their
complete identities were established during the distinct resume patch; this
continuation uses those bytes as input and does not replay the original
publication, audio behavior or provider reads. The bounded prior path history
reported christabel888's root relocation commit
`59fad72d9fbef9cfd6f47e215392da44488fcdc4`; it is not a complete authorship census.

## Teardown ordering

The hook owns a Set of its pending critical-tone timer handles. A timer removes
its own handle when invoked, then checks that the hook still owns its captured
AudioContext before constructing the second tone. The original 100 ms delay and
tone construction remain unchanged for a current context.

The stable cleanup callback first clears the pending timers and empties their
Set. It then captures the current AudioContext and sets the owning ref to null
before initiating close. This separates the old context from any subsequent
ordinary play call; a later close settlement cannot clear a newly created
context. A rejected close Promise goes to the existing logger abstraction.
Repeated cleanup sees no old context and no remaining owned timers.

The hook registers `useEffect(() => cleanup, [cleanup])`. The
[React useEffect contract](https://react.dev/reference/react/useEffect)
calls a returned cleanup function when the component is removed. Development
Strict Mode can also run an extra setup/cleanup cycle; the source design does not
create an AudioContext merely by mounting this effect, and leaves ordinary lazy
creation in the existing play path. No Strict Mode execution is claimed.

The [Web Audio close contract](https://webaudio.github.io/web-audio-api/#dom-audiocontext-close)
returns a Promise and can reject. It stops audio processing and releases system
resources, but does not automatically release every AudioContext-created
object. The patch therefore claims an attempted owned-context close with a
handled Promise, not synchronous release of all browser resources.

## Preserved behavior and explicit limits

`playSound` and `cleanup` remain the exported functions with their existing
synchronous calling convention. Explicit cleanup while mounted still permits a
later ordinary play call to lazily create a new context. The effect itself
creates no audio or state update.

The enabled/SSR checks, sound settings and priority selection, volume clamp,
first-tone scheduling, current-context second-tone scheduling, resume rejection
handler from #31935 and outer synchronous warning path remain unchanged.
Cleanup intentionally cancels pending second tones and requests closure of the
context owned at cleanup time.

The identity check prevents a delayed callback from constructing its tone on a
context that this cleanup detached. It does not claim cancellation of a callback
already executing, a browser scheduling guarantee, or a global notification
quiescence mechanism. Externally retained callers invoking playSound after
unmount, unrelated providers, setting changes, callback exceptions unrelated to
detachment, and logger failures remain outside this patch. No permission prompt,
resume retry, browser teardown acknowledgement, timing accuracy or actual audio
success is inferred.

No browser, audio device, AudioContext, timer, application, build, lint, test,
fixture or workflow was executed. Validation is retained complete source/caller
evidence, primary React/Web Audio contracts, exact composed text edits and
ordinary source-publication identity checks. Runtime and device acceptance
remain unperformed.

## Attribution

This packet contains only an attributed patch and this note. Original upstream
contributors retain credit; CI supplied the complete retained caller evidence.
The source itself is not republished in full and no upstream PR, claim,
submission, payment, permission or production action is performed.

The donor's differently attributed MIT notices are already preserved verbatim
under `work/bounty-intake/stellaranalysis-issue-generator-layout-20261006-7ca6/`:

- `upstream-licence-mclaughlin.md`:
  `57740b9d4d86aedf5d518f2f363d5cf192c54127`.
- `upstream-license-menke-laguna.md`:
  `af5411fa243cfcf2b61c79d081dbb6204e956041`.
- `upstream-license-de-wet.md`:
  `4a766e268772888af5df56c3f6c608f68558b789`.

No single notice is assigned a repository-wide scope by this continuation.
