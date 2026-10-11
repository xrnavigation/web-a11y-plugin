---
name: zoom-reflow
description: Guides responsive layouts through browser zoom, text resizing, and text-spacing overrides. Use when fixing clipped labels, overflow, sticky overlays, fixed-height containers, or layouts that must reflow at 320 CSS pixels.
---

# Zoom, Text Resizing, and Reflow

Preserve readable content and usable controls as users enlarge or space text. Apply this skill to layout changes; use `css-a11y` for contrast and focus styling.

## Requirements and guidance

The following are WCAG 2.2 **AA requirements**; the linked Understanding documents explain their application and are informative, not additional requirements. ([WCAG 2.2](https://www.w3.org/TR/WCAG22/))

| Criterion | Required outcome |
|---|---|
| 1.4.4 Resize Text | Except captions and images of text, resize text up to 200% without assistive technology or lost content/functionality. |
| 1.4.10 Reflow | Preserve content/functionality without two-dimensional scrolling at 320 CSS px width for vertically scrolling content, or 256 CSS px height for horizontally scrolling content. Except parts requiring two-dimensional layout for usage or meaning. |
| 1.4.12 Text Spacing | In markup supporting these properties, tolerate simultaneous overrides, changing no other property: line height at least 1.5×, paragraph spacing 2×, letter spacing 0.12×, word spacing 0.16× font size. Apply only applicable properties for the language/script; preserve content/functionality. |

These are outcome requirements. `rem` units, a mobile breakpoint, or an overflow assertion alone do not establish those outcomes. This skill's CSS patterns and testing workflow are **project guidance**, not mandated implementations.

## Build an adaptable layout

- Let text containers grow and labels wrap; avoid fixed block sizes with clipped overflow. Check controls and error messages as well as prose. ([Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html))
- Stack independent columns when space is insufficient; keep displaced navigation and actions available. Use a local scroll region for essential tables/maps as a project preference, and verify surrounding headings, controls, and table cells still reflow. A table exception does not exempt an entire page. ([Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html))
- Prefer fluid sizing, shrinkable grid tracks, and wrapping in the implementation below; media queries and grid are one documented technique, not the only route. ([C32](https://www.w3.org/WAI/WCAG22/Techniques/css/C32))
- Avoid counteracting zoom by shrinking text at narrow breakpoints. Verify an actual doubling of rendered text remains possible across layout changes; keeping every breakpoint's text size unchanged is not itself a requirement. ([Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html))
- At narrow or short viewports, make obstructing sticky regions static, collapsible, or dismissible. Check that content and controls remain reachable. ([Reflow, sticky content](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html))

Example project CSS; replace selectors and the breakpoint to fit actual content:

```css
* { box-sizing: border-box; }
html { font-size: 100%; }
body { margin: 0; }
.layout {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 2fr);
  gap: 1rem;
  padding: 1rem;
}
.layout > * { min-inline-size: 0; }
p, label, button, .error { overflow-wrap: anywhere; }
button, input, select, textarea { font: inherit; }
button { white-space: normal; }
.notice { padding: 1rem; } /* Content determines height. */
img, video { max-inline-size: 100%; block-size: auto; }
.table-scroll { max-inline-size: 100%; overflow: auto; }
.table-scroll th, .table-scroll td {
  max-inline-size: 16rem;
  white-space: normal;
  overflow-wrap: anywhere;
}
@media (max-width: 48rem) {
  .layout { grid-template-columns: minmax(0, 1fr); }
}
@media (max-width: 40rem), (max-height: 24rem) {
  .sticky-tools { position: static; }
}
```

Treat this as a starting point: short identifiers, code, and content requiring exact whitespace may need a separate presentation. Do not hide overflow to make a screenshot look clean. ([Reflow, meaningful formatting](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html))

## Verify behavior

Use the [manual matrix and viewport regression example](references/test-matrix.md). Test actual browser zoom, text resizing, and spacing separately; record browser, route/state, viewport, settings, and observations. Inspect hidden menus, dialogs, validation, long translations, and sticky controls. Report which checks were executed; do not describe authored examples as browser or screen-reader test results.

Read [common mistakes](references/common-mistakes.md) when diagnosing overflow. Consult [source provenance](references/sources.yaml) before changing numeric requirements.
