# Common Menu Accessibility Mistakes
## Contents

- [1. Using role="menu" for Site Navigation](#1-using-rolemenu-for-site-navigation)
- [2. Incomplete ARIA Role Application](#2-incomplete-aria-role-application)
- [3. Making Links into Menuitems](#3-making-links-into-menuitems)
- [4. Missing Accessible Name on Menu](#4-missing-accessible-name-on-menu)
- [5. Missing Keyboard Interaction](#5-missing-keyboard-interaction)
- [6. Using the HTML menu Element](#6-using-the-html-menu-element)
- [7. Dual-Purpose Menu Items](#7-dual-purpose-menu-items)
- [8. Top-Level Nav Links Made Non-Functional](#8-top-level-nav-links-made-non-functional)


---

## 1. Using `role="menu"` for Site Navigation

The most widespread mistake in menu accessibility. Navigation should use `<nav>` + `<ul>` + `<li>` + `<a>`.

```html
<!-- WRONG -->
<nav>
  <ul role="menu">
    <li role="menuitem"><a href="/about">About</a></li>
    <li role="menuitem"><a href="/news">News</a></li>
    <li role="menuitem"><a href="/contact">Contact</a></li>
  </ul>
</nav>

<!-- RIGHT -->
<nav aria-label="Main">
  <ul>
    <li><a href="/about">About</a></li>
    <li><a href="/news">News</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>
```

**Why it's wrong:**
- Triggers forms/focus mode in JAWS and NVDA, breaking normal page reading
- Requires JavaScript keyboard handling that is rarely implemented
- Breaks Tab navigation expectations
- Navigation disappears from landmarks list

Sources: [Roselli, 2017](https://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html); [Make Things Accessible](https://www.makethingsaccessible.com/guides/site-navigation-is-not-an-aria-menu/); [BOIA](https://www.boia.org/blog/avoiding-common-mistakes-with-arias-menu-role); [Pickering](https://inclusive-components.design/menus-menu-buttons/); [MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menu_role)

---

## 2. Incomplete ARIA Role Application

Adding `role="menu"` to a `<ul>` without fixing the entire subtree.

```html
<!-- WRONG — orphaned list items, violates SC 1.3.1 -->
<ul role="menu">
  <li><a href="/cut">Cut</a></li>
  <li><a href="/copy">Copy</a></li>
</ul>

<!-- STILL WRONG — links should not be menuitems if they navigate -->
<ul role="menu">
  <li role="presentation"><a role="menuitem" href="/cut">Cut</a></li>
</ul>

<!-- RIGHT — menuitems are actions, not links -->
<ul role="menu" aria-label="Edit actions">
  <li role="menuitem" tabindex="-1">Cut</li>
  <li role="menuitem" tabindex="-1">Copy</li>
  <li role="menuitem" tabindex="-1">Paste</li>
</ul>
```

**Why it's wrong:** A `role="menu"` "neuters" the native list semantics of `<ul>`, but without `role="presentation"` on `<li>` and `role="menuitem"` on interactive children, nothing valid replaces the lost semantics.

Source: [Make Things Accessible](https://www.makethingsaccessible.com/guides/site-navigation-is-not-an-aria-menu/)

---

## 3. Making Links into Menuitems

```html
<!-- WRONG — strips link semantics -->
<ul role="menu">
  <li role="presentation">
    <a role="menuitem" href="/settings">Settings</a>
  </li>
</ul>

<!-- RIGHT (if items are navigation) — don't use menu roles at all -->
<nav aria-label="Settings">
  <ul>
    <li><a href="/settings">Settings</a></li>
  </ul>
</nav>

<!-- RIGHT (if items are actions) — use non-link elements -->
<ul role="menu" aria-label="Actions">
  <li role="menuitem" tabindex="-1">Settings</li>
</ul>
```

**Why it's wrong:** `role="menuitem"` on `<a>` overrides the link role. Screen readers no longer announce items as links. Users cannot find them in link lists (Insert+F7 in JAWS, NVDA+F7 in NVDA). If the items are navigation destinations, they should be links, not menuitems.

Sources: [Pickering](https://inclusive-components.design/menus-menu-buttons/); [Roselli, 2017](https://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html)

---

## 4. Missing Accessible Name on Menu

```html
<!-- WRONG — screen reader cannot identify the menu -->
<ul role="menu">
  <li role="menuitem" tabindex="-1">Cut</li>
  <li role="menuitem" tabindex="-1">Copy</li>
</ul>

<!-- RIGHT — menu has an accessible name -->
<ul role="menu" aria-label="Edit actions">
  <li role="menuitem" tabindex="-1">Cut</li>
  <li role="menuitem" tabindex="-1">Copy</li>
</ul>

<!-- ALSO RIGHT — name from associated button -->
<button id="edit-btn" aria-haspopup="menu" aria-expanded="false">Edit</button>
<ul role="menu" aria-labelledby="edit-btn">
  <li role="menuitem" tabindex="-1">Cut</li>
  <li role="menuitem" tabindex="-1">Copy</li>
</ul>
```

Sources: [BOIA](https://www.boia.org/blog/avoiding-common-mistakes-with-arias-menu-role); [MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menu_role)

---

## 5. Missing Keyboard Interaction

Adding ARIA menu roles without implementing the required keyboard model.

```js
// WRONG — menu roles present but no keyboard handling
document.querySelector('[role="menu"]').innerHTML = `
  <li role="menuitem">Cut</li>
  <li role="menuitem">Copy</li>
`;
// Users hear "menu" but arrow keys, Home, End, Escape do nothing.

// RIGHT — full keyboard support
menuElement.addEventListener('keydown', (e) => {
  switch (e.key) {
    case 'ArrowDown': focusNextItem(); e.preventDefault(); break;
    case 'ArrowUp': focusPreviousItem(); e.preventDefault(); break;
    case 'Home': focusFirstItem(); e.preventDefault(); break;
    case 'End': focusLastItem(); e.preventDefault(); break;
    case 'Escape': closeMenu(); returnFocusToButton(); e.preventDefault(); break;
    case 'Enter': activateItem(e.target); closeMenu(); break;
    case ' ': activateItem(e.target); e.preventDefault(); break;
  }
});
```

> "Incorrect ARIA nesting can wreak havoc and make your site navigation completely unusable."
> — [Roselli, 2017](https://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html)

Sources: [Roselli, 2017](https://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html); [BOIA](https://www.boia.org/blog/avoiding-common-mistakes-with-arias-menu-role)

---

## 6. Using the HTML `<menu>` Element

```html
<!-- WRONG — deprecated HTML element, not the same as ARIA menu -->
<menu>
  <menuitem label="Cut" onclick="cut()">
</menu>

<!-- RIGHT — ARIA menu roles on standard elements -->
<ul role="menu" aria-label="Edit">
  <li role="menuitem" tabindex="-1">Cut</li>
</ul>
```

The HTML `<menu>` element is deprecated and maps to `<ul>` semantics. The HTML `<menuitem>` element is also deprecated. No modern browser provides reliable support. These are entirely distinct from ARIA menu roles.

> "Do not use them."
> — [Roselli, 2023](https://adrianroselli.com/2023/05/be-careful-using-menu.html)

---

## 7. Dual-Purpose Menu Items

```html
<!-- WRONG — item both navigates AND opens a submenu -->
<li role="menuitem" aria-haspopup="menu">
  <a href="/settings">Settings</a>
  <ul role="menu">
    <li role="menuitem">General</li>
    <li role="menuitem">Advanced</li>
  </ul>
</li>

<!-- RIGHT — separate the trigger from the submenu -->
<li role="menuitem" aria-haspopup="menu" aria-expanded="false">
  Settings
  <ul role="menu" aria-label="Settings">
    <li role="menuitem" tabindex="-1">General</li>
    <li role="menuitem" tabindex="-1">Advanced</li>
  </ul>
</li>
```

A single menuitem should not both execute a function and open a submenu. Users cannot predict what will happen on activation.

Source: [APG Menubar Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/)

---

## 8. Top-Level Nav Links Made Non-Functional

Some implementations prevent top-level navigation links from working, making them only open submenus. This removes primary navigation access for users who don't discover the submenu.

```html
<!-- WRONG — top-level link prevented from navigating -->
<a href="/products" onclick="event.preventDefault(); toggleSubmenu()">Products</a>

<!-- RIGHT (disclosure pattern) — button toggles, link works -->
<li>
  <a href="/products">Products</a>
  <button aria-expanded="false" aria-label="Products submenu">▾</button>
  <ul hidden>
    <li><a href="/products/widgets">Widgets</a></li>
    <li><a href="/products/gadgets">Gadgets</a></li>
  </ul>
</li>
```

Source: [Pickering](https://inclusive-components.design/menus-menu-buttons/)
