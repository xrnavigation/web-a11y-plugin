# Common mistakes

## Keyboard-only drag alternative

Keyboard operability and single-pointer alternatives are evaluated independently. ([Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html))

```js
// Wrong as the sole non-drag alternative: requires keyboard input.
handle.addEventListener('keydown', event => {
  if (event.key === 'ArrowUp') moveUp(itemId);
});
// Right: visible native button can be clicked/tapped and keyboard-activated.
moveButton.addEventListener('click', () => moveUp(itemId));
```

## Replacing dragging with swiping

A path-based swipe does not supply the required non-path pointer alternative. ([Pointer Gestures](https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html))

```js
// Wrong as the only alternative to a draggable carousel.
onHorizontalSwipe(() => nextSlide());
// Right: add an independently operable next control.
nextButton.addEventListener('click', nextSlide);
```

## Executing a command before release

Ordinary activation on down-event bypasses up-event cancellation unless another criterion route applies. ([Pointer Cancellation](https://www.w3.org/WAI/WCAG22/Understanding/pointer-cancellation.html))

```js
// Wrong for an ordinary irreversible command.
deleteButton.addEventListener('pointerdown', deleteItem);
// Right project pattern: ordinary native click activation.
deleteButton.addEventListener('click', deleteItem);
```

Undo remains useful but the criterion does not require undo for every `click` command. Assess which cancellation route the actual handler meets; do not add duplicate `touchend` and `click` commands. ([G212](https://www.w3.org/WAI/WCAG22/Techniques/general/G212))

## Overwriting visible labels

The accessible name must contain the visible text label. ([Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html))

```html
<!-- Wrong -->
<button aria-label="Raise priority">Move up</button>
<!-- Right -->
<button aria-label="Move up Budget">Move up</button>
```

## Making disabled-looking buttons still execute

Project rule: when retaining focusable boundary buttons, enforce their unavailable state in code and expose it with [`aria-disabled`](https://www.w3.org/TR/wai-aria-1.2/#aria-disabled). See [reorder example](reorder-example.md) for no-op bounds checks. Do not use visual styling as the only state.

```js
// Wrong: changes appearance only.
button.classList.add('disabled');
// Right: expose state and reject out-of-range moves in the shared action.
button.setAttribute('aria-disabled', 'true');
```

## Treating reduced animation as disabled motion input

2.5.4 covers sensor/user motion actuation, not animation preferences. Provide UI operation and a way to turn off the motion trigger. ([Motion Actuation](https://www.w3.org/WAI/WCAG22/Understanding/motion-actuation.html))

```js
// Wrong: shake handler always triggers even when animations are reduced.
function onShake() { undoLastAction(); }
// Right project pattern: ordinary Undo button plus explicit motion input setting.
function onShake() { if (motionInputEnabled) undoLastAction(); }
undoButton.addEventListener('click', undoLastAction);
```

## Confusing target dimensions and spacing

AA is 24×24 CSS px or a qualifying exception; the undersized-target spacing rule is a circle-intersection test, not a universal 24px gap. ([Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html))

```css
/* Wrong as proof of target size: an icon dimension is not the hit area. */
button svg { width: 24px; height: 24px; }
/* Right project pattern: size the actual rectangular control generously. */
button { min-width: 44px; min-height: 44px; border-radius: 0; }
```
