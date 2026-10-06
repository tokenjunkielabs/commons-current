# Remove the root viewport's explicit zoom restriction

The application root layout exports userScalable:false alongside its device-width and initial-scale settings. That asks browsers honoring this viewport directive to disable user scaling. This patch removes only that restriction, leaving the initial presentation and all other source behavior unchanged.

## Source and attribution

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at `482ee456369418ef82c4056718cb82d3468f762b`. A fresh native donor main-ref guard returned the same commit. The complete retained `src/app/layout.tsx` source is `d99613766c48f2be30014720edd01dc156d58696`, 1,968 UTF-8 bytes. Its default RootLayout renders the document html/body around the route children, and its exported typed viewport object is the actual framework consumer.

This minimal Commons patch and original guide preserve the original authors, assignments, acceptance and economic rights. No upstream branch, issue, author, award or payment is changed or claimed. There is no inferred repository-wide license from differently attributed notices under docs, and no complete donor module is republished.

## Contract and correction

The official [Next.js viewport reference](https://nextjs.org/docs/app/api-reference/functions/generate-viewport#width-initialscale-maximumscale-and-userscalable) documents the exported viewport object and maps userScalable:false to the user-scalable=no metadata directive. The source correction deletes that property instead of imposing a replacement maximum or minimum scale. The retained source does not declare maximumScale or minimumScale.

The [W3C ACT viewport zoom rule](https://www.w3.org/WAI/standards-guidelines/act/rules/b4f0c3/) explains that viewport metadata should preserve scaling. It also explicitly qualifies browser support: desktop and many modern mobile browsers ignore or override this restriction. Other text-resizing mechanisms can affect conformance conclusions. Accordingly, this packet claims removal of this root source restriction, not a demonstrated behavior change on every device or a WCAG result.

Apply `remove-root-zoom-restriction.patch` to the stated donor source:

| Source | Before blob | After blob | After bytes |
| --- | --- | --- | ---: |
| `src/app/layout.tsx` | `d99613766c48f2be30014720edd01dc156d58696` | `7db05b69f833bf8b994b9cbcc396377855281436` | 1945 |

The single hunk is +0/-1. Device width, initialScale:1, themeColor, metadata, font loading, root language/class values, hydration attributes and every JSX byte remain unchanged. No CSS, text-size preference, locale layout, route, gesture listener or browser setting is changed. Previously completed theme/text-size/layout packets touch other hunks and remain protected.

The complete serialized patch reconstructs the full postimage exactly and reverses to the full preimage. These are text-integrity checks, not application tests. Public exact userScalable history returned zero/native END; the bounded Commons Stellar/zoom PR query returned zero/incomplete_results:false. Neither establishes global absence of other work.

The retained complete donor tree contains no AGENTS/RULES path. Its EventSource-specific docs/CONTRIBUTING.md `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` does not override this session's explicit no-tests/no-runtime/no-package-publication scope.

## Limits

No compiled viewport tag, route-specific override, responsive reflow, focus behavior, browser gesture, screen reader, operating-system scaling or device compatibility was exercised. This changes the root declaration; it does not claim a census of every route's possible metadata or full application resize conformance. No runtime, build, test, fixture, browser/device, user data, account/payment or upstream action was performed.
