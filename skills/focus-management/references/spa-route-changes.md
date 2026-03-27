# SPA Route Change Focus — Reference

## The Problem

Traditional multi-page websites reset focus to the document top on each page load. Screen readers announce the new page title automatically. SPAs broke both behaviors: client-side navigation does not trigger a page load, so:

1. Screen readers do not announce the new page.
2. Focus remains on the now-stale navigation link (or is lost entirely).
3. Keyboard users have no indication that content changed.

Source: [Deque — Accessibility Tips in Single-Page Applications](https://www.deque.com/blog/accessibility-tips-in-single-page-applications/)

---

## Recommended Pattern: Focus the `<h1>`

User testing found the most well-received approach is to shift focus to the `<h1>` heading on each route change. This:

- Puts the user at the logical top of the new content.
- Causes screen readers to announce the page heading.
- Mimics traditional page load behavior.

```html
<h1 tabindex="-1" id="page-title">Dashboard</h1>
```

```js
// After route change and DOM update
document.querySelector('h1')?.focus();
```

The `tabindex="-1"` makes the heading programmatically focusable without entering the normal tab order.

**Do not focus on initial page load** — on first load, let users explore from the top naturally. Focus management is only needed on subsequent client-side navigations.

Source: [BBC GEL Technical Guide: Routing](https://bbc.github.io/gel/foundations/routing/)

---

## Announcement via Live Region

Some implementations use an ARIA live region to announce the new page instead of (or in addition to) moving focus:

```html
<div aria-live="assertive" class="sr-only" id="route-announcer"></div>
```

```js
// On route change
document.getElementById('route-announcer').textContent = `Navigated to ${pageTitle}`;
```

This approach avoids a "jarring" focus shift while still informing screen reader users. Next.js and Gatsby both use this pattern internally.

Source: [Deque — Accessibility Tips in Single-Page Applications](https://www.deque.com/blog/accessibility-tips-in-single-page-applications/)

---

## Checklist

On every client-side route change:

1. **Update `document.title`** — screen readers announce title changes.
2. **Move focus to `<h1>`** (with `tabindex="-1"`) or announce via live region.
3. **Set `aria-current="page"`** on the active navigation link; remove from others.
4. **Maintain browser back/forward** through proper history management (`pushState`/`replaceState`).
5. **Do not focus on initial load** — only on subsequent navigations.

---

## Framework Examples

### React (with React Router or similar)

```jsx
const headingRef = useRef(null);

useEffect(() => {
  headingRef.current?.focus();
}, [location.pathname]);

return <h1 ref={headingRef} tabIndex={-1}>{pageTitle}</h1>;
```

### Vue (with Vue Router)

```js
import { nextTick } from 'vue';

router.afterEach(() => {
  nextTick(() => {
    document.querySelector('h1')?.focus();
  });
});
```

Vue updates the DOM asynchronously. Attempting to focus immediately after a reactive data change fails because the DOM has not updated yet. Always use `nextTick`.

Sources:
- [marcus.io — Accessible routing with vue.js](https://marcus.io/blog/accessible-routing-vuejs)
- [MDN — Vue refs and lifecycle methods for focus management](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Frameworks_libraries/Vue_refs_focus_management)
