# Forced colors verification

Forced colors substitutes system palettes at paint time. Shadows become none;
non-URL background images are suppressed, while URL images remain. Browser
palette choices follow native semantics, not a custom ARIA role
([MDN forced-colors](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors)).

```css
.control:focus {
  outline: 3px solid #005fcc;
  outline-offset: 3px;
}
.card { border: 1px solid transparent; }
@media (forced-colors: active) {
  .control:focus { outline-color: Highlight; }
  .card { border-color: CanvasText; }
}
```

A transparent border can preserve a system-color boundary, but a transparent
outline alone is invisible in normal rendering. Keep a visible baseline and test
both modes. Do not rely on shadows alone for state indication
([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors)).

Avoid global `forced-color-adjust:none`; it disables the user's palette adaptation.
Use narrowly scoped exceptions only when the content genuinely needs its colors
and still communicates its information to users of forced colors
([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors)).

Test actual supported browser/OS forced-color modes and relevant palettes. Inspect
focus, selected/disabled states, icons, checked controls, charts, images, borders
and links. DevTools emulation is useful for a first pass; record real system-mode
checks separately. No platform support or visual outcome is guaranteed by the CSS
snippet alone.
