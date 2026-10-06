# USGS ShakeAlert production code review — RFI readiness packet

Prepared: 2026-10-06  
Notice: `140G0326Q0223`  
Current disposition: **conditional NO-GO until the named-personnel gate is evidenced**

## Decision summary

This is a sources-sought / market-research response, not a request for a price proposal or quote. The Government says it will not reimburse response preparation and is not committing to buy. A responsive submission is due **2026-10-16 at 12:00 p.m. Pacific / 3:00 p.m. Eastern** and must be a PDF capability statement plus a general approach.

Do not submit as a prime or team unless a named code-review lead can supply defensible evidence of demonstrated real-time or safety-critical software experience. General concurrency, performance, security, or ordinary production-engineering work is not enough to assert that qualification.

No buyer contact, Michael Clark contact, terms acceptance, submission, or price commitment is authorized by this packet.

## Money state

| State | Amount | Evidence |
|---|---:|---|
| Advertised contract value | Not stated | The notice is market research and requests no price. |
| Proposed | $0 | No quote or proposal prepared or sent. |
| Promised | $0 | No buyer commitment. |
| Funded to us | $0 | No award or payable offer. |
| Awarded | $0 | No award. |
| Invoiced | $0 | No invoice. |
| Received | $0 | No payment. |

## Source record

- Public notice: https://abierto.us/opportunities/140g0326q0223
- SAM.gov notice linked from the public record: https://sam.gov/opp/7addd373195d41a2af0606880e4cbf4a/view
- Statement of Work, version 2.0, September 2026: https://abierto.us/files/b18a2dbd6c128aa052fc46f71e7c08bce37249bd4ea94b648bec0bf3e17299a6/44049950_RFI_SOW_1.pdf

Fresh read on 2026-10-06 confirmed:

- 12-month remote period of performance.
- Task 1 covers quantitative and qualitative review of the production modules, modified Earthworm modules, and maintained third-party libraries.
- Task 2 covers GitLab workflow, automated static analysis, coding standards, and Ansible-related deployment practices.
- Deliverable 6 requires working GitLab CI/CD changes, not recommendations alone.
- Written reports must be delivered in PDF and editable Word formats.
- Code-review personnel must have demonstrated experience in real-time or safety-critical software systems.
- The response must state socioeconomic designation, business size, SAM UEI, GSA contract number if applicable, and ability to execute all tasks.
- Generic marketing material or a website reference is explicitly nonresponsive.

## Submission fence

A submission is allowed only after every item below is evidenced in a source-bound dossier.

| Gate | Required evidence | Current state |
|---|---|---|
| Named reviewer | Resume/project reference showing real-time or safety-critical software responsibility | **BLOCKED — no qualifying person evidenced** |
| Organizational identity | Legal entity name and owner-approved point of contact | BLOCKED — owner-controlled |
| SAM UEI | Active entity record and exact UEI | BLOCKED — not verified |
| Business size | Size representation for NAICS 541519 | BLOCKED — not verified |
| Socioeconomic status | Current, supportable designation or “none” | BLOCKED — not verified |
| GSA vehicle | Contract number, or explicit “not applicable” | BLOCKED — not verified |
| Full-task coverage | Named ownership for every SOW task and deliverable | PARTIAL — draft matrix below |
| Past performance | 3–5 attributable references with customer-verifiable outcomes | BLOCKED — not selected |
| Conflict / confidentiality | Ability to protect nonpublic code and execute an NDA at award | BLOCKED — legal/owner confirmation |
| Authorized send | Final PDF, recipient, subject, and one-time send approval | BLOCKED — no outreach authorized |

If the named-reviewer gate is still red at the internal decision checkpoint, release this opportunity as **NO-GO as prime**. A subcontract role remains possible only behind a qualified prime and without inflating TJLabs credentials.

## Capability and responsibility map

The companion `capability-matrix.csv` is the machine-readable version.

