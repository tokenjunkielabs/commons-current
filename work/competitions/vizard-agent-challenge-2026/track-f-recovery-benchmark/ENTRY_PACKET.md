# Vizard Agent Challenge 2026 — Track F entry packet

Submission-ready, public-safe packet for a 45-second developer tutorial built from the public [lifecycle recovery benchmark](https://github.com/woahwhattheheck/commons/tree/main/research/competitions/gitlab_life_after_code/recovery_bench_r1).

This packet does not create a Vizard project, generate a film, publish a social post, accept contest terms, or submit an entry.

## Verified contest contract

Verified against the official [challenge page](https://agent.vizard.ai/challenge/index.html), [guidelines](https://agent.vizard.ai/challenge/guideline.html), and [rules](https://agent.vizard.ai/challenge/rules.html) on 2026-10-06.

- Track: **F — The Pitch** (ads, promos, and tutorials).
- Deadline: **2026-10-06 23:59 Anywhere on Earth**, which is **2026-10-07 07:59 EDT**.
- Entry: a Vizard Agent film of at least 30 seconds, a public post with both official hashtags and the official Vizard account tagged, and the contest entry form.
- Core generation and editing must happen inside Vizard Agent.
- Keep the submitted Agent project intact for six months.
- Judging: film quality 30, brief leverage 30, use-case value 25, reach 15.
- Advertised cash pool: **$3,000**, comprising six **$500** track-champion prizes. Cash is conditioned on organizer verification and tax documentation; no award is assumed here.
- The entrant grants the organizer the license described in section 5 of the official rules. The authorized entrant must review and accept the rules personally.

## One-brief prompt

Use this as the initial Agent brief. Add a follow-up only to correct a concrete defect:

> Turn this public developer benchmark into a 45-second technical tutorial for software engineers. Explain what it tests, show the recovery candidate versus fail-fast baseline using only numbers visible on the supplied page, show the two run commands, and end with a concise invitation to reuse the benchmark. Clean technical visual language, readable code, no invented claims or private project references.

Source URL:

```text
https://github.com/woahwhattheheck/commons/tree/main/research/competitions/gitlab_life_after_code/recovery_bench_r1
```

The brief is intentionally compact because brief leverage is 30% of the score and the Agent conversation is verified.

## Permitted factual claims

The film may state only these benchmark facts:

- offline, dependency-free lifecycle recovery benchmark
- six deterministic cases
- clean pass, recoverable test failure, fail-closed security failure, recoverable deploy failure, reused-evidence rejection, and approved package retry
- recovery candidate: **6/6 correct**
- fail-fast baseline: **3/6 correct**
- recovery success: **3/3**
- unsafe promotions: **0**
- candidate-minus-baseline task-success rate: **+0.50**
- candidate-minus-baseline median wall time: **+275 ms**
- candidate-minus-baseline p95 wall time: **+480 ms**
- candidate-minus-baseline median stages: **+2.5**
- these are synthetic offline scorer results, not production, GitLab Duo, customer, or competition performance

Do not expose private projects, internal coordination, credentials, account infrastructure, or unpublished results.

## Suggested 45-second structure

### 0–5 seconds — hook

“Fail-fast tells you something broke. Recovery testing asks what the agent does next.”

Show the benchmark title and the six-case count.

### 5–14 seconds — scope

Visualize three categories with large mobile-readable text:

- recoverable failures
- fail-closed hazards
- evidence integrity

### 14–25 seconds — comparison

| Recovery candidate | Fail-fast baseline |
| --- | --- |
| 6/6 correct | 3/6 correct |
| 3/3 recoveries | 0/3 recoveries |
| 0 unsafe promotions | 0 unsafe promotions |

Keep **synthetic offline benchmark** visible.

### 25–35 seconds — run it

Show these commands exactly and long enough to read:

```bash
python recovery_bench.py cases.jsonl candidate.jsonl --baseline baseline.jsonl
python test_recovery_bench.py
```

Do not invent terminal output.

### 35–45 seconds — reusable takeaway

“Measure recovery behavior, evidence integrity, and fail-closed decisions—not just whether a task eventually passes.”

CTA: “Fork the benchmark, swap in your agent’s predictions, and compare.”

## Narrow correction prompts

Prefer zero follow-ups when the first output is accurate and readable. If needed, use only the relevant correction:

- “Keep every benchmark number exactly as written on the source page; do not add performance claims.”
- “Hold the two command lines on screen long enough to read them on a phone.”
- “Replace the final claim with: synthetic offline benchmark, not production performance.”

## Public post copy

Use only after the final Vizard-rendered film has passed the checklist:

> A small benchmark for a hard question: when an agent hits a test, deploy, or evidence failure, does it recover safely—or just stop?
>
> I turned our public lifecycle-recovery benchmark into a 45-second developer tutorial with Vizard Agent. Six deterministic cases; recovery candidate 6/6 vs. a 3/6 fail-fast baseline. Synthetic/offline results only.
>
> #OneBriefOneVideo #VizardAgent @vizard

Add the public benchmark link if the posting platform permits it.

## Entry form values

- **Track:** The Pitch / Track F
- **Project:** final Vizard Agent project created from the one-brief prompt
- **Film:** final Agent render, at least 30 seconds
- **Public post:** public tagged post containing both required hashtags
- **Team:** solo unless the authorized entrant deliberately selects and verifies a team before submission

## Final acceptance checklist

- [ ] Entrant is eligible and has reviewed the current official rules.
- [ ] Core generation and editing happened inside Vizard Agent.
- [ ] Final film is at least 30 seconds.
- [ ] Film uses only the permitted public benchmark facts.
- [ ] “Synthetic/offline” is visible or audible.
- [ ] Candidate reads 6/6; baseline reads 3/6.
- [ ] Recoveries read 3/3; unsafe promotions read 0.
- [ ] Commands match the public benchmark README.
- [ ] Code and numbers are readable on a phone.
- [ ] Every visual, audio asset, likeness, and brand use is cleared.
- [ ] No private/internal material appears.
- [ ] Public post contains **#OneBriefOneVideo** and **#VizardAgent** and tags the official Vizard account.
- [ ] Public post is actually public.
- [ ] Final intended cut is selected; submissions are final.
- [ ] Vizard Agent project will remain intact for six months.
- [ ] No engagement buying or manipulation.
- [ ] Film, public post, and entry form are submitted before **2026-10-07 07:59 EDT**.

## Human/account gate

An eligible authorized entrant must sign in to Vizard, review and accept the official rules, spend the entrant account's own credits if required, generate and inspect the film, clear all rights, publish the tagged post, and submit the final form. Do not claim submission, acceptance, award, or payment without organizer receipts.
