# Required ARIA Attributes by Role

Source: [WAI-ARIA 1.2 — W3C Recommendation](https://www.w3.org/TR/wai-aria-1.2/), Section 5.4 (Definition of Roles)

This reference lists required and commonly-used supported states/properties for the roles agents encounter most frequently. All roles also inherit global ARIA states and properties (Section 6.5), including `aria-atomic`, `aria-busy`, `aria-controls`, `aria-describedby`, `aria-disabled`, `aria-dropeffect`, `aria-flowto`, `aria-grabbed`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-relevant`, `aria-roledescription`.

## Roles with Required Attributes

These roles will fail accessibility checks if required attributes are missing.

| Role | Required Attributes | Section |
|---|---|---|
| `checkbox` | `aria-checked` | §5.4 |
| `combobox` | `aria-expanded`, `aria-controls` | §5.4 |
| `menuitemcheckbox` | `aria-checked` | §5.4 |
| `menuitemradio` | `aria-checked` | §5.4 |
| `radio` | `aria-checked` | §5.4 |
| `slider` | `aria-valuenow` | §5.4 |
| `switch` | `aria-checked` | §5.4 |

## Roles with No Required Attributes

These roles have no required states/properties beyond globals, but have important supported attributes.

| Role | Key Supported Attributes | Notes | Section |
|---|---|---|---|
| `alertdialog` | `aria-labelledby`, `aria-label` | Should have an accessible name; typically labeled by its heading | §5.4 |
| `button` | `aria-pressed`, `aria-expanded` | `aria-pressed` makes it a toggle button; `aria-expanded` indicates expandable | §5.4 |
| `dialog` | `aria-labelledby`, `aria-label` | Should have an accessible name | §5.4 |
| `grid` | `aria-activedescendant`, `aria-multiselectable`, `aria-readonly` | Complex widget requiring keyboard navigation | §5.4 |
| `gridcell` | `aria-selected`, `aria-expanded`, `aria-colindex`, `aria-colspan`, `aria-rowindex`, `aria-rowspan` | Must be contained in `row` | §5.4 |
| `link` | `aria-expanded` | Rarely needs attributes beyond an accessible name | §5.4 |
| `listbox` | `aria-activedescendant`, `aria-multiselectable`, `aria-readonly`, `aria-orientation` | Contains `option` children | §5.4 |
| `menu` | `aria-activedescendant`, `aria-orientation` | Contains `menuitem`, `menuitemcheckbox`, or `menuitemradio` | §5.4 |
| `menuitem` | `aria-posinset`, `aria-setsize` | Must be contained in `menu` or `menubar` | §5.4 |
| `option` | `aria-selected`, `aria-posinset`, `aria-setsize` | Must be contained in `listbox` | §5.4 |
| `radiogroup` | `aria-activedescendant`, `aria-readonly`, `aria-orientation` | Contains `radio` children | §5.4 |
| `tab` | `aria-selected`, `aria-posinset`, `aria-setsize` | Must be contained in `tablist` | §5.4 |
| `tablist` | `aria-activedescendant`, `aria-orientation`, `aria-multiselectable` | Contains `tab` children | §5.4 |
| `tabpanel` | `aria-labelledby` | Should be labeled by its associated `tab` | §5.4 |
| `tree` | `aria-activedescendant`, `aria-multiselectable`, `aria-orientation` | Contains `treeitem` children | §5.4 |
| `treeitem` | `aria-expanded`, `aria-selected`, `aria-posinset`, `aria-setsize` | Must be contained in `group` or `tree` | §5.4 |

## Quick Reference: What Agents Must Remember

### Always add `aria-checked` to:
- `checkbox` (values: `true`, `false`, `mixed`)
- `radio` (values: `true`, `false`)
- `switch` (values: `true`, `false`)
- `menuitemcheckbox` (values: `true`, `false`, `mixed`)
- `menuitemradio` (values: `true`, `false`)

### Always add `aria-expanded` and `aria-controls` to:
- `combobox` — `aria-expanded` indicates listbox visibility; `aria-controls` references the listbox element

### Always add `aria-valuenow` to:
- `slider` — must also typically include `aria-valuemin` and `aria-valuemax`

### Always provide an accessible name for:
- `dialog` and `alertdialog` — use `aria-labelledby` pointing to the dialog's heading
- `tabpanel` — use `aria-labelledby` pointing to its associated `tab`
- All interactive controls — via `aria-label`, `aria-labelledby`, or native labeling

### Parent-child role relationships (must be maintained):

| Parent Role | Required/Expected Children |
|---|---|
| `grid` | `row` (which contains `gridcell`, `columnheader`, `rowheader`) |
| `listbox` | `option` |
| `menu` / `menubar` | `menuitem`, `menuitemcheckbox`, `menuitemradio` |
| `radiogroup` | `radio` |
| `tablist` | `tab` |
| `tree` | `treeitem` (possibly in `group`) |
| `row` | `cell`, `gridcell`, `columnheader`, `rowheader` |

Violating parent-child relationships produces broken accessibility trees. Assistive technology will not correctly navigate the widget.
