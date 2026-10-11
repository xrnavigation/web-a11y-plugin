# ARIA roles, states and ownership

Check the role definition for required states/properties, required naming,
supported attributes and required ownership. A role with no required
state/property can still require a name. Do not describe every global attribute
as valid naming for every role
([WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/)).

| Role | State/property to implement | Naming/relationship notes |
|---|---|---|
| checkbox, menuitemcheckbox | `aria-checked` | Supports mixed state |
| radio, menuitemradio, switch | `aria-checked` | Use true/false |
| slider | `aria-valuenow` | Supply appropriate limits/value text |
| combobox | `aria-expanded`; `aria-controls` when popup visible | Name input and match popup role |
| dialog, alertdialog | Modality state when modal | Accessible name required; alert message association |
| tab | Selection state | Owned by tablist; controls panel |
| listbox | Multiple-selection state when applicable | Named; owns options or option groups |
| grid | Selection/read-only state when applicable | Named; owns rows and cells |

The role definitions in [WAI-ARIA](https://www.w3.org/TR/wai-aria-1.2/) specify
normative requirements. The conditional combobox controls relationship is
explained by [APG combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/).

## Relationship checks

- Check ID references resolve to the actual controlled or active elements.
- Preserve required ownership: tablist/tab, listbox/option, menu/menuitem, and
  grid/row/cell. Ownership does not always mean immediate DOM parentage.
- Do not duplicate ownership across widgets or use `aria-owns` simply to patch a
  structure that can be represented correctly in the DOM.
- Match exposed state to rendered behavior; ARIA itself does not implement it.

Definitions and role tables: [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/).

## Native controls

Use native checked, disabled, required and other supported attributes rather
than duplicating contradictory ARIA state. Consult element-specific allowed
roles and attributes before adding them
([ARIA in HTML](https://w3c.github.io/html-aria/)).
