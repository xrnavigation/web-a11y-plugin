---
name: form-a11y
description: Guides comprehensive form accessibility beyond basic labels — error messaging and association, validation patterns, field grouping, accessible authentication (WCAG 2.2), redundant entry prevention, and autocomplete attributes. Auto-invokes when creating forms, validation logic, authentication flows, or multi-step form wizards.
allowed-tools: Read, Glob, Grep
compatibility: "Claude Code, Codex CLI, Gemini CLI"
---

# Form Accessibility

> "The best error message is the one that never shows up."
> — Thomas Fuchs

Forms are the primary way users provide information on the web. Getting form accessibility wrong locks people out of purchases, registrations, healthcare portals, and government services. This skill covers everything beyond basic `<label>` + `<input>` pairing.

---

## 1. Error Association

Use `aria-describedby` + `aria-invalid` to connect error messages to fields. This is the proven, cross-browser pattern.

```html
<label for="email">Email</label>
<input id="email" type="email"
       aria-describedby="email-error"
       aria-invalid="true">
<span id="email-error">Enter a valid email address, e.g. name@example.com</span>
```

### Rules

- **Set `aria-invalid="true"`** when a field has an error. Remove the attribute entirely (not `"false"`) when valid.
- **Never set `aria-invalid` before the user interacts.** Do not mark required fields invalid on page load.
- **Use `aria-describedby`** to point the input to the error message element's `id`. Screen readers announce the description when the field receives focus.
- **Multiple descriptions:** space-separate IDs to include both a hint and an error:

```html
<input id="phone" type="tel"
       aria-describedby="phone-hint phone-error"
       aria-invalid="true">
<span id="phone-hint">Format: (555) 123-4567</span>
<span id="phone-error">Phone number is required.</span>
```

