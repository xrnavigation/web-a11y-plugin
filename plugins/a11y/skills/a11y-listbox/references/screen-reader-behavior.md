# Listbox Screen Reader Behavior

---

## General Announcements

When a listbox receives focus, screen readers typically announce ([APG](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)):

1. The accessible name (from `aria-label` or `aria-labelledby`)
2. The role ("list box")
3. The focused option's text
4. Position in set (e.g., "3 of 12") if supported
5. Selection state ("selected" / "not selected")

---

## JAWS

- Announces listbox role and switches to Forms mode automatically when focus enters the widget.
- Handles `aria-activedescendant` well.
- Will toggle to Virtual PC Cursor / browse mode when a button is focused, even inside a composite widget — this can cause problems if buttons are placed inside listbox options ([TPGi](https://www.tpgi.com/the-road-to-accessible-drag-and-drop-part-2/)).

**Testing note:** Ensure JAWS stays in Forms mode throughout listbox interaction. If you hear "virtual PC cursor" while navigating options, something is wrong with the widget structure.

---

## NVDA

- Switches to focus/forms mode automatically for widget roles like listbox.
- Does **not** announce the "selected" state of an option; however, it announces "not selected" for non-selected options. This asymmetry can confuse users ([24a11y, "Select Your Poison Part 2"](https://www.24a11y.com/2019/select-your-poison-part-2/)).
- ARIA 1.1 combobox patterns (wrapping listbox) "did not show up in scan mode at all" — reinforcing the preference for ARIA 1.2 patterns ([24a11y](https://www.24a11y.com/2019/select-your-poison-part-2/)).

**Testing note:** Because NVDA does not announce "selected," users may need to rely on other cues. Consider live region announcements for selection changes in critical workflows.

---

## VoiceOver (macOS)

- Maps custom listbox differently than native `<select>` (popup button + menu vs listbox + options) ([24a11y](https://www.24a11y.com/2019/select-your-poison/)).
- Can be inconsistent with arrowing and typing in custom implementations.
- Advised a keyboard shortcut "that did nothing" for some combobox patterns ([24a11y](https://www.24a11y.com/2019/select-your-poison-part-2/)).

**Testing note:** Always test both native `<select>` and custom listbox with VoiceOver. The interaction models differ significantly.

---

## VoiceOver (iOS)

- Does not always announce the edit field for comboboxes.
- "Buggy and inconsistent interaction with the options menu" ([24a11y](https://www.24a11y.com/2019/select-your-poison-part-2/)).
- Fails to move keyboard focus when VoiceOver focus enters a combobox.
- May fail to report list boundaries or selected state.

**Testing note:** iOS VoiceOver is the most likely to break with custom listbox implementations. If you must support it, test thoroughly and consider whether native `<select>` would serve users better.

---

## Key Testing Insight

Native `<select>` scored 100% success and 97.5% usability across all screen readers tested. Custom ARIA listbox implementations consistently scored lower ([24a11y, "Select Your Poison Part 2"](https://www.24a11y.com/2019/select-your-poison-part-2/)).

**Recommendation:** If your custom listbox does not pass manual testing with at least JAWS + Chrome, NVDA + Firefox, and VoiceOver + Safari, strongly reconsider whether native `<select>` or a select-only combobox would better serve your users.

---

## Platform Semantics Note

Native `<select>` maps to different platform accessibility roles: combobox on Windows (UI Automation) vs popup button on macOS. Custom ARIA listbox implementations use a single semantic structure for all platforms, which will feel unfamiliar to users on one platform or the other ([24a11y](https://www.24a11y.com/2019/select-your-poison/)).
