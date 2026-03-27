# Common CSS Accessibility Mistakes — Reference

## 1. `outline: none` in CSS Resets

**Problem:** Removes focus visibility for all users, including in Windows High Contrast Mode. Many CSS resets (normalize, Eric Meyer's reset) include `outline: 0` or `outline: none`.

**Fix:**
```css
/* Instead of outline: none, use transparent + replacement */
button:focus:not(:focus-visible) {
  outline-color: transparent;
}

button:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 0.25em;
}
```

**Sources:** [outlinenone.com](https://www.outlinenone.com/); [WebAIM — The Plague of outline:0](https://webaim.org/blog/plague-of-outline-0/)

---

## 2. `box-shadow` as Focus Indicator

**Problem:** `box-shadow` disappears entirely in forced-colors mode. Users relying on Windows High Contrast Mode see no focus indicator at all.

**Fix:** Use `outline` as the primary indicator. If you want the visual appearance of a box-shadow focus ring in normal mode, layer it:

```css
button:focus-visible {
  outline: 3px solid transparent; /* visible in forced-colors */
  box-shadow: 0 0 0 3px #4a90d9;  /* visible in normal mode */
}
```

**Source:** [Smashing Magazine — The Guide to Windows High Contrast Mode](https://www.smashingmagazine.com/2022/06/guide-windows-high-contrast-mode/)

---

## 3. Color Alone for Status/Error States

**Problem:** Status indicators using only color (green = success, red = error) are invisible to color-blind users (~8% of males). Violates WCAG 1.4.1.

**Fix:** Add shape, icon, or text alongside color:

```css
/* Bad */
.status-success { color: green; }
.status-error { color: red; }

/* Good */
.status-success::before { content: "\2713 "; /* checkmark */ }
.status-error::before { content: "\2717 "; /* X mark */ }
```

**Source:** [W3C Understanding SC 1.4.1: Use of Color](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html)

---

## 4. Removing All Animation with `prefers-reduced-motion`

**Problem:** The global `animation-duration: 0.01ms !important` pattern kills all animation, including meaningful transitions (list reflow, state changes) that aid comprehension.

**Fix:** Replace problematic animations individually:

```css
.hero-image {
  animation: slide-in 0.6s ease-out;
}

@media (prefers-reduced-motion: reduce) {
  .hero-image {
    animation: fade-in 0.3s ease-out; /* gentler alternative */
  }
}
```

**Source:** [MDN — prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)

---

## 5. `:focus` Instead of `:focus-visible`

**Problem:** `:focus` shows focus rings on mouse click, which looks unpolished. Developers respond by adding `outline: none`, breaking keyboard accessibility. The root cause was using `:focus` instead of `:focus-visible`.

**Fix:**
```css
/* Only show focus ring for keyboard users */
button:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 0.25em;
}
```

**Source:** [Sara Soueidan — A Guide to Designing Accessible Focus Indicators](https://www.sarasoueidan.com/blog/focus-indicators/)

---

## 6. CSS Visual Reordering Breaking Tab Order

**Problem:** CSS properties that change visual order — `order`, `flex-direction: row-reverse`, `grid-row`/`grid-column` placement — make the visual reading order diverge from the DOM (and therefore tab) order. Keyboard users tab through elements in an unexpected sequence.

**Fix:** Keep DOM order aligned with visual order. If reordering is necessary, ensure the DOM order matches the intended reading/interaction sequence. Use CSS Grid's `grid-auto-flow: column` with `grid-template-rows` to create multi-column layouts that preserve logical tab order.

**Source:** [Modern CSS Upgrades to Improve Accessibility](https://moderncss.dev/modern-css-upgrades-to-improve-accessibility/)

---

## 7. Styling by Class Instead of Attribute for State

**Problem:** Using `.is-disabled` instead of `[disabled]`, `.is-open` instead of `[aria-expanded="true"]`. This creates two sources of truth — the CSS class and the actual accessibility state can diverge.

**Fix:** Style off the semantic attribute directly:

```css
/* Bad */
.btn.is-disabled { opacity: 0.5; }

/* Good — CSS tracks the actual accessibility state */
button[disabled] { opacity: 0.5; }

/* Bad */
.dropdown.is-open .dropdown-menu { display: block; }

/* Good */
[aria-expanded="true"] + .dropdown-menu { display: block; }
```

This ensures visual presentation always matches what assistive technology sees.

**Source:** [Adrian Roselli — Using CSS to Enforce Accessibility](https://adrianroselli.com/2021/06/using-css-to-enforce-accessibility.html)

---

## 8. Tiny Touch Targets

**Problem:** Interactive elements below 24×24 CSS pixels without adequate spacing. Common in icon buttons, close buttons, inline action links, and mobile interfaces.

**Fix:**
```css
button, [role="button"] {
  min-height: 44px; /* comfortable for touch */
  min-width: 44px;
}

/* If 44px is too large for the design, 24px is the AA minimum */
@media (any-hover: hover) and (any-pointer: fine) {
  button, [role="button"] {
    min-height: 24px;
    min-width: 24px;
  }
}
```

**Source:** [WCAG 2.2 Understanding Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
