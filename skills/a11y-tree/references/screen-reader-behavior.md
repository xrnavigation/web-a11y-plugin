# Screen Reader Behavior — Tree Views

---

## What Screen Readers Announce

When focus lands on a treeitem, screen readers typically convey:

- **Role**: "tree item" or equivalent
- **Name**: the accessible name of the node
- **State**: "expanded" or "collapsed" (for parent nodes)
- **Level**: "level 2" (from `aria-level` or computed from DOM nesting)
- **Position**: "3 of 10" (from `aria-posinset`/`aria-setsize` or computed)
- **Selection**: "selected" or "not selected" (when `aria-selected` is present)

— [APG Tree View Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)

---

## Per-Reader Behavior

### JAWS (Windows)

- Announces tree identification in browse mode only.
- Reliably conveys expanded/collapsed state and branch level.
- Reports sibling position for collapsed/end nodes but not for expanded nodes.
- In IE, concatenated all descendant text into the accessible name (verbosity issue; less relevant with modern browsers).

— [Accessible Culture (2013)](https://accessibleculture.org/articles/2013/02/not-so-simple-aria-tree-views-and-screen-readers/)

### NVDA (Windows)

- Performs well in Firefox; historically had issues in IE.
- Announces expanded/collapsed states and branch level in Firefox.
- May not announce sibling position in all browser contexts.

— [Accessible Culture (2013)](https://accessibleculture.org/articles/2013/02/not-so-simple-aria-tree-views-and-screen-readers/)

### VoiceOver (macOS/iOS)

- Has historically identified trees as "tables" rather than tree views.
- Older versions required `aria-activedescendant`; did not sync with roving tabindex.
- Arrow key navigation conflicts with native VoiceOver key commands (users must be in the correct interaction mode).
- `aria-labelledby` pointing to explicit text IDs (rather than relying on text content) is critical for consistent announcements.

— [GitHub Blog (2023)](https://github.blog/engineering/user-experience/considerations-for-making-a-tree-view-component-accessible/), [Accessible Culture (2013)](https://accessibleculture.org/articles/2013/02/not-so-simple-aria-tree-views-and-screen-readers/)

### Orca (Linux)

- Does not announce child count or sibling position.
- `aria-setsize` and `aria-posinset` had no effect in tested versions.

— [Accessible Culture (2013)](https://accessibleculture.org/articles/2013/02/not-so-simple-aria-tree-views-and-screen-readers/)

---

## Focus Management Recommendations

### Roving tabindex (recommended)

Set `tabindex="0"` on the focused item, `tabindex="-1"` on all others. Move tabindex as focus moves.

**Pros:** Better VoiceOver support (modern); DOM focus matches visible focus.
**Cons:** Requires DOM manipulation on every focus change.

### aria-activedescendant

Set `tabindex="0"` on the tree container; `aria-activedescendant` points to the currently "focused" treeitem ID.

**Pros:** No DOM manipulation needed; simpler state management.
**Cons:** VoiceOver support has been inconsistent; older versions required it, newer versions work better with roving tabindex.

**GitHub's recommendation (2023):** Use roving tabindex. It outperformed `aria-activedescendant` in real-world testing across NVDA, JAWS, and VoiceOver.

— [GitHub Blog (2023)](https://github.blog/engineering/user-experience/considerations-for-making-a-tree-view-component-accessible/)

---

## Live Region Announcements for Async Loading

GitHub implemented live region announcements for dynamic content:

- Known count: "Loading {x} items"
- Unknown count: "Loading..."
- Empty branches: "{branch name} is empty"
- Focus moves to first child when content loads, or returns to parent if empty.

— [GitHub Blog (2023)](https://github.blog/engineering/user-experience/considerations-for-making-a-tree-view-component-accessible/)
