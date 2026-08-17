---
name: a11y-tree
description: Guides accessible tree view and treegrid implementation per APG patterns. Auto-invokes when creating tree views, file browsers, hierarchical lists, nested navigation trees, or treegrid components. Covers tree vs treegrid decision, required ARIA roles/states, keyboard interaction, and multi-select patterns.
allowed-tools: Read, Glob, Grep
---

# Accessible Tree View & Treegrid

> "No ARIA is better than Bad ARIA."
> — [APG Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)

Tree views have no native HTML equivalent. You must use ARIA — which means you own all keyboard interaction, focus management, and state updates. A `role="tree"` without the full keyboard model leaves users stranded.

---

## 1. Tree vs Treegrid

Choose the right pattern before writing any markup.

| Criterion | Tree | Treegrid |
|-----------|------|----------|
| Data shape | Single-column labels (file names, nav items) | Multi-column tabular data per row |
| Cell focus | No — focus is on the treeitem only | Yes — individual cells are focusable |
| Editing | Not applicable | Cells may contain editable inputs |
| Use cases | File explorer sidebar, settings categories | Expandable data tables, task lists with columns |
| Keyboard model | Arrow keys navigate between nodes | Arrow keys navigate between rows AND cells |

— [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/), [APG Treegrid Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treegrid/)

**Important:** If the widget is expandable site navigation, use the **disclosure pattern** (`<details>`/`<summary>`) instead. The tree role requires complex keyboard handling that users do not expect on typical web content. — [MDN tree role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role), [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)

---

## 2. Required ARIA Structure

### Minimal tree markup

Use semantic `ul`/`li` elements with ARIA roles overlaid. GitHub's engineering team found this provides the best cross-platform support — better accessibility tree generation, automatic Forced Color Mode support, and improved behavior on less-common assistive technologies. — [GitHub Blog (2023)](https://github.blog/engineering/user-experience/considerations-for-making-a-tree-view-component-accessible/)

```html
<h3 id="tree-label">Files</h3>
<ul role="tree" aria-labelledby="tree-label">
  <li role="treeitem" aria-expanded="true">
    <span>src</span>
    <ul role="group">
      <li role="treeitem" aria-expanded="false">
        <span>components</span>
        <ul role="group">
          <li role="treeitem">Button.tsx</li>
        </ul>
      </li>
      <li role="treeitem">index.ts</li>
    </ul>
  </li>
  <li role="treeitem">README.md</li>
</ul>
```

### Role hierarchy

| Role | Required parent | Required children | Purpose |
|------|----------------|-------------------|---------|
| `tree` | None | One or more `treeitem` (directly or via `group`) | Root container |
| `treeitem` | `tree`, `treeitem`, or `group` | Optional `group` for children | Each node |
| `group` | `treeitem` | One or more `treeitem` | Wraps child nodes of a parent |

— [MDN tree role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role), [MDN treeitem role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/treeitem_role)

### Attribute checklist

| Attribute | Where | When | Values |
|-----------|-------|------|--------|
| `aria-labelledby` or `aria-label` | `tree` | Always (required) | Reference to visible label or string |
| `aria-expanded` | Parent `treeitem` only | Always on parent nodes | `true` / `false` |
| `aria-selected` | Selectable `treeitem` | Single-select or multi-select | `true` / `false` |
| `aria-checked` | Selectable `treeitem` | Alternative to `aria-selected` (checkbox-style) | `true` / `false` / `mixed` |
| `aria-multiselectable` | `tree` | Multi-select trees | `true` |
| `aria-level` | `treeitem` | Dynamic/virtual trees | Integer (1-based) |
| `aria-setsize` | `treeitem` | Dynamic/virtual trees | Integer |
| `aria-posinset` | `treeitem` | Dynamic/virtual trees | Integer (1-based) |
| `aria-owns` | `tree` or `treeitem` | When children are not DOM descendants | Space-separated ID list |
| `aria-activedescendant` | `tree` | When using activedescendant focus pattern | ID of focused treeitem |

— [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/), [MDN treeitem role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/treeitem_role)

### Focus management: roving tabindex vs aria-activedescendant

| Approach | How it works | Pros | Cons |
|----------|-------------|------|------|
| Roving tabindex | `tabindex="0"` on focused item, `tabindex="-1"` on all others | Better VoiceOver support (modern); DOM focus matches visible focus | Requires DOM manipulation on every focus change |
| aria-activedescendant | `tabindex="0"` stays on tree container; `aria-activedescendant` points to focused treeitem ID | No DOM manipulation; simpler state management | VoiceOver support has been inconsistent |

