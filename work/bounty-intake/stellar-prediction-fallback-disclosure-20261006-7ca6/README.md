# Explain the prediction page's simulation fallback

The mounted prediction page presents payment-success probabilities, confidence ranges, risk recommendations and alternative routes. Its actual API helper catches a failed backend prediction and returns locally generated simulated results, with no result-source discriminator. The existing page gives the reader no explanation of that fallback.

This narrow continuation adds one paragraph beside the page heading: if the backend prediction cannot be completed, results are simulated locally, and the time-of-day input affects only simulated results. It changes no prediction, threshold, request, recommendation or financial assumption.

## Canonical source and attribution

Repository: [Stellar-Analysis/frontend](https://github.com/Stellar-Analysis/frontend).
Immutable source commit: `482ee456369418ef82c4056718cb82d3468f762b`.

| Complete acquired input | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| `src/app/[locale]/prediction/page.tsx` | `3830ebab4cb7b9f1bde09ff6cf0e88ccc046795c` | 159 |
| `src/components/prediction/prediction-form.tsx` | `ff35f630bd0fa92771180471ce096125a8816c00` | 19,198 |
| `src/lib/api/api.ts` | `1af4d71a9127deb5186f016718483dbab088f414` | 7,998 |

The App Router page imports and directly renders PredictionForm. The form imports getPaymentPrediction from the acquired API module and awaits it in its submit handler. The API body was already retained as input to earlier, separate HealthDashboard work; this continuation uses that real body for the new prediction consumer, without replaying completed source checks or invoking the API.

A current native path-history page returned the repository-flattening commit `59fad72d9fbef9cfd6f47e215392da44488fcdc4`, attributed to christabel888. That relocation does not establish original authorship of every line. The existing contributor source and ownership are preserved; this patch is not an upstream submission, issue assignment, reward or acceptance claim. No external source PR was established for this current-main copy defect.

Dedicated current Commons PR search for PredictionForm plus simulation, upstream repository PR search for prediction plus fallback, and a public Slack search for PredictionForm plus simulation each returned zero results. These are bounded overlap checks, not exhaustive absence claims.

## Actual producer and consumer contract

getPaymentPrediction requests `/ml/predict` with the source/destination corridor and amount_usd. Its successful branch transforms the backend success probability, confidence, risk level, recommendation and model version into the frontend response shape. That request does not send the form's time_of_day value.

The catch branch calls generateMockPrediction. This local generator uses fixed corridor probabilities, random values for corridors not in that fixed map, an amount adjustment and a time-of-day adjustment. It constructs the interval, risk category, recommendation and alternatives locally and returns the literal model version 1.0.0. The acquired form then renders those returned fields in the same results panel used for backend responses.

The new paragraph explains these two observed source facts. It does not imply that every response is simulated, that a displayed response has been individually classified, or that the returned probabilities are validated. It does not recast the existing confidence interval as statistically calibrated, certify a model, or make a recommendation to send funds.

## Exact source change

`describe-prediction-fallback.patch` is **+4/-0 in one hunk**, modifying only `src/components/prediction/prediction-form.tsx`.

| Source identity | Git blob | UTF-8 bytes |
| --- | --- | ---: |
| Before | `ff35f630bd0fa92771180471ce096125a8816c00` | 19,198 |
| After | `a396a44caa14a9d300914c6365ea8ae768a1f0c6` | 19,438 |

It adds one ordinary text paragraph under the existing heading description. Removing that exact insertion reconstructs every original byte. All controls, their associations, defaults, event handlers, loading/error transitions, numeric conversions, API calls, fallback policy, chart calculations, labels, recommendations and result markup remain as acquired. No translation infrastructure or new per-result field is introduced.

The paragraph is an explanation of existing application behavior. It does not solve the absence of a per-result backend-versus-simulation marker. That larger API/consumer change remains outside this packet. The current heuristic values, literal fallback model version, error classification and prediction reliability remain unchanged and unverified.

## Source validation and limits

Independent UTF-8 counts and Git blob identities matched each complete input. The serialized patch reconstructs the entire postimage, and its inverse reconstructs the entire preimage. The source-preservation check also removes only the inserted paragraph and obtains the exact original body.

No browser, prediction request, payment, wallet, account, model, fixture, test, build or application runtime was used. No actual result, user input or financial data was acquired. This is source reasoning and text reconstruction only, not a whole-build, accessibility, model-quality or live-service verdict.

The retained complete donor tree contains no AGENTS/RULES paths. The known contribution document is EventSource-specific release guidance; the authorized source-only scope excludes its test/npm workflow. Three differently attributed documentation MIT notices do not establish whole-repository licensing. Accordingly, this Commons continuation publishes only the minimal attributed patch and this original explanation, not the full source module. Other completed frontend packets and all exact failed-route holds remain unchanged.
