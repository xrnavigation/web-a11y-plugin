---
name: testing-strategy
description: Plans web accessibility verification across automation, keyboard, assistive technology, zoom, pointer input and media. Use when defining acceptance criteria, choosing a support matrix, or deciding what evidence a feature needs.
argument-hint: "[component-or-feature]"
---

# Accessibility testing strategy

Define the journey, states, support matrix and evidence needed for the change.
Combine automated, manual and user evaluation; no fixed percentage describes the
coverage of an arbitrary product or establishes conformance
([WAI evaluation](https://www.w3.org/WAI/test-evaluate/),
[Playwright](https://playwright.dev/docs/accessibility-testing)).

## Map risk to evidence

| Lane | Useful evidence | Limit |
|---|---|---|
| Static and rendered automation | Rule results, accessible names, states and interaction assertions | Detectable rules and tested states only |
| Keyboard | Full task without pointer, sensible focus order and escape paths | Does not establish speech behavior or touch access |
| Real screen reader | Observed names, roles, states, reading order, announcements and task completion | Tested OS/browser/AT/settings only |
| Low vision | Text resizing, reflow, spacing overrides, focus visibility and contrast | Needs visual review and applicable exceptions |
| Pointer and touch | Single-pointer alternatives, cancellation and target spacing | Keyboard alternatives alone do not verify pointer criteria |
| Media | Captions, descriptions, alternatives and usable controls | Track presence alone does not verify content quality |

Use these lanes as a project testing plan, not a claim that WCAG specifies this
particular process. See `a11y-audit`, `at-experience-verification`, `zoom-reflow`,
`pointer-gestures` and `media-a11y` for scoped workflows. WCAG applicability comes
from the actual success criteria ([WCAG 2.2](https://www.w3.org/TR/WCAG22/)).

## Exercise meaningful states

Include initial/loading, ready, empty, error, validation, expansion, selection,
modal open/close, async completion and route transitions relevant to the change.
Reuse existing test helpers and capture readiness before scanning
([Playwright](https://playwright.dev/docs/accessibility-testing)).

Verify keyboard operation and meaningful focus order, including reverse traversal.
Composite widgets may use one Tab stop and arrows internally; do not require every
option to be a separate Tab stop. A modal's intentional containment needs a working
exit path, not unrestricted Tab into the background
([APG keyboard practices](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/),
[WCAG keyboard trap](https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html)).

Test visible keyboard focus (2.4.7 AA), author-created focus contrast where
applicable (1.4.11 AA), and focus not entirely obscured by author content
(2.4.11 AA). Treat 2.4.13 Focus Appearance's area/change-contrast conditions as AAA,
not a blanket AA two-pixel rule
([WCAG 2.2](https://www.w3.org/TR/WCAG22/)).

Test text resizing to 200% separately from reflow at 320 CSS pixels wide for
vertical-scrolling content, or 256 CSS pixels high for horizontal-scrolling
content. For example, a 1280 CSS pixel viewport at 400% zoom is equivalent to
320 CSS pixels wide. Record applicable two-dimensional exceptions and test spacing
overrides without content/function loss
([Resize text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html),
[Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html),
[Text spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)).

## Choose the AT support matrix

Use product user needs and support commitments. Record exact versions, interaction
mode, verbosity and settings. Cover the environments affected by a change rather
than treating an old survey's percentages as present-day coverage. Mark unavailable
combinations **not tested** and predictions **predicted**
([APG read me first](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)).

## Write acceptance criteria and report

```text
Journey / component / revision:
Requirement or project recommendation and primary source:
Starting state and action:
Expected semantic information and task outcome:
Automated evidence:
Keyboard evidence:
Observed AT output, environment and settings:
Zoom / spacing / pointer / media evidence as applicable:
Exceptions, incomplete results and checks not run:
Fix / retest evidence:
```

Example: after submitting an empty email field, the visible error identifies the
problem, the field exposes its invalid state and associated error, focus remains
useful, and correction succeeds. Verify on the supported combinations; exact
utterance wording is not the acceptance criterion
([WAI validation](https://www.w3.org/WAI/tutorials/forms/validation/)).

Do not replace unrun manual or AT checks with a passing axe scan. Report findings,
remaining coverage and blocked checks in plain language
([Playwright](https://playwright.dev/docs/accessibility-testing)).

Read the [keyboard checklist](references/keyboard-testing-checklist.md),
[screen reader commands](references/screen-reader-commands.md),
[acceptance templates](references/acceptance-criteria-templates.md),
[common mistakes](references/common-mistakes.md) and
[source registry](references/sources.yaml) as needed.
