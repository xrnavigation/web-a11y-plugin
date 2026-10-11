# Keyboard verification checklist

Use the widget's documented interaction contract and native platform behavior.
Tab traverses components; arrows may navigate inside composite widgets. Not every
interactive item needs its own Tab stop
([APG keyboard interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/)).

| Check | Sequence and evidence |
|---|---|
| Reachability | Complete the main task and reverse traversal without a pointer |
| Focus order | Preserve meaning and operation as the view changes |
| Operability | Native links/buttons work; composite keys follow the chosen pattern |
| Focus visibility | Inspect focused states, forced colors, sticky content and zoom |
| Escape path | Leave embedded/custom controls; exit modal through its intended close path |
| Modal lifecycle | Initial focus, containment, close and useful restoration |
| Skip link | Reach and activate bypass; verify focus and next Tab location |
| Async/error states | Focus survives results, validation, insertion and deletion |

Keyboard operability is SC 2.1.1; no trap is 2.1.2; meaningful focus order is 2.4.3;
Focus Visible is 2.4.7 AA; Focus Not Obscured is 2.4.11 AA. Focus Appearance's area
and change-contrast requirements are 2.4.13 AAA. Author-created focus-state
contrast is covered by 1.4.11 with its exceptions
([WCAG 2.2](https://www.w3.org/TR/WCAG22/)).

Record actual environment, sequence and outcome. A modal's intended containment
is not an inescapable trap when an operable exit is available
([No keyboard trap](https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html)).
