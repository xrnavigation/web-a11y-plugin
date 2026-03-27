# Common Form Accessibility Mistakes

Each mistake is cited to its source. These are real patterns from accessibility audits and screen reader testing.

---

## 1. Blocking Paste on Password Fields

```html
<!-- WRONG -->
<input type="password" onpaste="return false">

<!-- RIGHT -->
<input type="password" autocomplete="current-password">
```

Blocking paste prevents password manager use and fails WCAG 3.3.8 (Accessible Authentication). Users with cognitive disabilities rely on password managers to handle complex passwords.

Source: [W3C Understanding SC 3.3.8](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html)

---

## 2. Validating on Every Keystroke

```javascript
// WRONG — fires errors before user finishes typing
input.addEventListener('input', validate);

// RIGHT — validate after user leaves the field
input.addEventListener('blur', () => {
  if (input.value !== input.defaultValue) {
    validate(input);
  }
});
```

The `input` event fires on every character. A user typing "jo" into an email field gets an error after "j". Validate on `blur`, and only if the value changed.

Source: [TetraLogical, 2024](https://tetralogical.com/blog/2024/10/21/foundations-form-validation-and-error-messages/); [Smashing Magazine, 2023](https://www.smashingmagazine.com/2023/02/guide-accessible-form-validation/)

---

## 3. Using aria-live on Individual Field Errors

```html
<!-- WRONG — clips next field announcement -->
<span id="email-error" aria-live="assertive">Invalid email</span>

<!-- RIGHT — no aria-live on field errors -->
<span id="email-error">Invalid email</span>
```

Roselli's testing found `aria-live="assertive"` on field errors clips the next field name announcement in multiple SR/browser combos. Chromium/JAWS already treats `aria-describedby` targets as assertive live regions, causing double announcements.

Use `aria-live` only on error **summaries**, not individual field errors.

Source: [Adrian Roselli: Exposing Field Errors](https://adrianroselli.com/2023/04/exposing-field-errors.html)

---

## 4. Setting aria-invalid Before User Interaction

```html
<!-- WRONG — invalid state on page load -->
<input type="email" required aria-invalid="true">

<!-- RIGHT — no aria-invalid until user attempts submission -->
<input type="email" required>
```

Marking fields invalid before the user interacts creates a hostile experience. Set `aria-invalid="true"` only after the user has attempted to submit or has blurred the field after editing.

Source: [Deque](https://www.deque.com/blog/aria-invalid-error-indication/); [Smashing Magazine, 2023](https://www.smashingmagazine.com/2023/02/guide-accessible-form-validation/)

---

## 5. Using Color Alone for Error Indication

```html
<!-- WRONG — red border only -->
<input style="border-color: red" aria-invalid="true">

<!-- RIGHT — icon + text + color -->
<input aria-invalid="true" aria-describedby="email-error">
<span id="email-error">⚠ Enter a valid email address.</span>
```

Red borders or text without icons or explicit error text fails WCAG 1.4.1 (Use of Color). Users who cannot perceive color differences will miss the error.

Source: [Smashing Magazine, 2023](https://www.smashingmagazine.com/2023/02/guide-accessible-form-validation/)

---

## 6. Vague Error Messages

```html
<!-- WRONG -->
<span id="date-error">Invalid input</span>

<!-- RIGHT -->
<span id="date-error">Enter a date in MM/DD/YYYY format, e.g. 03/15/2025</span>
```

"Invalid input" gives no guidance on how to fix the problem. Error messages must be specific and actionable — tell the user what's wrong and how to correct it.

Source: [TetraLogical, 2024](https://tetralogical.com/blog/2024/10/21/foundations-form-validation-and-error-messages/); [WebAIM](https://webaim.org/techniques/formvalidation/)

---

## 7. Clearing Form Fields on Validation Failure

```javascript
// WRONG — destroys user input
form.addEventListener('submit', (e) => {
  if (!isValid()) {
    form.reset(); // Clears all fields
    showErrors();
  }
});

// RIGHT — preserve values, show errors
form.addEventListener('submit', (e) => {
  e.preventDefault();
  if (!isValid()) {
    showErrors(); // Fields retain their values
  }
});
```

Clearing the form forces users to re-enter everything. This is hostile to all users and directly contradicts the spirit of WCAG 3.3.7 (Redundant Entry).

Source: [W3C Understanding SC 3.3.7](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html)

---

## 8. Missing Autocomplete on Login Fields

```html
<!-- WRONG — no autocomplete -->
<input type="text" name="user">
<input type="password" name="pass">

<!-- RIGHT -->
<input type="text" name="user" autocomplete="username">
<input type="password" name="pass" autocomplete="current-password">
```

Without proper `autocomplete` attributes, password managers cannot reliably identify and autofill login fields. This can fail WCAG 3.3.8 (Accessible Authentication) because users are forced to remember and manually type credentials.

Source: [W3C Understanding SC 3.3.8](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html)

---

## 9. aria-label Instead of Visible Labels

```html
<!-- WRONG — invisible label -->
<input type="text" aria-label="Search">

<!-- RIGHT — visible label -->
<label for="search">Search</label>
<input id="search" type="text">
```

`aria-label` does not create a visible label, is not translated by many localization tools, and does not expand the click/tap target. Use `<label>` with `for` attribute as the first choice. Reserve `aria-label` for cases where a visible label truly cannot exist (e.g., icon-only buttons with visible tooltips).

Source: [Adrian Roselli: Priority of Methods for Labeling a Control](https://adrianroselli.com/2020/01/my-priority-of-methods-for-labeling-a-control.html)

---

## 10. Wrapping Entire Field Content in Label

```html
<!-- WRONG — interactive elements inside label -->
<label>
  Email address
  <input type="email">
  <span class="error">Invalid email</span>
  <a href="/help">Help</a>
</label>

<!-- RIGHT — label references input via for/id -->
<label for="email">Email address</label>
<input id="email" type="email" aria-describedby="email-error">
<span id="email-error">Invalid email</span>
<a href="/help">Help</a>
```

Wrapping everything in a `<label>` confuses screen readers about what the actual label text is and creates click-conflict issues with interactive elements (links, buttons) inside the label.

Source: [Smashing Magazine, 2023](https://www.smashingmagazine.com/2023/02/guide-accessible-form-validation/)

---

## 11. Using aria-errormessage in Production

```html
<!-- AVOID — insufficient SR support -->
<input type="email" aria-errormessage="email-err">
<span id="email-err">Invalid email</span>

<!-- USE INSTEAD -->
<input type="email" aria-describedby="email-err" aria-invalid="true">
<span id="email-err">Invalid email</span>
```

`aria-errormessage` has insufficient screen reader support as of 2024-2025. TalkBack has no support. iOS VoiceOver only works with specific hiding techniques. Use `aria-describedby` until support broadens.

Source: [Bogdan Cerovac, 2024](https://cerovac.com/a11y/2024/06/support-for-aria-errormessage-is-getting-better-but-still-not-there-yet/)

---

## 12. Disabled Form Controls

```html
<!-- PROBLEMATIC -->
<button disabled>Submit</button>

<!-- BETTER — keep enabled, explain constraints -->
<button type="submit">Submit</button>
<!-- Validate on click and show clear error messages -->
```

Disabled controls are not focusable, not announced by some screen readers, and provide no explanation of why they're disabled. Users encounter a control they can't interact with and get no feedback. Prefer keeping controls enabled and validating on submission with clear error messages.

Source: [Adrian Roselli: Don't Disable Form Controls](https://adrianroselli.com/2024/02/dont-disable-form-controls.html)
