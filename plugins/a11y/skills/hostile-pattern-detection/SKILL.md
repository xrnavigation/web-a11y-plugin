---
name: hostile-pattern-detection
description: Detects and prevents hostile-by-design UI patterns that disproportionately harm disabled users. Auto-invokes when creating carousels, infinite scroll, hover-only interactions, auto-playing media, CAPTCHAs, cookie consent banners, or when considering accessibility overlay widgets. These patterns may be technically "fixable" but are fundamentally hostile — the skill recommends alternatives.
allowed-tools: Read, Glob, Grep
---

# Hostile Pattern Detection

> "I approach every digital task with trepidation, caution, and a fair degree of uncertainty — consistently asking 'Will it work for me?'"
> — A blind screen reader user ([UsableNet](https://blog.usablenet.com/a-screen-reader-users-honest-take))

> "Participants experienced manipulative effects regardless of designer intent."
> — PMC study on deceptive design and disability ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12188898/))

These patterns are not just inaccessible. They are hostile by design. They remove user agency, punish disability, and create barriers that persist even when you add ARIA attributes and keyboard handlers. The right response is not to make them "accessible" — it is to stop building them.

---

## 1. Why These Patterns Are Hostile

An inaccessible pattern fails to meet a spec. A hostile pattern conflicts with how disabled users interact with the web at a fundamental level — the interaction model itself is the problem.

**The common thread:** Every pattern in this skill removes user agency. Carousels advance without permission. Infinite scroll loads without request. Overlays apply settings without consent. Auto-play starts without action. CAPTCHAs gatekeep without alternatives. Cookie banners obscure without escape. Hover interactions hide without fallback. Placeholders disappear without warning. Dark patterns manipulate without transparency.

**The compounding effect:** These patterns rarely appear alone. A typical page combines a carousel, a cookie banner, auto-playing video, and placeholder-only forms. A screen reader user arriving hears: an overlay alert, auto-playing audio competing with their screen reader, a cookie banner they cannot dismiss, a carousel cycling content they cannot control, and form fields with no labels. Each pattern independently creates barriers; together, they create an experience that is fundamentally unusable.

**The antidote is always the same:** Give the user control.

---

## 2. The Patterns

### 2.1 Carousels / Sliders

**What it is:** Auto-rotating panels cycling through content with navigation dots and prev/next arrows.

