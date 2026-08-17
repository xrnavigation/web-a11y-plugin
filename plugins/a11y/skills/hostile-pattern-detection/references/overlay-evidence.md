# The Case Against Accessibility Overlays
## Contents

- [What Overlays Are](#what-overlays-are)
- [Why They Fail: The Technical Reality](#why-they-fail-the-technical-reality)
- [User Experience Evidence](#user-experience-evidence)
  - [WebAIM Screen Reader Survey #10 (2024, 1,539 respondents)](#webaim-screen-reader-survey-10-2024-1539-respondents)
  - [Direct User Testimony (from Overlay Fact Sheet)](#direct-user-testimony-from-overlay-fact-sheet)
  - [Overlay Widget Behavior](#overlay-widget-behavior)
- [Privacy and Disclosure Harms](#privacy-and-disclosure-harms)
- [Legal and Regulatory Evidence](#legal-and-regulatory-evidence)
  - [FTC Enforcement (April 2025)](#ftc-enforcement-april-2025)
  - [Lawsuit Data (UsableNet 2024)](#lawsuit-data-usablenet-2024)
  - [NFB Ban (2021)](#nfb-ban-2021)
- [Professional Consensus](#professional-consensus)
- [What To Do Instead](#what-to-do-instead)
- [Responding to Stakeholders](#responding-to-stakeholders)
- [Sources](#sources)


## What Overlays Are

Third-party JavaScript widgets (accessiBe, UserWay, AudioEye, EqualWeb, and others) that claim to make websites WCAG-compliant via a single `<script>` tag. They typically provide:
- A user-facing toolbar with font, contrast, and cursor adjustments
- Claims of automatic detection and repair of accessibility issues using AI

## Why They Fail: The Technical Reality

**Automated tools can only detect 25-30% of accessibility issues.** The remaining 70-75% require human judgment and source code changes. If a `<div>` should be a `<button>`, no JavaScript overlay can create correct semantics — it cannot know the developer's intent, and even if it could, injecting ARIA attributes on top of broken markup creates new problems.

Overlays cannot fix:
- Missing or incorrect heading hierarchy
- Meaningful alt text (they cannot understand image context)
- Logical tab order
- Correct ARIA role selection
- Form label associations
- Reading order vs. visual order mismatches
- Complex widget keyboard behavior

## User Experience Evidence

### WebAIM Screen Reader Survey #10 (2024, 1,539 respondents)

- **72% of disabled respondents** rated overlays "not at all" or "not very" effective
- **Only 2.4%** rated them "very effective"

Source: [WebAIM Survey #10](https://webaim.org/projects/screenreadersurvey10/)

### Direct User Testimony (from Overlay Fact Sheet)

> "Any site which has deployed an overlay in the past year and a half has been less useable for both my wife and me — both blind."

> "Focus jumps all over the place with #AccessiBe enabled."

> "Makes sites harder to use by getting in the way of browsing and changing access barriers on a page."

A user reported **needing to block accessiBe in their Windows Hosts file** to regain access to their account on an overlay-equipped site.

Source: [Overlay Fact Sheet](https://overlayfactsheet.com/en/)

### Overlay Widget Behavior

On every page load, overlays:
1. Fire unsolicited alert messages ("This site has been adjusted for your screen reader"), disrupting navigation
2. Inject unwanted headings into the page, breaking heading-based navigation
3. Cause unpredictable focus jumps
4. Conflict with the user's own carefully configured AT settings
5. Force users to learn a new, unfamiliar toolbar for every overlay-equipped site

## Privacy and Disclosure Harms

- **Forced disability disclosure:** Overlays offer disability-specific "profiles" ("Screen Reader Profile," "Cognitive Disability Profile"). Selecting one broadcasts disability status.
- **AT detection without consent:** Overlays detect assistive technology use and expose disability status without user knowledge or permission.
- **Cross-site tracking:** Some overlays persist settings via cookies without opt-out, creating potential GDPR and CCPA violations.

## Legal and Regulatory Evidence

### FTC Enforcement (April 2025)

The FTC **fined accessiBe $1 million** for:
- False advertising claims that the product made websites "WCAG compliant"
- Fake customer reviews

This is the first major federal enforcement action specifically targeting an overlay vendor's false accessibility claims.

### Lawsuit Data (UsableNet 2024)

- **25% of all digital accessibility lawsuits** targeted websites using overlay widgets
- **1,023 companies** with overlay widgets were sued in that period
- Overlays **increase** legal risk rather than reducing it

Source: [Accessibility.Works](https://www.accessibility.works/blog/avoid-accessibility-overlay-tools-toolbar-plugins/)

### NFB Ban (2021)

The **National Federation of the Blind banned accessiBe from their 2021 conference**, stating the company "currently engages in behavior that is harmful to the advancement of blind people in society."

Source: [NFB bans accessiBe](https://adabook.medium.com/nfb-bans-accessibe-calls-overlay-seller-harmful-5230ab467e95)

## Professional Consensus

**1,000+ accessibility professionals** signed the Overlay Fact Sheet, including:
- W3C WCAG and ARIA specification contributors
- Accessibility experts from Google, Microsoft, Apple, BBC, and Shopify
- JAWS and NVDA screen reader contributors
- University faculty from MIT, Carnegie Mellon, and Gallaudet

Source: [Overlay Fact Sheet signatories](https://overlayfactsheet.com/en/)

## What To Do Instead

1. **Fix accessibility at the source.** Remediate HTML, CSS, and JavaScript directly.
2. **Build accessibility into development.** Use accessible component libraries. Review designs for accessibility before coding.
3. **Test with real AT.** NVDA, JAWS, VoiceOver, keyboard-only, voice control. Automated tools (axe-core, WAVE) supplement but never replace human testing.
4. **Involve disabled users** in usability testing.
5. **Never recommend overlays.** If asked, explain why they fail — share this document.

## Responding to Stakeholders

If someone proposes an overlay, share these facts:

| Stakeholder Concern | Overlay Promise | Reality |
|---|---|---|
| "We need to be WCAG compliant" | "One script makes you compliant" | Automated tools detect 25-30% of issues. 70-75% require code changes. |
| "We'll get sued" | "Our widget prevents lawsuits" | 25% of a11y lawsuits target overlay-equipped sites. Risk increases. |
| "It's cheaper than remediation" | "No developer time needed" | FTC fined accessiBe $1M. Lawsuits cost more than remediation. |
| "Disabled users will benefit" | "AI fixes everything" | 72% of disabled users rate overlays ineffective. NFB calls them harmful. |

## Sources

- [Overlay Fact Sheet](https://overlayfactsheet.com/en/)
- [Accessibility.Works: Overlay Widgets Attract Lawsuits](https://www.accessibility.works/blog/avoid-accessibility-overlay-tools-toolbar-plugins/)
- [Adrian Roselli: Overlays Underwhelm](https://adrianroselli.com/2022/03/overlays-underwhelm-a11y-nyc.html)
- [NFB Bans accessiBe](https://adabook.medium.com/nfb-bans-accessibe-calls-overlay-seller-harmful-5230ab467e95)
- [Karl Groves: Overlay Fact Sheet](https://karlgroves.com/overlay-fact-sheet-what-it-is-and-how-to-make-it-work-for-you/)
- [WebAIM Screen Reader Survey #10](https://webaim.org/projects/screenreadersurvey10/)
- [Should I Use An Accessibility Overlay?](https://shouldiuseanaccessibilityoverlay.com/)
