# Live region mistakes

## Hidden announcer

Wrong: `<p role="status" hidden={!message}>{message}</p>`.
Right: `<p role="status">{message}</p>` kept mounted and exposed. `hidden` and
`display:none` remove ordinary accessibility exposure; DOM presence alone is not
enough ([MDN live regions](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)).

## Guaranteed delay

Wrong: assert that `setTimeout(update, 100)` ensures speech on every platform.
Right: mount an empty announcer before updates and test actual output. Timing
experiments describe their tested browser/AT versions, not universal guarantees
([TetraLogical](https://tetralogical.com/blog/2024/05/01/why-are-my-live-regions-not-working/)).

## Competing field and summary announcements

Wrong: make every field error assertive while focusing and announcing a summary.
Right: associate visible field errors and select one summary/focus strategy for the
flow; retest failed submission and correction
([WAI validation](https://www.w3.org/WAI/tutorials/forms/validation/)).

## Incorrect urgency

Wrong: `<p role="alert">Settings saved</p>` on every edit.
Right: `<p role="status">Settings saved</p>` for routine completion. Alert/status
have assertive/polite defaults respectively; actual timing needs verification
([WAI-ARIA](https://www.w3.org/TR/wai-aria-1.2/#attrs_liveregions)).
