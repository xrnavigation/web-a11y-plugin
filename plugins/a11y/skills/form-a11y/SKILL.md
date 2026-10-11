---
name: form-a11y
description: Guides form labels, grouped controls, validation feedback, autocomplete, accessible authentication and redundant-entry prevention. Use when creating or repairing forms, sign-in flows, checkout or multi-step input journeys.
---

# Form accessibility

Build an understandable input-and-recovery journey. Prefer native controls with
visible, associated labels; placeholder text does not replace a label
([WAI labels](https://www.w3.org/WAI/tutorials/forms/labels/)).

## Name, group and identify purpose

```html
<fieldset>
  <legend>Shipping address</legend>
  <label for="street">Street address (required)</label>
  <input id="street" name="street" autocomplete="shipping street-address" required>
</fieldset>
```

Use fieldset/legend for a meaningful related group and labels for individual
fields. Explain required input and format before submission
([WAI grouping](https://www.w3.org/WAI/tutorials/forms/grouping/)).
Native `required` participates in browser validation; `aria-required` only exposes
semantics. For custom feedback, `novalidate` can suppress native submission
validation while retaining the appropriate input constraints
([WAI validation](https://www.w3.org/WAI/tutorials/forms/validation/)).

SC 1.3.5 AA covers fields collecting information about the user whose purposes are
in the specified taxonomy, where the technology supports identifying the purpose.
HTML autocomplete tokens are a technique for those applicable fields, not a demand
that every input have autocomplete
([Identify input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html)).

## Validate and recover

As project guidance, avoid premature errors while the user is still composing an
answer. Validate on submit and, when useful, after an edited field loses focus.
Preserve safe entered data; use the application's security policy for passwords,
payment secrets and verification codes. Client validation does not replace server
validation ([WAI validation](https://www.w3.org/WAI/tutorials/forms/validation/)).

```html
<label for="email">Email address</label>
<input id="email" type="email" aria-invalid="true"
       aria-describedby="email-hint email-error">
<p id="email-hint">We send your receipt here.</p>
<p id="email-error">Enter an email address like name@example.com.</p>
```

Set invalid state after a failed validation. Remove `aria-invalid` or set `false`
when valid; both express the default non-invalid state
([WAI-ARIA invalid](https://www.w3.org/TR/wai-aria-1.2/#aria-invalid)).
Keep errors visible and associated with fields; provide text identification and
known correction suggestions where applicable
([WAI validation](https://www.w3.org/WAI/tutorials/forms/validation/)).

For several errors, provide a summary with links to fields. Choose a focused
summary or first invalid field according to the flow. If a separate live summary
is needed, verify that it does not repeat or clip focus speech; do not make every
field assertive by default ([WAI validation](https://www.w3.org/WAI/tutorials/forms/validation/)).

`aria-errormessage` is a valid mechanism when paired with the invalid state and a
visible error. Decide from the target support matrix; old support reports do not
establish a present-day production ban. An associated description is another
strategy. Do not expose the same error redundantly through both without testing
([WAI-ARIA error message](https://www.w3.org/TR/wai-aria-1.2/#aria-errormessage)).

## Authentication and repeated input

SC 3.3.8 AA permits a cognitive test only with an alternative, an assistance
mechanism, object recognition, or personal-content recognition. At 3.3.9 AAA only
the alternative/mechanism options remain. Assess every step, including MFA and
recovery, rather than labeling OAuth, passkeys or PINs inherently compliant
([Authentication minimum](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html),
[Authentication enhanced](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-enhanced.html)).

Enable password-manager and copy/paste assistance where used. Verify real filling,
password reveal, one-time-code entry and accessible alternatives. A markup example
alone does not prove authentication compliance
([Authentication minimum](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html)).

```html
<label for="username">Username</label>
<input id="username" autocomplete="username">
<label for="password">Password</label>
<input id="password" type="password" autocomplete="current-password">
```

SC 3.3.7 A concerns information entered by or provided to the user earlier in the
same process: auto-populate it or offer selection, except when re-entry is
essential, needed for security, or the information is no longer valid. Do not
infer that all retained data should cross sessions or security boundaries
([Redundant entry](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html)).

## Verify

Test submit, server rejection, correction, back/forward and repeat submission.
Inspect actual names, invalid/required states, focus, visible errors, password
manager/paste behavior and observed speech in the support matrix. Mark unrun AT
checks not tested. Consult `live-regions` for announcement lifecycle.

Read [error association](references/error-association-patterns.md),
[autocomplete tokens](references/autocomplete-values.md),
[common mistakes](references/common-mistakes.md) and [sources](references/sources.yaml).
