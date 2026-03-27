# Native `<details>`/`<summary>` Reference

## How It Works

The `<details>` element is a built-in disclosure widget. The `<summary>` child acts as a toggle; clicking or pressing Enter/Space reveals or hides sibling content inside `<details>`. No JavaScript is required for basic show/hide. ([HTML Spec](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element))

## Attributes

### `open` (boolean)

Reflects whether the `<details>` is expanded. Setting or removing it toggles visibility and fires a `toggle` event (`ToggleEvent` with `oldState`/`newState`).

### `name` (string)

Multiple `<details>` elements sharing the same `name` value form an exclusive accordion group: opening one automatically closes others in the group.

```html
<details name="faq">
  <summary>Question 1</summary>
  <p>Answer 1</p>
</details>
<details name="faq">
  <summary>Question 2</summary>
  <p>Answer 2</p>
</details>
```

**Browser support (all stable):**
- Chrome 120+
- Safari 17.2+
- Firefox 130+ (stable since April 2025)

Source: [MDN Blog](https://developer.mozilla.org/en-US/blog/html-details-exclusive-accordions/), [Chrome for Developers](https://developer.chrome.com/docs/css-ui/exclusive-accordion)

### `toggle` Event

Fires on state change. Coalesced when toggled multiple times in rapid succession. The `ToggleEvent` provides `oldState` and `newState` properties.

## Default Summary

If no `<summary>` child is provided, the browser renders a default label (typically "Details"). Always provide an explicit `<summary>`.

## Limitations

### 1. Heading Semantics Destroyed Inside `<summary>`

`<summary>` maps to a button role. Headings nested inside it are flattened to presentational semantics in most screen readers:

- **JAWS + Firefox/Chrome:** Headings not announced, not navigable via heading shortcuts.
- **NVDA:** Heading announced but may suppress expanded/collapsed state.
- **VoiceOver:** Inconsistent — sometimes navigable, sometimes not.

Source: [Roselli 2019](https://adrianroselli.com/2019/04/details-summary-are-not-insert-control-here.html), [O'Hara 2018](https://www.scottohara.me/blog/2018/09/03/details-and-summary.html)

### 2. No Arrow-Key Navigation

Native `<details>` only supports Enter/Space on the focused `<summary>` and Tab for sequential navigation. The APG accordion pattern's optional arrow-key navigation between headers is absent.

### 3. No Grouping Semantics

A set of `<details>` elements is not announced as a group. There is no built-in equivalent of `role="group"` with `aria-labelledby`. Users cannot perceive that the sections are related.

### 4. Inconsistent Role Announcements

- VoiceOver/Safari announces `<summary>` with its state but no standard role name.
- NVDA announces it as "button."
- JAWS behavior varies by browser.
- Adding `role="button"` to `<summary>` can suppress state announcements in VoiceOver.

Source: [O'Hara 2018](https://www.scottohara.me/blog/2018/09/03/details-and-summary.html)

### 5. Not Suitable for Other Patterns

The HTML spec explicitly states `<details>` should not replace tab widgets, menu widgets, or other non-disclosure patterns. It is a disclosure widget only.

## Progressive Enhancement Pattern

Start with `<details>`/`<summary>` for no-JS baseline, then enhance:

```html
<div role="group" aria-labelledby="faq-title">
  <h2 id="faq-title">Frequently Asked Questions</h2>
  <details name="faq">
    <summary>Question 1</summary>
    <p>Answer 1</p>
  </details>
  <details name="faq">
    <summary>Question 2</summary>
    <p>Answer 2</p>
  </details>
</div>
```

JavaScript enhancement adds:
- `role="group"` wrapper with `aria-labelledby` for grouping semantics
- Exclusive-open behavior (or rely on `name` attribute where supported)
- Optional arrow-key navigation between summaries

Source: [Roselli 2023](https://adrianroselli.com/2023/08/progressively-enhanced-html-accordion.html)
