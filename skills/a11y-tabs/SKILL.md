---
name: a11y-tabs
description: Guides accessible tab interface implementation per APG patterns. Auto-invokes when creating tabs, tabbed panels, tab navigation, or tabbed content components. Covers required ARIA roles/states, keyboard interaction, automatic vs manual activation, and horizontal vs vertical orientation.
allowed-tools: Read, Glob, Grep
compatibility: "Claude Code, Codex CLI, Gemini CLI"
---

# Accessible Tabs

> "No ARIA is better than Bad ARIA."
> — [APG Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)

Tabs have no native HTML equivalent — ARIA is required. That means you own all behavior: keyboard interaction, focus management, and state updates. The [APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/) is the normative reference.

---

## 1. Required ARIA Structure

Three roles form the tab pattern. All three are mandatory. ([APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/))

| Element | Role | Required Context |
|---------|------|-----------------|
| Container for tabs | `tablist` | Must own `tab` elements directly (no wrapper divs between them) |
| Each tab trigger | `tab` | Must be inside a `tablist` |
| Each content panel | `tabpanel` | Associated with its `tab` via `aria-labelledby` |

### Minimal Skeleton

```html
<!-- RIGHT -->
<div role="tablist" aria-label="Settings">
  <button role="tab" id="tab-1" aria-selected="true" aria-controls="panel-1" tabindex="0">
    General
  </button>
  <button role="tab" id="tab-2" aria-selected="false" aria-controls="panel-2" tabindex="-1">
    Advanced
  </button>
</div>

<div role="tabpanel" id="panel-1" aria-labelledby="tab-1" tabindex="0">
  <!-- General settings content -->
</div>

<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>
  <!-- Advanced settings content -->
</div>
```

### Required Attributes Checklist

**On `tablist`:** ([APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/))
- `aria-label` or `aria-labelledby` — names the tab group

**On each `tab`:** ([APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/))
- `aria-selected="true|false"` — active tab is `true`, all others `false`
- `aria-controls` — references the `id` of the associated `tabpanel`
- `tabindex="0"` on the active tab; `tabindex="-1"` on all inactive tabs (roving tabindex)

