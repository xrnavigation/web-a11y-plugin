# Listbox Common Mistakes — Expanded Reference
## Contents

- [1. Using ARIA listbox when native select suffices](#1-using-aria-listbox-when-native-select-suffices)
- [2. Missing aria-selected on options](#2-missing-aria-selected-on-options)
- [3. No focus management](#3-no-focus-management)
  - [Roving tabindex approach](#roving-tabindex-approach)
  - [aria-activedescendant approach](#aria-activedescendant-approach)
- [4. No type-ahead for long lists](#4-no-type-ahead-for-long-lists)
- [5. Mixing aria-selected and aria-checked](#5-mixing-aria-selected-and-aria-checked)
- [6. Interactive elements inside options](#6-interactive-elements-inside-options)
- [7. Missing aria-orientation on horizontal listboxes](#7-missing-aria-orientation-on-horizontal-listboxes)
- [8. Selection follows focus in multi-select](#8-selection-follows-focus-in-multi-select)
- [9. No visible focus indicator](#9-no-visible-focus-indicator)
- [10. Not scrolling focused option into view](#10-not-scrolling-focused-option-into-view)


---

## 1. Using ARIA listbox when native `<select>` suffices

Native `<select>` scored 100% success rate and 97.5% usability across all screen readers tested. Custom ARIA implementations consistently scored lower ([24a11y, "Select Your Poison Part 2"](https://www.24a11y.com/2019/select-your-poison-part-2/)). MDN explicitly recommends native `<select>`, radio buttons, or checkboxes over custom listbox implementations ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listbox_role)).

**Use ARIA listbox only when:** options contain complex content, you need a dual-listbox transfer widget, or the design requires non-text layouts that `<select>` cannot render.

---

## 2. Missing `aria-selected` on options

When `aria-multiselectable="true"` is set on the container, **every** `role="option"` must have `aria-selected="true"` or `aria-selected="false"` explicitly. Omitting `aria-selected` causes VoiceOver to refuse to read the options ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listbox_role)).

```html
<!-- WRONG -->
<ul role="listbox" aria-multiselectable="true">
  <li role="option">Unselected item</li>          <!-- no aria-selected! -->
  <li role="option" aria-selected="true">Selected</li>
</ul>

<!-- RIGHT -->
<ul role="listbox" aria-multiselectable="true">
  <li role="option" aria-selected="false">Unselected item</li>
  <li role="option" aria-selected="true">Selected</li>
</ul>
```

For single-select listboxes, set `aria-selected="true"` on the selected option and `aria-selected="false"` on all others.

---

## 3. No focus management

The listbox container must handle keyboard events and manage focus — either via roving tabindex or `aria-activedescendant`. Without this, keyboard users cannot navigate options ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listbox_role); [APG](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).

### Roving tabindex approach
```js
// Set tabindex="0" on focused option, tabindex="-1" on all others
function focusOption(option, allOptions) {
  allOptions.forEach(o => o.setAttribute('tabindex', '-1'));
  option.setAttribute('tabindex', '0');
  option.focus();
}
```

### aria-activedescendant approach
```js
// Container keeps focus; aria-activedescendant points to the "focused" option
function focusOption(listbox, optionId) {
  listbox.setAttribute('aria-activedescendant', optionId);
  // Visually highlight the option — AT reads it as focused
}
```

---

## 4. No type-ahead for long lists

Lists with 7+ options become tedious to navigate without character-match focus movement. Implement single-character and rapid-string type-ahead ([APG](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).

```js
// Collect typed characters within a timeout window (~500ms)
// Match against option text content
// Move focus to first matching option
```

---

## 5. Mixing `aria-selected` and `aria-checked`

The APG calls this "extremely rare" and strongly discourages it. Convention: use `aria-selected` for single-select, `aria-selected` for multi-select. Do not mix both in one listbox ([APG](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).

---

## 6. Interactive elements inside options

Links, buttons, or checkboxes inside `role="option"` elements are not valid. Screen readers expect options to be leaf nodes. If you need interactive children, use the Grid pattern instead ([APG](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).

---

## 7. Missing `aria-orientation` on horizontal listboxes

The implicit orientation value is `vertical` ([WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/#listbox)). Horizontal layouts must explicitly set `aria-orientation="horizontal"`. Without it:
- Screen readers may announce incorrect navigation instructions
- Arrow key mappings (left/right vs up/down) will confuse users

---

## 8. Selection follows focus in multi-select

In single-select, selection may follow focus. In multi-select, this destroys existing selections when the user arrows through options. Multi-select must decouple focus from selection — arrow keys move focus, Space toggles selection ([APG](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)).

---

## 9. No visible focus indicator

The focused option must have a visible focus ring or highlight. Without it, sighted keyboard users cannot tell which option is active ([WCAG 2.4.7](https://www.w3.org/WAI/WCAG21/Understanding/focus-visible.html)).

```css
/* Minimum viable focus style */
[role="option"]:focus,
[role="option"].focused {
  outline: 2px solid #005fcc;
  outline-offset: -2px;
}
```

---

## 10. Not scrolling focused option into view

In scrollable listboxes, programmatic scroll-into-view on focus change is required. Without it, the focused option may be off-screen while sighted users see no indication of where focus is.

```js
function focusOption(option) {
  // ... focus management ...
  option.scrollIntoView({ block: 'nearest' });
}
```
