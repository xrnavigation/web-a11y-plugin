# Native dialog implementation

## Opening and closing

Use `showModal()` for document modality and `show()` for non-modal presentation.
Do not toggle the `open` attribute as a substitute for `showModal()`; that does
not invoke the modal opening behavior. The modal dialog is in the top layer and
its document background becomes inert
([HTML dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)).

```html
<button type="button" id="show-preferences">Preferences</button>
<dialog id="preferences" aria-labelledby="preferences-title">
  <h2 id="preferences-title">Preferences</h2>
  <form method="dialog">
    <button value="cancel" autofocus>Cancel</button>
    <button value="save">Save</button>
  </form>
</dialog>
<script>
  const preferences = document.getElementById('preferences');
  document.getElementById('show-preferences').addEventListener('click', () => {
    preferences.returnValue = '';
    preferences.showModal();
  });
  preferences.addEventListener('close', () => {
    if (preferences.returnValue === 'save') {
      // Apply the settings here.
    }
  });
</script>
```

`method="dialog"` closes and provides the activated button's value; it does not
submit the form over the network. `close()` is explicit closing, while a close
request can raise the cancel event. Distinguish dismissal from affirmative
confirmation when handling `returnValue`
([HTML dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)).

## Author responsibilities

Provide a name with a visible title via `aria-labelledby`, or `aria-label`.
Choose and test initial focus and restoration. Provide a visible close control.
Use `aria-describedby` only for a useful short description, not extensive
structured content ([APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).

`closedby` defines allowed user closing actions (`any`, `closerequest`, `none`).
Its modal default is close-request behavior; non-modal defaults differ. Verify
features such as light dismissal in target browsers rather than assuming the
specification means identical deployed support
([HTML dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)).

Check keyboard traversal, platform close requests, scrolling, dynamic content
and nesting. A native element reduces implementation work but does not establish
that the surrounding content, labels or workflow are accessible.
