# Accessibility Acceptance Criteria Templates

## Template 1: Per-Story Criteria

Add accessibility-specific acceptance criteria to each user story:

```
As a [user type], I want to [action] so that [benefit].

Acceptance Criteria:
- [ ] All interactive elements are reachable and operable by keyboard
- [ ] Focus order matches the visual/logical order
- [ ] Screen reader announces [specific element] as [expected announcement]
- [ ] Color contrast meets WCAG AA (4.5:1 normal text, 3:1 large text)
- [ ] Error messages are programmatically associated with their fields
- [ ] State changes are announced to assistive technology
```

## Template 2: Disability-Specific Stories

Write explicit stories for specific user needs:

### Keyboard-Only User

```
As a keyboard-only user, I want to [complete this workflow using only
the keyboard] so that I can [accomplish task independently].

Acceptance Criteria:
- [ ] All controls reachable via Tab / Shift+Tab
- [ ] No keyboard traps
- [ ] Visible focus indicator on every interactive element
- [ ] Modal traps focus and returns it on close
```

### Screen Reader User

```
As a screen reader user, I want [the form to announce field labels,
required status, and errors] so that I can complete it without sighted
assistance.

Acceptance Criteria:
- [ ] Each input has a programmatically associated label
- [ ] Required fields announce "required"
- [ ] Error messages are announced when they appear (via aria-live or focus)
- [ ] Form completion confirmation is announced
```

### Low Vision User

```
As a user with low vision, I want [content to be readable at 200% zoom]
so that I can read without horizontal scrolling.

Acceptance Criteria:
- [ ] Content reflows at 200% zoom without horizontal scrollbar
- [ ] Text spacing can be adjusted without loss of content (WCAG 1.4.12)
- [ ] All text meets 4.5:1 contrast ratio
```

## Template 3: Component-Level Criteria

For design system or component library work:

```
Component: [Name]
ARIA Pattern: [APG reference]

Keyboard:
- [ ] [Key]: [Expected behavior]
- [ ] [Key]: [Expected behavior]

Screen Reader:
- [ ] Role announced as: [expected role]
- [ ] Name announced as: [expected name]
- [ ] State changes announced: [list states]

Visual:
- [ ] Focus indicator visible (3:1 contrast minimum)
- [ ] Color contrast meets AA thresholds
- [ ] Works at 200% zoom
```

## Definition of Done Checklist

Add to your team's Definition of Done:

1. Automated scan passes (axe-core, zero violations)
2. Keyboard-only operation verified (full workflow)
3. Focus management correct (modals, route changes, dynamic content)
4. Screen reader announces all content meaningfully (tested with NVDA or VoiceOver)
5. Color contrast meets AA thresholds
6. Content reflows at 200% zoom
7. Error states are announced and associated with fields
8. Heading hierarchy is logical (no skipped levels, reflects page structure)

## Usage Notes

- **Be specific.** "Must be accessible" is not testable. Name the expected screen reader announcement, keyboard interaction, and contrast ratio.
- **Include the ARIA pattern reference.** For custom widgets, link to the [APG pattern](https://www.w3.org/WAI/ARIA/apg/patterns/) so implementers know the expected keyboard behavior.
- **Test with the criteria.** Each checkbox should be verifiable by a tester using keyboard, screen reader, or automated tool.

Sources: [TetraLogical, "How to write user stories for accessibility"](https://tetralogical.com/blog/2022/05/26/how-to-write-user-stories-for-accessibility/), [Section508.gov Sample User Stories](https://www.section508.gov/develop/user-stories/), [TPGi, "How to Write User Stories for Accessibility Requirements"](https://www.tpgi.com/how-write-user-stories-accessibility-requirements/)
