# Live region recipes

## Search status

```html
<form id="search-form">
  <label for="query">Search products</label>
  <input id="query" name="q" type="search">
  <button>Search</button>
</form>
<p id="result-status" role="status"></p>
<div id="results"></div>
```

Keep the status node mounted, render results, then update useful text after the
current request completes. Guard stale/aborted responses in the application's
request lifecycle. Do not move focus merely because results arrived. Status has
polite and atomic defaults
([WAI-ARIA status](https://www.w3.org/TR/wai-aria-1.2/#status)).

## Form feedback

```html
<label for="email">Email</label>
<input id="email" type="email" aria-invalid="true" aria-describedby="email-error">
<p id="email-error">Enter an email address like name@example.com.</p>
```

Associate visible field errors; choose a focused summary or first invalid field
for a failed submit. Use a separate live summary only when the tested flow needs
it. Avoid also announcing the same paragraph through an alert on every field
([WAI validation](https://www.w3.org/WAI/tutorials/forms/validation/)).

## Framework status

```tsx
function SearchStatus({ message }: { message: string }) {
  return <p role="status">{message}</p>;
}
```

Mount before the request, with an empty message. Do not conditionally mount or
hide the active announcer. If visual hiding is needed, use a tested visually
hidden utility that keeps accessibility exposure
([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)).

## Routes and chat

Coordinate route feedback with the router's focus/title behavior; avoid duplicate
speech when a heading already identifies the new view. For sequential messages,
a named `role="log"` expresses polite non-atomic additions. Test whether only
new messages are presented rather than replaying history
([WAI-ARIA log](https://www.w3.org/TR/wai-aria-1.2/#log)).
