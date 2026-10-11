# Listbox mistakes

## Controls nested inside an option

```html
<!-- Wrong: an independently interactive button inside an option. -->
<li role="option">Article A <button>Move up</button></li>
<!-- Right structural separation; implement the move action separately. -->
<ul role="listbox" tabindex="0" aria-label="Reading queue" aria-activedescendant="article-a">
  <li role="option" id="article-a" aria-selected="true">Article A</li>
</ul>
<button type="button">Move selected item up</button>
```

Listbox interaction does not provide access to buttons or links inside options.
Use external move controls, or another pattern such as a grid when each row
needs independent interactive controls
([APG listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/),
[APG rearrangeable listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/examples/listbox-rearrangeable/)).

## Selection erased by arrow navigation

Wrong for the recommended multi-select model: clear every selected option when
arrows move focus. Right: update focus independently and toggle the active
option with Space. Another supported model uses modifiers; document and implement
one complete model ([APG listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).

## Every option in sequential Tab order

Wrong: give every option `tabindex="0"`.
Right: use roving tabindex or focus the container with `aria-activedescendant`.
The container does not always need a tabindex in the roving-option model
([APG listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).

## Keyboard-only drag alternative

Wrong: offer Alt+Up but no click/tap method.
Right: offer external move buttons tied to the same action, preserve the active
item, and prevent moves beyond boundaries. A single-pointer alternative is
required for non-exempt dragging functionality
([Understanding 2.5.7](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)).
