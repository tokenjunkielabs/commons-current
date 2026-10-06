# PayD Avatar: show initials after an image error

The current Avatar component hides its image when loading fails, but its existing initials span always has the hidden class. The error path therefore leaves the avatar without either image or initials. This source correction uses one component state flag to select image or initials, and clears that flag when the still-mounted image reports a later successful load.

## Exact source and attribution

Donor repository: `Protocol-Guild/PayD`  
Observed main commit: `171c74b454daba241bfb75f36d10a0a3a77a68e5`  
Changed path: `frontend/src/components/Avatar.tsx`

This is a current-main source residual. The original repository authors retain attribution. A bounded all-state PR search for Avatar returned PR660 and the existing test contribution PR440. Current native metadata identifies PR660 as open/unmerged on SrvFernandes/PayD at `9533adfbac502c08737a3462db39be8c9ce5f049`; its complete sixteen-path diff metadata concerns a separate root workspace and does not modify this frontend Avatar path. No PR660 source body, PR440 test source or contributor branch was modified. This is a bounded overlap check, not a global absence or ownership claim.

| Complete source text | Git blob | UTF-8 bytes |
|---|---|---:|
| Original Avatar.tsx | `d2b531f6ec8c6b51b04c9c9292b79cb24386a8f5` | 1308 |
| Prepared Avatar.tsx | `7fca1d6f572b8f400f1b42c9a49f4978f7e27ae7` | 1532 |
| frontend/src/components/EmployeeList.tsx | `277684e5f87cabd72ff5aadd04299a5360fdf3e0` | 20441 |
| frontend/src/pages/EmployeeEntry.tsx | `b89a5c832191a19a52c4f7b99201da5ece9acef8` | 11774 |
| frontend/src/App.tsx | `acc3dfc6f6d5c04ccb1ab693b3a0d5735b81c10c` | 6460 |
| frontend/src/main.tsx | `f84f187971ba135010c48e69fda10f0c0f71ebd9` | 1664 |
| LICENSE | `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64` | 11357 |

The complete Avatar and list source strings matched native and independent Git identities. The retained complete entry, App, main and license texts were transferred for this new consumer and independently matched the current complete tree's exact path/blob entries. The original immutable license fetch supplied content without a native SHA field: its identity is request-bound plus independently measured, not an invented returned field.

## Connected display consumer

The acquired main entry renders App. App renders EmployeeEntry at `/employee`; EmployeeEntry renders EmployeeList. The list renders Avatar in its desktop row and mobile card, passing existing row email, name and optional image URL. That source connection establishes a mounted consumer without accessing any employee records, account, image resource or backend endpoint.

A separate acquired AppNav also references Avatar, but the current App uses EmployerLayout, whose acquired source does not mount that AppNav. This packet therefore does not rely on the mock navigation user or claim that navigation path is mounted. AvatarUpload remains separately unqualified as a mounted component. No caller module is changed.

## Focused change

An unconditional `useState(false)` supplies `imageFailed`. The existing image remains mounted, with its display controlled by that flag. Its error handler sets the flag; its load handler clears it. The initials span uses the same flag to choose flex or hidden and fills/centers within the existing wrapper.

The image URL choice, Gravatar URL/hash calculation, initials algorithm, input props/defaults, size mapping, wrapper title/class, image alt text and gradient colors remain unchanged. The component does not fetch, retry, clear or replace any URL itself.

Primary browser event documentation acquired for this correction:

- Resource failures, including images, produce the element error event: https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/error_event
- A successful resource load produces the load event, including for img elements: https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/load_event

The state flag makes the two visual branches complementary after these event handlers run. A later delivered load event restores image visibility and hides initials. This is conditional on delivery of the image event; it is not a promise that a replacement URL succeeds. While a replacement is pending after failure, the initials remain shown. The image is retained in the DOM, not conditionally unmounted.

## Verification and limits

The actual serialized patch has three hunks, thirty complete rows, nine insertions and five deletions. Independent forward materialization gives the exact 1,532-byte prepared component; inverse materialization recovers the exact 1,308-byte original. Unchanged source ranges match in full. This validation handles strings and patch structure, not React, CSS, an image or a synthetic event sequence.

No automatic same-URL retry, request-generation tracking, stale-event suppression, unmount cancellation or initial-loading placeholder is added. Empty/malformed names and the existing initials algorithm remain unchanged. No broader accessibility, contrast, pixel layout, installed dependency or full-build acceptance is claimed. There is no screen-reader/browser/screenshot evidence.

No user record, employee data, email value, image, Gravatar request, storage, upload, product API, network event, DOM/React runtime, compiler, test/fixture, upstream submission, sponsor, account or payment action was performed. The source correction concerns presentation only and changes no row actions or business handlers.

## Artifacts and license

`image-error-fallback.patch` modifies only the named Avatar source against the pinned main commit. This guide records the modification, author context and evidence limits. `LICENSE` is the full unchanged Apache-2.0 text. Retain original repository attribution and notices; no full donor module, caller or image is republished.
