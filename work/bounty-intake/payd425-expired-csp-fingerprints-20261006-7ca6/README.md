# PayD CSP reports: remove expired fingerprint entries

The contributor's report buffer is capped at 500 records, but its separate fingerprint Map retains every distinct accepted directive/blocked-URI pair indefinitely. This source continuation removes entries that are already outside the existing five-minute duplicate window when another report is processed. It does not change the report buffer, logging, route configuration or current duplicate cutoff.

## Source and contributor

Canonical issue: https://github.com/Protocol-Guild/PayD/issues/425  
Existing contributor PR: https://github.com/Protocol-Guild/PayD/pull/438  
Donor repository: `Mercy017/PayD`  
Donor branch: `feat/csp-violation-reporting-425`  
Immutable head: `bd8966a61224d7b284217ac2ac4f574476611866`  
Changed production path: `backend/src/services/cspReport.service.ts`

Acquired native metadata identifies the existing PR as open and unmerged, with four changed files and no PR issue/review comments. The current bounded issue listing identifies issue 425 as open and assigned to Mercy017. All three returned issue-comment bodies were read: Silver36-ship-it and Mercy017 request participation, and the bot reports Mercy017's assignment. These are attributed contributor records, not upstream acceptance or authority to change the contributor branch. Preserve Mercy017's implementation and the original repository authors. This packet changes only Commons artifacts.

| Complete acquired text | Git blob | UTF-8 bytes |
|---|---|---:|
| Original service | `50143a81ce4022688ca9f606b042aee188dbaf28` | 3629 |
| Prepared service | `fd9c3dc3f4463d8b9827339b0163500690e4af5a` | 3784 |
| backend/src/routes/cspReport.routes.ts | `1be63f703427dd0a2551d953ccc3e756c6adb792` | 1443 |
| backend/src/app.ts | `88fd30760141a2acbcd82dff68d813a6e21d6b36` | 7182 |
| LICENSE | `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64` | 11357 |

Every acquired full text matched its returned native blob identity and an independent Git blob hash. The prepared postimage was independently hashed as a complete string. The existing contributor test appears in changed-file metadata but was not acquired or executed.

## Connected source behavior

The acquired app imports the CSP route module and mounts it at `/api/csp-report`. Its Helmet configuration uses the same report URI. The route POST calls `recordCspViolation(req.body)`, catches thrown failures and then acknowledges with 204. The route GET calls the unchanged recent-report reader. This establishes the source connection; it is not evidence of a running server, browser policy delivery or actual report traffic.

The service extracts the report, captures `Date.now()` once and checks the fingerprint Map. Its predicate suppresses a report when `now - lastSeen < DEDUPE_WINDOW_MS`. A newly accepted report updates the fingerprint timestamp, appends a record, caps the record array and calls the existing logger. Before this correction, no path deletes any Map entry.

The patch inserts the following loop after the single captured time and before the unchanged duplicate check:

```typescript
  for (const [key, lastSeen] of lastSeenByFingerprint) {
    if (now - lastSeen >= DEDUPE_WINDOW_MS) {
      lastSeenByFingerprint.delete(key);
    }
  }
```

For finite saved timestamps at this invocation, an entry satisfying the removal predicate cannot satisfy the unchanged duplicate predicate. Entries younger than the window remain; equality is expired. Negative ages are retained at this invocation, matching the existing predicate's treatment of a clock rollback. Cleanup and admission use the same captured time. Iteration visits the existing Map and removes only current expired keys; it does not add fingerprints during the loop.

This is an expiration policy using the existing wall clock. It does not guarantee whole-history equivalence under later backward clock jumps: once an expired entry is removed, a future rollback cannot revive that discarded timestamp. No monotonic-clock or clock-change mechanism is added.

## Verification and material limits

The actual serialized unified patch has one hunk, twelve complete rows, six insertions and no deletions. Independent parsing and forward materialization reproduce the exact 3,784-byte prepared source; inverse materialization reproduces the exact 3,629-byte donor source. All source outside the recorded insertion remains byte-for-byte unchanged. This verification operates on strings and patch structure; the TypeScript service was not run.

Cleanup runs only when another report reaches this service. It scans the current Map once per invocation, so work is linear in the number of stored fingerprints. It does not reclaim entries while idle and does not cap the number of distinct fingerprints received within one five-minute interval. No fixed memory bound, throughput improvement or denial-of-service protection is claimed.

The app's existing mount order places this route before later audit, rate-limit and tenant middleware. The acquired GET route exposes its existing review behavior. This packet does not alter or approve those policies, report privacy, log content, parser validation, batched-report extraction, GET limit handling or authentication. It does not establish that the service comment's broad never-throws claim is true. No report, log, database, credential or user data was accessed.

No server, HTTP endpoint, browser, logger, TypeScript compiler, package installation, test, fixture, performance measurement, deployment, upstream issue/PR, account, sponsor or reward action was performed. This is a narrow source correction, not completion or acceptance of the broader CSP issue.

## Artifacts and license

`expired-fingerprints.patch` modifies only the named service against the exact contributor head. This guide describes that modification and its scope. `LICENSE` is the full unchanged Apache-2.0 text acquired from the same donor. Retain the original contributor attribution and notices. The full donor service, route and app are not republished.
