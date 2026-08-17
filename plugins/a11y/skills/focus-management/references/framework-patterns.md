# Framework-Specific Focus Management Patterns — Reference
## Contents

- [React](#react)
  - [Focus on mount/update with useRef and useEffect](#focus-on-mountupdate-with-useref-and-useeffect)
  - [Focus trap hook](#focus-trap-hook)
  - [Focus restoration hook](#focus-restoration-hook)
  - [Libraries](#libraries)
- [Vue](#vue)
  - [Focus with nextTick and template refs](#focus-with-nexttick-and-template-refs)
  - [Route change focus (Vue Router)](#route-change-focus-vue-router)
- [Angular](#angular)
  - [CDK cdkTrapFocus](#cdk-cdktrapfocus)
  - [Features](#features)
  - [Limitation](#limitation)
- [Roving Tabindex vs. aria-activedescendant](#roving-tabindex-vs-aria-activedescendant)
  - [Roving tabindex](#roving-tabindex)
  - [aria-activedescendant](#aria-activedescendant)
  - [Selection vs. focus](#selection-vs-focus)


## React

### Focus on mount/update with `useRef` and `useEffect`

```jsx
const headingRef = useRef(null);

useEffect(() => {
  headingRef.current?.focus();
}, [currentRoute]);

return <h1 ref={headingRef} tabIndex={-1}>{pageTitle}</h1>;
```

### Focus trap hook

```jsx
function useFocusTrap(modalRef, isOpen) {
  useEffect(() => {
    if (!isOpen) return;
    const focusableEls = modalRef.current.querySelectorAll(
      'a[href], button:not([disabled]), input:not([disabled]), ' +
      'select:not([disabled]), textarea:not([disabled]), ' +
      '[tabindex]:not([tabindex="-1"])'
    );
    const firstEl = focusableEls[0];
    const lastEl = focusableEls[focusableEls.length - 1];

    function handleKeyDown(e) {
      if (e.key !== 'Tab') return;
      if (e.shiftKey && document.activeElement === firstEl) {
        e.preventDefault();
        lastEl.focus();
      } else if (!e.shiftKey && document.activeElement === lastEl) {
        e.preventDefault();
        firstEl.focus();
      }
    }
    modalRef.current.addEventListener('keydown', handleKeyDown);
    firstEl?.focus();
    return () => modalRef.current?.removeEventListener('keydown', handleKeyDown);
  }, [isOpen]);
}
```

### Focus restoration hook

```jsx
function useModal() {
  const [isOpen, setIsOpen] = useState(false);
  const triggerRef = useRef(null);

  const open = () => {
    triggerRef.current = document.activeElement;
    setIsOpen(true);
  };

  const close = () => {
    setIsOpen(false);
    triggerRef.current?.focus();
  };

  return { isOpen, open, close };
}
```

### Libraries

- **`focus-trap-react`** — wraps `focus-trap` with a React component. Handles edge cases like dynamically added focusable elements. ([LogRocket](https://blog.logrocket.com/build-accessible-modal-focus-trap-react/))
- **Mantine `useFocusTrap`** — hook that creates a focus trap on a container ref. ([Mantine docs](https://mantine.dev/hooks/use-focus-trap/))

---

## Vue

### Focus with `nextTick` and template refs

Vue updates the DOM asynchronously. Attempting to focus an element immediately after a reactive data change may fail because the DOM has not updated. Always use `nextTick`:

```js
import { ref, nextTick } from 'vue';

const modalRef = ref(null);
const isOpen = ref(false);

async function openModal() {
  isOpen.value = true;
  await nextTick();
  modalRef.value?.focus();
}
```

### Route change focus (Vue Router)

```js
router.afterEach(() => {
  nextTick(() => {
    const heading = document.querySelector('h1');
    heading?.focus();
  });
});
```

Sources:
- [MDN — Vue refs and lifecycle methods for focus management](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Frameworks_libraries/Vue_refs_focus_management)
- [marcus.io — Accessible routing with vue.js](https://marcus.io/blog/accessible-routing-vuejs)

---

## Angular

### CDK `cdkTrapFocus`

Angular's Component Dev Kit (CDK) provides the `cdkTrapFocus` directive from `@angular/cdk/a11y`:

```typescript
import { A11yModule } from '@angular/cdk/a11y';
```

```html
<div cdkTrapFocus [cdkTrapFocusAutoCapture]="true">
  <!-- modal content -->
</div>
```

### Features

| Attribute | Purpose |
|---|---|
| `cdkTrapFocusAutoCapture` | Auto-focuses the first focusable item on initialization |
| `cdkFocusInitial` | Specifies which element receives initial focus |
| `cdkFocusRegionStart` / `cdkFocusRegionEnd` | Define focus trap boundaries |

### Limitation

The CDK directive only traps keyboard Tab cycling. It does not prevent focus from moving out via mouse interaction. For full modal behavior, combine with a backdrop overlay.

Sources:
- [Brian Treese — Angular CDK Focus Trap](https://briantree.se/using-the-angular-cdk-trap-focus-directive/)
- [Angular Material CDK a11y docs](https://v12.material.angular.io/cdk/a11y)

---

## Roving Tabindex vs. `aria-activedescendant`

Two strategies for managing focus within composite widgets (tab lists, menus, listboxes, toolbars).

### Roving tabindex

One child has `tabindex="0"`, all others have `tabindex="-1"`. On arrow key navigation: set the new target to `tabindex="0"`, old target to `tabindex="-1"`, and call `.focus()`.

**Advantage:** Browser automatically scrolls the focused element into view.

**Use for:** Most composite widgets — tabs, toolbars, radio groups, tree views.

### `aria-activedescendant`

Container keeps DOM focus with `tabindex="0"`. Set `aria-activedescendant` to the `id` of the visually active child. The active child must be a DOM descendant, referenced via `aria-owns`, or within an `aria-controls` target.

**Advantage:** DOM focus stays on the container — essential for comboboxes where the input must retain focus for typing.

**Use for:** Combobox, searchbox, filterable listbox patterns.

### Selection vs. focus

Focus is a pointer — there is only one point of focus at any time. Selection is separate state (`aria-selected="true"`) that can span multiple elements.

In single-select widgets, selection can follow focus automatically, but only when content change is instantaneous. If changes trigger network requests, require explicit activation via Enter/Space.

Source: [W3C APG — Keyboard Interface Practice](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/)
