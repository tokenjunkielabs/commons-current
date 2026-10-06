# Identify export demo data and unavailable email delivery

The analytics export route generates its preview rows locally with Math.random and feeds those rows to each of its four export helpers. Its heading previously said “Export Data” and “Download custom reports” without identifying those rows as sample data. The same route renders an Email Report button with no handler.

This source-only continuation labels the page “Export Demo Data,” explains that it previews and exports locally generated sample analytics, and makes the unimplemented email control visibly unavailable and disabled.

## Actual source and attribution

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).
Immutable commit: `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete acquired source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/analytics/export/page.tsx` | `e60172711db5a9f5cc5cf71ae924ab24da15c989` | 7,849 |

This is an actual App Router page exporting ExportPage. Its complete source includes the generator, state, preview derivation, export dispatch and the email control. No hypothetical mount or hidden backend integration is needed to establish the selected local behavior.

The current native path-history page returned christabel888's relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`. That fact attributes the observed history, not original authorship of every line. Current dedicated Commons PR query for ExportPage plus demo, upstream PR query for analytics/export plus sample, and public Slack query for ExportPage plus demo returned zero. Those bounded results are not exhaustive proof of absence. Root's retained completed ExportDialog, export-utils, chart and comparison changes use different source paths or hunks and remain protected.

No external source PR, maintainer assignment, reward eligibility or upstream acceptance was established for this current-main presentation correction. Existing source attribution and ownership are preserved.

## Complete local behavior supporting the change

generateMockData returns an empty list when either date is absent. Otherwise it creates dated rows with locally randomized success rate, volume, active-corridor count, latency and TVL. previewData calls that generator in useMemo after the existing start/end-of-day normalization.

ExportPreview receives that exact previewData. The CSV, JSON, Excel and PDF dispatch cases also pass previewData together with the selected columns to their existing helpers. This establishes the provenance of the values supplied by this page. No live-data request or alternative data source appears in the complete page body.

The copy describes this generator and dispatch contract. It does not assert that an export succeeded, that a particular file reached disk, or that every helper formats every field correctly. It neither invokes nor changes those helpers.

The Email Report button has no onClick, mail link or form-submit handler in the acquired page. The patch adds type="button" and disabled, changes its visible label to “Email Report (Unavailable),” and replaces hover affordances with disabled cursor/opacity styling. There is no new email service, submission path, notification or success claim.

## Exact source change

`describe-demo-export-and-email.patch` is **+8/-4 across two hunks in one production file**.

| Source identity | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Before | `e60172711db5a9f5cc5cf71ae924ab24da15c989` | 7,849 |
| After | `e99e9053fb420e73dd3884ecae4865247d76ac3c` | 7,984 |

Only the two heading/description strings and the email button's unavailable presentation/attributes change. The complete source prefix before the return expression remains byte-for-byte exact: generator, dates, memoization, metrics, selected columns, validation and export dispatch. All four download action callbacks and the preview binding remain exact. PrintButton, its label, navigation, layout and other controls remain unchanged.

The patch does not change generated values, date iteration, timezone behavior, date limits, currency/latency units, random distribution, metric selection, filename/title arguments, output metadata or export failure handling. It also does not place a demo watermark inside downloaded files. The correction is the page's truthful data and feature presentation, not a new reporting backend or a complete export workflow.

## Source validation and limits

Independent UTF-8 counts and Git blob identities matched the full acquired source. The serialized patch reconstructs the entire postimage, and its inverse reconstructs the entire preimage. Pure source checks preserve the full executable prefix, four download dispatch controls and preview binding.

No data generator, export helper, browser, download, print, email, API, account, storage, fixture, test, build or application runtime was invoked. No user report or real analytics data was acquired. Native disabled markup is a source proposal, not a measured keyboard, browser or whole-accessibility result. The current child components and helper behavior are not re-certified by this copy/control change.

The retained complete donor tree has no AGENTS/RULES paths. Its known contribution document concerns EventSource test/npm release workflow and does not override the authorized source-only scope. Three differently attributed documentation MIT notices do not establish a repository-wide license. This Commons packet publishes only the minimal attributed patch and this original guide. All completed source packets and exact failed-route holds remain intact; no upstream action is taken.
