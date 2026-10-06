# Provide the SEP-31 fields with their component's local form context

The mounted Sep31PaymentFlow creates a local useForm result, watches its values and uses its handleSubmit callback. Its six shared FormField children obtain registration and errors from useFormContext. The complete component does not provide its local form result to those children.

This is an **uncompiled source proposal** to pass that same local result through FormProvider. Every existing quote, payment, history, effect, validation-gating and JSX body remains exact. No payment or other application operation was performed.

## Actual source and caller

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).
Immutable donor: `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete acquired source | Git blob identity | UTF-8 bytes | Qualification |
| --- | --- | ---: | --- |
| `src/app/[locale]/send-payment/page.tsx` | `390ab4f17dd7a0461e26c3e77e8a310b962bc658` | 1,201 | Retained tree pin, native blob and independent hash matched |
| `src/components/Sep31PaymentFlow.tsx` | `52907a4ab7e7577f74d792d5375cf3cb2c9b73c5` | 16,658 | Complete source at immutable contents URL; independent derived identity, no separate native SHA field |
| `src/components/ui/FormField.tsx` | `b33a9c042b16d6284019a34a1225bed4947a8756` | 7,473 | Exact retained pin reacquired for this new consumer after cache loss, native/independent identity matched |

The actual send-payment App Router page dynamically imports the named Sep31PaymentFlow with ssr:false and renders it without props. The complete child calls useForm<Sep31PaymentFlowForm> once with its current zodResolver, onChange mode and six empty-string defaults. It renders FormField for transferServer, amount, receiverId, sourceAsset, destAsset and jwt. The complete shared FormField destructures register and formState.errors from useFormContext, then registers its input by name.

This establishes the local producer/consumer mismatch. There is no provider carrying this component's useForm result anywhere in its returned JSX. The proposal does not depend on assuming that every possible outer layout lacks every form provider; an unrelated outer form would still not carry this component's local result.

## History and ownership

The native current source path-history page returned christabel888's relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`. This is observed history, not a claim of original authorship for every line. Dedicated upstream and Commons PR queries for Sep31PaymentFlow plus FormProvider and the matching public Slack query returned zero. These are bounded overlap checks, not global absence guarantees.

The earlier [calculator context proposal, Commons #32113](https://github.com/woahwhattheheck/commons/pull/32113), concerns a different production module. Its completion is preserved and was not revalidated. This new packet is based on the actual send-payment page and complete Sep31PaymentFlow/shared-field source. No maintainer assignment, reward eligibility, source PR acceptance or upstream submission is asserted.

## Exact proposal

`provide-sep31-form-context.patch` is **+15/-11 across five hunks in one production file**.

| Source identity | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Before | `52907a4ab7e7577f74d792d5375cf3cb2c9b73c5` | 16,658 |
| After | `1e1caa1995d9b54d74848ad5d7b72d7e10dc9781` | 16,780 |

The patch imports FormProvider from the existing react-hook-form dependency, retains the full useForm return as methods, and destructures exactly the prior members from that result. The existing JSX is assigned to a local paymentFlow element value and returned as the provider's child. This preserves the entire JSX body without a large indentation-only rewrite. It adds no HTML form, submit action, second form instance, new validation call or altered field.

The complete watch/effect/callback block from the first watch through statusColor remains byte-for-byte exact. So does the entire JSX body: fields, buttons, handlers, disabled predicates, feedback, quote and transaction rendering. The useForm option object and the single call are unchanged. Existing imports/bindings that may be unused remain outside this correction.

## Dependency and documentation limits

Retained root manifest/lock facts identify package `2b1c6ac1f83096666c7fd6d5ba3fd22780e6b8eb` / 3,119 bytes and lock `7ecba249d1b7cd41e629e2fff2782ed6805186f5` / 359,885 bytes. They declare/resolve react-hook-form 7.79.0, @hookform/resolvers 5.2.2 and zod 4.4.3; the resolver's declared RHF peer is ^7.55.0, and the lock associates RHF with React 19.2.7. These are transferred declared/locked facts, not installed or executed dependencies.

Two earlier exact primary routes, https://react-hook-form.com/docs/formprovider and https://react-hook-form.com/docs/useformcontext, returned 403 Forbidden and remain held. They were not retried, and no alternate documentation or package-source route was acquired to recover them. No successful primary FormProvider API or installed implementation verification is claimed.

The proposal uses the conventional provider/context pairing indicated by the actual local import/use contract and the declared library. It is deliberately published with that source-only uncertainty, as was the distinct calculator proposal. It is not a successful typecheck, runtime proof, library implementation audit or whole-payment-flow readiness verdict.

## Validation and unchanged boundaries

Native and independently computed identities matched the pinned route and shared-field sources; the component's independent identity is distinguished from a separately returned native SHA. The serialized patch reconstructs the full postimage, and its inverse reconstructs the full preimage. Pure source comparisons confirmed one unchanged useForm call/options object, the exact handler/effect block and the exact entire JSX body.

No application, compiler, typecheck, build, fixture, test, browser, wallet, auth, token, account, quote request, transaction construction, signature, payment submission, history load or API operation was invoked. No credentials or user financial data were acquired. The component's source includes an optional JWT field, but no actual JWT value was read or generated.

This patch does not change preset-anchor/default selection, dirty/valid gating, setValue options, quote freshness/identity, transaction status classification, request lifetime, concurrent requests, schema assumptions, amounts, assets, endpoint selection or payment authorization. It does not certify any of those behaviors. Existing PocketPay/SDK payment holds are unrelated and remain untouched.

The retained complete donor tree has no AGENTS/RULES paths. Known contribution guidance is EventSource-specific tests/npm release workflow, outside this authorized source-only scope. Three differently attributed documentation MIT notices do not establish whole-repository licensing. Only the minimal attributed patch and this original guide are published to Commons; completed work, ownership and all exact failed-route holds remain preserved.
