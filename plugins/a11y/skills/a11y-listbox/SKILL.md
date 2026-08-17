---
name: a11y-listbox
description: Guides accessible listbox implementation for single and multi-select lists per APG patterns. Auto-invokes when creating listboxes, selection lists, option lists, or custom multi-select components. Covers required ARIA, keyboard interaction, single vs multi-select, and reorderable lists (WCAG 2.2 dragging alternatives).
allowed-tools: Read, Glob, Grep
---

# Accessible Listbox Implementation

> "It is highly recommended using the HTML select element... because there is a lot of keyboard interactivity to manage focus for all the descendants, and native HTML elements provide this functionality for you for free."
> — [MDN: ARIA listbox role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listbox_role)

A listbox presents a list of options and allows the user to select one or more. Every ARIA listbox you build is a promise to implement all keyboard interaction, focus management, and state updates yourself. Native `<select>` does this for free.

---

## 1. Decision: Native `<select>` vs ARIA Listbox

### Use native `<select>` by default

Native `<select>` scored 100% success rate and 97.5% usability across all screen readers tested ([24a11y, "Select Your Poison Part 2"](https://www.24a11y.com/2019/select-your-poison-part-2/)). Custom ARIA implementations consistently scored lower.

### Use ARIA listbox only when

- Options must contain images or complex content that `<select>` cannot render ([APG Listbox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/))
- A dual-listbox transfer pattern or other composite widget is required
- Custom scrollable lists with non-text layouts are needed

### Use combobox pattern instead when

- The dropdown needs filtering/autocomplete — see `a11y-combobox` skill
- You need a custom-styled single-select that collapses to a button — use the [APG select-only combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-select-only/), not a standalone listbox

### Use checkboxes/radio buttons when

- Single-select with few options: radio button group
- Multi-select with few options: checkbox group

These outperform custom multi-select for usability ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listbox_role); [24a11y](https://www.24a11y.com/2019/select-your-poison/)).

---

## 2. Required ARIA Structure

### Single-select listbox

```html
<label id="color-label">Favorite color</label>
<ul role="listbox"
    tabindex="0"
    aria-labelledby="color-label">
  <li role="option" id="opt-red" aria-selected="true">Red</li>
  <li role="option" id="opt-blue" aria-selected="false">Blue</li>
  <li role="option" id="opt-green" aria-selected="false">Green</li>
</ul>
```

### Multi-select listbox

```html
<label id="toppings-label">Toppings</label>
<ul role="listbox"
    tabindex="0"
    aria-labelledby="toppings-label"
    aria-multiselectable="true">
  <li role="option" id="top-cheese" aria-selected="true">Cheese</li>
  <li role="option" id="top-peppers" aria-selected="false">Peppers</li>
  <li role="option" id="top-onions" aria-selected="false">Onions</li>
</ul>
```

### Required attributes summary

| Component | Attribute | When |
|-----------|-----------|------|
| Container | `role="listbox"` | Always |
| Container | `tabindex="0"` | Always |
| Container | `aria-labelledby` or `aria-label` | Always |
| Container | `aria-multiselectable="true"` | Multi-select only |
| Container | `aria-orientation="horizontal"` | Horizontal layout only (default is `vertical`) |
| Container | `aria-activedescendant` | When using activedescendant focus management |
| Option | `role="option"` | Always |
| Option | `aria-selected` | Always — every option needs `true` or `false` |
| Group | `role="group"` + `aria-label` | When grouping options |
| Virtualized | `aria-setsize` + `aria-posinset` | When not all options are in the DOM |

([APG Listbox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/); [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/#listbox))

---

## 3. Single vs Multi-select

The architectural difference: in single-select, **selection may follow focus** (arrow keys both move focus and change selection). In multi-select, **focus and selection are decoupled** — moving focus must not change existing selections ([APG Listbox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).

```js
// WRONG — selection follows focus in multi-select
function onArrowDown(listbox) {
  focusNext();
  if (listbox.getAttribute('aria-multiselectable') === 'true') {
    selectFocused(); // Destroys existing selections!
  }
}

// RIGHT — decouple focus from selection in multi-select
function onArrowDown(listbox) {
  focusNext();
  // In multi-select: focus moves, selection unchanged
  // User must press Space to toggle selection
}
```

### Focus landing behavior

- **Single-select**: Focus pre-selected option, or first option (which may auto-select)
- **Multi-select**: Focus first selected option, or first option. Never auto-select on focus.

([APG Listbox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/))

---

## 4. Keyboard Interaction Summary

### All listboxes

| Key | Behavior |
|-----|----------|
| Down Arrow | Move focus to next option |
| Up Arrow | Move focus to previous option |
| Home | Focus first option (recommended for 5+ options) |
| End | Focus last option (recommended for 5+ options) |
| Type-ahead | Focus matching option (recommended for 7+ options) |

### Single-select additions

| Key | Behavior |
|-----|----------|
| Space | Select focused option |
| Down/Up Arrow | May also select (selection follows focus) |

### Multi-select additions (recommended model)

| Key | Behavior |
|-----|----------|
| Space | Toggle selection of focused option |
| Shift + Down/Up | Move focus and toggle selection |
| Shift + Space | Select contiguous range |
| Ctrl + A | Select/deselect all |

For the complete keyboard spec including the alternative modifier-key model, see [references/keyboard-interaction.md](references/keyboard-interaction.md).

---

## 5. Reorderable Lists (WCAG 2.2)

WCAG 2.5.7 Dragging Movements (Level AA) requires that all drag-and-drop functionality provide a single-pointer alternative that does not require dragging ([WCAG 2.2 SC 2.5.7](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)).

A keyboard alternative alone is **insufficient** — touch-screen users may not have a physical keyboard. You must provide both:

1. **Keyboard reordering**: e.g., Alt + Arrow keys to move selected item
2. **Pointer-based non-drag alternative**: visible up/down buttons, "move to position" menu, or numeric input

### Compliant alternatives

```html
<!-- RIGHT — visible move buttons satisfy SC 2.5.7 -->
<li role="option" aria-selected="true">
  Item A
  <button aria-label="Move Item A up">Up</button>
  <button aria-label="Move Item A down">Down</button>
</li>
```

**Note:** The move buttons must be outside the `role="option"` element — interactive elements inside options are not valid. Use the Grid pattern if options need interactive children ([APG Listbox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).

([W3C Technique G219](https://www.w3.org/WAI/WCAG22/Techniques/general/G219.html); [Sparkbox](https://sparkbox.com/foundry/understanding_implementing_wcag_dragging_movements_accessibility))

---

## 6. Common Mistakes

### 6.1 Using ARIA listbox when native `<select>` suffices

```html
<!-- WRONG — unnecessary complexity -->
<div role="listbox" tabindex="0">
  <div role="option">Option 1</div>
</div>

<!-- RIGHT — native element, zero ARIA needed -->
<select>
  <option>Option 1</option>
</select>
```

Native elements get keyboard interaction for free ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listbox_role); [APG](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).

### 6.2 Missing `aria-selected` on options in multi-select

```html
<!-- WRONG — VoiceOver refuses to read options without explicit state -->
<ul role="listbox" aria-multiselectable="true">
  <li role="option">Cheese</li>
  <li role="option" aria-selected="true">Peppers</li>
</ul>

<!-- RIGHT — every option declares its selection state -->
<ul role="listbox" aria-multiselectable="true">
  <li role="option" aria-selected="false">Cheese</li>
  <li role="option" aria-selected="true">Peppers</li>
</ul>
```

When `aria-multiselectable="true"` is set, every option must have explicit `aria-selected` ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listbox_role)).

### 6.3 Interactive elements inside options

```html
<!-- WRONG — links/buttons inside role="option" are not valid -->
<li role="option">
  <a href="/details">Item A</a>
  <button>Remove</button>
</li>

<!-- RIGHT — use Grid pattern for interactive children -->
<div role="grid">
  <div role="row">
    <div role="gridcell"><a href="/details">Item A</a></div>
    <div role="gridcell"><button>Remove</button></div>
  </div>
</div>
```

([APG Listbox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/))

### 6.4 Missing `aria-orientation` on horizontal listboxes

The implicit orientation is `vertical`. Horizontal layouts must set `aria-orientation="horizontal"` explicitly, or arrow key expectations will be wrong ([WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/#listbox)).

### 6.5 No visible focus indicator

The focused option must have a visible focus ring or highlight. Without it, sighted keyboard users cannot orient ([WCAG 2.4.7](https://www.w3.org/WAI/WCAG21/Understanding/focus-visible.html)).

### 6.6 Not scrolling focused option into view

In scrollable listboxes, programmatic scroll-into-view on focus change is required. Without it, the focused option becomes invisible to sighted users.

---

## 7. Cross-References

- `aria-decision-framework` — decide whether you need ARIA at all (start here)
- `a11y-combobox` — for filterable/autocomplete dropdowns and styled select replacements

For detailed reference material:

- [references/keyboard-interaction.md](references/keyboard-interaction.md) — complete keyboard spec for both multi-select models
- [references/common-mistakes.md](references/common-mistakes.md) — expanded mistake catalog with screen reader details
- [references/screen-reader-behavior.md](references/screen-reader-behavior.md) — JAWS, NVDA, VoiceOver behavior notes
- [references/sources.yaml](references/sources.yaml) — provenance for all cited sources
