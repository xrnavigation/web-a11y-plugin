---
name: a11y-tree
description: Guides accessible trees and treegrids. Use when building hierarchical selection, file explorers, navigation trees, or expandable data grids with author-managed focus, keyboard behavior, and selection.
---

# Accessible trees and treegrids

Choose a tree for a hierarchical list and a treegrid for hierarchical tabular
information with row/cell interaction. Implement the chosen widget's focus and
keyboard behavior together with its semantics
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/),
[APG treegrid](https://www.w3.org/WAI/ARIA/apg/patterns/treegrid/)).

Prefer ordinary disclosure controls and links for typical website navigation.
A navigation tree is nevertheless a legitimate APG pattern when its full
composite interaction serves the task; navigation use alone is not invalid
([APG navigation tree](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/examples/treeview-navigation/)).

## Structure and states

This is a structural skeleton, not an operable tree. Add the keyboard behavior
below, update roving tabindex, and synchronize expansion with child visibility:

```html
<h3 id="files-label">Files</h3>
<ul role="tree" aria-labelledby="files-label">
  <li role="treeitem" aria-labelledby="src-label" aria-expanded="true" tabindex="0">
    <span id="src-label">src</span>
    <ul role="group">
      <li role="treeitem" tabindex="-1">index.ts</li>
    </ul>
  </li>
  <li role="treeitem" tabindex="-1">README.md</li>
</ul>
```

Name the tree. Parents contain or own child groups; leaves omit `aria-expanded`.
Hide collapsed descendants and keep the active node visible. For partial DOM
rendering, supply `aria-level`, `aria-setsize` and `aria-posinset` that describe
the complete hierarchy, not just the rendered slice
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)).

Choose roving DOM focus or container focus with `aria-activedescendant` and keep
that model consistent. Historical reader-specific workarounds do not determine
the best current choice; verify the product's supported combinations
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)).

## Keyboard contract

For vertical trees, implement arrows, Home/End and the node's default action.
Right opens a closed parent or moves to its first child when open. Left closes
an open parent or moves from a closed/end child to its parent. Up/Down traverse
visible focusable nodes. Enter performs the task's default action; expansion is
one possible default for a parent, not mandatory behavior for every parent.
Type-ahead is recommended for all trees, especially larger ones; `*` to expand
siblings is optional
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)).

Treegrid keys depend on row versus cell focus. With cell focus, Ctrl+Home/End
moves to the first/last row **in the same column**. Ctrl+Space selects the column
with cell focus, but all cells with row focus when selection is supported
([APG treegrid](https://www.w3.org/WAI/ARIA/apg/patterns/treegrid/)).

Read [keyboard interaction](references/keyboard-interaction.md) for the separate
focus and selection models; APG is guidance, not a separate normative WCAG
keyboard checklist.

## Selection

Usually use either `aria-selected` or `aria-checked` consistently. Set true for
selected nodes, false for unselected selectable nodes, and omit the attribute on
non-selectable nodes. Rare use of both requires different meanings, visibly
apparent purposes and a separate way to control each state; do not duplicate
one selection state in both attributes
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)).

For multi-selection, set `aria-multiselectable="true"` and distinguish selection
from focus. The recommended model lets unmodified arrows move without clearing
selection and Space toggle the active node. An alternative model uses modifiers
to preserve selection. Choose one complete model
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)).

## Treegrid structure

A treegrid owns rows, and rows own `gridcell`, `rowheader` or `columnheader`
elements. Name the treegrid. Put expansion state on a parent row or its
controlling cell and omit it for leaf rows. Use `aria-multiselectable` when
multiple rows/cells can be selected; expose partial row/column counts and indices
when rendering an incomplete subset
([APG treegrid](https://www.w3.org/WAI/ARIA/apg/patterns/treegrid/)).

## Verify

Check entry/exit, expansion, collapsed descendants, selection, deletion,
virtualization and loading. For treegrids, also check row/cell transitions and
editor entry/exit. Record actual supported environments and observed results;
do not promise a fixed announcement.

Read [common mistakes](references/common-mistakes.md),
[AT verification](references/screen-reader-behavior.md) and
[source provenance](references/sources.yaml).
