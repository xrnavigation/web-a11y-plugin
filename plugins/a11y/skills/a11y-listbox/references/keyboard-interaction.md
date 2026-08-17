# Listbox Keyboard Interaction — Complete Spec

Source: [W3C APG Listbox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)

---

## Navigation (all listbox types)

| Key | Behavior | Notes |
|-----|----------|-------|
| Down Arrow | Move focus to next option | In single-select, may also move selection |
| Up Arrow | Move focus to previous option | In single-select, may also move selection |
| Home | Move focus to first option | Optional; recommended for 5+ options |
| End | Move focus to last option | Optional; recommended for 5+ options |
| Type-ahead (single char) | Focus next option starting with that character | Recommended for 7+ options |
| Type-ahead (rapid multiple chars) | Focus first option matching the typed string | Recommended for 7+ options |

---

## Single-select

| Key | Behavior |
|-----|----------|
| Space | Select/confirm focused option |
| Down/Up Arrow | May both move focus and change selection (selection follows focus) |

**Focus landing:** If an option is pre-selected, focus goes there; otherwise focus goes to the first option (which may auto-select).

---

## Multi-select: Recommended Model

In this model, arrow keys move focus without requiring modifier keys and **do not change selection**.

| Key | Behavior | Required? |
|-----|----------|-----------|
| Space | Toggle selection state of focused option | Required |
| Shift + Down Arrow | Move focus to next option and toggle its selection | Optional |
| Shift + Up Arrow | Move focus to previous option and toggle its selection | Optional |
| Shift + Space | Select contiguous items from most recently selected to focused | Optional |
| Ctrl + Shift + Home | Select from focused option to first option | Optional |
| Ctrl + Shift + End | Select from focused option to last option | Optional |
| Ctrl + A | Select all (toggle if all already selected) | Optional |

**This is the recommended model** because it does not require modifier keys for basic navigation, making it more discoverable.

---

## Multi-select: Alternative Model

In this model, unmodified arrow keys move focus **and deselect all except the focused option** (like single-select behavior). Modifier keys are needed to preserve existing selections.

| Key | Behavior | Required? |
|-----|----------|-----------|
| Shift + Down Arrow | Move focus and toggle next option's selection | Required |
| Shift + Up Arrow | Move focus and toggle previous option's selection | Required |
| Ctrl + Down Arrow | Move focus without changing selection | Required |
| Ctrl + Up Arrow | Move focus without changing selection | Required |
| Ctrl + Space | Toggle selection of focused option | Required |
| Shift + Space | Select contiguous items from last selected to focused | Optional |
| Ctrl + Shift + Home | Select from focused to first | Optional |
| Ctrl + Shift + End | Select from focused to last | Optional |
| Ctrl + A | Select/deselect all | Optional |

**Warning:** This model is less discoverable because users must know to use Ctrl+Arrow to navigate without losing selections. Use the recommended model unless you have a strong reason.

---

## Scrollable Listbox Notes

- The focused option must always be scrolled into view programmatically when keyboard navigation moves focus ([APG](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).
- Use `aria-setsize` and `aria-posinset` for virtualized/dynamically loaded lists where not all options exist in the DOM.
- Type-ahead becomes critical for long scrollable lists (recommended for 7+ options).
- Home/End keys are strongly recommended for lists with 5+ options.
- Avoid very long option names in scrollable lists — truncation or wrapping impairs screen reader comprehension ([APG](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).

---

## Reorderable Listbox Keyboard

For reorderable listboxes, add these keyboard shortcuts:

| Key | Behavior |
|-----|----------|
| Alt + Down Arrow | Move selected item down one position |
| Alt + Up Arrow | Move selected item up one position |

These are in addition to — not a replacement for — the standard listbox keyboard interaction.

**Important:** Keyboard reordering alone does not satisfy WCAG 2.5.7 (Dragging Movements). A pointer-based non-drag alternative (e.g., visible up/down buttons) is also required ([WCAG 2.2 SC 2.5.7](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)).
