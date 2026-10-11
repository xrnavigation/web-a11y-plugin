---
name: pointer-gestures
description: Guides single-pointer alternatives for drag/drop, reordering, sliders, maps, swipe controls, and touch interfaces. Use when implementing gesture input, pointer cancellation, motion actuation, or target sizing; evaluates pointer alternatives separately from keyboard access.
---

# Pointer and Gesture Accessibility

Make author-provided gesture functions usable through simple clicks/taps. Keep keyboard access as a separate check; a keyboard shortcut alone does not satisfy the pointer alternatives. ([Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html), [Pointer Gestures](https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html))

## Identify the required outcomes

These are WCAG 2.2 requirements. Understanding documents and techniques are informative explanations; examples and implementation choices below are project guidance. ([WCAG 2.2](https://www.w3.org/TR/WCAG22/))

| Criterion | Level | Required outcome |
|---|---|---|
| 2.5.1 Pointer Gestures | A | Multipoint/path-based functionality has a single-pointer, non-path alternative unless essential. |
| 2.5.2 Pointer Cancellation | A | Single-pointer actions use no down-event execution, completion on up-event with abort/undo, up-event reversal, or essential down-event execution. |
| 2.5.3 Label in Name | A | A control's accessible name contains its visible text label. |
| 2.5.4 Motion Actuation | A | Provide UI operation and disable motion response; exceptions concern accessibility-supported interfaces or essential motion. |
| 2.5.7 Dragging Movements | AA | Drag functions have a single-pointer alternative without dragging unless essential or unmodified user-agent functionality. |
| 2.5.8 Target Size (Minimum) | AA | Pointer targets are at least 24×24 CSS px, or meet an applicable exception. |

Author-interpreted pointer gestures are in scope; browser/assistive technology operation is outside 2.5.1/2.5.7. Native scrolling is different from an author-suppressed/reimplemented scrolling mechanism. ([Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html))

## Provide equivalent actions

Inventory every gesture and its result, then supply an alternative that achieves the same result. Examples from W3C include map pan buttons, zoom buttons, item move controls, carousel navigation, and numeric value entry. ([Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html), [Pointer Gestures](https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html))

| Gesture | Suggested project alternative | Verify |
|---|---|---|
| Drag to reorder or change column | Visible move buttons or select destination + Move | All destinations and constraints match drag. |
| Drag slider/color indicator | Click/tap value selection, numeric input, or step controls | Full required range and precision are reachable. |
| Swipe carousel | Previous/Next buttons | Same slides and boundary behavior. |
| Pinch or drag map | Zoom and directional pan buttons | Same area and scale range are reachable. |
| Drag rectangular selection | Select first corner, then opposite corner | Same rectangle can be produced without holding a pointer. |

Do not call arbitrary dragging path-based: 2.5.1 concerns the trajectory; 2.5.7 concerns holding and moving an object. A slider forcing a precise trajectory can involve both. A swipe is not a sufficient drag alternative when it still requires a path. ([Pointer Gestures](https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html))

Use the [working reorder example](references/reorder-example.md) for native move buttons calling one shared action. Preserve focus, communicate boundaries, and offer undo as project choices; assess cancellation requirements separately.

## Cancellation, labels, motion, and size

- Use native controls with `click` activation for ordinary commands, rather than performing the command on `pointerdown`. Native activation supports up-event cancellation; exercise actual pointer behavior. Custom drag operations need an abort/undo route when completion follows down-event work. ([G212](https://www.w3.org/WAI/WCAG22/Techniques/general/G212), [Pointer Cancellation](https://www.w3.org/WAI/WCAG22/Understanding/pointer-cancellation.html))
- Keep visible label words in the accessible name: `<button aria-label="Move up Budget">Move up</button>`. Putting the visible words first is best practice, not an extra normative requirement. ([Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html))
- For tilt/shake/camera gesture commands, offer ordinary UI controls **and** a way to disable motion response. Reduced-motion animation CSS is not that setting. Document the reason for any exception. ([Motion Actuation](https://www.w3.org/WAI/WCAG22/Understanding/motion-actuation.html))
- Measure the actual clickable area, not the icon. The 2.5.8 exceptions are spacing, same-page equivalent control, inline/line-height constraints, unmodified user-agent size, and essential or legally required presentation. The spacing test uses 24px diameter circles centered on undersized targets' bounding boxes; these must intersect neither another target nor another undersized target's circle. ([Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html))
- Prefer comfortably larger rectangular hit areas in the project. A blanket 24px gap, browser zoom, or visual icon measurement is not the criterion's test. ([Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html))

## Test and report

Use the [input test matrix](references/test-matrix.md), including pointer-only operation without hardware keyboard, keyboard operation, cancellation, all boundaries/destinations, and motion-disabled operation. Report executed environments and results; do not promise exact screen-reader speech or imply live assistive technology testing from code inspection.

Read [common mistakes](references/common-mistakes.md) when correcting input handlers. See [source provenance](references/sources.yaml) for verified primary sources. Use adjacent keyboard/widget skills for complete keyboard patterns.