**Recommendation:** Use roving tabindex. GitHub found it outperformed `aria-activedescendant` in real-world testing across NVDA, JAWS, and VoiceOver. — [GitHub Blog (2023)](https://github.blog/engineering/user-experience/considerations-for-making-a-tree-view-component-accessible/)

---

## 3. Keyboard Interaction Summary

All keyboard behavior is **required** — `role="tree"` without it is broken. — [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)

### Core navigation (vertical tree)

| Key | Behavior |
|-----|----------|
| **Right Arrow** | Closed parent: open it. Open parent: move to first child. End node: nothing. |
| **Left Arrow** | Open parent: close it. Child/end node: move to parent. Root closed/end: nothing. |
| **Down Arrow** | Move focus to next visible node. |
| **Up Arrow** | Move focus to previous visible node. |
| **Home** | Move focus to first node. |
| **End** | Move focus to last visible node. |
| **Enter** | Perform default action (toggle expand/collapse for parents; select for leaves in single-select). |
| **Type-ahead** | Focus moves to next node whose label starts with typed character(s). Recommended for trees with 7+ root nodes. |
| **\* (Asterisk)** | Optional. Expand all siblings at the same level. |

### Focus on entry

- No selection: focus goes to first node.
- Single-select with selection: focus goes to selected node.
- Multi-select with selection: focus goes to first selected node.

### Treegrid-specific additions

| Key | Behavior |
|-----|----------|
| **Tab** | Move through focusable elements within a row; exit grid at last element. |
| **Right/Left Arrow** (cell focus) | Move between cells in a row. |
| **Page Up / Page Down** | Scroll by an author-determined number of rows. |

— [APG Treegrid Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treegrid/)

For the complete keyboard interaction specification including multi-select key combinations, see [references/keyboard-interaction.md](references/keyboard-interaction.md).

---

## 4. Multi-select Trees

### Container requirement

Set `aria-multiselectable="true"` on the `tree` element. — [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)

### Selection attribute choice

- Use `aria-selected` for typical selection semantics.
- Use `aria-checked` for checkbox/toggle semantics (permissions, feature toggles).
- **Never use both on the same tree.** — [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/), [MDN tree role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role)
- Selected: `"true"`. Unselected but selectable: `"false"`. Non-selectable: omit attribute entirely.

### Selection vs focus

In multi-select trees, **selection is always independent of focus**. Users navigate with arrow keys (focus) and use Space/Shift/Ctrl to change selection. Visual design must clearly distinguish focus from selected state.

**Selection-follows-focus** (auto-selecting on navigate) must NOT be used with multi-select trees — it makes navigation without changing selection impossible, which "can severely degrade accessibility." — [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)

### Multi-select keyboard (recommended model)

| Key | Behavior |
|-----|----------|
| **Space** | Toggle selection of focused node. |
| **Shift + Down/Up Arrow** | Move focus and toggle selection. (Optional) |
| **Shift + Space** | Select contiguous range from last selected to current. (Optional) |
| **Ctrl + A** | Select all / unselect all. (Optional) |

---

## 5. Common Mistakes

### 5.1 Adding `aria-expanded` to leaf nodes

```html
<!-- WRONG -->
<li role="treeitem" aria-expanded="false">README.md</li>

<!-- RIGHT -->
<li role="treeitem">README.md</li>
```

Leaf nodes must not have `aria-expanded`. Its presence tells assistive technology the node is a parent that can be expanded — which is false and confusing. — [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/), [MDN treeitem role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/treeitem_role), [Pope Tech (2023)](https://blog.pope.tech/2023/07/06/create-an-accessible-tree-view-widget-using-aria/)

### 5.2 Adding ARIA roles without keyboard behavior

```html
<!-- WRONG — semantic promise with no behavioral fulfillment -->
<ul role="tree">
  <li role="treeitem" onclick="toggle()">src</li>
</ul>
<!-- No arrow key handling, no Home/End, no type-ahead -->
```

ARIA provides only semantics, not behavior. Adding `role="tree"` without the full keyboard interaction model leaves keyboard users stranded. "No ARIA is better than bad ARIA." — [MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role), [Pope Tech (2023)](https://blog.pope.tech/2023/07/06/create-an-accessible-tree-view-widget-using-aria/)

### 5.3 Missing accessible name on the tree

```html
<!-- WRONG -->
<ul role="tree">...</ul>

<!-- RIGHT -->
<h3 id="tree-label">Project Files</h3>
<ul role="tree" aria-labelledby="tree-label">...</ul>
```

The tree container must always have `aria-labelledby` or `aria-label`. Without it, screen readers cannot identify the widget. — [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/), [MDN tree role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role)

### 5.4 Using tree view when a simpler pattern suffices

Navigation menus styled to look like trees should use the disclosure pattern (`<details>`/`<summary>`), not `role="tree"`. The tree role requires complex keyboard handling that users do not expect in typical site navigation. — [MDN tree role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role), [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)

### 5.5 Missing `aria-level`/`aria-setsize`/`aria-posinset` for dynamic trees

When nodes load dynamically and the full DOM tree is not present, browsers cannot compute positional information. Screen readers then cannot announce "item 3 of 10, level 2." — [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/), [MDN treeitem role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/treeitem_role)

### 5.6 Mixing `aria-selected` and `aria-checked`

Using both attributes on nodes in the same tree creates contradictory signals for assistive technology. Pick one and use it consistently across the entire tree. — [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/), [MDN tree role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role)

For the full list of mistakes with screen reader behavior details, see [references/common-mistakes.md](references/common-mistakes.md).

---

## 6. Cross-References

For broader ARIA guidance and the decision of whether to use ARIA at all:
- `aria-decision-framework` — the five rules of ARIA, native-first decision tree

For related widget patterns:
- `a11y-grid` — data grid and spreadsheet patterns (if your tree has multi-column data, consider treegrid or grid instead)

For detailed reference material:
- [references/keyboard-interaction.md](references/keyboard-interaction.md) — complete keyboard spec for tree and treegrid
- [references/common-mistakes.md](references/common-mistakes.md) — expanded anti-patterns with screen reader context
- [references/screen-reader-behavior.md](references/screen-reader-behavior.md) — per-reader announcements and quirks
- [references/sources.yaml](references/sources.yaml) — provenance for all cited sources
