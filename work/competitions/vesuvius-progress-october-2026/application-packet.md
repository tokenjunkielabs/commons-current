# Vesuvius Challenge — October 2026 Progress Prize application packet

Status: **ready for entrant review; not submitted**  
Evidence freeze: **2026-10-06 UTC**  
Current deadline recorded from the live October form: **2026-10-31 11:59 p.m. Pacific**

This packet binds the application narrative to the accepted source and the successful public-data UI evidence. It does not establish applicant eligibility, accept terms, upload anything, or submit the prize form.

## Canonical contribution

- Sponsor repository: [ScrollPrize/villa](https://github.com/ScrollPrize/villa)
- Merged sponsor PR: [#1849 — VC3D: support UNC paths in Attach Segments browser](https://github.com/ScrollPrize/villa/pull/1849)
- Sponsor baseline: `c4902849470a2e4005c8492120007280f087d636`
- Accepted contribution head: `da0a0c378cf2089debda2b3f3c324dccdb1f300b`
- Sponsor merge commit: `0f7be4a4c9e449caad35537011502cc7ab7bc6fe`
- Original submission owner: GitHub user `woahwhattheheck`

The merged fix replaces manual `file://` slicing and concatenation with Qt's native local-file URI conversion. That preserves a UNC host authority such as `//wsl.localhost/Ubuntu/...`, accepts Windows-native typed separators, and normalizes local navigation without flattening network paths.

## Reproducible evidence

### Source-equivalent Windows regression

[Workflow run 35534398783](https://github.com/woahwhattheheck/villa/actions/runs/35534398783) checked out source whose four changed blobs match accepted PR #1849. Its Windows Server 2025 / Qt 6.11.1 evidence reports:

- selected CTest: 1/1 passed;
- direct QtTest: 14 passed, 0 failed, 0 skipped;
- coverage includes UNC-authority preservation and Windows-native typed paths.

This is source-equivalent regression evidence. It is not the public-scroll UI demonstration.

### Public-data before/after UI evidence

- Evidence implementation commit: [`815ba9141113ce0e4a247f230dc0b349f5a87c55`](https://github.com/woahwhattheheck/villa/commit/815ba9141113ce0e4a247f230dc0b349f5a87c55)
- Successful workflow: [run 37376072127](https://github.com/woahwhattheheck/villa/actions/runs/37376072127)
- Successful job: [111985118562](https://github.com/woahwhattheheck/villa/actions/runs/37376072127/job/111985118562)
- Retained artifact: [villa1849-public-unc-evidence-37376072127](https://github.com/woahwhattheheck/villa/actions/runs/37376072127/artifacts/11371777303)
- Artifact digest: `sha256:ca00ac3e3322f078863f43df58ac404f256ac560a9edb2b449aec4fa8c3e01f6`
- Artifact expiry: 2027-01-03

Input is the public PHercParis4 `outer_shell` segmentation directory. The artifact records the exact path:

```text
//localhost/D$/a/_temp/villa1849-public-unc/public-data/PHercParis4/outer_shell
```

The baseline result is `visible_path_error`: the unpatched application displays "No such path" and leaves the empty project unchanged.

The accepted result is `attached_with_visible_segmentation_directory`: the patched application persists the public segment `s1_2um_outer` and matching output path, and the unobscured Volume Package manager visibly displays `Segmentation Directory: outer_shell`.

Truth boundary: the evidence does **not** claim a visible selected surface row. The artifact records `surface_row_exposed=false` and zero volumes. The contribution fixes path handling and segment registration; it does not prove surface rendering or ink detection.

## Ready-to-paste application narrative

### What problem did the contribution solve?

VC3D's Attach Segments local browser manually removed and rebuilt `file://` prefixes. On Windows this flattened the authority in UNC-style paths, including the network path used to expose public scroll data from the test environment. A valid path such as `file://localhost/D$/...` therefore became a different local path and failed with "No such path."

### What changed?

The merged contribution delegates local file-URI conversion to Qt:

- `QUrl::fromLocalFile()` creates platform-correct file URIs;
- `QUrl::toLocalFile()` preserves UNC authorities;
- `QDir::fromNativeSeparators()` normalizes pasted Windows paths;
- root-aware trailing-separator handling avoids damaging filesystem roots;
- focused Windows-path regressions cover the repaired behavior.

This is a narrow integration fix in the existing VC3D Attach Segments flow, not a new file browser or data format.

### Which scroll data was used?

The public PHercParis4 spiral-dataset `outer_shell` segmentation was used. The test consumed its `meta.json` and TIFF coordinate files through an actual UNC path and exercised the VC3D Attach Segments UI against the baseline and accepted builds.

Dataset context:

- [Vesuvius Challenge datasets](https://scrollprize.org/data_datasets)
- [PHercParis4 outer_shell directory](https://dl.ash2txt.org/datasets/spiral_datasets/PHercParis4/outer_shell/)

### What was the demonstrated before/after result?

Before the merge, VC3D showed "No such path" for the identical public-data UNC URI and retained no segment in the empty project.

With the accepted contribution, VC3D persisted exactly one PHercParis4 `outer_shell` segment and its output path. The Volume Package manager visibly reported `Segmentation Directory: outer_shell`. The evidence run completed successfully and retained the screenshots, UI metadata, result JSON, and exact input/path identities in the linked artifact.

### How does this raise the odds of reading the scrolls?

The fix removes a Windows interoperability failure at the point where a researcher attaches segmentation data to VC3D. Researchers who keep Vesuvius data in WSL, a local file share, or another UNC-addressed location can use the normal Attach Segments workflow without copying the dataset to a different local path or manually rewriting the URI. That makes public segmentations easier to load into the visualization and annotation tool used for downstream scroll analysis.

Bound the claim to workflow access and reproducibility. Do not claim that this change improves segmentation accuracy, surface extraction, ink detection, or text recovery.

### Why is the contribution useful to the community?

- It is merged into the sponsor's public VC3D repository.
- It uses Qt's maintained platform path primitives rather than a special-case path rewrite.
- It adds focused regression coverage for the exact Windows/UNC boundary.
- It preserves the existing URI and native-path interfaces.
- The public-data UI demonstration is replayable from a pinned source commit, workflow run, and retained artifact.

## Entrant checklist

Complete these steps manually through the authorized entrant/account surface:

- [ ] Re-open the [official Progress Prize rules](https://scrollprize.org/prizes#progress-prizes) and current [October form](https://docs.google.com/forms/d/e/1FAIpQLSc4flEfgK2nyjoczz2_U_XrIGMlgrnSknWatLqrFPnbtKfZwg/viewform) immediately before submission.
- [ ] Fill the entrant-controlled applicant, team, contribution-rights, and terms fields through the authorized account.
- [ ] Confirm that the form still shows the October 31, 2026 11:59 p.m. Pacific cutoff.
- [ ] Download the retained artifact before its 2027-01-03 expiry.
- [ ] Select the clearest baseline-error and accepted Volume Package screenshots from the artifact.
- [ ] Preserve the `surface_row_exposed=false` limitation in any caption or answer.
- [ ] Paste only the verified narrative above; do not include closed/unmerged PRs #1851 or #1854.
- [ ] Submit the form once.
- [ ] Retain the form provider receipt, submission timestamp, applicant identity, and any confirmation email or status page.
- [ ] Record later sponsor status separately as submitted, accepted, awarded, payout pending, or received.

## Money state

- Advertised: **$20,000** for the guaranteed monthly best Progress Prize submission.
- Proposed: **$0**
- Independently verified funded for this specific entry: **$0**
- Awarded: **$0**
- Invoiced: **$0**
- Received: **$0**

A merged contribution and an application-ready evidence packet are not a prize submission or a receivable.
