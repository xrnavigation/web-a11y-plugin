# Choose table or grid

Use the interaction contract to choose, rather than a count of buttons or an
“app-like” appearance. A table represents tabular data; a grid is a composite
widget with author-managed focus and two-dimensional navigation
([APG table](https://www.w3.org/WAI/ARIA/apg/patterns/table/),
[APG grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)).

| Task | Starting pattern | Required implementation |
|---|---|---|
| Read rows, follow a link | Native table | Headers, name, native links |
| Sort by a column | Native table with header buttons | Actual reorder, header sort state |
| Edit cells with spreadsheet navigation | Data grid | Arrow navigation, editor entry/exit, focus and selection |
| Navigate a composite card layout | Layout grid if justified | Meaningful arrow order and composite focus |

A sortable table example keeps table semantics
([APG sortable table](https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/)).

A grid can use `<table role="grid">`; native table rows/cells provide structure.
If using divs, explicitly supply row and cell/header roles. A layout grid need
not resemble a data table, but its movement must make sense as content reflows
([APG grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)).

Before choosing grid, specify entry/exit, arrows, boundaries, editing and
selection. If those behaviors are not part of the product, ordinary table
controls may serve the task with less custom focus management. Verify the
chosen pattern with target keyboard and screen reader combinations.
