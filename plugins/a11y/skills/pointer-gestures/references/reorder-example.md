# One action for move controls and drag integration

## Contents

- [Reorder example](#reorder-example)

## Reorder example

This project example supplies a complete button-based reorder workflow. An optional application's drag layer should call `moveTo(id, finalIndex)` after a valid completed drop; cancel/invalid drops must leave the order unchanged. It deliberately does not implement a drag recognizer. Clickable move controls illustrate W3C's non-drag alternative; `click` activation on native controls follows the up-event technique. ([Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html), [G212](https://www.w3.org/WAI/WCAG22/Techniques/general/G212))

Copy this into an HTML page. Boundary controls remain focusable with [`aria-disabled`](https://www.w3.org/TR/wai-aria-1.2/#aria-disabled); the handler explicitly blocks their effect. That focus policy and undo stack are project choices. Status markup follows [ARIA22](https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA22); verify announcements in supported screen readers rather than claiming particular speech.

```html
<h2 id="tasks-title">Task order</h2>
<p>Use Move up or Move down to change the order.</p>
<ol id="tasks" aria-labelledby="tasks-title"></ol>
<button id="undo" type="button" aria-disabled="true">Undo move</button>
<p id="move-status" role="status" aria-atomic="true"></p>
<style>
  #tasks li { margin-block: 1rem; }
  button { min-width: 44px; min-height: 44px; border-radius: 0; }
  button[aria-disabled="true"] { opacity: 0.7; }
  button:focus-visible { outline: 3px solid currentColor; outline-offset: 2px; }
</style>
<script>
const list = document.querySelector('#tasks');
const status = document.querySelector('#move-status');
const undo = document.querySelector('#undo');
const items = [
  { id: 'budget', label: 'Budget' },
  { id: 'travel', label: 'Travel' },
  { id: 'report', label: 'Report' }
];
let order = items.map(item => item.id);
const history = [];
const rows = new Map();

for (const item of items) {
  const row = document.createElement('li');
  const label = document.createElement('span');
  label.textContent = `${item.label} `;
  row.append(label);
  for (const [text, delta] of [['Move up', -1], ['Move down', 1]]) {
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = text;
    button.setAttribute('aria-label', `${text} ${item.label}`);
    button.dataset.delta = String(delta);
    button.addEventListener('click', () => {
      const position = order.indexOf(item.id);
      const destination = position + delta;
      if (!moveTo(item.id, destination)) {
        status.textContent = `${item.label} is already at this boundary.`;
      }
    });
    row.append(button);
  }
  rows.set(item.id, row);
}

function render() {
  // Moving existing DOM nodes may disturb focus; restore the same control.
  const focused = document.activeElement;
  const restore = list.contains(focused);
  for (const [index, id] of order.entries()) {
    const row = rows.get(id);
    list.append(row);
    for (const button of row.querySelectorAll('button')) {
      const next = index + Number(button.dataset.delta);
      button.setAttribute('aria-disabled', String(next < 0 || next >= order.length));
    }
  }
  undo.setAttribute('aria-disabled', String(history.length === 0));
  if (restore) focused.focus();
}

// finalIndex is the item's index in the resulting order, after removal/reinsertion.
function moveTo(id, finalIndex) {
  const from = order.indexOf(id);
  if (from < 0 || !Number.isInteger(finalIndex) || finalIndex < 0 ||
      finalIndex >= order.length || from === finalIndex) return false;
  history.push([...order]);
  order.splice(from, 1);
  order.splice(finalIndex, 0, id);
  render();
  const item = items.find(item => item.id === id);
  status.textContent = `${item.label} moved to position ${finalIndex + 1} of ${order.length}.`;
  return true;
}

undo.addEventListener('click', () => {
  if (history.length === 0) {
    status.textContent = 'No move to undo.';
    return;
  }
  order = history.pop();
  render();
  status.textContent = 'Previous task order restored.';
  // The Undo button remains in place and retains keyboard focus.
});
render();
</script>
```

Labels begin with the visible words, supporting the [Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html) requirement and best practice. The 44px rectangular button sizing is a project preference above the [24×24 CSS px AA minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), not a claim of satisfying every input criterion.

When integrating persistence, commit the same action for both input paths, handle rejection, restore the prior order, and show an error. For concurrent edits, validate the destination against current state. Do not describe this in-memory example as covering server failures, drag cancellation, or browser/assistive technology testing.
