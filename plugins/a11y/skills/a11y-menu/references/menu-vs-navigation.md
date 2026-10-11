# Menu roles and navigation

Ordinary site navigation usually works with `<nav>`, links and disclosure
buttons. An ARIA menu is a composite widget with arrows, focus management,
activation and dismissal; its role is a promise to implement those behaviors
([APG menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/),
[APG menubar](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/)).

```html
<nav aria-label="Main">
  <ul><li><a href="/help">Help</a></li></ul>
</nav>
```

This is the simpler starting point for a set of ordinary links. Do not add menu
roles merely because the design calls a link list a “menu.”

## Menus can contain navigation links

```html
<!-- Part of a fully implemented menu button, not a complete widget. -->
<ul role="menu" aria-label="Resources">
  <li role="none"><a role="menuitem" tabindex="-1" href="/help">Help</a></li>
</ul>
```

Links with `role="menuitem"` are legitimate in APG's navigation menu-button
pattern. Implement the complete composite interaction and retain destinations;
do not classify the roles alone as prohibited or as a WCAG failure
([APG navigation menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/examples/menu-button-links/)).

## HTML menu is a list

HTML `<menu>` is valid and represents a list of commands. It does not
instantiate an ARIA popup widget or supply its keyboard handlers. Do not confuse
it with the obsolete HTML `<menuitem>` element
([HTML menu](https://html.spec.whatwg.org/multipage/grouping-content.html#the-menu-element)).

Evaluate the actual interaction and accessibility tree; do not force or predict
screen reader modes solely from a role name.
