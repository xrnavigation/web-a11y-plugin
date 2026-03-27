# Error Association Patterns

Detailed patterns for associating error messages with form fields, including screen reader test results.

---

## The Reliable Pattern: aria-describedby + aria-invalid

```html
<label for="email">Email</label>
<input id="email" type="email"
       aria-describedby="email-error"
       aria-invalid="true">
<span id="email-error">Enter a valid email address, e.g. name@example.com</span>
```

When the user focuses the field, the screen reader announces:
1. The label ("Email")
2. The input type ("edit text")
3. The invalid state ("invalid")
4. The description ("Enter a valid email address...")

---

## Multiple Descriptions (Hint + Error)

Space-separate `aria-describedby` IDs to include both a persistent hint and a dynamic error:

```html
<label for="phone">Phone Number</label>
<input id="phone" type="tel"
       aria-describedby="phone-hint phone-error"
       aria-invalid="true">
<span id="phone-hint">Format: (555) 123-4567</span>
<span id="phone-error">Phone number is required.</span>
```

Screen readers announce descriptions in the order the IDs appear.

---

## Adrian Roselli's Screen Reader Test Results

Roselli tested seven screen reader/browser combinations (2023). Key findings:

### aria-describedby WITHOUT aria-live (RECOMMENDED)

| SR + Browser | Announces error on focus? | Clips next field? |
|---|---|---|
| JAWS + Chrome | Yes | No |
| JAWS + Firefox | Yes | No |
| NVDA + Chrome | Yes | No |
| NVDA + Firefox | Yes | No |
| VoiceOver + Safari (macOS) | Yes | No |
| VoiceOver + Safari (iOS) | Yes | No |
| TalkBack + Chrome (Android) | Yes | No |

**Result:** Consistently announces errors without disruption.

### aria-describedby WITH aria-live="assertive" (AVOID)

| SR + Browser | Problem |
|---|---|
| JAWS + Chrome | Double announcement (Chromium treats aria-describedby as assertive already) |
| NVDA + Chrome | Clips next field name |
| VoiceOver + Safari | Interrupts navigation flow |

**Result:** Adding `aria-live` to individual field errors causes timing conflicts.

Source: [Adrian Roselli: Exposing Field Errors](https://adrianroselli.com/2023/04/exposing-field-errors.html)

---

## aria-errormessage: Current Support Status (2024-2025)

`aria-errormessage` is the purpose-built attribute but lacks adequate support:

| Screen Reader | Support |
|---|---|
| NVDA 2024.3+ | Yes (stable) |
| iOS VoiceOver/Safari | Partial — works with `visibility: hidden`/`opacity: 0.01`, not `display: none` or `hidden` |
| TalkBack (Android) | No |
| JAWS | Unclear |

**Recommendation:** Continue using `aria-describedby`. Monitor `aria-errormessage` support via [a11ysupport.io](https://a11ysupport.io/tech/aria/aria-errormessage_attribute).

Source: [Bogdan Cerovac, 2024](https://cerovac.com/a11y/2024/06/support-for-aria-errormessage-is-getting-better-but-still-not-there-yet/)

---

## Description Limitations

From Roselli's research on accessible descriptions:

1. **Changes while focused are silent.** If you update the text content of an element referenced by `aria-describedby` while the input has focus, the screen reader will NOT re-announce it. The user must leave and re-focus the field.

2. **Descriptions are secondary.** Screen readers announce descriptions after a pause, and some users configure their SR to skip descriptions. Do not put critical-path information exclusively in descriptions.

3. **Not all SRs expose descriptions equally.** Test with multiple screen readers.

Source: [Adrian Roselli: Accessible Description Exposure](https://adrianroselli.com/2022/04/accessible-description-exposure.html)

---

## Error State Management

### Setting aria-invalid

```javascript
// After validation fails
input.setAttribute('aria-invalid', 'true');
errorEl.textContent = 'This field is required.';
errorEl.removeAttribute('hidden');

// After validation passes
input.removeAttribute('aria-invalid'); // Remove entirely, don't set to "false"
errorEl.textContent = '';
errorEl.setAttribute('hidden', '');
```

### Timing Rules

- **On page load:** Do NOT set `aria-invalid` on any field.
- **On blur (first interaction):** Set `aria-invalid="true"` only if the field was modified and is invalid.
- **On submit:** Set `aria-invalid="true"` on all invalid fields.
- **On correction:** Remove `aria-invalid` when the field becomes valid.

### Focus After Submit

```javascript
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const invalidFields = form.querySelectorAll('[aria-invalid="true"]');
  if (invalidFields.length > 0) {
    invalidFields[0].focus(); // Focus first invalid field
  }
});
```

---

## Labeling Priority

Order of preference for giving a form control an accessible name (Roselli):

1. **`<label>` with `for`/`id`** — 20+ years of support, expands click target, works with voice control
2. **`aria-labelledby`** pointing to visible text — works with voice control, supports translation
3. **Visually hidden text** (`.sr-only`) — translatable, benefits only SR users
4. **`aria-label`** — last resort. Not translatable by many tools, invisible to non-SR users

Source: [Adrian Roselli: My Priority of Methods for Labeling a Control](https://adrianroselli.com/2020/01/my-priority-of-methods-for-labeling-a-control.html)
