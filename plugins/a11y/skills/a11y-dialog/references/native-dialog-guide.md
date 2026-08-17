# Native `<dialog>` Element Guide
## Contents

- [When to Use Native dialog](#when-to-use-native-dialog)
- [Opening Methods](#opening-methods)
  - [.showModal()](#showmodal)
  - [.show()](#show)
  - [Never use the open attribute directly](#never-use-the-open-attribute-directly)
- [closedby Attribute](#closedby-attribute)
- [Events and Return Value](#events-and-return-value)
  - [returnValue](#returnvalue)
- [Styling](#styling)
  - [::backdrop](#backdrop)
  - [Dialog positioning](#dialog-positioning)
  - [Reduced motion](#reduced-motion)
- [What Native dialog Does NOT Do](#what-native-dialog-does-not-do)


## When to Use Native `<dialog>`

Use native `<dialog>` as the default for all new dialogs. MDN recommends: "Use the native `<dialog>` HTML element when possible."

The native element handles the hardest accessibility problems automatically — focus trapping, background inertness, and Escape-to-close. What remains for authors is accessible naming, focus placement, and focus restoration.

*Source: [MDN — ARIA dialog role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/dialog_role)*

---

## Opening Methods

### `.showModal()`

Opens as a modal dialog:
- Places dialog in the **top layer** (above all other content, including `z-index` stacking)
- All background content becomes **automatically inert** (no explicit `inert` attribute needed)
- Adds `::backdrop` pseudo-element for styling the overlay
- Defaults to `closedby="closerequest"` (Escape closes it)
- Focus is trapped within the dialog automatically
- `aria-modal` is implicit — do not add it manually

### `.show()`

Opens as a non-modal (modeless) dialog:
- Background content remains fully interactive
- No backdrop
- No inert behavior on background
- Defaults to `closedby="none"`
- Focus is NOT trapped — user can Tab to background content
- Appropriate for persistent panels, chat widgets, toolbars

### Never use the `open` attribute directly

```html
<!-- WRONG — does not trigger focus management or top layer -->
<dialog open>Content</dialog>

<!-- RIGHT — use JavaScript methods -->
<script>dialog.showModal();</script>
```

*Source: [HTML Spec — The dialog element](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)*

---

## `closedby` Attribute

Controls which user actions automatically close the dialog.

| Value | Behavior | Default for |
|-------|----------|-------------|
| `"closerequest"` | Close requests only (Escape key, platform close gestures) | Modal (`.showModal()`) |
| `"any"` | Close requests + clicking outside the dialog (light dismiss) | — |
| `"none"` | No automatic closing — must be closed programmatically | Non-modal (`.show()`) |

```html
<!-- Light-dismiss modal -->
<dialog closedby="any">
  <p>Click outside or press Escape to close.</p>
</dialog>

<!-- Modal that requires explicit action -->
<dialog closedby="none">
  <p>You must choose an option.</p>
  <button>Accept</button>
  <button>Decline</button>
</dialog>
```

*Source: [HTML Spec — The dialog element](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)*

---

## Events and Return Value

| Event | When | Cancelable |
|-------|------|------------|
| `beforetoggle` | Before dialog opens or closes | Yes — `preventDefault()` blocks the state change |
| `toggle` | After dialog opens or closes | No |
| `close` | After dialog closes | No |

### `returnValue`

Communicates which button closed the dialog. Set via `<form method="dialog">`:

```html
<dialog id="confirm" aria-labelledby="ct">
  <h2 id="ct">Save changes?</h2>
  <form method="dialog">
    <button value="discard">Discard</button>
    <button value="save">Save</button>
  </form>
</dialog>

<script>
  confirm.addEventListener('close', () => {
    if (confirm.returnValue === 'save') {
      saveChanges();
    }
  });
</script>
```

*Source: [HTML Spec — The dialog element](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)*

---

## Styling

### `::backdrop`

The `::backdrop` pseudo-element is available only with `.showModal()`. Covers the entire viewport behind the dialog.

```css
dialog::backdrop {
  background: rgba(0, 0, 0, 0.5);
}
```

### Dialog positioning

Dialogs opened with `.showModal()` are centered by default. Override with standard CSS positioning if needed.

### Reduced motion

Respect `prefers-reduced-motion` for dialog open/close animations:

```css
@media (prefers-reduced-motion: reduce) {
  dialog {
    animation: none;
  }
}
```

---

## What Native `<dialog>` Does NOT Do

Even with native `<dialog>`, authors must still:

1. **Add `aria-labelledby`** pointing to the title element — not automatic
2. **Optionally add `aria-describedby`** for descriptive content
3. **Manage context-appropriate initial focus** — use `autofocus` or programmatic focus per the rules in `focus-management-rules.md`
4. **Handle focus restoration on close** — browser behavior varies; implement explicitly
5. **Provide a visible close button** — Escape-to-close is not discoverable

*Sources: [Adrian Roselli — Dialog Focus in Screen Readers](https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html); [APG Dialog (Modal) Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)*
