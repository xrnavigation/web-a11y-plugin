---
name: aria-decision-framework
description: Guides choosing native HTML and correct ARIA roles, names, states, and ownership. Use when writing ARIA attributes, reviewing custom controls, or deciding whether an interaction needs a composite widget.
---

# ARIA decisions

Start with the required task and use a native element when it supplies the
needed semantics and behavior. ARIA augments semantics; it does not implement a
custom control's keyboard interaction
([WAI-ARIA introduction](https://www.w3.org/TR/wai-aria-1.2/)).

## Decide before adding a role

1. Match the task to HTML: button for actions, link for navigation, checkbox for
   a binary choice, select for option selection. Check permitted role overrides
   and native restrictions before repurposing an element
   ([ARIA in HTML](https://w3c.github.io/html-aria/)).
2. Add states that native HTML does not express, such as `aria-pressed` on a
   toggle button, without replacing its native role
   ([APG button](https://www.w3.org/WAI/ARIA/apg/patterns/button/)).
3. For a composite widget, choose its pattern and implement focus, keyboard
   behavior, state updates and role ownership together. APG is implementation
   guidance; ARIA defines role/state requirements
   ([APG read me first](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)).

## Examples

```html
<!-- Wrong: role alone adds no activation behavior. -->
<div role="button" onclick="save()">Save</div>
<!-- Prefer native semantics and keyboard activation. -->
<button type="button" onclick="save()">Save</button>

<!-- Toggle behavior still needs JavaScript to update this state. -->
<button type="button" aria-pressed="false">Mute</button>

<!-- Wrong: still programmatically focusable while hidden from AT. -->
<button aria-hidden="true" tabindex="-1">Close</button>
<!-- Remove from rendering, or make the relevant region inert. -->
<button hidden>Close</button>
<div inert><button>Close</button></div>
```

A negative tabindex removes a control from sequential focus navigation but does
not prevent programmatic focus. `aria-hidden` does not implement focus exclusion
([HTML focus](https://html.spec.whatwg.org/multipage/interaction.html#the-tabindex-attribute),
[WAI-ARIA aria-hidden](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden),
[HTML inert](https://html.spec.whatwg.org/multipage/interaction.html#inert)).

## Names and relationships

Use visible text or labels where the role permits naming. `aria-label` and
`aria-labelledby` cannot name roles with naming prohibited, such as `generic`.
Keep the accessible name consistent with visible labels
([ARIA in HTML](https://w3c.github.io/html-aria/)).

For comboboxes, `aria-expanded` is required; `aria-controls` must identify the
popup while visible and may remain when it is hidden. Required ownership is
not a universal direct-DOM-child rule: descendant or explicitly owned elements
can satisfy relationships, subject to the role's requirements
([APG combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/),
[WAI-ARIA definitions](https://www.w3.org/TR/wai-aria-1.2/)).

Ordinary navigation usually needs links and disclosures, but fully implemented
navigation menu buttons can legitimately use links with `role="menuitem"`
([APG navigation menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/examples/menu-button-links/)).

Read [HTML mappings](references/html-aria-mapping.md),
[ARIA authoring rules](references/five-rules-of-aria.md),
[required attributes](references/required-aria-attributes.md),
[common mistakes](references/common-mistakes.md) and
[sources](references/sources.yaml). Verify supported combinations and report
actual observations rather than claiming a universal announcement.
