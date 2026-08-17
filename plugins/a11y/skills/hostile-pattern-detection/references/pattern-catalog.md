# Hostile Pattern Catalog: Alternatives and Implementation
## Contents

- [Carousel Alternatives](#carousel-alternatives)
- [Infinite Scroll → Pagination or "Load More"](#infinite-scroll-pagination-or-load-more)
  - [Option A: Pagination (Preferred)](#option-a-pagination-preferred)
  - [Option B: "Load More" Button](#option-b-load-more-button)
- [Hover-Only → Focus Parity + Persistent Content](#hover-only-focus-parity-persistent-content)
  - [Tooltip with Focus Parity](#tooltip-with-focus-parity)
  - [Better Alternative: Persistent Visible Content](#better-alternative-persistent-visible-content)
- [Auto-Play → User-Initiated Playback](#auto-play-user-initiated-playback)
  - [Video: Muted with Visible Controls](#video-muted-with-visible-controls)
- [CAPTCHA → Bot Detection Without Human Testing](#captcha-bot-detection-without-human-testing)
  - [Option A: Honeypot Field (Preferred)](#option-a-honeypot-field-preferred)
  - [Option B: Proof-of-Work (Invisible Challenge)](#option-b-proof-of-work-invisible-challenge)
  - [Option C: Rate Limiting + Server-Side Detection](#option-c-rate-limiting-server-side-detection)
  - [Option D: Multi-Factor Authentication](#option-d-multi-factor-authentication)
- [Cookie Banners → Accessible Consent](#cookie-banners-accessible-consent)
- [Placeholder Text → Visible Labels](#placeholder-text-visible-labels)
- [Dark Patterns → Transparent Design](#dark-patterns-transparent-design)
  - [Checklist](#checklist)
  - [Sources](#sources)


This reference provides implementation-level guidance for each hostile pattern's alternative. The SKILL.md explains why each pattern is hostile; this document explains what to build instead.

---

## Carousel Alternatives

See [carousel alternatives](carousel-alternatives.md) for detailed implementations.

---

## Infinite Scroll → Pagination or "Load More"

### Option A: Pagination (Preferred)

```html
<nav aria-label="Search results pages">
  <ul>
    <li><a href="?page=1" aria-current="page">1</a></li>
    <li><a href="?page=2">2</a></li>
    <li><a href="?page=3">3</a></li>
    <li><a href="?page=4">4</a></li>
    <li><a href="?page=5">5</a></li>
  </ul>
</nav>
```

**Why it works:** Users know how much content exists, can bookmark pages, can return to specific positions, and the footer is always reachable.

### Option B: "Load More" Button

```html
<div id="results-container" aria-live="polite">
  <!-- Existing items -->
</div>
<button id="load-more" aria-label="Load more results (showing 20 of 143)">
  Load more results
</button>
```

```javascript
loadMoreBtn.addEventListener('click', async () => {
  loadMoreBtn.setAttribute('aria-busy', 'true');
  loadMoreBtn.textContent = 'Loading...';
  const newItems = await fetchMore();
  container.append(...newItems);
  // Update button label with new count
  loadMoreBtn.textContent = 'Load more results';
  loadMoreBtn.setAttribute('aria-label',
    `Load more results (showing ${currentCount} of ${totalCount})`);
  loadMoreBtn.setAttribute('aria-busy', 'false');
  // Move focus to first new item for discoverability
  newItems[0].focus();
});
```

**Key requirements:**
- Button is a real `<button>`, keyboard accessible by default
- `aria-busy` indicates loading state
- `aria-live="polite"` on container announces new content
- Focus moves to first new item after load
- Count communicates progress ("showing 20 of 143")

---

## Hover-Only → Focus Parity + Persistent Content

### Tooltip with Focus Parity

```html
<button aria-describedby="tooltip-1">Settings</button>
<div role="tooltip" id="tooltip-1" class="tooltip">
  Configure your account preferences
</div>
```

```css
.tooltip {
  display: none;
  position: absolute;
}
/* Both hover AND focus trigger the tooltip */
button:hover + .tooltip,
button:focus + .tooltip {
  display: block;
}
/* Respect reduced motion */
@media (prefers-reduced-motion: reduce) {
  .tooltip { transition: none; }
}
```

**WCAG 1.4.13 requirements (all three must be met):**
1. **Dismissable:** User can close popup without moving pointer (Escape key)
2. **Hoverable:** User can move pointer over the popup content without it disappearing
3. **Persistent:** Content stays visible until user dismisses, moves focus, or information becomes invalid

### Better Alternative: Persistent Visible Content

If the information is important enough to put in a tooltip, put it in the page instead:

```html
<label for="username">Username</label>
<input type="text" id="username" aria-describedby="username-hint">
<p id="username-hint" class="hint">3-20 characters, letters and numbers only</p>
```

---

## Auto-Play → User-Initiated Playback

### Video: Muted with Visible Controls

```html
<div class="video-container">
  <video
    id="hero-video"
    muted
    playsinline
    poster="hero-poster.jpg"
    aria-label="Product demonstration video"
  >
    <source src="hero.mp4" type="video/mp4">
    <track kind="captions" src="hero-captions.vtt" srclang="en" label="English">
  </video>
  <button id="play-btn" aria-label="Play video with sound">
    Play Video
  </button>
</div>
```

```javascript
// Respect user motion preferences
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

if (prefersReducedMotion.matches) {
  video.pause();
  video.removeAttribute('autoplay');
  playBtn.textContent = 'Play Video';
} else {
  // Auto-play muted is acceptable, but controls must be accessible
  video.play();
  playBtn.textContent = 'Pause Video';
  playBtn.setAttribute('aria-label', 'Pause video');
}
```

**Rules:**
- Never auto-play audio
- If auto-play video, always muted with poster image fallback
- Play/pause control before the video in tab order
- Always provide captions (`<track kind="captions">`)
- Respect `prefers-reduced-motion` — disable auto-play entirely

---

## CAPTCHA → Bot Detection Without Human Testing

### Option A: Honeypot Field (Preferred)

```html
<form>
  <label for="email">Email</label>
  <input type="email" id="email" name="email" required>

  <!-- Honeypot: visually hidden, not in tab order -->
  <div aria-hidden="true" style="position:absolute;left:-9999px;">
    <label for="website">Leave blank</label>
    <input type="text" id="website" name="website" tabindex="-1" autocomplete="off">
  </div>

  <button type="submit">Subscribe</button>
</form>
```

```python
# Server-side: reject submissions where honeypot is filled
if request.form.get('website'):
    return abort(400)  # Bot detected
```

**Why it works:** Bots fill all fields. Humans never see or interact with the honeypot. Screen readers skip it due to `aria-hidden`. Keyboard users skip it due to `tabindex="-1"`. No CAPTCHA challenge for anyone.

### Option B: Proof-of-Work (Invisible Challenge)

Services like **Friendly Captcha** and **Cloudflare Turnstile** challenge the browser, not the human. The device solves a computational puzzle while the user fills out the form. No interaction required from the user at all.

### Option C: Rate Limiting + Server-Side Detection

```python
# Combine multiple signals — no user interaction needed
def is_likely_bot(request):
    checks = [
        check_rate_limit(request.ip),          # Too many requests
        check_request_timing(request),          # Form submitted too fast
        check_ip_reputation(request.ip),        # Known bot IP
        check_honeypot(request.form),           # Honeypot filled
        check_user_agent(request.headers),      # Missing/suspicious UA
    ]
    return any(checks)
```

### Option D: Multi-Factor Authentication

For high-security contexts. Must offer multiple modality options:
- Push notification (accessible to most users)
- Email verification (accessible to most users)
- SMS code (excludes some deaf users if sole option)
- Hardware security key (requires motor ability to insert/tap)

Never rely on a single modality.

---

## Cookie Banners → Accessible Consent

```html
<dialog id="cookie-banner" aria-labelledby="cookie-heading" open>
  <h2 id="cookie-heading">Cookie preferences</h2>
  <p>We use cookies for site functionality and analytics.</p>

  <fieldset>
    <legend>Cookie categories</legend>
    <label>
      <input type="checkbox" checked disabled> Essential (required)
    </label>
    <label>
      <input type="checkbox" name="analytics"> Analytics
    </label>
    <label>
      <input type="checkbox" name="marketing"> Marketing
    </label>
  </fieldset>

  <!-- Equal prominence: both are <button>, same size, same contrast -->
  <div class="cookie-actions">
    <button type="button" id="reject-all">Reject All</button>
    <button type="button" id="accept-all">Accept All</button>
  </div>
</dialog>
```

```javascript
const banner = document.getElementById('cookie-banner');
// Move focus to banner on load
banner.querySelector('h2').focus();

// Focus trap: Tab cycles within the banner only
// (native <dialog> handles this when used with showModal())

// Return focus after dismissal
function closeBanner() {
  banner.close();
  document.querySelector('main').focus();
}
```

**Requirements:**
- Use `<dialog>` for native focus trapping
- "Reject All" and "Accept All" are both `<button>` elements with equal visual weight
- Focus moves to banner on appearance
- Focus returns to main content on dismissal
- Plain language descriptions — no legal jargon
- All checkboxes have programmatic `<label>` associations
- Test with NVDA, JAWS, VoiceOver before deployment

---

## Placeholder Text → Visible Labels

```html
<!-- WRONG: placeholder as label -->
<input type="email" placeholder="Email address">

<!-- RIGHT: visible persistent label -->
<label for="email">Email address</label>
<input type="email" id="email" aria-describedby="email-hint">
<p id="email-hint" class="hint">e.g., name@example.com</p>
```

**The safest pattern:**
1. Visible `<label>` above the field (never disappears)
2. Hint text below the field via `aria-describedby` (never disappears)
3. No `placeholder` attribute at all

---

## Dark Patterns → Transparent Design

### Checklist

- [ ] All options (accept, reject, cancel, subscribe, unsubscribe) use `<button>` or `<a>`
- [ ] All options have equal visual prominence (size, contrast, position)
- [ ] "Cancel" and "unsubscribe" are early in tab order, not buried
- [ ] Copy uses active voice, no double negatives, one idea per sentence
- [ ] Opt-out requires the same number of steps as opt-in
- [ ] No countdown timers without genuine justification
- [ ] All interactive elements have accessible names that describe their actual function
- [ ] Tested with a screen reader: can the user distinguish between opting in and opting out?

### Sources

- [PMC: Inaccessible and Deceptive](https://pmc.ncbi.nlm.nih.gov/articles/PMC12188898/)
- [UX Planet: Evil UX Patterns and Cognitive Disability](https://uxplanet.org/the-disproportionate-impact-of-evil-ux-patterns-on-the-cognitively-disabled-community-c6b9eee71682)
- [netz-barrierefrei: Dark Patterns and Digital Accessibility](https://www.netz-barrierefrei.de/en/patterns.html)
