# Sensory and interruption review

Treat these as potential barriers to investigate with users, not inevitable symptoms of autism, ADHD, dyslexia, or any other diagnosis. User needs and preferences vary. ([COGA usable](https://www.w3.org/TR/coga-usable/))

| Presentation | Project review question | Suggested response |
|---|---|---|
| Parallax/full-screen movement | Can content be read without decorative motion? | Static alternative, reduced-motion treatment. |
| Auto-rotating content | Can users finish reading and operating a panel? | User control; pause/stop mechanism where required. |
| Competing prompts | Do optional prompts interrupt a primary task? | Defer/dismiss optional prompts and retain task state. |
| Transient messages | Is essential information still findable? | Persistent status or a message history. |
| Dense text | Can readers understand structure and instructions? | Meaningful headings, short sections, adaptable text. |
| Audio | Can playback be controlled independently? | Visible, operable play/pause/volume controls. |

## Requirements versus project preference

- SC 2.2.2 (A): moving/blinking/scrolling information that starts automatically, lasts more than five seconds, and accompanies other content needs pause/stop/hide unless essential; auto-updating information has a related control requirement without that five-second threshold. ([Pause Stop Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html))
- SC 2.3.1 (A): flashes must not exceed three per second **or** must remain below the general/red flash thresholds. Avoid flashing as project guidance; do not simplify the actual criterion to a blanket flash count. ([Three Flashes or Below Threshold](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html))
- SC 2.3.3 (AAA): nonessential interaction-triggered motion animation can be disabled. ([Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html))

Do not reduce required contrast based on a diagnosis or mandate one palette/font. Support customization while preserving readable defaults. Test functional information, not just decorative animation, after preference changes. ([COGA usable](https://www.w3.org/TR/coga-usable/))
