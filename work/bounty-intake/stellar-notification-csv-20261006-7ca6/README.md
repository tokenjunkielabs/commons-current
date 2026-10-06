# Notification history CSV serialization

The mounted Notification Center can export stored notification history to CSV. Its producer assumes every timestamp is a Date, although the actual persistence hook restores timestamps as strings. The producer also surrounds each field with quotes without escaping quotes inside the field. This patch corrects both failures in the same CSV serialization path.

## Source and attribution

This is a narrow continuation over the existing Stellar-Analysis/frontend implementation at commit `482ee456369418ef82c4056718cb82d3468f762b`. Original implementation, contributor ownership, assignment and upstream acceptance remain with that project. This Commons packet contains a minimal attributed patch and this original guide; it is not an upstream submission or a claim to the full notification feature.

| Role | Exact path | Git blob |
| --- | --- | --- |
| Changed producer | `src/services/notificationService.ts` | `f979e6357339d236f619efc9c64852919e90610b` |
| Persistence hook | `src/hooks/useLocalStorage.ts` | `96720ed34bd96b3e6aa8e441b97ce8d5d710d791` |
| Provider and stored notification creation | `src/contexts/NotificationContext.tsx` | `8a05dbf6fb720af3f876baef6b14f035d02b6c51` |
| Declared record shape | `src/types/notifications.ts` | `ab97b18fd0e9c78562181659141660e8a92c21ec` |
| Center export handler | `src/components/notifications/NotificationCenter/NotificationCenter.tsx` | `0cd01f490a82263a5961f4567d62931ae3ffd186` |
| Actual CSV button | `src/components/notifications/NotificationCenter/NotificationsTab.tsx` | `56e2737f7b4cb1825f0e3f711c9e51ce1f28206b` |
| Navbar consumer | `src/components/navbar.tsx` | `1d519697311060e2d72c1a8fcaa59d1eb6148277` |
| Bell consumer | `src/components/notifications/NotificationBell.tsx` | `8e17fc08741d51bda9d0b3169a4b563fd528e89b` |

The fully read locale layout mounts the notification provider and navbar; the navbar's notification barrel resolves to NotificationBell, which mounts the center. NotificationsTab's CSV button calls the supplied handler with `csv`; the center passes the current filtered notifications to this service before creating a download Blob. This is a mounted consumer, not a demo-only export.

The provider creates notifications with `timestamp: new Date()` and persists its array under `stellar-notifications`. The hook writes `JSON.stringify(valueToStore)`, initializes with plain `JSON.parse(item)`, and processes storage events with plain `JSON.parse(e.newValue)`. Neither path supplies a Date reviver. Therefore a valid saved Date is restored as its ISO string, while the original CSV serializer calls a Date method directly. The service's existing filtering and analytics already normalize timestamps using `new Date(notification.timestamp)`.

## Exact change

The single hunk changes two lines (+2/-2):

- Convert the timestamp through `new Date(notification.timestamp).toISOString()`, accepting the valid Date or serialized ISO-string representation established by this producer/persistence chain.
- Double each embedded double quote before putting the existing double quotes around every CSV cell.

All declared fields used here are strings after the existing timestamp/read conversions. Headers, field order, notification order, commas, existing LF record separators and JSON export bytes remain unchanged. No storage migration, schema change, filtering, selection, batch operation, download lifecycle or error UI is added. The completed selection-membership packet [Commons #31943](https://github.com/woahwhattheheck/commons/pull/31943) is on different files and composes independently. The separately published `src/lib/export-utils.ts` CSV change is a different producer.

The primary [RFC 4180 section 2](https://www.rfc-editor.org/info/rfc4180/) describes enclosing special-character fields in double quotes and doubling embedded quotes. It is Informational. This change preserves the existing LF separators and makes no full RFC-conformance, spreadsheet interoperability or formula-injection claim. [MDN Date.toJSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toJSON) documents the automatic JSON serialization to an ISO string and Date reconstruction; those primary contracts were read without running their examples.

## Applying and source integrity

Apply `notification-csv.patch` to the pinned producer above. Its source identities are:

| State | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Before | `f979e6357339d236f619efc9c64852919e90610b` | 10509 |
| After | `bf800b761703b30404fa783f14905b5d6ebd2994` | 10539 |

The complete acquired source matched its native blob identity. The complete serialized patch reconstructed the postimage forward and the preimage in reverse, with every hunk row included. These are text/source integrity checks, not application execution or behavior tests. Exact public notificationService CSV and toISOString history searches returned no results; one bounded Commons PR query for notificationService plus CSV returned zero with incomplete_results false. These searches do not establish global absence.

The full donor tree exposed no AGENTS/RULES path. The retained docs/CONTRIBUTING.md at `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` is EventSource release guidance. Current task restrictions exclude tests, runtime and package publication. The differently attributed MIT notices under docs do not establish a repository-wide license, so this packet does not republish complete source modules.

## Limits

This repair assumes the actual declared record fields and valid timestamps generated by the acquired provider. It adds no malformed-storage validation, arbitrary date interpretation or fallback for invalid dates. The type still declares Date even though JSON restoration produces strings. The existing module also refers to NotificationPreferences without importing it; that separate type/import problem is unchanged, so no typecheck or whole-module build success is claimed.

No browser, storage access, actual notification data, download, spreadsheet, tests, build, dependency installation, runtime, upstream change, sponsor acceptance, bounty award or payment operation was performed.
