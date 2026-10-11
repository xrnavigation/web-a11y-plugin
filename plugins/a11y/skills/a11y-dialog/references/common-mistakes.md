# Dialog mistakes

## Inert background mistaken for Tab wrapping

Wrong: add `inert` to background and assume a custom dialog now wraps Tab.
Right: implement boundary wrapping and background exclusion, updating tabbable
controls as dialog content changes. Native `showModal()` supplies document
modality; verify its focus behavior rather than adding a competing trap
([APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/),
[HTML dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)).

## Hidden from AT but still interactive

```html
<!-- Wrong: aria-hidden does not block focus or clicks. -->
<main aria-hidden="true"><button>Background action</button></main>
<!-- Right background exclusion for a custom modal. -->
<main inert><button>Background action</button></main>
```

Do not make an ancestor containing the dialog inert. Remove temporary inertness
when the last modal depending on it closes
([HTML inert](https://html.spec.whatwg.org/multipage/interaction.html#inert)).

## Name limited to one naming mechanism

```html
<!-- Both naming mechanisms are valid. Prefer a visible title when present. -->
<div role="dialog" aria-labelledby="settings-title"><h2 id="settings-title">Settings</h2></div>
<div role="dialog" aria-label="Settings"></div>
```

These are naming examples, not complete dialogs. `aria-labelledby` is not the
only valid naming method. Associate a short description when useful; avoid
flattening extensive structured content into one description
([APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).

## Incorrect initial focus or restoration

Wrong: always focus the destructive action or restore focus to a removed button.
Right: use the less destructive action for irreversible choices, a static
starting element for large content, and a useful fallback if the invoker no
longer exists. Include a visible close control
([APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).
