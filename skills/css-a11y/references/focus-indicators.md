# Focus Indicators — Reference

## `:focus-visible` vs `:focus`

`:focus` fires on every focus event (mouse click, keyboard tab, programmatic). `:focus-visible` fires only when the browser determines a focus ring is useful — typically keyboard navigation.

```css
/* Preferred: only show ring for keyboard users */
button:focus-visible {
  outline: max(1px, 0.1em) solid currentColor;
  outline-offset: 0.25em;
}
```

Using `currentColor` ensures the outline inherits the element's text color, which adapts automatically in forced-colors mode. Using `em` units scales the outline with font size.

**Source:** [Modern CSS Upgrades to Improve Accessibility](https://moderncss.dev/modern-css-upgrades-to-improve-accessibility/)

---

## Double-Outline Technique

A two-color focus indicator ensures visibility against any background color.

### Light backgrounds

```css
:focus-visible {
  outline: 3px solid black;
  box-shadow: 0 0 0 6px white;
}
```

### Dark backgrounds

```css
:focus-visible {
  outline: 3px solid white;
  box-shadow: 0 0 0 6px black;
}
```

### "Oreo" pattern (doubled inner outline)

```css
:focus-visible {
  outline: 9px double black;
  box-shadow: 0 0 0 6px white;
}
```

**Important:** The `box-shadow` component disappears in forced-colors mode. Use `outline-color: transparent` as a fallback if the outline itself is your only indicator — the transparent outline becomes visible in forced-colors mode.

**Source:** [Sara Soueidan — A Guide to Designing Accessible Focus Indicators](https://www.sarasoueidan.com/blog/focus-indicators/)

---

## `outline-offset`

- **Positive offset** (e.g., `0.25em`): separates the ring from the element edge, improving visibility.
- **Negative offset** (e.g., `-3px`): creates an inset indicator inside the element.

```css
button:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 0.25em;
}
```

**Source:** [Modern CSS Upgrades to Improve Accessibility](https://moderncss.dev/modern-css-upgrades-to-improve-accessibility/)

---

## Never `outline: none` Without Replacement

Setting `outline: none` or `outline: 0` removes focus visibility for all users, including in Windows High Contrast Mode. Many CSS resets include this.

### Safer alternative

```css
/* Hides outline visually but preserves it in forced-colors mode */
button:focus:not(:focus-visible) {
  outline-color: transparent;
}
```

If you must override the default outline, always provide a visible replacement: border change, background-color change, text-decoration, or box-shadow (with outline fallback for forced-colors).

**Sources:**
- [outlinenone.com](https://www.outlinenone.com/)
- [The A11Y Project — Never Remove CSS Outlines](https://www.a11yproject.com/posts/never-remove-css-outlines/)
- [Adrian Roselli — Keep the Focus Outline](https://adrianroselli.com/2014/06/keep-focus-outline.html)
- [Eevis Panula — Don't Set outline: 0 or outline: none](https://eevis.codes/blog/2022-07-28/dont-set-outline-0-or-outline-none-for-focus/)

---

## WCAG Criteria for Focus Indicators

| WCAG Criterion | Level | Requirement |
|---|---|---|
| 2.4.7 Focus Visible | A | Keyboard focus indicator must be visible |
| 1.4.11 Non-Text Contrast | AA | Focus indicator needs 3:1 contrast ratio against adjacent colors |
| 2.4.11 Focus Not Obscured (Minimum) | AA | Focused component not entirely hidden by author-created content (sticky headers, modals) |
| 2.4.13 Focus Appearance | AAA | Indicator area ≥ 2px thick perimeter, 3:1 contrast between focused and unfocused states |

### SC 2.4.13 Area Calculation

For a 90×30px button, the minimum indicator area is:

```
2 × (2×90 + 2×30) = 480 CSS px²
```

A 2px solid outline around the entire perimeter satisfies this. A partial underline or dot indicator likely does not.

**Source:** [WCAG 2.2 Understanding Focus Appearance](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html)
