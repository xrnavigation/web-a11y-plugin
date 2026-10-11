# Tree and treegrid keyboard interaction

These summaries distinguish core navigation from APG recommendations and
optional additions; consult the linked patterns for all alternatives.

## Vertical tree

| Key | Behavior |
|---|---|
| Right | Closed parent: open without moving focus. Open parent: first child. Leaf: no action. |
| Left | Open parent: close. Closed/end child: parent. Closed/end root: no action. |
| Down / Up | Next/previous visible focusable node without expansion changes |
| Home / End | First/last focusable node without opening more nodes |
| Enter | Node's default action; a parent may expand, navigate or perform its defined task |

Type-ahead is recommended for all trees, especially with more than seven root
nodes. A character or rapidly typed prefix moves to the next matching name.
`*` expanding siblings at the focused node's level is optional
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)).

On entry, use the selected node for single-select, first selected node for
multi-select, or first node when none is selected. Horizontal trees transpose
expansion and traversal arrows as specified by APG
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)).

## Multi-selection

| Model | Navigate without clearing selection | Toggle active node |
|---|---|---|
| Recommended | Unmodified Up/Down | Space |
| Alternative | Ctrl+Up/Down | Ctrl+Space |

The alternative model changes selection during unmodified navigation. Both
models support Shift+Up/Down for focus and selection movement (optional in the
recommended model). Range shortcuts and Ctrl+A are optional; a Select All
control can also be useful. Keep focus and selection visually distinguishable
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)).

## Treegrid: choose row focus, cell focus, or both

| Key | Row focus | Cell focus |
|---|---|---|
| Right | Expand collapsed parent; otherwise enter first cell | Next cell, staying at right boundary |
| Left | Collapse expanded parent; otherwise stay | Previous cell; from first cell, row if row focus supported |
| Up / Down | Previous/next row | Previous/next row in the same column |
| Home / End | First/last row | First/last cell in current row |
| Ctrl+Home / Ctrl+End | First/last row | First/last row in the same column |
| Page Up / Page Down | Author-determined row movement | Author-determined row movement in same column |

The contract changes with focus location, not just a generic “treegrid” label.
The pattern describes Tab navigation through focusable controls in a row and
exit after the final row control; when rows themselves are focusable, the
specified row-to-cell entry also applies. Editors may need their own mode for
arrows and caret navigation
([APG treegrid](https://www.w3.org/WAI/ARIA/apg/patterns/treegrid/)).

## Treegrid selection, when supported

| Key | Row focus | Cell focus |
|---|---|---|
| Ctrl+Space | Select all cells | Select focused column |
| Shift+Space | Select focused row | Select row containing focused cell |
| Ctrl+A | Select all cells | Select all cells |
| Shift+Right / Left | No selection change | Extend selection one cell horizontally |
| Shift+Down / Up | Extend selection to next/previous row's cells | Extend selection one cell vertically |

These are selection conventions for a treegrid that offers those functions;
not every treegrid must implement selection
([APG treegrid](https://www.w3.org/WAI/ARIA/apg/patterns/treegrid/)).

With dynamic loading, first/last-row shortcuts can reach the last available DOM
row rather than all server data. Make that behavior understandable and verify
indices/counts and focus after loading
([APG treegrid](https://www.w3.org/WAI/ARIA/apg/patterns/treegrid/)).
