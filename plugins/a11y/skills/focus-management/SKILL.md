---
name: focus-management
description: Guides focus placement, containment, restoration and recovery during dialogs, route transitions and dynamic content changes. Use when focus gets lost, a component opens or closes, or navigation changes the visible task.
---

# Focus management

Choose a useful next location based on the user's action and the new workflow.
Preserve meaningful focus order and visible keyboard focus
([Focus order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html),
[Focus visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)).

## Modal lifecycle

Prefer native `dialog.showModal()` or an existing tested dialog component. Native
modal dialogs enter the top layer and make the document outside them inert;
`dialog.show()` is modeless and should not trap Tab
([WHATWG dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)).

For custom modals, implement initial focus, wrapping within the modal, operable
close, useful restoration and actual background inertness. `aria-modal` declares
semantics; `aria-hidden` alone does not prevent pointer or keyboard interaction
([APG dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/),
[WHATWG inert](https://html.spec.whatwg.org/multipage/interaction.html#the-inert-attribute)).

Choose initial focus for the content: first input, a static heading for long
structured content, or the least destructive action for an irreversible decision.
Do not focus a destructive action by default. On close, return to the trigger when
it remains usable; otherwise choose a surviving logical workflow target
([APG dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).

Avoid a hand-written static selector as proof of a complete focus trap: visibility,
inertness, disabled fieldsets, radio groups, shadow DOM and dynamic controls affect
reachability. Reuse the project's tested component and test its actual lifecycle.

## Route changes

Update the page title to describe the new route; do not assume changing
`document.title` alone yields speech. Select and test a focus/announcement policy
for full route changes, hash jumps, back/forward and dialogs. Focusing the new
heading is one useful project pattern, not a WCAG mandate for every DOM update
([Page titled](https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html),
[Focus order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html)).

```html
<h1 id="page-heading" tabindex="-1">Orders</h1>
```

After the requested route commits and the heading exists, focus that heading when
appropriate to the selected policy. Do not steal focus for initial render,
background refreshes or stale async completions. Coordinate router title/focus
and any announcer to avoid duplicate speech; test the actual support matrix.

## Insertion, deletion and notifications

- If the action removes the focused control, choose a surviving related control
  or meaningful container with programmatic focus. Verify the next action avoids
  accidental repeat deletion; do not insist on a previous sibling in all layouts.
- Keep focus for background content updates. A user-triggered insertion may
  warrant focus on the new editable item, depending on the task.
- Announce routine results through a stable status region where needed. Keep
  reachable Undo/status information; do not focus a toast merely because it has an
  action or time limit. Use the dialog pattern for a required interrupting decision
  ([APG alert](https://www.w3.org/WAI/ARIA/apg/patterns/alert/)).

## Skip links and obscured focus

```html
<a href="#main" class="skip-link">Skip to main content</a>
<main id="main" tabindex="-1">...</main>
```

Keep the skip link reachable early, visible when focused, and the target valid
through navigation. Verify both activation and the next Tab position
([Bypass blocks](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html)).

SC 2.4.11 AA prevents a focused component from being entirely hidden by
author-created content; 2.4.12 AAA prevents any part being hidden. Use tested scroll
padding/margins and responsive sticky UI; CSS declarations alone do not prove
visibility ([Focus not obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)).

## Verify

Test open/close, removed trigger, empty controls, reverse traversal, route races,
back/forward, zoom and sticky banners. Inspect focus destinations and observed AT
feedback separately. Read [modal lifecycle](references/modal-focus-trapping.md),
[route changes](references/spa-route-changes.md),
[framework patterns](references/framework-patterns.md),
[common mistakes](references/common-mistakes.md) and [sources](references/sources.yaml).
