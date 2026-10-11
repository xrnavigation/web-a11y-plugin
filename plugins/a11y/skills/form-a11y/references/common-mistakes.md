# Form mistakes

Wrong: `<input placeholder="Email">` alone.
Right: `<label for="email">Email</label><input id="email" type="email">`.
A placeholder does not replace the visible associated label
([WAI labels](https://www.w3.org/WAI/tutorials/forms/labels/)).

Wrong: keep `aria-invalid="true"` after correction, or forbid `false`.
Right: remove it or set false when validation succeeds
([WAI-ARIA](https://www.w3.org/TR/wai-aria-1.2/#aria-invalid)).

Wrong: add an assertive region to each field plus focused alert summary.
Right: associate visible errors and choose one tested summary/focus strategy
([WAI validation](https://www.w3.org/WAI/tutorials/forms/validation/)).

Wrong: block password paste or require unaided MFA transcription.
Right: provide assistance or another qualifying alternative and test all steps
([Authentication minimum](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html)).

Wrong: claim autocomplete is required on every field.
Right: identify applicable user-information purposes with supported tokens
([Input purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html)).

Wrong: ban `aria-errormessage` forever from a 2024 support report.
Right: test valid invalid-state/error association on the actual support matrix
([WAI-ARIA](https://www.w3.org/TR/wai-aria-1.2/#aria-errormessage)).
