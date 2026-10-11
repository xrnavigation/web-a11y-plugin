# Disclosure and accordion AT verification

Record the actual OS/browser/AT versions, settings and interaction mode. Published
compatibility observations are historical examples, not versionless guarantees.
APG examples require testing before production use
([APG read me first](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)).

| Action | Semantic/task expectation to verify |
|---|---|
| Focus trigger | Useful name and disclosure/button operation |
| Toggle | Expansion state matches visible content |
| Read closed section | Hidden content is not traversed |
| Read opened section | Content reachable in meaningful sequence |
| Navigate headings | Intended heading structure is retained |
| Tab/Shift+Tab | Sensible traversal; panel controls reachable when open |
| Multiple expansions | Optional region landmarks remain useful |

Use the native HTML contract for details and the chosen APG interaction pattern for
custom accordions; optional arrow keys and regions are not universal requirements
([WHATWG details](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element),
[APG accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)).
Capture observed output or mark it not tested. Do not invent a support matrix.
