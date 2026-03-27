---
name: aria-decision-framework
description: Guides correct ARIA usage by encoding the "first rule of ARIA" — use native HTML elements before reaching for ARIA roles. Auto-invokes when writing ARIA attributes, custom interactive elements, or role attributes. Prevents the most common LLM accessibility error: ARIA misuse and overuse.
allowed-tools: Read, Glob, Grep
compatibility: "Claude Code, Codex CLI, Gemini CLI"
---

# ARIA Decision Framework

> "No ARIA is better than Bad ARIA."
> — [APG Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)

> "WAI-ARIA is intended to be used as a supplement for native language semantics, not a replacement."
> — [WAI-ARIA 1.2, §1.1](https://www.w3.org/TR/wai-aria-1.2/)

ARIA does not add behavior. It only changes what the browser communicates to the accessibility tree. A `<div role="button">` looks like a button to a screen reader, but it does not act like one — no focus, no keyboard activation, no form submission. Every ARIA role you add is a promise to implement the behavior yourself.

---

## 1. The Five Rules of ARIA

These rules are from the W3C note [Using ARIA](https://www.w3.org/TR/using-aria/). They are not suggestions.

### Rule 1: Use Native HTML Instead of ARIA

> "If you can use a native HTML element with the semantics and behavior you require already built in, instead of re-purposing an element and adding an ARIA role, state or property to make it accessible, then do so."

**For agents:** Before writing `role="..."`, check whether a native HTML element already does what you need. The answer is usually yes.

### Rule 2: Do Not Change Native Semantics

> "Do not change native semantics, unless you really have to."

```html
<!-- WRONG --> <h2 role="tab">Settings</h2>
<!-- RIGHT --> <div role="tab"><h2>Settings</h2></div>
```

**For agents:** Never put a `role` on a semantic element unless the spec explicitly allows it and you have a real reason.

### Rule 3: All Interactive ARIA Controls Must Be Keyboard Accessible

> "All interactive ARIA controls must be usable with the keyboard."

**For agents:** If you write `role="button"`, you must also write `tabindex="0"` and keyboard event handlers for Enter and Space. If you write `role="slider"`, you must handle Arrow keys. If this sounds like a lot of work — use `<button>` or `<input type="range">` instead.

### Rule 4: Do Not Hide Focusable Elements from AT

> "Do not use `role='presentation'` or `aria-hidden='true'` on a focusable element."

**For agents:** Before writing `aria-hidden="true"`, check: can anything inside this container receive focus? If yes, use `display: none`, `hidden`, or the `inert` attribute instead.

### Rule 5: All Interactive Elements Must Have an Accessible Name

> "All interactive elements must have an accessible name."

**For agents:** Every `<button>`, `<a>`, `<input>`, and custom widget needs a name. Use visible text content, `<label>`, `aria-label`, or `aria-labelledby`. Never ship an unnamed interactive element.

---

## 2. Decision Tree

Use this flowchart every time you are about to write ARIA attributes or custom interactive elements.

```
START: "I need an interactive element that does X"
  │
  ├─ Step 1: Is there a native HTML element that does X?
  │   │
  │   ├─ YES → Use it. Stop. Do not add ARIA roles.
  │   │   Examples:
  │   │     Need a button → <button>
  │   │     Need a link → <a href="...">
  │   │     Need a checkbox → <input type="checkbox">
  │   │     Need a text field → <input type="text"> or <textarea>
  │   │     Need a dropdown → <select>
  │   │     Need a disclosure → <details>/<summary>
  │   │     Need a dialog → <dialog>
  │   │     Need a progress bar → <progress>
  │   │     Need a slider → <input type="range">
  │   │
  │   └─ NO → Continue to Step 2
  │
  ├─ Step 2: Can you style a native element to match the design?
  │   │
  │   ├─ YES → Use the native element + CSS. Stop.
  │   │   A styled <button> is always better than a <div role="button">.
  │   │
  │   └─ NO → Continue to Step 3
  │
  └─ Step 3: No native element exists. Use ARIA.
      │
      You now own:
      ├─ Keyboard interaction (all of it)
      ├─ Focus management
      ├─ State management (aria-expanded, aria-checked, etc.)
      ├─ Required ARIA attributes for the role
      └─ Parent-child role relationships

      See: ${CLAUDE_SKILL_DIR}/references/required-aria-attributes.md
```

**Legitimate Step 3 cases** (widgets with no native HTML equivalent):
- Tabs (`tablist`/`tab`/`tabpanel`)
- Tree views (`tree`/`treeitem`)
- Combobox with custom popup (`combobox` — native `<select>` can't be styled)
- Menu buttons (`menu`/`menuitem` — application-style, NOT site navigation)
- Grids with interactive cells (`grid`/`gridcell`)
- Toggle buttons (`button` with `aria-pressed`)
- Toolbars (`toolbar`)
- Accordions (though `<details>`/`<summary>` often suffices)

---

## 3. Native Element to ARIA Role Mapping (Top 20)

When the native element exists, ARIA is redundant. Do not add these roles.

| Native HTML | Implicit ARIA Role | Do NOT Write |
|---|---|---|
| `<button>` | `button` | `<button role="button">` |
| `<a href="...">` | `link` | `<a role="link">` |
| `<input type="checkbox">` | `checkbox` | `<input type="checkbox" role="checkbox">` |
| `<input type="radio">` | `radio` | `<input type="radio" role="radio">` |
| `<input type="range">` | `slider` | `<input type="range" role="slider">` |
| `<input type="number">` | `spinbutton` | `<input type="number" role="spinbutton">` |
| `<input type="text">` | `textbox` | `<input type="text" role="textbox">` |
| `<textarea>` | `textbox` | `<textarea role="textbox">` |
| `<select>` | `combobox`/`listbox` | `<select role="combobox">` |
| `<option>` | `option` | `<option role="option">` |
| `<nav>` | `navigation` | `<nav role="navigation">` |
| `<main>` | `main` | `<main role="main">` |
| `<header>` (top-level) | `banner` | `<header role="banner">` |
| `<footer>` (top-level) | `contentinfo` | `<footer role="contentinfo">` |
| `<aside>` | `complementary` | `<aside role="complementary">` |
| `<form>` | `form` | `<form role="form">` |
| `<dialog>` | `dialog` | `<dialog role="dialog">` |
| `<table>` | `table` | `<table role="table">` |
| `<progress>` | `progressbar` | `<progress role="progressbar">` |
| `<output>` | `status` | `<output role="status">` |

For the complete mapping (all HTML elements), see: `${CLAUDE_SKILL_DIR}/references/html-aria-mapping.md`

---

## 4. Never Do This

These are the most common ARIA mistakes in LLM-generated code. Each is a real pattern from accessibility audits.

### 4.1 `<div role="button">` Without Full Keyboard Support

```html
<!-- WRONG -->
<div role="button" onclick="save()">Save</div>

<!-- RIGHT -->
<button onclick="save()">Save</button>
```

A `role="button"` without `tabindex="0"`, Enter handling, and Space handling is broken. "A role is a promise" — if you promise a button, deliver a button. ([APG Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/))

### 4.2 `aria-label` on Non-Interactive Generic Elements

```html
<!-- WRONG — aria-label ignored on <div> and <span> -->
<div aria-label="Statistics">42 users</div>
<span aria-label="Warning">Check email</span>

<!-- RIGHT — use a landmark or visible text -->
<section aria-label="Statistics">42 users</section>
<div><h2>Statistics</h2><p>42 users</p></div>
```

`aria-label` is not reliably supported on elements with `role="generic"` (the implicit role of `<div>` and `<span>`). ([WAI-ARIA 1.2, §5.4](https://www.w3.org/TR/wai-aria-1.2/))

### 4.3 Redundant ARIA

```html
<!-- WRONG — redundant -->
<nav role="navigation">
<button role="button">
<a href="/" role="link">

<!-- RIGHT — native semantics are sufficient -->
<nav>
<button>
<a href="/">
```

The element already has the implicit role. Adding it explicitly is noise. ([ARIA in HTML](https://w3c.github.io/html-aria/))

### 4.4 `aria-hidden="true"` on Focusable Elements

```html
<!-- WRONG — focusable but hidden from AT -->
<button aria-hidden="true">Close</button>

<!-- RIGHT -->
<button style="display:none">Close</button>
<!-- or -->
<div inert><button>Close</button></div>
```

Keyboard users tab to it; screen readers say nothing. ([Using ARIA, Rule 4](https://www.w3.org/TR/using-aria/); [ADG Bad Practices](https://www.accessibility-developer-guide.com/knowledge/aria/bad-practices/))

### 4.5 `role="menu"` for Site Navigation

```html
<!-- WRONG — navigation is not an application menu -->
<nav>
  <ul role="menu">
    <li role="menuitem"><a href="/">Home</a></li>
  </ul>
</nav>

<!-- RIGHT — just a nav with a list of links -->
<nav aria-label="Main">
  <ul>
    <li><a href="/">Home</a></li>
  </ul>
</nav>
```

ARIA `menu` is for application-style menus (context menus, action dropdowns). Site navigation is a list of links in a `<nav>` landmark. Using `role="menu"` breaks list semantics and violates WCAG 1.3.1. ([APG Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/); [Make Things Accessible](https://www.makethingsaccessible.com/guides/site-navigation-is-not-an-aria-menu/))

### 4.6 `aria-label` That Doesn't Match Visible Text

```html
<!-- WRONG — voice control users can't activate this -->
<button aria-label="Submit form data">Send</button>

<!-- RIGHT -->
<button>Send</button>
```

WCAG 2.5.3 (Label in Name) requires the accessible name to contain the visible text. ([WCAG 2.1, SC 2.5.3](https://www.w3.org/WAI/WCAG21/Understanding/label-in-name.html))

### 4.7 `aria-roledescription` Overuse

```html
<!-- WRONG — breaks localization and role announcements -->
<button aria-roledescription="attachment button">📎</button>

<!-- RIGHT — let native role announce in user's language -->
<button aria-label="Attach file">📎</button>
```

`aria-roledescription` replaces the role name entirely, breaking localization. Native role names auto-translate; `aria-roledescription` does not. ([Roselli, 2020](https://adrianroselli.com/2020/04/avoid-aria-roledescription.html))

---

## 5. When You Must Use ARIA

ARIA is the right tool when there is genuinely no native HTML equivalent. In these cases, you take full responsibility:

**You must provide:**
1. All required ARIA attributes for the role (see table below)
2. Complete keyboard interaction per the APG pattern
3. Focus management (what happens when the widget opens, closes, or changes state)
4. State updates (toggling `aria-expanded`, `aria-checked`, `aria-selected`, etc.)
5. Correct parent-child role relationships

**The rule:** If you add `role="..."`, you are responsible for implementing every behavior that role implies. ARIA changes semantics only — it adds zero behavior.

---

## 6. Required Attributes Quick Reference

These roles REQUIRE specific attributes. Omitting them produces broken widgets.

| Role | Required Attributes | Common Mistake |
|---|---|---|
| `checkbox` | `aria-checked` (`true`/`false`/`mixed`) | Forgetting `aria-checked` |
| `combobox` | `aria-expanded`, `aria-controls` | Missing `aria-controls` reference |
| `menuitemcheckbox` | `aria-checked` | Same as checkbox |
| `menuitemradio` | `aria-checked` | Same as radio |
| `radio` | `aria-checked` (`true`/`false`) | Not managing group state |
| `slider` | `aria-valuenow` | Missing min/max context |
| `switch` | `aria-checked` (`true`/`false`) | Using `aria-pressed` instead |

**Roles that need an accessible name** (not technically "required" in spec, but broken without one):
- `dialog`, `alertdialog` — use `aria-labelledby` pointing to the heading
- `tabpanel` — use `aria-labelledby` pointing to the associated `tab`
- `region` / `section` — use `aria-label` or `aria-labelledby`

**Parent-child relationships** (must be maintained):
| Parent | Expected Children |
|---|---|
| `tablist` | `tab` |
| `tree` | `treeitem` (possibly grouped) |
| `listbox` | `option` |
| `menu`/`menubar` | `menuitem`, `menuitemcheckbox`, `menuitemradio` |
| `radiogroup` | `radio` |
| `grid` | `row` → `gridcell`/`columnheader`/`rowheader` |

For the complete reference, see: `${CLAUDE_SKILL_DIR}/references/required-aria-attributes.md`

---

## 7. Cross-References

For specific widget implementation patterns, see these companion skills:

- `a11y-combobox` — combobox/autocomplete patterns
- `a11y-tabs` — tab/tablist/tabpanel patterns
- `a11y-dialog` — dialog and alertdialog patterns
- `a11y-menu` — application menu patterns (NOT navigation)
- `a11y-tree` — tree view patterns
- `a11y-grid` — data grid and spreadsheet patterns
- `a11y-accordion` — disclosure/accordion patterns
- `a11y-listbox` — listbox selection patterns

For detailed reference material:

- `${CLAUDE_SKILL_DIR}/references/html-aria-mapping.md` — complete HTML → ARIA role mapping
- `${CLAUDE_SKILL_DIR}/references/five-rules-of-aria.md` — detailed rules with examples
- `${CLAUDE_SKILL_DIR}/references/required-aria-attributes.md` — all required/supported attributes by role
- `${CLAUDE_SKILL_DIR}/references/common-aria-mistakes.md` — anti-patterns with citations
- `${CLAUDE_SKILL_DIR}/references/sources.yaml` — provenance for all cited sources
