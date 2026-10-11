# Evidence examples

## Labeled input

Wrong: `<label>Email</label><input type="email">` has no association.
Right: `<label for="email">Email</label><input id="email" type="email">`.
Test the exposed name and actual task interaction
([WAI labels](https://www.w3.org/WAI/tutorials/forms/labels/)).

## Dialog transcript

Wrong: infer `NVDA announces Settings dialog` without running NVDA.
Right: expect a named Settings dialog, useful focus and working close/restoration;
record observed output under a stated environment
([APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).

## Dynamic feedback

Wrong: mark a DOM `role="status"` check as observed speech.
Right: trigger the update, retain visible feedback and record actual output;
otherwise label the speech check not tested
([WCAG status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)).
