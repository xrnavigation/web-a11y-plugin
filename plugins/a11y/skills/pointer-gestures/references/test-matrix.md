# Input test matrix

Use this project matrix against every gesture function and each supported input environment. Record browser/OS/device, route, item/value state, action, expected result, actual result, and evidence. These checks target the outcomes explained in [Pointer Gestures](https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html), [Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html), and [Pointer Cancellation](https://www.w3.org/WAI/WCAG22/Understanding/pointer-cancellation.html); they are not a complete conformance audit.

| Check | Procedure | Expected observation |
|---|---|---|
| Mouse/pen single pointer | Operate the alternative using clicks/taps only, without holding/moving or shortcuts. | Every gesture result is reachable. |
| Touch single pointer | Use one finger and visible controls; no hardware keyboard, multipoint input, swipe, or drag. | Same destinations, full ranges, and precision. A value input may use the on-screen keyboard. |
| Keyboard separately | Tab to native alternatives; activate with Enter/Space. | Same results; focus remains usable after move/undo. This does not prove pointer equivalence. |
| Gesture equivalence | Compare drag and controls for every destination/range limit. | Shared constraints and state changes; no privileged drag-only outcome. |
| Up-event cancellation | Press an ordinary button, move away, release; repeat touch interaction where supported. | No command execution when cancelled. Record actual device behavior. |
| Interrupted drag | Start then abort, drop outside valid targets, or trigger platform cancellation. | No committed unintended move, or a working undo route appropriate to the chosen cancellation mechanism. |
| Boundaries | First/last item, minimum/maximum values, unavailable destination, single item. | No invalid state; exposed unavailable state and clear feedback. |
| Undo | Move with each input path, then undo once/repeatedly to empty history. | Earlier order/value restored; sensible focus and empty-history behavior. |
| Rapid operation | Activate twice; try duplicate gesture/click dispatch and delayed persistence. | No unintended duplicate command or divergent model/DOM order. |
| Name and label | Inspect computed accessible name against visible words. | Visible text included; add context without replacing visible words. |
| Targets | Measure actual hit area at 100% zoom; inspect undersized targets and neighbors. | Size or documented 2.5.8 exception holds; overlapping expanded hit areas do not intercept a neighbor. |
| Motion enabled/disabled | Operate the UI equivalent, then disable motion and repeat shake/tilt/camera action. | UI still works; motion no longer triggers. |
| Screen reader | Inspect names/states/order/status with project-supported combinations. | Changes are understandable; record observed output instead of promising exact speech. |

Name checks derive from [Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html), target exceptions from [Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), motion checks from [Motion Actuation](https://www.w3.org/WAI/WCAG22/Understanding/motion-actuation.html), and status markup from [ARIA22](https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA22). Test integration behavior in the actual application; a standalone reorder example cannot cover persistence or platform input support.

For any essential exception, record the particular function, why removing that input would fundamentally change it, why the information/functionality cannot be achieved in another conforming way, and which criterion's exception is invoked. A team's preference for dragging or a third-party library's limitations are not themselves evidence of essential functionality. ([WCAG 2.2, essential definition](https://www.w3.org/TR/WCAG22/#dfn-essential))
