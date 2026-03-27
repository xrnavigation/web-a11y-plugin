---
name: a11y-menu
description: Guides accessible application menu and menu button implementation per APG patterns. Auto-invokes when creating menus, menubars, context menus, action dropdowns, or menu buttons. Critical distinction — site navigation is NOT a menu. Covers menu/menubar/menuitem roles, menuitemcheckbox, menuitemradio, and the menu button pattern.
allowed-tools: Read, Glob, Grep
compatibility: "Claude Code, Codex CLI, Gemini CLI"
---

# Accessible Menu Patterns

> **Site navigation is NOT a menu.** If you are building navigation links, stop here. Use `<nav>` with a list of links. See Section 1.

> "Generally, don't use `menu`, `menuitem`, `menubar`, `menuitemcheckbox`, or `menuitemradio`. Only if you build something like Google Docs... these are warranted."
> — Marco Zehe, Mozilla (cited in [Roselli, 2017](https://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html))

---

## 1. Navigation Is NOT a Menu

This is the most common mistake in menu accessibility. ARIA `menu`/`menubar`/`menuitem` roles exist exclusively for **application-style menus** — the kind in desktop software (File, Edit, View). They are never for website navigation.

### Why `role="menu"` Breaks Navigation

1. **Screen readers switch interaction modes.** JAWS enters forms mode; NVDA enters focus mode. Arrow keys stop reading content and are intercepted for menu navigation. Users can no longer browse the page normally. ([Tink.uk](https://tink.uk/understanding-screen-reader-interaction-modes/); [Accessible Culture](https://accessibleculture.org/articles/2012/09/aria-widgets-and-focus-forms-mode-support/))

2. **Keyboard expectations change completely.** `role="menu"` commits you to implementing Enter, Space, Down/Up/Left/Right Arrow, Home, End, Escape, and character-key navigation. Most site navs implement none of these. Users hear "menu," try menu keyboard commands, and nothing works. ([Roselli, 2017](https://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html))

3. **Navigation disappears from landmarks and link lists.** The `<nav>` landmark is replaced by a menu widget. Links given `role="menuitem"` vanish from the screen reader links list (Insert+F7 in JAWS). Users lose two primary ways to discover site structure. ([Roselli, 2017](https://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html))

4. **Broken parent-child relationships.** `<ul role="menu">` without `role="presentation"` on `<li>` and `role="menuitem"` on `<a>` creates orphaned elements, violating WCAG SC 1.3.1. ([Make Things Accessible](https://www.makethingsaccessible.com/guides/site-navigation-is-not-an-aria-menu/))

### Wrong vs Right

```html
<!-- WRONG — navigation is not an application menu -->
<nav>
  <ul role="menu">
    <li role="menuitem"><a href="/about">About</a></li>
    <li role="menuitem"><a href="/news">News</a></li>
  </ul>
</nav>

<!-- RIGHT — semantic navigation, no ARIA needed -->
<nav aria-label="Main">
  <ul>
    <li><a href="/about">About</a></li>
    <li><a href="/news">News</a></li>
  </ul>
</nav>
```

For collapsible/dropdown navigation, use the **disclosure pattern** (`<button>` + `aria-expanded`), not menu roles. See [Roselli, "Link + Disclosure Widget Navigation" (2019)](https://adrianroselli.com/2019/06/link-disclosure-widget-navigation.html).

### When to Use Menu Roles

Use `menu`/`menubar`/`menuitem` only when **all** of these are true:

1. You are building an **application** (not a content website)
2. Items are **actions or functions** (not links to other pages)
3. You will implement the **complete keyboard interaction model**
4. The pattern mirrors **desktop application menus**
5. You want screen readers to enter **forms/focus mode**

Examples: rich text editor toolbar, email client actions, IDE menu bar, drawing app context menu.

---

## 2. Menu Button Pattern

The menu button is the most common legitimate use of ARIA menus. A button opens a popup menu of actions. ([APG Menu Button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/))

### Required Structure

```html
<button
  aria-haspopup="menu"
  aria-expanded="false"
  aria-controls="actions-menu"
>
  Actions
</button>

<ul id="actions-menu" role="menu" aria-label="Actions" hidden>
  <li role="menuitem" tabindex="-1">Cut</li>
  <li role="menuitem" tabindex="-1">Copy</li>
  <li role="menuitem" tabindex="-1">Paste</li>
  <li role="separator"></li>
  <li role="menuitem" tabindex="-1">Delete</li>
</ul>
```

### Button Requirements

| Property | Value |
|----------|-------|
| Element | `<button>` (native, not `<div>`) |
| `aria-haspopup` | `"menu"` (never changes) |
| `aria-expanded` | `"true"` when open, `"false"` when closed |
| `aria-controls` | ID of the `menu` element (optional but recommended) |

### Button Keyboard Interaction

| Key | Action |
|-----|--------|
| Enter / Space | Opens menu, focuses first item |
| Down Arrow | (Optional) Opens menu, focuses first item |
| Up Arrow | (Optional) Opens menu, focuses last item |

### Focus Management

- **Open:** focus moves to the first menu item (or the currently checked item for persistent selections — [Pickering](https://inclusive-components.design/menus-menu-buttons/))
- **Close (Escape or activation):** focus returns to the button
- **Tab:** exits the menu and closes it

### Screen Reader Announcements

VoiceOver announces `aria-haspopup` values differently: `"menu"` produces "menu pop-up, button" while `"true"` produces "menu button, group." JAWS adds: "Press Space to activate the menu. Then navigate with arrow keys." ([Matuzovic, 2023](https://www.matuzo.at/blog/2023/aria-haspopup/))

---

## 3. Required ARIA Structure

### Menu / Menubar Skeleton

```html
<!-- Menubar (persistent, horizontal) -->
<div role="menubar" aria-label="Text Editor">
  <!-- Top-level item with submenu -->
  <div role="menuitem" aria-haspopup="menu" aria-expanded="false" tabindex="0">
    File
    <ul role="menu" aria-label="File">
      <li role="menuitem" tabindex="-1">New</li>
      <li role="menuitem" tabindex="-1">Open...</li>
      <li role="menuitem" tabindex="-1">Save</li>
      <li role="separator"></li>
      <li role="menuitem" tabindex="-1">Exit</li>
    </ul>
  </div>

  <div role="menuitem" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
    Edit
    <ul role="menu" aria-label="Edit">
      <li role="menuitem" tabindex="-1">Undo</li>
      <li role="menuitem" tabindex="-1">Redo</li>
    </ul>
  </div>
</div>
```

### Key Rules

- **Roving tabindex:** first menubar item gets `tabindex="0"`, all others get `tabindex="-1"`. Move `tabindex="0"` as focus changes. ([APG Menubar](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/))
- **Accessible name:** every `menu` and `menubar` needs `aria-label` or `aria-labelledby`. ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menu_role); [BOIA](https://www.boia.org/blog/avoiding-common-mistakes-with-arias-menu-role))
- **Valid children only:** `menu`/`menubar` may only contain `menuitem`, `menuitemcheckbox`, `menuitemradio`, `group`, or `separator`. ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menu_role))
- **Disabled items:** use `aria-disabled="true"` — items remain focusable but cannot be activated. ([APG Menubar](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/))
- **Submenu items:** add `aria-haspopup="menu"` and `aria-expanded` to any menuitem that opens a submenu.
- **Avoid dual-purpose items:** a menuitem should not both execute a function AND open a submenu. ([APG Menubar](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/))
- **Dialog items:** append ellipsis ("...") to items that open dialogs.

### Required States and Properties

| Property | Where | Value |
|----------|-------|-------|
| `aria-haspopup` | Menuitem with submenu | `"menu"` |
| `aria-expanded` | Menuitem with submenu | `"true"` / `"false"` |
| `aria-checked` | `menuitemcheckbox` / `menuitemradio` | `"true"` / `"false"` (+ `"mixed"` for checkbox) |
| `aria-disabled` | Disabled items | `"true"` |
| `aria-label` / `aria-labelledby` | `menu` / `menubar` | Accessible name |
| `tabindex` | First menubar item: `0`; all others: `-1` | Roving tabindex |

---

## 4. Menuitemcheckbox and Menuitemradio

### menuitemcheckbox

A checkable menu item with three possible states. ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemcheckbox_role))

```html
<ul role="menu" aria-label="View options">
  <li role="menuitemcheckbox" aria-checked="true" tabindex="-1">Show toolbar</li>
  <li role="menuitemcheckbox" aria-checked="false" tabindex="-1">Show status bar</li>
  <li role="menuitemcheckbox" aria-checked="mixed" tabindex="-1">Show rulers</li>
</ul>
```

- `aria-checked`: `"true"`, `"false"`, or `"mixed"` (indeterminate)
- **Enter** toggles checked state and **closes** the menu
- **Space** toggles checked state and **keeps the menu open** (allows toggling multiple items)
- All descendants are presentational — semantic elements inside lose their semantics

### menuitemradio

A mutually exclusive option within a group. ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemradio_role))

```html
<ul role="menu" aria-label="Text size">
  <li role="group" aria-label="Font size">
    <li role="menuitemradio" aria-checked="false" tabindex="-1">Small</li>
    <li role="menuitemradio" aria-checked="true" tabindex="-1">Medium</li>
    <li role="menuitemradio" aria-checked="false" tabindex="-1">Large</li>
  </li>
</ul>
```

- `aria-checked`: `"true"` or `"false"` only (no `"mixed"`)
- When activated, set own `aria-checked="true"` and all siblings' to `"false"`
- Groups: use `group` role or `separator` to define separate radio groups within the same menu
- Cannot contain interactive content or elements with `tabindex`

### Visual Indicators (CSS)

Use CSS pseudo-elements — avoids adding DOM content that screen readers would announce redundantly. ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemcheckbox_role))

```css
[role="menuitemcheckbox"][aria-checked="true"]::before { content: "\2713"; }
[role="menuitemradio"][aria-checked="true"]::before {
  background-color: currentColor;
  border-radius: 50%;
}
```

---

## 5. Keyboard Interaction Summary

Full keyboard model is in `${CLAUDE_SKILL_DIR}/references/keyboard-interaction.md`.

| Key | In Menubar | In Menu (Popup/Submenu) |
|-----|-----------|------------------------|
| Enter | Opens submenu (first item) | Activates item, closes menu |
| Space | Opens submenu (first item) | Checkbox/radio: toggles (menu stays open). Other: activates, closes |
| Down Arrow | Opens submenu (first item) | Next item |
| Up Arrow | (Optional) Opens submenu (last item) | Previous item |
| Right Arrow | Next menubar item | Opens submenu / moves right in menubar |
| Left Arrow | Previous menubar item | Closes submenu / moves left in menubar |
| Escape | — | Closes menu, returns focus to invoker |
| Home / End | First / last menubar item | First / last item in current menu |

**Critical:** if you add `role="menu"`, you must implement **all** of these. Partial implementation is worse than none — users hear "menu," try the expected keys, and nothing works. ([Roselli, 2017](https://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html); [BOIA](https://www.boia.org/blog/avoiding-common-mistakes-with-arias-menu-role))

---

## 6. Common Mistakes

Detailed examples in `${CLAUDE_SKILL_DIR}/references/common-mistakes.md`.

### 1. Using `role="menu"` for site navigation

The most widespread mistake. Triggers forms/focus mode, breaks Tab navigation, requires unimplemented keyboard handling. ([Roselli, 2017](https://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html); [Make Things Accessible](https://www.makethingsaccessible.com/guides/site-navigation-is-not-an-aria-menu/))

### 2. Incomplete ARIA role application

Adding `role="menu"` to `<ul>` without `role="presentation"` on `<li>` and `role="menuitem"` on children. Creates orphaned elements, violates SC 1.3.1. ([Make Things Accessible](https://www.makethingsaccessible.com/guides/site-navigation-is-not-an-aria-menu/))

### 3. Making links into menuitems

`role="menuitem"` on `<a>` strips link semantics. Screen readers no longer announce links; items vanish from link lists. If items are navigation destinations, they must be links, not menuitems. ([Pickering](https://inclusive-components.design/menus-menu-buttons/); [Roselli, 2017](https://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html))

### 4. Missing accessible name on menu

A `menu` requires `aria-label` or `aria-labelledby`. Without it, screen reader users cannot identify the menu's purpose. ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menu_role); [BOIA](https://www.boia.org/blog/avoiding-common-mistakes-with-arias-menu-role))

### 5. Missing keyboard interaction

Adding ARIA menu roles without implementing arrow keys, Home, End, Escape, character navigation. The roles promise behavior that is absent. Roselli: incorrect ARIA nesting "can wreak havoc and make your site navigation completely unusable." ([Roselli, 2017](https://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html))

### 6. Using the HTML `<menu>` element

The HTML `<menu>` element is deprecated and maps to `<ul>` semantics. The `<menuitem>` HTML element is also deprecated. No modern browser supports them reliably. These are unrelated to ARIA menu roles. Roselli: "Do not use them." ([Roselli, 2023](https://adrianroselli.com/2023/05/be-careful-using-menu.html))

---

## 7. Cross-References

- **`aria-decision-framework`** — use the decision tree before reaching for any ARIA role. Menu roles are Step 3 cases — only when no native HTML equivalent exists.
- **`a11y-combobox`** — if users are selecting a value (not executing an action), use `combobox` or `listbox`, not `menu`.
- **`a11y-dialog`** — menuitems that open dialogs should append "..." to their label.

For detailed reference material:
- `${CLAUDE_SKILL_DIR}/references/menu-vs-navigation.md` — full decision criteria
- `${CLAUDE_SKILL_DIR}/references/keyboard-interaction.md` — complete keyboard spec
- `${CLAUDE_SKILL_DIR}/references/menu-button-pattern.md` — menu button implementation details
- `${CLAUDE_SKILL_DIR}/references/common-mistakes.md` — anti-patterns with code examples
- `${CLAUDE_SKILL_DIR}/references/sources.yaml` — provenance for all cited sources
