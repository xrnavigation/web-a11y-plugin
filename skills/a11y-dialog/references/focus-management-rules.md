# Focus Management Rules for Dialogs

## Where Focus Goes on Open

Focus placement is context-dependent. Adrian Roselli's guidance (June 2025): "Blanket statements about where to put focus when opening a modal dialog are wrong, including this one."

### Decision Table

| Dialog Type | Focus Target | Rationale | Implementation |
|------------|--------------|-----------|----------------|
| Short informational message | Close button | Users can quickly dismiss; `aria-describedby` on dialog references message text | `<button autofocus>Close</button>` |
| Long/interactive content | Dialog element itself or primary heading | Users need to orient before interacting | Set `tabindex="-1"` on heading, focus programmatically |
| Irreversible/consequential action | Least destructive option (Cancel/Close) | Prevents accidental activation of destructive action | `<button autofocus>Cancel</button>` |
| Brief familiar form (e.g., login) | First relevant form field | Reduces interaction steps | Only if user intentionally triggered the dialog |
| Long/unfamiliar form | Dialog or heading, NOT the form field | Prevents premature keyboard/soft-keyboard activation; lets user orient | Focus heading with `tabindex="-1"` |
| Legal/financial agreements | Do NOT focus "I agree" | Prevents accidental acceptance | Focus dialog element or explanatory heading |

*Source: [Adrian Roselli — Where to Put Focus When Opening a Modal Dialog](https://adrianroselli.com/2025/06/where-to-put-focus-when-opening-a-modal-dialog.html)*

### Dark Pattern Warning

**Do NOT auto-focus text fields in unexpected/unsolicited modals.** This causes:
- Single-keystroke deletion of existing content on mobile
- Unexpected soft keyboard appearing on touch devices
- Disorientation for screen reader users

*Source: [Adrian Roselli — Where to Put Focus When Opening a Modal Dialog](https://adrianroselli.com/2025/06/where-to-put-focus-when-opening-a-modal-dialog.html)*

### Native `<dialog>` Focus Algorithm

The spec defines automatic dialog focusing steps:
1. If any element inside the dialog has `autofocus`, that element receives focus
2. Otherwise, focus delegates to the dialog's focus delegate
3. If neither applies, the dialog element itself receives focus

Use `autofocus` explicitly for predictable placement.

*Source: [HTML Spec — The dialog element](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)*

---

## Tab Cycling (Focus Trapping)

For modal dialogs, focus must not escape the dialog boundary:

- **Tab** from last focusable element wraps to first focusable element
- **Shift+Tab** from first focusable element wraps to last focusable element
- The dialog container itself (`tabindex="-1"`) is excluded from the tab cycle
- Native `<dialog>.showModal()` handles this automatically via top-layer inertness

### Focusable Element Detection

Programmatically identifying all focusable elements is imperfect. Elements that may be missed:
- `<object>`, `<embed>`
- `<details>` without `<summary>`
- `<iframe>` elements
- Custom elements with `delegatesFocus`

*Sources: [APG Dialog (Modal) Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/); [a11y-dialog — Focus Considerations](https://a11y-dialog.netlify.app/advanced/focus-considerations)*

---

## Focus Restoration on Close

Focus returns to whichever element had focus before the dialog opened (typically the trigger button).

### Implementation Pattern

```javascript
// Store trigger before opening
const trigger = document.activeElement;
dialog.showModal();

// Restore on close
dialog.addEventListener('close', () => {
  trigger?.focus();
});
```

### Edge Cases

| Scenario | Action |
|----------|--------|
| Trigger element no longer exists in DOM | Focus a logically related element (e.g., parent container, sibling) |
| Workflow suggests different target | Focus contextually appropriate element (e.g., newly created table row after table-editing dialog) |
| Dialog opened programmatically (no trigger) | Focus the element that makes most sense in context |

*Sources: [APG Dialog (Modal) Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/); [a11y-dialog — Focus Considerations](https://a11y-dialog.netlify.app/advanced/focus-considerations)*

---

## Special Cases

### `role="document"` Inside Dialog

Kitty Giraudel's a11y-dialog library uses `role="document"` on the inner dialog window. This allows NVDA users to use browse mode within dialog content (NVDA normally switches to forms/application mode inside dialogs, which limits navigation).

*Source: [a11y-dialog — Markup](https://a11y-dialog.netlify.app/usage/markup)*

### Elements Outside Dialog DOM

Some UI patterns (tooltips via Popper.js, portaled dropdowns) render elements outside the dialog DOM tree. The a11y-dialog library provides `data-a11y-dialog-ignore-focus-trap` for this case, but warns this "can severely damage screen-reader users' experience."

*Source: [a11y-dialog — Focus Considerations](https://a11y-dialog.netlify.app/advanced/focus-considerations)*

### Include a Visible Close Button

Every dialog should include a visible close button in the tab sequence. This is separate from Escape-to-close behavior — sighted keyboard users and screen reader users need a discoverable close mechanism.

*Source: [APG Dialog (Modal) Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)*
