---
name: a11y-grid
description: Guides accessible data tables and interactive grids. Use when building tabular data, sortable tables, spreadsheet navigation, or grids with cell editing and selection.
---

# Accessible tables and grids

Choose a table for tabular information with ordinary links, buttons or sorting.
Choose a grid when the interface needs composite two-dimensional keyboard
navigation. Grids can serve data editing or layout; neither an application label
nor a percentage of interactive cells determines the correct role
([APG table](https://www.w3.org/WAI/ARIA/apg/patterns/table/),
[APG grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)).

## Ordinary sortable table

```html
<table>
  <caption>Employee directory</caption>
  <thead><tr>
    <th scope="col" aria-sort="ascending">
      <button type="button">Name <span aria-hidden="true">▲</span></button>
    </th>
    <th scope="col"><button type="button">Start date</button></th>
  </tr></thead>
  <tbody><tr><th scope="row">Alex</th><td>2024-04-01</td></tr></tbody>
</table>
```

This scaffold needs sorting logic. Put `aria-sort` on the sorted header and
move it when the sort column changes; keep the visual indicator consistent.
Sorting does not require a grid
([APG sortable table](https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/)).

## Interactive grid

A grid may use native table markup: `<table role="grid">` is supported by the
APG pattern. Native rows and cells supply their structural roles. A div-based
implementation must supply `row` and cell/header roles. Choose based on data and
behavior, not a ban on table elements
([APG grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)).

```html
<!-- Structural scaffold; add roving focus and arrow navigation. -->
<table role="grid" aria-label="Editable inventory">
  <tbody><tr>
    <td tabindex="0">Pencil</td><td tabindex="-1">12</td>
  </tr></tbody>
</table>
```

Give the grid a name. Implement one entry tab stop and arrow navigation among
cells or contained controls. Provide a documented way to enter/leave editing
when arrows are also needed by a cell's editor. Keep selection separate from
focus where the interaction needs it. Add virtualized row/column counts and
indices when the exposed subset would otherwise lose its position
([APG grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)).

## Verify the interaction

Test entry, exit, boundaries, editing and selection with keyboard and supported
screen readers. Check names, headers and row/column positions against the actual
rendered data. Check responsive layout and virtualization preserve meaningful
navigation. Do not equate an announced word such as “table” with a verdict on
the implemented grid.

Read [table/grid choices](references/table-vs-grid-decision.md),
[keyboard interaction](references/keyboard-interaction.md),
[sorting](references/sortable-tables.md),
[common mistakes](references/common-mistakes.md) and
[sources](references/sources.yaml).
