---
name: live-regions
description: Guides ARIA live region usage for dynamic content announcements. Auto-invokes when creating notifications, toasts, status messages, loading indicators, search result counters, form validation summaries, or SPA route change announcers. Covers timing requirements, politeness levels, implicit live regions, and common pitfalls.
allowed-tools: Read, Glob, Grep
---

# ARIA Live Regions

> "The live region container must exist in the DOM *before* content is injected into it."
> — [TetraLogical](https://tetralogical.com/blog/2024/05/01/why-are-my-live-regions-not-working/), [MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions), [Sara Soueidan](https://www.sarasoueidan.com/blog/accessible-notifications-with-aria-live-regions-part-1/)

Live regions allow screen readers to announce dynamic content changes without moving focus. They are the foundation of accessible notifications, status messages, and real-time updates. The single most important rule: the container must exist before the content.

---

## 1. The Timing Rule

Screen readers register live regions through the accessibility API when they first appear in the DOM. If you create a container and populate it in the same operation, the screen reader has no prior state to diff against and **the update is silently dropped**.

### What works

```html
<!-- In initial markup: empty container, already monitored -->
<div id="status" aria-live="polite"></div>
```

```javascript
// Later, on user action:
document.getElementById('status').textContent = '5 results found';
// Screen reader announces: "5 results found"
```

### What fails

```javascript
// Creating and populating in the same operation — NOT announced
const div = document.createElement('div');
div.setAttribute('aria-live', 'polite');
div.textContent = 'This will be missed';
document.body.appendChild(div);
```

### If you must create dynamically

Wait at least 100ms before injecting content. This gives the accessibility API time to register the region. ([TetraLogical](https://tetralogical.com/blog/2024/05/01/why-are-my-live-regions-not-working/))

```javascript
const region = document.createElement('div');
region.setAttribute('aria-live', 'polite');
document.body.appendChild(region);

setTimeout(() => {
  region.textContent = 'Now this will be announced';
}, 100);
```

### Framework-specific timing trap

**Never conditionally render live region containers.** Using `*ngIf` (Angular), `v-if` (Vue), or `{condition && <div>}` (React) destroys the element when the condition is false. When recreated, initial content is missed.

**Fix:** Use `[hidden]`, `v-show`, or `hidden={!condition}` to preserve DOM presence. ([dev.to](https://dev.to/dkoppenhagen/when-your-live-region-isnt-live-fixing-aria-live-in-angular-react-and-vue-1g0j))

```tsx
// WRONG: conditional rendering destroys the live region
{showMessage && <div aria-live="polite">{message}</div>}

// RIGHT: element stays in DOM
<div aria-live="polite" hidden={!showMessage}>{message}</div>
```

---

## 2. Politeness Levels

### `aria-live="polite"` — the default choice

Announcements wait until the user is idle. Use for the vast majority of notifications.

**Use for:** search result counts, form submission success, status updates, cart updates, content feed changes.

### `aria-live="assertive"` — use sparingly

Interrupts the user immediately. Can be disruptive and disorienting, especially for users with cognitive disabilities. ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions), [Sara Soueidan](https://www.sarasoueidan.com/blog/accessible-notifications-with-aria-live-regions-part-1/))

**Use for:** error messages requiring immediate attention, session timeout warnings, security alerts, connection loss.

**Never use for:** routine status updates, non-critical notifications, frequent updates.

### `aria-live="off"` — the default value

Updates are only exposed when user focus is on or inside the element. Used implicitly by `role="marquee"` and `role="timer"` for continuously updating content that should not interrupt. ([WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/#attrs_liveregions))

---

## 3. Implicit Live Regions

Certain ARIA roles have built-in live region semantics. Do not add redundant `aria-live` attributes unless noted.

| Role | Implicit `aria-live` | Implicit `aria-atomic` | Notes |
|------|---------------------|----------------------|-------|
| `alert` | `assertive` | `true` | Do NOT also add `aria-live="assertive"` — causes double-speaking in VoiceOver iOS. ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)) |
| `status` | `polite` | `true` | For advisory info. `<output>` has implicit `role="status"`. |
| `log` | `polite` | `false` | For sequential info (chat, error logs). Add redundant `aria-live="polite"` for older screen reader compatibility. |
| `timer` | `off` | — | Not announced by default (would be overwhelming). |
| `marquee` | `off` | — | Non-essential scrolling content. Not announced by default. |

### Alert pattern rules ([APG](https://www.w3.org/WAI/ARIA/apg/patterns/alert/))

- Alerts must NOT affect keyboard focus.
- Do NOT use alerts for messages before page load completes (they won't be announced).
- Do NOT use alerts that auto-dismiss (risks WCAG 2.2.3 violation — "No Timing").
- If user interaction is required, use the Alert Dialog pattern instead.
- Excessive alerts harm users with cognitive disabilities.

---

## 4. `aria-atomic` and `aria-relevant`

### `aria-atomic`

Controls whether AT presents the entire element or only changed nodes. ([WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/#attrs_liveregions))

| Value | Behavior | Default |
|-------|----------|---------|
| `false` | Only modified content is announced | **Yes** |
| `true` | Complete element content presented as a single unit | |

**Use `aria-atomic="true"` when** partial updates are meaningless without context (e.g., a clock showing "34" instead of "17:34").

### `aria-relevant`

Specifies what types of changes trigger announcements.

| Value | Meaning |
|-------|---------|
| `additions` | Element nodes added |
| `removals` | Element nodes removed |
| `text` | Text content changed |
| `all` | Equivalent to `additions removals text` |

Default: `additions text`.

**Warning:** Both `aria-relevant` and `aria-atomic` have inconsistent cross-platform support. Do not rely on them as the sole mechanism for critical behavior. ([Sara Soueidan](https://www.sarasoueidan.com/blog/accessible-notifications-with-aria-live-regions-part-1/))

### `aria-busy`

Set `aria-busy="true"` before batch updates, then `false` when complete, so only the final state is announced. Support is inconsistent — provide fallback behavior. ([Sara Soueidan](https://www.sarasoueidan.com/blog/accessible-notifications-with-aria-live-regions-part-1/))

---

## 5. Recipes Summary

Quick patterns for common use cases. Full implementations with framework variants are in [references/recipes.md](references/recipes.md).

### Form validation errors

```html
<div id="form-errors" role="alert" aria-atomic="true"></div>
```
Use `role="alert"` (implicit assertive) because errors are time-sensitive. `aria-atomic="true"` ensures the full error summary is read.

### Search results count

```html
<div id="search-status" role="status"></div>
```
Use `role="status"` (implicit polite) — informational, not urgent.

### Loading states

```html
<div id="loading-region" aria-live="polite" aria-busy="false">
  <p>Content here</p>
</div>
```
Set `aria-busy="true"` during updates, `false` when complete. Because `aria-busy` support is inconsistent, also announce "Loading..." as a polite message.

### SPA route changes

```html
<div id="route-announcer" aria-live="polite" class="sr-only"></div>
```
On route change, update with `"Navigated to ${pageTitle}"`. Complement with focus management — move focus to the new page's `<h1>` (with `tabindex="-1"`). ([Almero Steyn](https://almerosteyn.com/2017/03/accessible-react-navigation))

### Chat / message log

```html
<div role="log" aria-live="polite" aria-relevant="additions">
  <!-- New messages appended here -->
</div>
```
`role="log"` with `aria-relevant="additions"` announces only new messages.

---

## 6. Common Mistakes

### 1. Creating and populating simultaneously

The live region must exist before content injection. Creating `<div aria-live="polite">Message</div>` and appending it in one step silently fails. ([TetraLogical](https://tetralogical.com/blog/2024/05/01/why-are-my-live-regions-not-working/), [MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions))

### 2. Live region spam

Rapid updates queue announcements users cannot skip. Known NVDA bug: polite region changes repeated up to 6x in Chrome. Debounce updates and prefer `polite` over `assertive`. ([NVDA #7996](https://github.com/nvaccess/nvda/issues/7996))

### 3. Assertive overuse

Using `assertive` for non-critical notifications constantly interrupts users. Reserve for genuine emergencies. ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions), [Sara Soueidan](https://www.sarasoueidan.com/blog/accessible-notifications-with-aria-live-regions-part-1/))

### 4. Conditional rendering in frameworks

`*ngIf`, `v-if`, and `{condition && <div>}` destroy the live region element. Use CSS hiding to preserve DOM presence. ([dev.to](https://dev.to/dkoppenhagen/when-your-live-region-isnt-live-fixing-aria-live-in-angular-react-and-vue-1g0j))

### 5. Combining `role="alert"` with `aria-live="assertive"`

`role="alert"` already implies `aria-live="assertive"`. Adding the explicit attribute causes double announcement in VoiceOver iOS. ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions))

### 6. Using `display:none` on live regions

Screen readers ignore `display: none` and `visibility: hidden`. Use the sr-only/visually-hidden CSS pattern (clip, 1px dimensions) for visually-hidden live regions.

For the complete list with remediation details, see [references/common-mistakes.md](references/common-mistakes.md).

---

## 7. Cross-References

- **form-a11y** — form validation patterns, error association with `aria-describedby`
- **focus-management** — focus handling for SPA route changes, modal dialogs
- **aria-decision-framework** — when to use ARIA roles vs native HTML elements

For detailed reference material:

- [references/recipes.md](references/recipes.md) — full recipes with framework variants (Angular, React, Vue)
- [references/screen-reader-behavior.md](references/screen-reader-behavior.md) — cross-platform behavior matrix
- [references/common-mistakes.md](references/common-mistakes.md) — anti-patterns with citations and fixes
- [references/sources.yaml](references/sources.yaml) — provenance for all cited sources
