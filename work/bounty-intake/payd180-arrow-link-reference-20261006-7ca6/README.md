# PayD180: ArrowLink source reference

This packet adds an immediately readable reference for one actual custom frontend component: ArrowLink. It documents props, rendering branches, real mounted usage, static examples, styling and accessibility considerations. ARROW_LINK.md is the deliverable; a possible future upstream location is docs/components/ArrowLink.md, which is absent from the complete retained donor tree. No upstream file is created by this Commons packet.

## Qualified source map

Canonical donor: Protocol-Guild/PayD@171c74b454daba241bfb75f36d10a0a3a77a68e5.

| Path | Git blob | UTF-8 bytes | Acquisition/use |
| --- | --- | ---: | --- |
| frontend/src/components/ArrowLink.tsx | 2b65d3119f48bc056eab0a0462433ca109078b0d | 1294 | Full new immutable component read |
| frontend/src/pages/Home.tsx | 4440a792e577a1f82deafa5225410c849a53fd74 | 2983 | Full new immutable production caller read |
| frontend/src/index.css | 91a759763e2d95a56274460685978f2a024c3b53 | 8054 | Full new immutable stylesheet read |
| frontend/src/App.tsx | acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c | 6460 | Previously acquired complete retained canonical caller |
| frontend/src/main.tsx | f84f187971ba135010c48e69fda10f0c0f71ebd9 | 1664 | Previously retained complete entry bytes, reused by exact canonical-tree blob identity |
| LICENSE | 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64 | 11357 | Exact retained Apache-2.0 file |

The complete retained canonical tree contains 753 entries, reports no truncation, and binds these paths and blobs to the donor. The entry bytes were originally requested at another pinned donor ref, not newly read from canonical main; identity with the canonical tree is the precise reuse basis. Component, Home and CSS returned native blobs equal independently computed hashes of their complete UTF-8 contents.

A bounded code search for ArrowLink returned two path matches and incomplete_results=false: its definition and Home.tsx. That is the actual returned search result, not a future or repository-wide usage guarantee. Full Home, App and entry source establish the chain BrowserRouter → App / route → Home → ArrowLink. Only the to mode is used in that acquired production caller. Documentation of href and onClick is tied to the full exported component source instead of an invented production caller.

## Issue and authorship boundary

The current repository-local backlog row for issue180 requests documentation for custom UI components, props, usage examples and accessibility considerations. A bounded all-state PR query for 180 with topn20 returned zero rows. Both returned issue comments were read: contributors asked to work on or be assigned the issue. Neither a contributor request nor the query result establishes assignment, ownership absence, completion acceptance or permission to alter an upstream branch.

This is a partial, narrowly scoped documentation contribution toward that request. It does not claim to document every button, modal, table or badge, create Storybook, establish a design-system policy, or complete issue180. The existing repository authors retain credit for ArrowLink, Home, App, styling and the surrounding application. No source implementation is reproduced as a new invention. The unchanged full upstream Apache-2.0 LICENSE is included; its exact blob is listed above.

The separate open ADR PR638 by guptakumarranjeet150 is preserved. Its acquired index/process documents yielded NO PATCH; their authored Accepted labels are not PR acceptance. No ADR or contributor branch is changed. Prior protected source families and exact held routes remain unchanged.

## Document construction and checks

ARROW_LINK.md distinguishes the typed union from truthy runtime branch selection, documents unsupported attribute forwarding, records the exact external-prefix behavior, and separates real Home snippets from unexecuted illustrative examples. It explains that the arrow is decorative while caller-supplied content must name the destination/action. CSS descriptions come from complete source rules and are not computed-style observations.

The component's source was not executed to produce this document. No handler, URL, route, wallet, account, payment, network request, environment value, application data, browser, compiler, build, test or fixture was used. The two example snippets are requested usage documentation; they are not synthetic test inputs. No source code, dependency, stylesheet, repository configuration or upstream issue is modified.

Primary native-element references were acquired during preparation and linked in the component document. Their use is limited to ordinary button/anchor semantics; no browser compatibility or full accessibility verdict is inferred. No accepted computation or completed source patch was replayed.

All three publication files are full retained strings with independently computed Git blob identities. The guarded Commons publisher compares complete immutable returned contents and metadata; a separate final named-main observation either qualifies an equality alias or requires all files at the observed immutable commit. Actual results are recorded only in the completion receipt after those checks.

Files:
- ARROW_LINK.md: the new component reference.
- README.md: this source, attribution and verification boundary.
- LICENSE: exact upstream Apache-2.0 file.
