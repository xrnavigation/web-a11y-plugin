---
name: a11y-dialog
description: Guides accessible native and custom modal dialogs. Use when building dialogs, confirmation prompts, alertdialogs, or modal overlays with focus placement, containment, and restoration.
---

# Accessible dialogs

Prefer native `<dialog>` when it fits the task. `showModal()` makes the dialog
modal and the rest of its document inert; `show()` opens it non-modally. A custom
ARIA dialog needs behavior implemented separately
([HTML dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element),
[APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).

## Native modal example

```html
<button id="open-dialog" type="button">Delete file</button>
<dialog id="confirmation" aria-labelledby="confirmation-title">
  <h2 id="confirmation-title">Delete the file?</h2>
  <p>This action cannot be undone.</p>
  <form method="dialog">
    <button value="cancel" autofocus>Cancel</button>
    <button value="delete">Delete</button>
  </form>
</dialog>
<script>
  const dialog = document.getElementById('confirmation');
  document.getElementById('open-dialog').addEventListener('click', () => {
    dialog.returnValue = ''; // Avoid retaining a prior confirmed choice.
    dialog.showModal();
  });
  dialog.addEventListener('close', () => {
    // Perform deletion only if returnValue === 'delete'.
  });
</script>
```

This example only opens the dialog and returns a choice. `method="dialog"`
closes the dialog without submitting a network request. Verify focus placement,
close requests and restoration in target environments
([HTML dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)).

## Custom modal responsibilities

- Name it with `aria-labelledby` referencing a visible title, or `aria-label`.
  Use `aria-describedby` for a short description; omit it when a single flattened
  announcement would obscure structured content
  ([APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).
- Set `role="dialog"` and `aria-modal="true"` only when it behaves modally. Move
  focus inside, wrap Tab/Shift+Tab within its current tabbable controls, provide
  Escape/close behavior and restore focus to the invoker or a useful fallback
  ([APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).
- Make background regions inert without making the dialog itself inert. Inert
  background and Tab wrapping solve different problems; custom modals need both
  background exclusion and focus containment
  ([HTML inert](https://html.spec.whatwg.org/multipage/interaction.html#inert),
  [APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).

Choose initial focus from content: a static heading with `tabindex="-1"` for
long structured content, an appropriate field for a small form, or the less
destructive action for an irreversible choice. Do not add `tabindex` to native
`<dialog>` itself ([APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/),
[HTML dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)).

Use `alertdialog` for a brief important message requiring a response; provide
its name and reference the message with `aria-describedby`. This role does not
implement modality or guarantee a sound
([APG alert dialog](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/)).

Read [focus rules](references/focus-management-rules.md),
[native guide](references/native-dialog-guide.md),
[verification](references/screen-reader-behavior.md),
[common mistakes](references/common-mistakes.md) and
[sources](references/sources.yaml).
