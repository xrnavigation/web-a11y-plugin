# Framework integration

Reuse the repository's dialog/router lifecycle owners. Framework state can commit
after an event handler; target focus only when the destination is mounted and the
request still corresponds to the user action.

## Native dialog example

```html
<button id="open-settings" type="button">Settings</button>
<dialog id="settings" aria-labelledby="settings-title">
  <h2 id="settings-title">Settings</h2>
  <form method="dialog"><button value="close">Close</button></form>
</dialog>
<script>
const dialog = document.getElementById('settings');
document.getElementById('open-settings').addEventListener('click', () => dialog.showModal());
</script>
```

HTML defines modal display, inertness and dialog-form closing. Test actual initial
focus and restoration; choose the destination for the content and workflow
([WHATWG dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element),
[APG dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).

## Lifecycle checklist

Bind listeners through the framework's lifecycle and remove them on cleanup.
Capture the opener before opening. When the destination is removed, choose a
surviving logical element; don't call focus on stale refs or hidden/inert targets.
Coordinate nested dialogs through the same component owner. Test unmount during
open, async updates, repeat opening and Back/Forward navigation.

Composite widgets use roving tabindex or aria-activedescendant according to the
chosen pattern, not modal trapping
([APG keyboard interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/)).
