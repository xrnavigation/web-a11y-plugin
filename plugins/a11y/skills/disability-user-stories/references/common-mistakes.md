# User-story mistakes and corrections

## Attribute checklist without an outcome

```gherkin
# Wrong: a role alone does not establish usable errors.
Then every error has role="alert"
# Right project acceptance example:
Given I entered an incorrect date
When I submit the form
Then the date error identifies the problem and a supported correction
And the field exposes its associated error description
And submission feedback or deliberate focus lets me find the errors
And I can correct the date without re-entering unrelated data
```

Choose and test the actual notification strategy; do not demand assertive alerts on every field. ([WAI notifications](https://www.w3.org/WAI/tutorials/forms/notifications/))

## Treating a persona as a whole population

Wrong: “A blind user always hears the page linearly and cannot use visual layout.”

Right: “For this task, include participants using relevant screen-reader/braille/magnification workflows and record their strategies.” WAI stories are examples, not universal profiles. ([WAI user stories](https://www.w3.org/WAI/people-use-web/user-stories/))

## Keyboard-only acceptance for dragging

```gherkin
# Incomplete for WCAG 2.5.7:
Then I can reorder with arrow keys
# Add independently:
Then I can reorder to each valid position using visible click/tap controls
And no dragging or path-based gesture is required
```

Pointer equivalence and keyboard access are separate outcomes. ([Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html))

## Passing automation described as conformance

Wrong: “No automated violations means this story is WCAG compliant.”

Right: “The automated checks passed for the tested state; manual keyboard/zoom/AT checks and remaining coverage are recorded.” Evaluation tools assist but do not determine accessibility on their own. ([WAI tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/))

## Simulating disability described as user research

Wrong: “Wearing blurred glasses proves the low-vision user experience.”

Right: “Use an inspection as one preliminary check, then involve participants with relevant access needs and distinguish their observations from the simulation.” ([WAI involving users](https://www.w3.org/WAI/test-evaluate/involving-users/))
