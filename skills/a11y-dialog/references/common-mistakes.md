# Common Dialog Accessibility Mistakes

## 1. Not Blocking Screen Reader Virtual Cursor from Background

**The problem:** A CSS overlay and JavaScript focus trapping prevent mouse and keyboard interaction with background content, but screen reader virtual cursors bypass both. Users navigating with NVDA/JAWS arrow keys or VoiceOver swipe gestures can reach background content.

**The fix:** Use one of:
- Native `<dialog>.showModal()` (automatic background inertness)
- `inert` attribute on all sibling content
- `aria-hidden="true"` on all sibling content (legacy approach)

```html
<!-- WRONG — focus trap + CSS overlay, screen reader escapes -->
<div class="overlay"></div>
<div role="dialog" aria-modal="true">...</div>
<main>Background content still reachable by virtual cursor</main>

<!-- RIGHT — inert blocks everything -->
<main inert>Background content</main>
<div role="dialog" aria-modal="true">...</div>
```

*Sources: [MDN — ARIA dialog role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/dialog_role); [Common Accessibility Issues with Modals](https://blog.openreplay.com/common-accessibility-issues-modals-fix/)*

---

## 2. Always Focusing the First Interactive Element

**The problem:** "Focus the first focusable element" is a widespread but harmful oversimplification. It leads to:
- Destructive actions receiving focus on confirmation dialogs
- "I agree" buttons getting focus on legal agreements
- Text fields gaining focus in unexpected modals (triggering soft keyboards, single-keystroke deletion)

**The fix:** Focus placement depends on dialog purpose. See the decision table in `focus-management-rules.md`.

```html
<!-- WRONG — destructive action gets focus -->
<dialog>
  <h2>Delete all files?</h2>
  <button autofocus>Delete everything</button>
  <button>Cancel</button>
</dialog>

<!-- RIGHT — safe action gets focus -->
<dialog>
  <h2>Delete all files?</h2>
  <button>Delete everything</button>
  <button autofocus>Cancel</button>
</dialog>
```

*Source: [Adrian Roselli — Where to Put Focus When Opening a Modal Dialog](https://adrianroselli.com/2025/06/where-to-put-focus-when-opening-a-modal-dialog.html)*

---

## 3. Missing Accessible Name

**The problem:** Adding `role="dialog"` (or using `<dialog>`) without `aria-labelledby` or `aria-label`. Screen readers announce "dialog" with zero context about what the dialog is for.

**The fix:** Always add `aria-labelledby` referencing the visible title. Use `aria-label` only when there is no visible title.

```html
<!-- WRONG -->
<dialog>
  <h2>Confirm Payment</h2>
</dialog>

<!-- RIGHT -->
<dialog aria-labelledby="pay-title">
  <h2 id="pay-title">Confirm Payment</h2>
</dialog>
```

Note: Native `<dialog>` does NOT automatically set `aria-labelledby`. This is a manual requirement.

*Source: [MDN — ARIA dialog role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/dialog_role)*

---

## 4. Not Restoring Focus on Close

**The problem:** When a dialog closes without returning focus to the trigger element, keyboard and screen reader users lose their place in the document. Focus falls to `<body>`, forcing the user to navigate from the top of the page.

**The fix:** Store a reference to the trigger element before opening and restore focus on close.

```javascript
// Store before opening
const trigger = document.activeElement;
dialog.showModal();

// Restore on close
dialog.addEventListener('close', () => {
  if (trigger && document.contains(trigger)) {
    trigger.focus();
  } else {
    // Trigger removed — focus logically related element
    fallbackElement.focus();
  }
});
```

*Sources: [APG Dialog (Modal) Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/); [Scott O'Hara — accessible_modal_window](https://github.com/scottaohara/accessible_modal_window)*

---

## 5. Focus Escaping the Dialog

**The problem:** Tab or Shift+Tab moves focus to background content, breaking the modal contract. Users interact with content they shouldn't be able to reach.

**The fix:** For native `<dialog>.showModal()`, this is handled automatically. For custom dialogs, use `inert` on background content OR implement a JavaScript focus trap that wraps Tab at the boundaries.

*Source: [APG Dialog (Modal) Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)*

---

## 6. Using `alertdialog` for Non-Urgent Content

**The problem:** The `alertdialog` role triggers system alert sounds and interrupts screen reader flow. Using it for settings panels, forms, or informational content causes unnecessary noise and disruption.

**The fix:** Reserve `alertdialog` for:
- Destructive action confirmations ("Delete this?")
- Error acknowledgments
- Critical notifications requiring immediate response

Everything else is `dialog`.

*Source: [APG Alert and Message Dialogs](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/)*

---

## 7. Adding Redundant `aria-modal` to Native `<dialog>`

**The problem:** When `<dialog>` is opened via `.showModal()`, `aria-modal="true"` is implicit. Adding it manually is unnecessary and suggests misunderstanding of the native element.

**The fix:** Omit `aria-modal` when using native `<dialog>` with `.showModal()`. Only add it for custom dialogs using `role="dialog"`.

```html
<!-- UNNECESSARY -->
<dialog aria-modal="true">...</dialog>

<!-- CORRECT — aria-modal is implicit with .showModal() -->
<dialog>...</dialog>
```

*Source: [Adrian Roselli — Dialog Focus in Screen Readers](https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html)*

---

## 8. Relying Only on Automated Testing

**The problem:** Automated testing tools can identify structural issues (missing attributes, role violations) but cannot validate:
- Correct focus placement for context
- Screen reader announcement quality
- Focus restoration behavior
- Virtual cursor containment
- Keyboard interaction flow

**The fix:** Supplement automated checks with manual testing. At minimum: NVDA + Firefox, keyboard-only navigation, and VoiceOver + Safari.

*Source: [Common Accessibility Issues with Modals](https://blog.openreplay.com/common-accessibility-issues-modals-fix/)*
