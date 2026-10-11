# Testing mistakes

Wrong: `axe passes, therefore the site conforms`.
Right: record detectable rules, states, incomplete results, manual/AT checks and
untested scope ([Playwright](https://playwright.dev/docs/accessibility-testing)).

Wrong: `200% zoom proves reflow`.
Right: test text enlargement to 200% and reflow at 320 CSS pixels wide (vertical
scrolling) or 256 CSS pixels high (horizontal scrolling), with scoped exceptions
([Resize text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html),
[Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)).

Wrong: assert exact NVDA wording from a DOM snapshot.
Right: record the semantic expectation, then observed speech with versions and
settings; mark unrun tests not tested
([APG](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)).

Wrong: keyboard Move buttons establish every pointer criterion automatically.
Right: actually complete the task with single-pointer clicks/taps without dragging
and verify cancellation and target spacing
([Dragging movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)).
