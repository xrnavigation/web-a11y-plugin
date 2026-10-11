# Menu mistakes

## Incomplete navigation menu

```html
<!-- Wrong: menu items without the promised composite behavior. -->
<ul role="menu"><li><a href="/help">Help</a></li></ul>
<!-- Default for ordinary site links. -->
<nav aria-label="Main"><ul><li><a href="/help">Help</a></li></ul></nav>
```

Do not call every navigation menu a WCAG failure. If implementing the full menu
interaction is appropriate, links can legitimately carry `role="menuitem"`;
APG includes a navigation menu-button example
([APG navigation menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/examples/menu-button-links/)).

## Invalid nested list items

```html
<!-- Wrong HTML. -->
<li role="group"><li role="menuitemradio">Small</li></li>
<!-- Right group inside a list item of the containing menu. -->
<li role="none">
  <ul role="group" aria-label="Font size">
    <li role="menuitemradio" aria-checked="true" tabindex="-1">Small</li>
    <li role="menuitemradio" aria-checked="false" tabindex="-1">Large</li>
  </ul>
</li>
```

Use valid list structure and implement exclusive checked state
([HTML lists](https://html.spec.whatwg.org/multipage/grouping-content.html#the-li-element),
[APG menubar](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/)).

## HTML menu treated as an automatic popup

Wrong: expect `<menu>` to supply application-style popup behavior, or call it
deprecated. Right: recognize it as a valid list of commands and implement an
ARIA menu's keyboard and focus behavior when that widget is intended
([HTML menu](https://html.spec.whatwg.org/multipage/grouping-content.html#the-menu-element)).

## Focus remains on the opener while item handlers expect DOM focus

Wrong: open a DOM-focus menu without moving focus inside.
Right: focus the first menu item, navigate according to the chosen focus model,
and return focus on Escape. Implement disabled activation prevention rather
than relying on `aria-disabled`
([APG menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/),
[APG menubar](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/)).
