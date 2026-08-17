# Keyboard Interaction — Tree View & Treegrid

Complete keyboard specification from the APG patterns.

---

## Core Navigation (Single-select, Vertical Tree)

| Key | Behavior |
|-----|----------|
| **Right Arrow** | Closed parent node: open it. Open parent node: move focus to first child. End node: do nothing. |
| **Left Arrow** | Open parent node: close it. Child or end node: move focus to parent. Root-level closed/end node: do nothing. |
| **Down Arrow** | Move focus to the next visible node (does not expand or collapse). |
| **Up Arrow** | Move focus to the previous visible node (does not expand or collapse). |
| **Home** | Move focus to the first node in the tree. |
| **End** | Move focus to the last visible node in the tree. |
| **Enter** | Perform the default action on the node. For parent nodes: toggle expand/collapse. For leaf nodes in single-select without selection-follows-focus: select. |
| **Type-ahead** | Focus moves to the next node whose label starts with the typed character(s). Recommended for trees with 7+ root nodes. Successive rapid characters match longer prefixes. |
| **\* (Asterisk)** | Optional. Expands all siblings of the focused node that are at the same level. |

— [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)

---

## Focus on Entry

- No node selected: focus goes to the first node.
- A node is selected (single-select): focus goes to the selected node.
- Multi-select with selection: focus goes to the first selected node.

— [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)

---

## Multi-select Trees — Recommended Model

This model does not require modifier keys for basic navigation.

| Key | Behavior |
|-----|----------|
| **Space** | Toggle selection of the focused node. |
| **Shift + Down Arrow** | Move focus down and toggle selection state of the newly focused node. (Optional) |
| **Shift + Up Arrow** | Move focus up and toggle selection state of the newly focused node. (Optional) |
| **Shift + Space** | Select a contiguous range from the most recently selected node to the current node. (Optional) |
| **Ctrl + Shift + Home** | Select from the focused node to the first node. (Optional) |
| **Ctrl + Shift + End** | Select from the focused node to the last visible node. (Optional) |
| **Ctrl + A** | Select all nodes. If all are selected, unselect all. (Optional) |

— [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)

---

## Multi-select Trees — Alternative Model

This model requires modifier keys for navigation without changing selection.

| Key | Behavior |
|-----|----------|
| **Ctrl + Down/Up Arrow** | Move focus without changing selection. |
| **Ctrl + Space** | Toggle selection of the focused node. |
| **Shift + Down/Up Arrow** | Move focus and toggle selection. |

— [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)

---

## Treegrid-specific Keyboard Additions

| Key | Behavior |
|-----|----------|
| **Tab** | Move through focusable elements within a row; exit grid at last element. |
| **Right/Left Arrow** (cell focus) | Move between cells in a row. |
| **Page Up / Page Down** | Scroll by an author-determined number of rows. |
| **Home / End** (cell focus) | Move to first/last cell in the current row. |
| **Ctrl + Home / Ctrl + End** | Move to first/last cell in the entire grid. |
| **Shift + Space** | Select the current row. |
| **Ctrl + Space** | Select the entire column. |

— [APG Treegrid Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treegrid/)

---

## Navigation Models for Treegrid

The APG defines three approaches:

1. **Rows-first:** Arrow keys move between rows. Right Arrow on a row moves into cells. Best when rows are the primary unit (e.g., file browser with metadata columns).
2. **Cells-first:** Arrow keys move between cells. Best when cell-level interaction is primary (e.g., editable data).
3. **Cells-only:** Rows are never focused; only cells receive focus. Best for spreadsheet-like interfaces.

Choose based on use case. — [APG Treegrid Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treegrid/)
