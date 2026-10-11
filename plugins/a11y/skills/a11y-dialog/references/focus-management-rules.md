# Dialog focus management

## Initial focus

Choose an element inside the dialog from its content and task:

| Content/task | Useful initial target |
|---|---|
| Large structured content | Static heading or introductory paragraph with `tabindex="-1"` |
| Small form | Appropriate first field |
| Irreversible action | Less destructive choice |
| Short information | Useful control, often Close |

These are APG recommendations, not a fixed screen reader announcement contract
([APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).

```html
<dialog id="details" aria-labelledby="details-title">
  <h2 id="details-title" tabindex="-1" autofocus>Report details</h2>
  <p>Long structured content begins here.</p>
  <form method="dialog"><button>Close</button></form>
</dialog>
```

Do not add `tabindex` to native `<dialog>` itself. Use a descendant for explicit
focus placement ([HTML dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)).

## Custom modal boundaries

Implement Tab from the last tabbable control to the first, and Shift+Tab from
the first to the last. Recompute valid targets when controls become hidden,
disabled or removed. A visible close control must remain usable. Background
inertness does not replace this wrapping
([APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).

## Close and restore

Restore focus to the invoker unless it disappeared or the completed workflow
makes another target more useful. Nested dialogs restore to the still-open
parent dialog. Keep background inert until the parent is also dismissed
([APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).

Test forward/backward traversal, dynamic content, empty dialog content, close
requests, nested dialogs and removed invokers. Report behavior observed on the
supported combinations; do not add `role="document"` solely from a presumed
universal screen reader mode switch.
