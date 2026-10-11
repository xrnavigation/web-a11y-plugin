# Focus indicator checks

## Conditions

2.4.7 is AA and requires visible keyboard focus in a mode of operation. 1.4.11 AA
covers required author-created state information at 3:1 against adjacent colors,
with exceptions. 2.4.13 AAA adds qualifying changed area and focused/unfocused
contrast requirements. Do not equate any two-pixel outline with a passing result
([Focus visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html),
[Non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html),
[Focus appearance](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html)).

## Visible baseline example

```css
.control:focus { outline: 3px solid #005fcc; outline-offset: 3px; }
@media (forced-colors: active) {
  .control:focus { outline-color: Highlight; }
}
```

Verify each theme and surrounding color; this example is not universally suitable.
Browser `:focus-visible` heuristics may include programmatic or pointer focus, not
only keyboard. Keep a working baseline if altering the heuristic-based presentation
([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible)).

Test Tab/Shift+Tab, programmatic recovery, sticky headers, scroll containers,
overflow clipping, zoom and forced colors. Record rendered evidence, not just the
presence of CSS declarations. Shadows disappear in forced colors, so retain an
outline/border fallback
([MDN forced-colors](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors)).