**On each `tabpanel`:** ([APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/), [Access & Use](https://accessuse.eu/en/tabbed-interfaces.html))
- `aria-labelledby` — references the `id` of the associated `tab`
- `tabindex="0"` if the panel has no focusable elements (so keyboard users can reach it)

### Hiding Inactive Panels

```html
<!-- WRONG — aria-hidden is inconsistent across screen readers -->
<div role="tabpanel" aria-hidden="true">...</div>

<!-- RIGHT — CSS or hidden attribute reliably removes from both visual and a11y tree -->
<div role="tabpanel" hidden>...</div>
<div role="tabpanel" style="display: none">...</div>
```

Use `display: none`, `visibility: hidden`, or the `hidden` attribute — not `aria-hidden`. ([Adrian Roselli](https://adrianroselli.com/2013/02/aria-tabs.html))

---

## 2. Automatic vs Manual Activation

**Default to automatic activation.** The APG states that manual activation "significantly hampers users' ability to navigate efficiently." ([APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/))

| Mode | Behavior | When to Use |
|------|----------|-------------|
| **Automatic** (default) | Arrow key focus change immediately displays the panel | Content is local or loads instantly |
| **Manual** | Arrow keys move focus; Enter/Space activates | Content requires network requests, has side effects, or causes noticeable lag |

```js
// Automatic — activate on arrow key
tab.addEventListener('focus', () => activateTab(tab));

// Manual — activate on Enter/Space only
tab.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault();
    activateTab(tab);
  }
});
```

---

## 3. Horizontal vs Vertical Orientation

Orientation determines which arrow keys navigate between tabs. ([APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/))

| Orientation | Navigate with | Ignored keys | `aria-orientation` |
|-------------|--------------|-------------|-------------------|
| **Horizontal** (default) | Left/Right Arrow | Up/Down (pass through for page scroll) | Omit or `"horizontal"` |
| **Vertical** | Up/Down Arrow | Left/Right | **Must set** `"vertical"` |

```html
<!-- Vertical tabs — aria-orientation is REQUIRED -->
<div role="tablist" aria-label="Sections" aria-orientation="vertical">
  ...
</div>
```

Without `aria-orientation="vertical"`, screen readers will not communicate the vertical layout to users.

---

## 4. Keyboard Interaction Summary

The full keyboard spec is in `${CLAUDE_SKILL_DIR}/references/keyboard-interaction.md`. The essentials:

| Key | Action |
|-----|--------|
| Arrow keys | Move focus to next/previous tab (direction depends on orientation; wraps) |
| Tab | Into tablist: focuses the active tab. From tab: moves to panel or next focusable element |
| Enter / Space | Activates focused tab (manual mode only) |
| Home / End (optional) | First / last tab |
| Delete (optional) | Removes current tab if deletable |

**Critical:** The Tab key does NOT cycle through individual tabs. Arrow keys handle inter-tab navigation; Tab exits the tablist. Violating this "defeats the pattern's purpose." ([James Bateson](https://jamesbateson.co.uk/articles/making-tab-patterns-accessible/))

---

## 5. Common Mistakes

### 5.1 Nesting Interactive Elements Inside Tabs

```html
<!-- WRONG — button semantics are stripped -->
<div role="tab"><button>Settings</button></div>

<!-- RIGHT — tab IS the interactive element -->
<button role="tab">Settings</button>
```

The `tab` role marks all children as **presentational**. Buttons, links, or inputs inside a `tab` lose their semantics entirely. ([Adrian Roselli](https://adrianroselli.com/2020/04/when-is-a-vetted-pattern-no-longer-a-vetted-pattern.html), [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/#tab))

### 5.2 Using Tab Key Between Tabs

```js
// WRONG — Tab key cycles through tabs like a toolbar
tabs.forEach(tab => tab.tabIndex = 0);

// RIGHT — roving tabindex: only active tab is in tab order
tabs.forEach(tab => {
  tab.tabIndex = tab === activeTab ? 0 : -1;
});
```

Keyboard users expect Tab to move to the next widget, not the next sibling tab. ([James Bateson](https://jamesbateson.co.uk/articles/making-tab-patterns-accessible/))

### 5.3 Missing ARIA Relationships

```html
<!-- WRONG — no association between tab and panel -->
<button role="tab">Info</button>
<div role="tabpanel">Content here</div>

<!-- RIGHT — two-way association -->
<button role="tab" id="t1" aria-controls="p1">Info</button>
<div role="tabpanel" id="p1" aria-labelledby="t1">Content here</div>
```

Without `aria-controls` and `aria-labelledby`, screen readers cannot tell users which panel belongs to which tab. ([APG Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/))

### 5.4 Unfocusable Panels

When a panel has only static text, keyboard users cannot Tab into it. Screen readers in forms mode make this worse — the user must manually switch modes to read content. ([Access & Use](https://accessuse.eu/en/tabbed-interfaces.html))

**Fix:** Add `tabindex="0"` to the panel, or programmatically move focus to it on activation.

### 5.5 Wrapper Elements Breaking Role Hierarchy

```html
<!-- WRONG — div breaks tablist → tab ownership -->
<div role="tablist">
  <div class="tab-wrapper">
    <button role="tab">One</button>
  </div>
</div>

<!-- RIGHT — tabs are direct children of tablist -->
<div role="tablist">
  <button role="tab">One</button>
</div>
```

Incorrect DOM hierarchy between `tablist` and `tab` can break screen reader announcements entirely. "No ARIA is better than bad ARIA." ([James Bateson](https://jamesbateson.co.uk/articles/making-tab-patterns-accessible/))

### 5.6 Modifying Patterns Without Re-Testing

Adding features (close buttons, pin buttons, drag handles) to a working tab pattern creates compounding interaction problems. "You must consider that you are also introducing code that can result in bugs... changes that can be confusing to users." ([Adrian Roselli](https://adrianroselli.com/2020/04/when-is-a-vetted-pattern-no-longer-a-vetted-pattern.html))

---

## 6. Cross-References

- `aria-decision-framework` — check whether you even need ARIA (you do for tabs, but the decision process matters)
- `focus-management` — roving tabindex, focus trapping, and programmatic focus patterns
- `${CLAUDE_SKILL_DIR}/references/keyboard-interaction.md` — full keyboard spec with edge cases
- `${CLAUDE_SKILL_DIR}/references/common-mistakes.md` — extended mistake catalog with citations
- `${CLAUDE_SKILL_DIR}/references/screen-reader-behavior.md` — JAWS, NVDA, and VoiceOver differences
- `${CLAUDE_SKILL_DIR}/references/sources.yaml` — provenance for all cited sources
