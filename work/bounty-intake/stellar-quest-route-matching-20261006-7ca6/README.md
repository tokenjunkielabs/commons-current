# Match quest progress to the actual localized route

The locale layout mounts QuestProgressTracker, which passes Next.js usePathname directly into checkPathCompletion. The actual routing configuration always prefixes en, es or zh, while quest definitions contain locale-free paths. The matcher also treats the dashboard's root entry "/" as a prefix of every path. These two source conditions prevent intended localized matches and can attribute an unrelated visit to the dashboard quest.

This patch uses the existing locale-aware pathname hook and restricts each definition to its exact route or a non-root child route with a slash boundary.

## Source and attribution

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend) at `482ee456369418ef82c4056718cb82d3468f762b`. This minimal Commons patch and original guide preserve the original authors, assignments, acceptance and economic rights. There is no upstream submission or whole-quest-feature claim.

| Source | Original Git blob | UTF-8 bytes | Role |
| --- | --- | ---: | --- |
| `src/components/QuestProgressTracker.tsx` | `684ce7fae434b9cd444932e0f8e49fd4133aabff` | 418 | Mounted pathname producer |
| `src/lib/quests.ts` | `1f106e06eb47b551d65fbb39d88427a7edf76117` | 6576 | Definitions and completion matcher |
| `src/i18n/navigation.ts` | `fd8ba9aa80bb0d0dd56eb76a3891caa0afe0c803` | 182 | Existing createNavigation exports |
| `src/i18n/routing.ts` | `7a1c19fa17133fa33179f3381d115f8d2ee542f7` | 175 | en/es/zh, default en, always-prefixed routing |
| `src/app/[locale]/layout.tsx` | `1f016787657313d58504e79bccbe634a843ce8b5` | 4212 | Directly renders the tracker |

Complete source strings were acquired or transferred from retained native custody and independently matched their stated Git blob identities. The navigation and routing transfers matched their exact 182 and 175 byte counts respectively. No missing module was reconstructed from an abbreviated description.

## Actual contract and correction

QuestProgressTracker runs checkPathCompletion in its effect when pathname changes. The helper iterates the existing QUESTS list, skips already completed IDs, compares each pathMatch, records the first match and breaks. Definitions include /corridors, /anchors, /analytics and other exact paths; the dashboard has both /dashboard and /. The current source tree also contains actual corridor [pair] and anchor [address] child routes.

The first changed line imports usePathname from the existing `@/i18n/navigation` module. That module exports the hook from createNavigation(routing). Its actual configuration has no pathnames map. The primary [next-intl Navigation APIs documentation](https://next-intl.dev/docs/routing/navigation#usepathname) specifies that this hook returns the current pathname without a locale prefix. This avoids manually stripping or assuming a language code in the tracker.

The second changed line matches `pathname === p`, or a child beginning with `p + "/"` when p is not /. Thus the root definition remains an exact root match, and a route-name prefix without a segment boundary cannot complete another route's quest. Child paths remain eligible. These conclusions follow from the literal predicates and acquired route definitions; no sample navigation, classifier or synthetic case was executed.

Quest order, already-completed handling, one-completion-per-navigation break, storage key/read/write implementation, timestamps, IDs, XP values, achievements and the mock leaderboard remain byte-for-byte unchanged. The patch neither awards external value nor establishes payment, reward eligibility or server authority. It does not navigate or perform a storage operation.

## Source integrity and composition

Apply `match-localized-quest-routes.patch` to the donor commit:

| Changed file | Postimage Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/components/QuestProgressTracker.tsx` | `681df2ce330149dd01d39f7c02a3b31de958131b` | 420 |
| `src/lib/quests.ts` | `be3ef45ab09aa97cd29956df3f22fa36e94c7729` | 6597 |

The complete serialized two-hunk patch is +2/-2. Each forward reconstruction equals its complete postimage; each inverse reconstructs its complete original source. These are text-integrity operations, not runtime tests. Exact public QuestProgressTracker history returned zero/native END; the bounded Commons PR query returned zero/incomplete_results:false. Those checks do not prove global absence.

Existing locale forwarding, notification, heatmap, theme, PWA and shortcut packets touch other source paths and remain protected. This packet does not broaden or revalidate them.

The full donor tree exposed no AGENTS/RULES path. Retained EventSource-specific docs/CONTRIBUTING.md `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` does not alter the current no-tests/no-runtime/no-package-publication boundary. Differently attributed MIT notices under docs do not establish repository-wide licensing; complete modules are not republished.

## Limits

This is a forward routing correction. Existing incorrectly recorded progress is not removed, migrated or re-awarded. The localStorage schema/availability/concurrency behavior and the source's explicit mock leaderboard remain unchanged. Repeated locale-only navigation now resolves to the same locale-free pathname; the tracker continues to react to that pathname, not to a separate locale preference. No new locale/path mapping, trailing-slash normalization or query-string policy is introduced.

No compiler, tests, fixtures, browser, navigation, storage access, quest completion, wallet/account/chain/payment action, upstream submission or full-feature acceptance was performed.
