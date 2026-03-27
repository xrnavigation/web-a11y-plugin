# Sortable Table Columns

Sources: [Adrian Roselli, Sortable Table Columns](https://adrianroselli.com/2021/04/sortable-table-columns.html), [APG Sortable Table Example](https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/)

## Key Principle

Sortable tables do NOT require `role="grid"`. A standard `<table>` with `<button>` elements in `<th>` headers works correctly and is better supported across assistive technology.

## Recommended HTML Structure

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
          Department
          <span aria-hidden="true">▲</span>
        </button>
      </th>
      <th>Address</th><!-- not sortable, no button -->
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alice Smith</td>
      <td>Engineering</td>
      <td>123 Main St</td>
    </tr>
    <!-- more rows -->
  </tbody>
</table>
```

## Implementation Rules

### 1. `aria-sort` placement

Place `aria-sort` on the `<th>`, NOT on the `<button>` inside it. The sort state describes the column, not the button.

### 2. Only one sorted column at a time

Set `aria-sort` only on the **currently sorted column**. Remove the attribute entirely from all other columns. Do NOT set `aria-sort="none"` — omit the attribute.

### 3. Valid `aria-sort` values

- `"ascending"` — sorted lowest to highest
- `"descending"` — sorted highest to lowest
- Do NOT use `"none"` — just omit the attribute
- Do NOT use `"other"`

### 4. Sort trigger must be a `<button>`

Using `<button>` inside `<th>` gives keyboard access for free — no custom keyboard handlers needed. The button is focusable and activatable with Enter and Space.

### 5. Visual sort indicators

- Use `aria-hidden="true"` on visual indicators (arrows, icons)
- Do not rely solely on color to indicate sort direction (WCAG 1.4.1 Use of Color)
- Consider using CSS `::after` pseudo-elements for sort arrows

### 6. Caption with sort instructions

Append a visually-hidden description to the caption explaining that columns with buttons are sortable. This helps screen reader users understand the interaction pattern before encountering the buttons.

```html
<caption>
  Table title
  <span class="sr-only">. Column headers with buttons are sortable.</span>
</caption>
```

## Screen Reader Compatibility

| Screen Reader | Platform | Announces sort change? |
|--------------|----------|----------------------|
| NVDA | Firefox | Yes |
| JAWS | Chrome | Yes |
| Narrator | Edge | Yes |
| VoiceOver | iPadOS | Yes |
| VoiceOver | macOS | **No** |
| TalkBack | Android | **No** |

Source: [a11ysupport.io, aria-sort](https://a11ysupport.io/tech/aria/aria-sort_attribute)

### Workaround for VoiceOver/macOS and TalkBack

Use an `aria-live="polite"` region to announce sort state changes:

```html
<div aria-live="polite" class="sr-only" id="sort-status"></div>
```

```javascript
function onSort(column, direction) {
  // Update table sorting...

  // Announce to screen readers that don't support aria-sort announcements
  const status = document.getElementById('sort-status');
  status.textContent = `Sorted by ${column}, ${direction}`;

  // Clear after delay to avoid redundant announcements on subsequent navigation
  setTimeout(() => { status.textContent = ''; }, 1000);
}
```

## Common Mistakes

1. **Using `role="grid"` for a sortable table** — sorting does not require grid semantics
2. **Putting `aria-sort` on the button** — it belongs on the `<th>`
3. **Setting `aria-sort="none"` on unsorted columns** — omit the attribute entirely
4. **Making the entire `<th>` clickable without a `<button>`** — keyboard users can't activate it
5. **Using only color to show sort direction** — fails WCAG 1.4.1

## Sources

- [Adrian Roselli, Sortable Table Columns](https://adrianroselli.com/2021/04/sortable-table-columns.html)
- [APG Sortable Table Example](https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/)
- [a11ysupport.io, aria-sort attribute](https://a11ysupport.io/tech/aria/aria-sort_attribute)
- [MDN, ARIA: aria-sort attribute](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-sort)