| SOW area | Proposed TJLabs contribution | Required teammate / buyer input | Readiness |
|---|---|---|---|
| Repository census and metrics | Reproducible inventory; LOC/test/comment split; complexity, Halstead, coverage, documentation and dependency data | Language/build profile and production-branch access from USGS | Conditional |
| Module code review | Evidence register, file-bound findings, severity rubric and actionable recommendations | Named real-time/safety-critical lead owns expert judgment | Blocked |
| Fault and degraded-state review | Structured review of missing/out-of-order data, partial failures, retries and failure propagation | Production semantics and known-issue briefings from USGS | Conditional |
| Concurrency and real-time review | Review harnesses, traceable observations, blocking/unbounded-operation inventory | Qualified lead and system timing constraints | Blocked |
| ActiveMQ to NATS interfaces | Schema/order/timing matrix covering current and target states | Interface definitions and transition plan from USGS | Conditional |
| SA/DM alert logic | Evidence organization and test/readout support | Scientific/domain interpretation remains with USGS; expert reviewer required | Blocked |
| GitLab practices | Branch/MR/tagging assessment and resource-aware recommendations | Current GitLab settings and staff constraints | Conditional |
| Static analysis and coverage | Candidate open-source tool evaluation and merge-request reporting design | Actual language/build/licensing profile | Conditional |
| Deployment practices | Reproducibility, rollback, configuration validation and smoke-test assessment | Current Ansible/deployment artifacts | Conditional |
| Working CI/CD changes | Implement approved baseline GitLab pipeline under USGS review | Write access supplied for Deliverable 6; approval before merge | Conditional |
| Reports and briefing | Traceable PDF/DOCX reports, CSV/JSON data and briefing package | Prime owns final claims and customer-facing delivery | Conditional |

## Twelve-month delivery/RACI

R = responsible, A = accountable, C = consulted, I = informed.

| Month | Deliverable | Prime / contract lead | Qualified review lead | TJLabs technical production | USGS |
|---:|---|:---:|:---:|:---:|:---:|
| 1 | Kickoff and work plan | A/R | C | R | C |
| 1–3 | Repository census and metrics baseline | A | C | R | C |
| 2–6 | Detailed module review and prioritized findings | A | A/R | R | C |
| 3–8 | GitLab, static-analysis, standards and deployment assessment | A | C | R | C |
| 6–11 | Consolidated action plan and final report | A/R | R | R | C |
| 11 | Approximately two-hour briefing | A/R | R | C | I |
| 8–12 | Baseline GitLab CI/CD implementation and guide | A | C | R | A/C |

Accountability assignments are placeholders until a legal prime and named qualified reviewer accept them.

## Toolchain proposal — candidates, not commitments

The SOW says tools and standards will be agreed at kickoff after language and build access. Candidate evaluation should therefore be capability-based:

1. Repository and language census: `scc` or `cloc`, plus build-manifest discovery.
2. C/C++ static analysis: `clang-tidy`, `cppcheck`, compiler diagnostics, and selected CERT/MISRA-compatible checks.
3. Complexity and Halstead metrics: language-appropriate open-source analyzers validated against a small known corpus before baseline collection.
4. Coverage: the project’s existing framework, `gcov/lcov` or `llvm-cov` where compatible.
5. Documentation coverage: Doxygen-compatible extraction or language-equivalent public-API analysis.
6. Dependency evidence: compiler/build-graph extraction plus include/import graphing.
7. CI: GitLab merge-request pipelines for build verification, static analysis, unit tests, metrics artifacts and configurable coverage-decline alerts.
8. Deployment review: Ansible linting, configuration validation, version-bound artifacts, rollback rehearsal evidence, and post-deploy smoke-test design.

Every tool must be checked for language compatibility, license, deterministic output, operational overhead and fit for a small team before recommendation.

## Evidence packet still needed

Use attributable, customer-verifiable receipts only. Do not cite internal agent throughput or infer customer acceptance from source publication.

- Real-time or safety-critical reviewer resume and two relevant engagements.
- Three to five references covering code review, CI/CD implementation, C/C++ analysis, operational reliability, or regulated/federal environments.
- A redacted sample finding register.
- A redacted metrics baseline showing raw CSV/JSON plus a narrative summary.
- A redacted GitLab CI implementation receipt with build/static-analysis/test/coverage stages.
- Entity registration, representations, insurance/conflict posture, and authorized signatory.

## Acquisition-shaping questions

These are internal drafting prompts only; do not send without explicit approval.

1. Which languages, compilers, build systems and test frameworks are present in each module?
2. What GitLab runner environments and artifact-retention constraints apply?
3. Which production timing budgets and latency/error thresholds are authoritative?
4. What interface schemas and conformance tests exist for ActiveMQ and the planned NATS transition?
5. Which modified Earthworm and third-party components are in scope, and what licenses govern them?
6. What historic incident data and reproducible cases will be available for known timing/order issues and the 2022 Ferndale pause/update defect?
7. Are pipeline changes expected in one shared template, per-module configurations, or both?
8. What federal environment, access-control and data-handling requirements apply to review tooling and artifacts?

## Owner decision

- **GO** only if the named-personnel, entity, full-task, references and authorized-send gates become green.
- **NO-GO as prime** if the real-time/safety-critical reviewer cannot be evidenced.
- **SUBCONTRACT-ONLY** is acceptable behind a qualified prime when TJLabs scope and claims stay bounded to evidenced technical production.

Suggested internal decision checkpoint: **2026-10-10**, leaving six calendar days for owner/legal review, PDF production, and a single authorized submission if the gates clear.
