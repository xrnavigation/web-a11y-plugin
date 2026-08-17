# Forced-Colors Mode — Reference
## Contents

- [What Is Forced-Colors Mode?](#what-is-forced-colors-mode)
- [Properties Forced to System Colors](#properties-forced-to-system-colors)
- [Properties Forced to none](#properties-forced-to-none)
- [Other Forced Values](#other-forced-values)
- [What Survives](#what-survives)
- [Transparent Outline/Border Technique](#transparent-outlineborder-technique)
- [System Color Keywords](#system-color-keywords)
  - [Important Semantic Behavior](#important-semantic-behavior)
- [forced-color-adjust](#forced-color-adjust)
- [General Approach](#general-approach)
- [currentColor for Automatic Adaptation](#currentcolor-for-automatic-adaptation)
- [Sources](#sources)


## What Is Forced-Colors Mode?

When `forced-colors: active` (Windows High Contrast Mode), the browser forcibly overrides author-specified colors with the user's chosen system palette. This is not a suggestion — the browser takes control.

---

## Properties Forced to System Colors

- `color`
- `background-color`
- `text-decoration-color`
- `text-emphasis-color`
- `border-color`
- `outline-color`
- `column-rule-color`
- SVG `fill` and `stroke`

## Properties Forced to `none`

- `box-shadow`
- `text-shadow`
- `background-image` (except `url()` values — actual images are preserved)

## Other Forced Values

- `color-scheme` → `light dark`
- `scrollbar-color` → `auto`

**Consequence:** Any visual distinction relying on `box-shadow`, background gradients, or `background-color` alone will disappear.

---

## What Survives

**Borders and outlines persist.** They are the only reliable way to convey visual boundaries and focus states in forced-colors mode.

**Images loaded via `url()` persist.** Background images specified with `url()` are not removed — only gradient and generated background-images are.

---

## Transparent Outline/Border Technique

Use transparent borders and outlines in base styles. They are invisible in normal rendering but become visible in forced-colors mode (the browser maps `transparent` to a system color).

```css
/* Invisible boundary that appears in HCM */
.card {
  border: 2px solid transparent;
}

/* Focus indicator that works everywhere */
button:focus-visible {
  outline: 3px solid transparent;
  outline-offset: 2px;
}
```

This is the single most important forced-colors technique. It solves most problems without any `@media` query.

---

## System Color Keywords

System colors map to the user's chosen high-contrast palette:

| Keyword | Maps To |
|---|---|
| `Canvas` | Background color |
| `CanvasText` | Foreground text color |
| `LinkText` | Link color |
| `ButtonText` | Button text color |
| `ButtonBorder` | Button border color |
| `Highlight` | Selected item background |
| `HighlightText` | Selected item text |
| `GrayText` | Disabled text |

### Important Semantic Behavior

System colors are assigned based on **native HTML semantics**, not ARIA roles. A `<div role="button">` will NOT automatically get `ButtonText` coloring — only a native `<button>` will. This is another reason to use native HTML elements.

---

## `forced-color-adjust`

```css
@media (forced-colors: active) {
  .color-swatch {
    forced-color-adjust: none;
  }
}
```

- `auto` (default): browser replaces colors with system palette
- `none`: element retains its original colors

**Use `none` sparingly** — only when color IS the content:
- Color pickers
- Data visualizations where color carries meaning
- Brand logos where specific colors are essential

---

## General Approach

1. **Do not create a separate design** for forced-colors users.
2. Use `@media (forced-colors: active)` only for small tweaks where default forced-colors behavior breaks usability.
3. Rely on native HTML semantics — they get correct system color treatment automatically.
4. Use transparent borders/outlines as your primary tool.
5. Test with Windows High Contrast Mode themes (both dark and light).

---

## `currentColor` for Automatic Adaptation

Icons and decorative elements using `currentColor` automatically adapt to forced-colors mode without any media query:

```css
svg {
  fill: currentColor;
  stroke: currentColor;
}
```

**Source:** [Modern CSS Solutions](https://moderncss.dev/modern-css-upgrades-to-improve-accessibility/)

---

## Sources

- [Smashing Magazine — The Guide to Windows High Contrast Mode](https://www.smashingmagazine.com/2022/06/guide-windows-high-contrast-mode/)
- [MDN — forced-colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors)
- [MS Edge Blog — Styling for Windows High Contrast](https://blogs.windows.com/msedgedev/2020/09/17/styling-for-windows-high-contrast-with-new-standards-for-forced-colors/)
- [Smashing Magazine — Windows High Contrast Mode, Forced Colors Mode and CSS Custom Properties](https://www.smashingmagazine.com/2022/03/windows-high-contrast-colors-mode-css-custom-properties/)
