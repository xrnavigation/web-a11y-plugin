---
name: a11y-grid
description: Guides accessible data grid, interactive table, and sortable table implementation. Auto-invokes when creating data grids, spreadsheet interfaces, sortable tables, or interactive table cells. Critical distinction — most data tables do NOT need role="grid". Covers table vs grid decision, HTML table accessibility, sortable columns, and the APG grid pattern.
allowed-tools: Read, Glob, Grep
compatibility: "Claude Code, Codex CLI, Gemini CLI"
---

# Accessible Data Grids & Tables

> "Tables can be sortable, filterable, virtualized, and can contain links and buttons without needing to be a grid."
> — [Sarah Higley, Grids Part 1](https://sarahmhigley.com/writing/grids-part1/)

> "Don't use ARIA grid roles simply to make rows clickable in a table."
> — [Adrian Roselli](https://adrianroselli.com/2023/11/dont-turn-a-table-into-an-aria-grid-just-for-a-clickable-row.html)

Most data tables do NOT need `role="grid"`. The grid pattern is for spreadsheet-like interfaces where most cells are interactive widgets. Getting this wrong is a common and serious accessibility mistake — it breaks keyboard navigation expectations for screen reader users.

---

## 1. Table vs Grid Decision

This is the single most important decision. Get it wrong and everything downstream breaks.

> "A WAI-ARIA table is a static tabular structure containing one or more rows that each contain one or more cells; it is not an interactive widget."
> — [APG Table Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/table/)

### The Two-Question Test

1. Is the primary goal **consuming data** or **interacting with data**?
2. Do **most cells** require interaction, or just a few?

**Consuming + few interactive cells = table.**
**Manipulating + most cells interactive = grid.**

### Use HTML `<table>` (NOT grid) when:

- Users primarily **read and understand** data
- The table contains few or no interactive elements (links, buttons in cells are fine)
- Sorting, filtering, pagination act on the whole table, not individual cells
- Content is on a website/content page

### Use `role="grid"` when:

- Users primarily **edit, manipulate, or interact** with cell content (spreadsheet-like)
- Most or all cells contain interactive widgets requiring efficient navigation
- The interface is app-like (admin dashboards, data management) where users spend significant time
- You genuinely need two-dimensional arrow-key navigation among cells

> "If you want an Excel-like experience, ARIA grid may be a good fit."
> — [Adrian Roselli, ARIA Grid As an Anti-Pattern](https://adrianroselli.com/2020/07/aria-grid-as-an-anti-pattern.html)

For the full decision criteria, see: `${CLAUDE_SKILL_DIR}/references/table-vs-grid-decision.md`

---

## 2. HTML Table Accessibility

When you decide it's a table (the common case), get the basics right:

### Caption — the table's accessible name

```html
<table>
  <caption>Quarterly sales by region</caption>
  <!-- ... -->
</table>
```

- `<caption>` provides the accessible name for the table ([APG Table Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/table/))
- If a visible heading exists elsewhere, use `aria-labelledby` instead
- All screen readers announce the caption when entering the table

### Headers — `<th>` with `scope`

```html
<thead>
  <tr>
    <th scope="col">Name</th>
    <th scope="col">Email</th>
    <th scope="col">Role</th>
  </tr>
</thead>
<tbody>
  <tr>
    <th scope="row">Alice</th>
    <td>alice@example.com</td>
    <td>Admin</td>
  </tr>
</tbody>
```

- Use `scope="col"` for column headers, `scope="row"` for row headers ([W3C Tables Tutorial](https://www.w3.org/WAI/tutorials/tables/))
- For headers spanning multiple columns/rows: `scope="colgroup"` or `scope="rowgroup"`
- For complex multi-level tables: use `id` on `<th>` and `headers` attribute on `<td>` — last resort, prefer simpler structures

### Structural rules

- Header cells must use `<th>`, data cells must use `<td>` — never interchange them
- Do not use tables for layout — use CSS
- **Do not override CSS `display` on table elements** — see Section 5

---

## 3. Sortable Tables

Sortable tables do NOT require `role="grid"`. This is a common misconception. A standard `<table>` with buttons in headers works correctly. ([Adrian Roselli, Sortable Table Columns](https://adrianroselli.com/2021/04/sortable-table-columns.html); [APG Sortable Table Example](https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/))

### Recommended pattern

```html
<table>
  <caption>
    Employee directory
    <span class="sr-only">. Column headers with buttons are sortable.</span>
  </caption>
  <thead>
    <tr>
      <th aria-sort="ascending">
        <button>
          Name
          <span aria-hidden="true">▲</span>
        </button>
      </th>
      <th>
        <button>
          Date
          <span aria-hidden="true">▲</span>
        </button>
      </th>
      <th>Address</th><!-- not sortable, no button -->
    </tr>
  </thead>
  <!-- tbody -->
</table>
```

### Key rules

1. Place `aria-sort` on the `<th>`, NOT the `<button>` ([Roselli](https://adrianroselli.com/2021/04/sortable-table-columns.html))
2. Only set `aria-sort` on the **currently sorted column** — remove from all others
3. Values: `"ascending"` or `"descending"`. Do NOT use `"none"` — omit the attribute entirely for unsorted columns
4. Use `<button>` inside `<th>` for the sort trigger — gives keyboard access for free
5. Visual sort indicators should use `aria-hidden="true"` and not rely solely on color (WCAG 1.4.1)

### Screen reader compatibility for `aria-sort`

VoiceOver on macOS and TalkBack do NOT announce sort state changes. Add an `aria-live="polite"` region that briefly announces the sort change, then clears after ~1 second. ([a11ysupport.io](https://a11ysupport.io/tech/aria/aria-sort_attribute))

For the full sortable table reference, see: `${CLAUDE_SKILL_DIR}/references/sortable-tables.md`

---

## 4. APG Grid Pattern

When you genuinely need a grid (spreadsheet-like interface), follow the [APG Grid Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/grid/) exactly.

### Required ARIA structure

```
grid (aria-label or aria-labelledby required)
  > rowgroup (optional — thead/tbody/tfoot equivalent)
    > row
      > gridcell | columnheader | rowheader
```

A `row` must be owned by `grid`, `rowgroup`, or `treegrid`. A `gridcell` must be owned by `row`. ([WAI-ARIA 1.2, grid role](https://www.w3.org/TR/wai-aria-1.2/#grid))

### Required states and properties

- **`aria-label`** or **`aria-labelledby`** on the grid — always required
- **`aria-sort`** on column headers — when sorted
- **`aria-readonly`** on cells — to mark non-editable cells
- **`aria-selected`** — for cell/row/column selection
- **`aria-colcount`** / **`aria-rowcount`** — when using virtual scrolling (not all rows/cols in DOM)
- **`aria-colindex`** / **`aria-rowindex`** — cell position when virtualized

### Focus management

Two patterns for cell focus:

1. **Cell contains a single widget** (button, link, checkbox) — focus the widget directly
2. **Cell contains text/graphics** — focus the cell itself (`tabindex="-1"` on the `<td>` or `<div role="gridcell">`)

Cells with multiple widgets: Enter/F2 activates edit mode, Escape restores grid navigation.

### Keyboard interaction

Full keyboard spec in: `${CLAUDE_SKILL_DIR}/references/keyboard-interaction.md`

Key points:
- Arrow keys move between cells (not Tab)
- Tab exits the grid entirely
- Enter/F2 toggle edit mode within a cell
- Home/End move to first/last cell in row
- Ctrl+Home/Ctrl+End move to first/last cell in grid

### Screen reader behavior differences

- **JAWS**: Announces as "grid", triggers forms mode — arrow keys navigate cells, regular reading keys stop working ([PowerMapper](https://www.powermapper.com/tests/screen-readers/tables/table-role-grid/))
- **NVDA**: Announces as "table" even with `role="grid"` — less behavioral impact in browse mode
- **VoiceOver**: Announces as "table", no forms/application mode distinction

**Critical**: A grid that works in VoiceOver testing may be broken for JAWS/NVDA users. Do not test grids with VoiceOver alone. ([PowerMapper](https://www.powermapper.com/tests/screen-readers/tables/table-role-grid/))

---

## 5. CSS Display Overrides Warning

Overriding `display` on `<table>`, `<tr>`, `<td>` elements removes their default semantics in some browser/AT combinations.

```css
/* WRONG — breaks table semantics */
table { display: grid; }
tr { display: flex; }
td { display: block; }

/* WORKAROUND — add roles back manually */
table[role="table"] { display: grid; }
tr[role="row"] { display: flex; }
td[role="cell"] { display: block; }
```

Adding explicit ARIA roles can restore semantics, but this is fragile. Prefer keeping native `display` values on table elements. ([Sarah Higley, Grids Part 2](https://sarahmhigley.com/writing/grids-part2/))

---

## 6. Common Mistakes

### 6.1 Using grid when table suffices

The #1 mistake. Tables with sorting, filtering, links in cells, and pagination are still tables. Grid is only for when **most cells themselves** are interactive widgets. ([Sarah Higley](https://sarahmhigley.com/writing/grids-part1/); [Roselli](https://adrianroselli.com/2023/11/dont-turn-a-table-into-an-aria-grid-just-for-a-clickable-row.html))

### 6.2 Using grid for clickable rows

```html
<!-- WRONG -->
<table role="grid">
  <tr role="row" onclick="navigate()" tabindex="0">...</tr>
</table>

<!-- RIGHT — use checkboxes for row selection -->
<table>
  <tr>
    <td><input type="checkbox" aria-label="Select row 1"></td>
    <td>...</td>
  </tr>
</table>
```

For clickable rows, use a checkbox or link in each row instead of grid semantics. ([Roselli](https://adrianroselli.com/2023/11/dont-turn-a-table-into-an-aria-grid-just-for-a-clickable-row.html))

### 6.3 Putting `role="grid"` on an HTML `<table>`

Adding `role="grid"` to a `<table>` can create semantic conflicts. Build grid widgets from `<div>`s with explicit ARIA roles, or use a plain `<table>` without the grid role.

### 6.4 Ignoring responsive design

Grid navigation assumes a fixed two-dimensional layout. When content reflows responsively, arrow key behavior contradicts the visual layout. This breaks the user's mental model. ([Roselli](https://adrianroselli.com/2020/07/aria-grid-as-an-anti-pattern.html))

### 6.5 Trusting data grid library accessibility claims

Most data grid libraries (AG Grid, DataTables, etc.) claim accessibility but have significant gaps. Always test with actual screen readers — automated tests cannot verify grid keyboard interaction works correctly. ([Roselli](https://adrianroselli.com/2020/07/aria-grid-as-an-anti-pattern.html))

### 6.6 Breaking table semantics with CSS display overrides

See Section 5. Using `display: flex`, `display: grid`, or `display: block` on table elements removes their semantics in some browser/AT combinations. ([Sarah Higley, Grids Part 2](https://sarahmhigley.com/writing/grids-part2/))

For code examples and fixes, see: `${CLAUDE_SKILL_DIR}/references/common-mistakes.md`

---

## 7. Cross-References

- `aria-decision-framework` — the five rules of ARIA; decision tree for when to use ARIA at all
- `a11y-tree` — tree view patterns (for hierarchical data, not tabular data)

For detailed reference material:

- `${CLAUDE_SKILL_DIR}/references/table-vs-grid-decision.md` — full decision criteria with examples
- `${CLAUDE_SKILL_DIR}/references/keyboard-interaction.md` — complete keyboard spec for grids
- `${CLAUDE_SKILL_DIR}/references/sortable-tables.md` — sortable table implementation details
- `${CLAUDE_SKILL_DIR}/references/common-mistakes.md` — anti-patterns with code examples and citations
- `${CLAUDE_SKILL_DIR}/references/sources.yaml` — provenance for all cited sources
