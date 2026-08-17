# Common Mistakes — Tabs
## Contents

- [1. Nesting Interactive Elements Inside Tabs](#1-nesting-interactive-elements-inside-tabs)
- [2. Using Tab Key for Inter-Tab Navigation](#2-using-tab-key-for-inter-tab-navigation)
- [3. Missing or Incorrect ARIA Relationships](#3-missing-or-incorrect-aria-relationships)
- [4. Using aria-hidden to Hide Inactive Panels](#4-using-aria-hidden-to-hide-inactive-panels)
- [5. Unfocusable Panels with Static Content](#5-unfocusable-panels-with-static-content)
- [6. Wrapper Elements Breaking Role Hierarchy](#6-wrapper-elements-breaking-role-hierarchy)
- [7. Modifying Vetted Patterns Without Re-Testing](#7-modifying-vetted-patterns-without-re-testing)
- [8. Missing aria-orientation on Vertical Tabs](#8-missing-aria-orientation-on-vertical-tabs)
- [9. Changing Native Semantics with Tab Role](#9-changing-native-semantics-with-tab-role)


Extended catalog of tab accessibility mistakes with citations. The top mistakes are summarized in the main SKILL.md; this file provides additional detail and edge cases.

---

## 1. Nesting Interactive Elements Inside Tabs

The `tab` role has **presentational children** — all child elements lose their semantics in the accessibility tree. This is a spec requirement.

```html
<!-- WRONG — the <a> and <button> are invisible to screen readers -->
<div role="tab">
  <a href="/settings">Settings</a>
  <button aria-label="Close">×</button>
</div>

<!-- RIGHT — the tab IS the interactive element -->
<button role="tab" id="tab-settings" aria-selected="true" aria-controls="panel-settings">
  Settings
</button>
```

"The tab role explicitly treats all children as presentation, stripping their semantics."

Source: [Adrian Roselli](https://adrianroselli.com/2020/04/when-is-a-vetted-pattern-no-longer-a-vetted-pattern.html), [WAI-ARIA 1.2 — tab role](https://www.w3.org/TR/wai-aria-1.2/#tab)

---

## 2. Using Tab Key for Inter-Tab Navigation

```js
// WRONG — every tab has tabindex="0", Tab key cycles through them
document.querySelectorAll('[role="tab"]').forEach(tab => {
  tab.setAttribute('tabindex', '0');
});

// RIGHT — roving tabindex pattern
function setActiveTab(activeTab, allTabs) {
  allTabs.forEach(tab => {
    tab.setAttribute('tabindex', tab === activeTab ? '0' : '-1');
    tab.setAttribute('aria-selected', String(tab === activeTab));
  });
}
```

When all tabs have `tabindex="0"`, the Tab key cycles through each tab individually. This defeats the pattern: keyboard users expect Tab to move to the next widget (the panel), not the next sibling tab. Arrow keys handle intra-tablist navigation.

Source: [James Bateson](https://jamesbateson.co.uk/articles/making-tab-patterns-accessible/), [APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)

---

## 3. Missing or Incorrect ARIA Relationships

Each tab-panel pair requires a two-way association:

```html
<!-- WRONG — no association -->
<button role="tab">Profile</button>
<div role="tabpanel">Profile content</div>

<!-- WRONG — one-way only -->
<button role="tab" aria-controls="p1">Profile</button>
<div role="tabpanel" id="p1">Profile content</div>

<!-- RIGHT — two-way association -->
<button role="tab" id="tab-profile" aria-controls="panel-profile">Profile</button>
<div role="tabpanel" id="panel-profile" aria-labelledby="tab-profile">Profile content</div>
```

Without `aria-labelledby` on the panel, screen readers cannot announce which tab the panel belongs to when focus enters it.

Source: [APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)

---

## 4. Using `aria-hidden` to Hide Inactive Panels

```html
<!-- WRONG — inconsistent screen reader support -->
<div role="tabpanel" aria-hidden="true">Hidden content</div>

<!-- RIGHT — reliably hidden from both visual and a11y tree -->
<div role="tabpanel" hidden>Hidden content</div>
```

Adrian Roselli originally used `aria-hidden` for inactive panels but revised this approach after feedback from Marco Zehe. `aria-hidden` is not consistently supported across screen readers (particularly older JAWS versions). `display: none`, `visibility: hidden`, or the `hidden` attribute reliably remove content from both visual display and the accessibility tree.

Source: [Adrian Roselli](https://adrianroselli.com/2013/02/aria-tabs.html)

---

## 5. Unfocusable Panels with Static Content

When a tab panel contains only text (no links, buttons, or form fields), keyboard users cannot Tab into it after activating the tab.

```html
<!-- WRONG — panel is unreachable via keyboard -->
<div role="tabpanel" aria-labelledby="tab-1">
  <p>This is plain text content with no interactive elements.</p>
</div>

<!-- RIGHT — panel itself is focusable -->
<div role="tabpanel" aria-labelledby="tab-1" tabindex="0">
  <p>This is plain text content with no interactive elements.</p>
</div>
```

This is especially critical because screen readers enter forms/application mode when interacting with a tablist. In forms mode, users can only navigate to focusable elements — static text in an unfocusable panel is effectively invisible until the user manually switches to browse mode.

Source: [APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/), [Access & Use](https://accessuse.eu/en/tabbed-interfaces.html)

---

## 6. Wrapper Elements Breaking Role Hierarchy

The `tablist` role expects direct `tab` children. Inserting wrapper elements between them can break the parent-child relationship.

```html
<!-- WRONG — wrapper breaks tablist → tab ownership -->
<div role="tablist">
  <div class="tab-container">
    <button role="tab">One</button>
  </div>
  <div class="tab-container">
    <button role="tab">Two</button>
  </div>
</div>

<!-- RIGHT — tabs are direct children -->
<div role="tablist">
  <button role="tab">One</button>
  <button role="tab">Two</button>
</div>
```

"No ARIA is better than bad ARIA" — incorrect DOM hierarchy can cause screen readers to not announce the tablist structure at all.

Source: [James Bateson](https://jamesbateson.co.uk/articles/making-tab-patterns-accessible/)

---

## 7. Modifying Vetted Patterns Without Re-Testing

Adding features to a working tab pattern (close buttons, pin buttons, drag-and-drop reordering) creates compounding interaction problems. Each addition:

- Introduces new keyboard shortcuts that may conflict
- Creates additional focus management requirements
- May break the presentational-children model (see mistake #1)
- Requires re-testing across all screen reader / browser combinations

"You must consider that you are also introducing code that can result in bugs... changes that can be confusing to users."

Source: [Adrian Roselli](https://adrianroselli.com/2020/04/when-is-a-vetted-pattern-no-longer-a-vetted-pattern.html)

---

## 8. Missing `aria-orientation` on Vertical Tabs

```html
<!-- WRONG — screen reader assumes horizontal layout -->
<div role="tablist" aria-label="Sidebar">
  <!-- Visual layout is vertical but aria-orientation is absent -->
</div>

<!-- RIGHT -->
<div role="tablist" aria-label="Sidebar" aria-orientation="vertical">
  ...
</div>
```

Without `aria-orientation="vertical"`, users expect Left/Right arrows to work and may not try Up/Down. The default is `"horizontal"`, which must be overridden for vertical layouts.

Source: [APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)

---

## 9. Changing Native Semantics with Tab Role

```html
<!-- WRONG — heading semantics are overridden -->
<h2 role="tab">Settings</h2>

<!-- RIGHT — nest the heading, don't overwrite its semantics -->
<button role="tab"><h2>Settings</h2></button>
```

ARIA Rule 2: "Do not change native semantics, unless you really have to." Placing `role="tab"` on an `<h2>` removes its heading semantics from the accessibility tree.

Source: [Using ARIA, Rule 2](https://www.w3.org/TR/using-aria/)
