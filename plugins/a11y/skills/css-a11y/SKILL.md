---
name: css-a11y
description: Guides visible focus, forced colors, contrast, reduced motion and accessible target styling. Use when changing interactive CSS, focus rings, animations, visual state cues or theme adaptations.
---

# CSS accessibility

Keep states and controls perceptible across themes and input methods. Distinguish
WCAG thresholds from this collection's implementation recommendations.

## Visible focus

Preserve browser focus indication or provide a tested replacement. `:focus-visible`
uses browser heuristics; it does not mean keyboard-only in every situation. A
visible `:focus` baseline is a useful project choice for programmatic/pointer focus
as well ([Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html),
[MDN focus-visible](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible)).

```css
button:focus {
  outline: 3px solid #005fcc;
  outline-offset: 3px;
}
@media (forced-colors: active) {
  button:focus { outline-color: Highlight; }
}
```

This is a sample for a tested light theme, not a guarantee on every background.
Check actual adjacent colors, clipping and sticky overlays. Transparent outlines
need another visible indicator in normal colors; `outline: none` alone removes it
([Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)).

| Criterion | Level | Check |
|---|---|---|
| 2.4.7 Focus Visible | AA | A mode with visible keyboard focus |
| 1.4.11 Non-text Contrast | AA | Required visual control/state information meets 3:1 adjacent contrast, with exceptions |
| 2.4.11 Focus Not Obscured (Minimum) | AA | Component not entirely hidden by author content |
| 2.4.13 Focus Appearance | AAA | Qualifying changed indicator area and 3:1 focused/unfocused contrast, with exceptions |

Read the actual conditions in [WCAG 2.2](https://www.w3.org/TR/WCAG22/); do not
teach the AAA perimeter/change-contrast requirement as an AA focus-ring rule.

## Forced colors and contrast preferences

Shadows and gradients can disappear in forced colors. Retain real borders/outlines
and test system colors; avoid disabling user color adaptation globally with
`forced-color-adjust:none`. Background images are not all removed: URL images and
non-URL images have different forced-color behavior
([MDN forced-colors](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors)).

```css
.card { border: 1px solid transparent; }
@media (forced-colors: active) {
  .card { border-color: CanvasText; }
}
```

`prefers-contrast` and `forced-colors` represent different preferences/features;
do not infer a specific OS or absence of another preference from either
([MDN prefers-contrast](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-contrast)).

## Color and motion

Do not convey information by color alone. Keep visible text/icons/patterns for
errors, selection and charts. Normal text contrast is 4.5:1, large text 3:1 at AA,
with criterion exceptions; evaluate actual foreground/background combinations
([Use of color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html),
[Contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)).

```css
@media (prefers-reduced-motion: reduce) {
  .decorative-spinner { animation: none; }
  html { scroll-behavior: auto; }
}
```

As project guidance, reduce nonessential motion while retaining meaningful status
text. Do not depend on animation-end events for required functionality. Reduced
motion is a preference, not a substitute for pause controls or flash testing
([MDN reduced motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)).
SC 2.2.2 A requires pause/stop/hide for automatically starting moving/blinking/
scrolling information lasting over five seconds and presented alongside other
content, unless essential; auto-updating information has a separate branch without
that five-second threshold
([Pause Stop Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)).

## Targets and layout

SC 2.5.8 AA requires 24 by 24 CSS pixel targets or a qualifying exception, including
its precise spacing construction. Forty-four CSS pixels is a useful project target
and appears in 2.5.5 AAA with different exceptions; do not confuse the levels
([Target minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html),
[Target enhanced](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html)).

```css
.action { min-inline-size: 2.75rem; min-block-size: 2.75rem; }
```

Measure the rendered hit area in CSS pixels: rem depends on root font size. Do not
shrink controls because `any-pointer:fine` matches; hybrid devices may also have
touch. Keep DOM and visual order meaningful and verify keyboard traversal
([MDN any-pointer](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/any-pointer),
[Focus order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html)).

Use `zoom-reflow` for resizing/spacing, `pointer-gestures` for pointer alternatives.
Read [focus indicators](references/focus-indicators.md),
[forced colors](references/forced-colors-mode.md),
[common mistakes](references/common-mistakes.md) and [sources](references/sources.yaml).
