# Overlay Evidence Base

Detailed evidence supporting the overlay-resistance skill. Each claim in SKILL.md traces to sources documented here.

---

## 1. Technical Failures

### 1.1 Accessibility Tree Timing

Screen readers and assistive technologies build the accessibility tree from raw HTML before JavaScript executes. Overlays modify the DOM after this parsing is complete, meaning their changes may not be reflected in the accessibility tree that assistive technology is already using.

- TestParty: [Death of Overlays](https://testparty.ai/blog/death-of-overlays)
- Zoonou: [Why Overlays Don't Work](https://zoonou.com/blog/i-use-assistive-tech-heres-why-accessibility-overlays-dont-work/)

### 1.2 Automated Detection Limits

Industry consensus places automated WCAG detection at 25-35% of total violations. The remaining 65-75% require human judgment for context, reading order, cognitive load, screen reader announcement quality, and task flow evaluation.

- AccessibilityChecker.org: [Accessibility Remediation](https://www.accessibilitychecker.org/blog/accessibility-remediation/)
- Deque: [Auditing Design Systems](https://www.deque.com/blog/auditing-design-systems-for-accessibility/)

### 1.3 Overlays Increase Violations (Measured)

Adrian Roselli tested accessiBe's overlay on a page and measured WCAG violations before and after:

| Tool | Before Overlay | After Overlay | Change |
|---|---|---|---|
| Deque Axe | 4 violations | 12 violations | +200% |
| ARC Toolkit | 19 violations | 38 violations | +100% |

The overlay doubled or tripled the number of accessibility violations.

- Adrian Roselli: [accessiBe Will Get You Sued](https://adrianroselli.com/2020/06/accessibe-will-get-you-sued.html)

### 1.4 What Overlays Cannot Fix

Overlays operate at the DOM/CSS level and cannot address:

- Semantic HTML structure (heading hierarchy, landmark regions)
- Form label associations at the HTML level
- Keyboard navigation requiring restructured event handlers
- Meaningful alt text (requires human understanding of content purpose)
- PDF, video, Canvas, or SVG accessibility
- Server-rendered content or SPA routing issues
- Reading order determined by DOM structure

- TestParty: [Overlay vs Source Code Fixes](https://testparty.ai/blog/accessibility-overlay-vs-source-code-fixes)
- ASU IT Accessibility: [Overlays](https://accessibility.asu.edu/articles/overlays)

---

## 2. Legal Evidence

### 2.1 FTC Enforcement Action Against accessiBe

**Date:** January 2025 (finalized April 2025)
**Penalty:** $1,000,000
**Findings:**
- False claim that AI product could make any website WCAG-compliant within 48 hours
- Product failed to make basic components accessible (navigation, forms, images)
- Paid endorsements disguised as impartial third-party reviews without disclosure
- Consent order prohibits future deceptive practices

- FTC: [Press Release](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-order-requires-online-marketer-pay-1-million-deceptive-claims-its-ai-product-could-make-websites)
- FTC: [Case Page](https://www.ftc.gov/legal-library/browse/cases-proceedings/2223156-accessibe-inc)

### 2.2 ADA Lawsuit Volume Against Overlay Users

| Year | Lawsuits Against Overlay Users | % of Total ADA Web Lawsuits |
|---|---|---|
| 2022 | ~600 | — |
| 2024 | 1,023 | 25% |
| H1 2025 | 456 | 22.6% |

- UsableNet: [2025 Midyear Report](https://info.usablenet.com/hubfs/2025-MidYear-Report-FINAL.pdf)
- Accessibility.Works: [2024 Lawsuit Trends](https://www.accessibility.works/blog/ada-lawsuit-trends-statistics-2024-summary/)

### 2.3 Named Lawsuits Citing Overlay Failures

| Case | Issue |
|---|---|
| Klaus v. Upright Technologies | Screen readers could not access the overlay itself |
| Douglass v. Masterbuilt | "Screen Reader Mode" restricted access, prevented purchases |
| Murphy v. Eyebobs | Users trapped navigating the overlay, unable to complete transactions |
| Fischler v. Dorai Homes | Missing alt text despite AI claims |
| Sherwin v. accessiBe | Class action: breach of contract, inadequate legal support |

- Adrian Roselli: [accessiBe Will Get You Sued](https://adrianroselli.com/2020/06/accessibe-will-get-you-sued.html)

### 2.4 UserWay Lawsuit (February 2025)

A small business sued UserWay after its overlay failed to deliver on promises.

- Lainey Feingold: [UserWay Overlay Lawsuit](https://www.lflegal.com/2025/02/userway-overlay-lawsuit/)

---

## 3. Disability Community Opposition

### 3.1 National Federation of the Blind

The NFB Board of Directors reviewed accessiBe and concluded the company "engages in behavior that is harmful to the advancement of blind people in society." Specific findings:

- "Peremptorily and scornfully dismisses the concerns blind people have"
- "Treats blind access technology experts shabbily and disrespectfully"
- "Disparages the blind in the press"
- "Overstates the effectiveness of automated testing"
- "Promotes false claims of attaining WCAG compliance through one line of code"

Convention sponsorship revoked June 22, 2021.

- NFB: [Convention Sponsorship Statement](https://nfb.org/about-us/press-room/national-convention-sponsorship-statement-regarding-accessibe)

### 3.2 Overlay Fact Sheet (1,000+ Signatories)

Signed by accessibility professionals including WCAG/ARIA/HTML spec contributors, accessibility leads at Google, Microsoft, Apple, BBC, Shopify, eBay, Target, CVS Health, Dell, Lyft, Expedia, and consultants from 20+ countries.

- [Overlay Fact Sheet](https://overlayfactsheet.com/en/)
- Karl Groves: [Overlay Fact Sheet Explanation](https://karlgroves.com/overlay-fact-sheet-what-it-is-and-how-to-make-it-work-for-you/)

### 3.3 AccessiByeBye Browser Extension

Users install this extension specifically to block overlay scripts from accessiBe, AudioEye, EqualWeb, MaxAccess, TruAbilities, User1st, and UserWay.

- [AccessiByeBye](https://www.accessibyebye.org/)

### 3.4 User Experience Reports

Blind users report overlay widgets as instant page-abandonment triggers. Overlays fire alert messages on arrival, disrupting screen reader navigation. WebAIM Screen Reader Survey respondents and blind user experience blogs consistently identify overlays as harmful.

- Allyant: [Navigating the Web as a Blind User](https://allyant.com/blog/my-experience-of-navigating-the-web-as-a-blind-user/)
- WebAIM: [Screen Reader Survey #10](https://webaim.org/projects/screenreadersurvey10/)

---

## 4. SLAPP Lawsuits Against Critics

AudioEye sued Adrian Roselli for public criticism of overlays. Condemned as a SLAPP (Strategic Lawsuit Against Public Participation). Dropped January 3, 2024.

accessiBe attempted a W3C Community Group called "Accessibility at the Edge" — documented as an overlay industry smoke screen.

- LFLegal: [Roselli SLAPP](https://www.lflegal.com/2023/07/adrian-roselli-slapp-lawsuit/)
- Adrian Roselli: [Accessibility at the Edge](https://adrianroselli.com/2022/09/accessibility-at-the-edge-w3c-cg-is-an-overlay-smoke-screen.html)
