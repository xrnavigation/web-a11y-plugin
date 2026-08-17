---
name: a11y-dialog
description: >-
  Guides accessible modal and non-modal dialog implementation. Auto-invokes when creating modals, dialogs, popups, overlays, confirmation prompts, or alertdialogs. Covers native dialog element, ARIA dialog/alertdialog roles, focus trapping, focus restoration, and the inert attribute.
allowed-tools: Read, Glob, Grep
---

# Accessible Dialog Implementation

> "Blanket statements about where to put focus when opening a modal dialog are wrong, including this one."
> — [Adrian Roselli, 2025](https://adrianroselli.com/2025/06/where-to-put-focus-when-opening-a-modal-dialog.html)

---

## 1. Decision: Native `<dialog>` vs ARIA Dialog

**Default to native `<dialog>`.** MDN explicitly recommends: "Use the native `<dialog>` HTML element when possible." ([MDN — ARIA dialog role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/dialog_role))

### Use native `<dialog>` when:

- Building any new dialog — it is the recommended default
- You need modal behavior (`.showModal()` gives you focus trapping, backdrop, background inertness, and Escape-to-close for free)
- You need non-modal/modeless dialogs (`.show()`)

### Use ARIA `role="dialog"` when:

- You cannot use `<dialog>` (legacy browser requirements, though increasingly rare)
- You are enhancing a custom component that cannot be restructured to use `<dialog>`
- Shadow DOM edge cases where `<dialog>` is unavailable

### What native `<dialog>` gives you for free vs what you still own

| Aspect | Native `<dialog>` | ARIA `role="dialog"` |
|--------|-------------------|---------------------|
| Focus trapping | Automatic (top layer) | Manual JS required |
| Background inertness | Automatic | Manual (`inert` or `aria-hidden`) |
| Backdrop | `::backdrop` pseudo-element | Custom overlay element |
| Escape to close | Built-in (`closedby`) | Manual `keydown` handler |
| `aria-modal` | Implicit | Must add explicitly |
| Accessible name | **Manual** (`aria-labelledby`) | **Manual** (`aria-labelledby`) |

*Sources: [HTML Spec — The dialog element](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element); [MDN — ARIA dialog role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/dialog_role)*

---

## 2. Native `<dialog>` Quick Reference

### `.showModal()` vs `.show()`

- **`.showModal()`** — modal: top layer, background inert, `::backdrop`, defaults to `closedby="closerequest"` (Escape closes)
- **`.show()`** — non-modal: background remains interactive, no backdrop, defaults to `closedby="none"`

### `closedby` attribute

| Value | Behavior | Default for |
|-------|----------|-------------|
| `"closerequest"` | Escape / platform close gestures | Modal dialogs |
| `"any"` | Escape + clicking outside | — |
| `"none"` | No automatic closing | Non-modal dialogs |

### Built-in focus management

1. If any element inside has `autofocus`, that element receives focus
2. Otherwise, focus delegates to the dialog's focus delegate
3. If neither applies, the dialog element itself receives focus

Use `autofocus` explicitly for predictable focus placement.

### Events

- `close` — fires after dialog closes
- `toggle` / `beforetoggle` — fires on open/close state changes
- `returnValue` — communicates which button closed the dialog

### Minimal correct example

```html
<dialog id="confirm" aria-labelledby="confirm-title">
  <h2 id="confirm-title">Confirm deletion</h2>
  <p id="confirm-desc">This action cannot be undone.</p>
  <button autofocus>Cancel</button>
  <button>Delete</button>
</dialog>

<script>
  document.getElementById('confirm').showModal();
</script>
```

*Source: [HTML Spec — The dialog element](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)*

---

## 3. ARIA Dialog Pattern

Use this only when native `<dialog>` is not viable. You take full ownership of behavior.

### Required roles, states, and properties

| Attribute | Requirement | Notes |
|-----------|-------------|-------|
| `role="dialog"` | Required on container | Not needed on `<dialog>` element |
| `aria-modal="true"` | Required for modal | Implicit with `<dialog>.showModal()` |
| `aria-labelledby` | Required (preferred) | References visible dialog title |
| `aria-label` | Alternative | When no visible title exists |
| `aria-describedby` | Recommended | References content describing dialog purpose |

**Critical rule:** Only set `aria-modal="true"` when your code actually prevents all interaction outside the dialog AND visual styling obscures external content. ([APG Dialog Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/))

### Minimal correct ARIA skeleton

```html
<!-- WRONG — role without behavior -->
<div role="dialog" aria-label="Settings">
  <p>Content here</p>
</div>

<!-- RIGHT — role with all required behavior -->
<div role="dialog" aria-modal="true"
     aria-labelledby="dlg-title" aria-describedby="dlg-desc"
     tabindex="-1">
  <h2 id="dlg-title">Settings</h2>
  <p id="dlg-desc">Configure your preferences.</p>
  <!-- focusable content -->
  <button>Save</button>
  <button>Cancel</button>
</div>
<!-- All sibling content must have inert attribute -->
```

You must implement: focus trapping, Escape to close, focus restoration, background inertness.

*Source: [APG Dialog (Modal) Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)*

---

## 4. Alertdialog: When and How

### When to use `alertdialog` vs `dialog`

| Use `alertdialog` | Use `dialog` |
|-------------------|-------------|
| Action confirmation ("Delete this?") | Forms and data entry |
| Error message confirmations | Information display |
| Critical notifications demanding response | Multi-step workflows, settings |

The `alertdialog` role tells assistive technologies to "give alert dialogs special treatment, such as playing a system alert sound." ([APG Alert and Message Dialogs](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/))

### Required attributes

| Attribute | Requirement |
|-----------|-------------|
| `role="alertdialog"` | Required on container |
| `aria-labelledby` or `aria-label` | Required (one of) |
| `aria-describedby` | **Must** reference the alert message element |

### Example

```html
<dialog role="alertdialog" aria-labelledby="alert-title"
        aria-describedby="alert-msg">
  <h2 id="alert-title">Delete account?</h2>
  <p id="alert-msg">This will permanently delete your account and all data.</p>
  <button autofocus>Cancel</button>
  <button>Delete</button>
</dialog>
```

Keyboard interaction is identical to modal dialog. Some implementations intentionally block Escape dismissal for alertdialogs.

*Source: [APG Alert and Message Dialogs](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/)*

---

## 5. Focus Management

Focus placement is **context-dependent**. There is no single correct answer.

### Where focus goes on open

| Dialog Type | Focus Target | Rationale |
|------------|--------------|-----------|
| Short informational message | Close button | Quick dismissal; `aria-describedby` conveys message |
| Long/interactive content | Dialog element or heading | User needs to orient first |
| Irreversible action (delete, payment) | **Least destructive** option (Cancel) | Prevents accidental activation |
| Brief familiar form (login) | First form field | Reduces steps; only if user triggered the dialog |
| Long/unfamiliar form | Dialog or heading, NOT form field | Prevents premature keyboard activation |
| Legal/financial agreement | Do NOT focus "I agree" | Prevents accidental acceptance |

**Do NOT auto-focus text fields in unexpected/unsolicited modals** — this is a dark pattern.

*Source: [Adrian Roselli — Where to Put Focus](https://adrianroselli.com/2025/06/where-to-put-focus-when-opening-a-modal-dialog.html)*

### Focus restoration on close

Focus returns to the element that had focus before the dialog opened (typically the trigger button). Edge cases:
- Trigger no longer exists → focus a logically related element
- Workflow suggests a different target (e.g., newly created row) → focus the contextually appropriate element

### Tab cycling (modal only)

- Tab from last focusable element wraps to first
- Shift+Tab from first wraps to last
- The dialog container (`tabindex="-1"`) is excluded from the tab cycle

For detailed rules, see: [references/focus-management-rules.md](references/focus-management-rules.md)

*Sources: [APG Dialog Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/); [a11y-dialog — Focus Considerations](https://a11y-dialog.netlify.app/advanced/focus-considerations)*

---

## 6. The `inert` Attribute

### What it does

The `inert` attribute makes an element and all descendants non-interactive:
- No pointer events, no text selection, not editable
- Not focusable, not exposed to accessibility APIs (screen readers skip entirely)
- Excluded from find-in-page

### Relationship to dialog

- **Native `<dialog>.showModal()`** — background automatically becomes inert. No `inert` attribute needed.
- **Custom dialog** — apply `inert` to sibling content manually. This replaces the old triple-technique approach.

### What `inert` replaces

Before `inert`, you needed all three:
1. `aria-hidden="true"` on siblings (screen readers)
2. JavaScript focus trapping (keyboard)
3. CSS `pointer-events: none` or overlay (pointer)

`inert` or native `.showModal()` replaces all three.

### Browser support

Chrome 102+, Firefox 112+, Safari 15.5+. Use it.

*Sources: [HTML Spec — The inert attribute](https://html.spec.whatwg.org/multipage/interaction.html#the-inert-attribute); [MDN — ARIA dialog role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/dialog_role)*

---

## 7. Keyboard Interaction

| Key | Action | Notes |
|-----|--------|-------|
| **Escape** | Closes dialog | Native `<dialog>` handles automatically. For `alertdialog`, consider blocking Escape. |
| **Tab** | Next focusable element, wraps at end | Must be trapped within modal. |
| **Shift+Tab** | Previous focusable element, wraps at start | Must be trapped within modal. |
| **Enter** | Activates focused control | Standard, no special handling. |

*Source: [APG Dialog (Modal) Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)*

---

## 8. Common Mistakes

### 8.1 Not blocking screen reader virtual cursor from background

```html
<!-- WRONG — CSS overlay does not block screen readers -->
<div class="overlay"></div>
<div role="dialog">...</div>

<!-- RIGHT — use native dialog or inert -->
<dialog>...</dialog>
<!-- or -->
<main inert>...</main>
<div role="dialog" aria-modal="true">...</div>
```

Screen readers navigate via virtual cursor, which ignores CSS. You must use `inert`, `aria-hidden="true"`, or native `.showModal()`. ([MDN — ARIA dialog role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/dialog_role))

### 8.2 Always focusing the first interactive element

```html
<!-- WRONG — delete button gets focus on a confirmation dialog -->
<dialog aria-labelledby="t">
  <h2 id="t">Delete account?</h2>
  <button autofocus>Delete permanently</button> <!-- dangerous! -->
  <button>Cancel</button>
</dialog>

<!-- RIGHT — least destructive option gets focus -->
<dialog aria-labelledby="t">
  <h2 id="t">Delete account?</h2>
  <button>Delete permanently</button>
  <button autofocus>Cancel</button> <!-- safe default -->
</dialog>
```

Focus placement depends on dialog purpose. ([Roselli, 2025](https://adrianroselli.com/2025/06/where-to-put-focus-when-opening-a-modal-dialog.html))

### 8.3 Missing accessible name

```html
<!-- WRONG — screen reader announces "dialog" with no context -->
<dialog>
  <h2>Settings</h2>
  <p>Configure options.</p>
</dialog>

<!-- RIGHT — dialog has an accessible name -->
<dialog aria-labelledby="settings-title">
  <h2 id="settings-title">Settings</h2>
  <p>Configure options.</p>
</dialog>
```

Native `<dialog>` does NOT auto-set `aria-labelledby`. You must add it. ([MDN — ARIA dialog role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/dialog_role))

### 8.4 Not restoring focus on close

When the dialog closes without returning focus, keyboard/screen reader users lose their place in the document. Store the trigger element reference before opening and restore focus on close. ([APG Dialog Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/))

### 8.5 Using `alertdialog` for non-urgent content

`alertdialog` triggers system alert sounds and interrupts screen reader flow. Reserve it for confirmations and critical errors only. ([APG Alert and Message Dialogs](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/))

### 8.6 Adding redundant `aria-modal` to native `<dialog>`

When using `.showModal()`, `aria-modal` is implicit. Adding it is unnecessary noise. ([Roselli, 2020](https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html))

For more anti-patterns, see: [references/common-mistakes.md](references/common-mistakes.md)

---

## 9. Cross-References

- **aria-decision-framework** — when to use ARIA vs native HTML (start here if unsure whether you need `role="dialog"`)
- **focus-management** — general focus management patterns beyond dialogs
- **css-a11y** — styling considerations for dialogs (backdrop, reduced-motion, forced-colors)

For detailed reference material:

- [references/focus-management-rules.md](references/focus-management-rules.md) — context-dependent focus placement
- [references/native-dialog-guide.md](references/native-dialog-guide.md) — complete native `<dialog>` reference
- [references/screen-reader-behavior.md](references/screen-reader-behavior.md) — per-AT behavior differences
- [references/common-mistakes.md](references/common-mistakes.md) — expanded anti-patterns with citations
- [references/sources.yaml](references/sources.yaml) — provenance for all cited sources
