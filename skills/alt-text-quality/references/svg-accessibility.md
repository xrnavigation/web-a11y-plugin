# SVG Accessibility Patterns

Sources: [Scott O'Hara](https://www.scottohara.me/blog/2019/05/22/contextual-images-svgs-and-a11y.html), [Deque](https://www.deque.com/blog/creating-accessible-svgs/)

---

## Pattern 1: Meaningful Inline SVG (with tooltip)

```html
<svg role="img" focusable="false" aria-labelledby="svg-title">
  <title id="svg-title">Descriptive name here</title>
  <use xlink:href="#icon-id" aria-hidden="true" />
</svg>
```

- `role="img"` — ensures announced as "image" or "graphic" across screen readers
- `<title>` — provides the accessible name and a native tooltip on hover
- `aria-labelledby` pointing to the `<title>` — most robust cross-browser pattern
- `aria-hidden="true"` on `<use>` — prevents redundant announcements or bugs where accessible name is ignored
- `focusable="false"` — prevents keyboard focus in IE/old Edge

Compatibility: "properly announce the SVG as an 'image' or 'graphic' in all tested screen reader and browser pairings" (Scott O'Hara)

---

## Pattern 2: Meaningful Inline SVG (without tooltip)

```html
<svg role="img" aria-label="Descriptive name" focusable="false">
  <use xlink:href="#icon-id" aria-hidden="true"></use>
</svg>
```

Use `aria-label` instead of `<title>` when you do not want a native tooltip on hover.

---

## Pattern 3: Complex SVG (with description)

```html
<svg role="img" aria-labelledby="chart-title chart-desc">
  <title id="chart-title">Q3 Sales Overview</title>
  <desc id="chart-desc">Bar chart showing sales increasing from $2M in July to $3.5M in September</desc>
  <!-- SVG content -->
</svg>
```

`aria-labelledby` references both `<title>` and `<desc>` IDs, separated by a space. Most reliable pattern for complex SVGs per Deque testing.

---

## Pattern 4: Decorative SVG

```html
<svg aria-hidden="true" focusable="false">
  <!-- decorative content -->
</svg>
```

Without `aria-hidden="true"`, some screen readers announce decorative SVGs as a "group" with no name, which is confusing.

---

## Pattern 5: SVG in Interactive Element (button/link)

```html
<button>
  <svg aria-hidden="true" focusable="false"><!-- icon --></svg>
  <span class="visually-hidden">Search</span>
</button>
```

The SVG is decorative *within the button context*. The button gets its accessible name from the text. Never rely on SVG `<title>` or `aria-label` on the SVG itself for button labeling — it fails across browser/screen reader combinations (Scott O'Hara testing).

---

## Critical Implementation Notes

1. **Design tool exports:** SVGs exported from Figma, Illustrator, and Sketch often have unhelpful `<title>` elements like "Layer 1" or "Untitled". Remove or replace these — they produce confusing screen reader announcements.

2. **Avoid `aria-describedby` on SVGs** for the description — support is inconsistent across screen readers.

3. **Add `aria-hidden="true"` to child `<use>` elements** to prevent redundant announcements.

4. **Prefer SVGs over icon fonts** — SVGs work in Windows High Contrast Mode; icon fonts may not render correctly.

5. **`focusable="false"`** is needed on all SVGs that should not receive keyboard focus (IE/old Edge treat SVGs as focusable by default).
