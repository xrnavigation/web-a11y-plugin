---
name: css-a11y
description: Guides CSS patterns that affect accessibility — focus indicators, forced-colors mode, prefers-reduced-motion, prefers-contrast, color-only information avoidance, and target sizing. Auto-invokes when writing CSS for interactive elements, animations, transitions, media queries, or custom focus styles.
allowed-tools: Read, Glob, Grep
compatibility: "Claude Code, Codex CLI, Gemini CLI"
---

# CSS Accessibility Patterns

> "Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element."
> — [WCAG 2.1, SC 1.4.1](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html)

CSS controls what users see. When CSS removes focus indicators, ignores user preferences, or relies on color alone, it creates barriers that no amount of semantic HTML or ARIA can fix. Every visual pattern below has a direct WCAG success criterion behind it.

---

## 1. Focus Indicators

Focus indicators tell keyboard users where they are. Removing or weakening them is the most common CSS accessibility failure.

### Use `:focus-visible`, Not `:focus`

`:focus-visible` shows focus rings for keyboard navigation but not mouse clicks. This eliminates the "ugly ring on click" complaint that leads developers to remove outlines entirely.

```css
button:focus-visible {
  outline: max(1px, 0.1em) solid currentColor;
  outline-offset: 0.25em;
}
```

Using `currentColor` ensures the outline adapts in forced-colors mode. Using `em` units makes it scale with font size. ([Modern CSS Solutions](https://moderncss.dev/modern-css-upgrades-to-improve-accessibility/))

### Double-Outline Technique

A two-color indicator ensures visibility against any background:

```css
:focus-visible {
  outline: 3px solid black;
  box-shadow: 0 0 0 6px white;
}
```

For dark backgrounds, invert the colors. This satisfies SC 1.4.11 (Non-Text Contrast, 3:1 ratio) and works toward SC 2.4.13 (Focus Appearance). ([Sara Soueidan](https://www.sarasoueidan.com/blog/focus-indicators/))

### Never `outline: none` Without Replacement

Setting `outline: none` or `outline: 0` removes focus visibility for all users, including Windows High Contrast Mode users. Many CSS resets include this — always redefine focus styles when using them.

**Safer pattern:** Use `outline-color: transparent` instead of `outline: none`. This preserves the outline in forced-colors mode while hiding it visually in normal rendering. ([A11Y Project](https://www.a11yproject.com/posts/never-remove-css-outlines/); [outlinenone.com](https://www.outlinenone.com/))

### WCAG Criteria

| Criterion | Level | Requirement |
|---|---|---|
| 2.4.7 Focus Visible | A | Keyboard focus indicator must be visible |
| 1.4.11 Non-Text Contrast | AA | Focus indicator needs 3:1 contrast against adjacent colors |
| 2.4.11 Focus Not Obscured (Min) | AA | Focused component not entirely hidden by other content |
| 2.4.13 Focus Appearance | AAA | Indicator area ≥ 2px thick perimeter, 3:1 contrast between focused/unfocused states |

For details, see: `${CLAUDE_SKILL_DIR}/references/focus-indicators.md`

---

## 2. Forced-Colors Mode

When `forced-colors: active` (Windows High Contrast Mode), the browser forcibly overrides colors, shadows, and background images. Visual distinctions that rely on `box-shadow`, background gradients, or `background-color` alone disappear.

### What Survives

Borders and outlines persist. They are the only reliable way to convey visual boundaries and focus states.

### Transparent Outline/Border Pattern

Use transparent borders in base styles — invisible normally, visible in forced-colors mode:

```css
.card {
  border: 2px solid transparent;
}

button:focus-visible {
  outline: 3px solid transparent;
  outline-offset: 2px;
}
```

### System Color Keywords

System colors map to the user's high-contrast palette: `Canvas`, `CanvasText`, `LinkText`, `ButtonText`, `ButtonBorder`, `Highlight`, `HighlightText`, `GrayText`. These are assigned based on native HTML semantics — a `<div role="button">` does NOT get `ButtonText` coloring.

### `forced-color-adjust: none`

Use only when color IS the content (color pickers, data visualizations). Do not create a separate design for forced-colors users — use the media query only for small fixups.

```css
@media (forced-colors: active) {
  .color-swatch {
    forced-color-adjust: none;
  }
}
```

For details, see: `${CLAUDE_SKILL_DIR}/references/forced-colors-mode.md`

([Smashing Magazine](https://www.smashingmagazine.com/2022/06/guide-windows-high-contrast-mode/); [MDN forced-colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors))

---

## 3. `prefers-reduced-motion`

The goal is to reduce vestibular-triggering motion, not to strip all animation. Some transitions (list reflow, gentle fades) actively help comprehension.

### Replace, Don't Remove

```css
.hero-image {
  animation: slide-in 0.6s ease-out;
}

@media (prefers-reduced-motion: reduce) {
  .hero-image {
    animation: fade-in 0.3s ease-out; /* Replace, don't remove */
  }
}
```

The global nuclear option (`animation-duration: 0.01ms !important` on `*`) is a last resort — it removes meaningful transitions alongside problematic ones.

### Smooth Scrolling

Only enable smooth scrolling when the user has no motion preference:

```css
@media (prefers-reduced-motion: no-preference) {
  html { scroll-behavior: smooth; }
}
```

### On-Page Controls

WCAG requires a pause mechanism for any movement lasting more than 5 seconds. Provide an on-page toggle in addition to respecting the OS preference.

([MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion); [W3C Technique C39](https://www.w3.org/WAI/WCAG21/Techniques/css/C39))

---

## 4. `prefers-contrast`

### When It Matters

- **macOS "Increase Contrast"** fires `prefers-contrast: more`. Your styles apply — the author retains color control.
- **Windows High Contrast** fires `forced-colors: active`. The browser overrides colors; `prefers-contrast` styles may be invisible.

Target `prefers-contrast: more` for macOS users and similar environments where you keep color control:

```css
@media (prefers-contrast: more) {
  :root {
    --border-color: black;
    --text-secondary: #333;  /* was #666 */
    --bg-subtle: white;      /* was #f5f5f5 */
  }

  .card {
    border: 2px solid var(--border-color);
  }
}
```

([MDN prefers-contrast](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-contrast); [Kilian Valkhof](https://kilianvalkhof.com/2023/css-html/i-no-longer-understand-prefers-contrast/))

---

## 5. Color-Only Information

WCAG 1.4.1 prohibits using color as the only visual means of conveying information.

### Common Violations

- Required fields indicated only by red border
- Links distinguished from body text only by color (no underline)
- Status badges using only green/red/yellow
- Chart series differentiated only by color
- Error messages in red text without icon or label

### Compliant Patterns

**Status indicators — color + icon + text:**
```css
.status-success::before { content: "\2713 "; /* checkmark */ }
.status-error::before { content: "\2717 "; /* X mark */ }
```

**Links — underline or non-color indicator:**
```css
a {
  color: #0066cc;
  text-decoration: underline;
}
```

If removing underlines (e.g., in navs), provide other visual distinction: font-weight, border-bottom, icon, or background change on hover/focus.

**Grayscale test:** View the interface in grayscale. If you cannot distinguish states, the design relies on color alone.

([W3C SC 1.4.1](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html))

---

## 6. Target Size

WCAG 2.5.8 (Level AA): Interactive targets must be at least **24 × 24 CSS pixels**.

```css
button, a, input, select, textarea {
  min-height: 24px;
  min-width: 24px;
}

/* Better: comfortable for touch */
button, [role="button"] {
  min-height: 44px;
  min-width: 44px;
}
```

### Responsive Sizing with `max()`

```css
.avatar-grid {
  grid-template-columns: repeat(auto-fill, max(44px, 3rem));
}
```

### Device-Aware Targets

```css
.control { min-height: 44px; }

@media (any-hover: hover) and (any-pointer: fine) {
  .control { min-height: 24px; }
}
```

### Five Exceptions

1. **Spacing** — undersized but circles (24px diameter) don't overlap with adjacent targets
2. **Equivalent** — another same-page control meets the requirement
3. **Inline** — target within a sentence, constrained by line-height
4. **User agent control** — size determined by the browser (native checkboxes)
5. **Essential** — position is fundamental to meaning (map pins, data points)

([WCAG 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html))

---

## 7. Common Mistakes

These are the most frequent CSS accessibility failures. Each is cited.

1. **`outline: none` in CSS resets** without replacement focus styles. Breaks keyboard navigation and forced-colors mode. ([outlinenone.com](https://www.outlinenone.com/); [WebAIM](https://webaim.org/blog/plague-of-outline-0/))

2. **`box-shadow` for focus indication.** Disappears in forced-colors mode. Use `outline` instead. ([Smashing Magazine](https://www.smashingmagazine.com/2022/06/guide-windows-high-contrast-mode/))

3. **Color alone for status/error states.** Invisible to color-blind users. Violates SC 1.4.1. ([W3C SC 1.4.1](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html))

4. **Removing all animation** with `prefers-reduced-motion` instead of replacing with gentler alternatives. ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion))

5. **`:focus` instead of `:focus-visible`.** Shows rings on mouse click, leading developers to remove them entirely. ([Sara Soueidan](https://www.sarasoueidan.com/blog/focus-indicators/))

6. **CSS visual reordering breaking tab order.** `order`, `flex-direction: row-reverse`, grid placement make visual order diverge from DOM/focus order. ([Modern CSS Solutions](https://moderncss.dev/modern-css-upgrades-to-improve-accessibility/))

7. **Styling by class instead of attribute for state.** `.is-disabled` instead of `[disabled]`, `.is-open` instead of `[aria-expanded="true"]`. CSS should key off accessibility semantics. ([Adrian Roselli](https://adrianroselli.com/2021/06/using-css-to-enforce-accessibility.html))

For the full list with code examples, see: `${CLAUDE_SKILL_DIR}/references/common-mistakes.md`

---

## 8. Cross-References

Related skills:
- `aria-decision-framework` — when CSS focus styles interact with ARIA widgets, the framework determines which HTML elements to use; this skill determines how to style them
- `focus-management` — programmatic focus movement complements CSS focus indicators

Related references:
- `${CLAUDE_SKILL_DIR}/references/focus-indicators.md` — detailed focus indicator patterns and WCAG criteria
- `${CLAUDE_SKILL_DIR}/references/forced-colors-mode.md` — complete forced-colors property behavior and system colors
- `${CLAUDE_SKILL_DIR}/references/common-mistakes.md` — expanded anti-patterns with before/after code
- `${CLAUDE_SKILL_DIR}/references/sources.yaml` — provenance for all cited sources
