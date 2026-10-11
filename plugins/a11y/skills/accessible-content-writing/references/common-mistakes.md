# Content mistakes and corrections

## Label-looking text without association

A visible label must be associated with its control; a neighboring `<label>` with no `for` and no nested input does not do that. ([WAI labels](https://www.w3.org/WAI/tutorials/forms/labels/))

```html
<!-- Wrong -->
<label>Email address</label><input type="email" placeholder="Email">
<!-- Right -->
<label for="email">Email address</label>
<p id="email-hint">For example, name@example.com</p>
<input id="email" type="email" aria-describedby="email-hint">
```

## Generic destination text

SC 2.4.4 (A) allows programmatically determined context; independently meaningful links are a project preference and support link-list navigation. Do not call every “Read more” an automatic failure without inspecting context. ([Link Purpose in Context](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html))

```html
<!-- Weak outside surrounding context -->
<a href="/report">Read more</a>
<!-- Clearer -->
<a href="/report">Read the emissions report</a>
```

## Visual headings without structure

Use a heading for a real section and ranks reflecting relationships. Avoid downward rank skips as authoring guidance; do not invent a universal WCAG h1 count or ban normal return to a higher-level heading. ([WAI headings](https://www.w3.org/WAI/tutorials/page-structure/headings/))

```html
<!-- Wrong: visually presents a section heading as ordinary prose. -->
<p class="large-bold">Required documents</p>
<!-- Right: meaningful section heading. -->
<h2>Required documents</h2>
```

## Error copy without a usable correction

Name the field and problem; give a known correction unless it would jeopardize security or purpose. A fixed count of icons or words does not establish comprehension. ([Error Suggestion](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html))

```text
Wrong: Invalid input.
Right: Enter a date before today.
```

Test labels, headings, links, and corrections with the actual content and supported reading/input modes. Do not claim exact screen-reader speech from a markup example.
