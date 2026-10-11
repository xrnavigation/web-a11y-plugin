# Sortable tables

Keep table semantics for ordinary sortable data. Put a native button in each
sortable header; put `aria-sort` on the header currently expressing the sort,
not on the button. Update visual state and actual row order together
([APG sortable table](https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/)).

```html
<table id="directory">
  <caption>Employee directory. Activate a column button to sort.</caption>
  <thead><tr>
    <th scope="col" aria-sort="ascending">
      <button type="button" data-sort="name">Name <span aria-hidden="true">▲</span></button>
    </th>
    <th scope="col"><button type="button" data-sort="date">Start date</button></th>
  </tr></thead>
  <tbody><tr><th scope="row">Alex</th><td>2024-04-01</td></tr></tbody>
</table>
```

This scaffold needs data-aware sort logic. Parse dates/numbers according to
the actual data model rather than sorting every displayed string identically.
Keep focus on the invoked sort button while rows reorder.

```js
function updateSortHeader(table, selectedHeader, direction) {
  table.querySelectorAll('[aria-sort]').forEach(header => {
    header.removeAttribute('aria-sort');
  });
  selectedHeader.setAttribute('aria-sort', direction);
  // Caller sorts rows and updates the visible indicator using the same state.
}
```

`ascending` and `descending` indicate the order; `none` is a valid ARIA value,
although removing it from unsorted headers keeps the pattern concise
([WAI-ARIA aria-sort](https://www.w3.org/TR/wai-aria-1.2/#aria-sort)).

Test actual header state, button access and resulting order. If supported
combinations fail to communicate an important result, add a concise targeted
status message and check duplicate announcements. Do not assume a universal
screen reader support matrix or clear live text on an arbitrary timer.
