# Anxiety, time pressure, and recovery

Use these project design prompts to reduce uncertainty. Do not describe distress or coping strategies as universal to a diagnosis. W3C's supplemental [COGA guidance](https://www.w3.org/TR/coga-usable/) addresses understandable, predictable tasks; the [data-loss pattern](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p09-data-loss/) explains why recovery and breaks matter.

| Risk to inspect | Suggested change | Test |
|---|---|---|
| Countdown during document collection | Remove optional limit or provide an applicable timing route | Gather documents slowly, extend, then resume. |
| Unsaved work at expiration | Save eligible draft data under an appropriate retention policy | Expire/re-authenticate; confirm recoverable fields and omissions. |
| Ambiguous destructive action | Explain exact scope and recovery limits | User can describe consequences before committing. |
| Unclear submission state | Show truthful saved/submitted/failed status | Retry does not create an unnoticed duplicate. |
| Unexpected navigation | Use explicit actions and explain context changes | Back returns to a useful state without losing entries. |

## Timing precision

Do not replace “at least ten extensions” with “extension up to 10×”. The adjustment route operates before encountering the limit; the extension route supplies a warning and at least 20 seconds for a simple action, repeatable at least ten times. Document any real-time, essential, or over-20-hour exception. ([Timing Adjustable, A](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html))

The >20-hour preservation exception belongs to SC 2.2.6 (AAA). Choose retention based on the task, privacy, and security requirements; a warning is its other route. Do not recommend saving credentials or all sensitive data in browser storage. ([Timeouts](https://www.w3.org/WAI/WCAG22/Understanding/timeouts.html))

## Review consequences

```html
<!-- Wrong: scope and consequence are unclear. -->
<button type="button">Yes</button>
<!-- Right project copy: implement a review/recovery path suited to the action. -->
<p>Deleting this album permanently removes its 47 photos.</p>
<button type="button">Delete album and 47 photos</button>
<button type="button">Keep album</button>
```

Undo and confirmation are different tools; choose based on reversibility and consequence. Extra confirmation dialogs can add work, while undo cannot recover an already irreversible action. ([COGA usable](https://www.w3.org/TR/coga-usable/))
