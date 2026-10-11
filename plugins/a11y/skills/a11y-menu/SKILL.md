---
name: a11y-menu
description: Guides accessible menu buttons, action menus, menubars, and context menus. Use when implementing menu roles and composite keyboard behavior or choosing ordinary navigation links instead.
---

# Accessible menus

Default ordinary website navigation to `<nav>` with links and disclosure
buttons. Menu roles introduce a composite keyboard contract; choose them only
when implementing that interaction. Links can be menu items in a properly built
navigation menu button; menu roles are not inherently a WCAG failure
([APG navigation menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/examples/menu-button-links/)).

## Menu button scaffold

```html
<button id="actions" type="button" aria-haspopup="menu"
        aria-expanded="false" aria-controls="actions-popup">Actions</button>
<ul id="actions-popup" role="menu" aria-labelledby="actions" hidden>
  <li role="none"><button type="button" role="menuitem" tabindex="-1">Copy</button></li>
  <li role="none"><button type="button" role="menuitem" tabindex="-1">Delete</button></li>
</ul>
```

Implement opening, keyboard navigation and activation; this markup alone is not
a menu. Enter/Space on the button opens and focuses the first item. Inside the
menu, arrows navigate, Escape closes and restores focus, and Tab leaves the
menu rather than cycling through all items. Synchronize visibility and
`aria-expanded`; `aria-controls` is optional in the menu-button pattern
([APG menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/),
[APG menubar](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/)).

## Groups and submenu ownership

Use valid HTML as well as valid ARIA. Do not nest `<li>` directly inside `<li>`.
A radio group can be an inner list within a presentation list item:

```html
<ul role="menu" aria-label="Text settings">
  <li role="none">
    <ul role="group" aria-label="Font size">
      <li role="menuitemradio" aria-checked="true" tabindex="-1">Small</li>
      <li role="menuitemradio" aria-checked="false" tabindex="-1">Large</li>
    </ul>
  </li>
</ul>
```

Implement exclusive radio state and activation. A checkbox menu item uses
`aria-checked`; disabled items stay focusable in the APG model, but your code
must prevent activation. Submenu triggers expose `aria-haspopup="menu"` and
`aria-expanded`, and the submenu owns its items
([APG menubar](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/)).

HTML `<menu>` remains a valid list of commands; it does not implement an ARIA
popup menu's focus/keyboard behavior
([HTML menu](https://html.spec.whatwg.org/multipage/grouping-content.html#the-menu-element)).

## Verify

Exercise button entry, item movement, activation, disabled items, submenu
entry/exit, Escape and Tab. Observe actual names, checked/expanded states and
focus restoration on target combinations. Do not use role names as a reason to
force a particular screen reader mode or promise a fixed announcement.

Read [menu vs navigation](references/menu-vs-navigation.md),
[menu button details](references/menu-button-pattern.md),
[keyboard interaction](references/keyboard-interaction.md),
[common mistakes](references/common-mistakes.md) and
[sources](references/sources.yaml).
