# Keep an unwired contact form from claiming delivery

The current contact form has no delivery operation. Its complete submit handler only prevents native submission, displays a sending state, waits 1,600 ms and then displays “Message Sent” with a promised reply. Those states report an outcome that the source never performs.

This patch gives the form an explicit unavailable state: a localized explanation, a disabled submit button, and a handler that continues to prevent default submission. The listed contact channels and the controlled field values remain available and unchanged.

## Actual source and localized composition

Canonical donor: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend), immutable commit `482ee456369418ef82c4056718cb82d3468f762b`.

The complete App Router entry `src/app/[locale]/contact/page.tsx` is blob `8dc4061d68085c095ecca08fb00b541a3b4f3822`, 7,835 UTF-8 bytes. It is the actual mounted route, not an unconnected component. Its handleSubmit makes no fetch, service or other delivery call. Its only await is a timeout.

The complete locale loader `src/i18n/request.ts`, blob `8af4c1d67b6814b5f5ea577a1eb6d1839a208015`, 458 B, selects the configured en/es/zh locale and imports messages from that locale's JSON resource. The actual route reads the contact namespace. Complete resources were already acquired for the distinct dashboard disclosure task and are reused as inputs here; no provider/source replay was performed.

The resource preimages below include the completed #32063 dashboard.dataNotice addition. That key and every other non-contact resource value remain exact. No earlier dashboard patch is replaced.

| Source path | Patch preimage Git blob / bytes | Postimage Git blob / bytes |
| --- | --- | --- |
| `src/app/[locale]/contact/page.tsx` | `8dc4061d68085c095ecca08fb00b541a3b4f3822` / 7,835 | `e3f982c4a053cdda0bf9ce878d1dbab834202d30` / 6,609 |
| `messages/en.json` | `528c489e465ec4827ca563368fae71e488ba05cb` / 7,968 | `e747de7fd55e09ac4ed8dcc3e99d8f7d0988df80` / 8,201 |
| `messages/es.json` | `d4fe7836ad5d92e0a4d2b0a73a9b7dc3541f2969` / 7,309 | `541a4c64c0620744be42e65dc1c28b706e8e970d` / 7,562 |
| `messages/zh.json` | `8235f8898a87130daecf74d9d17e7a2413301bfa` / 6,099 | `8bea9fa8286a2f95d753c0a6e875374895d7afb1` / 6,274 |

Original donor resource identities before #32063 were en `d714ba710db0e7287bf81d3ebfd00cbe8292ef88` / 7,724 B; es `eeeb6e815a966037e0c7bbac524438bf423f8aa8` / 6,988 B; and zh `f37d511ba8aa41c7d6e1f17129856aa92537d8c4` / 5,885 B. Apply this incremental patch after the dashboard disclosure resource patch. The contact route itself uses its donor preimage.

## Coherent unavailable-state change

`show-contact-form-unavailable.patch` changes **+11/-40 in eight hunks across four source files**.

* Remove the synthetic sending/sent state, timeout and success/reset view, along with their unused type and icons.
* Retain the submit handler's preventDefault so keyboard/native form submission cannot navigate or send through the browser's default form behavior.
* Disable the existing submit button and show a localized “Form unavailable” label.
* Add an explanation before the fields that the form is not connected to delivery and will not send the message.
* Update each locale's subtitle to direct the user to the already listed contact channels instead of inviting submission through the form.

The existing name/email/subject/message fields, labels, validation attributes, values, onChange callback, option values and input styles remain byte-for-byte exact. Fields remain editable as local component state. No data is submitted, persisted, copied, discarded by a success reset or moved into a new service.

All channel destinations, visible addresses, external-link attributes, channel hints and their render loop remain unchanged. This patch does not establish that those destinations are operated, reachable or subject to their existing response-time hints. None was opened or contacted.

The now-unrendered legacy sending/success translation keys are retained for compatibility; the route no longer renders them. Only contact.subtitle changes, and contact.form.unavailable plus contact.form.unavailableButton are added in en/es/zh. Parsed-resource comparison confirms every other existing key/value remains unchanged.

## Validation and limits

Every serialized file patch reconstructs its complete postimage, and every inverse reconstructs its complete preimage. Independent UTF-8 byte counts and Git blob identities match. Retained-string guards confirm exact fields/channel configuration, disabled submit, the preventDefault handler, absence of the synthetic timer/state and preserved dashboard disclosure.

No JSX/application compiler, browser, timer, form submission, contact channel, email, user input, storage, fixture or test was executed. This is not a delivery integration or a claim of full UI, accessibility, translation or build acceptance. The existing form layout remains; removing the synthetic confirmation naturally removes that screen and its reset action.

## Attribution and authority

Bounded current-path history returned relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4` by `christabel888`; original contributors retain their rights and no sole-author claim is inferred. A repository-specific Commons PR query for ContactPage returned zero with incomplete_results false, and the public Slack query returned zero. These are bounded overlap results, not a global absence claim.

The complete donor tree had no root AGENTS/RULES path. EventSource-specific contribution/release instructions do not override the explicit no-tests/no-runtime/no-upstream scope. Differently attributed documentation MIT notices do not establish whole-frontend licensing. This packet publishes only a minimal patch and original attributed guide.

No upstream branch, PR, comment, maintainer assignment, sponsor acceptance, bounty/payment, contact action or whole-issue completion is performed or claimed.
