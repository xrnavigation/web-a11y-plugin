# Acceptance criteria templates

## Form error journey

```text
Given a ready form with blank required Email field,
when Submit is activated,
then a visible text error identifies Email and suggests correction,
the field exposes its invalid state and associated error,
a documented summary/field focus strategy lets the user find and fix it,
and corrected input can be submitted without losing other entered values.
Evidence: revision, actions, DOM assertions, keyboard and observed AT results.
```

Use the application's actual field IDs and tested feedback mechanism. Error
identification and association are described in
[WAI validation](https://www.w3.org/WAI/tutorials/forms/validation/).

## Component lifecycle

```text
Component / revision / support matrix:
Chosen native element or APG interaction contract:
Expected name, role, states and task outcome:
Open / move / activate / close / restore actions:
Automated assertions and rendered scans:
Observed keyboard and AT evidence:
Zoom / spacing / pointer alternatives as applicable:
Exceptions and checks not run:
```

Follow the selected widget contract; exact speech wording varies by combination
([APG keyboard interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/)).

## Layout

```text
Text enlargement: 200%, no information/function loss (applicable exceptions).
Reflow: 320 CSS px width for vertical or 256 CSS px height for horizontal flow.
Two-dimensional exception: affected section and essential meaning documented.
Spacing overrides: line 1.5, paragraph 2, letter .12, word .16 times font size.
Check ready, modal and error states; report viewport, zoom and actual outcome.
```

Thresholds and exceptions:
[Resize text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html),
[Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html),
[Text spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html).
