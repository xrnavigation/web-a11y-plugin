---
name: testing-strategy
description: Guides accessibility testing strategy — what to test automatically vs manually vs with assistive technology. Provides keyboard testing checklists, screen reader testing basics, and acceptance criteria templates. Use when planning testing, writing acceptance criteria, or deciding how to verify accessibility.
argument-hint: "[component-or-feature]"
allowed-tools: Read, Glob, Grep
---

# Accessibility Testing Strategy

> "Automated testing with axe-core identifies 57% of digital accessibility issues by volume."
> — [Deque, Automated Testing Study (2023)](https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues/)

> "Automated scans reliably flag only 13% of WCAG 2.1 AA success criteria."
> — [Accessible.org](https://accessible.org/automated-scans-wcag/)

Automated testing is necessary but insufficient. A complete accessibility testing strategy uses three tiers, each catching different categories of issues.

---

## 1. Three Testing Tiers

### Tier 1: Automated Testing (~57% of issues by volume)

**Tools:** axe-core, Lighthouse, WAVE, HTML validators
**When:** Every build / CI pipeline

Catches well:
- Color contrast ratios below thresholds ([WCAG 1.4.3](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html))
- Missing `alt` attributes, form labels, page `lang` ([Deque, 2023](https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues/))
- Invalid ARIA: duplicate IDs, broken references, invalid roles
- Structural issues: missing bypass blocks, empty/skipped headings
- Missing page title, missing language declaration

**Key stat:** Seven WCAG criteria account for over 80% of all issues found, with contrast alone at ~30%. ([Deque, 2023](https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues/))

### Tier 2: Keyboard Testing

**Tools:** None required beyond a keyboard
**When:** Every feature / PR

Catches issues automation misses:
- Focus visibility and indicator quality ([WCAG 2.4.7](https://www.w3.org/WAI/WCAG21/Understanding/focus-visible.html))
- Tab order matching visual/reading order ([WCAG 2.4.3](https://www.w3.org/WAI/WCAG21/Understanding/focus-order.html))
- Keyboard traps ([WCAG 2.1.2](https://www.w3.org/WAI/WCAG21/Understanding/no-keyboard-trap.html))
- Interactive element operability ([WCAG 2.1.1](https://www.w3.org/WAI/WCAG21/Understanding/keyboard.html))
- Skip links and modal focus management

See: [references/keyboard-testing-checklist.md](references/keyboard-testing-checklist.md)

### Tier 3: Screen Reader Testing

**Tools:** NVDA + Chrome (Windows), VoiceOver + Safari (macOS/iOS), TalkBack + Chrome (Android)
**When:** New components, significant UI changes, pre-release

Catches issues that require hearing what AT communicates:
- Reading order and meaningful sequence ([WCAG 1.3.2](https://www.w3.org/WAI/WCAG21/Understanding/meaningful-sequence.html))
- Live region announcements ([WCAG 4.1.3](https://www.w3.org/WAI/WCAG21/Understanding/status-messages.html))
- Name, role, value correctness ([WCAG 4.1.2](https://www.w3.org/WAI/WCAG21/Understanding/name-role-value.html))
- Info and relationships communication ([WCAG 1.3.1](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships.html))

See: [references/screen-reader-commands.md](references/screen-reader-commands.md)

---

## 2. What Automated Testing Catches vs Misses

### Coverage Breakdown (WCAG 2.1 AA, 55 criteria)

| Detection Level | Criteria Count | Percentage |
|---|---|---|
| Mostly accurate automated detection | 7 of 55 | 13% |
| Partially detectable (flags, needs human review) | 25 of 55 | 45% |
| Cannot be detected by automation | 23 of 55 | 42% |

Source: [Accessible.org](https://accessible.org/automated-scans-wcag/)

### What Automation Cannot Catch

| Category | Why Automation Fails |
|---|---|
| Alt text quality | Detects missing `alt` but not whether text is meaningful |
| Reading order | DOM vs visual order requires human judgment |
| Keyboard operability | Dynamic interaction sequences can't be fully automated |
| Focus management | Context-dependent behavior in SPAs, modals |
| Meaningful labels | "Click here" is technically present but not descriptive |
| Error message quality | Detects presence but not helpfulness |
| Cognitive load | Information organization, plain language |
| Live region behavior | Timing and appropriateness of announcements |

Source: [Deque, Manual vs Automated Testing](https://www.deque.com/blog/how-accessibility-programs-benefit-from-both-manual-and-automated-testing/)

---

## 3. Keyboard Testing Summary

Disconnect the mouse. Start from the browser address bar.

| Check | What to Verify |
|---|---|
| Tab order | Tab moves through all interactive elements in logical order |
| Focus visibility | Every focused element has a visible indicator (3:1 contrast min) |
| Operability | Links: Enter. Buttons: Enter/Space. Checkboxes: Space. Radios: Arrows |
| No traps | Focus never gets stuck; Tab/Shift+Tab/Escape always works |
| Modals | Focus enters modal, cycles within it, Escape closes, focus returns |
| Skip links | First focusable element, moves focus past navigation |

**Standard keys:**

| Key | Expected Action |
|---|---|
| Tab / Shift+Tab | Move forward/backward through interactive elements |
| Enter | Activate link or button |
| Space | Activate button, toggle checkbox, open select |
| Arrow keys | Navigate within widget (radio group, menu, tabs, listbox) |
| Escape | Close modal, menu, or dialog |
| Home / End | Jump to first/last item in list or menu |

Sources: [WebAIM Keyboard Accessibility](https://webaim.org/techniques/keyboard/), [UW Keyboard Checklist](https://www.washington.edu/accesstech/checklist/keyboard/), [W3C Easy Checks](https://www.w3.org/WAI/test-evaluate/easy-checks/keyboard-focus/)

Full checklist: [references/keyboard-testing-checklist.md](references/keyboard-testing-checklist.md)

---

## 4. Screen Reader Testing Basics

### Which SR + Browser Pairings to Test

Test in priority order based on market share ([WebAIM Survey #10, 2024](https://webaim.org/projects/screenreadersurvey10/)):

| Priority | Combination | Coverage | Cost |
|---|---|---|---|
| 1 | NVDA + Chrome (Windows) | 21.3% of users | Free |
| 2 | VoiceOver + Safari (macOS) | 7.0% + all iOS | Built-in |
| 3 | JAWS + Chrome (Windows) | 24.7% of users | License required |
| 4 | TalkBack + Chrome (Android) | 27.6% of mobile | Built-in |

### Desktop Market Share

| Screen Reader | Share |
|---|---|
| JAWS | 40.5% |
| NVDA | 37.7% |
| VoiceOver | 9.7% |

### What to Listen For

When testing with a screen reader, verify:
1. **Element identification** — role announced correctly ("button", "link", "heading level 2")
2. **Accessible name** — label is meaningful and matches visible text ([WCAG 2.5.3](https://www.w3.org/WAI/WCAG21/Understanding/label-in-name.html))
3. **State changes** — expanded/collapsed, checked/unchecked, selected announced on change
4. **Reading order** — content reads in meaningful sequence
5. **Live regions** — dynamic updates announced without requiring navigation
6. **Heading structure** — headings navigable (H key in NVDA), hierarchy logical

Full command reference: [references/screen-reader-commands.md](references/screen-reader-commands.md)

---

## 5. WCAG Criteria Requiring Human Judgment

These criteria cannot be verified by automation — they require understanding of meaning, context, and quality.

| Criterion | Why Human Judgment Needed |
|---|---|
| 1.1.1 Non-text Content (quality) | Can detect missing `alt` but not accuracy |
| 1.2.1–1.2.5 Media alternatives | Cannot verify transcript/caption accuracy |
| 1.3.2 Meaningful Sequence | Cannot determine if reading order preserves meaning |
| 1.3.3 Sensory Characteristics | Cannot detect reliance on shape/color/location alone |
| 2.4.5 Multiple Ways | Cannot assess navigation method availability across site |
| 2.4.6 Headings and Labels (quality) | Detects headings, not whether they are descriptive |
| 3.1.2 Language of Parts | Cannot determine where language changes occur |
| 3.2.3 Consistent Navigation | Cannot compare consistency across pages |
| 3.2.4 Consistent Identification | Cannot verify consistent naming across pages |
| 3.3.3 Error Suggestion | Cannot evaluate if error messages are helpful |
| 3.3.4 Error Prevention | Cannot verify confirmation/review for critical transactions |

### Partially Detectable (flagged but need human confirmation)

| Criterion | Automation Flags | Humans Must Verify |
|---|---|---|
| 1.3.1 Info and Relationships | Missing semantic markup | Whether markup conveys right relationships |
| 1.4.5 Images of Text | Presence of images | Whether images contain text that should be HTML |
| 2.4.4 Link Purpose | Link text exists | Whether text is meaningful in context |
| 4.1.2 Name, Role, Value | ARIA attributes present | Whether names are accurate and useful |

Source: [Accessible.org](https://accessible.org/automated-scans-wcag/)

---

## 6. Writing Acceptance Criteria

### Per-Story Template

Add to each user story:

```
Acceptance Criteria:
- [ ] All interactive elements reachable and operable by keyboard
- [ ] Focus order matches visual/logical order
- [ ] Screen reader announces [element] as [expected announcement]
- [ ] Color contrast meets WCAG AA (4.5:1 text, 3:1 large text)
- [ ] Error messages programmatically associated with fields
- [ ] State changes announced to assistive technology
```

### Component-Level Template

```
Component: [Name]
ARIA Pattern: [APG reference]

Keyboard:
- [ ] [Key]: [Expected behavior]

Screen Reader:
- [ ] Role announced as: [expected role]
- [ ] Name announced as: [expected name]
- [ ] State changes announced: [list states]

Visual:
- [ ] Focus indicator visible (3:1 contrast)
- [ ] Color contrast meets AA
- [ ] Works at 200% zoom
```

### Definition of Done Checklist

1. Automated scan passes (axe-core, zero violations)
2. Keyboard-only operation verified (full workflow)
3. Focus management correct (modals, route changes, dynamic content)
4. Screen reader announces all content meaningfully (NVDA or VoiceOver)
5. Color contrast meets AA thresholds
6. Content reflows at 200% zoom
7. Error states announced and associated with fields
8. Heading hierarchy logical (no skipped levels)

Full templates: [references/acceptance-criteria-templates.md](references/acceptance-criteria-templates.md)

Sources: [TetraLogical](https://tetralogical.com/blog/2022/05/26/how-to-write-user-stories-for-accessibility/), [Section508.gov](https://www.section508.gov/develop/user-stories/), [TPGi](https://www.tpgi.com/how-write-user-stories-accessibility-requirements/)

---

## 7. Common Mistakes

See: [references/common-mistakes.md](references/common-mistakes.md)

The most frequent testing anti-patterns:

1. **"Axe passes, so we're accessible"** — Automation catches at most 57% of issues by volume, and only 13% of WCAG criteria with high confidence. ([Deque](https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues/), [Accessible.org](https://accessible.org/automated-scans-wcag/))

2. **Testing only with one screen reader** — JAWS, NVDA, and VoiceOver behave differently. A component working in one may fail in another. Test with at least two. ([WebAIM Survey #10](https://webaim.org/projects/screenreadersurvey10/))

3. **Skipping keyboard testing** — The fastest, cheapest tier. No tools needed. Catches focus traps, missing operability, and broken tab order that automation misses entirely.

4. **Testing at the end** — Accessibility debt compounds. Test each tier as part of the PR workflow, not as a pre-release gate.

5. **Writing vague acceptance criteria** — "Must be accessible" is not testable. Specify what the screen reader should announce, what keyboard interaction is expected, and what contrast ratio applies.

6. **Ignoring mobile** — 91.3% of screen reader users use one on mobile. VoiceOver (iOS) and TalkBack (Android) have different interaction models than desktop. ([WebAIM Survey #10](https://webaim.org/projects/screenreadersurvey10/))

7. **Not testing with real assistive technology** — Browser DevTools accessibility inspectors show the accessibility tree but not what users actually hear. Run NVDA or VoiceOver and listen.

---

## 8. Cross-References

- `a11y-audit` — Full audit methodology and WCAG conformance checking
- `aria-decision-framework` — When and how to use ARIA correctly
- `focus-management` — Focus trapping, restoration, and roving tabindex patterns
- `form-a11y` — Form labeling, error handling, and validation patterns
- `live-regions` — `aria-live` region patterns and announcement timing
