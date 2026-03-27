---
name: a11y-combobox
description: Guides accessible combobox and autocomplete implementation per APG patterns. Auto-invokes when creating combobox, autocomplete, typeahead, select-with-search, or custom dropdown components. Covers required ARIA, keyboard interaction, and variant selection (select-only, editable, autocomplete modes).
allowed-tools: Read, Glob, Grep
compatibility: "Claude Code, Codex CLI, Gemini CLI"
---

# Accessible Combobox Implementation

> "No ARIA is better than Bad ARIA."
> — [APG Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)

A combobox is a composite widget combining a named input with a popup that lets users set the input's value. The popup can be a `listbox`, `grid`, `tree`, or `dialog`. ([APG Combobox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/))

This is one of the hardest widgets to get right. Screen reader support is inconsistent, `aria-activedescendant` is unreliable, and the keyboard interaction surface is large. Read this skill before building.

---

## 1. When to Use Native `<select>` vs Combobox

Use this decision tree before reaching for ARIA combobox.

| Situation | Use | Why |
|---|---|---|
| Single selection, < 15 items, no filtering needed | `<select>` | 100% AT success rate, 97.5 usability score in testing. ([24a11y study](https://www.24a11y.com/2019/select-your-poison-part-2/)) |
| Simple autocomplete, inconsistent styling acceptable | `<datalist>` | Native, but broken on Android Firefox, iOS/iPadOS VoiceOver limited to 3 options. ([Roselli](https://adrianroselli.com/2023/06/under-engineered-comboboxen.html)) |
| > 15 options, need type-ahead filtering, closed list | Select-only combobox | Custom styling possible; caveat: WebKit bug with `aria-activedescendant` in VoiceOver/Safari. ([APG](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-select-only/)) |
| Free text input + optional suggestions | Editable combobox | Search, address lookup, autocomplete patterns. ([APG](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)) |
| Multi-select from list | **Avoid `<select multiple>`** | Only 25.3% AT success rate. Use a listbox with checkboxes instead. ([24a11y study](https://www.24a11y.com/2019/select-your-poison-part-2/)) |

**Do NOT use** the ARIA 1.1 readonly-input combobox pattern — it is invisible to NVDA scan mode. ([24a11y study](https://www.24a11y.com/2019/select-your-poison-part-2/))

---

## 2. Combobox Variants

### Autocomplete Modes

| Mode | `aria-autocomplete` | Behavior |
|------|---------------------|----------|
| No autocomplete | `none` | Popup shows fixed suggestions (e.g., recent searches) |
| List (manual) | `list` | Popup filters to matches; user must explicitly select |
| List (automatic) | `list` | First match auto-highlighted; becomes value on blur |
| Inline + list | `both` | First match auto-highlighted AND inline completion shown in input |

Source: [APG Combobox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)

### Structural Variants

1. **Select-only** — No text input; `<div role="combobox">`. Functionally replaces `<select>`. ([Example](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-select-only/))
2. **Editable + autocomplete="both"** — Full inline + list filtering. ([Example](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-autocomplete-both/))
3. **Editable + autocomplete="list"** — List filtering, manual selection. ([Example](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-autocomplete-list/))
4. **Editable + autocomplete="none"** — Fixed suggestion list, no filtering. ([Example](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-autocomplete-none/))
5. **Grid popup** — `role="grid"` popup for tabular suggestions. ([Example](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/grid-combo/))
6. **Dialog popup** — `role="dialog"` popup (e.g., date picker). DOM focus moves into dialog. ([Example](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-datepicker/))

---

## 3. Required ARIA Structure

### Minimal Correct Markup (Editable + Listbox)

```html
<!-- WRONG — missing aria-controls, no listbox role, no option roles -->
<input type="text" role="combobox">
<ul class="dropdown">
  <li>Option 1</li>
</ul>

<!-- RIGHT -->
<label for="fruit-input">Fruit</label>
<input
  id="fruit-input"
  role="combobox"
  type="text"
  aria-expanded="false"
  aria-controls="fruit-listbox"
  aria-autocomplete="list"
  aria-activedescendant=""
>
<ul id="fruit-listbox" role="listbox" hidden>
  <li id="opt-apple" role="option">Apple</li>
  <li id="opt-banana" role="option">Banana</li>
</ul>
```

### Minimal Correct Markup (Select-Only)

```html
<!-- WRONG — using readonly input (ARIA 1.1 pattern, invisible to NVDA scan mode) -->
<input type="text" role="combobox" readonly>

<!-- RIGHT -->
<label id="color-label">Color</label>
<div
  role="combobox"
  tabindex="0"
  aria-labelledby="color-label"
  aria-expanded="false"
  aria-controls="color-listbox"
  aria-haspopup="listbox"
  aria-activedescendant=""
>Red</div>
<ul id="color-listbox" role="listbox" hidden>
  <li id="opt-red" role="option" aria-selected="true">Red</li>
  <li id="opt-blue" role="option">Blue</li>
</ul>
```

### Required Attributes Reference

| Element | Attribute | Value | Notes |
|---------|-----------|-------|-------|
| Combobox | `role` | `combobox` | On `<input>` or `<div>` (select-only) |
| Combobox | `aria-controls` | IDREF | Must reference popup; present even when hidden |
| Combobox | `aria-expanded` | `true`/`false` | Reflects popup visibility |
| Combobox | `aria-autocomplete` | `none`/`list`/`both` | Omit only if `none` |
| Combobox | `aria-haspopup` | `grid`/`tree`/`dialog` | Only when popup is NOT listbox (default) |
| Combobox | `aria-activedescendant` | IDREF | Points to focused option; DOM focus stays on combobox |
| Popup | `role` | `listbox`/`grid`/`tree`/`dialog` | Must match `aria-haspopup` |
| Options | `role` | `option`/`gridcell`/`treeitem` | Per popup type |
| Options | `aria-selected` | `true` | On currently focused/selected option |

Source: [APG Combobox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/), [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/#combobox)

---

## 4. Keyboard Interaction Summary

Abbreviated table. Full spec per variant: `${CLAUDE_SKILL_DIR}/references/keyboard-interaction.md`

| Key | Editable Combobox | Select-Only (Closed) | Select-Only (Open) |
|-----|-------------------|----------------------|---------------------|
| Down Arrow | Open popup, focus first/next option | Open popup | Next option |
| Up Arrow | Open popup (optional), focus last | Open popup | Previous option |
| Enter | Accept focused option, close | Open popup | Accept option, close |
| Escape | Close popup | — | Close without selecting |
| Tab | Move focus out | Move focus out | Accept + close + move focus |
| Printable chars | Type in input | Open + jump to match | Jump to matching option |
| Home/End | Move cursor in input | — | First/last option |
| Alt+Down | Open without moving focus | Open popup | — |

---

## 5. Common Mistakes

### 5.1 Treating `aria-activedescendant` as DOM Focus

```html
<!-- WRONG — moving DOM focus to each option -->
<input role="combobox" ...>
<ul role="listbox">
  <li role="option" tabindex="0">Apple</li> <!-- Don't make options focusable -->
</ul>

<!-- RIGHT — DOM focus stays on input, aria-activedescendant points to option -->
<input role="combobox" aria-activedescendant="opt-apple" ...>
<ul role="listbox">
  <li id="opt-apple" role="option" aria-selected="true">Apple</li>
</ul>
```

`aria-activedescendant` is a screen reader semantic, not focus. Only one element has true focus (`document.activeElement`). Keyboard events fire on the focused element, not the active descendant. ([Higley](https://sarahmhigley.com/writing/activedescendant/))

**Exception:** Dialog popups DO move real DOM focus into the dialog. They do NOT use `aria-activedescendant`. ([APG](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/))

### 5.2 Relying Solely on `aria-activedescendant` for Announcements

VoiceOver ignores `aria-activedescendant` changes when the input is empty (Safari) or when `aria-selected="true"` is missing (Chrome). NVDA fails to announce character deletions. Mobile screen readers essentially ignore it entirely.

**Fix:** Supplement with a hidden `aria-live` region for critical state changes (option count, selected value). React Aria had to adopt this workaround. ([React Aria](https://react-aria.adobe.com/blog/building-a-combobox); [Higley](https://sarahmhigley.com/writing/activedescendant/))

### 5.3 Using `role="group"` on Option Groups

```html
<!-- WRONG — VoiceOver fails to announce focus on grouped options -->
<ul role="listbox">
  <li role="group">
    <ul>
      <li role="option">Apple</li>
    </ul>
  </li>
</ul>

<!-- RIGHT — flat list, use aria-label on options if grouping context needed -->
<ul role="listbox">
  <li role="option" aria-label="Fruit: Apple">Apple</li>
</ul>
```

Source: [React Aria](https://react-aria.adobe.com/blog/building-a-combobox)

### 5.4 Missing `aria-controls` When Popup Is Hidden

`aria-controls` must reference the popup element even when the popup is not visible. The referenced element must exist in the DOM. ([APG Combobox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/))

### 5.5 Adding Screen Reader Control Hints

```html
<!-- WRONG — screen readers already announce how to use a combobox -->
<input role="combobox" aria-description="Use arrow keys to navigate options">

<!-- RIGHT — let the screen reader provide its own instructions -->
<input role="combobox" ...>
```

Screen readers already tell users how to interact with standard controls. Custom instructions create conflicts, redundancy, and verbosity. ([Roselli](https://adrianroselli.com/2019/10/stop-giving-control-hints-to-screen-readers.html))

### 5.6 Auto-filtering Without User Request

The 24a11y study found that auto-filtering options without explicit user opt-in reduced success rates. Show the full list first; filter only on explicit interaction. ([24a11y study](https://www.24a11y.com/2019/select-your-poison-part-2/))

---

## 6. Cross-References

- `aria-decision-framework` — check whether you need ARIA combobox at all (use native `<select>` first)
- `${CLAUDE_SKILL_DIR}/references/keyboard-interaction.md` — complete keyboard spec per variant
- `${CLAUDE_SKILL_DIR}/references/screen-reader-behavior.md` — per-AT behavior differences and workarounds
- `${CLAUDE_SKILL_DIR}/references/common-mistakes.md` — expanded anti-patterns with citations
- `${CLAUDE_SKILL_DIR}/references/sources.yaml` — provenance for all cited sources
