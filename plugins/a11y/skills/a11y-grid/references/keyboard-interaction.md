# Grid Keyboard Interaction

Source: [APG Grid Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)

## Navigation (arrow keys move focus between cells)

| Key | Action |
|-----|--------|
| Right Arrow | Move focus one cell right. If at last cell in row, do nothing (or wrap to next row). |
| Left Arrow | Move focus one cell left. If at first cell in row, do nothing (or wrap to previous row). |
| Down Arrow | Move focus one cell down. If at last row, do nothing. |
| Up Arrow | Move focus one cell up. If at first row, do nothing. |
| Home | Move focus to first cell in current row. |
| End | Move focus to last cell in current row. |
| Ctrl+Home | Move focus to first cell in first row (top-left). |
| Ctrl+End | Move focus to last cell in last row (bottom-right). |
| Page Down (optional) | Scroll down by one "page" of visible rows; move focus accordingly. |
| Page Up (optional) | Scroll up by one "page" of visible rows; move focus accordingly. |
| Tab | Move focus OUT of the grid to the next focusable element on the page. |
| Shift+Tab | Move focus OUT of the grid to the previous focusable element. |

**Critical:** Tab does NOT move between cells. Tab exits the grid. This is the fundamental difference between a grid and a table with interactive elements.

## Selection (optional — only if the grid supports selection)

| Key | Action |
|-----|--------|
| Space | Select/deselect current cell or row |
| Ctrl+Space | Select entire column |
| Shift+Space | Select entire row |
| Ctrl+A | Select all cells |
| Shift+Arrow | Extend selection in arrow direction |

When selection is supported, use `aria-selected="true"` on selected cells/rows and `aria-multiselectable="true"` on the grid if multi-select is allowed.

## Edit Mode (for editable cells)

| Key | Action |
|-----|--------|
| Enter | Enter edit mode on current cell, or activate the first widget in the cell |
| F2 | Toggle edit mode on/off |
| Escape | Exit edit mode; restore grid navigation. Optionally undo the edit. |
| Alphanumeric keys | When not in edit mode: optionally start editing (replaces cell content) |

### While in edit mode

- Arrow keys operate contained widgets (e.g., dropdown navigation), NOT grid navigation
- Tab / Shift+Tab move between widgets within the same cell
- Escape returns to grid navigation mode

## Focus Management Rules

### Which element receives focus in a cell?

1. **Cell contains a single focusable widget** (button, link, checkbox): focus the widget directly. The cell itself does not need `tabindex`.
2. **Cell contains only text/graphics**: focus the cell itself. Set `tabindex="-1"` on the cell element.
3. **Cell contains multiple widgets**: focus the cell first. Enter/F2 moves focus into the cell's widgets. Escape returns focus to the cell.

### Roving tabindex pattern

Only one navigation target has `tabindex="0"`: the cell or its focused widget. Other navigation targets have `tabindex="-1"`. When focus moves, update the tabindex values:

```javascript
// Pseudocode
function moveFocus(fromCell, toCell) {
  fromCell.tabIndex = -1;
  toCell.tabIndex = 0;
  toCell.focus();
}
```

This ensures that Tab/Shift+Tab enters the grid at the last-focused cell.

## UX Warning

> "A user who may expect to tab to a link, button, or checkbox they can see in the grid may be confused when they tab past it."
> — [Adrian Roselli](https://adrianroselli.com/2020/07/aria-grid-as-an-anti-pattern.html)

Project recommendation: provide concise visible instructions where arrow navigation or editing is unfamiliar. Verify actual focus and exposed roles; do not assume a particular spoken role announcement.

## Sources

- [APG Grid Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)
- [WAI-ARIA 1.2, grid role](https://www.w3.org/TR/wai-aria-1.2/#grid)
- [Adrian Roselli, ARIA Grid As an Anti-Pattern](https://adrianroselli.com/2020/07/aria-grid-as-an-anti-pattern.html)
