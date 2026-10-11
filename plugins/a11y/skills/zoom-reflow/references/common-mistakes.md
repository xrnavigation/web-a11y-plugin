# Common mistakes

## Fixed-height text boxes

Clipping resized or spaced text can lose content. ([Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html), [Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html))

```css
/* Wrong: extra lines disappear. */
.message { height: 3rem; overflow: hidden; }
/* Right: project pattern that allows the box to grow. */
.message { min-block-size: 3rem; padding: 0.75rem; }
```

## Hiding page overflow

An overflow-free document is not evidence that all content is available. Inspect clipped descendants and missing functionality. ([Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html))

```css
/* Wrong: masks inaccessible offscreen controls. */
body { overflow-x: hidden; }
.toolbar { width: 900px; }
/* Right: wrap ordinary controls; inspect their contents at zoom. */
.toolbar { display: flex; flex-wrap: wrap; gap: 0.5rem; }
```

## Broad two-dimensional exceptions

A data table's necessary geometry does not exempt its heading or pagination; keep the exception scoped to content whose usage or meaning requires it. ([Reflow, scope of exceptions](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html))

```html
<!-- Wrong: wide wrapper forces ordinary content offscreen. -->
<div style="min-width: 900px"><h2>Sales</h2><table>...</table></div>
<!-- Right: project pattern isolates the necessary scrolling. -->
<h2 id="sales-heading">Sales</h2>
<div class="table-scroll" tabindex="0" role="region"
     aria-labelledby="sales-heading"><table>...</table></div>
```

Give a focusable scroll region a visible focus style; exercise keyboard scrolling in target browsers. Use the existing keyboard/focus skills for interaction details. The example's extra focus stop is a project choice, not required by Reflow.

## Treating spacing values as author defaults

The criterion tests override tolerance; it does not require the page's default typography to use the test values. ([Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html))

```css
/* Wrong: fixed single-line height breaks after spacing overrides. */
.heading { height: 1.2em; overflow: hidden; }
/* Right: user-set line height can change the block's height. */
.heading { line-height: 1.2; }
```

## Shrinking fonts to cancel zoom

`rem` is not proof of text enlargement. Check whether breakpoint changes offset browser zoom; 200% text enlargement must remain possible. ([Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html))

```css
/* Wrong as an automatic fix for narrow layouts: examine actual enlargement. */
@media (max-width: 40rem) { body { font-size: 0.5rem; } }
/* Right as project guidance: adapt columns and let labels wrap. */
@media (max-width: 40rem) { .layout { grid-template-columns: 1fr; } }
```
