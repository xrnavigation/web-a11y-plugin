# Modal Focus Trapping — Reference
## Contents

- [The inert Attribute (Preferred)](#the-inert-attribute-preferred)
  - [Native dialog with showModal()](#native-dialog-with-showmodal)
  - [Custom modal with inert](#custom-modal-with-inert)
  - [inert vs disabled](#inert-vs-disabled)
  - [Browser support](#browser-support)
- [Sentinel Focus Trap (Legacy Fallback)](#sentinel-focus-trap-legacy-fallback)
  - [Focusable element selectors](#focusable-element-selectors)
  - [Keyboard event interception](#keyboard-event-interception)
- [Initial Focus Placement](#initial-focus-placement)
  - [Guidelines](#guidelines)
  - [The rule](#the-rule)


## The `inert` Attribute (Preferred)

The HTML `inert` attribute makes an element and its entire flat tree of descendants non-interactive. The subtree is removed from the accessibility tree, cannot receive focus, cannot be hit-tested, and cannot have text selected.

> "User agents do not expose the inert nodes to accessibility APIs or assistive technologies."
> — [WHATWG HTML Spec](https://html.spec.whatwg.org/multipage/interaction.html#the-inert-attribute)

### Native `<dialog>` with `showModal()`

When a dialog is opened via `showModal()`, the browser automatically makes all content outside the dialog inert:

> "While document is so blocked, every node that is connected to document... must become inert."

No manual `inert` attribute is needed. This is the simplest correct implementation.

### Custom modal with `inert`

For custom modal implementations (not using `<dialog>`), apply `inert` to sibling containers:

```html
<div id="app" inert><!-- page content --></div>
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirm</h2>
  <p>Are you sure?</p>
  <button>Cancel</button>
  <button>Confirm</button>
</div>
```

When the modal closes, remove the `inert` attribute:

```js
function openModal() {
  document.getElementById('app').inert = true;
  modalEl.hidden = false;
}

function closeModal() {
  document.getElementById('app').inert = false;
  modalEl.hidden = true;
  trigger?.focus();
}
```

### `inert` vs `disabled`

The WHATWG spec warns: do not overuse `inert` on individual form controls. The `disabled` attribute is "probably more appropriate" for those cases. Use `inert` for large sections of the page that should be blocked while a modal is open.

Content marked as `inert` should be visually obscured (e.g., with a backdrop overlay) to prevent user confusion.

### Browser support

- Chrome 102+
- Safari 15.5+
- Firefox 112+

---

## Sentinel Focus Trap (Legacy Fallback)

Place invisible focusable elements at the start and end of the modal. When focus reaches a sentinel, redirect to the opposite end.

### Focusable element selectors

```js
const FOCUSABLE_SELECTOR = [
  'a[href]',
  'button:not([disabled])',
  'input:not([disabled])',
  'select:not([disabled])',
  'textarea:not([disabled])',
  '[tabindex]:not([tabindex="-1"])',
  'audio[controls]',
  'video[controls]',
  'details > summary',
  '[contenteditable]:not([contenteditable="false"])'
].join(', ');
```

### Keyboard event interception

An alternative to sentinels: listen for `keydown` on Tab and Shift+Tab, detect when focus would leave the modal, and redirect:

```js
function handleKeyDown(e) {
  if (e.key !== 'Tab') return;
  const focusableEls = modal.querySelectorAll(FOCUSABLE_SELECTOR);
  const firstEl = focusableEls[0];
  const lastEl = focusableEls[focusableEls.length - 1];

  if (e.shiftKey && document.activeElement === firstEl) {
    e.preventDefault();
    lastEl.focus();
  } else if (!e.shiftKey && document.activeElement === lastEl) {
    e.preventDefault();
    firstEl.focus();
  }
}
```

Source: [Medium — Achieving Focus Trapping in a React Modal Component](https://medium.com/cstech/achieving-focus-trapping-in-a-react-modal-component-3f28f596f35b)

---

## Initial Focus Placement

Adrian Roselli's testing found "there is no single correct answer" — it depends on context, dialog type, and user skill level.

### Guidelines

| Dialog Type | Focus Target | Rationale |
|---|---|---|
| Small confirmation | Cancel/close button | Avoids accidental destructive action |
| Large form | Heading or first input | Provides context before interaction |
| Informational | Close button or heading | Lets user dismiss or read |

### The rule

**Never place initial focus on a destructive action button.** A delete confirmation that auto-focuses "Delete" risks accidental activation by keyboard users who press Enter/Space reflexively.

Source: [Adrian Roselli — Dialog Focus in Screen Readers](https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html)
