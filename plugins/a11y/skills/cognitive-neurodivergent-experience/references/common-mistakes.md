# Cognitive experience mistakes and corrections

## Assuming one experience for a diagnosis

Wrong: “All autistic people panic when this timer appears.”

Right: “This timer may create time pressure. Evaluate the task with participants who need more time; offer an appropriate timing route.” WAI stories illustrate varied situations, not diagnostic guarantees. ([WAI user stories](https://www.w3.org/WAI/people-use-web/user-stories/))

## Claiming population figures predict product failure

Wrong: “20% of users cannot complete this flow.”

Right: “The flow requires recalling earlier entries. Add review/save options and measure actual completion.” Label this as a project hypothesis until tested. ([COGA usable](https://www.w3.org/TR/coga-usable/))

## Confusing adjustment and extension

```text
Wrong: Extension is only allowed up to ten times the original duration.
Right: For the WCAG extension route, warn before expiry, give at least 20 seconds
       for a simple action, and allow extension at least ten times.
```

The separate adjustment route works before encountering the limit over a range at least ten times the default. Document applicable exceptions. ([Timing Adjustable](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html))

## Restricting typography by diagnosis

```css
/* Wrong as a universal dyslexia rule: reduces contrast without measurement. */
body { color: #aaa; background: white; }
/* Right project example: retain contrast and allow responsive text. */
body { color: #222; background: white; font-size: 100%; }
```

Do not mandate one font/palette for a diagnosis. Evaluate readability and preserve contrast while supporting adaptable presentation. ([COGA usable](https://www.w3.org/TR/coga-usable/))

## Advertising a save that did not succeed

```js
// Wrong: communicates a successful save before persistence resolves.
status.textContent = 'Saved';
await saveDraft();
// Right project pattern: communicate confirmed success and failure.
try { await saveDraft(); status.textContent = 'Draft saved'; }
catch { status.textContent = 'Draft was not saved. Try again.'; }
```

Test break/resume and recovery; do not promise that every field will be retained if privacy/security rules prohibit it. ([COGA data-loss pattern](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p09-data-loss/))
