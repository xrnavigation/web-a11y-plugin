# Error association and lifecycle

## Field pattern

```html
<label for="email">Email</label>
<input id="email" type="email" aria-invalid="true" aria-describedby="email-error">
<p id="email-error">Enter an email address like name@example.com.</p>
```

On failed validation, expose the field's invalid state and a visible associated
message. On correction remove invalid state or set false. Description output and
update timing need testing; do not require a specific spoken sentence
([WAI-ARIA invalid](https://www.w3.org/TR/wai-aria-1.2/#aria-invalid),
[WAI validation](https://www.w3.org/WAI/tutorials/forms/validation/)).

## Alternative error-message property

```html
<label for="email">Email</label>
<input id="email" type="email" aria-invalid="true" aria-errormessage="email-error">
<p id="email-error">Enter an email address like name@example.com.</p>
```

Verify the actual target combinations before adopting this property. When invalid
is false, the error-message relationship is not pertinent; hide or remove stale
visible errors accordingly. Do not use opacity tricks to leave invisible active
errors in the UI. Old support observations are not universal current claims
([WAI-ARIA error message](https://www.w3.org/TR/wai-aria-1.2/#aria-errormessage)).

## Summary and recovery

```html
<section id="errors" tabindex="-1" aria-labelledby="error-title">
  <h2 id="error-title">Check your details</h2>
  <ul><li><a href="#email">Email: enter an email address</a></li></ul>
</section>
```

As a project pattern, move focus to this rendered summary after a failed submit
with several errors. Verify activating its link puts the user at the editable
field. Avoid adding assertive speech on the summary while simultaneously focusing
it unless the tested matrix demonstrates useful non-duplicate behavior
([WAI validation](https://www.w3.org/WAI/tutorials/forms/validation/)).

Test error arrival while focused, blur/submit timing, corrected input, multiple
errors, repeat submissions and server errors. Record visible fallback and observed
AT behavior; no browser/AT combinations were executed to establish these examples.
