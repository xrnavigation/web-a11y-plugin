# Tab keyboard interaction

This is an APG implementation summary, not a normative WCAG checklist
([APG tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)).

| Key | Behavior |
|---|---|
| Tab / Shift+Tab | Enter or leave the tablist using its single roving tab stop |
| Left / Right | Previous/next horizontal tab, wrapping |
| Up / Down | Previous/next vertical tab, wrapping |
| Enter / Space | Activate focused tab in manual mode |
| Home / End | Optional first/last tab |
| Delete | Optional removal with focus to next, or previous if last |
| Shift+F10 | Open associated context menu if offered |

Horizontal tabs do not capture Up/Down, preserving page scrolling. Set
`aria-orientation="vertical"` for vertical tabs. If all tabs can be removed,
move focus to a useful workflow target after removing the last one
([APG tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)).

## Keep focus separate from activation

```js
// Helpers, not a full widget: caller supplies keyboard/click handlers.
function focusTab(tabs, target) {
  tabs.forEach(tab => { tab.tabIndex = tab === target ? 0 : -1; });
  target.focus();
}
function activateTab(tabs, target) {
  tabs.forEach(tab => {
    const selected = tab === target;
    tab.setAttribute('aria-selected', String(selected));
    const panel = document.getElementById(tab.getAttribute('aria-controls'));
    if (panel) panel.hidden = !selected;
  });
}
```

In manual mode, arrows call `focusTab` without changing selection. Enter/Space
calls `activateTab`. Pointer activation calls both helpers so selection and the
entry Tab stop remain useful. In automatic mode, movement calls both. Use
automatic activation only when panels display without noticeable latency
([APG tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)).

Keep the active panel reachable via Tab. Add `tabindex="0"` if its first useful
content is not otherwise focusable. Test focus and selection independently,
including a manually focused unselected tab and backward re-entry.
