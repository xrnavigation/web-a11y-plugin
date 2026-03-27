# The Rules of ARIA Use

Source: [Using ARIA — W3C Working Group Note](https://www.w3.org/TR/using-aria/)

The "Using ARIA" W3C note defines rules for correct ARIA usage. These rules encode the fundamental principle that ARIA is a supplement, not a replacement, for native HTML semantics.

---

## Rule 1: Use Native HTML Instead of ARIA When Possible

> "If you _can_ use a native HTML element or attribute with the semantics and behavior you require **already built in**, instead of re-purposing an element and adding an ARIA role, state or property to make it accessible, **then do so**."
>
> — Using ARIA, Rule 1

### Explanation

Native HTML elements come with built-in:
- Keyboard interaction (e.g., `<button>` responds to Enter and Space)
- Focus management (e.g., `<a href>` is focusable by default)
- State communication (e.g., `<details>` communicates open/closed)
- Semantics understood by all assistive technologies
- Localization (role names announced in the user's language)

ARIA provides none of these behaviors — it only changes what is communicated to the accessibility tree. When you use ARIA instead of native HTML, you must manually implement every behavior the native element provides for free.

### When native HTML may not suffice

The spec acknowledges three situations where ARIA may be needed:
1. The feature exists in HTML but lacks adequate browser/AT accessibility support
2. Visual design constraints genuinely prevent using the native element (even with CSS)
3. The required feature does not exist in HTML at all

### Examples

```html
<!-- WRONG: div with ARIA role -->
<div role="button" tabindex="0" onclick="handleClick()">Save</div>

<!-- RIGHT: native button -->
<button onclick="handleClick()">Save</button>

<!-- WRONG: span with link role -->
<span role="link" tabindex="0" onclick="navigate()">Home</span>

<!-- RIGHT: native anchor -->
<a href="/home">Home</a>

<!-- WRONG: div with checkbox role -->
<div role="checkbox" aria-checked="false" tabindex="0">Agree</div>

<!-- RIGHT: native checkbox -->
<input type="checkbox" id="agree">
<label for="agree">Agree</label>
```

---

## Rule 2: Do Not Change Native Semantics

> "Do not change native semantics, unless you really have to."
>
> — Using ARIA, Rule 2

### Explanation

Every HTML element has implicit semantics. Adding an ARIA role overrides those semantics entirely. This can break assistive technology expectations.

### Examples

```html
<!-- WRONG: heading used as a tab -->
<h2 role="tab">Settings</h2>
<!-- The heading semantics are lost. Screen reader users lose the heading in heading navigation. -->

<!-- RIGHT: heading inside a tab container -->
<div role="tab"><h2>Settings</h2></div>
<!-- The heading remains a heading; the container is the tab. -->

<!-- WRONG: list used as a tablist -->
<ul role="tablist">
  <li role="tab">Tab 1</li>
</ul>
<!-- List semantics are destroyed. -->

<!-- RIGHT: div-based tablist -->
<div role="tablist">
  <button role="tab">Tab 1</button>
</div>
```

---

## Rule 3: All Interactive ARIA Controls Must Be Keyboard Accessible

> "All interactive ARIA controls must be usable with the keyboard."
>
> — Using ARIA, Rule 3

### Explanation

If a user can click, tap, drag, or otherwise interact with a widget using a pointing device, it must also be fully operable via keyboard. This is not optional — it is a requirement of WCAG 2.1 Success Criterion 2.1.1 (Keyboard).

Specific keyboard requirements by role:
- `role="button"`: must respond to Enter and Space
- `role="link"`: must respond to Enter
- `role="checkbox"`, `role="switch"`: must respond to Space
- `role="slider"`: must respond to Arrow keys
- `role="tab"`: must respond to Arrow keys (within tablist)
- `role="combobox"`: must respond to Arrow keys, Enter, Escape
- `role="menu"`: must respond to Arrow keys, Enter, Escape

### Example

```html
<!-- WRONG: div button with no keyboard support -->
<div role="button" onclick="save()">Save</div>
<!-- Cannot be focused. Cannot be activated with keyboard. -->

<!-- RIGHT: div button with full keyboard support -->
<div role="button" tabindex="0"
     onclick="save()"
     onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();save()}">
  Save
</div>
<!-- Focusable and keyboard-activatable. But still worse than <button>. -->

<!-- BEST: just use a button -->
<button onclick="save()">Save</button>
```

---

## Rule 4: Do Not Use `role="presentation"` or `aria-hidden="true"` on Focusable Elements

> "Do not use `role='presentation'` or `aria-hidden='true'` on a **focusable** element."
>
> — Using ARIA, Rule 4

### Explanation

Using `role="presentation"` or `aria-hidden="true"` on a focusable element creates a disconnect: keyboard users can focus the element, but screen reader users cannot perceive it. The user tabs to something invisible, with no announcement.

This also applies to parent elements. If you set `aria-hidden="true"` on a container, all focusable descendants become invisible to assistive technology but remain in the tab order.

### Examples

```html
<!-- WRONG: hidden but focusable -->
<button aria-hidden="true">Close</button>
<!-- Keyboard users tab to it; screen readers say nothing. -->

<!-- WRONG: hidden container with focusable children -->
<div aria-hidden="true">
  <a href="/settings">Settings</a>
  <button>Save</button>
</div>
<!-- Both the link and button are still focusable but invisible to AT. -->

<!-- RIGHT: truly hide if not needed -->
<button style="display:none">Close</button>
<!-- OR use inert attribute -->
<div inert>
  <a href="/settings">Settings</a>
  <button>Save</button>
</div>
```

---

## Rule 5: All Interactive Elements Must Have an Accessible Name

> "All interactive elements must have an accessible name."
>
> — Using ARIA, Rule 5

### Explanation

Every interactive element needs a name that assistive technology can announce. Without a name, a screen reader user encounters an unlabeled control — they know there is a button, but not what it does.

Accessible names come from (in priority order per the accessible name computation algorithm):
1. `aria-labelledby` (references another element's text)
2. `aria-label` (string attribute)
3. Native labeling (`<label>`, `alt`, element text content)
4. `title` attribute (last resort, often not accessible)

### Examples

```html
<!-- WRONG: icon button with no name -->
<button><svg><!-- icon --></svg></button>
<!-- Screen reader: "button" — no indication of purpose. -->

<!-- RIGHT: icon button with aria-label -->
<button aria-label="Close"><svg><!-- close icon --></svg></button>

<!-- RIGHT: icon button with visually-hidden text -->
<button>
  <svg aria-hidden="true"><!-- close icon --></svg>
  <span class="visually-hidden">Close</span>
</button>

<!-- WRONG: text input with no label -->
<input type="text" placeholder="Search...">
<!-- Placeholder is not a reliable accessible name. -->

<!-- RIGHT: text input with label -->
<label for="search">Search</label>
<input type="text" id="search">
```

---

## Summary for Agents

When generating code, apply these rules as a checklist:

1. **Can a native HTML element do this?** → Use it. Do not reach for ARIA.
2. **Are you overriding native semantics?** → Stop. Restructure instead.
3. **Does your custom widget work with keyboard only?** → If not, it's broken.
4. **Is anything focusable but hidden from AT?** → Fix the mismatch.
5. **Does every interactive element have a name?** → Verify before shipping.
