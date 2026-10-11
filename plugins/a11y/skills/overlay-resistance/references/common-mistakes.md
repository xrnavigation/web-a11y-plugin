# Overlay evaluation mistakes and corrections

## Frozen-tree rationale

```js
// Wrong reasoning: this cannot work because AT only sees initial raw HTML.
field.setAttribute('aria-describedby', 'email-hint');
// Right project practice: put the association in the owned component,
// or update it deliberately, then inspect the runtime description and behavior.
```

Accessibility APIs support state/property updates. Evaluate actual semantics and interoperability; do not assert that JavaScript changes are categorically invisible. ([Core AAM change events](https://www.w3.org/TR/core-aam-1.2/#mapping_events_state-change))

## Global name patch without context

```js
// Wrong: all buttons get the same ambiguous name.
document.querySelectorAll('button').forEach(b => b.setAttribute('aria-label', 'Action'));
// Right project fix: define purpose at the source with visible native button text.
```

```html
<button type="button">Download annual report</button>
```

Visible words must be included in the accessible name. A global patch can overwrite useful labels; inspect the actual result. ([Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html))

## One enforcement action treated as an all-vendor finding

Wrong: “Every overlay company has been fined by the FTC.”

Right: “The FTC announced a final accessiBe consent order on April 22, 2025, requiring a $1 million payment over deceptive or unsubstantiated claims and endorsement practices.” Keep the named parties/date attached; do not extrapolate. ([FTC announcement](https://www.ftc.gov/news-events/news/press-releases/2025/04/ftc-approves-final-order-requiring-accessibe-pay-1-million))

## Opaque automation treated as conformance

Wrong: “A one-line script or green scan proves compliance.”

Right: “Fix maintained components, combine automated/manual evaluation, and record tested routes/states/input environments.” ([WAI tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/))

## Removing legitimate preference controls blindly

Wrong: “Any text-size button is an overlay; delete it.”

Right: “Inspect the feature's purpose and effects. Preserve useful user-controlled preferences while replacing unsupported automated-compliance claims with tested source remediation.” This is project policy; runtime customization is not inherently an accessibility failure.
