# Common Mistakes with Data Grids & Tables
## Contents

- [1. Using Grid When Table Suffices](#1-using-grid-when-table-suffices)
- [2. Using Grid for Clickable Rows](#2-using-grid-for-clickable-rows)
- [3. Putting role="grid" on an HTML table](#3-putting-rolegrid-on-an-html-table)
- [4. Ignoring Responsive Design](#4-ignoring-responsive-design)
- [5. Breaking Table Semantics with CSS Display](#5-breaking-table-semantics-with-css-display)
- [6. Trusting Data Grid Library Accessibility Claims](#6-trusting-data-grid-library-accessibility-claims)
- [Sources](#sources)


## 1. Using Grid When Table Suffices

The most common mistake. Any interactivity does NOT make a table into a grid.

> "Sometimes there seems to be the misconception that if a table has any interactivity, it must be a grid."
> — [Sarah Higley, Grids Part 1](https://sarahmhigley.com/writing/grids-part1/)

```html
<!-- WRONG — this is just a table with links -->
<table role="grid">
  <tr role="row">
    <td role="gridcell"><a href="/users/1">Alice</a></td>
    <td role="gridcell">alice@example.com</td>
  </tr>
</table>

<!-- RIGHT — plain table -->
<table>
  <tr>
    <td><a href="/users/1">Alice</a></td>
    <td>alice@example.com</td>
  </tr>
</table>
```

## 2. Using Grid for Clickable Rows

> "Don't use ARIA grid roles simply to make rows clickable in a table."
> — [Adrian Roselli](https://adrianroselli.com/2023/11/dont-turn-a-table-into-an-aria-grid-just-for-a-clickable-row.html)

```html
<!-- WRONG — grid semantics for row clicks -->
<table role="grid">
  <tr role="row" onclick="navigate('/users/1')" tabindex="0">
    <td role="gridcell">Alice</td>
    <td role="gridcell">Admin</td>
  </tr>
</table>

<!-- RIGHT — use a link or checkbox in the row -->
<table>
  <tr>
    <td><a href="/users/1">Alice</a></td>
    <td>Admin</td>
  </tr>
</table>

<!-- RIGHT — for row selection, use checkboxes -->
<table>
  <tr>
    <td><input type="checkbox" aria-label="Select Alice"></td>
    <td>Alice</td>
    <td>Admin</td>
  </tr>
</table>
```

## 3. Putting `role="grid"` on an HTML `<table>`

Adding `role="grid"` to an HTML `<table>` overrides its native table semantics. This can create confusion and semantic conflicts. If you genuinely need a grid, build it from `<div>` elements with explicit ARIA roles.

```html
<!-- PROBLEMATIC -->
<table role="grid">...</table>

<!-- BETTER — if you need a grid, use divs -->
<div role="grid" aria-label="Data editor">
  <div role="row">
    <div role="columnheader">Name</div>
    <div role="columnheader">Value</div>
  </div>
  <div role="row">
    <div role="gridcell">Setting A</div>
    <div role="gridcell"><input type="text" value="42"></div>
  </div>
</div>
```

## 4. Ignoring Responsive Design

Grid keyboard navigation assumes a fixed two-dimensional layout. When content reflows (e.g., on mobile), arrow keys contradict the visual layout.

> Grid navigation breaks down at smaller viewports when cells reflow.
> — [Adrian Roselli, ARIA Grid As an Anti-Pattern](https://adrianroselli.com/2020/07/aria-grid-as-an-anti-pattern.html)

**Solutions:**
- Degrade to a table or list layout on narrow viewports
- Remove grid role and keyboard handlers below a breakpoint
- Consider a responsive table pattern (stacked cards, horizontal scroll) instead of a grid

## 5. Breaking Table Semantics with CSS Display

Overriding `display` on table elements removes their semantics in some browser/AT combinations.

> CSS display properties can break the association between table elements and their semantic roles.
> — [Sarah Higley, Grids Part 2](https://sarahmhigley.com/writing/grids-part2/)

```css
/* WRONG — breaks semantics */
table { display: block; }
tr { display: flex; }
td { display: block; }

/* WORKAROUND — restore roles explicitly */
table[role="table"] { display: block; }
tr[role="row"] { display: flex; }
td[role="cell"] { display: block; }
```

Better: avoid overriding `display` on table elements altogether. Use wrapper elements for layout.

## 6. Trusting Data Grid Library Accessibility Claims

> Most data grid libraries claim accessibility support. Few deliver it fully.
> — [Adrian Roselli, ARIA Grid As an Anti-Pattern](https://adrianroselli.com/2020/07/aria-grid-as-an-anti-pattern.html)

**Always:**
- Test with actual screen readers (JAWS + Chrome, NVDA + Firefox, VoiceOver + Safari)
- Test keyboard-only navigation (no screen reader — just Tab and arrow keys)
- Verify the library handles focus management correctly
- Check that virtual scrolling preserves `aria-rowcount`/`aria-rowindex`

**Do not** rely on:
- The library's accessibility documentation alone
- Automated accessibility testing tools (they cannot verify keyboard interaction patterns)
- Testing with only one screen reader (especially not VoiceOver alone for grids)

## Sources

- [Sarah Higley, Grids Part 1](https://sarahmhigley.com/writing/grids-part1/)
- [Sarah Higley, Grids Part 2](https://sarahmhigley.com/writing/grids-part2/)
- [Adrian Roselli, ARIA Grid As an Anti-Pattern](https://adrianroselli.com/2020/07/aria-grid-as-an-anti-pattern.html)
- [Adrian Roselli, Don't Turn a Table into an ARIA Grid Just for a Clickable Row](https://adrianroselli.com/2023/11/dont-turn-a-table-into-an-aria-grid-just-for-a-clickable-row.html)
- [APG Grid Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)
