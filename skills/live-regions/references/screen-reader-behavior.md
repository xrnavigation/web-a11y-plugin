# Screen Reader Behavior: Live Regions

Cross-platform behavior matrix for ARIA live region features.

Sources: [TetraLogical](https://tetralogical.com/blog/2024/05/01/why-are-my-live-regions-not-working/), [MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)

---

## Behavior Matrix

| Behavior | JAWS | NVDA | VoiceOver (macOS) | VoiceOver (iOS) | TalkBack |
|----------|------|------|-------------------|-----------------|----------|
| Pre-populated polite regions | Not announced | Not announced | Not announced | Not announced | May announce |
| Pre-populated `role="alert"` | Inconsistent | Announced | Announced (with alert sound) | Announced | Announced |
| Injected content (polite) | Works | Works | Works | Works | Works |
| Injected content (assertive) | Works | Works | Works | Works | Works |
| `role="alert"` + `aria-live="assertive"` | Single | Single | **Double-speaks** | **Double-speaks** | Single |
| `aria-atomic` | Supported | Supported | Supported | Inconsistent | Inconsistent |
| `aria-relevant` | Partial | Partial | Partial | Minimal | Minimal |
| `aria-busy` | Partial | Partial | Partial | Minimal | Minimal |

---

## Key Takeaways

### Most reliable pattern

An empty container with `aria-live="polite"` (or an implicit live region role like `role="status"`) that exists in the DOM from page load, with content injected later via `textContent` updates. This works across all screen reader and browser combinations.

### Least reliable features

`aria-relevant`, `aria-atomic`, and `aria-busy` have inconsistent support across platforms. They should not be the sole mechanism for any critical behavior. Always provide a fallback that works without them.

### Known bugs

- **NVDA + Chrome:** Changes to polite live regions can be repeated up to 6 times when control labels change simultaneously. ([NVDA #7996](https://github.com/nvaccess/nvda/issues/7996))
- **NVDA + Firefox:** Same bug reproduces up to 3 times.
- **VoiceOver iOS:** Adding `aria-live="assertive"` to `role="alert"` causes double announcement. Never combine them.

### TalkBack differences

TalkBack on Android is more forgiving than desktop screen readers — it may announce pre-populated live regions that other screen readers ignore. Do not rely on this behavior; code for the least-forgiving implementation.

---

## Pre-populated vs Injected Content

| Scenario | Announced? |
|----------|-----------|
| Empty container in DOM, text injected later | Yes (all screen readers) |
| Container with text already present when added to DOM | No (most screen readers) |
| `role="alert"` with text already present | Inconsistent (varies by screen reader) |
| Hidden container revealed (`display:none` → `display:block`) | No (content was not "changed") |
| Container created and populated in same JS tick | No (screen reader never registered the region) |

---

## Recommendations for Cross-Platform Reliability

1. Always place empty live region containers in initial HTML or mount them early in app lifecycle.
2. Use `textContent` updates (not DOM structure changes) to trigger announcements.
3. Use `role="status"` for polite announcements and `role="alert"` for assertive — they have better cross-platform support than bare `aria-live`.
4. Never add `aria-live="assertive"` to `role="alert"`.
5. Treat `aria-relevant`, `aria-atomic`, and `aria-busy` as progressive enhancements, not requirements.
