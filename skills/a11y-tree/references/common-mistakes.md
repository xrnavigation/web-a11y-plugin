# Common Mistakes — Tree View Accessibility

---

## 1. Adding `aria-expanded` to leaf nodes

Leaf/end nodes must not have `aria-expanded`. Its presence tells assistive technology the node is a parent that can be expanded, which is false and confusing.

```html
<!-- WRONG -->
<li role="treeitem" aria-expanded="false">README.md</li>

<!-- RIGHT -->
<li role="treeitem">README.md</li>
```

— [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/), [MDN treeitem role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/treeitem_role), [Pope Tech (2023)](https://blog.pope.tech/2023/07/06/create-an-accessible-tree-view-widget-using-aria/)

---

## 2. Mixing `aria-selected` and `aria-checked`

Using both attributes on nodes in the same tree creates contradictory signals for assistive technology. Pick one and use it consistently.

- `aria-selected` — for typical selection semantics (file browsers, navigation).
- `aria-checked` — for checkbox/toggle semantics (permissions, feature toggles).

Never use both on the same tree.

— [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/), [MDN tree role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role)

---

## 3. Adding ARIA roles without keyboard behavior

ARIA provides only semantics, not behavior. Adding `role="tree"` without implementing the full keyboard interaction model (arrow keys, Home/End, expand/collapse, type-ahead) leaves keyboard users stranded. "No ARIA is better than bad ARIA."

```html
<!-- WRONG — semantic promise with no behavioral fulfillment -->
<ul role="tree">
  <li role="treeitem" onclick="toggle()">src</li>
</ul>
<!-- Missing: arrow key navigation, Home/End, expand/collapse, type-ahead -->

<!-- RIGHT — implement the full keyboard model -->
<ul role="tree" aria-labelledby="label" @keydown="handleTreeKeys">
  <li role="treeitem" tabindex="0" aria-expanded="false">src</li>
</ul>
```

— [MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role), [Pope Tech (2023)](https://blog.pope.tech/2023/07/06/create-an-accessible-tree-view-widget-using-aria/)

---

## 4. Missing accessible name on the tree

The tree container must always have `aria-labelledby` or `aria-label`. Without it, screen readers cannot identify the widget.

```html
<!-- WRONG -->
<ul role="tree">...</ul>

<!-- RIGHT -->
<h3 id="tree-label">Project Files</h3>
<ul role="tree" aria-labelledby="tree-label">...</ul>
```

— [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/), [MDN tree role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role)

---

## 5. Using tree view when a simpler pattern suffices

Navigation menus styled to look like trees should use the disclosure pattern (`<details>`/`<summary>`), not `role="tree"`. The tree role requires complex, non-standard keyboard handling that users do not expect in typical site navigation.

```html
<!-- WRONG — navigation with tree semantics -->
<nav>
  <ul role="tree">
    <li role="treeitem" aria-expanded="true">
      Products
      <ul role="group">
        <li role="treeitem"><a href="/widgets">Widgets</a></li>
      </ul>
    </li>
  </ul>
</nav>

<!-- RIGHT — disclosure pattern for expandable navigation -->
<nav aria-label="Main">
  <ul>
    <li>
      <details open>
        <summary>Products</summary>
        <ul>
          <li><a href="/widgets">Widgets</a></li>
        </ul>
      </details>
    </li>
  </ul>
</nav>
```

— [MDN tree role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role), [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)

---

## 6. Using `aria-activedescendant` without testing screen readers

VoiceOver (macOS/iOS) has had issues with `aria-activedescendant`. GitHub's team found roving tabindex to be more reliable across screen readers. However, older VoiceOver versions required `aria-activedescendant`. The choice requires testing.

— [GitHub Blog (2023)](https://github.blog/engineering/user-experience/considerations-for-making-a-tree-view-component-accessible/), [Accessible Culture (2013)](https://accessibleculture.org/articles/2013/02/not-so-simple-aria-tree-views-and-screen-readers/)

---

## 7. Not specifying positional attributes for dynamic trees

When nodes load dynamically and the full DOM tree is not present, browsers may not compute positional information. Screen readers then cannot announce "item 3 of 10, level 2."

Required for dynamic/virtual trees:
- `aria-level` — nesting depth (1-based integer)
- `aria-setsize` — total siblings in set
- `aria-posinset` — position within set (1-based integer)

— [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/), [MDN treeitem role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/treeitem_role)

---

## 8. Selection follows focus in inappropriate contexts

Automatically selecting items as the user navigates works for simple single-select trees but destroys usability in:
- Multi-select trees (impossible to navigate without changing selection)
- Trees where selection triggers expensive actions (API calls, page loads)

"Can severely degrade accessibility." — [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)

---

## 9. Failing to test with actual assistive technology

Compatibility varies significantly across JAWS, NVDA, VoiceOver, and Orca. Automated testing cannot catch these differences. Test with at least NVDA + Firefox and VoiceOver + Safari.

— [GitHub Blog (2023)](https://github.blog/engineering/user-experience/considerations-for-making-a-tree-view-component-accessible/), [Accessible Culture (2013)](https://accessibleculture.org/articles/2013/02/not-so-simple-aria-tree-views-and-screen-readers/)
