# Screen Reader Behavior Reference

## Native `<details>`/`<summary>`

| Screen Reader + Browser | Role Announced | State Announced | Headings in `<summary>` | Notes |
|------------------------|---------------|----------------|------------------------|-------|
| JAWS + Chrome | Button | Yes (expanded/collapsed) | Not announced, not navigable | Omits role re-announcement on state change |
| JAWS + Firefox | Button | Yes + toggle key hint | Not announced, not navigable | Announces Space/Enter key |
| NVDA + Chrome | Button | Yes, on state change | Announced but may suppress state | Bug: heading presence can suppress expanded/collapsed state |
| NVDA + Firefox | Button | Inconsistent | Announced | State changes not always announced |
| VoiceOver + macOS Safari | "Summary" role | Yes | Announced and navigable | Adding `role="button"` suppresses state announcement |
| VoiceOver + iOS Safari | No role | Yes | Not discoverable via form nav | Fixed in iOS 17.3 |
| TalkBack + Android | Disclosure triangle | Initial state only | N/A | State changes not announced until element re-focused |

Source: [O'Hara 2018](https://www.scottohara.me/blog/2018/09/03/details-and-summary.html), [Roselli 2023](https://adrianroselli.com/2023/08/progressively-enhanced-html-accordion.html)

### Key Takeaways for Native `<details>`

1. **VoiceOver/Safari is the most reliable** for native `<details>` — announces state and allows heading navigation inside `<summary>`. But adding `role="button"` breaks state announcements.
2. **JAWS destroys heading semantics** inside `<summary>` across browsers. If heading navigation is needed, use the ARIA accordion pattern.
3. **NVDA has bugs** where heading presence inside `<summary>` can suppress state announcements.
4. **TalkBack does not announce state changes** until the user re-focuses the element. Consider supplementing with `aria-live` announcements for Android users.
5. **iOS VoiceOver** had significant issues prior to iOS 17.3. The `<summary>` was not discoverable via form navigation.

---

## ARIA Accordion (`<button>` in `<h#>` Pattern)

| Screen Reader | Behavior |
|--------------|----------|
| All major (JAWS, NVDA, VoiceOver, TalkBack) | Button role announced reliably |
| All major | `aria-expanded` state changes announced on toggle |
| All major | Heading level announced and navigable via heading shortcuts (H key) |
| JAWS | `aria-controls` relationship discoverable via Ctrl+Alt+M |
| NVDA | `aria-controls` not surfaced to user but does not cause issues |
| VoiceOver | `aria-controls` not surfaced but structure is navigable |

Source: [APG Accordion Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)

### Key Takeaways for ARIA Accordion

1. **Consistent cross-AT behavior.** The button-in-heading pattern works reliably across all major screen readers.
2. **Heading navigation works.** Unlike `<summary>`, a `<button>` inside an `<h3>` preserves heading semantics. Users can navigate via H key.
3. **`aria-expanded` is reliably announced** across all tested screen readers.
4. **`aria-controls` has limited practical support** — JAWS is the only screen reader that surfaces the relationship. However, omitting it is still wrong per the APG spec.

---

## Practical Recommendations

| Requirement | Recommended Pattern | Reason |
|-------------|-------------------|--------|
| Maximum AT compatibility | ARIA accordion (`<button>` in `<h#>`) | Consistent role, state, and heading announcements across all ATs |
| Progressive enhancement / no-JS | Native `<details>`/`<summary>` | Works without JavaScript; accept inconsistent AT behavior |
| Heading navigation required | ARIA accordion only | Native `<summary>` destroys heading semantics in JAWS and NVDA |
| Mobile screen reader support | Either, but test TalkBack | TalkBack has gaps with both patterns; native `<details>` slightly worse |
