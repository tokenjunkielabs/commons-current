# Active-contract activity windows: source qualification before backend #21

The current canonical backend has no mounted active-contract endpoint. The concrete contract-event producer stores a snapshot payload timestamp of undeclared units, leaves its received ledger-close timestamp unused, and writes processing time into `created_at`. A count presented as recent seven-day contract activity therefore needs a producer, time and coverage contract before implementation. This packet records the integration evidence and deliberately selects no endpoint patch.

The analysis concerns [Stellar-Analysis/backend issue #21](https://github.com/Stellar-Analysis/backend/issues/21) at commit `965e916227cf9173cf6ad254a6971429060c1d19`, with complete tree `c39f5c12c3421cd08180adab6508f2f365a8e10b` (431 entries). It is an original analysis-only addition to Commons. It contains no copied source files, code patch, deployed-state claim or upstream submission.

## What the issue and consumer actually require

Issue #21 requests a distinct-contract count backed by stored event rows over a recent window. It explicitly warns that the answer depends on issue #20's ingestion coverage. The issue itself does not choose seven days, a window parameter/default, timestamp column, interval boundaries, timezone or network filter.

The already reviewed frontend supplies the concrete consumer: its mounted Soroban page calls the active-contract helper with `7d`; the helper requests `/api/v1/soroban/active-contracts?window=7d` and sends no network filter. The success contract reads a numeric `count`, optional `window` and optional numeric `trend`. Its existing caught-failure path marks the display unavailable. A missing or nonnumeric successful count still normalizes to zero in the existing frontend; that separate limitation is not repaired or reinterpreted here.

This frontend evidence is a coordinator transfer from complete source review, not a second source audit by this packet's author. The original canonical revision is `482ee456369418ef82c4056718cb82d3468f762b`; paths are `src/lib/soroban-api.ts`, `src/app/[locale]/soroban/page.tsx` and `src/components/soroban/ActiveContractsPanel.tsx`. Current composed source identities are API `a3ba6bc1f13ec89d31191d18550e8bb0b584b407` (9,226 bytes) and page `80ba478b5aa34d8af463ea4a5c6f969eeca114fa` (6,254 bytes), preserved in the public Commons checkpoint lineage identified in SOURCE_EVIDENCE.json. Those composed blobs are not attributed to the original canonical frontend tree. Accepted frontend packets #32125, #32129, #32132 and #32134 remain unchanged.

## Actual router and database integration

The acquired `src/main.rs` calls `api::v1::routes`. That router mounts versioned routes at `/api/v1` and also preserves its unversioned router. Neither this complete composition nor its API module list registers a Soroban/active-contract endpoint, and the complete tree has no `src/api/soroban.rs`.

The existing `src/api/contract_events.rs` serves event-list, verification-summary and audit-statistic functions. Its router is not merged into the acquired canonical main/v1 route chain. Reusing the module name would therefore not by itself make a handler reachable.

The declared dependency features and concrete source types use SQLx `SqlitePool`: startup creates the pool and runs migrations; shared `AppState` contains `Arc<Database>`; `Database::pool()` is public. The README's production-PostgreSQL wording does not override those source types. A new read handler can in principle use this existing storage. It would still require explicit module/router integration and an agreed metric definition; this is not a repair of an existing active-contract implementation.

Nearby API functions return direct JSON objects/vectors and propagate failures as HTTP status/string errors. Event statistics query failures are not converted to successful zero counts in that source. A future handler should preserve a meaningful failure boundary, without copying the existing disclosure of underlying error strings merely for stylistic consistency.

## Three different notions of time

| Stored or received field | Evidence in the pinned source | Consequence |
| --- | --- | --- |
| `contract_events.timestamp` | Migration 022 labels it an optional integer Unix timestamp for indexing. The listener extracts the snapshot payload's numeric timestamp and stores it without a unit conversion or ledger-time comparison. | This producer does not establish a general ledger-event timestamp or its units. |
| `ContractEvent.ledger_closed_at` | The listener declares this string in its RPC event model. Its declaration is its only occurrence in the complete file. | The potentially relevant event-envelope time is not parsed or persisted by this listener. |
| `contract_events.created_at` | The concrete listener binds the processing-time clock when it stores a snapshot. The general indexer instead binds the caller's supplied creation time. Its ordering comments call this insertion time. | Counting recently inserted rows is a different metric from recent on-chain activity, particularly after delayed ingestion or backfill. |
| `contract_events.timestamp_dt` | Migration 022 supplies an optional timestamp for replay. Neither of the acquired listener/indexer insert column lists writes it. | Its existence in the schema does not establish population for this producer. |

The concrete listener handles only the `SNAP_SUB` topic. It constructs `SnapshotEvent` and inserts directly into `contract_events`; it does not construct `IndexedEvent`. Its snapshot timestamp comes from the contract payload, while its `created_at` value is the local processing time. Both that listener and the separate indexer omit `timestamp_dt` and `network` from the acquired insert paths.

The general `EventIndexer` permits a missing indexing timestamp and passes caller values through. Its existing time-range filter and last-24-hour statistic use `created_at`. Those queries are evidence of insertion-time analytics, not authorization to label an insertion-time count as recent contract activity.

These distinctions prevent two tempting but unsound substitutions: silently querying `created_at` for the caller's activity window, or querying only non-null payload timestamps and representing a resulting zero as established absence of recent activity. This packet does not supply a fallback clock, reinterpret payload units, or infer database contents.

## Coverage remains an existing-pipeline dependency

The coordinator separately acquired [issue #20](https://github.com/Stellar-Analysis/backend/issues/20)'s public body and metadata. It remains open with no native assignee or comments. Its requirements say the pipeline already exists and should be extended, not duplicated. It names the existing listener job, contract listener, indexer and event table; calls out the single configured snapshot contract; and requests coverage of every needed contract with rate-limit awareness and verification across distinct contracts before staged integration.

The issue author reports ten relevant contracts and only three then emitting real events, citing another contracts issue. Those are attributed issue statements, not independently verified network or current contract counts. The referenced contracts issue was not opened for this analysis.

The acquired listener's request filter uses one configured contract, and non-snapshot topics are ignored. The separately acquired listener job's missed-event body returns a placeholder zero. These facts support retaining the coverage dependency. They do not establish that every possible ingestion path is absent or broken, and no ingestion correction is selected.

## Decision and conditions for a later implementation

No truthful seven-day event-window implementation is selected from the currently qualified contract. A later bounded handler proposal would first need to establish:

1. A producer-backed event-time field, explicit units, accepted provenance and handling of missing/invalid values across the relevant row producers.
2. Precise window boundaries and treatment of late ingestion/backfill, without substituting processing time for activity time.
3. Network/data-set scope, since the current frontend sends no network filter and the acquired insertion paths do not set the nullable network column.
4. An explicit coverage/freshness contract compatible with the unfinished existing-pipeline work, so a successful numeric count is not mistaken for complete network coverage.
5. A failure response distinguishable from a genuine empty observed window, followed by routing into the actual maintained Axum chain.

This is an integration decision from the inspected source, not a claim that the broader feature is impossible. The source is structurally capable of a database-backed read endpoint once its metric and input contract are established.

## Source identity and review limits

All fourteen newly acquired backend source strings were independently hashed with the existing Git UTF-8 blob-identity helper. Each complete byte count and computed SHA matches both the native content response and the pinned canonical tree. The helper identity is `132074b6393afd73a921939ad39789f3a6b38ce5` (3,003 bytes), public Commons path `host/connected_git_blob_identity.cjs`. This verifies byte identity; it does not execute or validate the application. SOURCE_EVIDENCE.json records structured public provenance and clearly distinguishes the transferred frontend/issue20 evidence.

| Backend source at the pinned revision | Git blob SHA | UTF-8 bytes |
| --- | --- | ---: |
| [README.md](https://github.com/Stellar-Analysis/backend/blob/965e916227cf9173cf6ad254a6971429060c1d19/README.md) | `160135699501a4db3ad4ab8439fc9f19625e7fe4` | 3,413 |
| [Cargo.toml](https://github.com/Stellar-Analysis/backend/blob/965e916227cf9173cf6ad254a6971429060c1d19/Cargo.toml) | `f0fe093ebbb5c3eb962b3337beb1b764afd0fd39` | 3,555 |
| [src/lib.rs](https://github.com/Stellar-Analysis/backend/blob/965e916227cf9173cf6ad254a6971429060c1d19/src/lib.rs) | `6de97c5a7dbc81abe6a2b243b22cb214544bbd3e` | 1,769 |
| [src/api/mod.rs](https://github.com/Stellar-Analysis/backend/blob/965e916227cf9173cf6ad254a6971429060c1d19/src/api/mod.rs) | `23141dded2c5491442d04021c0127c6fd030aa9f` | 777 |
| [src/api/v1/mod.rs](https://github.com/Stellar-Analysis/backend/blob/965e916227cf9173cf6ad254a6971429060c1d19/src/api/v1/mod.rs) | `a3677c8afa44f712a391a15ff1765b6a095b37ac` | 7,385 |
| [src/main.rs](https://github.com/Stellar-Analysis/backend/blob/965e916227cf9173cf6ad254a6971429060c1d19/src/main.rs) | `622bfe12d04b476206149e2fbf42cb42bc922bde` | 23,450 |
| [src/api/contract_events.rs](https://github.com/Stellar-Analysis/backend/blob/965e916227cf9173cf6ad254a6971429060c1d19/src/api/contract_events.rs) | `4045b0d71b248c6747e711c29b0da44df3f96092` | 7,920 |
| [src/database.rs](https://github.com/Stellar-Analysis/backend/blob/965e916227cf9173cf6ad254a6971429060c1d19/src/database.rs) | `0d1a0c5deb3ac6c070df1477d5ef457ac0e31281` | 77,481 |
| [src/state.rs](https://github.com/Stellar-Analysis/backend/blob/965e916227cf9173cf6ad254a6971429060c1d19/src/state.rs) | `0399f0e69e7ac7c70bfc6d192e236a50bc5463dc` | 3,059 |
| [src/services/event_indexer.rs](https://github.com/Stellar-Analysis/backend/blob/965e916227cf9173cf6ad254a6971429060c1d19/src/services/event_indexer.rs) | `05eb9a09f7f65e54b1df836a4f7cf7c13f134353` | 25,981 |
| [src/jobs/contract_event_listener.rs](https://github.com/Stellar-Analysis/backend/blob/965e916227cf9173cf6ad254a6971429060c1d19/src/jobs/contract_event_listener.rs) | `359cffac835f330af35dc3ff17f3838209504816` | 8,546 |
| [migrations/022_create_replay_tables.sql](https://github.com/Stellar-Analysis/backend/blob/965e916227cf9173cf6ad254a6971429060c1d19/migrations/022_create_replay_tables.sql) | `2ca56434b39fe86f11b2e13a61d6b887d311257f` | 4,166 |
| [migrations/025_create_contract_events.sql](https://github.com/Stellar-Analysis/backend/blob/965e916227cf9173cf6ad254a6971429060c1d19/migrations/025_create_contract_events.sql) | `b00a0b837f3af30c56ccd9de88c40779c094ab94` | 70 |
| [src/services/contract_listener.rs](https://github.com/Stellar-Analysis/backend/blob/965e916227cf9173cf6ad254a6971429060c1d19/src/services/contract_listener.rs) | `d50cfd47c73af574a831b4e64c24533150859b0c` | 20,083 |

The repository metadata reported no license, and the complete tree exposed no AGENTS.md, CONTRIBUTING.md or license filename. The README and Cargo lint configuration were read. These are bounded metadata/filename observations, not a legal conclusion or an inferred license grant. No donor source payload is reproduced in this packet.

The earlier dedicated issue21 PR search returned only the related, already merged schema PR #55, which closes #46. Its source was not acquired, and its completion is preserved. That bounded result is not proof of global implementation absence. Other endpoint issues and external owners are not taken over.

No application/API/RPC invocation, database query, contract/account/transaction action, build or test was performed. No upstream issue or branch was changed. No private messages, journals, cache keys or account data are included. The conclusions apply to the pinned source and the separately attributed consumer/dependency evidence, not to deployed state.
