# Top 20 Accessibility Violations

Based on axe-core rule IDs and WebAIM Million 2025 data. The WebAIM survey found an average of 51 errors per page across 1 million sites, with 96.4% of errors falling into six categories: missing alt text, low contrast, missing form labels, missing document language, empty buttons, and empty links.

---

| # | Rule ID | WCAG | Impact | What It Means | Fix Pattern |
|---|---|---|---|---|---|
| 1 | `color-contrast` | 1.4.3 AA | Serious | Text does not have sufficient contrast against background. AA requires 4.5:1 for normal text, 3:1 for large text (18pt+ or 14pt+ bold). | Adjust foreground/background colors to meet ratio. Use a contrast checker. |
| 2 | `image-alt` | 1.1.1 A | Critical | `<img>` missing `alt` attribute. | Add descriptive `alt="..."`. Decorative images: `alt=""` or `role="presentation"`. |
| 3 | `label` | 1.3.1 A, 4.1.2 A | Critical | Form `<input>` has no associated `<label>`. | Add `<label for="id">` matching input's `id`, or use `aria-label`/`aria-labelledby`. |
| 4 | `button-name` | 4.1.2 A | Critical | `<button>` has no discernible accessible name. | Add text content, `aria-label`, or `aria-labelledby`. |
| 5 | `link-name` | 4.1.2 A, 2.4.4 A | Serious | `<a>` has no discernible accessible name. | Add text content or `aria-label`. Icon links: `aria-label="description"`. |
| 6 | `html-has-lang` | 3.1.1 A | Serious | `<html>` missing `lang` attribute. | Add `<html lang="en">` (or appropriate language code). |
| 7 | `document-title` | 2.4.2 A | Serious | Page has no `<title>` element. | Add `<title>Descriptive Page Title</title>` in `<head>`. |
| 8 | `heading-order` | 1.3.1 A | Moderate | Heading levels skip (e.g., h1 to h3). | Use sequential levels: h1, h2, h3 without skipping. |
| 9 | `list` | 1.3.1 A | Serious | Invalid list markup (non-li children in ul/ol). | Ensure `<ul>`/`<ol>` contain only `<li>`, `<script>`, or `<template>` children. |
| 10 | `listitem` | 1.3.1 A | Serious | `<li>` not contained in `<ul>` or `<ol>`. | Wrap `<li>` elements in `<ul>` or `<ol>`. |
| 11 | `region` | 1.3.1 A | Moderate | Content not in a landmark region. | Wrap sections in landmarks: `<main>`, `<nav>`, `<header>`, `<footer>`, `<aside>`. |
| 12 | `aria-allowed-attr` | 4.1.2 A | Critical | ARIA attribute not allowed on this element. | Remove invalid ARIA attribute or change the element's role. |
| 13 | `aria-valid-attr-value` | 4.1.2 A | Critical | ARIA attribute has an invalid value. | Correct the value (e.g., `aria-hidden="true"` not `aria-hidden="yes"`). |
| 14 | `aria-required-attr` | 4.1.2 A | Critical | Element with ARIA role missing required attributes. | Add required attributes (e.g., `role="checkbox"` needs `aria-checked`). |
| 15 | `aria-hidden-focus` | 4.1.2 A | Serious | `aria-hidden="true"` contains focusable elements. | Remove focusable children, remove `aria-hidden`, or use `inert` attribute. |
| 16 | `duplicate-id` | 4.1.1 A | Minor | Multiple elements share the same `id`. | Ensure all `id` values are unique on the page. |
| 17 | `tabindex` | 2.4.3 A | Serious | Element has `tabindex` > 0. | Use `tabindex="0"` (natural order) or `tabindex="-1"` (programmatic). Never positive values. |
| 18 | `meta-viewport` | 1.4.4 AA | Critical | Viewport meta disables zoom (`maximum-scale=1` or `user-scalable=no`). | Remove `maximum-scale=1` and `user-scalable=no` from viewport meta. |
| 19 | `bypass` | 2.4.1 A | Serious | Page lacks skip navigation mechanism. | Add "Skip to main content" link as first focusable element, linking to `<main>`. |
| 20 | `autocomplete-valid` | 1.3.5 AA | Serious | Form field has incorrect `autocomplete` value. | Use valid tokens: `autocomplete="email"`, `autocomplete="given-name"`, etc. |

---

## WCAG Tag Filters

To scan for specific WCAG levels with axe-core:

```bash
# Level A only
axe https://example.com --tags wcag2a

# Level AA (includes A)
axe https://example.com --tags wcag2a,wcag2aa

# WCAG 2.1 AA (includes 2.0)
axe https://example.com --tags wcag2a,wcag2aa,wcag21a,wcag21aa

# WCAG 2.2 AA
axe https://example.com --tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa

# Best practices (not WCAG-required)
axe https://example.com --tags best-practice
```
