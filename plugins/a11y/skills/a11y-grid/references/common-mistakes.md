# Table and grid mistakes

## Sorting treated as a reason for grid roles

Wrong: add `role="grid"` to expose ordinary sort buttons.
Right: put buttons in native table headers and `aria-sort` on the sorted header
([APG sortable table](https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/)).

## Native tables banned from grids

```html
<!-- Valid grid foundation: add the full keyboard interaction. -->
<table role="grid" aria-label="Inventory editor">
  <tbody><tr><td tabindex="0">Pencil</td><td tabindex="-1">12</td></tr></tbody>
</table>
```

`role="grid"` on a table is permitted by the APG grid pattern. A grid built from
divs instead needs explicit row and cell/header roles. The failure is incomplete
behavior, not using native table markup
([APG grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)).

## Click-only row interaction

```html
<!-- Wrong: no native activation control. -->
<tr onclick="openRecord()"><td>Alex</td></tr>
<!-- Right for navigation: use a link in the relevant cell. -->
<tr><th scope="row"><a href="/people/alex">Alex</a></th></tr>
```

Use the control matching the action: a link for navigation, checkbox for
selection, or button for an action. A table may contain these controls without
becoming a grid ([APG table](https://www.w3.org/WAI/ARIA/apg/patterns/table/)).

## Arrows collide with a cell editor

Wrong: consume every arrow key while the user edits text in a cell.
Right: distinguish grid navigation from interaction within a cell, with an
entry/exit mechanism such as Enter/F2 and Escape. Test all contained widgets
([APG grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)).
