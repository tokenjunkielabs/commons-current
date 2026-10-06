# PayD top bar: identify its fixed sample values

The mounted DashboardTopBar declares its organization name and balance as fixed string constants under a Mock org data comment. It takes no props and performs no lookup for either value. The visible labels currently say Organization and Available Balance. This patch changes those two labels to Demo organization and Sample balance so the existing examples are not presented as an available account balance.

## Source qualification

Canonical donor: Protocol-Guild/PayD at `171c74b454daba241bfb75f36d10a0a3a77a68e5`.
Changed source: `frontend/src/components/DashboardTopBar.tsx`, mode 100644.

| Complete source | Git blob | UTF-8 bytes |
|---|---|---:|
| Canonical DashboardTopBar.tsx | 617350d5649d30be44a2a01c1776d69870edd840 | 1603 |
| Prepared DashboardTopBar.tsx | ef3399a77d8ad34d0ca1f693b0e537664cddcdfc | 1605 |
| EmployerLayout.tsx | 5cd117fcdaf260873f1e9f8655787857a3288ca2 | 3061 |
| App.tsx | acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c | 6460 |

The complete component, caller and route bodies were retained during the earlier ThemeToggle source qualification. Native blob identities, independent Git hashes and path/mode/size against the complete canonical tree all match. This correction uses those complete bodies without rereading or replaying the earlier ThemeToggle work.

App actually installs EmployerLayout as a route layout, and EmployerLayout directly renders DashboardTopBar alongside its outlet. Thus the two labels are on a connected rendered component, rather than an unmounted catalogue example. This establishes the source chain, not a request, route visit, authorization result or observed browser display.

The source itself fixes both orgName and balance locally. No prop, state, effect or data request in DashboardTopBar supplies either value. The complete constant declarations remain exact. The statement is limited to these two values; it does not classify data in child controls or the rest of the application.

A new bounded all-state Commons PR query for PayD / DashboardTopBar / balance, topn10, returned zero entries through the dedicated PR search tool. This is bounded overlap evidence rather than a repository-wide ownership or issue-completion claim. Earlier Sidebar, EmployerLayout, ThemeToggle, account and financial families remain protected and unchanged.

## Two visible text changes

The Organization label becomes Demo organization. The Available Balance label becomes Sample balance. These are existing English text nodes inside the same design-system Text elements. The existing values, class strings, styling props, imports, containers, responsive classes and child element order are byte-identical.

The original organization block has hidden/lg:flex classes; its visibility remains existing behavior. The balance block and its styling remain unchanged. The longer/different labels have not been visually measured, and no wrapping, clipping or viewport guarantee is claimed.

ThemeToggle and ConnectAccount invocations are untouched. No account source or credential is acquired, and no connect, wallet, balance, payment or theme action is performed. The patch does not add an API, convert a currency, refresh a balance, change permissions or replace the fixed data.

This is a source-connected presentation correction discovered while documenting reusable components. It is not a claim to complete the wider PayD180 documentation issue, any balance feature or an account integration. Internationalization and replacement of the sample constants remain separate work.

## Static validation

The actual serialized patch has 2 complete hunks and 16 rows, two insertions and two deletions. Forward application produces the exact 1605-byte prepared source and inverse application recovers the exact 1603-byte preimage. Reversing the two unique text replacements recovers every original byte. The complete mock-constant section and the entire child-controls section match exactly.

This is text and Git-identity verification. No React component, design-system dependency, route, browser, CSS engine, account provider, formatter, currency expression, network data path, test or fixture was executed. No user or account data was needed.

## Artifact and license scope

label-sample-topbar-values.patch is the source patch; README.md is this guide. LICENSE is the original Apache-2.0 notice retained from the canonical donor, blob 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64, 11357 bytes, reproduced unchanged. Original Protocol-Guild/PayD contributors retain attribution. No complete component or caller is republished.

The Commons publication adds these three artifacts under work/bounty-intake/payd-topbar-sample-labels-20261006-7ca6/. Guarded tree construction preserves existing repository contents. All three complete immutable readbacks are compared to authored text with native blob IDs and independent Git hashes; final metadata and exact paths are checked where available, preserving any failure rather than retrying a held route.

A fresh same-repository main equality is a separate predeclared alias only if main equals the verified merge/readback ref. Otherwise all three full artifacts are read once at one observed immutable main without branch chasing. This validates published documents, not a production deployment or observed financial state.

No runtime, compiler, tests, screenshots, authentication, account, wallet, payment, upstream submission, sponsor or whole-feature acceptance action is performed.
