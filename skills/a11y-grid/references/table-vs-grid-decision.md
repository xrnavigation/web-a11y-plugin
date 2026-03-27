# Table vs Grid Decision

## The Core Question

Most tabular data should use an HTML `<table>`. The `role="grid"` pattern is only appropriate for spreadsheet-like interfaces where most cells are interactive widgets.

## Decision Criteria

### Use HTML `<table>` (or `role="table"`) when:

| Criterion | Explanation |
|-----------|-------------|
| Primary purpose is reading data | Users consume, compare, or reference information |
| Few or no interactive elements | Links, buttons in some cells are fine — they don't make it a grid |
| Table-level controls | Sorting, filtering, pagination act on the whole table |
| Content/website context | Discoverability matters more than navigation speed |

> "A WAI-ARIA table is a static tabular structure containing one or more rows that each contain one or more cells; it is not an interactive widget."
> — [APG Table Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/table/)

### Use `role="grid"` when:

| Criterion | Explanation |
|-----------|-------------|
| Primary purpose is editing/manipulating | Spreadsheet-like data entry or manipulation |
| Most cells are interactive widgets | Inputs, selects, checkboxes in most cells |
| App-like interface | Admin dashboards, management systems, extended-use tools |
| Need 2D arrow-key navigation | Navigating a dense field of interactive controls |

> "If you want an Excel-like experience, ARIA grid may be a good fit."
> — [Adrian Roselli, ARIA Grid As an Anti-Pattern](https://adrianroselli.com/2020/07/aria-grid-as-an-anti-pattern.html)

## The Two-Question Test

```
Question 1: Is the primary goal CONSUMING data or INTERACTING with data?
Question 2: Do MOST cells require interaction, or just a few?

Consuming + few interactive cells → table
Consuming + many interactive cells → probably still table (consider if cells can be simplified)
Manipulating + most cells interactive → grid
Manipulating + few interactive cells → table with interactive cells
```

## Examples

### Table (NOT grid):
- Product listing with "Add to cart" buttons
- User directory with email links
- Log viewer with sortable columns
- Data dashboard with read-only metrics
- Report with filterable/paginated rows

### Grid (genuinely needed):
- Spreadsheet application
- Bulk data entry form (editable cells throughout)
- Scheduling matrix where every cell is a toggleable time slot
- Configuration matrix with dropdowns/checkboxes in every cell

## Common Traps

### "But my table has sorting" — still a table
> "Tables can be sortable, filterable, virtualized, and can contain links and buttons without needing to be a grid."
> — [Sarah Higley, Grids Part 1](https://sarahmhigley.com/writing/grids-part1/)

### "But my rows are clickable" — still a table
> "Don't use ARIA grid roles simply to make rows clickable in a table."
> — [Adrian Roselli](https://adrianroselli.com/2023/11/dont-turn-a-table-into-an-aria-grid-just-for-a-clickable-row.html)

Use checkboxes for row selection, or links within cells for navigation.

### "But my table has inline editing on one column" — still a table
One editable column in an otherwise read-only table does not justify grid semantics. Use a button or input within the relevant cells.

## Sources

- [APG Table Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/table/)
- [APG Grid Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)
- [Adrian Roselli, ARIA Grid As an Anti-Pattern](https://adrianroselli.com/2020/07/aria-grid-as-an-anti-pattern.html)
- [Adrian Roselli, Don't Turn a Table into an ARIA Grid Just for a Clickable Row](https://adrianroselli.com/2023/11/dont-turn-a-table-into-an-aria-grid-just-for-a-clickable-row.html)
- [Sarah Higley, Grids Part 1: To grid or not to grid](https://sarahmhigley.com/writing/grids-part1/)
