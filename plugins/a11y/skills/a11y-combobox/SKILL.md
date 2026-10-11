---
name: a11y-combobox
description: Guides accessible combobox and autocomplete implementation. Use when building editable suggestions, typeahead, select-only comboboxes, or custom popup selection controls.
---

# Accessible comboboxes

Use native selection controls when they meet the task. Choose a custom combobox
for the interaction needed, rather than an arbitrary option-count threshold.
A combobox is single-select; multi-selection needs a different pattern
([APG combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)).

## Choose the interaction

- Use a native `<select>` for fixed single choices; evaluate `<select multiple>`
  or a checkbox group for multiple choices. Native controls remain valid options;
  a historical usability study does not establish a universal ban
  ([HTML select](https://html.spec.whatwg.org/multipage/form-elements.html#the-select-element)).
- For an editable field with suggestions, choose `aria-autocomplete="none"`,
  `"list"` or `"both"` to match actual behavior. A select-only combobox does not
  filter by typing into an editable field
  ([APG combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)).

## Build semantics and behavior together

The following is an initial markup scaffold, not a complete widget:

```html
<label for="fruit">Fruit</label>
<input id="fruit" role="combobox" aria-expanded="false"
       aria-controls="fruit-options" aria-autocomplete="list">
<ul id="fruit-options" role="listbox" aria-label="Fruit suggestions" hidden>
  <li id="fruit-apple" role="option" aria-selected="false">Apple</li>
  <li id="fruit-pear" role="option" aria-selected="false">Pear</li>
</ul>
```

Maintain `aria-expanded` with visibility. Set `aria-controls` while the popup is
visible; retaining it while a hidden popup exists is valid. Name the combobox.
For a non-listbox popup, set `aria-haspopup` to its actual role (`grid`, `tree`
or `dialog`). Set `aria-activedescendant` to an existing active item for
listbox/grid/tree popups while DOM focus stays on the combobox; remove it when
there is no active item. Dialog popups move DOM focus into the dialog
([APG combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)).

Implement the chosen variant's arrows, acceptance and dismissal. Preserve
native text editing in editable variants; do not intercept cursor movement as
list navigation. Distinguish the active suggestion from the committed input
value, and implement the chosen manual/automatic selection model
([APG combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)).

## Verify

Test open, filter, navigate, accept, dismiss, clear and refocus on the project's
supported combinations. Inspect actual option names and selection state. Do not
prescribe universal screen reader output or add live messages to every movement;
first establish the missing information and check for duplicate speech.

Read [keyboard interaction](references/keyboard-interaction.md),
[verification guidance](references/screen-reader-behavior.md),
[common mistakes](references/common-mistakes.md) and
[source provenance](references/sources.yaml).
