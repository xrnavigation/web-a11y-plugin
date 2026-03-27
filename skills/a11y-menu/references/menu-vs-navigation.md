# Menu vs Navigation: Decision Criteria

## The Core Distinction

ARIA `menu`, `menubar`, and `menuitem` roles are for **application-type menus** — the kind found in desktop software (Photoshop, Word, Google Docs). They are **not** for website navigation.

> "A properly-coded web page navigation menu needs no ARIA. Once you add ARIA, however, you have put yourself on the hook to handle some complex interactions."
> — [Adrian Roselli, 2017](https://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html)

---

## Why `role="menu"` Breaks Site Navigation

### 1. Screen Reader Mode Switching

When focus enters `role="menu"`:

| Screen Reader | Behavior |
|---------------|----------|
| JAWS | Enters **forms mode**. Arrow keys navigate menu items instead of reading content. Virtual cursor suspended. Announces: "Press Space to activate the menu. Then navigate with arrow keys." |
| NVDA | Enters **focus mode** automatically. Arrow keys passed to widget, not used for browse navigation. |
| VoiceOver (macOS) | No mode switch, but announces "menu" and expects menu keyboard conventions. |

Sources: [Tink.uk](https://tink.uk/understanding-screen-reader-interaction-modes/); [Accessible Culture](https://accessibleculture.org/articles/2012/09/aria-widgets-and-focus-forms-mode-support/)

### 2. Keyboard Behavior Expectations Change

Adding `role="menu"` commits you to implementing: Enter, Space, Down Arrow, Up Arrow, Right Arrow, Left Arrow, Home, End, Escape, and character-key navigation. Most site navigations implement none of these.

> "A user who might want to use one of these keys for its traditional purpose on the web page will instead trigger the function in your menus. Imagine how confusing it might be to hit Space to scroll the page and have a new nested menu open instead."
> — [Roselli, 2017](https://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html)

### 3. Navigation Disappears from Landmarks and Link Lists

- `<nav>` landmark is replaced by a menu widget — disappears from landmarks list
- Links given `role="menuitem"` vanish from the screen reader links list (Insert+F7 in JAWS, NVDA+F7 in NVDA)
- Users lose two primary means of discovering site structure

Source: [Roselli, 2017](https://adrianroselli.com/2017/10/dont-use-aria-menu-roles-for-site-nav.html)

### 4. Broken Parent-Child Relationships

When `<ul role="menu">` is applied without changing `<li>` to `role="presentation"` and `<a>` to `role="menuitem"`, list semantics are "neutered by ARIA" but nothing valid replaces them. This violates WCAG SC 1.3.1 Info and Relationships (Level A).

Source: [Make Things Accessible](https://www.makethingsaccessible.com/guides/site-navigation-is-not-an-aria-menu/)

### 5. ARIA Menus Can Only Contain Menu Parts

A `menu` may only own `menuitem`, `menuitemcheckbox`, `menuitemradio`, `group`, or `separator`. Links (`<a>`) are not valid children unless given `role="menuitem"`, which strips their link semantics.

Source: [MDN, "ARIA: menu role"](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menu_role)

---

## Decision Flowchart

```
Are the items links to pages/sections?
  YES -> <nav> + <ul> + <a>. Never role="menu".
  NO  -> Are the items actions/commands in an application?
           YES -> Do you commit to full keyboard model?
                    YES -> role="menu" + role="menuitem"
                    NO  -> Don't use menu roles. Use buttons.
           NO  -> Are items form selections?
                    YES -> listbox or combobox
                    NO  -> Use buttons or other appropriate pattern.
```

---

## Use `menu`/`menubar`/`menuitem` When ALL Are True

1. You are building an **application** (not a content website)
2. The menu offers **actions or functions** (not navigation to other pages)
3. You will implement the **complete keyboard interaction model**
4. The pattern mirrors **desktop application menus** (File, Edit, View)
5. You want screen readers to enter **forms/focus mode**

Examples: rich text editor toolbar, email client actions menu, IDE menu bar, context menu in a drawing application.

## Use `<nav>` + Links When ANY Are True

1. Items are **links to other pages or page sections**
2. Users expect to **Tab between items**
3. The list represents **site structure or information architecture**
4. You want items to appear in screen reader **link lists**

Examples: site header navigation, sidebar navigation, breadcrumbs, footer links.

## Use Disclosure Pattern (`button` + `aria-expanded`) When

1. You have **navigation links** organized into **collapsible groups**
2. You need a "hamburger" menu or responsive navigation toggle
3. Sub-navigation sections expand/collapse but items are still links

This is Roselli's ["Link + Disclosure Widget Navigation" pattern (2019)](https://adrianroselli.com/2019/06/link-disclosure-widget-navigation.html).

## Use `listbox` / `combobox` When

1. Users are **selecting a value** (not executing an action)
2. The control is part of a **form**
3. The selected value **persists in a form field**

---

## The HTML `<menu>` Element (Unrelated, Deprecated)

The HTML `<menu>` element is deprecated and maps to `<ul>` semantics. The `<menuitem>` HTML element is also deprecated. No modern browser provides reliable support. These are distinct from ARIA menu roles.

> "Do not use them."
> — [Roselli, 2023](https://adrianroselli.com/2023/05/be-careful-using-menu.html)

---

## Expert Consensus

> "ARIA menus are not designated for navigation but for application behavior."
> — [Heydon Pickering, Inclusive Components](https://inclusive-components.design/menus-menu-buttons/)

> ARIA's second rule: "Do not change native semantics, unless you really have to."
> — [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)

Website navigation already communicates structure via semantic HTML. Adding ARIA menu roles replaces working semantics with broken promises.
