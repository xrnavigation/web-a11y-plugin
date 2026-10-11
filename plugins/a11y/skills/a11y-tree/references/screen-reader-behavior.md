# Tree AT verification

Tree/treeitem/group roles and expanded, selected, level and position properties
express intended structure and state. Verify what the actual support matrix
exposes; exact speech and navigation modes vary
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/),
[WAI-ARIA tree](https://www.w3.org/TR/wai-aria-1.2/#tree)).

Test entering/exiting the tree, all documented arrow keys, expansion/collapse,
selection, type-ahead, moving focus versus changing selection, deleted/virtualized
items and lazy loading. Verify a collapsed subtree is not traversed, and that
focus remains on a surviving logical node after collapsing a focused descendant
([APG treeview](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)).

Record OS/browser/AT versions, mode/settings, action, observed output, DOM focus or
active descendant and selection. Historical 2013/2023 support reports do not
establish current per-reader guarantees. Use additional live announcements only
for a reproduced task gap, avoiding duplicate state speech
([APG read me first](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)).
