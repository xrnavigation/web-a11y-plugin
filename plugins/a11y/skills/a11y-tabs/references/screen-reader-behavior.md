# Screen Reader Behavior — Tabs
## Contents

- [General Announcement Pattern](#general-announcement-pattern)
- [JAWS (Windows)](#jaws-windows)
- [NVDA (Windows)](#nvda-windows)
- [VoiceOver (macOS)](#voiceover-macos)
- [VoiceOver (iOS)](#voiceover-ios)
- [Critical Issue: Panels Without Focusable Content](#critical-issue-panels-without-focusable-content)
  - [Mitigations](#mitigations)
- [Testing Recommendations](#testing-recommendations)


How different screen readers handle the tab pattern. Understanding these differences helps you test effectively and avoid assumptions about universal behavior.

---

## General Announcement Pattern

When a screen reader user focuses a tab, the screen reader typically announces:

1. The tab role ("tab")
2. The tab's accessible name (text content or `aria-label`)
3. The selection state ("selected" or "not selected")
4. Position in the set (e.g., "1 of 4")

Source: [Access & Use](https://accessuse.eu/en/tabbed-interfaces.html), [Deque](https://www.deque.com/blog/a11y-support-series-part-1-aria-tab-panel-accessibility/)

---

## JAWS (Windows)

- Announces a keyboard shortcut for jumping directly to the associated panel
- Enters **forms/application mode** when focus reaches a tablist — standard browse-mode shortcuts (H for headings, T for tables, etc.) are disabled
- Automatically enters focus mode, which means only focusable elements are reachable
- Position announcement: "Tab, [name], selected, [n] of [total]"

**Implication:** Panel content must be focusable (via `tabindex="0"` on the panel or focusable elements inside it), or JAWS users in forms mode cannot read it without manually switching to browse mode.

Source: [Access & Use](https://accessuse.eu/en/tabbed-interfaces.html)

---

## NVDA (Windows)

- Announces tab role, name, state, and count (e.g., "Tab 1, selected, tab, 1 of 3")
- Enters **forms mode** when focus reaches the tablist
- Does NOT announce a panel-jump shortcut (unlike JAWS)
- Arrow keys work as expected for tab navigation in forms mode

**Implication:** Same as JAWS — forms mode limits navigation to focusable elements. Unfocusable panels are a barrier.

Source: [Access & Use](https://accessuse.eu/en/tabbed-interfaces.html)

---

## VoiceOver (macOS)

- Does not use a separate forms/application mode — navigation model is unified
- May navigate differently through tablist structures compared to JAWS/NVDA
- Can miss certain issues that JAWS/NVDA catch due to the lack of mode-switching
- Announcement pattern is similar but phrasing differs

Source: [Access & Use](https://accessuse.eu/en/tabbed-interfaces.html)

---

## VoiceOver (iOS)

- Mobile VoiceOver users interact via swipe gestures, not keyboard
- Lacks distinct focus operations, making tabbed structure less clear on touchscreens
- The swipe-to-next paradigm means tabs and panels appear sequentially rather than as a grouped widget
- Consider whether a tabbed interface is the best pattern for mobile at all — sometimes a simple stacked layout or accordion is more usable

Source: [Access & Use](https://accessuse.eu/en/tabbed-interfaces.html)

---

## Critical Issue: Panels Without Focusable Content

This is the most common screen reader issue with tabs. When screen readers enter forms/application mode at a tablist, discovering a tab panel with no focusable elements becomes difficult:

1. The user activates a tab (or arrows to it)
2. The user presses Tab to move to the panel
3. If the panel has `tabindex="0"`, focus lands on the panel — user can read content
4. If the panel has NO focusable elements, focus jumps past the panel entirely

### Mitigations

**Option A: Make the panel focusable (recommended)**
```html
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1" tabindex="0">
  <p>Static text content the user needs to read.</p>
</div>
```

**Option B: Programmatically move focus on activation**
```js
function activateTab(tab) {
  const panel = document.getElementById(tab.getAttribute('aria-controls'));
  panel.setAttribute('tabindex', '-1');
  panel.focus();
}
```

**Option C: Add usage instructions (supplementary)**
```html
<div role="tablist" aria-label="Account settings" aria-describedby="tab-instructions">
  ...
</div>
<p id="tab-instructions" class="visually-hidden">
  Use arrow keys to select tabs. Press Tab to move to the selected panel.
</p>
```

Source: [Access & Use](https://accessuse.eu/en/tabbed-interfaces.html), [APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)

---

## Testing Recommendations

Test with at minimum:
1. **JAWS + Chrome** (Windows) — most common enterprise screen reader
2. **NVDA + Firefox** (Windows) — most common free screen reader
3. **VoiceOver + Safari** (macOS) — primary macOS screen reader

Verify:
- Tab role, name, state, and position are announced correctly
- Arrow keys navigate between tabs
- Tab key moves from active tab to panel content
- Panel content is reachable and readable in forms mode
- Inactive panels are NOT announced

Source: [Deque](https://www.deque.com/blog/a11y-support-series-part-1-aria-tab-panel-accessibility/)
