# Keyboard Interaction — Tabs

Full keyboard specification from the [APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/).

---

## Core Navigation

### Tab Key

- **Into the tablist:** Focuses the currently active tab (the one with `aria-selected="true"` and `tabindex="0"`).
- **From a tab:** Moves focus to the next focusable element outside the tablist — typically the active panel or the first focusable element within it.
- The Tab key NEVER cycles between individual tabs. That is the arrow keys' job.

Source: [APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/), [A11y Collective](https://www.a11y-collective.com/blog/accessibility-tab/)

### Arrow Keys

Direction depends on `aria-orientation`:

| Orientation | Forward | Backward |
|-------------|---------|----------|
| `horizontal` (default) | Right Arrow | Left Arrow |
| `vertical` | Down Arrow | Up Arrow |

Behavior:
- Moves focus to the next/previous tab in the tablist
- **Wraps:** from the last tab, forward goes to the first; from the first, backward goes to the last
- In **automatic activation** mode, also activates the newly focused tab
- In **manual activation** mode, only moves focus — activation requires Enter or Space
- Updates `tabindex`: the newly focused tab gets `tabindex="0"`, the previously focused tab gets `tabindex="-1"`

**Cross-axis keys are NOT captured:**
- Horizontal tabs: Up/Down Arrow pass through for normal page scrolling
- Vertical tabs: Left/Right Arrow pass through

Source: [APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)

### Space and Enter

- **Automatic activation mode:** Not needed (tab activates on focus). If implemented, should be harmless (no-op or re-activate).
- **Manual activation mode:** Activates the currently focused tab — displays its panel and sets `aria-selected="true"`.

Source: [APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)

---

## Optional Keys

These are recommended but not required. Implement them if the tab interface has many tabs.

### Home

Moves focus to the first tab in the tablist. In automatic mode, also activates it.

### End

Moves focus to the last tab in the tablist. In automatic mode, also activates it.

### Delete

Only applicable when tabs are closeable/removable:
- Closes the currently focused tab and its associated panel
- Moves focus to the next tab (or previous if the deleted tab was last)
- If the deleted tab was the active tab, activates the newly focused tab

### Shift+F10

Opens the context/popup menu associated with the tab, if one exists (indicated by `aria-haspopup` on the tab).

Source: [APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)

---

## Focus Management (Roving Tabindex)

The tab pattern uses roving tabindex, NOT `aria-activedescendant`:

```js
function focusTab(tabs, targetTab) {
  tabs.forEach(tab => {
    const isTarget = tab === targetTab;
    tab.setAttribute('tabindex', isTarget ? '0' : '-1');
    tab.setAttribute('aria-selected', isTarget ? 'true' : 'false');
  });
  targetTab.focus();
}
```

**Why roving tabindex:**
- Only one tab is in the tab order at a time (`tabindex="0"`)
- All other tabs are removed from the tab order (`tabindex="-1"`) but remain focusable via arrow key JS
- The Tab key skips over inactive tabs — it jumps from the active tab directly to the panel content

Source: [APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/), [A11y Collective](https://www.a11y-collective.com/blog/accessibility-tab/)

---

## Implementation Template

```js
function initTabs(tablist) {
  const tabs = Array.from(tablist.querySelectorAll('[role="tab"]'));
  const isVertical = tablist.getAttribute('aria-orientation') === 'vertical';
  const isManual = tablist.dataset.activation === 'manual';

  const NEXT = isVertical ? 'ArrowDown' : 'ArrowRight';
  const PREV = isVertical ? 'ArrowUp' : 'ArrowLeft';

  tablist.addEventListener('keydown', (e) => {
    const current = tabs.indexOf(document.activeElement);
    if (current === -1) return;

    let target;
    switch (e.key) {
      case NEXT:
        target = tabs[(current + 1) % tabs.length];
        break;
      case PREV:
        target = tabs[(current - 1 + tabs.length) % tabs.length];
        break;
      case 'Home':
        target = tabs[0];
        break;
      case 'End':
        target = tabs[tabs.length - 1];
        break;
      case 'Enter':
      case ' ':
        if (isManual) {
          e.preventDefault();
          activateTab(tabs, tabs[current]);
        }
        return;
      default:
        return;
    }

    e.preventDefault();
    if (isManual) {
      // Focus only — don't activate
      target.setAttribute('tabindex', '0');
      tabs[current].setAttribute('tabindex', '-1');
      target.focus();
    } else {
      activateTab(tabs, target);
    }
  });
}

function activateTab(tabs, target) {
  tabs.forEach(tab => {
    const isTarget = tab === target;
    tab.setAttribute('tabindex', isTarget ? '0' : '-1');
    tab.setAttribute('aria-selected', String(isTarget));

    const panel = document.getElementById(tab.getAttribute('aria-controls'));
    if (panel) panel.hidden = !isTarget;
  });
  target.focus();
}
```

Source: Derived from [APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/) and [APG Manual Activation Example](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/examples/tabs-manual/)
