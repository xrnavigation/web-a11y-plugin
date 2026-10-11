---
name: live-regions
description: Guides dynamic status and alert announcements without unnecessary focus movement. Use when implementing toasts, search counts, loading status, form feedback, chat logs or route announcers; handles region lifecycle, politeness and real AT verification.
---

# Live regions

Expose useful status updates while preserving the user's task and focus. ARIA
expresses announcement intent; actual output depends on browser/AT behavior and
must be tested ([WAI-ARIA live regions](https://www.w3.org/TR/wai-aria-1.2/#attrs_liveregions),
[MDN live regions](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)).

## Keep a registered announcer

Prefer an empty, stable container exposed to the accessibility tree before its
text changes. Do not use `hidden`, `display:none`, `visibility:hidden`, `inert` or
`aria-hidden` on an active announcer. Visually hidden CSS can retain accessibility
exposure. Initial content in an ordinary live region is not reliably announced;
`role="alert"` has special handling and still needs compatibility testing
([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)).

```html
<p id="search-status" role="status"></p>
```

```js
// After the user's search completes; keep the same DOM node.
document.getElementById('search-status').textContent = '5 results found';
```

```tsx
// Keep mounted and exposed even when message is empty.
<p role="status">{message}</p>
```

A fixed 100ms delay, a frame callback or a framework tick is not a universal
registration or speech guarantee. Prefer a mounted announcer and test updates on
the support matrix. Historical timing experiments are evidence for their tested
environments ([TetraLogical testing](https://tetralogical.com/blog/2024/05/01/why-are-my-live-regions-not-working/)).

## Select semantics and content

| Pattern | Intended semantics | Project guidance |
|---|---|---|
| `role="status"` | Implicit polite, atomic | Routine completed actions, counts and progress milestones |
| `role="alert"` | Implicit assertive, atomic | Urgent changes needing attention; avoid routine interruptions |
| `role="log"` | Implicit polite, not atomic | Sequential additions such as chat messages |
| `aria-live="off"` | Updates can be presented when focus is within the region | Does not mean universally silent |

Roles and defaults come from [WAI-ARIA](https://www.w3.org/TR/wai-aria-1.2/#attrs_liveregions).
Avoid duplicating explicit `aria-live="assertive"` on alerts without a demonstrated
need; redundant settings can cause duplicate output in some combinations
([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)).

Use `aria-atomic` when a partial update loses meaning, `aria-relevant` for change
types and `aria-busy` during batching. They express intended handling; verify the
result rather than assuming a specific utterance
([WAI-ARIA](https://www.w3.org/TR/wai-aria-1.2/#attrs_liveregions)).

## Handle interaction and competing announcements

- Keep visible messages available for users who miss speech. Avoid hiding the
  only error or automatically dismissing actionable information.
- Associate field errors with the field and set the invalid state; do not add an
  assertive region to every field by default. Select a visible error summary or
  focused invalid field according to the form flow; avoid simultaneously moving
  focus and announcing the same paragraph
  ([WAI validation](https://www.w3.org/WAI/tutorials/forms/validation/)).
- Do not steal focus for routine toasts or search results. An alert is not an
  interactive alert dialog; use the dialog pattern when an interrupting decision
  requires focus ([APG alert](https://www.w3.org/WAI/ARIA/apg/patterns/alert/)).
- Debounce rapid updates and announce useful milestones as project policy. Keep
  route announcements coordinated with title/focus handling; test for duplicates.
  Status-message identification applies when the WCAG definition is met, not to
  every DOM mutation ([SC 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)).

## Verify and report

Run the actual sequence, including rapid requests, cancellations, repeated text,
failed requests, hidden/unmounted containers and navigation away. Record versions,
settings, action, observed speech, visible fallback and focus. Label unrun speech
checks **not tested**. Do not infer output from a DOM snapshot
([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)).

Use [recipes](references/recipes.md),
[screen reader testing](references/screen-reader-behavior.md),
[common mistakes](references/common-mistakes.md) and [sources](references/sources.yaml).
