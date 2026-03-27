---
name: cognitive-a11y
description: Guides cognitive accessibility patterns — clear actionable error messages, consistent navigation, predictable behavior, timeout handling with warnings, progress indicators for multi-step processes, consistent help placement (WCAG 2.2), and plain language. Auto-invokes when writing error messages, multi-step flows, session timeout logic, or navigation structures.
allowed-tools: Read, Glob, Grep
compatibility: "Claude Code, Codex CLI, Gemini CLI"
---

# Cognitive Accessibility Patterns

> "People who may have difficulty locating help are more likely to find it when it is consistently located."
> — [WCAG 2.2 SC 3.2.6 Understanding](https://www.w3.org/WAI/WCAG22/Understanding/consistent-help.html)

Cognitive accessibility ensures interfaces are usable by people with memory deficits, attention disorders, learning disabilities, and cognitive fatigue. These patterns benefit all users under stress, distraction, or unfamiliarity.

---

## 1. Clear Error Messages

**WCAG SC 3.3.1 Error Identification (Level A)** and **SC 3.3.3 Error Suggestion (Level AA)** require that errors are identified in text and include correction suggestions.

### Template

```
[Field name]: [What went wrong]. [How to fix it].
```

**Keep messages under 14 words.** At 8 words or fewer, comprehension reaches 100%. ([NN/g](https://www.nngroup.com/articles/error-message-guidelines/))

### Examples

```html
<!-- WRONG -->
<span class="error">Invalid input</span>
<span class="error">An error occurred</span>

<!-- RIGHT -->
<span class="error" id="email-error">
  Email: must include an @ symbol. Example: name@example.com
</span>
```

### Tone

Use positive, non-blaming language. Avoid "invalid," "illegal," or "incorrect." The system adapts — it does not blame. ([NN/g](https://www.nngroup.com/articles/error-message-guidelines/))

### Placement and ARIA

- Display errors adjacent to the field (above or beside).
- Mark the field: `aria-invalid="true"` and `aria-describedby` pointing to the error text.
- For dynamically injected errors: use `role="alert"` or `aria-live="assertive"`.
- Do NOT show errors during exploratory interaction (e.g., on first blur of an empty field before submission).

```html
<label for="email">Email</label>
<input id="email" type="email"
       aria-invalid="true"
       aria-describedby="email-error">
<span id="email-error" role="alert">
  Email: must include an @ symbol. Example: name@example.com
</span>
```

### Redundant Cues

Use multiple indicators simultaneously: text + border highlight + icon. Never rely on color alone (~350M people have color-vision deficiency). ([NN/g](https://www.nngroup.com/articles/error-message-guidelines/))

### Preserve User Input

Always allow correction by editing the original entry. Never clear form fields on validation failure. Display the user's original text even if non-compliant.

For detailed error message patterns, see: `${CLAUDE_SKILL_DIR}/references/error-message-patterns.md`

---

## 2. Consistent Navigation

**WCAG Guideline 3.2 Predictable:** Navigation elements must appear in the same relative order across all pages within a set.

### Requirements

- Navigation elements (menus, search bars, home buttons) must be in the same position on every page. Same order, same location.
- Use descriptive labels for menu items, not generic text.
- Maintain consistent terminology — do not call the same thing by different names on different pages (e.g., "Cart" on one page, "Basket" on another).
- Provide orientation aids: "you are here" indicators, breadcrumbs, and highlighted current-page links.
- Avoid automatic page refreshes or unexpected content rearrangement.

### Cognitive Rationale

People with memory deficits rely on spatial consistency. Changing navigation position forces re-learning the interface on every page. ([WebAIM](https://webaim.org/articles/cognitive/design))

---

## 3. Predictable Behavior

### SC 3.2.1 On Focus (Level A)

When a component receives focus, it must NOT initiate a change of context. Prohibited:
- Forms auto-submitting when a field receives focus
- New windows launching on focus
- Focus shifting to a different component unexpectedly

```html
<!-- WRONG — dialog opens on focus -->
<input onfocus="openHelp()">

<!-- RIGHT — help opens on explicit activation -->
<input>
<button onclick="openHelp()">Help</button>
```

### SC 3.2.2 On Input (Level A)

Changing the setting of a component must NOT automatically cause a context change unless the user was advised beforehand.

```html
<!-- WRONG — auto-submits on selection -->
<select onchange="this.form.submit()">

<!-- RIGHT — explicit submit -->
<select id="country">
<button type="submit">Apply</button>
```

**Always provide explicit submit buttons.** If auto-advance behavior exists (e.g., phone number fields advancing automatically), disclose this before the form. ([WCAG SC 3.2.2](https://www.w3.org/WAI/WCAG22/Understanding/on-input.html))

### Warn Before Irreversible Actions

Confirm before deletions, financial commitments, and other non-undoable operations. Users with cognitive disabilities may activate controls accidentally.

---

## 4. Timeout Handling

**WCAG SC 2.2.1 Timing Adjustable (Level A)** requires that for every time limit, at least one of these is true:

1. **Turn off:** User can disable the limit before encountering it.
2. **Adjust:** User can set the limit to at least 10x the default.
3. **Extend:** User is warned before expiration, given at least 20 seconds to extend with a simple action (e.g., pressing Space), and extension is available at least 10 times.

Exceptions: real-time events, essential time limits, and limits exceeding 20 hours.

### Warning Pattern

- Warn at least **2 minutes** before session expiration.
- Use a modal dialog or banner with clear language: state what will happen and offer a single action to extend.
- Use `role="alertdialog"` or `role="alert"` for the warning.
- The extension action must be achievable with a simple keypress (Space or Enter).

```html
<div role="alertdialog"
     aria-label="Session expiring"
     aria-describedby="timeout-msg">
  <p id="timeout-msg">
    Your session will end in 2 minutes.
    Unsaved work will be lost.
  </p>
  <button autofocus>Continue session</button>
</div>
```

### Data Preservation

- Preserve all user-entered data if the session expires — do not discard form progress.
- **SC 2.2.6 Timeouts (Level AAA):** Warn users of inactivity duration that causes data loss, or preserve data for at least 20 hours.

### Never Do This

- `<meta http-equiv="refresh">` for automatic page reloading
- Server-side redirects after timeout without warning
- Silent session expiry that discards user data

For implementation details, see: `${CLAUDE_SKILL_DIR}/references/timeout-handling.md`

---

## 5. Progress Indicators

For multi-step processes, provide clear progress information so users know where they are, where they've been, and what remains.

### Page Title

Include step progress before other title content — screen reader users encounter this first:

```html
<title>Step 2 of 4: Shipping Address - Complete Purchase - Shop</title>
```

### Main Heading

```html
<h1>Shipping Address (Step 2 of 4)</h1>
```

### Step Indicator List

```html
<ol aria-label="Checkout progress">
  <li>
    <span class="sr-only">Completed:</span>
    <a href="/cart">Cart</a>
  </li>
  <li aria-current="true">
    <span class="sr-only">Current:</span>
    Shipping Address
  </li>
  <li>
    <span class="sr-only">Pending:</span>
    Payment
  </li>
  <li>
    <span class="sr-only">Pending:</span>
    Review
  </li>
</ol>
```

### Visual Distinction

- Completed, current, and pending steps must have distinct visual treatments with accessible contrast.
- Current step must be the most visually prominent.
- Keep step labels short.

### Back Navigation

- Provide links to completed steps so users can review and correct previous entries.
- Use descriptive link text: "Back to payment information" not "Previous."
- Preserve all previously entered data when returning to a completed step.
- Set focus on the next relevant form element when navigating between steps.

### HTML5 Progress Element

For variable-length processes:

```html
<progress max="7" value="2">(Step 2 of circa 7)</progress>
```

Disable automatic animations on custom progress bars (WCAG SC 2.2.2). ([W3C WAI Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/multi-page/))

---

## 6. Consistent Help (WCAG 2.2)

**SC 3.2.6 Consistent Help (Level A, new in WCAG 2.2):** If a page contains any of these help mechanisms and they repeat across multiple pages, they must appear in the same relative order:

- Human contact details (phone, email, hours)
- Human contact mechanism (contact form, chat)
- Self-help option (FAQ, how-to, knowledge base)
- Automated contact mechanism (chatbot)

### Key Details

- This criterion does NOT require providing help — only that existing help is consistently positioned across pages.
- "Same relative order" refers to serialized DOM order, not just visual placement (though consistent visual placement is strongly recommended).
- Sufficient technique: G220 — provide a contact-us link in a consistent location.

```html
<!-- Footer help section — same position on every page -->
<footer>
  <nav aria-label="Help">
    <a href="/faq">FAQ</a>
    <a href="/contact">Contact us</a>
    <a href="tel:+18005551234">Call: 1-800-555-1234</a>
  </nav>
</footer>
```

---

## 7. Plain Language

**Target: approximately 8th-grade reading level.** WCAG SC 3.1.5 (Level AAA) recommends content be understandable at a lower secondary education level.

### Sentence Structure

- Keep sentences to 15-20 words maximum.
- One idea per sentence.
- Use short, simple, unambiguous phrases.

### Vocabulary

- Avoid jargon; when technical terms are required, define them inline.
- Do not use sarcasm, parody, or metaphors — users with cognitive disabilities may interpret them literally.
- Use consistent terminology: same concept = same word everywhere.

### Content Structure

- Break information into small chunks, not long paragraphs.
- Use clear headings, short sections, and bullet points.
- Add white space between elements.
- Supplement text with illustrations, icons, video, and audio where helpful.
- Use structural HTML: headings, lists, landmarks, regions.

### Provide Context

Do not assume prior knowledge. Provide necessary background information before asking users to act.

---

## 8. Common Mistakes

These are the most frequent cognitive accessibility failures. Each is cited to primary sources.

| # | Mistake | Why It Fails | Source |
|---|---------|-------------|--------|
| 1 | Relying solely on color to indicate errors | ~350M people have color-vision deficiency | [NN/g](https://www.nngroup.com/articles/error-message-guidelines/) |
| 2 | Premature error display (on blur before submission) | Punishes exploration, increases cognitive load | [NN/g](https://www.nngroup.com/articles/error-message-guidelines/) |
| 3 | Generic error messages ("An error occurred") | Users with cognitive disabilities cannot infer the problem | [WCAG SC 3.3.3](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html) |
| 4 | Auto-submitting forms on input change | Violates SC 3.2.2 | [WCAG SC 3.2.2](https://www.w3.org/WAI/WCAG22/Understanding/on-input.html) |
| 5 | Context changes on focus | Violates SC 3.2.1 | [WCAG SC 3.2.1](https://www.w3.org/WAI/WCAG22/Understanding/on-focus.html) |
| 6 | Silent session expiry | Violates SC 2.2.1; user data lost | [WCAG SC 2.2.1](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html) |
| 7 | Inconsistent help placement across pages | Violates SC 3.2.6 | [WCAG SC 3.2.6](https://www.w3.org/WAI/WCAG22/Understanding/consistent-help.html) |
| 8 | Inconsistent terminology across pages | Forces users to re-learn vocabulary | [A11Y Collective](https://www.a11y-collective.com/blog/cognitive-accessibility/) |
| 9 | No progress indication in multi-step processes | Users lose track; abandonment increases | [WebAIM](https://webaim.org/articles/cognitive/design) |
| 10 | Destroying user input on validation error | Forces re-entry of all data | [NN/g](https://www.nngroup.com/articles/error-message-guidelines/) |

For expanded examples and fixes, see: `${CLAUDE_SKILL_DIR}/references/common-mistakes.md`

---

## 9. Cross-References

Related skills in this plugin:

- `form-a11y` — form labeling, grouping, validation patterns
- `live-regions` — `aria-live`, `role="alert"`, `role="status"` patterns
- `aria-decision-framework` — when to use ARIA vs. native HTML
- `a11y-dialog` — dialog and alertdialog patterns (relevant to timeout warnings)

Related references:

- `${CLAUDE_SKILL_DIR}/references/error-message-patterns.md` — error message templates by field type
- `${CLAUDE_SKILL_DIR}/references/timeout-handling.md` — timeout implementation patterns
- `${CLAUDE_SKILL_DIR}/references/common-mistakes.md` — expanded anti-patterns with fixes
- `${CLAUDE_SKILL_DIR}/references/sources.yaml` — provenance for all cited sources