- **Do NOT use `aria-live` on individual field errors.** Roselli's testing across seven SR/browser combinations found that `aria-live="assertive"` on field errors clips the next field name announcement. Chromium/JAWS already treats `aria-describedby` as an assertive live region, doubling announcements if you also add `aria-live`. ([Roselli, 2023](https://adrianroselli.com/2023/04/exposing-field-errors.html))
- **Do NOT use `aria-errormessage` in production yet.** Support is insufficient as of 2024-2025 — TalkBack has no support, iOS VoiceOver/Safari only partial. Continue using `aria-describedby`. ([Cerovac, 2024](https://cerovac.com/a11y/2024/06/support-for-aria-errormessage-is-getting-better-but-still-not-there-yet/))

### Limitation

Changes to `aria-describedby` content while the input is focused will **not** trigger re-announcement — the user must re-focus the field. ([Roselli, 2022](https://adrianroselli.com/2022/04/accessible-description-exposure.html))

---

## 2. Validation Patterns

### Timing

- **Validate on blur**, not on every keystroke. The `input` event fires errors before the user finishes typing — this is disruptive.
- **Refinement:** only trigger blur validation if the field value actually changed. This prevents false errors from accidental focus (scrolling, tabbing past).
- **Always validate on submit.** Client-side validation can be bypassed; always validate server-side as well.

([TetraLogical, 2024](https://tetralogical.com/blog/2024/10/21/foundations-form-validation-and-error-messages/); [Smashing Magazine, 2023](https://www.smashingmagazine.com/2023/02/guide-accessible-form-validation/))

### Inline Errors

- Display error messages near their associated field.
- Use distinctive styling — not color alone (WCAG 1.4.1). Add an icon, text prefix ("Error:"), or border change alongside color.
- Associate each error to its field via `aria-describedby`.

### Error Summary

For longer forms, display a summary of all errors above the form (or before the submit button):

- Include links to each invalid field.
- Set focus to the summary container after submission.
- Use `aria-live="assertive"` on the summary container — **not** on individual field errors.

For short forms (2-3 fields), focusing the first invalid field with `HTMLElement.focus()` is sufficient — the screen reader announces the error via `aria-describedby`.

### Recommended: Combined Approach

Use both an error summary **and** inline errors. The summary provides orientation ("3 errors found"); inline errors provide context at each field. ([WebAIM](https://webaim.org/techniques/formvalidation/))

---

## 3. Field Grouping (fieldset/legend)

Use `<fieldset>` and `<legend>` to group related controls. The `<legend>` acts as the group label — screen readers announce it when a user enters the fieldset.

### When to Use

- **Radio button groups** — the legend provides the group question
- **Checkbox groups** — when checkboxes share a common category
- **Address blocks** — shipping vs. billing address sections
- **Related field sets** — e.g., "Emergency Contact" fields

```html
<fieldset>
  <legend>Shipping Address</legend>
  <label for="street">Street</label>
  <input id="street" type="text" autocomplete="shipping street-address">
  <!-- more fields -->
</fieldset>
```

### When NOT to Use

- Do **not** wrap the entire form in a single fieldset — it adds noise without value.
- A single input with its own `<label>` does not need a fieldset.
- Use fieldset only when fields share a relationship that needs a group label.

---

## 4. Required Fields

### Visual Indicators

- Use text "(required)" near the label, not asterisks alone.
- If using asterisks, include a legend at the top of the form: "Fields marked with * are required."
- Never rely on color alone (WCAG 1.4.1).

```html
<label for="name">Full Name <span aria-hidden="true">*</span>
  <span class="sr-only">(required)</span>
</label>
<input id="name" type="text" required>
```

### `required` vs. `aria-required="true"`

| Attribute | SR announces "required" | Browser-native validation | Prevents empty submission |
|---|---|---|---|
| `required` | Yes | Yes | Yes |
| `aria-required="true"` | Yes | No | No |

Use `required` when browser-native validation is acceptable. Use `aria-required="true"` when you need custom validation UX and want to suppress browser tooltips (add `novalidate` to the `<form>`).

---

## 5. Accessible Authentication (WCAG 2.2)

### SC 3.3.8 — Level AA

A cognitive function test (remembering a password, solving a puzzle, transcribing a code) must NOT be required for authentication unless:

1. **Alternative** — another method exists that doesn't require the test
2. **Mechanism** — assistance is available (password manager, paste)
3. **Object Recognition** — the test uses object recognition (AA only)
4. **Personal Content** — the test uses content the user provided (AA only)

### SC 3.3.9 — Level AAA

Same as 3.3.8, but only the Alternative and Mechanism exceptions remain.

### What Complies

- Username/password with proper `autocomplete` attributes (`username`, `current-password`, `new-password`)
- Paste is **not blocked** on authentication fields
- WebAuthn / passkeys (fingerprint, face, PIN)
- Third-party OAuth (Sign in with Google, etc.)
- Email-link / magic link authentication
- Multi-factor with hardware tokens, QR codes, or device notifications

### What Fails

- Blocking paste on password or verification code fields
- Requiring manual transcription of verification codes without copy/paste
- CAPTCHAs or puzzles with no alternative
- Requiring memorization without allowing password managers

### Implementation Checklist

```html
<!-- Login form — compliant -->
<form>
  <label for="user">Username</label>
  <input id="user" type="text" autocomplete="username">

  <label for="pass">Password</label>
  <input id="pass" type="password" autocomplete="current-password">
  <!-- Do NOT add onpaste="return false" -->

  <button type="submit">Sign In</button>
</form>
```

([W3C Understanding SC 3.3.8](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html))

---

## 6. Redundant Entry (WCAG 2.2)

### SC 3.3.7 — Level A

Information previously entered by the user that is required again in the same process must be either **auto-populated** or **available for the user to select**.

Exceptions: re-entry is essential, required for security (password confirmation), or the information is no longer valid.

### Implementation Techniques

- "Billing address same as shipping" checkbox
- Pre-populate fields from earlier steps (allow edits)
- Dropdowns populated from previous input
- **Retain field values after validation errors** — never clear the form on failed submission
- Pre-fill search terms on results pages

([W3C Understanding SC 3.3.7](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html))

---

## 7. Autocomplete Attributes

The `autocomplete` attribute enables browsers and password managers to auto-fill fields. Required for WCAG 1.3.5 (Identify Input Purpose) and supports accessible authentication (3.3.8/3.3.9).

### Quick Reference

| Purpose | Values |
|---|---|
| Identity | `name`, `given-name`, `family-name`, `nickname`, `username`, `organization` |
| Authentication | `current-password`, `new-password`, `one-time-code` |
| Address | `street-address`, `address-line1`, `address-line2`, `address-level2` (city), `address-level1` (state), `country`, `postal-code` |
| Payment | `cc-name`, `cc-number`, `cc-exp`, `cc-exp-month`, `cc-exp-year`, `cc-csc` |
| Contact | `tel`, `email`, `url` |
| Personal | `bday`, `sex`, `language`, `photo` |

### Modifiers

- **Scope:** `section-{name}` groups related fields (e.g., `section-emergency-contact`)
- **Purpose:** `shipping`, `billing` prefix address/contact fields
- **Contact type:** `home`, `work`, `mobile` prefix tel/email fields
- **WebAuthn:** `webauthn` for passkey/credential fields

```html
<input autocomplete="shipping address-line1" name="ship-street">
<input autocomplete="billing cc-number" name="card">
<input autocomplete="section-emergency-contact tel" name="emergency-phone">
```

For the complete list of all autocomplete values, see: `${CLAUDE_SKILL_DIR}/references/autocomplete-values.md`

---

## 8. Common Mistakes

These are real patterns from accessibility audits. Each is cited.

1. **Blocking paste on password fields** — prevents password manager use, fails WCAG 3.3.8. ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html))
2. **Validating on every keystroke** — fires errors before the user finishes typing. Validate on blur. ([TetraLogical](https://tetralogical.com/blog/2024/10/21/foundations-form-validation-and-error-messages/))
3. **`aria-live` on individual field errors** — clips next field announcement in multiple SR/browser combos. Use `aria-live` only on error summaries. ([Roselli](https://adrianroselli.com/2023/04/exposing-field-errors.html))
4. **`aria-invalid` before user interaction** — do not mark required fields invalid on page load. ([Deque](https://www.deque.com/blog/aria-invalid-error-indication/))
5. **Color alone for error indication** — red borders without icons or text fails WCAG 1.4.1. ([Smashing Magazine](https://www.smashingmagazine.com/2023/02/guide-accessible-form-validation/))
6. **Vague error messages** — "Invalid input" is unhelpful. Provide specific guidance: "Enter a date in MM/DD/YYYY format." ([WebAIM](https://webaim.org/techniques/formvalidation/))
7. **Clearing form on validation failure** — destroys user input, fails the spirit of SC 3.3.7. ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html))
8. **Missing `autocomplete` on login fields** — without `autocomplete="username"` and `autocomplete="current-password"`, password managers can't autofill, risking WCAG 3.3.8 failure. ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html))
9. **`aria-label` instead of visible `<label>`** — not translated by many localization tools, doesn't expand click target. Use `<label for="...">` first. ([Roselli](https://adrianroselli.com/2020/01/my-priority-of-methods-for-labeling-a-control.html))
10. **Using `aria-errormessage` in production** — insufficient SR support as of 2024-2025. Use `aria-describedby`. ([Cerovac](https://cerovac.com/a11y/2024/06/support-for-aria-errormessage-is-getting-better-but-still-not-there-yet/))
11. **Disabled form controls** — not focusable, not announced by some screen readers, no explanation of why disabled. Prefer keeping controls enabled and validating on submission. ([Roselli](https://adrianroselli.com/2024/02/dont-disable-form-controls.html))
12. **Wrapping entire field content in `<label>`** — confuses screen readers about actual label text and creates click-conflict with interactive elements inside the label. ([Smashing Magazine](https://www.smashingmagazine.com/2023/02/guide-accessible-form-validation/))

For detailed patterns and anti-patterns, see: `${CLAUDE_SKILL_DIR}/references/common-mistakes.md`

---

## 9. Cross-References

- `live-regions` — for `aria-live` usage on error summaries and dynamic content announcements
- `cognitive-a11y` — for cognitive accessibility considerations (clear language, error recovery, timeouts)
- `aria-decision-framework` — for when to use ARIA vs. native HTML elements

For detailed reference material:

- `${CLAUDE_SKILL_DIR}/references/error-association-patterns.md` — complete error association patterns with SR test results
- `${CLAUDE_SKILL_DIR}/references/autocomplete-values.md` — full autocomplete attribute value list
- `${CLAUDE_SKILL_DIR}/references/common-mistakes.md` — anti-patterns with citations
- `${CLAUDE_SKILL_DIR}/references/sources.yaml` — provenance for all cited sources
