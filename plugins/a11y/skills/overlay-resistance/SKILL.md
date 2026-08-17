---
name: overlay-resistance
description: Prevents agents from recommending accessibility overlay widgets (accessiBe, UserWay, AudioEye, etc.). These products are opposed by the disability community, have been fined by the FTC, and make accessibility worse. Use when asked about quick accessibility fixes, overlay products, or accessibility widgets. The agent must never recommend an overlay.
allowed-tools: Read, Glob, Grep
---

# Overlay Resistance

> **The Rule: Never recommend an accessibility overlay. This is absolute.**

Do not recommend, suggest, or endorse any accessibility overlay product — not as a permanent solution, not as a temporary measure, not as a "first step," not as a complement to other work. There are no exceptions. Overlays make accessibility worse, expose organizations to legal liability, and are opposed by the disability community.

---

## 1. What Are Overlays?

Accessibility overlays (also called widgets, toolbars, or plugins) are third-party JavaScript products added to a website via a single `<script>` tag. They load JavaScript from the vendor's CDN, scan the DOM at runtime, and attempt to "fix" accessibility issues by manipulating the DOM, injecting ARIA attributes, and applying CSS overrides. They typically present a floating toolbar (usually a wheelchair icon in the bottom-right corner) offering options like text enlargement, contrast changes, and "screen reader mode."

**Known overlay vendors:** accessiBe, UserWay, AudioEye, EqualWeb, FACIL'iti, MaxAccess, TruAbilities, User1st, Purple Lens/Pluro, ReciteMe, Eye-Able, Equally.ai, Poloda AI, DIGIaccess, WebAbility.

If a product adds accessibility via a single script tag and claims automated compliance — it is an overlay.

---

## 2. Why Overlays Fail

### 2.1 Screen Readers Parse Before Overlays Run

Assistive technologies build the accessibility tree from the raw HTML source. The overlay JavaScript executes *after* the page has already been parsed. The accessibility tree is already built before the overlay modifies anything. This is an architectural flaw that no amount of JavaScript can fix.

