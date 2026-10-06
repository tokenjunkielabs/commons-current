# Align the IP resolver with the supplied TrustedHops API

The existing IP-allowlist implementation calls two methods that its supplied TrustedHops type does not define: is_trusted() and count(). The complete configuration module instead defines trusts_any_proxy() and get(), with the boolean and usize results needed at those exact call sites.

This two-line source continuation changes only those method names in backend/ip_allowlist/resolve.rs. It retains every existing branch, parser, fallback, index calculation and public API. It is an interface alignment within the authored implementation, not a completed proxy-trust or security solution.

## Existing carrier and attribution

The carrier is [Stellar-Analysis/frontend PR #403](https://github.com/Stellar-Analysis/frontend/pull/403), authored by **daniel6yi8-gif**. The current native PR observation at 2026-10-06 13:41:45 UTC established:

| Field | Observed value |
| --- | --- |
| State | Open, unmerged, draft=false |
| Head repository | daniel6yi8-gif/frontend |
| Head branch | drips/333-334-335 |
| Head commit | `3566cbbd307c5fc1316477b3ef83c57b83af3eb9` |
| Base commit | `482ee456369418ef82c4056718cb82d3468f762b` |
| Changed files | 11 |

Despite its backup-oriented title, the PR body explicitly combines issues #333, #334 and #335. This packet supplies one narrow residual for [issue #334](https://github.com/Stellar-Analysis/frontend/issues/334), preserving the original author and whole existing carrier. Other fleet work on its backup and background-job modules is separate.

Root transferred the current issue scope and assignment metadata: restrict admin/metrics access using explicit trusted-proxy topology, with spoofed-header and legitimate-path tests expected. The transferred task text is a faithful summary, not a claim that this seat independently received the complete native issue body. No issue assignment, upstream comment, source push, PR mutation, closure or payout action is made.

## Complete acquired source and actual caller

The three immutable blob responses supplied complete content without a separate returned SHA field. Their request-bound identities independently matched the full UTF-8 strings.

| Path in head repository | Input Git blob | UTF-8 bytes |
| --- | --- | ---: |
| backend/ip_allowlist/mod.rs | `470d4385d85fc578813f630df22f7d8ca6c4d752` | 1,759 |
| backend/ip_allowlist/resolve.rs | `2bc988bff693254624e3f8b82252951b2a6edae4` | 2,377 |
| backend/ip_allowlist/trusted_hops.rs | `7311af12f9d61692b03d0cb1de0bb6c17edec0b2` | 2,423 |

The acquired mod.rs re-exports the resolver and TrustedHops, stores the configuration in IpAllowlist, and calls resolve_client_ip from IpAllowlist::is_allowed before checking the resulting address against the permitted IP vector. This establishes a real intra-module caller. It does not establish HTTP middleware registration or deployment.

The complete supplied TrustedHops implementation exposes these relevant methods:

| Existing method | Actual source behavior | Resolver use |
| --- | --- | --- |
| trusts_any_proxy(self) -> bool | Returns whether the configured usize is greater than zero | Initial branch deciding whether to ignore forwarded input |
| get(self) -> usize | Returns the configured usize | Existing hop-count and index calculation |

TrustedHops derives Copy and Clone. The patch uses its existing methods and does not add aliases, change constructors/defaults, alter representation or introduce a dependency. The existing redundant usize cast is left in place to keep the change to two identifiers.

## Exact correction

| Changed path | Postimage Git blob | UTF-8 bytes | Diff |
| --- | --- | ---: | --- |
| backend/ip_allowlist/resolve.rs | `2e83f689c89e00e6ab0d325c96f655349e27399c` | 2,381 | +2 / -2 |

The two substitutions are is_trusted() → trusts_any_proxy() and count() → get(). Replacing those two new names back with the original names recovers the complete input exactly. Both strings retain the final newline. The other two acquired modules remain byte-exact.

The [Rust Reference on inherent implementations](https://doc.rust-lang.org/reference/items/implementations.html#inherent-implementations) explains how functions and methods defined in an impl belong to its implementing type. The current primary reference supports checking the supplied method identifiers against the actual implementation. It also permits multiple inherent implementations; this source analysis is scoped to the acquired modules and transferred complete PR delta, not an installed compiler or hypothetical additional crate code.

No compiler diagnostic was produced. The concrete evidence is the mismatch between the resolver's two names and the methods provided by the acquired type, together with their compatible result types and the actual IpAllowlist caller.

## Important remaining limits

This correction does not certify the issue's trust model or acceptance criteria. The source continues to:

- Represent trust as a hop count; it does not independently authenticate the immediate peer's identity.
- Filter out unparseable forwarded entries rather than preserve every original chain position or reject the whole header.
- Use its existing short-chain fallback and chain.len() - hops - 1 selection. The relationship between that selection and the documented single-proxy topology remains unqualified here.
- Fall back to the immediate peer under its existing conditions and compare the selected address against the existing allowed vector.

These are grounded remaining source questions, not new guarantees. The patch neither chooses a deployment topology nor changes allow/deny behavior through a new policy. No spoofing scenario, traffic, fixture, socket or proxy environment was run.

The retained complete canonical base tree has no backend root. Root's current complete PR delta contains these eleven added paths: backend/backup/{classify.rs,mod.rs,watermark.rs}, backend/ip_allowlist/{mod.rs,resolve.rs,trusted_hops.rs}, backend/jobs/{dead_letter.rs,error.rs,mod.rs,scheduler.rs}, and backend/tests/dr_drill_test.rs. No manifest, application registration or named spoofed_header_test.rs / legitimate_path_test.rs addition appears in that delta. The PR body's statements about middleware and those tests remain attributed author claims, not evidence that this packet ran or verified them.

Accordingly this patch targets the exact PR head, not canonical main, and does not claim an integrated backend build, a working admin-route boundary, safe endpoint deployment, whole-issue completion or passing tests.

## Source custody, instructions and validation

Same-base metadata was transferred from the existing complete canonical tree observation: 959 entries, truncated=false, no AGENTS/RULES, and branch tree `44703ba39198f99b6541450c740db0d1c3c0f7b8`. The recursive response echoed its requested commit; no independent full-tree reconstruction is asserted. The all-added eleven-file PR delta introduces no instruction or license file.

The retained docs/CONTRIBUTING.md, `f66db3b0eece27eb6fa888948c31ee8c7eabcfd2` (274 bytes), explicitly concerns EventSource tests and release commands. This packet does not change or release EventSource. Three differently attributed license notices remain preserved in [the generator continuation packet](../stellaranalysis-issue-generator-layout-20261006-7ca6/) without inferring repository-wide scope. Only this narrow patch and guide are published.

Validation consists of complete immutable source inspection, independent UTF-8/Git blob identities, current native PR-head observation, primary language-reference reading, exact reconstruction and unchanged-section comparison. There was no Rust compiler, Cargo, shell, executor, test, fixture, API server, socket, proxy, workflow or accepted-work replay. No runtime, security, integration, whole-build or deployment success is inferred.
