# Error Message Craft
## Contents

- [NN/g Framework: Three Pillars](#nng-framework-three-pillars)
  - [Visibility — The User Must Notice the Error](#visibility-the-user-must-notice-the-error)
  - [Communication — The User Must Understand the Error](#communication-the-user-must-understand-the-error)
  - [Efficiency — The User Must Be Able to Fix the Error](#efficiency-the-user-must-be-able-to-fix-the-error)
- [GOV.UK Error Patterns](#govuk-error-patterns)
  - [Language Rules](#language-rules)
  - [Structure](#structure)
  - [Specificity by Error Type](#specificity-by-error-type)
- [Bad vs. Good Examples](#bad-vs-good-examples)
- [Assistive Technology Integration](#assistive-technology-integration)
  - [Screen Reader Announcements](#screen-reader-announcements)
  - [Dynamic Error Announcements](#dynamic-error-announcements)
  - [Key ARIA Attributes for Errors](#key-aria-attributes-for-errors)
- [Sources](#sources)


This reference covers writing error messages that are accessible, specific, and actionable — organized around the NN/g framework and GOV.UK design patterns, with assistive technology integration guidance.

---

## NN/g Framework: Three Pillars

### Visibility — The User Must Notice the Error

- Display the message **adjacent to the field** that caused the error, not in a distant banner alone.
- Use **at least 3 redundant indicators**: bold text, red color, icon, border highlight, field shading. Never rely on color alone (350 million people have color-vision deficiency).
- All indicators must meet **WCAG AA contrast requirements** (4.5:1 for text, 3:1 for non-text).
- **Do not show premature errors** while the user is still typing — this feels hostile and disrupts flow.

### Communication — The User Must Understand the Error

- **Plain language.** No jargon, no error codes ("Form POST error 422").
- **Be specific** about what went wrong. "An error occurred" is useless. "Email address must include an @ symbol" is actionable.
- **Offer a constructive solution**, not just a description of the problem.
- **Non-blaming tone.** Avoid "invalid," "illegal," "you failed to," "forbidden."

### Efficiency — The User Must Be Able to Fix the Error

- **Preserve user input.** Never clear a form field on error.
- **Suggest corrections** when possible ("Did you mean gmail.com?").
- **Link to supplementary help** without overwhelming.
- **Detect common mistakes** proactively (missing email attachment, duplicate submission).

([NN/g Error-Message Guidelines](https://www.nngroup.com/articles/error-message-guidelines/))

---

## GOV.UK Error Patterns

The GOV.UK Design System provides concrete, tested patterns used across UK government services.

### Language Rules

**Do not use:** technical jargon, "please," "sorry," "valid/invalid," "forbidden," humor ("oops!"), negative phrasing ("you forgot").

**Do use:** direct instructions for empty fields ("Enter your first name") and descriptions for constraint violations ("First name must be 35 characters or fewer").

**Match the field label.** If the label says "How many hours do you work a week?" the error says "Enter how many hours you work a week," not "This field is required."

### Structure

- Show **BOTH** an error summary at the top of the page **AND** an inline error next to the field.
- Use **identical wording** in both locations so users are not confused by different messages for the same problem.
- **Prefix error messages** with a visually hidden "Error:" so screen readers announce "Error: Enter your first name."
- **Do not clear form fields** when displaying errors.

### Specificity by Error Type

For a single field, the error message varies based on the problem:

| Error Type | Example Message |
|-----------|----------------|
| Empty field | "Enter your email address" |
| Wrong format | "Enter an email address in the correct format, like name@example.com" |
| Too long | "Email address must be 256 characters or fewer" |
| Too short | "Email address must be 5 characters or more" |
| Not a match | "Email address does not match. Enter the same email address in both fields." |

([GOV.UK Error Message](https://design-system.service.gov.uk/components/error-message/); [GOV.UK Error Summary](https://design-system.service.gov.uk/components/error-summary/); [GOV.UK Validation Pattern](https://design-system.service.gov.uk/patterns/validation/))

---

## Bad vs. Good Examples

| Bad | Good | Why |
|-----|------|-----|
| "Invalid input" | "Enter a date of birth in the format DD/MM/YYYY" | Bad version tells the user nothing about what is wrong or how to fix it. Good version names the field, states the expected format. |
| "Error: field required" | "Enter your National Insurance number" | Generic message forces user to figure out which field and what it wants. Good version is specific. |
| "Please enter a valid email" | "Enter an email address in the correct format, like name@example.com" | "Valid" is jargon. The example format shows what "correct" means concretely. |
| "Oops! Something went wrong" | "Your payment could not be processed. Check your card details and try again." | Humor is patronizing during task completion. Good version states what happened and what to do. |
| "Error 422: Unprocessable Entity" | "Date of birth must be in the past" | Error codes are meaningless to users. Good version states the constraint in plain language. |
| "This field is required" (on 5 fields) | "Enter your first name" / "Enter your email address" / "Select your country" | Generic message repeated provides no useful distinction. Each field gets a specific message. |

---

## Assistive Technology Integration

### Screen Reader Announcements

Error messages must be programmatically associated with their fields so screen readers announce them when the field receives focus:

```html
<!-- Error linked to field via aria-describedby -->
<label for="email">Email address</label>
<span id="email-error" class="error">
  <span class="sr-only">Error:</span>
  Enter an email address in the correct format, like name@example.com
</span>
<input id="email" type="email" aria-describedby="email-error" aria-invalid="true">
```

### Dynamic Error Announcements

When errors appear after form submission (without page reload), use `role="alert"` or `aria-live="assertive"` on the error summary so screen readers announce it immediately:

```html
<div role="alert">
  <h2>There is a problem</h2>
  <ul>
    <li><a href="#email">Enter an email address in the correct format, like name@example.com</a></li>
  </ul>
</div>
```

### Key ARIA Attributes for Errors

| Attribute | Purpose | When to Use |
|-----------|---------|-------------|
| `aria-invalid="true"` | Marks a field as containing an error | On the input element when validation fails |
| `aria-describedby` | Links error message text to the field | Points to the error message element ID |
| `role="alert"` | Announces content immediately to screen readers | On the error summary container |
| `aria-live="assertive"` | Announces dynamic content changes | Alternative to `role="alert"` for error summaries |

([TetraLogical Form Validation](https://tetralogical.com/blog/2024/10/21/foundations-form-validation-and-error-messages/); [Smashing Magazine Accessible Form Validation](https://www.smashingmagazine.com/2023/02/guide-accessible-form-validation/); [WebAIM Form Validation](https://webaim.org/techniques/formvalidation/))

---

## Sources

- [NN/g Error-Message Guidelines](https://www.nngroup.com/articles/error-message-guidelines/)
- [GOV.UK Error Message Component](https://design-system.service.gov.uk/components/error-message/)
- [GOV.UK Error Summary Component](https://design-system.service.gov.uk/components/error-summary/)
- [GOV.UK Validation Pattern](https://design-system.service.gov.uk/patterns/validation/)
- [TetraLogical Form Validation](https://tetralogical.com/blog/2024/10/21/foundations-form-validation-and-error-messages/)
- [Smashing Magazine Accessible Form Validation](https://www.smashingmagazine.com/2023/02/guide-accessible-form-validation/)
- [WebAIM Form Validation](https://webaim.org/techniques/formvalidation/)
