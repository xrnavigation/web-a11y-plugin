# Live region support verification

Use a test record instead of a versionless cross-platform support matrix.
Published experiments are historical evidence for the exact combinations tested
([TetraLogical](https://tetralogical.com/blog/2024/05/01/why-are-my-live-regions-not-working/)).

| Sequence | Information to observe |
|---|---|
| Mounted empty status, later text update | Whether the new status is spoken |
| Ordinary region inserted already populated | Whether initial content is silent or presented |
| Initially populated alert | Special alert handling and duplicate speech |
| Hidden then revealed announcer | Whether the update was registered |
| Same message repeated after another action | Whether useful repeated feedback is presented |
| Rapid async requests, abort and stale response | Whether obsolete feedback is prevented |
| Atomic/relevant/busy batch updates | Whether intended final content is presented |

These are tests, not predetermined outcomes. ARIA defines roles/properties;
implementation output can vary
([WAI-ARIA](https://www.w3.org/TR/wai-aria-1.2/#attrs_liveregions),
[MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)).
Record OS/browser/AT versions, settings, starting state, action, exact observed
speech, focus and persistent visible fallback. Mark absent environments not tested.
