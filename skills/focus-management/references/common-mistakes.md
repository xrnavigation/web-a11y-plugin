# Common Focus Management Mistakes — Reference

Every mistake below is cited from accessibility practitioner research or specification analysis.

---

## 1. Removing Focus Outline Globally

```css
/* WRONG */
*:focus { outline: none; }
```

This destroys keyboard accessibility for every interactive element on the page. Adrian Roselli recommends "not just keeping the focus for all interactive controls, but also going beyond the browser defaults" with custom, high-visibility focus indicators.

**Fix:** Customize the outline rather than removing it. Use `:focus-visible` for mouse-click aesthetics, but keep `:focus` as the baseline for all assistive technology users.

```css
/* RIGHT */
:focus {
  outline: 2px solid #005fcc;
  outline-offset: 2px;
}
:focus:not(:focus-visible) {
  outline: none; /* Only hide for mouse clicks */
}
```

Source: [Adrian Roselli — Keep the Focus Outline](https://adrianroselli.com/2014/06/keep-focus-outline.html)

---

## 2. Not Restoring Focus on Modal Close

> "When the close button is hidden the body element will be focused by default, which will force keyboard users to step through the page manually to find where they left off."

**Fix:** Store `document.activeElement` before opening the modal. Call `.focus()` on it when the modal closes.

Source: [Medium — Stop Breaking Modal Accessibility](https://medium.com/@alexdev82/stop-breaking-modal-accessibility-the-focus-management-mistake-90-of-devs-make-9605bad927e2)

---

## 3. Placing Initial Focus on Destructive Actions

Opening a delete confirmation dialog and auto-focusing the "Delete" button risks accidental activation — keyboard users may press Enter/Space reflexively.

**Fix:** Focus the cancel/close button or the dialog heading instead.

Source: [Adrian Roselli — Dialog Focus in Screen Readers](https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html)

---

## 4. No Focus Management on SPA Route Changes

> "When navigation happens without page reloads, screen readers don't automatically announce changes, and when DOM updates happen dynamically, focus can get lost."

**Fix:** On every client-side route change, move focus to the `<h1>` (with `tabindex="-1"`) and update `document.title`.

Source: [Deque — Accessibility Tips in Single-Page Applications](https://www.deque.com/blog/accessibility-tips-in-single-page-applications/)

---

## 5. Using `display: none` on Skip Links

```css
/* WRONG — removes from keyboard navigation */
.skip-link { display: none; }
.skip-link:focus { display: block; }
```

`display: none` removes the element from the accessibility tree and keyboard tab order. The link cannot receive focus, so the `:focus` rule never activates.

**Fix:** Position off-screen and reveal on focus:

```css
.skip-link {
  position: absolute;
  top: -40px;
}
.skip-link:focus {
  top: 0;
}
```

Source: [WebAIM — Skip Navigation Links](https://webaim.org/techniques/skipnav/)

---

## 6. Ignoring the Trigger-Removed Edge Case

If the element that opened a modal is removed from the DOM while the modal is open (e.g., confirming a row deletion), focus falls to `<body>` on close, stranding keyboard users.

**Fix:** Before restoring focus, verify the trigger element still exists in the DOM. Fall back to: previous sibling's control → containing element → `<main>` → skip-nav target. Never let focus fall to `<body>`.

Source: [Bootstrap Issue #12364](https://github.com/twbs/bootstrap/issues/12364)

---

## 7. Relying Solely on `:focus-visible`

> "Voice users, touch users, sighted screen reader users" may not see `:focus-visible` styles.

`:focus-visible` is a progressive enhancement for mouse users, not a replacement for `:focus`.

**Fix:** Use `:focus` as the baseline. Layer `:focus-visible` on top for visual refinement.

Source: [Adrian Roselli — Where to Put Focus When Deleting a Thing](https://adrianroselli.com/2023/08/where-to-put-focus-when-deleting-a-thing.html)

---

## 8. Not Using `scroll-padding` with Sticky Headers

Focused elements disappear under sticky headers/footers when keyboard users tab through the page, failing WCAG 2.4.11 (Focus Not Obscured).

**Fix:** Apply `scroll-padding` to the scroll container:

```css
html, body {
  scroll-padding-top: 6rem;
  scroll-padding-bottom: 4rem;
}
```

Source: [TetraLogical — Sticky content: focus in view](https://tetralogical.com/blog/2023/06/08/focus-in-view/)

---

## 9. Testing with Only One Screen Reader

Adrian Roselli's testing found "significant inconsistencies across screen readers" in dialog focus behavior. What works in NVDA may fail in JAWS or VoiceOver.

**Fix:** Test with at least two combinations:
- NVDA + Firefox (Windows)
- VoiceOver + Safari (macOS)
- JAWS + Chrome (Windows) if possible

Source: [Adrian Roselli — Dialog Focus in Screen Readers](https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html)