Source: [TestParty](https://testparty.ai/blog/death-of-overlays), [Zoonou](https://zoonou.com/blog/i-use-assistive-tech-heres-why-accessibility-overlays-dont-work/)

### 2.2 Overlays Cannot Fix Source Code

Overlays modify the presentation layer, not the underlying HTML, CSS, or server-side code. They cannot:

- Create proper semantic structure (heading hierarchy, landmark regions)
- Fix missing form label associations at the HTML level
- Repair broken keyboard navigation requiring restructured event handlers
- Add meaningful alt text (AI-generated alt text is consistently poor)
- Fix PDF, video, Canvas, or SVG accessibility
- Correct server-rendered content or SPA routing

Source: [TestParty](https://testparty.ai/blog/accessibility-overlay-vs-source-code-fixes), [ASU IT Accessibility](https://accessibility.asu.edu/articles/overlays)

### 2.3 Automated Detection Catches Only 25-35% of Issues

Overlays rely on automated rule-based detection. Automated scanning catches at most 25-35% of WCAG violations. The remaining 65-75% require human judgment: context, reading order, cognitive load, screen reader announcement quality, and actual task flows.

Source: [AccessibilityChecker.org](https://www.accessibilitychecker.org/blog/accessibility-remediation/), [Deque](https://www.deque.com/blog/auditing-design-systems-for-accessibility/)

### 2.4 Overlays Increase Violations

Adrian Roselli's testing demonstrated that enabling the accessiBe overlay **increased** WCAG violations:

- **Deque Axe:** violations went from 4 to 12 after enabling overlay
- **ARC Toolkit:** violations went from 19 to 38 after enabling overlay

The overlay actively made accessibility worse.

Source: [Adrian Roselli](https://adrianroselli.com/2020/06/accessibe-will-get-you-sued.html)

### 2.5 Performance and Security Costs

Overlay scripts add page weight and execution time, disproportionately affecting users on older devices or slower connections — the same users statistically more likely to use assistive technology. Installing an overlay also means allowing a third party to inject and execute arbitrary JavaScript on every page, creating a supply chain security risk for zero accessibility benefit.

---

## 3. Who Opposes Overlays

### 3.1 National Federation of the Blind (NFB)

The NFB Board of Directors found that accessiBe "engages in behavior that is harmful to the advancement of blind people in society," including dismissing blind users' concerns, treating blind experts "shabbily and disrespectfully," and promoting "false claims of attaining WCAG compliance through the integration of one line of code." The NFB revoked accessiBe's convention sponsorship and banned the company from their platform (June 2021).

Source: [NFB Statement](https://nfb.org/about-us/press-room/national-convention-sponsorship-statement-regarding-accessibe)

### 3.2 Over 1,000 Accessibility Professionals

The [Overlay Fact Sheet](https://overlayfactsheet.com/en/) is signed by over 1,000 professionals worldwide, including:

- Contributors and editors for WCAG, ARIA, and HTML specifications
- Internal accessibility leads at Google, Microsoft, Apple, BBC, Shopify, eBay, Target, CVS Health, Dell, Lyft, Expedia
- Consultants from 20+ countries

The statement declares that overlays do not meet legal requirements, do not provide adequate accessibility, and in many cases make accessibility worse.

### 3.3 Real Users Actively Block Overlays

The browser extension [AccessiByeBye](https://www.accessibyebye.org/) exists specifically to block overlay scripts. Its existence demonstrates that disabled users find overlays harmful enough to install software to remove them.

### 3.4 Overlays as Instant-Leave Triggers

WebAIM Screen Reader Survey respondents and blind user experience reports identify overlay widgets that fire alert messages on page arrival as immediate page-abandonment triggers.

Source: [Allyant](https://allyant.com/blog/my-experience-of-navigating-the-web-as-a-blind-user/)

---

## 4. Legal Risk

### 4.1 FTC $1 Million Fine (January 2025)

The FTC ordered accessiBe to pay $1 million for deceptive marketing. Findings:

- accessiBe falsely claimed its AI product could make any website WCAG-compliant within 48 hours
- The product failed to make basic components accessible: navigation menus, form fields, image descriptions
- accessiBe paid for endorsements disguised as impartial reviews without disclosure
- Consent order prohibits future deceptive practices (finalized April 2025)

Source: [FTC Press Release](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-order-requires-online-marketer-pay-1-million-deceptive-claims-its-ai-product-could-make-websites)

### 4.2 Overlay Users Get Sued at Scale

UsableNet ADA lawsuit tracking:

- **2022:** ~600 companies with an overlay were sued
- **2024:** 1,023 lawsuits against overlay users — **25% of all ADA web accessibility lawsuits**
- **H1 2025:** 456 lawsuits (22.6% of filings) targeted sites with overlays installed

Having an overlay does not reduce lawsuit risk. Plaintiffs frequently cite the overlay widget itself as a barrier.

Source: [UsableNet 2025 Midyear Report](https://info.usablenet.com/hubfs/2025-MidYear-Report-FINAL.pdf), [Accessibility.Works 2024](https://www.accessibility.works/blog/ada-lawsuit-trends-statistics-2024-summary/)

### 4.3 UserWay Also Sued (2025)

In February 2025, a small business sued UserWay after its overlay failed to deliver on accessibility promises.

Source: [Lainey Feingold](https://www.lflegal.com/2025/02/userway-overlay-lawsuit/)

### 4.4 SLAPP Lawsuits Against Critics

AudioEye sued Adrian Roselli — a globally recognized accessibility expert — for his public criticism of overlay products. The lawsuit was condemned as a SLAPP and dropped January 2024. accessiBe attempted a W3C Community Group ("Accessibility at the Edge") documented as an overlay industry smoke screen.

Source: [LFLegal](https://www.lflegal.com/2023/07/adrian-roselli-slapp-lawsuit/), [Adrian Roselli](https://adrianroselli.com/2022/09/accessibility-at-the-edge-w3c-cg-is-an-overlay-smoke-screen.html)

---

## 5. Detection Patterns

When reviewing code or sites, flag these indicators of overlay installation:

### 5.1 Script Tags Loading Overlay CDNs

```
acsbapp.com, acsbap.com          → accessiBe
accesswidget, accessibe          → accessiBe
cdn.userway.org                  → UserWay
audioeye.com, audioeye-cdn       → AudioEye
equalweb                         → EqualWeb
facil-iti                        → FACIL'iti
truabilities                     → TruAbilities
maxaccess                        → MaxAccess
reciteme                         → ReciteMe
```

### 5.2 DOM Indicators

- Floating accessibility icon (wheelchair symbol, typically bottom-right)
- Elements with class names containing: `acsb`, `userway`, `audioeye`, `equalweb`
- `div` or `iframe` elements injected at end of `<body>` with vendor identifiers
- Global variables: `window._acsb`, `window.UserWay`
- `data-acsb` or vendor-prefixed data attributes on `<body>` or `<html>`

### 5.3 Agent Action on Detection

When you detect an overlay in code:

1. **Flag it for removal.** The overlay is adding legal risk, degrading performance, harming disabled users, and creating a false sense of compliance.
2. **Do not suggest keeping it "temporarily."** There is no safe interim period — the overlay is actively harmful from the moment it is installed.
3. **Recommend the real remediation path** (see Section 6).

For detailed detection patterns, see: [references/detection-patterns.md](references/detection-patterns.md)

---

## 6. What to Recommend Instead

When asked about accessibility fixes, recommend these — never an overlay:

### 6.1 Manual Accessibility Audit

Hire qualified accessibility professionals (ideally including people with disabilities) to audit against WCAG 2.1 AA or 2.2 AA. Automated tools (axe, Lighthouse, WAVE) catch only 25-35% of issues. Manual testing with screen readers (NVDA, JAWS, VoiceOver), keyboard-only navigation, and zoom/reflow testing is required.

### 6.2 Fix the Source Code

Remediate the actual HTML, CSS, and JavaScript:

- Semantic HTML: proper headings, landmarks, lists, tables
- Form labels associated with inputs via `for`/`id` or nesting
- Meaningful alt text written by humans who understand the content's purpose
- Keyboard navigation following ARIA Authoring Practices patterns
- Focus management for dynamic content
- Color contrast meeting 4.5:1 (text) and 3:1 (UI components) minimums

### 6.3 Accessible Design Systems

Fix accessibility at the component level. When a component is fixed, every instance inherits the fix. Recommended libraries: Radix UI, React Aria (Adobe), GOV.UK Design System, US Web Design System (USWDS), Reach UI, Headless UI.

### 6.4 Integrate Into CI/CD

- Run axe-core in CI pipelines to catch regressions
- Require accessibility checks in code review
- Include screen reader testing in QA

### 6.5 User Testing With Disabled People

Test with actual users who rely on assistive technology. No automated testing or expert review replaces observing a blind user navigate your checkout flow or a motor-impaired user trying to complete your form.

### 6.6 Accessibility Roadmap

1. Fix highest-impact barriers first (navigation, forms, critical user flows)
2. Establish ongoing monitoring
3. Train development teams on accessible coding patterns
4. Document accessibility in component specifications

---

## 7. Responding to Common Arguments

| Argument | Response |
|---|---|
| "It's better than nothing" | No. Overlays increase violations (Roselli testing: 4→12 axe violations). They are worse than nothing. |
| "It's a temporary fix while we work on real accessibility" | Overlays create legal exposure from day one. 25% of ADA lawsuits target overlay users. There is no safe interim. |
| "The vendor guarantees compliance" | The FTC fined accessiBe $1M for exactly this false claim. No overlay can guarantee compliance. |
| "We can't afford a full remediation" | You can't afford the lawsuit. Start with the highest-impact fixes: headings, form labels, alt text, keyboard navigation. These cost engineering time, not vendor contracts. |
| "Our legal team recommended it" | Share the FTC consent order, the 1,000+ lawsuits/year data, and the NFB statement. Legal teams recommending overlays are not aware of the evidence. |

---

## 8. Cross-References

- `a11y-audit` — how to conduct a proper accessibility audit
- `testing-strategy` — automated and manual testing approaches
- `aria-decision-framework` — correct ARIA usage (overlays inject ARIA incorrectly)
- `alt-text-quality` — why AI-generated alt text (used by overlays) fails
- `focus-management` — keyboard navigation that overlays cannot fix
- `form-a11y` — form accessibility that requires source code changes

For evidence and detection details:

- [references/overlay-evidence.md](references/overlay-evidence.md) — full evidence base with citations
- [references/detection-patterns.md](references/detection-patterns.md) — code patterns to detect overlays
- [references/sources.yaml](references/sources.yaml) — provenance for all cited sources
