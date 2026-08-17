# Common ARIA Mistakes
## Contents

- [1. div or span as Interactive Element (The "Fake Button")](#1-div-or-span-as-interactive-element-the-fake-button)
- [2. aria-label on Non-Interactive Elements](#2-aria-label-on-non-interactive-elements)
- [3. Redundant ARIA (Adding Roles Elements Already Have)](#3-redundant-aria-adding-roles-elements-already-have)
- [4. aria-hidden="true" on Focusable Elements](#4-aria-hiddentrue-on-focusable-elements)
- [5. role="menu" for Site Navigation](#5-rolemenu-for-site-navigation)
- [6. aria-roledescription Overuse](#6-aria-roledescription-overuse)
- [7. Missing Required ARIA Attributes](#7-missing-required-aria-attributes)
- [8. ARIA Labels That Differ from Visible Text](#8-aria-labels-that-differ-from-visible-text)
- [Summary: What LLMs Get Wrong Most Often](#summary-what-llms-get-wrong-most-often)


This reference documents real-world ARIA misuse patterns, drawing from practitioner sources and accessibility auditing experience. These are the mistakes that LLM-generated code makes most frequently.

---

## 1. `<div>` or `<span>` as Interactive Element (The "Fake Button")

**What people do wrong:**
```html
<div class="btn" onclick="handleClick()" role="button">Submit</div>
<span role="link" onclick="navigate('/home')">Home</span>
```

**Why it's wrong:**
- Not focusable by default (needs `tabindex="0"`)
- No keyboard activation (must manually handle Enter and Space)
- No form submission behavior
- No implicit accessible name computation from value/content in all contexts
- Missing native click-on-Enter behavior

As the Accessibility Developer Guide states: "Using ARIA to add missing semantical information is never a good solution. The approach lacks standard functionality like focusability, requires custom JavaScript, breaks browser history, and may lack legacy screen reader support." ([Accessibility Developer Guide, Bad ARIA Practices](https://www.accessibility-developer-guide.com/knowledge/aria/bad-practices/))

**What to do instead:**
```html
<button onclick="handleClick()">Submit</button>
<a href="/home">Home</a>
```

**Source:** [Using ARIA, Rule 1](https://www.w3.org/TR/using-aria/); [APG Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/) — "A role is a promise"

---

## 2. `aria-label` on Non-Interactive Elements

**What people do wrong:**
```html
<div aria-label="User statistics">
  <p>42 users online</p>
</div>
<span aria-label="Important note">Check your email</span>
```

**Why it's wrong:**
- `aria-label` is only reliably supported on interactive elements and landmark roles
- On generic elements like `<div>` and `<span>` (with no role), `aria-label` is ignored by many screen readers
- Creates a false sense of accessibility — developers think it's labeled, but users never hear the label
- The accessible name computation algorithm does not apply `aria-label` to elements with `role="generic"` (which is the implicit role of `<div>` and `<span>`)

**What to do instead:**
```html
<!-- If it needs a label, it needs a role or landmark -->
<section aria-label="User statistics">
  <p>42 users online</p>
</section>

<!-- Or use visible text -->
<div>
  <h2>User Statistics</h2>
  <p>42 users online</p>
</div>
```

**Source:** [WAI-ARIA 1.2, §5.4](https://www.w3.org/TR/wai-aria-1.2/) — naming requirements per role; [ARIA in HTML](https://w3c.github.io/html-aria/) — allowed ARIA attributes per element

---

## 3. Redundant ARIA (Adding Roles Elements Already Have)

**What people do wrong:**
```html
<nav role="navigation">...</nav>
<main role="main">...</main>
<button role="button">Click me</button>
<a href="/home" role="link">Home</a>
<input type="checkbox" role="checkbox">
<ul role="list">...</ul>
```

**Why it's wrong:**
- These elements already have the specified implicit ARIA role
- Redundant ARIA clutters the code and signals misunderstanding
- In rare cases, redundant roles can cause double-announcement in screen readers
- Violates the principle: "Do not change native semantics, unless you really have to" ([Using ARIA, Rule 2](https://www.w3.org/TR/using-aria/))

**What to do instead:**
```html
<nav>...</nav>
<main>...</main>
<button>Click me</button>
<a href="/home">Home</a>
<input type="checkbox">
<ul>...</ul>
```

**Note:** There is one edge case where `<ul role="list">` may be intentional — Safari/VoiceOver removes list semantics from `<ul>` elements styled with `list-style: none`. Adding `role="list"` restores the semantics. This is a known browser behavior, not a spec requirement.

**Source:** [ARIA in HTML](https://w3c.github.io/html-aria/) — implicit role mapping table

---

## 4. `aria-hidden="true"` on Focusable Elements

**What people do wrong:**
```html
<button aria-hidden="true">Close</button>
<div aria-hidden="true">
  <input type="text" placeholder="Search">
  <a href="/help">Help</a>
</div>
```

**Why it's wrong:**
- The element remains in the tab order — keyboard users can focus it
- But screen readers will not announce it — the user lands on something invisible
- This is explicitly prohibited by Using ARIA Rule 4
- The Accessibility Developer Guide notes: "the browser still allows to focus such elements using the Tab key, but because of aria-hidden screen readers will not announce it" ([ADG, Bad ARIA Practices](https://www.accessibility-developer-guide.com/knowledge/aria/bad-practices/))

**What to do instead:**
```html
<!-- If truly hidden, remove from tab order too -->
<button style="display:none">Close</button>
<!-- Or use the inert attribute -->
<div inert>
  <input type="text" placeholder="Search">
  <a href="/help">Help</a>
</div>
<!-- Or use tabindex="-1" if aria-hidden is intentional and temporary -->
<button aria-hidden="true" tabindex="-1">Close</button>
```

**Source:** [Using ARIA, Rule 4](https://www.w3.org/TR/using-aria/); [ADG Bad ARIA Practices](https://www.accessibility-developer-guide.com/knowledge/aria/bad-practices/)

---

## 5. `role="menu"` for Site Navigation

**What people do wrong:**
```html
<nav>
  <ul role="menu">
    <li role="menuitem"><a href="/">Home</a></li>
    <li role="menuitem"><a href="/about">About</a></li>
    <li role="menuitem"><a href="/contact">Contact</a></li>
  </ul>
</nav>
```

**Why it's wrong:**
- ARIA `menu` role is for application-style menus (like a context menu, dropdown action menu, or menubar in a desktop application)
- Site navigation is semantically a list of links, not an application menu
- Using `role="menu"` overrides the list semantics, breaking the parent-child relationship between `<ul>` and `<li>`
- Requires Arrow key navigation instead of Tab, which confuses users expecting standard navigation behavior
- As Make Things Accessible explains: "A role='menu' cannot be an `<li>`'s parent as it's like a different species. When the parent's native semantics are overridden by ARIA, orphaned list items lose their proper structure." This violates WCAG 1.3.1 (Info and Relationships). ([Make Things Accessible](https://www.makethingsaccessible.com/guides/site-navigation-is-not-an-aria-menu/))

**What to do instead:**
```html
<nav aria-label="Main">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>
```

The `<nav>` element provides the `navigation` landmark automatically. No ARIA roles needed.

**Source:** [APG Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/); [Make Things Accessible — Site Navigation Is Not an ARIA Menu](https://www.makethingsaccessible.com/guides/site-navigation-is-not-an-aria-menu/)

---

## 6. `aria-roledescription` Overuse

**What people do wrong:**
```html
<input type="text" aria-roledescription="Only numbers are allowed">
<button aria-roledescription="attachment button">📎</button>
```

**Why it's wrong:**
- `aria-roledescription` replaces the role announcement entirely — the user loses the element type information
- Causes double-announcement in some screen readers (e.g., JAWS on Chrome: "attachment button button")
- Breaks localization — native roles are announced in the user's language, but `aria-roledescription` text stays in whatever language the developer wrote
- Adrian Roselli: "Once you override its role with `aria-roledescription`, they will hear it in whatever language you provided. There is no auto-translation." ([Roselli, 2020](https://adrianroselli.com/2020/04/avoid-aria-roledescription.html))

**What to do instead:**
- Use the correct native element. "HTML has all sorts of built-in features that, when used correctly, are accessible, will localize, and which just work." ([Roselli, 2020](https://adrianroselli.com/2020/04/avoid-aria-roledescription.html))
- If you must override a role description, only do so for generic roles (`group`, `region`) where the default announcement is unhelpful — and test with actual screen readers first.

**Source:** [Adrian Roselli — Avoid aria-roledescription](https://adrianroselli.com/2020/04/avoid-aria-roledescription.html)

---

## 7. Missing Required ARIA Attributes

**What people do wrong:**
```html
<div role="checkbox">Remember me</div>
<!-- Missing aria-checked -->

<div role="slider">Volume</div>
<!-- Missing aria-valuenow, aria-valuemin, aria-valuemax -->

<input role="combobox" type="text">
<!-- Missing aria-expanded, aria-controls -->
```

**Why it's wrong:**
- Several ARIA roles have required states/properties. Without them, the role is incomplete and assistive technology cannot convey the widget state.
- A checkbox without `aria-checked` cannot communicate whether it is checked.
- A slider without `aria-valuenow` cannot communicate the current value.

**What to do instead:**
```html
<div role="checkbox" aria-checked="false" tabindex="0">Remember me</div>

<div role="slider" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100" tabindex="0">Volume</div>

<input role="combobox" type="text" aria-expanded="false" aria-controls="listbox-id">
```

Or better — use native elements:
```html
<label><input type="checkbox"> Remember me</label>
<label for="vol">Volume</label>
<input type="range" id="vol" min="0" max="100" value="50">
```

**Source:** [WAI-ARIA 1.2, §5.4](https://www.w3.org/TR/wai-aria-1.2/) — required states/properties per role

---

## 8. ARIA Labels That Differ from Visible Text

**What people do wrong:**
```html
<button aria-label="Submit form data">Send</button>
<a href="/contact" aria-label="Get in touch with our team">Contact Us</a>
```

**Why it's wrong:**
- Violates WCAG 2.5.3 (Label in Name) — the accessible name must contain the visible text
- Voice control users say "click Send" but the accessible name is "Submit form data" — the command fails
- Creates confusion when sighted users and screen reader users discuss the same interface

**What to do instead:**
```html
<button>Send</button>
<!-- If more context needed, use aria-describedby -->
<button aria-describedby="submit-help">Send</button>
<span id="submit-help" hidden>Submits the contact form</span>
```

**Source:** [WCAG 2.1, SC 2.5.3 Label in Name](https://www.w3.org/WAI/WCAG21/Understanding/label-in-name.html)

---

## Summary: What LLMs Get Wrong Most Often

Ranked by frequency in LLM-generated code:

1. **Redundant ARIA** — adding `role="button"` to `<button>`, `role="navigation"` to `<nav>`, etc.
2. **`<div>`/`<span>` as buttons/links** — using ARIA roles instead of native elements
3. **`aria-label` on non-interactive generic elements** — labels that no screen reader will announce
4. **Missing required attributes** — `role="checkbox"` without `aria-checked`
5. **`role="menu"` for navigation** — using application menu semantics for site nav
6. **`aria-hidden="true"` on focusable elements** — hiding from AT but not from keyboard
7. **Visible text mismatch** — `aria-label` that doesn't contain the visible button text
8. **`aria-roledescription` overuse** — replacing useful role information with custom strings
