# Tree mistakes

## Leaves falsely exposed as expandable

```html
<!-- Wrong for a leaf. -->
<li role="treeitem" aria-expanded="false">README.md</li>
<!-- Correct leaf semantics within a tree. -->
<li role="treeitem" tabindex="-1">README.md</li>
```

Only parent nodes expose expansion state
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)).

## Roles mistaken for keyboard implementation

Wrong: add a tree role and a click-only handler, then call it a working tree.
Better structural starting point, still requiring JavaScript behavior:

```html
<!-- Incomplete skeleton: implement arrows, focus and visibility updates. -->
<h3 id="project-files-label">Project files</h3>
<ul role="tree" aria-labelledby="project-files-label">
  <li role="treeitem" aria-labelledby="source-label" tabindex="0" aria-expanded="false">
    <span id="source-label">src</span>
    <ul role="group" hidden>
      <li role="treeitem" tabindex="-1">index.ts</li>
    </ul>
  </li>
</ul>
```

The label resolves and the parent owns actual children. No undefined framework
handler implies this markup supplies keyboard behavior. Implement core
navigation and default activation, recommended type-ahead, and optional sibling
expansion only if offered
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)).

## Duplicate selection state

Wrong: mirror one choice into both `aria-selected` and `aria-checked`.
Right: choose one consistent state. Rare distinct purposes can use both only
when their meanings are apparent and each has a separate control method
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)).

## Navigation trees declared forbidden

Wrong: claim a tree role is invalid solely because items navigate to pages.
Right: prefer ordinary links/disclosures for typical navigation, or implement a
navigation tree's complete composite contract when justified. APG includes that
pattern ([APG navigation tree](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/examples/treeview-navigation/)).

## Default activation confused with expansion

Wrong: always expand a parent on Enter, even when its task is opening a page.
Right: define the node's default action; use arrows for tree expansion and
navigation. Enter expansion is one possible parent action
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)).

## Grid shortcuts copied into treegrid

Wrong: Ctrl+End moves cell focus diagonally to the bottom-right cell, or
Ctrl+Space always selects a column. Right: keep the cell's column for
Ctrl+Home/End; Ctrl+Space selects its column with cell focus or all cells with
row focus, if selection is provided
([APG treegrid](https://www.w3.org/WAI/ARIA/apg/patterns/treegrid/)).

## Partial rendering loses hierarchy

Wrong: report sibling count using only the visible DOM slice.
Right: provide level, set size and position for the intended tree when complete
nodes are not rendered. Test actual exposure rather than promising exact speech
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)).
