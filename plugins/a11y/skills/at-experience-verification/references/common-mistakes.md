# AT evidence mistakes

Wrong: put `NVDA announces "Email, edit text"` in a report without running NVDA.
Right: say `predicted: labeled editable field`; capture the actual output with
versions and settings when tested. APG examples require support testing
([APG](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)).

Wrong: an unnamed `<input>` is shown as a labeled correct example.
Right: `<label for="email">Email</label><input id="email" type="email">`.
Verify the exposed name and task completion
([WAI labels](https://www.w3.org/WAI/tutorials/forms/labels/)).

Wrong: claim a clean accessibility tree proves users hear async status updates.
Right: trigger the update in the tested AT/browser and record what happens; keep
status available visibly even if speech is missed
([WCAG status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)).
