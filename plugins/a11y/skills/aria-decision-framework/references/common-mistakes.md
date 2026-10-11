# Common ARIA mistakes

## Semantic role without behavior

```html
<!-- Wrong: not keyboard operable by role alone. -->
<div role="button" onclick="save()">Save</div>
<!-- Right: native action control. -->
<button type="button" onclick="save()">Save</button>
```

Role semantics do not supply the full interaction contract
([APG read me first](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)).

## Negative tabindex mistaken for non-focusability

```html
<!-- Wrong: remains programmatically focusable while hidden from AT. -->
<button aria-hidden="true" tabindex="-1">Close</button>
<!-- Right: remove from rendering or exclude the relevant region. -->
<button hidden>Close</button>
<div inert><button>Close</button></div>
```

Negative tabindex removes sequential navigation, not programmatic focus.
`aria-hidden` alone does not prevent focus or activation
([HTML tabindex](https://html.spec.whatwg.org/multipage/interaction.html#the-tabindex-attribute),
[HTML inert](https://html.spec.whatwg.org/multipage/interaction.html#inert),
[WAI-ARIA aria-hidden](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden)).

## Naming where naming is prohibited

Wrong: `<div aria-label="Statistics">42 users</div>` with implicit generic role.
Right: use a heading plus visible content or a named section where appropriate.
Name-from-author is prohibited for generic roles, unlike named landmarks and
widgets ([ARIA in HTML](https://w3c.github.io/html-aria/)).

## Direct-child rule invented

Wrong: reject every neutral wrapper between `tablist` and descendant `tab`.
Right: preserve role ownership and assess the actual accessibility-tree
structure ([WAI-ARIA tablist](https://www.w3.org/TR/wai-aria-1.2/#tablist)).

## Menu roles treated as forbidden for links

Wrong: claim every `<a role="menuitem">` is prohibited.
Right: prefer ordinary links for ordinary navigation, or implement the complete
menu-button interaction when justified
([APG navigation menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/examples/menu-button-links/)).

## Visible and accessible names disagree

Wrong: `<button aria-label="Submit form data">Send</button>`.
Right: `<button>Send</button>` or an accessible name containing “Send”. For
controls with visible text labels, WCAG requires that text in the accessible name
([Understanding 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html)).
