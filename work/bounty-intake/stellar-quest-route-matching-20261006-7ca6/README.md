# Quest route matching and initial progress rendering

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

## Additive continuation: restore one progress snapshot after hydration

The actual `src/app/[locale]/quests/page.tsx` at native blob `ea55ab2602a0f36d9dd0e8b7f9a744bc647b4dd2` initializes state with getProgress() and separately calls four storage-backed metric getters during render. The helper returns an empty array on the server but reads browser localStorage on the client. Saved progress can therefore alter the initial cards, counts, XP, achievements and leaderboard output before hydration. QuestCard `5e3ceb655d66b9924a40a016cbbacfbf14b6ae48` receives completed from the page and already uses the localized Link; it is unchanged.

The additional patch initializes the page's typed progress state to an empty array. Its existing pathname effect still checks the current path, loads getProgress(), and retains its JSON equality check before updating state. That effect is the existing restoration/update point; no storage write, schema or progress migration is introduced.

The four helpers now accept an optional `progress: QuestProgress[] = getProgress()` argument. The page supplies the same progress array to completed-count, XP, achievements and leaderboard calculations. Nested count/XP/DeFi calculations forward that array even when empty; none falls back to another storage read. No helper mutates the supplied array. The mock leaderboard remains a newly created array sorted with the existing comparator.

No-argument callers retain their API and load persisted progress by default. The page's render avoids those defaults, making its first empty snapshot deterministic and later saved-progress output consistent across cards and metrics. All existing numeric formulas, thresholds, quest definitions, completed-ID handling, mock rows, displayed copy and JSX remain exact. The source change is not a new reward calculation.

The already-read primary [React hydrateRoot contract](https://react.dev/reference/react-dom/client/hydrateRoot) requires matching initial rendered output and describes an effect-driven subsequent render for client-dependent content. The [Next.js Server and Client Components documentation](https://nextjs.org/docs/app/getting-started/server-and-client-components) establishes that client components participate in initial HTML prerendering. These contracts apply to the acquired locale route and its localStorage-dependent source; no hydration run was performed.

Apply `restore-quest-progress-after-hydration.patch` after `match-localized-quest-routes.patch`:

| Changed source | Preimage Git blob / bytes | Postimage Git blob / bytes |
| --- | --- | --- |
| `src/app/[locale]/quests/page.tsx` | `ea55ab2602a0f36d9dd0e8b7f9a744bc647b4dd2` / 8054 | `5b8101b247dc4fc495b54bedfaa2c442c24b9ae4` / 8143 |
| `src/lib/quests.ts` | `be3ef45ab09aa97cd29956df3f22fa36e94c7729` / 6597 | `f6c177ed9768aacfd1cae45e583e24feb866066b` / 6741 |

The additional serialized patch contains four hunks, +15/-15. Each complete forward reconstruction matches its postimage and each inverse matches its preimage. The original route patch is unchanged, and the new helper postimage preserves its corrected route predicate exactly. These are source-text integrity checks, not executed tests or computed quest results.

A bounded exact QuestsPage public search returned zero/native END; the Commons PR query for quests plus hydration returned zero/incomplete_results:false. No global absence or whole-build result is inferred.

The initial empty-progress presentation may briefly precede saved progress after the effect runs. There is no claim of flash-free rendering, malformed-storage validation, cross-tab live synchronization, atomic storage snapshots or whole-page/application hydration success. Metric calculations now deliberately use the page snapshot rather than opportunistically rereading storage on unrelated renders; the existing pathname effect remains the update trigger. Existing correctly or incorrectly saved progress is preserved without removal/re-awarding. No browser, storage/user data, fixture, runtime, compiler, test, navigation, account, chain, payment or upstream operation was performed.
