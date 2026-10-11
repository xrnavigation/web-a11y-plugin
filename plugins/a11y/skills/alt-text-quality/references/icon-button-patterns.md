# Icon Button Labeling Patterns
## Contents

- [Core Principle](#core-principle)
- [Technique 1: Visually Hidden Text (Most Robust)](#technique-1-visually-hidden-text-most-robust)
- [Technique 2: Hidden Text with aria-labelledby](#technique-2-hidden-text-with-aria-labelledby)
- [Technique 3: aria-label on the Button](#technique-3-aria-label-on-the-button)
- [Anti-Patterns (Do NOT Use)](#anti-patterns-do-not-use)
  - [aria-label on the SVG itself](#aria-label-on-the-svg-itself)
  - [aria-labelledby referencing SVG title](#aria-labelledby-referencing-svg-title)
- [Additional Rules](#additional-rules)
- [Visually Hidden CSS](#visually-hidden-css)


Source: [Sara Soueidan — Accessible Icon Buttons](https://www.sarasoueidan.com/blog/accessible-icon-buttons/)

---

## Core Principle

Icon-only buttons have no visible text. The icon is always **decorative** within the button context — it gets `aria-hidden="true"`. The **button itself** must carry the accessible name.

---

## Technique 1: Visually Hidden Text (Most Robust)

```html
<button>
  <svg aria-hidden="true" focusable="false"><!-- icon --></svg>
  <span class="visually-hidden">Menu</span>
</button>
```

- Icon hidden from AT via `aria-hidden="true"`
- Real text provides the accessible name
- Verify the computed name and actual output in the product support matrix
- `focusable="false"` prevents double tab stop in IE

**This is the recommended default technique.**

---

## Technique 2: Hidden Text with aria-labelledby

```html
<button aria-labelledby="btn-label">
  <span id="btn-label" hidden>Menu</span>
  <svg aria-hidden="true" focusable="false"><!-- icon --></svg>
</button>
```

- `hidden` element is invisible but referenceable via `aria-labelledby`
- Useful when the label text must not be in the visual flow at all

---

## Technique 3: aria-label on the Button

```html
<button aria-label="Menu">
  <svg aria-hidden="true" focusable="false"><!-- icon --></svg>
</button>
```

- Simplest markup
- Caveat: `aria-label` needs explicit localization and translation-pipeline verification
- Caveat: if there IS visible text, `aria-label` must contain it (WCAG 2.5.3 Label in Name)

---

## Anti-Patterns (Do NOT Use)

### aria-label on the SVG itself

```html
<!-- DO NOT — fails in testing -->
<button>
  <svg aria-label="Menu"><!-- icon --></svg>
</button>
```

### aria-labelledby referencing SVG title

```html
<!-- DO NOT — fails in testing -->
<button>
  <svg aria-labelledby="icon-title">
    <title id="icon-title">Menu</title>
  </svg>
</button>
```

Both patterns had failures across browser/screen reader combinations in Sara Soueidan's testing. The icon should always be treated as decorative (`aria-hidden="true"`), and the **button itself** should carry the accessible name.

---

## Additional Rules

1. **Use native `<button>` elements** — not `<div role="button">`. Native buttons provide keyboard support (Enter/Space activation, focus management) for free.

2. **Prefer SVG over icon fonts** — test SVG strokes/fills in forced colors; using SVG alone does not guarantee visibility.

3. **`focusable="false"` on SVGs inside buttons** — prevents a double-focus issue in IE/old Edge where the SVG receives its own tab stop.

4. **Toggle buttons** — use `aria-pressed="true"` / `aria-pressed="false"` on the button while keeping the action label stable when using pressed-state semantics ([APG button](https://www.w3.org/WAI/ARIA/apg/patterns/button/)).

---

## Visually Hidden CSS

```css
.visually-hidden {
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  height: 1px;
  overflow: hidden;
  position: absolute;
  white-space: nowrap;
  width: 1px;
}
```

Do not use `display: none` or `visibility: hidden` for visually hidden text — both remove the content from the accessibility tree.
