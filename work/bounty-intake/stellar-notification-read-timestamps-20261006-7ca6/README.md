# Record notification read transitions for the existing metric

The mounted Notification Center displays an average response-time metric, but its actual read actions never supply the read timestamps that the calculation requires. This continuation connects those actions to the existing metadata contract and preserves a valid zero in the display.

## Source and authorship

Donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), immutable commit `482ee456369418ef82c4056718cb82d3468f762b`. This minimal patch and original guide preserve the upstream contributors' work, ownership, assignments and acceptance conditions. There is no upstream submission, issue-completion or bounty claim.

| Path | Original Git blob | Role |
| --- | --- | --- |
| `src/contexts/NotificationContext.tsx` | `8a05dbf6fb720af3f876baef6b14f035d02b6c51` | Changed read actions |
| `src/components/notifications/NotificationCenter/AnalyticsTab.tsx` | `229ac9c09f22558f78c2fab38979a8f03e7e9a88` | Changed numeric display condition |
| `src/services/notificationService.ts` | `f979e6357339d236f619efc9c64852919e90610b` | Existing response-time calculation and metadata contract |
| `src/components/notifications/NotificationCenter/NotificationCenter.tsx` | `0cd01f490a82263a5961f4567d62931ae3ffd186` | Actual individual/batch/all-read and analytics caller |
| `src/components/notifications/NotificationCenter/NotificationsTab.tsx` | `56e2737f7b4cb1825f0e3f711c9e51ce1f28206b` | Actual rendered controls |
| `src/hooks/useLocalStorage.ts` | `96720ed34bd96b3e6aa8e441b97ce8d5d710d791` | Existing notification persistence |
| `src/types/notifications.ts` | `ab97b18fd0e9c78562181659141660e8a92c21ec` | Existing read boolean and metadata record |

The acquired locale layout/provider/navbar/Bell chain mounts this center. The center's notification click invokes provider `markAsRead` for unread records; its batch handler invokes the same action for selected IDs. The rendered mark-all control receives provider `markAllAsRead`. The original provider maps each applicable record to `read: true` without adding metadata.

The unchanged service includes only records with both `read` and `metadata.readAt` in the average. Its own separate `batchMarkAsRead` helper already writes an ISO string in that field, but the acquired mounted center does not use that helper. The analytics tab displays the resulting `averageResponseTime`. These complete actual producers and consumers establish the integration gap without runtime observation.

## Correction

The two-file patch changes +13/-3 in two hunks:

- Each provider read action captures one ISO timestamp before entering its state updater. The updater adds that value to `metadata.readAt` only when changing an unread record to read.
- Existing metadata is spread into the updated record. Nonmatching records and already-read records are returned intact, so repeated marking does not revise an existing read time.
- The analytics tab treats `undefined` as unavailable and renders a numeric zero as `0m`, using the same existing rounding and suffix.

Capturing time outside the updater keeps the transition value stable if the existing state updater is evaluated again. The mark-all action uses one timestamp for its changed records. The current batch handler still invokes the individual action once per selected ID; this patch does not impose a new common timestamp on that separate loop.

All notification IDs, array ordering, deletion/dismissal, preference gates, storage key/API, analytics arithmetic, filter/selection policy, sounds, desktop notifications and WebSocket logic stay unchanged. This records the time of a local mark-read action, not proof that a person read or acted on a notification.

Already-read history without `readAt` is not backfilled with an invented historical time. Invalid metadata, clock changes, arbitrary external records, cross-tab races, persistence failures and full analytics quality remain outside this correction. The calculation's existing lack of malformed-date validation is unchanged. No notification data was accessed.

## Composition and exact identities

Apply `record-read-transitions.patch` at the pinned source. It touches neither the selection-membership files changed by [Commons #31943](https://github.com/woahwhattheheck/commons/pull/31943) nor the CSV producer changed by [Commons #31947](https://github.com/woahwhattheheck/commons/pull/31947). Those packets compose independently; their completed work is not repeated here.

| Source | Before blob / UTF-8 bytes | After blob / UTF-8 bytes |
| --- | --- | --- |
| `src/contexts/NotificationContext.tsx` | `8a05dbf6fb720af3f876baef6b14f035d02b6c51` / 10074 | `128f95e7295d03f1de7ea4c5c23dca20b24eb63e` / 10332 |
| `src/components/notifications/NotificationCenter/AnalyticsTab.tsx` | `229ac9c09f22558f78c2fab38979a8f03e7e9a88` / 6159 | `e3f32b9dbffa0c4fd41f7254ce9a87ce6f7c8d1e` / 6173 |

Both complete original files match their native identities. Every serialized patch hunk was projected, then forward reconstruction matched each complete postimage and inverse reconstruction matched each preimage, including AnalyticsTab's existing absent final newline. These checks are source-text integrity only; the application and classifier/calculation were not executed.

Bounded public Slack and Commons PR searches for NotificationContext plus readAt returned no matches; the GitHub response reported incomplete_results false. This is bounded collision evidence, not a global completeness claim.

The complete donor tree exposed no AGENTS/RULES path. Retained `docs/CONTRIBUTING.md` at `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` describes an EventSource release workflow. Current task constraints prohibit new tests/runtime/package publication. Differently attributed MIT notices under docs do not establish a repository-wide license; complete modules are not republished.

No tests, fixtures, browser, local-storage operations, audio, runtime, build, dependency installation, account/backend/payment operation, upstream mutation, acceptance, award or payout occurred. Existing unrelated module/type-import limitations remain; this packet makes no full build or whole-feature readiness claim.
