# Keyboard Interaction — Combobox Variants
## Contents

- [Editable Combobox (Input Level)](#editable-combobox-input-level)
- [Editable Combobox (Listbox Popup)](#editable-combobox-listbox-popup)
- [Select-Only Combobox](#select-only-combobox)
  - [Closed State](#closed-state)
  - [Open State](#open-state)
- [Grid Popup](#grid-popup)
- [Tree Popup](#tree-popup)
- [Dialog Popup](#dialog-popup)


Keyboard summary per variant. APG is implementation guidance; consult the linked pattern/examples for their full alternatives and optional interactions.

All source: [APG Combobox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)

---

## Editable Combobox (Input Level)

| Key | Action |
|-----|--------|
| Tab | Moves focus into/out of the combobox in page tab sequence |
| Down Arrow | Opens popup if closed; moves visual focus to first or next suggestion |
| Up Arrow | (Optional) Opens popup and focuses last element |
| Escape | Closes popup; optionally clears the combobox value |
| Enter | Accepts the focused suggestion; closes popup |
| Alt + Down Arrow | (Optional) Opens popup without moving focus into it |
| Alt + Up Arrow | (Optional) Closes popup or returns focus from popup |
| Printable characters | Types in the input; popup filters if `aria-autocomplete="list"` or `"both"` |
| Standard editing keys | Cursor movement, text selection, deletion (platform-specific) |

Source: [APG Combobox Pattern — Keyboard Interaction](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)

---

## Editable Combobox (Listbox Popup)

When visual focus is in the popup (via `aria-activedescendant`; DOM focus remains on input):

| Key | Action |
|-----|--------|
| Enter | Accepts focused option, closes popup |
| Escape | Closes popup, returns focus to combobox |
| Down Arrow | Next option; optionally wraps to first option or returns to combobox |
| Up Arrow | Previous option; optionally wraps to last option or returns to combobox |
| Right Arrow | (If editable) Returns to combobox and moves cursor right |
| Left Arrow | (If editable) Returns to combobox and moves cursor left |
| Home | (Optional) First option, or returns to combobox with cursor at start |
| End | (Optional) Last option, or returns to combobox with cursor at end |
| Printable character | If editable: types in combobox and filters; else: jumps to matching option |
| Backspace / Delete | (Optional) Returns to combobox and edits text |

Source: [APG Combobox Pattern — Keyboard Interaction](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)

---

## Select-Only Combobox

### Closed State

| Key | Action |
|-----|--------|
| Down Arrow | Opens listbox, focuses first option |
| Alt + Down Arrow | Opens listbox |
| Up Arrow | Opens listbox, focuses last option |
| Enter | Opens listbox |
| Space | Opens listbox |
| Home | Opens listbox, focuses first option |
| End | Opens listbox, focuses last option |
| Printable character | Opens listbox, moves focus to matching option (type-ahead) |

### Open State

| Key | Action |
|-----|--------|
| Enter | Selects focused option, closes listbox |
| Space | Selects focused option, closes listbox |
| Tab | Selects focused option, closes listbox, moves focus to next tab stop |
| Escape | Closes listbox without changing selection |
| Down Arrow | Moves focus to next option |
| Up Arrow | Moves focus to previous option |
| Home | Moves focus to first option |
| End | Moves focus to last option |
| Page Down | Moves focus down ~10 options |
| Page Up | Moves focus up ~10 options |
| Printable character | Moves focus to next option starting with typed character(s) |

Source: [APG Select-Only Combobox Example](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-select-only/)

---

## Grid Popup

When popup is `role="grid"`:

| Key | Action |
|-----|--------|
| Enter | Accepts selected cell value, closes popup |
| Escape | Closes popup, returns to combobox |
| Down Arrow | Moves focus to next row (same column) |
| Up Arrow | Moves focus to previous row (same column) |
| Right Arrow | Moves focus to next cell in row |
| Left Arrow | Moves focus to previous cell in row |
| Page Down | (Optional) Moves down multiple rows |
| Page Up | (Optional) Moves up multiple rows |
| Home | (Optional) First cell in row |
| End | (Optional) Last cell in row |
| Ctrl + Home | (Optional) First cell in grid |
| Ctrl + End | (Optional) Last cell in grid |

Source: [APG Grid Combobox Example](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/grid-combo/)

---

## Tree Popup

When popup is `role="tree"`:

| Key | Action |
|-----|--------|
| Right Arrow | Opens closed node; if open, moves to first child |
| Left Arrow | Closes open node; if closed, moves to parent |
| Down Arrow | Next focusable tree node |
| Up Arrow | Previous focusable tree node |
| Home | First focusable tree node |
| End | Last focusable tree node |
| Enter | Accepts focused node value, closes popup |
| Escape | Closes popup, returns to combobox |

Source: [APG Combobox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)

---

## Dialog Popup

When popup is `role="dialog"` (e.g., date picker):

- DOM focus moves INTO the dialog (this is the exception — do NOT use `aria-activedescendant`)
- Tab key cycles within the dialog (focus trap)
- Escape closes the dialog and returns focus to the combobox
- Two exit paths: action button (sets value) or cancel (clears/maintains value)
- Internal keyboard interaction follows the dialog's own pattern (e.g., calendar grid uses arrow keys)

Source: [APG Date Picker Combobox Example](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-datepicker/)
