# Common Cognitive Accessibility Mistakes

Expanded anti-patterns with code examples and fixes. Each is cited to primary sources.

---

## 1. Relying Solely on Color to Indicate Errors

Color-vision deficiency affects approximately 350 million people worldwide.

```html
<!-- WRONG — red border only -->
<input style="border-color: red">

<!-- RIGHT — text + border + icon -->
<input style="border-color: red" aria-invalid="true" aria-describedby="err1">
<span id="err1" role="alert">&#9888; Email: must include an @ symbol.</span>
```

Always combine: text description + visual indicator (border/icon) + ARIA markup.
([NN/g](https://www.nngroup.com/articles/error-message-guidelines/))

---

## 2. Premature Error Display

Showing errors while the user is still typing or on first blur of an empty field (before submission attempt).

```javascript
// WRONG — validates on every keystroke
input.addEventListener('input', validate);

// WRONG — shows "required" error on first blur of untouched field
input.addEventListener('blur', () => {
  if (!input.value) showError('Required');
});

// RIGHT — validate on submission; after first submission failure,
// validate on blur for fields the user has attempted
form.addEventListener('submit', validateAll);
```

Premature validation punishes exploration and increases cognitive load. Users need space to think before the interface judges them.
([NN/g](https://www.nngroup.com/articles/error-message-guidelines/))

---

## 3. Generic Error Messages

```html
<!-- WRONG -->
<div class="error">An error occurred.</div>
<div class="error">Invalid input.</div>
<div class="error">Please check your entries.</div>

<!-- RIGHT -->
<div class="error" role="alert">
  Email: must include an @ symbol. Example: name@example.com
</div>
```

Users with cognitive disabilities cannot infer which field has the problem or what to do about it from generic messages. Name the field, describe the issue, suggest the fix.
([WCAG SC 3.3.3](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html))

---

## 4. Auto-Submitting Forms on Input Change

```html
<!-- WRONG — auto-submits on selection -->
<select onchange="this.form.submit()">
  <option>United States</option>
  <option>Canada</option>
</select>

<!-- RIGHT — explicit submit -->
<select id="country">
  <option>United States</option>
  <option>Canada</option>
</select>
<button type="submit">Apply</button>
```

Keyboard users cycling through options with arrow keys trigger submission on every option. Screen reader users navigating options cannot preview choices. Violates SC 3.2.2.
([WCAG SC 3.2.2](https://www.w3.org/WAI/WCAG22/Understanding/on-input.html))

---

## 5. Context Changes on Focus

```html
<!-- WRONG — opens dialog when field receives focus -->
<input onfocus="openHelpDialog()">

<!-- WRONG — navigates on focus -->
<a onfocus="window.location = this.href">Link</a>

<!-- RIGHT — context changes only on explicit activation -->
<input>
<button onclick="openHelpDialog()">Get help</button>
```

Keyboard users tab through elements to understand the page. If focus triggers context changes, navigation becomes impossible. Violates SC 3.2.1.
([WCAG SC 3.2.1](https://www.w3.org/WAI/WCAG22/Understanding/on-focus.html))

---

## 6. Silent Session Expiry

```javascript
// WRONG — expires without warning, discards data
setTimeout(() => {
  window.location = '/login';
}, 30 * 60 * 1000);

// RIGHT — warns before expiry, preserves data
setTimeout(() => {
  showTimeoutWarning(); // alertdialog with extend option
}, 28 * 60 * 1000);
```

Users who step away to collect documents, take medication, or rest lose all their work. Violates SC 2.2.1.
([WCAG SC 2.2.1](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html))

---

## 7. Inconsistent Help Placement

```html
<!-- Page A: help in header -->
<header><a href="/help">Help</a></header>
<main>...</main>

<!-- Page B: help in footer (WRONG — different position) -->
<header>...</header>
<main>...</main>
<footer><a href="/help">Help</a></footer>
```

Help mechanisms must appear in the same relative DOM order across all pages in a set. Users who learned to find help in the header should not have to hunt for it in the footer on the next page. Violates SC 3.2.6.
([WCAG SC 3.2.6](https://www.w3.org/WAI/WCAG22/Understanding/consistent-help.html))

---

## 8. Inconsistent Terminology

```html
<!-- Page A -->
<a href="/cart">Shopping Cart (3 items)</a>

<!-- Page B (WRONG — different term for same concept) -->
<a href="/cart">Your Basket (3 items)</a>

<!-- RIGHT — same term everywhere -->
<a href="/cart">Shopping Cart (3 items)</a>
```

Using different words for the same concept forces users to re-learn vocabulary on every page. People with cognitive disabilities may not realize "Cart" and "Basket" refer to the same thing.
([A11Y Collective](https://www.a11y-collective.com/blog/cognitive-accessibility/))

---

## 9. No Progress Indication in Multi-Step Processes

```html
<!-- WRONG — no indication of progress -->
<h1>Shipping Address</h1>

<!-- RIGHT — step count in heading and title -->
<title>Step 2 of 4: Shipping Address - Checkout</title>
<h1>Shipping Address (Step 2 of 4)</h1>
```

Users with memory deficits lose track of where they are and how much remains. Without step indicators, abandonment rates increase significantly.
([WebAIM](https://webaim.org/articles/cognitive/design))

---

## 10. Destroying User Input on Validation Error

```javascript
// WRONG — clears the form on error
if (!isValid(form)) {
  form.reset();
  showErrors();
}

// RIGHT — preserve input, show errors inline
if (!isValid(form)) {
  showErrorsInline(); // fields retain their values
}
```

Clearing fields forces users to re-enter everything from scratch. Users with memory or attention difficulties may not remember what they entered. Always preserve input and let users correct in place.
([NN/g](https://www.nngroup.com/articles/error-message-guidelines/))
