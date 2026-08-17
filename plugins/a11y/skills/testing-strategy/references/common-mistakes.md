# Common Accessibility Testing Mistakes

## 1. "Axe Passes, So We're Accessible"

Automated testing catches at most 57% of issues by volume ([Deque, 2023](https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues/)), and only 13% of WCAG 2.1 AA criteria can be reliably flagged by automation ([Accessible.org](https://accessible.org/automated-scans-wcag/)). A passing axe scan means the easiest-to-detect issues are absent — nothing more.

**What to do instead:** Use axe-core as the baseline (Tier 1), then keyboard test (Tier 2), then screen reader test (Tier 3). All three tiers are needed.

## 2. Testing Only With One Screen Reader

JAWS, NVDA, and VoiceOver handle ARIA differently. A component that works in NVDA may fail in JAWS or VoiceOver. Browser+SR combinations also matter: NVDA+Chrome behaves differently from NVDA+Firefox for some ARIA patterns.

**What to do instead:** Test with at least two pairings. Start with NVDA+Chrome (free, 21.3% market share) and VoiceOver+Safari (built-in, covers iOS). ([WebAIM Survey #10, 2024](https://webaim.org/projects/screenreadersurvey10/))

## 3. Skipping Keyboard Testing

Keyboard testing is the fastest, cheapest, and most impactful manual test. It requires no tools, no licenses, and no training beyond knowing Tab/Enter/Space/Escape/Arrow keys. It catches focus traps, missing operability, and broken tab order that automation cannot detect.

**What to do instead:** Make keyboard testing part of every PR review. Unplug the mouse and try the workflow.

## 4. Testing Only at the End

Accessibility debt compounds like technical debt. A modal built without focus management in sprint 1 becomes a modal used in 15 places by sprint 10. Retrofitting focus management across 15 call sites is far more expensive than building it once correctly.

**What to do instead:** Include accessibility acceptance criteria in each story. Run axe in CI. Keyboard-test each PR. Screen-reader-test new components.

## 5. Writing Vague Acceptance Criteria

"Must be accessible" is not testable. Neither is "meets WCAG." These criteria cannot be verified by a tester and will be silently skipped.

**What to do instead:** Write specific, verifiable criteria:
- "Screen reader announces the dialog title when opened"
- "Tab key moves focus through form fields in top-to-bottom order"
- "Error message is announced via aria-live when form submission fails"
- "Button contrast ratio is at least 4.5:1 against background"

## 6. Ignoring Mobile Assistive Technology

91.3% of screen reader users use one on mobile ([WebAIM Survey #10, 2024](https://webaim.org/projects/screenreadersurvey10/)). VoiceOver on iOS (70.6% of mobile SR users) and TalkBack on Android (27.6%) use gesture-based interaction that differs fundamentally from desktop keyboard navigation. Touch targets, gesture operability, and swipe navigation all need testing.

**What to do instead:** Test with VoiceOver on iOS and/or TalkBack on Android for any mobile-facing product.

## 7. Using DevTools Instead of Real Assistive Technology

Browser accessibility inspectors (Chrome DevTools, Firefox Accessibility Inspector) show the accessibility tree — what the browser exposes to AT. They do not show what the user actually hears. Live regions may appear correct in the tree but announce at the wrong time. Focus may look correct in the inspector but feel wrong when tabbing through.

**What to do instead:** Run the actual screen reader and listen. NVDA is free. VoiceOver is built into macOS and iOS. There is no substitute for hearing what users hear.

## 8. Testing Only the Happy Path

Accessibility testing often focuses on the default state: the form before errors, the modal before it opens, the page before dynamic content loads. Error states, loading states, empty states, and edge cases are where accessibility breaks.

**What to do instead:** Test error flows (form validation failures, network errors), loading states (skeleton screens, spinners with announcements), and dynamic content (items added/removed from lists, real-time updates).

## 9. Assuming Color Alone Conveys Information

Using only color to indicate status (red for error, green for success) fails [WCAG 1.4.1 Use of Color](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html). This is caught by manual review, not automation.

**What to do instead:** Add text labels, icons, or patterns alongside color. Test by viewing the interface in grayscale.

## 10. Not Testing Heading Structure

Screen reader users navigate primarily by headings — 71.6% use headings as their first strategy for finding content on lengthy pages ([WebAIM Survey #10, 2024](https://webaim.org/projects/screenreadersurvey10/)). Skipped heading levels (h1 to h3), missing headings, and headings used purely for visual styling break this navigation.

**What to do instead:** Verify heading hierarchy with a tool (headingsMap extension) or by pressing H in NVDA to step through all headings. Headings should form an outline of the page content.
