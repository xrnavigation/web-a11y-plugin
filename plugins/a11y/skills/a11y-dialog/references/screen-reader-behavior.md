# Screen Reader Behavior with Dialogs

Screen reader behavior with dialogs varies significantly across platforms and browser combinations. These observations are from Adrian Roselli's testing (2020). Screen reader behavior evolves — manual testing remains essential.

---

## Per-AT Behavior

### JAWS

| Browser | Behavior |
|---------|----------|
| Chrome | Announces "Dialog, [name] modal dialog" when wrapper is focused. Heading: "[name] modal dialog, [name] heading level 2" |
| Firefox | More verbose — reads dialog content automatically: "[name] modal dialog, Page has one region one heading and no links, [reads content]" |

### NVDA

| Browser | Behavior |
|---------|----------|
| Chrome | Includes "selected" status indicator. Announces "[name] dialog, selected" |
| Firefox | Very verbose — reads full content: "[name] dialog, document, [name] heading level 2, [name], button Close" |

NVDA switches to forms/application mode inside dialogs, limiting browse-mode navigation. Using `role="document"` on an inner wrapper (as a11y-dialog does) restores browse mode for NVDA users.

### VoiceOver (macOS)

| Browser | Behavior |
|---------|----------|
| Safari | Announces "[name], web dialog" when wrapper is focused. Heading: "[name], web dialog, heading level 2, [name]" |
| Chrome | Same pattern as Safari |

### TalkBack (Android)

| Browser | Behavior |
|---------|----------|
| Chrome | "[name] dialog, document" — minimal context on headings |
| Firefox | "[name], dialog, [name] paragraph, [content]" — reads content inline |

### VoiceOver (iOS)

Behavior is notably different from all other platforms and described as less predictable in testing.

*Source: [Adrian Roselli — Dialog Focus in Screen Readers](https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html)*

---

## Key Takeaways

### What screen readers announce

Screen readers announce: **dialog role** + **accessible name** + **optional description** + **currently focused element**.

The title and description referenced by `aria-labelledby`/`aria-describedby` do not need to be focused to be perceived — screen readers pull them from the dialog container.

### Firefox auto-reads content

Firefox paired with NVDA or JAWS tends to automatically read dialog content when focus lands on the dialog container. This affects whether you should focus the container vs a specific element:
- If auto-read provides sufficient context, focusing a specific control may be better
- If you want the user to hear a specific element first, focus that element directly

### `role="document"` for NVDA browse mode

NVDA enters forms mode inside `role="dialog"`, which prevents users from navigating with browse-mode shortcuts (H for headings, etc.). Adding `role="document"` on an inner wrapper element restores browse-mode navigation.

```html
<dialog aria-labelledby="title">
  <div role="document">
    <h2 id="title">Dialog Title</h2>
    <p>Content that NVDA users can navigate with browse mode.</p>
    <button>Close</button>
  </div>
</dialog>
```

*Source: [a11y-dialog — Markup](https://a11y-dialog.netlify.app/usage/markup)*

---

## Testing Recommendations

Automated testing cannot validate dialog accessibility adequately. "Automated testing tools can only catch a relatively low percentage of WCAG failures" for dialogs. Test manually with at least:

1. **NVDA + Firefox** (Windows) — most verbose, reveals content reading order issues
2. **JAWS + Chrome** (Windows) — most common enterprise combination
3. **VoiceOver + Safari** (macOS) — primary Mac screen reader
4. **Keyboard only** (no screen reader) — Tab cycling, Escape, focus restoration

*Source: [Common Accessibility Issues with Modals](https://blog.openreplay.com/common-accessibility-issues-modals-fix/)*
