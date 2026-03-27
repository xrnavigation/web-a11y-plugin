# Keyboard Interaction Reference

## APG Accordion Pattern

Source: [APG Accordion Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)

### Required Keys

| Key | Behavior |
|-----|----------|
| Enter | When focus is on an accordion header button, toggles the associated panel. If the panel is collapsed, it expands. If implementation allows collapsing, an expanded panel collapses. |
| Space | Same as Enter. |
| Tab | Moves focus to the next focusable element in document order. All focusable elements in the accordion are included in the page Tab sequence. |
| Shift+Tab | Moves focus to the previous focusable element in document order. |

### Optional Keys

These are recommended for the full accordion experience but not required.

| Key | Behavior |
|-----|----------|
| Down Arrow | When focus is on an accordion header, moves focus to the next accordion header. If on the last header, wraps to the first header. |
| Up Arrow | When focus is on an accordion header, moves focus to the previous accordion header. If on the first header, wraps to the last header. |
| Home | When focus is on an accordion header, moves focus to the first accordion header. |
| End | When focus is on an accordion header, moves focus to the last accordion header. |

### Implementation Notes

- Arrow key navigation only applies when focus is on accordion header buttons, not when focus is inside panel content.
- If arrow keys are implemented, they must wrap (last to first, first to last).
- Tab always moves through the entire document order — do not trap Tab within the accordion.
- If only one panel can be open at a time, the implementation may use `aria-disabled="true"` on the expanded header to indicate it cannot be collapsed.

---

## APG Disclosure Pattern

Source: [APG Disclosure Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/)

| Key | Behavior |
|-----|----------|
| Enter | Activates the disclosure button, toggling visibility of content. |
| Space | Activates the disclosure button, toggling visibility of content. |

No arrow-key navigation. Disclosure is a single button controlling a single content block.

---

## Native `<details>`/`<summary>`

| Key | Behavior |
|-----|----------|
| Enter | Toggles the `<details>` open/closed state when `<summary>` is focused. |
| Space | Toggles the `<details>` open/closed state when `<summary>` is focused. |
| Tab | Standard sequential focus navigation. |
| Shift+Tab | Standard reverse sequential focus navigation. |

No arrow-key navigation is provided natively. The `<summary>` element receives focus via Tab order like any other interactive element.

---

## Comparison Matrix

| Key | Native `<details>` | ARIA Disclosure | ARIA Accordion |
|-----|-------------------|-----------------|----------------|
| Enter/Space | Toggle | Toggle | Toggle |
| Tab/Shift+Tab | Sequential | Sequential | Sequential |
| Down Arrow | N/A | N/A | Next header (optional) |
| Up Arrow | N/A | N/A | Previous header (optional) |
| Home | N/A | N/A | First header (optional) |
| End | N/A | N/A | Last header (optional) |
