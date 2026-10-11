---
name: a11y-listbox
description: Guides accessible single and multiple selection listboxes. Use when building custom selection lists, option grouping, or reorderable listboxes with external move controls.
---

# Accessible listboxes

Use a listbox to select options, not to contain independently interactive
buttons or links. Prefer native controls when they meet the task; a custom
listbox owns focus, keyboard handling and state updates
([APG listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).

## Pick one focus model

Use roving tabindex on options **or** DOM focus on the listbox with
`aria-activedescendant`. Do not put every option in the Tab sequence. Name the
listbox; mark multi-selection with `aria-multiselectable="true"`. Use
`aria-selected` or `aria-checked` consistently for selectable options, not both
without a distinct documented meaning
([APG listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).

```html
<!-- Initial state; JavaScript must update active descendant and selection. -->
<p id="choices-label">Favorite color</p>
<ul role="listbox" tabindex="0" aria-labelledby="choices-label"
    aria-activedescendant="choice-red">
  <li role="option" id="choice-red" aria-selected="true">Red</li>
  <li role="option" id="choice-blue" aria-selected="false">Blue</li>
</ul>
```

Arrows move focus; single-selection may follow focus. In the recommended
multi-selection model, arrows do not clear selection and Space toggles the
active option. Implement Home/End and type-ahead where useful. Groups can use
`role="group"` with a name; do not flatten valid groups solely from historical
AT bug reports ([APG listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).

## Reorder with external controls

```html
<p id="queue-label">Reading queue</p>
<ul id="queue" role="listbox" tabindex="0" aria-labelledby="queue-label"
    aria-activedescendant="queue-a">
  <li id="queue-a" role="option" aria-selected="true">Article A</li>
  <li id="queue-b" role="option" aria-selected="false">Article B</li>
</ul>
<div aria-label="Queue actions" role="group">
  <button type="button" id="move-up" disabled>Move selected item up</button>
  <button type="button" id="move-down">Move selected item down</button>
</div>
<p role="status" id="queue-status"></p>
```

Keep move controls outside options. Implement them with the same reorder action
as dragging; keep the selected item and its stable ID, update order and boundary
states, preserve useful focus, and report the resulting position. APG's
rearrangeable example follows this separation
([APG rearrangeable listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/examples/listbox-rearrangeable/)).

For dragging, a keyboard shortcut alone does not meet the single-pointer
alternative requirement. Click/tap move buttons provide an alternative; the
criterion has essential and user-agent-controlled exceptions
([Understanding 2.5.7](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)).

Read [keyboard interaction](references/keyboard-interaction.md),
[verification](references/screen-reader-behavior.md),
[common mistakes](references/common-mistakes.md) and
[sources](references/sources.yaml).
