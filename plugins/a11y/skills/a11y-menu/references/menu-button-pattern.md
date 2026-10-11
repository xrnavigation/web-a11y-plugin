# Menu-button implementation decisions

Use a native button to open a named menu. Set `aria-haspopup="menu"` (or `true`)
and synchronize `aria-expanded` with visibility. `aria-controls` is optional in
this pattern ([APG menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/)).

```html
<button type="button" id="text-menu-button" aria-haspopup="menu"
        aria-expanded="false" aria-controls="text-menu">Text size</button>
<ul id="text-menu" role="menu" aria-labelledby="text-menu-button" hidden>
  <li role="none"><ul role="group" aria-label="Font size">
    <li role="menuitemradio" tabindex="-1" aria-checked="true">Small</li>
    <li role="menuitemradio" tabindex="-1" aria-checked="false">Large</li>
  </ul></li>
</ul>
```

This is a structural scaffold. Keep HTML lists valid; a `<li>` cannot directly
contain another `<li>` as the intended list hierarchy
([HTML li](https://html.spec.whatwg.org/multipage/grouping-content.html#the-li-element)).

## Behavior to implement

Enter/Space opens and focuses the first item; optional Down/Up can open at the
first/last item. Inside, implement arrows, activation, Escape, Tab exit, optional
type-ahead, and submenus if present. Radio activation checks one item in its
group; checkbox activation updates its state. Disabled items remain focusable
in the APG model but must not activate
([APG menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/),
[APG menubar](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/)).

Use roving DOM focus or container focus with `aria-activedescendant` consistently.
Escape returns to the button; activation may follow a destination or change
focus according to the action. Handle outside dismissal without blindly forcing
focus back if the user has intentionally moved to another control.

## Verification

Check button naming, open/closed state, item focus, checked state, disabled
activation, Escape, Tab, pointer actions and nested submenus. Record observed
behavior and environment. `aria-haspopup="menu"` and `true` communicate the
same popup type; do not promise identical spoken strings
([WAI-ARIA aria-haspopup](https://www.w3.org/TR/wai-aria-1.2/#aria-haspopup)).
