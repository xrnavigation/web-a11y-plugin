---
name: focus-management
description: Guides focus management for dynamic web applications — modal focus trapping, focus restoration, SPA route changes, dynamic content focus recovery, focus-not-obscured (WCAG 2.2), and skip navigation. Auto-invokes when creating modals, dialogs, SPAs, route handlers, or dynamically adding/removing DOM content.
allowed-tools: Read, Glob, Grep
compatibility: "Claude Code, Codex CLI, Gemini CLI"
---

# Focus Management

> "When navigation happens without page reloads, screen readers don't automatically announce changes, and when DOM updates happen dynamically, focus can get lost."
> — [Deque, Accessibility Tips in Single-Page Applications](https://www.deque.com/blog/accessibility-tips-in-single-page-applications/)

Focus management is the discipline of ensuring keyboard and screen reader users always know where they are, can reach what they need, and never get stranded. Every modal, route change, deletion, and insertion is a potential focus loss — and focus loss means a broken experience.

---

## 1. Modal Focus Trapping

When a modal opens, focus must stay inside it. Background content must become unreachable.

### Preferred: the `inert` attribute

Apply `inert` to sibling containers of the modal. The browser removes the inert subtree from the accessibility tree, prevents focus, and blocks hit-testing.

```html
<div id="app" inert><!-- page content --></div>
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirm Action</h2>
  <!-- modal content -->
</div>
```

For native `<dialog>` opened via `showModal()`, the browser handles inertness automatically — no manual `inert` attribute needed.

Browser support: Chrome 102+, Safari 15.5+, Firefox 112+.

Source: [WHATWG HTML Spec — The inert attribute](https://html.spec.whatwg.org/multipage/interaction.html#the-inert-attribute)

### Fallback: sentinel focus trap

Place invisible focusable sentinels at the start and end of the modal. When focus reaches a sentinel, redirect to the opposite end. This requires maintaining a list of focusable elements:

```
a[href], button:not([disabled]), input:not([disabled]),
select:not([disabled]), textarea:not([disabled]),
[tabindex]:not([tabindex="-1"]), audio[controls],
video[controls], details > summary,
[contenteditable]:not([contenteditable="false"])
```

### Where to place initial focus

There is no single correct answer — it depends on context ([Adrian Roselli, Dialog Focus in Screen Readers](https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html)):

- **Small confirmation dialogs** → Focus the cancel/close button. Never the destructive action.
- **Large form dialogs** → Focus the heading or first input field.
- **General rule** → Never place initial focus on a destructive action button.

See: `${CLAUDE_SKILL_DIR}/references/modal-focus-trapping.md`

---

## 2. Focus Restoration

When a modal closes, focus must return to the element that triggered it.

### Standard pattern

Store a reference to `document.activeElement` before opening the modal. On close, call `.focus()` on that stored reference.

```js
// Before opening
const trigger = document.activeElement;

// On close
trigger?.focus();
```

### Edge case: trigger removed from DOM

If the triggering element was removed while the modal was open (e.g., the modal confirmed a deletion that removes the trigger's row), attempting to focus it fails silently and focus falls to `<body>`, stranding keyboard users.

**Fallback chain (in order):**
1. Previous sibling's equivalent control
2. The containing element
3. `<main>` or the skip-nav target
4. **Never** let focus fall to `<body>`

> "When the close button is hidden the body element will be focused by default, which will force keyboard users to step through the page manually to find where they left off."
> — [Medium, Stop Breaking Modal Accessibility](https://medium.com/@alexdev82/stop-breaking-modal-accessibility-the-focus-management-mistake-90-of-devs-make-9605bad927e2)

Source: [Bootstrap Issue #12364](https://github.com/twbs/bootstrap/issues/12364)

---

## 3. SPA Route Changes

Traditional page loads reset focus to the document top and trigger screen reader announcements. Client-side navigation does neither. You must fix both.

### Focus the `<h1>`

On each route change, move focus to the page's `<h1>`. This mimics traditional page load behavior and causes screen readers to announce the new page.

```html
<h1 tabindex="-1" id="page-title">Dashboard</h1>
```

```js
// After route change completes
document.querySelector('h1')?.focus();
```

The `tabindex="-1"` makes the heading programmatically focusable without entering the tab order.

**Do not focus on initial page load** — let users explore from the top naturally.

Source: [BBC GEL Technical Guide: Routing](https://bbc.github.io/gel/foundations/routing/)

### Additional requirements

1. **Update `document.title`** on every route change — screen readers announce title changes.
2. **Use `aria-current="page"`** on the active navigation link.
3. **Announce the route change** via an ARIA live region (used by Next.js and Gatsby):

```html
<div aria-live="assertive" class="sr-only" id="route-announcer"></div>
```

Source: [Deque, Accessibility Tips in Single-Page Applications](https://www.deque.com/blog/accessibility-tips-in-single-page-applications/)

See: `${CLAUDE_SKILL_DIR}/references/spa-route-changes.md`

---

## 4. Dynamic Content

### Item deletion

When deleting an item from a group ([Adrian Roselli, Where to Put Focus When Deleting a Thing](https://adrianroselli.com/2023/08/where-to-put-focus-when-deleting-a-thing.html)):

- Move focus to the **previous item's equivalent control** (e.g., previous row's delete button).
- If the first item is deleted, focus the container element.
- For single dismissals (notifications, banners), restore focus to what had focus before the item appeared.

**Safeguards:**
1. The element receiving focus must have a useful accessible name — generic "Delete" without context confuses screen reader users.
2. Position focus carefully to prevent accidental double-deletions if users press Enter twice.
3. Never let focus jump to the page top or fall on non-focusable elements.

### Content insertion

- **User-initiated** (e.g., "Add item" button) → Focus the new content or its first interactive element.
- **Asynchronous** (e.g., new message in a feed) → Use `aria-live` regions. Do not steal focus — interrupting the user's task with a focus shift is hostile.

### Toasts and notifications

- Use `role="status"` or `aria-live="polite"` — announce without stealing focus.
- For urgent alerts, use `role="alert"` or `aria-live="assertive"`.
- Only move focus to a toast if it contains interactive elements requiring immediate action (e.g., an "Undo" button with a time limit).

---

## 5. Focus Not Obscured (WCAG 2.2)

### SC 2.4.11 — Focus Not Obscured (Minimum, Level AA)

> "When a user interface component receives keyboard focus, the component is not entirely hidden due to author-created content."

Sticky headers, footers, banners, and cookie dialogs must not entirely cover focused elements. This is the most common failure.

Source: [W3C, Understanding SC 2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)

### SC 2.4.12 — Focus Not Obscured (Enhanced, Level AAA)

The enhanced level requires **complete visibility** — no part of the focused component may be hidden.

### CSS solution: `scroll-padding`

Apply `scroll-padding` to the scroll container to create buffer space around sticky elements:

```css
html, body {
  scroll-padding-top: 6rem;    /* height of sticky header */
  scroll-padding-bottom: 4rem; /* height of sticky footer */
}
```

For conditionally-visible sticky content (e.g., dismissible cookie banners):

```css
:is(html, body):has(aside.cookie-banner) {
  scroll-padding-bottom: 6rem;
}
```

**Prefer `scroll-padding` over `scroll-margin`** — `scroll-margin` has browser incompatibilities, particularly in Safari ([TetraLogical, Sticky content: focus in view](https://tetralogical.com/blog/2023/06/08/focus-in-view/)).

Use `rem` or `em` units for responsive scaling with zoom/text sizing.

Source: [W3C Technique C43](https://www.w3.org/WAI/WCAG22/Techniques/css/C43)

---

## 6. Skip Navigation Links

Skip links satisfy **WCAG 2.4.1 Bypass Blocks (Level A)** — they let keyboard users skip repetitive content.

### Implementation

```html
<body>
  <a href="#maincontent" class="skip-link">Skip to main content</a>
  <header><!-- navigation --></header>
  <main id="maincontent" tabindex="-1">
    <!-- page content -->
  </main>
</body>
```

The skip link must be the **first interactive element** in the page.

### CSS: hidden until focused

```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  z-index: 100;
  padding: 8px;
  background: #000;
  color: #fff;
}
.skip-link:focus {
  top: 0;
}
```

**Do not use** `display: none`, `visibility: hidden`, or the `hidden` attribute — these remove the link from keyboard navigation entirely.

### SPA considerations

In SPAs, the `<main>` target must have `tabindex="-1"` and remain valid across client-side route changes.

Source: [WebAIM, Skip Navigation Links](https://webaim.org/techniques/skipnav/)

---

## 7. Common Mistakes

1. **Removing focus outline globally** — `*:focus { outline: none }` destroys keyboard accessibility. Go beyond browser defaults, not below them. ([Roselli, Keep the Focus Outline](https://adrianroselli.com/2014/06/keep-focus-outline.html))

2. **Not restoring focus on modal close** — Focus falls to `<body>`, stranding keyboard users. ([Medium, Stop Breaking Modal Accessibility](https://medium.com/@alexdev82/stop-breaking-modal-accessibility-the-focus-management-mistake-90-of-devs-make-9605bad927e2))

3. **Placing initial focus on destructive actions** — Opening a delete confirmation and focusing the "Delete" button risks accidental activation. ([Roselli, Dialog Focus in Screen Readers](https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html))

4. **No focus management on SPA route changes** — Screen readers don't announce client-side navigation. ([Deque, Accessibility Tips in SPAs](https://www.deque.com/blog/accessibility-tips-in-single-page-applications/))

5. **Using `display: none` on skip links** — Removes the link from keyboard navigation, defeating its purpose. ([WebAIM, Skip Navigation Links](https://webaim.org/techniques/skipnav/))

6. **Ignoring the trigger-removed edge case** — Focus falls to `<body>` when the modal trigger was removed during the modal's lifetime. ([Bootstrap #12364](https://github.com/twbs/bootstrap/issues/12364))

7. **Relying solely on `:focus-visible`** — Voice users, touch users, and sighted screen reader users may not see `:focus-visible` styles. Use `:focus` as the baseline. ([Roselli, Where to Put Focus When Deleting a Thing](https://adrianroselli.com/2023/08/where-to-put-focus-when-deleting-a-thing.html))

8. **Not using `scroll-padding` with sticky headers** — Focused elements disappear under sticky content, failing WCAG 2.4.11. ([TetraLogical, Sticky content: focus in view](https://tetralogical.com/blog/2023/06/08/focus-in-view/))

9. **Testing with only one screen reader** — Screen readers have significant inconsistencies in dialog focus announcements. ([Roselli, Dialog Focus in Screen Readers](https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html))

See: `${CLAUDE_SKILL_DIR}/references/common-mistakes.md`

---

## 8. Cross-References

For related patterns, see these companion skills:

- `a11y-dialog` — dialog and alertdialog implementation patterns
- `css-a11y` — CSS techniques for accessibility (including focus styles)
- `live-regions` — ARIA live region patterns for dynamic announcements

For detailed reference material:

- `${CLAUDE_SKILL_DIR}/references/modal-focus-trapping.md` — inert, sentinels, and initial focus placement
- `${CLAUDE_SKILL_DIR}/references/spa-route-changes.md` — route change patterns with framework examples
- `${CLAUDE_SKILL_DIR}/references/framework-patterns.md` — React, Vue, and Angular focus management
- `${CLAUDE_SKILL_DIR}/references/common-mistakes.md` — anti-patterns with citations
- `${CLAUDE_SKILL_DIR}/references/sources.yaml` — provenance for all cited sources
