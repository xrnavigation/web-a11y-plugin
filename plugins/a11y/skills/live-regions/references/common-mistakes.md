# Common Live Region Mistakes
## Contents

- [1. Creating and Populating Simultaneously](#1-creating-and-populating-simultaneously)
- [2. Live Region Spam (Over-Announcing)](#2-live-region-spam-over-announcing)
- [3. Assertive Overuse](#3-assertive-overuse)
- [4. Conditional Rendering in Frameworks](#4-conditional-rendering-in-frameworks)
- [5. Combining role="alert" with aria-live="assertive"](#5-combining-rolealert-with-aria-liveassertive)
- [6. Transient Announcements with No Fallback](#6-transient-announcements-with-no-fallback)
- [7. Using display:none or visibility:hidden on Live Regions](#7-using-displaynone-or-visibilityhidden-on-live-regions)


Anti-patterns with citations and remediation.

---

## 1. Creating and Populating Simultaneously

**The mistake:** Creating a `<div aria-live="polite">Message</div>` and appending it to the DOM in one operation.

**Why it fails:** Screen readers register live regions via the accessibility API when they first appear. With no prior state to diff against, the update is silently dropped.

**Fix:** Place an empty container in the initial markup. Inject content later.

```html
<!-- In initial markup -->
<div id="status" aria-live="polite"></div>
```

```javascript
// Later
document.getElementById('status').textContent = 'Update announced';
```

Sources: [TetraLogical](https://tetralogical.com/blog/2024/05/01/why-are-my-live-regions-not-working/), [MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)

---

## 2. Live Region Spam (Over-Announcing)

**The mistake:** Updating a live region on every keystroke, every API poll, or every animation frame.

**Why it fails:** Each update queues an announcement. Rapid updates create a backlog the user cannot skip or silence. NVDA has a known bug where polite region changes repeat up to 6 times in Chrome. ([NVDA #7996](https://github.com/nvaccess/nvda/issues/7996))

**Fix:** Debounce updates. Ask whether each update truly needs to be announced.

```javascript
// BAD: announces on every keystroke
input.addEventListener('input', () => {
  status.textContent = `${results.length} results`;
});

// GOOD: debounced
let timer;
input.addEventListener('input', () => {
  clearTimeout(timer);
  timer = setTimeout(() => {
    status.textContent = `${results.length} results`;
  }, 500);
});
```

---

## 3. Assertive Overuse

**The mistake:** Using `aria-live="assertive"` or `role="alert"` for non-critical notifications like "Settings saved" or "Item added to cart."

**Why it fails:** Assertive announcements interrupt users immediately, clearing the speech queue. Frequent interruptions are disorienting, especially for users with cognitive disabilities.

**Fix:** Use `aria-live="polite"` or `role="status"` for anything that is not a genuine emergency (errors, security alerts, session expiry).

Sources: [MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions), [Sara Soueidan](https://www.sarasoueidan.com/blog/accessible-notifications-with-aria-live-regions-part-1/)

---

## 4. Conditional Rendering in Frameworks

**The mistake:** Using `*ngIf` (Angular), `v-if` (Vue), or `{condition && <div>}` (React) to toggle live region visibility.

**Why it fails:** These directives remove the element from the DOM entirely. When recreated, the screen reader must re-register the region, and initial content is missed.

**Fix:** Use CSS-based hiding that preserves DOM presence.

| Framework | Wrong | Right |
|-----------|-------|-------|
| Angular | `@if (show) { <div aria-live> }` | `<div aria-live [hidden]="!show">` |
| React | `{show && <div aria-live>}` | `<div aria-live hidden={!show}>` |
| Vue | `<div v-if="show" aria-live>` | `<div v-show="show" aria-live>` |

Source: [dev.to](https://dev.to/dkoppenhagen/when-your-live-region-isnt-live-fixing-aria-live-in-angular-react-and-vue-1g0j)

---

## 5. Combining `role="alert"` with `aria-live="assertive"`

**The mistake:** Writing `<div role="alert" aria-live="assertive">`.

**Why it fails:** `role="alert"` already implies `aria-live="assertive"`. Adding the explicit attribute causes VoiceOver on iOS to announce the content twice.

**Fix:** Use `role="alert"` alone. Do not add `aria-live`.

```html
<!-- WRONG -->
<div role="alert" aria-live="assertive">Error occurred</div>

<!-- RIGHT -->
<div role="alert">Error occurred</div>
```

Source: [MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)

---

## 6. Transient Announcements with No Fallback

**The mistake:** Relying solely on live region announcements to communicate important information, with no persistent visual or programmatic alternative.

**Why it fails:** Live region announcements are fire-and-forget. Once spoken, they are gone. Users who miss them (distracted, volume low, switched apps) cannot retrieve the message.

**Fix:** Provide persistent alternatives — visible status text, a notification center, or a message history.

Source: [Sara Soueidan](https://www.sarasoueidan.com/blog/accessible-notifications-with-aria-live-regions-part-1/)

---

## 7. Using `display:none` or `visibility:hidden` on Live Regions

**The mistake:** Hiding a live region with `display: none` or `visibility: hidden` to make it visually hidden.

**Why it fails:** Screen readers ignore elements hidden with these CSS properties. The live region is effectively disabled.

**Fix:** Use the sr-only / visually-hidden CSS pattern:

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

This keeps the element in the accessibility tree while hiding it visually.
