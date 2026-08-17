# Common Accordion & Disclosure Mistakes
## Contents

- [1. Headings Inside summary](#1-headings-inside-summary)
- [2. Links as Disclosure Triggers](#2-links-as-disclosure-triggers)
- [3. Adjacent details Without Grouping](#3-adjacent-details-without-grouping)
- [4. Content Visible Only on Hover/Focus](#4-content-visible-only-on-hoverfocus)
- [5. Visually Hidden Content Still in Accessibility Tree](#5-visually-hidden-content-still-in-accessibility-tree)
- [6. role="region" on All Panels (6+ Sections)](#6-roleregion-on-all-panels-6-sections)
- [7. Adding role="button" to summary](#7-adding-rolebutton-to-summary)
- [8. Disclosed Content Not Following Trigger in DOM](#8-disclosed-content-not-following-trigger-in-dom)


## 1. Headings Inside `<summary>`

**Problem:** `<summary>` maps to a button role. Headings nested inside it are flattened to presentational semantics. Users cannot navigate to them via heading shortcuts (H key) in most screen reader + browser combinations.

```html
<!-- WRONG -->
<details>
  <summary><h3>FAQ Item</h3></summary>
  <p>Answer</p>
</details>

<!-- RIGHT (native) -->
<details>
  <summary>FAQ Item</summary>
  <p>Answer</p>
</details>

<!-- RIGHT (ARIA, when heading semantics needed) -->
<h3>
  <button aria-expanded="false" aria-controls="panel-1">FAQ Item</button>
</h3>
<div id="panel-1" role="region" aria-labelledby="..." hidden>
  <p>Answer</p>
</div>
```

Source: [Roselli 2019](https://adrianroselli.com/2019/04/details-summary-are-not-insert-control-here.html), [O'Hara 2018](https://www.scottohara.me/blog/2018/09/03/details-and-summary.html)

---

## 2. Links as Disclosure Triggers

**Problem:** Links (`<a>`) set a navigation expectation. Disclosure triggers must be buttons because they toggle visibility, not navigate.

```html
<!-- WRONG -->
<a href="#" onclick="toggle()">Show details</a>
<div id="details">...</div>

<!-- RIGHT -->
<button aria-expanded="false" aria-controls="details">Show details</button>
<div id="details" hidden>...</div>
```

Source: [Roselli 2020](https://adrianroselli.com/2020/05/disclosure-widgets.html)

---

## 3. Adjacent `<details>` Without Grouping

**Problem:** Multiple `<details>` elements placed next to each other are not announced as a related group. Screen reader users cannot perceive they form a set.

```html
<!-- WRONG — no group semantics -->
<details><summary>Q1</summary><p>A1</p></details>
<details><summary>Q2</summary><p>A2</p></details>
<details><summary>Q3</summary><p>A3</p></details>

<!-- RIGHT — wrap in labeled group -->
<div role="group" aria-labelledby="faq-heading">
  <h2 id="faq-heading">Frequently Asked Questions</h2>
  <details name="faq"><summary>Q1</summary><p>A1</p></details>
  <details name="faq"><summary>Q2</summary><p>A2</p></details>
  <details name="faq"><summary>Q3</summary><p>A3</p></details>
</div>
```

Source: [Roselli 2023](https://adrianroselli.com/2023/08/progressively-enhanced-html-accordion.html)

---

## 4. Content Visible Only on Hover/Focus

**Problem:** Disclosed content must remain visible once revealed. Content that disappears when the pointer or focus leaves violates user expectations and WCAG 1.4.13 (Content on Hover or Focus).

```javascript
// WRONG — content disappears on blur
button.addEventListener('blur', () => {
  panel.hidden = true;
});

// RIGHT — content stays visible until explicitly toggled
button.addEventListener('click', () => {
  const expanded = button.getAttribute('aria-expanded') === 'true';
  button.setAttribute('aria-expanded', String(!expanded));
  panel.hidden = expanded;
});
```

Source: [Roselli 2020](https://adrianroselli.com/2020/05/disclosure-widgets.html)

---

## 5. Visually Hidden Content Still in Accessibility Tree

**Problem:** Moving content off-screen (e.g., `left: -9999px`) hides it visually but leaves it in the accessibility tree. Screen readers announce it even though sighted users cannot see it.

```html
<!-- WRONG — visually hidden but still announced -->
<div class="panel" style="position: absolute; left: -9999px">
  Hidden content
</div>

<!-- RIGHT — properly hidden from everyone -->
<div class="panel" hidden>Hidden content</div>
<!-- or -->
<div class="panel" style="display: none">Hidden content</div>
```

Source: [O'Hara 2017](https://www.scottohara.me/blog/2017/10/25/accordion-release.html)

---

## 6. `role="region"` on All Panels (6+ Sections)

**Problem:** Each `role="region"` creates a landmark. With 6 or more panels, landmark navigation becomes cluttered and useless.

```html
<!-- WRONG with many sections — landmark proliferation -->
<div role="region" aria-labelledby="h1">Panel 1</div>
<div role="region" aria-labelledby="h2">Panel 2</div>
<div role="region" aria-labelledby="h3">Panel 3</div>
<!-- ... 5 more ... -->

<!-- RIGHT — omit role="region" when many panels exist -->
<div id="panel-1" aria-labelledby="btn-1" hidden>Panel 1</div>
<div id="panel-2" aria-labelledby="btn-2" hidden>Panel 2</div>
```

Source: [APG Accordion Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)

---

## 7. Adding `role="button"` to `<summary>`

**Problem:** Native `<summary>` already has implicit button-like behavior. Explicitly adding `role="button"` can suppress the expanded/collapsed state announcement in VoiceOver/Safari.

```html
<!-- WRONG — redundant and harmful -->
<details>
  <summary role="button">Toggle section</summary>
  <p>Content</p>
</details>

<!-- RIGHT — let native semantics work -->
<details>
  <summary>Toggle section</summary>
  <p>Content</p>
</details>
```

Source: [O'Hara 2018](https://www.scottohara.me/blog/2018/09/03/details-and-summary.html)

---

## 8. Disclosed Content Not Following Trigger in DOM

**Problem:** If disclosed content is placed elsewhere in the DOM (e.g., in a portal or at the end of `<body>`), reading order and focus order become illogical. The content must immediately follow its trigger.

```html
<!-- WRONG — content far from trigger -->
<button aria-expanded="true" aria-controls="panel-remote">Show</button>
<!-- ... other content ... -->
<div id="panel-remote">Panel content way down here</div>

<!-- RIGHT — content immediately follows trigger -->
<button aria-expanded="true" aria-controls="panel-1">Show</button>
<div id="panel-1">Panel content right here</div>
```

Source: [Roselli 2020](https://adrianroselli.com/2020/05/disclosure-widgets.html)
