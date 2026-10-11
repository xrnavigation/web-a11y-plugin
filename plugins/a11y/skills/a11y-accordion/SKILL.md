---
name: a11y-accordion
description: Guides native disclosures and custom accordion sections, including heading/button structure, expanded state, keyboard operation and optional landmarks. Use when building FAQs, collapsible sections or disclosure controls.
---

# Accordions and disclosures

Use native details/summary for basic disclosure when it fits the task. Choose a
custom accordion when the product needs its heading/button pattern or interaction
contract. Verify support rather than treating old compatibility observations as
universal failures
([WHATWG details](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element),
[APG accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)).

## Native disclosure

```html
<details>
  <summary>How do I change my booking?</summary>
  <p>Open your booking and select Change dates.</p>
</details>
```

Use explicit summary text. Shared details name can provide exclusive expansion;
choose exclusivity only when it suits users who may need several sections open.
A labeled wrapper is optional project guidance, not an APG grouping requirement
([WHATWG details](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element),
[APG accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)).

Test nested heading exposure rather than assuming every summary flattens headings.
Keep needed heading semantics outside the toggle if the supported combinations
cannot convey them reliably
([APG testing](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)).

## Custom accordion example

```html
<h2>
  <button id="booking-toggle" type="button" aria-expanded="false"
          aria-controls="booking-panel">Changing a booking</button>
</h2>
<div id="booking-panel" hidden>
  <p>Open your booking and select Change dates.</p>
</div>
<script>
const trigger = document.getElementById('booking-toggle');
const panel = document.getElementById('booking-panel');
trigger.addEventListener('click', () => {
  const expanded = trigger.getAttribute('aria-expanded') === 'true';
  trigger.setAttribute('aria-expanded', String(!expanded));
  panel.hidden = expanded;
});
</script>
```

A native button supplies activation. Keep expanded state and panel visibility
synchronized. In the APG accordion pattern, the trigger is the heading's only
content; place persistent extra controls outside the heading
([APG accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)).

A panel can optionally use `role="region" aria-labelledby="booking-toggle"`.
Avoid landmark proliferation, especially when more than approximately six panels
can be expanded simultaneously. This is guidance about useful regions, not a
fixed total panel limit. If a panel cannot be collapsed, expose aria-disabled
on its trigger while retaining appropriate focus/behavior
([APG accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)).

## Interaction and verification

Keep Enter/Space activation and normal forward/reverse Tab traversal. Optional
header arrow/Home/End navigation must follow the selected pattern; wrapping is
optional, not mandatory. Do not trap Tab inside the accordion
([APG accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)).

Test expanded/collapsed content, heading navigation, panel controls, repeated
activation, exclusive expansion, current focus when a panel closes and observed
AT state information. Do not substitute off-screen positioning for hiding closed
content ([WHATWG hidden](https://html.spec.whatwg.org/multipage/interaction.html#the-hidden-attribute)).

Read [keyboard interaction](references/keyboard-interaction.md),
[native details](references/native-details-summary.md),
[AT verification](references/screen-reader-behavior.md),
[common mistakes](references/common-mistakes.md) and [sources](references/sources.yaml).
