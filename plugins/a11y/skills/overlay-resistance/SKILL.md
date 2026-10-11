---
name: overlay-resistance
description: Guides source remediation instead of treating accessibility overlay widgets as evidence of WCAG conformance. Use when reviewing overlay scripts, evaluating automated-compliance claims, or proposing a quick accessibility fix; distinguishes product-specific evidence from project policy.
---

# Overlay Resistance

Project policy: recommend durable fixes in the application's HTML, CSS, JavaScript, content, and task flows. Do not recommend a third-party overlay as a substitute for remediation or evaluation. This policy follows WAI's warning that automated tools cannot determine accessibility on their own; it is not a claim that JavaScript cannot improve accessibility. ([WAI evaluation tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/))

## Evaluate the claim and the behavior

Separate an accessibility preference control from a promise of automated conformance. A user-controlled text-size or contrast option is not inherently an overlay-compliance claim. Inspect what a script actually changes, when it loads, which states it reaches, and whether the application's source remains maintained.

Runtime DOM changes can update semantics and accessibility APIs. The accessibility tree is not an immutable raw-HTML snapshot made before JavaScript. ARIA does not automatically supply the required interaction behavior. ([Core AAM, change events](https://www.w3.org/TR/core-aam-1.2/#mapping_events_state-change), [WAI-ARIA, author guidance](https://www.w3.org/TR/wai-aria-1.2/#managingfocus_authors))

Do not use an invented percentage of automated detection coverage. Tools can identify some problems and miss others; scope and human judgment matter. Do not generalize one vendor's test or legal case to every product. ([WAI evaluation tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/))

## Inspect installation before changing it

1. Inventory scripts, package dependencies, injected controls, DOM changes, and the critical flows they affect.
2. Treat vendor-like domains/classes as leads, not proof. Confirm the script's purpose and behavior in the application.
3. Reproduce specific barriers with keyboard, zoom, and supported assistive technology; record results actually observed.
4. Identify source fixes, then plan removal/replacement within the authorized change. Compare behavior before/after and preserve legitimate user preferences.

See [detection workflow](references/detection-patterns.md). Code inspection is not an executed browser or assistive technology test.

## Use specific evidence

On April 22, 2025, the FTC announced a final consent order requiring **accessiBe** to pay $1 million over deceptive or unsubstantiated compliance claims and endorsement practices. This is a dated case involving named parties, not a finding against every overlay vendor or a guarantee about a website's legal outcome. ([FTC final order announcement](https://www.ftc.gov/news-events/news/press-releases/2025/04/ftc-approves-final-order-requiring-accessibe-pay-1-million))

Consult [evidence and limits](references/overlay-evidence.md) when explaining this policy. Avoid unsourced lawsuit counts, universal performance claims, or assurances that installing/removing a script resolves legal exposure.

## Make the remediation concrete

Prefer a maintained component fix over an opaque global patch. Example: replace a placeholder-only field with an associated persistent label and hint, then test the entire form. ([WAI labels](https://www.w3.org/WAI/tutorials/forms/labels/))

```html
<label for="email">Email address</label>
<p id="email-hint">For example, name@example.com</p>
<input id="email" name="email" type="email" aria-describedby="email-hint">
```

Use `form-a11y`, `focus-management`, `alt-text-quality`, and `testing-strategy` for the corresponding fixes. Add regression checks plus manual task evaluation; report open coverage and evidence rather than a compliance score. ([WAI evaluation tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/))

## Respond to quick-fix requests

Explain the observed barrier and provide a small, testable remediation: “The email field lacks a persistent associated label. Add the label in the form component, verify error association, and test submission with keyboard and the supported screen reader.” Avoid a blanket technical claim that no runtime repair is possible.

Read [common mistakes](references/common-mistakes.md) and [source provenance](references/sources.yaml).
