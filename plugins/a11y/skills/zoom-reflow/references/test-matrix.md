# Reproducible layout checks

These are suggested project checks, not a complete WCAG conformance audit. Numeric targets come from [Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html), [Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html), and [Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html).

For each row record route, data/locale, open UI state, browser/OS, initial and resulting CSS viewport, setting, actual result, and any scoped exception. Run against the project's supported browsers. Use representative long labels, empty/populated states, validation, dialogs, expanded navigation, and loading/error states.

| Check | Procedure | Observe |
|---|---|---|
| Text enlargement | Start at 100%; use a supported resizing mechanism through intermediate steps to 200%. | Text actually doubles; labels, messages, and controls remain available and usable. |
| Text-only resizing | Where supported, enlarge only text to 200%. This is a resilience check when another mechanism already meets 1.4.4. | Containers grow; no overlaps or missing label text. |
| Vertical page reflow | Use a 320 CSS px viewport; separately exercise actual browser zoom. Starting at a 1280 CSS px viewport, 400% zoom corresponds to 320 CSS px; measure the resulting viewport rather than assuming screen resolution. | Ordinary content can be read with vertical scrolling alone; functionality remains available. |
| Horizontal page reflow | For content designed to scroll horizontally, test at 256 CSS px viewport height; separately zoom from an appropriate starting height. | Ordinary content requires horizontal scrolling alone. |
| Essential 2D regions | Test map/table content and its neighboring headings, inputs, captions, pagination, and cells. | Document the reason for the exception; ordinary surrounding content reflows. |
| Sticky content | Scroll and operate at narrow and short viewports, including 400% browser zoom. | Fixed controls do not block reading or prevent access to actions. |
| Spacing | Apply the four overrides simultaneously, changing no other style property. Verify computed values and repeat in reachable UI states. | No clipping, overlap, or lost actions. Use only relevant properties for the language/script. |
| Combined stress | Combine zoom and spacing, then use long translations. This extends the individual criterion checks. | Record resilience findings separately from individual WCAG failures. |

## Spacing override

Apply in a temporary test stylesheet. Ensure it reaches frames/shadow content where applicable, and inspect computed styles; a test tool's failed injection is not evidence of a page failure. ([Text Spacing, user responsibility](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html))

```css
* {
  line-height: 1.5 !important;
  letter-spacing: 0.12em !important;
  word-spacing: 0.16em !important;
}
p { margin-block-end: 2em !important; }
```

Target actual paragraph elements/components as needed, without changing additional properties. If existing spacing exceeds a threshold, preserve at least that larger value. This sample's blanket selector is a diagnostic tool, not production CSS or proof that every text node was covered.

## Viewport regression sample

Adapt this Playwright project example to an existing fixture, URL, and selectors. It uses documented [viewport emulation](https://playwright.dev/docs/emulation#viewport) and [bounding box measurement](https://playwright.dev/docs/api/class-locator#locator-bounding-box). It checks one layout constraint and one visible action; it does not emulate browser zoom, verify text enlargement, catch clipped text reliably, or establish conformance.

```js
import { test, expect } from '@playwright/test';

test('ordinary checkout content fits a narrow viewport', async ({ page }) => {
  await page.setViewportSize({ width: 320, height: 800 });
  await page.goto('/checkout');
  const content = page.locator('main');
  const bounds = await content.boundingBox();
  expect(bounds).not.toBeNull();
  expect(bounds.x).toBeGreaterThanOrEqual(0);
  expect(bounds.x + bounds.width).toBeLessThanOrEqual(321);
  await expect(page.getByRole('button', { name: 'Place order' })).toBeVisible();
  // Continue with the project's safe checkout fixture to verify operation.
});
```

Keep essential two-dimensional regions out of a blanket no-overflow assertion. Inspect actual content loss manually. Record this test as a viewport regression and report real browser zoom testing separately. ([Reflow, scope of exceptions](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html))
