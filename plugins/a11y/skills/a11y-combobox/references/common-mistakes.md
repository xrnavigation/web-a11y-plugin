# Combobox mistakes

## Relationship omitted while open

```html
<!-- Wrong: expanded popup has no controls relationship. -->
<input role="combobox" aria-expanded="true" aria-label="Fruit">
<!-- Right relationship; implement popup behavior separately. -->
<input role="combobox" aria-expanded="true" aria-controls="fruits" aria-label="Fruit">
<ul id="fruits" role="listbox" aria-label="Fruit suggestions">
  <li id="apple" role="option" aria-selected="false">Apple</li>
</ul>
```

`aria-controls` is needed while the popup is visible, and can remain while an
existing popup is hidden. Do not require a persistent hidden popup merely to
keep this attribute ([APG combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)).

## Moving DOM focus into an editable listbox popup

Wrong: focus each suggestion and then expect typing to remain in the input.
Right: keep DOM focus on the input and update `aria-activedescendant` to the
active suggestion's ID. A dialog popup uses actual DOM focus instead
([APG combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)).

## Duplicating every option announcement

Wrong: announce every arrow movement in a live region unconditionally.
Right: verify the exposed active item and actual output first. Add a targeted
status only for information the supported implementation otherwise fails to
communicate; check duplicate speech and interruption. Do not treat old AT bug
reports as universal behavior.

## Banning groups or native choices

Wrong: flatten all groups or ban `<select multiple>` based on a historical test.
Right: use the appropriate native control or named option groups, then verify the
chosen interaction. APG permits listbox groups; HTML defines multiple selection
([APG listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/),
[HTML select](https://html.spec.whatwg.org/multipage/form-elements.html#the-select-element)).
