---
name: a11y-accordion
description: Guides accessible accordion and disclosure implementation. Auto-invokes when creating accordions, collapsible sections, expandable panels, or disclosure widgets. Covers native <details>/<summary> vs ARIA accordion, the APG accordion pattern, and the disclosure pattern.
allowed-tools: Read, Glob, Grep
compatibility: "Claude Code, Codex CLI, Gemini CLI"
---

# Accessible Accordion & Disclosure Implementation

> "No ARIA is better than Bad ARIA."
> — [APG Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)

An accordion is a vertically stacked set of interactive headings, each controlling a content panel. A disclosure is simpler: a single button that shows/hides one block of content. These are different patterns with different requirements.

---

## 1. Decision: Native `<details>`/`<summary>` vs ARIA Accordion

Use this decision tree before reaching for ARIA.

| Situation | Use | Why |
|---|---|---|
| Single show/hide toggle | `<details>`/`<summary>` | Built-in, no JS, works without ARIA. ([HTML Spec](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element)) |
| Independent collapsible sections, no grouping needed | `<details>`/`<summary>` | Progressive enhancement, works without JS. |
| Related sections needing group semantics | ARIA accordion | Adjacent `<details>` lack group semantics. ([Roselli 2023](https://adrianroselli.com/2023/08/progressively-enhanced-html-accordion.html)) |
| Heading navigation on triggers required | ARIA accordion | Headings inside `<summary>` are flattened to presentational role. ([Roselli 2019](https://adrianroselli.com/2019/04/details-summary-are-not-insert-control-here.html); [O'Hara 2018](https://www.scottohara.me/blog/2018/09/03/details-and-summary.html)) |
| Arrow-key navigation between headers desired | ARIA accordion | Native `<details>` only supports Enter/Space. |
| Complex panels with nested headings/landmarks | ARIA accordion | `role="region"` with `aria-labelledby` provides structure. ([APG](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)) |

**Hybrid approach:** Start with `<details>`/`<summary>` for no-JS baseline, then enhance with JS: wrap in a container with `role="group"` and `aria-labelledby`, add exclusive-open behavior. ([Roselli 2023](https://adrianroselli.com/2023/08/progressively-enhanced-html-accordion.html))

---

## 2. Native `<details>`/`<summary>` Quick Reference

### What It Gives You

- **Toggle behavior** without JavaScript — `<summary>` triggers show/hide of sibling content.
- **`open` attribute** reflects state; fires a `toggle` event on change.
- **`name` attribute** for exclusive accordion — `<details>` elements sharing a `name` form a mutual-exclusion group. Opening one closes others. ([MDN Blog](https://developer.mozilla.org/en-US/blog/html-details-exclusive-accordions/))

```html
<details name="faq">
  <summary>Question 1</summary>
  <p>Answer 1</p>
</details>
<details name="faq">
  <summary>Question 2</summary>
  <p>Answer 2</p>
</details>
```

**`name` attribute browser support (all stable):** Chrome 120+, Safari 17.2+, Firefox 130+. ([Chrome for Developers](https://developer.chrome.com/docs/css-ui/exclusive-accordion))

### Limitations

1. **Headings inside `<summary>` are flattened.** `<summary>` maps to button role; nested headings lose heading semantics in most screen readers. ([Roselli 2019](https://adrianroselli.com/2019/04/details-summary-are-not-insert-control-here.html))
2. **No arrow-key navigation** between summaries.
3. **No grouping semantics.** A set of `<details>` is not announced as a group.
4. **Inconsistent role announcements** across screen readers. See `${CLAUDE_SKILL_DIR}/references/screen-reader-behavior.md`.

Full details: `${CLAUDE_SKILL_DIR}/references/native-details-summary.md`

---

## 3. Accordion vs Disclosure

| Criterion | Disclosure | Accordion |
|-----------|-----------|-----------|
| Sections | One (standalone) | Multiple (related set) |
| Grouping | None | Required (`role="group"` or wrapper) |
| Heading structure | Not needed | Headers wrap triggers |
| Arrow-key navigation | No | Optional but recommended |
| Mutual exclusivity | No | Typically yes |
| Use case | "Read more", help text, single FAQ | FAQ list, settings categories, stacked sections |

> "An accordion is more than a few disclosure widgets or `<details>`/`<summary>` elements one after another."
> — [Roselli 2020](https://adrianroselli.com/2020/05/disclosure-widgets.html)

### Disclosure Pattern (APG)

A button with `aria-expanded` that shows/hides content. No heading wrapper, no grouping, no arrow keys. ([APG Disclosure Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/))

```html
<button aria-expanded="false" aria-controls="help-text">Help</button>
<div id="help-text" hidden>
  <p>Helpful information here.</p>
</div>
```

---

## 4. ARIA Accordion Pattern

Source: [APG Accordion Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)

### Required Structure

```html
<!-- WRONG — no heading, no aria-expanded, div as trigger -->
<div class="accordion">
  <div class="header" onclick="toggle()">Section 1</div>
  <div class="panel">Content</div>
</div>

<!-- RIGHT -->
<div role="group" aria-labelledby="acc-label">
  <h3 id="acc-label" class="sr-only">Frequently Asked Questions</h3>

  <h3>
    <button
      id="acc-btn-1"
      aria-expanded="false"
      aria-controls="acc-panel-1"
    >Section 1</button>
  </h3>
  <div
    id="acc-panel-1"
    role="region"
    aria-labelledby="acc-btn-1"
    hidden
  >
    <p>Panel content.</p>
  </div>
</div>
```

### Required Attributes

| Attribute | Element | Requirement |
|-----------|---------|-------------|
| `role="button"` or native `<button>` | Header trigger | Required |
| Heading element (`<h2>`-`<h6>`) or `role="heading"` + `aria-level` | Wrapper around button | Required |
| `aria-expanded="true/false"` | Button | Required |
| `aria-controls="PANEL_ID"` | Button | Required |
| `aria-disabled="true"` | Button | Only when panel cannot be collapsed |
| `role="region"` | Panel | Optional; **avoid with 6+ panels** (landmark proliferation) |
| `aria-labelledby="BUTTON_ID"` | Region | Required when `role="region"` is used |

### Structural Rules

- The button must be the **only interactive element** inside the heading.
- Native `<h2>`-`<h6>` elements are preferred over `role="heading"` + `aria-level`.
- `role="region"` is useful when panels contain headings or nested interactive content, but creates landmark proliferation with many panels.

---

## 5. Keyboard Interaction Summary

| Key | Accordion Behavior |
|-----|--------------------|
| Enter / Space | Toggle panel (expand/collapse) |
| Tab / Shift+Tab | Standard sequential focus navigation |
| Down Arrow (optional) | Next header; wraps last to first |
| Up Arrow (optional) | Previous header; wraps first to last |
| Home (optional) | First header |
| End (optional) | Last header |

Native `<details>`/`<summary>` supports only Enter/Space and Tab. No arrow-key navigation.

Full keyboard spec: `${CLAUDE_SKILL_DIR}/references/keyboard-interaction.md`

---

## 6. Common Mistakes

### 6.1 Headings Inside `<summary>`

```html
<!-- WRONG — heading semantics destroyed -->
<details>
  <summary><h3>FAQ Item</h3></summary>
  <p>Answer</p>
</details>

<!-- RIGHT (native) — no heading in summary -->
<details>
  <summary>FAQ Item</summary>
  <p>Answer</p>
</details>

<!-- RIGHT (ARIA) — heading wraps button -->
<h3><button aria-expanded="false" aria-controls="p1">FAQ Item</button></h3>
<div id="p1" role="region" aria-labelledby="..." hidden>Answer</div>
```

Headings inside `<summary>` are flattened to presentational role. Users cannot navigate to them via heading shortcuts. ([Roselli 2019](https://adrianroselli.com/2019/04/details-summary-are-not-insert-control-here.html); [O'Hara 2018](https://www.scottohara.me/blog/2018/09/03/details-and-summary.html))

### 6.2 Links as Disclosure Triggers

```html
<!-- WRONG — link sets navigation expectation -->
<a href="#" onclick="toggle()">Show details</a>

<!-- RIGHT -->
<button aria-expanded="false" aria-controls="details-1">Show details</button>
```

Disclosure triggers must be buttons. Links signal navigation, not toggle. ([Roselli 2020](https://adrianroselli.com/2020/05/disclosure-widgets.html))

### 6.3 Adjacent `<details>` Called "Accordion" Without Grouping

```html
<!-- WRONG — no group semantics -->
<details><summary>Q1</summary><p>A1</p></details>
<details><summary>Q2</summary><p>A2</p></details>

<!-- RIGHT — wrap in labeled group -->
<div role="group" aria-labelledby="faq-heading">
  <h2 id="faq-heading">FAQ</h2>
  <details name="faq"><summary>Q1</summary><p>A1</p></details>
  <details name="faq"><summary>Q2</summary><p>A2</p></details>
</div>
```

Adjacent `<details>` lack group semantics. Wrap in a container with `role="group"` and `aria-labelledby`. ([Roselli 2023](https://adrianroselli.com/2023/08/progressively-enhanced-html-accordion.html))

### 6.4 Adding `role="button"` to `<summary>`

```html
<!-- WRONG — suppresses state announcements in VoiceOver -->
<details>
  <summary role="button">Toggle</summary>
  <p>Content</p>
</details>

<!-- RIGHT — summary already has implicit button behavior -->
<details>
  <summary>Toggle</summary>
  <p>Content</p>
</details>
```

Native `<summary>` already has button-like behavior. Adding `role="button"` can suppress expanded/collapsed state in VoiceOver/Safari. ([O'Hara 2018](https://www.scottohara.me/blog/2018/09/03/details-and-summary.html))

### 6.5 `role="region"` on All Panels in Large Accordions

```html
<!-- WRONG with 6+ sections — landmark proliferation -->
<div role="region" aria-labelledby="h1">...</div>
<div role="region" aria-labelledby="h2">...</div>
<!-- ... 8 more regions ... -->

<!-- RIGHT — omit role="region" for large accordions -->
<div id="panel-1" aria-labelledby="btn-1" hidden>...</div>
```

Too many landmarks makes landmark navigation useless. APG recommends avoiding `role="region"` when there are 6 or more panels. ([APG Accordion Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/))

### 6.6 Hidden Content Still in Accessibility Tree

```html
<!-- WRONG — visually hidden but still announced -->
<div class="panel" style="position: absolute; left: -9999px">Content</div>

<!-- RIGHT — properly hidden -->
<div class="panel" hidden>Content</div>
<!-- or -->
<div class="panel" style="display: none">Content</div>
```

If content is meant to be hidden, hide it from everyone. Off-screen positioning leaves content in the accessibility tree. ([O'Hara 2017](https://www.scottohara.me/blog/2017/10/25/accordion-release.html))

Full list: `${CLAUDE_SKILL_DIR}/references/common-mistakes.md`

---

## 7. Cross-References

- `aria-decision-framework` — check whether you need ARIA at all (use native HTML first)
- `${CLAUDE_SKILL_DIR}/references/native-details-summary.md` — full native element guide
- `${CLAUDE_SKILL_DIR}/references/keyboard-interaction.md` — complete keyboard spec
- `${CLAUDE_SKILL_DIR}/references/screen-reader-behavior.md` — per-AT behavior differences
- `${CLAUDE_SKILL_DIR}/references/common-mistakes.md` — expanded anti-patterns with citations
- `${CLAUDE_SKILL_DIR}/references/sources.yaml` — provenance for all cited sources
