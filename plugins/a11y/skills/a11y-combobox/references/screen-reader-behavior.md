# Screen Reader Behavior — Combobox

Per-AT behavior differences observed in testing. These are not theoretical — they are documented failures from practitioner testing and library development.

---

## JAWS (Windows)

- Announces combobox role correctly as "combo"
- Handles `aria-activedescendant` mode switching gracefully — the exception among screen readers
- Fails to announce returned values from `<datalist>` selections

Sources: [Roselli](https://adrianroselli.com/2023/06/under-engineered-comboboxen.html), [Higley](https://sarahmhigley.com/writing/activedescendant/)

---

## NVDA (Windows)

- Announces combobox as "combo box", reads values when returning to field
- **Does NOT sync cursor with `aria-activedescendant` when switching between browse/forms mode** — can cause the visual highlight and screen reader focus to desync
- Fails to announce character deletions and text cursor movement in combobox input
- ARIA 1.1 comboboxes (readonly input pattern) don't appear in scan mode at all — users cannot find them

Sources: [Roselli](https://adrianroselli.com/2023/06/under-engineered-comboboxen.html), [Higley](https://sarahmhigley.com/writing/activedescendant/), [React Aria](https://react-aria.adobe.com/blog/building-a-combobox), [24a11y study](https://www.24a11y.com/2019/select-your-poison-part-2/)

**Workaround:** Supplement `aria-activedescendant` with a hidden `aria-live="assertive"` region that announces the currently focused option text. React Aria uses this approach. ([React Aria](https://react-aria.adobe.com/blog/building-a-combobox))

---

## VoiceOver (macOS)

- Only announces the `value` attribute when it differs from visible text, omitting visible content
- `aria-activedescendant` changes are NOT announced when:
  - Input is empty (Safari)
  - `aria-selected="true"` is missing from the target option (Chrome)
- Grouped options (`role="group"` wrapping `role="option"`) cause focus announcements to fail entirely
- Does not announce total option count or section titles
- Selection state ("selected") is omitted from announcements
- Ignores `aria-activedescendant` unreliably — behavior varies between Safari and Chrome

Sources: [Roselli](https://adrianroselli.com/2023/06/under-engineered-comboboxen.html), [React Aria](https://react-aria.adobe.com/blog/building-a-combobox), [Higley](https://sarahmhigley.com/writing/activedescendant/)

**Workaround:** Always set `aria-selected="true"` on the active option. Use an `aria-live` region to announce option count and position. Avoid `role="group"` on option containers. ([React Aria](https://react-aria.adobe.com/blog/building-a-combobox))

---

## VoiceOver (iOS / iPadOS)

- Cannot navigate beyond the first three `<datalist>` options displayed above the keyboard
- Essentially ignores `aria-activedescendant` entirely
- Custom combobox popups may require touch-specific interaction patterns

Sources: [Roselli](https://adrianroselli.com/2023/06/under-engineered-comboboxen.html), [Higley](https://sarahmhigley.com/writing/activedescendant/)

**Workaround:** For mobile, consider rendering options as a native-like scrollable list rather than relying on `aria-activedescendant`. React Aria uses a `<select>` on mobile for maximum compatibility. ([React Aria](https://react-aria.adobe.com/blog/building-a-combobox))

---

## TalkBack (Android)

- Provides minimal guidance for combobox interaction
- Options only accessible via explore-by-touch (swipe navigation)
- Counts the keyboard as a list item in some contexts
- Landscape mode can cause option loss
- Essentially ignores `aria-activedescendant`

Sources: [Roselli](https://adrianroselli.com/2023/06/under-engineered-comboboxen.html), [Higley](https://sarahmhigley.com/writing/activedescendant/)

**Workaround:** Same as iOS — consider native `<select>` or mobile-specific rendering on Android. ([React Aria](https://react-aria.adobe.com/blog/building-a-combobox))

---

## Narrator (Windows)

- Does not sync cursor with `aria-activedescendant` during mode switching (same issue as NVDA)
- Less tested than JAWS/NVDA in practitioner literature; fewer documented workarounds

Source: [Higley](https://sarahmhigley.com/writing/activedescendant/)

---

## Summary: What Works Everywhere

| Feature | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Narrator |
|---------|------|------|----------|--------|----------|----------|
| `role="combobox"` announced | Yes | Yes | Yes | Partial | Partial | Yes |
| `aria-activedescendant` | Yes | Partial | Partial | No | No | Partial |
| `aria-selected` on options | Yes | Yes | Required | N/A | N/A | Yes |
| Option count announced | Yes | Yes | No | No | No | Partial |
| `role="group"` in listbox | Yes | Yes | **Broken** | N/A | N/A | Unknown |

**Conclusion:** `aria-activedescendant` alone is insufficient. Always supplement with:
1. `aria-selected="true"` on the visually focused option
2. A hidden `aria-live` region for critical announcements (selected option text, count)
3. Mobile fallback to native `<select>` when feasible
