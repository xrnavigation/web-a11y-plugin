# Menu Button Pattern
## Contents

- [Complete Implementation Example](#complete-implementation-example)
- [Button Requirements](#button-requirements)
  - [aria-haspopup Values and Screen Reader Behavior](#aria-haspopup-values-and-screen-reader-behavior)
- [Menu Requirements](#menu-requirements)
  - [Valid Children](#valid-children)
- [Focus Management](#focus-management)
  - [Opening the Menu](#opening-the-menu)
  - [Closing the Menu](#closing-the-menu)
- [Menu with Checkbox Items](#menu-with-checkbox-items)
- [Menu with Radio Items](#menu-with-radio-items)
- [Common Implementation Mistakes](#common-implementation-mistakes)
  - [Wrong: div as menu button](#wrong-div-as-menu-button)
  - [Wrong: Missing aria-expanded](#wrong-missing-aria-expanded)
  - [Wrong: Focus not managed on open](#wrong-focus-not-managed-on-open)
  - [Wrong: Focus not returned on close](#wrong-focus-not-returned-on-close)


Source: [APG Menu Button Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/)

A menu button is a button that opens a menu of actions. It is the most common legitimate use of ARIA menu roles on the web.

---

## Complete Implementation Example

```html
<button
  id="actions-btn"
  aria-haspopup="menu"
  aria-expanded="false"
  aria-controls="actions-menu"
>
  Actions ▾
</button>

<ul id="actions-menu" role="menu" aria-labelledby="actions-btn" hidden>
  <li role="menuitem" tabindex="-1">Cut</li>
  <li role="menuitem" tabindex="-1">Copy</li>
  <li role="menuitem" tabindex="-1">Paste</li>
  <li role="separator"></li>
  <li role="menuitem" aria-disabled="true" tabindex="-1">Undo</li>
</ul>
```

---

## Button Requirements

| Property | Value | Notes |
|----------|-------|-------|
| Element | `<button>` | Use native button, not `<div role="button">` |
| `aria-haspopup` | `"menu"` | Static — never changes regardless of menu state |
| `aria-expanded` | `"true"` / `"false"` | Dynamic — reflects current menu state |
| `aria-controls` | ID of menu element | Optional but recommended for programmatic association |

### `aria-haspopup` Values and Screen Reader Behavior

VoiceOver announces `aria-haspopup` values differently:

| Value | VoiceOver Announcement |
|-------|----------------------|
| `"true"` | "Settings, menu button, group" |
| `"menu"` | "Settings, menu pop-up, button" |

JAWS adds instructions regardless of value: "Press Space to activate the menu. Then navigate with arrow keys."

Source: [Manuel Matuzovic, 2023](https://www.matuzo.at/blog/2023/aria-haspopup/)

---

## Menu Requirements

| Property | Value |
|----------|-------|
| `role` | `menu` |
| `aria-labelledby` or `aria-label` | Accessible name (required) |
| `tabindex` | `-1` on the container |
| Visibility | `hidden` attribute or equivalent when closed |

### Valid Children

A `menu` may only contain:

- `menuitem`
- `menuitemcheckbox`
- `menuitemradio`
- `group` (wrapping related items)
- `separator` (non-focusable divider)

Source: [MDN, "ARIA: menu role"](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menu_role)

---

## Focus Management

### Opening the Menu

1. Set `aria-expanded="true"` on the button
2. Show the menu (remove `hidden`)
3. Move focus to the first `menuitem` with `tabindex="-1"` via `.focus()`

**Persistent selection pattern:** For menus with checkbox/radio items, focus the currently-checked item instead of the first item. This places keyboard users at the optimal position and reminds them of their current selection.

Source: [Heydon Pickering, Inclusive Components](https://inclusive-components.design/menus-menu-buttons/)

### Closing the Menu

**On Escape:**
1. Hide the menu (add `hidden`)
2. Set `aria-expanded="false"` on the button
3. Return focus to the button

**On item activation (Enter):**
1. Execute the item's action
2. Hide the menu
3. Set `aria-expanded="false"`
4. Return focus to the button

**On Tab:**
1. Hide the menu
2. Set `aria-expanded="false"`
3. Let default Tab behavior move focus to next focusable element

**On click outside:**
1. Hide the menu
2. Set `aria-expanded="false"`
3. Do not move focus — let the click target receive it

---

## Menu with Checkbox Items

```html
<button aria-haspopup="menu" aria-expanded="false" aria-controls="view-menu">
  View ▾
</button>

<ul id="view-menu" role="menu" aria-label="View options" hidden>
  <li role="menuitemcheckbox" aria-checked="true" tabindex="-1">
    Show toolbar
  </li>
  <li role="menuitemcheckbox" aria-checked="true" tabindex="-1">
    Show status bar
  </li>
  <li role="menuitemcheckbox" aria-checked="false" tabindex="-1">
    Show line numbers
  </li>
</ul>
```

- **Space** toggles checked state, menu stays open (allows toggling multiple items)
- **Enter** toggles checked state, menu closes

---

## Menu with Radio Items

```html
<button aria-haspopup="menu" aria-expanded="false" aria-controls="size-menu">
  Text Size ▾
</button>

<ul id="size-menu" role="menu" aria-label="Text size" hidden>
  <li role="group" aria-label="Font size">
    <li role="menuitemradio" aria-checked="false" tabindex="-1">Small</li>
    <li role="menuitemradio" aria-checked="true" tabindex="-1">Medium</li>
    <li role="menuitemradio" aria-checked="false" tabindex="-1">Large</li>
  </li>
</ul>
```

- When activated, set own `aria-checked="true"` and all siblings in group to `"false"`
- Use `group` or `separator` to define separate radio groups within the same menu

---

## Common Implementation Mistakes

### Wrong: `<div>` as menu button

```html
<!-- WRONG — not keyboard accessible, no implicit button role -->
<div onclick="toggleMenu()" aria-haspopup="menu">Actions</div>

<!-- RIGHT — native button with full keyboard support -->
<button onclick="toggleMenu()" aria-haspopup="menu" aria-expanded="false">
  Actions
</button>
```

### Wrong: Missing `aria-expanded`

```html
<!-- WRONG — screen reader cannot tell if menu is open or closed -->
<button aria-haspopup="menu">Actions</button>

<!-- RIGHT -->
<button aria-haspopup="menu" aria-expanded="false">Actions</button>
```

### Wrong: Focus not managed on open

```js
// WRONG — menu opens but focus stays on button
menu.hidden = false;

// RIGHT — focus moves to first item
menu.hidden = false;
menu.querySelector('[role="menuitem"]').focus();
```

### Wrong: Focus not returned on close

```js
// WRONG — focus lost when menu closes
menu.hidden = true;

// RIGHT — focus returns to button
menu.hidden = true;
button.focus();
```
