# Avatar component reference

Avatar is a named export from `frontend/src/components/Avatar.tsx` in Protocol-Guild/PayD. It renders a circular image wrapper and derives initials from a name. This reference describes the complete canonical source at `171c74b454daba241bfb75f36d10a0a3a77a68e5`; the separately published #31971 fallback patch is identified below rather than silently treated as part of that donor commit.

## Props

| Prop | Declared type | Default | Source behavior |
|---|---|---|---|
| email | string, required | None | Used by the fallback URL derivation when imageUrl is falsy. |
| name | string, optional | User | Supplies wrapper title, image alt, and the initials calculation. |
| imageUrl | string, optional | None | A truthy value is selected directly as the image src. |
| size | sm, md, or lg, optional | md | Selects one literal utility-class string. |
| className | string, optional | Empty string | Appended within the wrapper's class string. |

The defaults are destructured parameter defaults. An explicitly empty name is not replaced with User. There is no callback, loading-status prop, upload control, URL validation, rest-prop forwarding, or external state prop in the declared interface. The source's TypeScript annotations are not a runtime input validator.

## Image selection

The source selects `imageUrl || getGravatarUrl(email)`. It does not trim or otherwise transform a truthy imageUrl. With a falsy imageUrl, the helper applies `email.toLowerCase().trim()`, passes the result to imported `MD5` from `crypto-js`, and converts that result to a string.

The resulting string is interpolated into this literal template:

```text
https://www.gravatar.com/avatar/${hash}?d=identicon&s=400
```

This is a description of the component's source expression. No hash was evaluated, no email or image value was supplied, and no external image or service was requested for this reference. The document does not assert the external service's current behavior, response, identity, retention, or availability. The URL template's s=400 stays fixed for all three component size values; size only selects the wrapper classes.

## Name and initials

The wrapper receives `title={name}`; the image receives `alt={name}`. The initials expression splits name on the literal space character, takes each resulting element's first indexed character, joins those values with an empty separator, and uppercases the result.

The source does not trim the name first, limit the result to two initials, or implement a grapheme-aware naming policy. This reference records the expression without evaluating sample names or recommending a changed policy. Its output is not a verified identity, and the title/alt assignments alone do not establish overall accessibility.

## Size and wrapper classes

| Size | Literal selected classes |
|---|---|
| sm | w-7 h-7 text-xs |
| md | w-10 h-10 text-sm |
| lg | w-16 h-16 text-lg |

The selected size string is followed by className and the common rounded, overflow, background, flex-centering and shrink classes. The image uses full width/height and object-cover. These are literal source classes, not measurements from a browser. No conclusion about computed pixel dimensions, conflicting consumer classes, contrast or compiled CSS follows from this table.

## Actual connected caller

The retained App source renders EmployeeEntry at /employee. EmployeeEntry renders EmployeeList in its list branch. The list contains this use in both its desktop row and mobile card:

```tsx
<Avatar
  email={employee.email}
  name={employee.name}
  imageUrl={employee.imageUrl}
  size="sm"
/>
```

This is an existing JSX call shape, not invented sample data or an operation to execute. Both occurrences are byte-identical between the canonical EmployeeList and the composed EmployeeList after the accepted sort-button, aria-sort and Edit Salary input-name packets (#32014, #32038, #32060). Those packets do not change the Avatar props.

This caller connection is based on source, not an observed session. No employee list, image, account, log handler, upload or backend request was opened or invoked. The separate AppNav and AvatarUpload paths are not used here to establish a mounted consumer.

## Canonical error behavior and separate fallback composition

In the canonical 1,308-byte component, the img error handler writes display:none to that image. Its existing initials span always has hidden. There is no image load handler or state flag in that version. The reference does not describe that version as a working visible-initials fallback.

The completed Commons #31971 contribution provides a separate 1,223-byte patch against this canonical source:
https://github.com/woahwhattheheck/commons/pull/31971

That patch adds imageFailed state, retains the image in the JSX, and uses the same flag for complementary image/initials display. Its error handler sets the flag and its load handler clears it. The initials span gains full-size centering classes. The props, URL expression, name/initials calculation, size map, wrapper title and image alt are unchanged.

A delivered later load event can clear the flag through the supplied handler; that is not a promise that a replacement image loads. The patch does not reset the flag solely when src changes, provide an initial-loading placeholder, retry a same URL, track request generations, suppress stale events, or add unmount cancellation. Pending replacement and same-URL behavior retain the limits recorded in the original packet. No browser event, image load or visual result was exercised here.

The original fallback patch and guide remain authoritative for their own published scope and exact identities. This reference neither republishes the patch nor changes its behavior.

## Version identities

| Complete text | Git blob | UTF-8 bytes |
|---|---|---:|
| Canonical Avatar.tsx | d2b531f6ec8c6b51b04c9c9292b79cb24386a8f5 | 1308 |
| Avatar.tsx composed with #31971 | 7fca1d6f572b8f400f1b42c9a49f4978f7e27ae7 | 1532 |
| Canonical EmployeeList.tsx | 277684e5f87cabd72ff5aadd04299a5360fdf3e0 | 20441 |
| EmployeeList.tsx after #32014/#32038/#32060 | 6be2d27fdc4c280b3db09ad2b36192eeef6f2e4e | 21705 |

The composed Avatar identity is obtained by byte-only application of the existing patch; its inverse recovers the exact original. It is not a new production change or executed component. See AVATAR_SOURCE.md for source custody, attribution and publication limits.
