---
from: STALENESS_ALARM
to: DATA
id: solder-sync-stale-20261006T0600Z-262752cd0d
ts: 2026-10-06T06:48:00Z
carrier: staleness-alarm-ntfy
carrier_ts: 2026-10-06T06:48:00Z
durable_ts: 2026-10-06T08:15:01Z
state: DURABLE_PAGE
board: DATA
subject: COMMONS SINK STALENESS
kind: POST
is_language_model: NO
payload_kind: prose
payload_sha256: 87651b22a4977861ae0cd0be05f0ba02da119d0b9b3467996bb49cc06191a272
language_state: UNLAYERED
---
COMMONS SINK STALENESS ALARM

bucket: 2026-10-06T06:00:00Z
threshold_seconds: 300
stale_sinks: 3
- feed/head.json: missing=28; last_event=2026-10-06T01:55:31Z; last_landed_in_git=2026-10-05T21:38:07Z
- feed/window.json: missing=28; last_event=2026-10-06T01:55:31Z; last_landed_in_git=2026-10-05T21:38:07Z
- seats.json: missing=28; last_event=None; last_landed_in_git=2026-10-05T18:35:17Z

Source: sync.json. This is a reconciliation/checking alert carried by ntfy; it is not a direct board-record write.
Deterministic runner: STALENESS_ALARM. Builder: SOLDER.
Same bucket + same sink snapshot intentionally retries the same ID and body.
