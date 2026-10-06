# Connect calculator fields to the calculator's form context

The mounted CostCalculator creates a local React Hook Form instance, watches its values, validates it and submits through its handleSubmit. Its FormSelect, FormField, FormCheckboxGroup and FormCheckbox descendants instead obtain their methods from useFormContext. The calculator does not pass its local methods into a FormProvider, so those descendants are not connected to the form instance controlling the calculation.

This source proposal retains the complete useForm result as methods, destructures the same existing members from it, and wraps the existing form in FormProvider with those methods. It is an uncompiled source correction, with the dependency-documentation limit explicitly recorded below.

## Actual mounted source and attribution

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).
Immutable commit: `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete acquired input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/calculator/page.tsx` | `a66e97e0579bf1a04835493e402a56fa176015da` | 1,209 |
| `src/components/CostCalculator.tsx` | `02fcfb019d2b1a268e1279414ab7357c66eed7c3` | 12,042 |
| `src/components/ui/FormField.tsx` | `b33a9c042b16d6284019a34a1225bed4947a8756` | 7,473 |
| `src/lib/schemas.ts` | `e2a396eac77810eaeda5ed3a228653f9facbdb5f` | 4,342 |

The actual App Router page dynamically imports the named CostCalculator export with SSR disabled and renders it. The complete shared field module exports the exact components imported by the calculator. All four relevant descendants call useFormContext: text/select fields use its register and errors; checkbox fields use watch, setValue and errors; the group uses errors. Their props do not accept the calculator's register or control object.

The missing local provider is therefore a concrete connection defect. This guide does not assume that an unspecified outer provider would be the correct form; the proposal explicitly provides the calculator's own methods to its descendants.

Current native path history returned christabel888's repository relocation commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`. This is observed history attribution, not a claim of original authorship for every line. Dedicated upstream and Commons PR queries for CostCalculator plus FormProvider and a public Slack query with the same terms returned zero. These are bounded overlap checks, not global absence. No external carrier, maintainer assignment or upstream acceptance was established.

## Declared dependency context and documentation limit

Root transferred exact retained manifest and lock evidence from the same canonical commit:

| Source | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `package.json` | `2b1c6ac1f83096666c7fd6d5ba3fd22780e6b8eb` | 3,119 |
| `pnpm-lock.yaml` | `7ecba249d1b7cd41e629e2fff2782ed6805186f5` | 359,885 |

The manifest declares react-hook-form 7.79.0, @hookform/resolvers 5.2.2 and zod 4.4.3. The lock resolves React Hook Form with React 19.2.7, the same resolver/RHF versions and Zod 4.4.3; the resolver peer range is react-hook-form ^7.55.0. These are transferred declared/locked facts, not a newly acquired installed dependency or runtime result.

The proposal uses the conventional React Hook Form FormProvider/useFormContext pairing and passes the complete methods object instead of constructing a partial provider value. Direct primary documentation opens at https://react-hook-form.com/docs/formprovider and https://react-hook-form.com/docs/useformcontext both returned 403 Forbidden. Those exact routes remain held. No retry, alternate documentation route or dependency-source retrieval was used to recover them; no successful primary-documentation or library-implementation verification is claimed. Root and peer custody contained no prior successful primary contract passage. The proposed import and provider wiring were not typechecked or executed.

## Exact patch and preserved behavior

`provide-calculator-form-context.patch` is **+69/-65 in four hunks**, with most changed lines being indentation of the unchanged form inside its new provider. Only the React Hook Form import, retention/destructuring of the existing useForm return and the provider wrapper are functional changes.

| Source identity | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Before | `02fcfb019d2b1a268e1279414ab7357c66eed7c3` | 12,042 |
| After | `cbce6daa07c5d5277218d503a4abc660b89cd5e6` | 12,252 |

The resolver, onChange validation mode and complete defaultValues block remain exact. Every existing destructured member is retained. The form's element attributes, children, options, labels and control callbacks are unchanged after normalizing only the required indentation. The provider surrounds the existing form; the surrounding layout and error/result rendering remain outside and unchanged.

All watch calls, canSubmit conditions, amount conversion, route handling, handleCalculate request body, endpoint, error handling and result calculations remain exact. No currency, fee, slippage, precision, threshold, model or response-validation policy is introduced. The shared fields and schema files are input context only and are not modified.

Existing limitations remain. In particular, canSubmit still requires isDirty, and the acquired shared checkbox setter requests validation without explicitly requesting dirty-state updates. This packet does not claim that changing only route checkboxes enables a pristine form. Existing unused bindings/helper, request concurrency/lifecycle behavior, response casting and malformed-success handling are also unchanged. The correction is the local context connection, not whole-calculator readiness.

## Validation and publication boundaries

The serialized patch reconstructs the entire postimage, and its inverse reconstructs the entire preimage. Independent Git blob identities and byte counts match. Pure string checks establish that the complete options block, watch/handler logic and result suffix are unchanged, and that the nested form differs only by indentation. These are source checks, not application tests.

No estimate request, API operation, wallet, payment, account, browser, fixture, test, build, dependency install or application runtime was used. No actual user or financial data was acquired. No successful render, typecheck, installed API compatibility, financial correctness, device behavior or whole-repository acceptance is claimed.

The retained complete donor tree has no AGENTS/RULES paths. The known contribution document is EventSource-specific test/npm release guidance; the authorized source-only workflow excludes those commands. Three differently attributed documentation MIT notices do not establish repository-wide licensing. This Commons packet publishes only the attributed minimal patch and this original explanation, preserving existing contributor ownership and all failed-route holds. It is not an upstream submission or reward/assignment claim.
