# Evidence Cart — YouCam eCommerce readiness packet

Evidence Cart is a public-safe, dependency-free commerce decision core for the YouCam API Skin AI & eCommerce VTO Hackathon. It turns a provider-neutral skin observation into deterministic, explainable catalog suggestions and refuses to recommend when evidence is weak, no catalog item matches, or the provider fails.

This packet is an offline readiness artifact. It does **not** claim a live YouCam integration, medical diagnosis, competition entry, judging acceptance, or prize eligibility. The `Provider` protocol is an injection boundary; it deliberately does not invent an undocumented YouCam request or response shape. A registered entrant must implement and validate the live adapter from the authorized event documentation.

## Run the focused checks

From this directory:

```bash
python -m py_compile evidence_cart.py tests/test_evidence_cart.py
python -m unittest discover -s tests -v
python evidence_cart.py \
  --fixtures fixtures/cases.json \
  --catalog fixtures/catalog.json \
  --output benchmark-receipt.json
```

The five fixture journeys cover a grounded recommendation, low-quality input, zero catalog match, provider timeout, and malformed partial response. Three repeats per journey verify deterministic decision output. The receipt reports status coverage, grounding, latency plumbing, and an explicit raw-image exclusion flag; measured offline latency is not a live API performance claim.

## Integration contract

1. Obtain the user's explicit image-processing consent in the application UI.
2. Keep raw image bytes out of logs, benchmark fixtures, and receipts.
3. Implement `Provider.analyze(image_ref)` using only the authorized event API documentation and server-side credentials.
4. Map the validated live response into `face_detected`, `quality`, and `concerns[{name, confidence}]`.
5. Preserve the four result states: `ok`, `weak_evidence`, `zero_match`, and `provider_error`.
6. Render each `EvidenceCard.why` and provide a non-medical, user-visible uncertainty statement.

## Submission gates still requiring an authorized entrant

- join the event and accept its terms;
- obtain the included API units and event documentation;
- implement and test the real adapter without exposing credentials;
- build a coherent consumer/eCommerce UI around this core;
- capture the required screenshots and uninterrupted 1–3 minute functional demo on the target device;
- publish the runnable repository/instructions and submit through Devpost before the official deadline.

The current event listing advertises a competitive **$6,000 total cash pool**. This source packet has $0 proposed, promised, funded-to-us, awarded, invoiced, or received.