**Who it hurts and how:**
- **Screen reader users:** Non-visible slides remain in the accessibility tree. Changes are not announced. Users cannot determine position or total count. ([WebAIM](https://webaim.org/techniques/carousels/))
- **Keyboard users:** Focus lands on hidden slides, gets trapped, or skips the carousel entirely.
- **Cognitive/motor users:** Content disappears before it can be read or clicked. NNGroup: "Moving UI elements usually reduce accessibility, particularly for users with motor skill issues." ([NNGroup](https://www.nngroup.com/articles/auto-forwarding/))
- **Vestibular users:** Slide transitions trigger dizziness, vertigo, and nausea.

**Why "fixing" it is not enough:** The fundamental model — auto-advancing content with partial visibility — conflicts with sequential AT navigation. Even an "accessible" carousel forces screen reader users into a paradigm designed for visual scanning. And less than 1% of visitors click carousel features anyway. ([Notre Dame study, cited by multiple sources](https://www.nngroup.com/articles/designing-effective-carousels/))

**Build this instead:** Static content. Paginated sections. Accordion panels. Tabbed interfaces (with proper ARIA — see `a11y-tabs` skill). If a carousel is truly required, see [references/carousel-alternatives.md](references/carousel-alternatives.md).

### 2.2 Infinite Scroll

**What it is:** New content auto-loads as the user scrolls toward the bottom, creating an endlessly extending page.

**Who it hurts and how:**
- **Keyboard users:** Tabbing does not trigger scroll — keyboard users cannot cause new content to load. WordPress removed infinite scroll from its Media Library for this reason. This is effectively a keyboard trap. ([Deque](https://www.deque.com/blog/infinite-scrolling-rolefeed-accessibility-issues/))
- **Speech recognition users (Dragon):** Have no way to trigger the scroll-based loading mechanism. Completely excluded.
- **Screen reader users:** Dynamic loading is not announced. Users think the page is simply very long. The footer is unreachable.
- **Cognitive users:** No way to bookmark, return to, or remember a specific item. Removes natural stopping points — disproportionately affects ADHD and impulse-control difficulties.

**Why "fixing" it is not enough:** `role="feed"` only helps screen reader users. It does nothing for keyboard, motor, speech recognition, or cognitive accessibility. Even with `role="feed"`, less experienced AT users may not recognize the widget pattern.

**Build this instead:** Pagination with numbered links. A "Load more" button with `aria-live` announcement. Never auto-load.

### 2.3 Hover-Only Interactions

**What it is:** Content or functionality revealed only on mouse hover — tooltips, dropdowns, preview cards, expanded navigation.

**Who it hurts and how:**
- **Keyboard users:** Cannot trigger hover. Completely excluded. Violates WCAG 2.1.1 (Keyboard, Level A). ([BOIA](https://www.boia.org/blog/hover-actions-and-accessibility-addressing-a-common-wcag-violation))
- **Touch/mobile users:** No hover state exists. Affects all mobile users, not just disabled users.
- **Motor-impaired users:** Cannot maintain precise hover position long enough to read popup content.
- **Low-vision users with magnification:** Popups extend beyond the magnified viewport and cannot be dismissed without moving the pointer. ([W3C SC 1.4.13](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html))
- **Speech recognition users:** Voice control cannot trigger hover states.

**Why "fixing" it is not enough:** The pattern creates an invisible capability requirement: you must have a pointing device, the fine motor control to position it, and the ability to maintain that position. WCAG 1.4.13 requires hover content be dismissable, hoverable, and persistent — most implementations fail all three.

**Build this instead:** Ensure `:hover` and `:focus` parity. Provide click/tap alternatives. Use visible, persistent content. If information is important enough to exist, it is important enough to be visible.

### 2.4 Auto-Playing Media

**What it is:** Audio or video that begins playing automatically on page load.

**Who it hurts and how:**
- **Screen reader users:** Auto-playing audio competes with and drowns out screen reader speech. Two simultaneous audio streams — neither parseable. ([BOIA](https://www.boia.org/blog/why-autoplay-is-an-accessibility-no-no))
- **Epileptic users:** Flashing video content triggers photosensitive seizures. Twitter removed Vine ads in 2015 after six-second flashing videos triggered episodes.
- **Vestibular users:** Motion triggers dizziness, vertigo, and nausea.
- **ADHD users:** Unexpected audio/video disrupts focus and makes concentration on intended content extremely difficult.

**Why "fixing" it is not enough:** WCAG 1.4.2 allows auto-play if controls exist and audio stops within 3 seconds. But even a 2-second auto-play can startle, disorient, or trigger a seizure. The "3 second" rule is a minimum, not a safe harbor. The hostility is compounded when controls are unlabeled, keyboard-inaccessible, or hover-only.

**Build this instead:** Never auto-play audio. Never auto-play video with audio. If auto-play video is required, start muted with obvious unmute control. Respect `prefers-reduced-motion`. Provide captions and transcripts.

### 2.5 CAPTCHAs

**What it is:** Challenge-response tests to distinguish humans from bots — distorted text, image classification, audio challenges, puzzle sliders.

**Who it hurts and how:**
- **Blind users (most severely):** WebAIM Survey #10 (2024, 1,539 respondents) ranked CAPTCHA as the most problematic item on the web — unchanged for 14 years. Google reCAPTCHA "often labels screen reader behavior as a bot." ([WebAIM](https://webaim.org/projects/screenreadersurvey10/))
- **Deaf users:** Audio CAPTCHAs use intentionally distorted speech with background noise.
- **Deafblind users:** Zero CAPTCHA options exist. Neither visual nor audio alternatives work.
- **Cognitive/motor users:** Puzzle challenges require fine motor control and cognitive processing under time pressure.

**Why "fixing" it is not enough:** The W3C itself acknowledges this is fundamentally unsolved: "Interactive CAPTCHA approaches inherently exclude many people with disabilities, resulting in a denial of service to these users." The pattern is a Turing test that punishes disability. ([W3C](https://www.w3.org/TR/turingtest/))

**Build this instead:** Honeypot fields. Rate limiting. Server-side bot detection. Proof-of-work challenges (Friendly Captcha, Cloudflare Turnstile). Multi-factor authentication with multiple modality options. See [references/pattern-catalog.md](references/pattern-catalog.md) for implementation details.

### 2.6 Cookie Consent Banners

**What it is:** Modal or fixed-position overlays requesting cookie tracking consent, required by GDPR/ePrivacy.

**Who it hurts and how:**
- **Screen reader users:** Banners at DOM end are never encountered. Missing `role="dialog"` or `aria-modal` means no announcement. Checkboxes lack label associations. ([Smashing Magazine](https://www.smashingmagazine.com/2023/04/potentially-dangerous-non-accessibility-cookie-notices/))
- **Keyboard users:** Focus not trapped in banner — users tab past it into obscured content. Controls are often `<div>`s without keyboard support.
- **Cognitive users:** "Reject" is deliberately harder to find than "Accept" — smaller text, lower contrast, more clicks. Dark pattern integration.

**Why "fixing" it is not enough:** Inaccessible consent is legally invalid consent. Under GDPR, consent must be "freely given, specific, informed and unambiguous." If a user cannot perceive, understand, or operate the consent mechanism, no valid consent has been obtained — the tool meant to ensure privacy compliance creates accessibility non-compliance.

**Build this instead:** Use `<dialog>` with focus management. Use `<button>` for actions, `<label>` for checkboxes. Make "Reject All" as prominent and accessible as "Accept All." Write descriptions in plain language. Test with AT before deployment.

### 2.7 Accessibility Overlays

**What it is:** Third-party widgets (accessiBe, UserWay, AudioEye, EqualWeb) claiming to make websites WCAG-compliant via a single script injection.

**Who it hurts and how:**
- **Screen reader users:** Unsolicited alerts on every page load. Unwanted headings injected. Focus jumps unpredictably. One user blocked accessiBe in their Windows Hosts file to regain account access.
- **All AT users:** Overlays conflict with users' own carefully configured AT setups.
- **Privacy:** Overlays detect AT use without consent, exposing disability status. Force disability disclosure through "profiles" (e.g., "Screen Reader Profile"). ([Overlay Fact Sheet](https://overlayfactsheet.com/en/))

**Why "fixing" it is not enough:** Overlays cannot be fixed — they are the problem. Automated tools detect only 25-30% of accessibility issues. The remaining 70-75% require human judgment and code changes. WebAIM Survey: 72% of disabled respondents rated overlays "not at all" or "not very" effective. The FTC fined accessiBe $1 million (April 2025) for false advertising. 25% of digital accessibility lawsuits target overlay-equipped websites. The NFB banned accessiBe from their 2021 conference, calling the company "harmful." 1,000+ accessibility professionals signed the Overlay Fact Sheet. ([Adrian Roselli](https://adrianroselli.com/2022/03/overlays-underwhelm-a11y-nyc.html))

**Build this instead:** Fix accessibility at the source. See [references/overlay-evidence.md](references/overlay-evidence.md) for the complete evidence base.

### 2.8 Dark Patterns

**What it is:** Deceptive design practices — trick subscriptions, hidden fees, confusing opt-out language, buried unsubscribe links, artificial urgency, nagging.

**Who it hurts and how:**
- **Cognitive users:** Double negatives ("Check this box to opt out of not receiving emails") trap users with cognitive disabilities, dyslexia, or processing differences.
- **Screen reader users:** Unlabeled checkboxes cause accidental subscriptions. Countdown timers announced continuously create cognitive overload. Low-contrast buttons steer toward unwanted choices. ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12188898/))
- **Motor-impaired users:** "Roach motel" patterns — easy subscribe, hard cancel — create multi-step cancellation workflows that are physically painful.
- **All disabled users economically:** People with disabilities are disproportionately in lower socioeconomic strata. Financial dark patterns have disproportionate impact.

**Why "fixing" it is not enough:** Dark patterns weaponize accessibility barriers. A PMC study found six deceptive patterns amplified by access barriers: Sneaking (unlabeled checkboxes), Forced Action (inaccessible CAPTCHAs), Misdirection (low-contrast buttons), Obstruction (buried unsubscribe), Urgency (timer overload), and Nagging (popup focus disruption). The impact exists regardless of intent.

**Build this instead:** Clear, unambiguous copy. Active voice. No double negatives. Opt-out as easy as opt-in. All options equally keyboard-accessible with adequate contrast. Place cancel/reject/unsubscribe early in tab order.

### 2.9 Low-Contrast Placeholder Text as Labels

**What it is:** Using the `placeholder` attribute as a substitute for visible `<label>` elements, with the default light-gray color (~#757575) that fails WCAG 4.5:1 contrast.

**Who it hurts and how:**
- **Low-vision users:** Cannot read light-gray placeholder text. Field purpose is invisible before typing.
- **Cognitive users:** Placeholder disappears on focus, destroying the only label. Users with short-term memory issues, TBI, ADHD, or autism forget what the field requires. Some users think placeholder text is pre-populated data and submit forms without entering information. ([Deque](https://www.deque.com/blog/accessible-forms-the-problem-with-placeholders/))
- **Screen reader users:** AT support for placeholder-as-label is inconsistent. Some announce it, some do not.

**Why "fixing" it is not enough:** Increasing placeholder contrast creates a different problem — users confuse high-contrast placeholder with entered data. The `placeholder` attribute was designed for hints ("e.g., john@example.com"), not labels. NNGroup concluded "placeholders in form fields are harmful" — full stop. ([NNGroup](https://www.nngroup.com/articles/form-design-placeholders/))

**Build this instead:** Visible, persistent `<label>` elements with `for`/`id` association. Hint text outside the field via `aria-describedby`. The safest pattern: visible label above + hint text below + no placeholder at all. See `form-a11y` skill.

---

## 3. Detection Guidance

**If you are about to create any of these patterns, stop.**

Ask yourself:
1. **Am I removing user control?** If content changes, loads, plays, or disappears without the user choosing it — redesign.
2. **Am I hiding information?** If content is only visible on hover, disappears on interaction, or is buried behind multiple clicks — make it persistent and equally accessible.
3. **Am I testing the user's body?** If the interaction requires specific motor control, sensory ability, or cognitive processing speed — provide alternatives.
4. **Am I creating an illusion of compliance?** If you are adding an overlay, writing `role` attributes without behavior, or marking "Accept All" as the obvious choice — you are making things worse.
5. **Would this pattern survive if 100% of your users were keyboard-only?** If not — redesign.

---

## 4. Cross-References

For technical alternatives to hostile patterns, see these companion skills:

- `a11y-tabs` — tabbed interfaces (carousel alternative)
- `a11y-accordion` — disclosure/accordion patterns (carousel alternative)
- `a11y-dialog` — dialog and modal patterns (cookie banner, overlay implementation)
- `form-a11y` — form labels, hints, validation (placeholder alternative)
- `focus-management` — focus trapping, return, and announcement
- `cognitive-a11y` — plain language, predictable layouts, reduced cognitive load
- `aria-decision-framework` — when and how to use ARIA correctly

For detailed reference material:

- [references/carousel-alternatives.md](references/carousel-alternatives.md) — what to build instead of carousels
- [references/overlay-evidence.md](references/overlay-evidence.md) — the complete case against overlays
- [references/pattern-catalog.md](references/pattern-catalog.md) — per-pattern alternatives with implementation guidance
- [references/sources.yaml](references/sources.yaml) — provenance for all cited sources
