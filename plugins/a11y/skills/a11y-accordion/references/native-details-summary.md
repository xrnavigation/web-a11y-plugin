# Native details and summary

`details` is a native disclosure; an explicit summary labels its toggle. The open
attribute controls expansion. Sharing a name creates an exclusive group where
supported; decide whether users need several answers open at once
([WHATWG details](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element)).

```html
<details>
  <summary>How do I change my booking?</summary>
  <p>Open your booking and select Change dates.</p>
</details>
```

No script is needed for the basic toggle. Verify the target browser/AT's keyboard,
state and heading behavior; do not extrapolate 2018/2019 observations to every
current combination. Keep required headings outside summary if current testing
shows that nesting loses useful heading/disclosure semantics
([APG testing](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)).

A named wrapper can help identify a related section as project guidance; APG does
not require a group role around all accordions. For a custom APG accordion, use
heading/button triggers and synchronized expanded/controls/panel state. Regions
are optional and should avoid landmark proliferation when many panels can be
expanded simultaneously
([APG accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)).
