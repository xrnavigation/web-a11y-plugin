# Error Message Patterns
## Contents

- [Text Fields](#text-fields)
- [Required Fields](#required-fields)
- [Format Mismatches](#format-mismatches)
- [Out-of-Range Values](#out-of-range-values)
- [Constrained-Value Fields](#constrained-value-fields)
- [ARIA Markup](#aria-markup)
- [Error Summary](#error-summary)
- [Tone Guide](#tone-guide)


Reusable templates for clear, actionable error messages. Every message follows the pattern:

```
[Field name]: [What went wrong]. [How to fix it].
```

Keep messages under 14 words. At 8 words or fewer, comprehension reaches 100%.
([NN/g](https://www.nngroup.com/articles/error-message-guidelines/))

---

## Text Fields

```
Email: must include an @ symbol. Example: name@example.com
Phone: must be 10 digits. Example: (555) 123-4567
ZIP code: must be 5 digits. Example: 90210
```

## Required Fields

```
First name is required.
```

Not: "This field is required." Name the field.
([WCAG SC 3.3.1](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html))

## Format Mismatches

```
Date of birth: use MM/DD/YYYY format. Example: 03/15/1990
Password: must be at least 8 characters with one number.
```

## Out-of-Range Values

```
Quantity: must be between 1 and 99.
Year: must be 1900 or later.
```

## Constrained-Value Fields

When a field accepts only specific values, suggest the closest match:

```
Month: "Dcember" is not recognized. Did you mean "December"?
State: "CN" is not a US state. Did you mean "CA" (California) or "CT" (Connecticut)?
```

([WCAG SC 3.3.3](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html))

## ARIA Markup

Always pair error text with ARIA attributes on the field:

```html
<label for="email">Email address</label>
<input id="email" type="email"
       aria-invalid="true"
       aria-describedby="email-error">
<span id="email-error" role="alert">
  Email: must include an @ symbol. Example: name@example.com
</span>
```

- `aria-invalid="true"` marks the field as errored.
- `aria-describedby` associates the error text with the field.
- `role="alert"` or `aria-live="assertive"` announces dynamically injected errors.

## Error Summary

For forms with multiple errors, provide a summary at the top linking to each errored field:

```html
<div role="alert">
  <h2>Please fix 2 errors</h2>
  <ul>
    <li><a href="#email">Email: must include an @ symbol</a></li>
    <li><a href="#phone">Phone: must be 10 digits</a></li>
  </ul>
</div>
```

Move focus to the error summary on submission failure.

## Tone Guide

| Avoid | Use Instead |
|-------|-------------|
| Invalid email | Email: must include an @ symbol |
| Illegal character in name | Name: letters, spaces, and hyphens only |
| Incorrect password | Password does not match our records |
| Error: field required | First name is required |
| Bad input | Date of birth: use MM/DD/YYYY format |

Never blame the user. The system adapts; it does not judge.
([NN/g](https://www.nngroup.com/articles/error-message-guidelines/))
