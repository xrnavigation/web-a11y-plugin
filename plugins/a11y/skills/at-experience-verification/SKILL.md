---
name: at-experience-verification
description: Verifies a bounded web journey with real assistive technology and records observed names, roles, states, reading order, announcements, and task completion. Use when testing screen reader behavior or reviewing evidence; separates predictions from observed output.
argument-hint: "[component-or-page]"
---

# Assistive technology experience verification

Verify what users can accomplish in the requested journey. Accessibility tree
inspection and markup predictions help prepare tests; they are not observed
screen reader output. APG examples themselves require testing in supported
browser/AT combinations ([APG read me first](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)).

## Establish the evidence boundary

Record revision/URL, OS, browser and AT versions, speech/verbosity settings,
navigation mode, viewport, starting state, action sequence and capture method.
Choose combinations from the product's support policy and user needs. Include
mobile where supported; do not infer universal coverage from a desktop run
([WAI evaluation](https://www.w3.org/WAI/test-evaluate/)).

Label each result **observed**, **predicted**, or **not tested**. If AT is unavailable,
perform useful DOM, accessibility tree and keyboard checks, but leave the speech
result unverified. Never fabricate a transcript.

## Prepare expectations from semantics

For each control, record expected name, role, state and operation rather than an
exact mandatory sentence. AT may vary wording, order and timing; semantic roles
and states are the authoring contract
([WAI-ARIA](https://www.w3.org/TR/wai-aria-1.2/)).

```html
<label for="email">Email address</label>
<input id="email" type="email" aria-describedby="email-help">
<p id="email-help">We send your receipt here.</p>
```

Expectation: the field exposes the label and help text and accepts input. Verify
the actual speech, navigation and any description-verbosity setting. Explicit
label association comes from HTML labeling
([WAI labels](https://www.w3.org/WAI/tutorials/forms/labels/)).

## Walk the journey

1. Read headings, landmarks, links and meaningful reading order using the AT's
   normal document-navigation commands. Compare meaning with visual content
   ([WCAG meaningful sequence](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence.html)).
2. Operate controls with keyboard and the platform's AT interaction methods.
   Record unreachable actions, traps, unexpected mode switches and lost focus
   ([WCAG keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html)).
3. Trigger expansion, selection, validation, modal open/close, async completion
   and route changes. Check name/role/value and status information; keep exact
   observed utterances in evidence rather than teaching them as universal output
   ([WCAG name role value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html),
   [WCAG status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)).
4. Repeat the sequence on the support combinations affected by a defect. Compare
   behavior with the intended widget interaction contract and task completion
   ([APG](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)).

## Report

```text
Journey/revision:
Environment and settings:
Starting state and actions:
Expected semantic information / operation:
Observed behavior and speech (or predicted / not tested):
User task affected:
Evidence artifact:
Fix and same-sequence retest:
Other combinations and states not tested:
```

Treat low-vision zoom/reflow and keyboard-only checks as separate evidence lanes;
use `zoom-reflow`, `focus-management` and `testing-strategy`. Consult the
[illustrative output catalog](references/screen-reader-output-catalog.md) only
as hypotheses to test, plus [keyboard experience](references/keyboard-experience.md),
[low-vision experience](references/low-vision-experience.md),
[examples](references/good-vs-bad-examples.md),
[common mistakes](references/common-mistakes.md) and [sources](references/sources.yaml).
