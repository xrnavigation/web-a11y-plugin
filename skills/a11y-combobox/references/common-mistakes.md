# Common Combobox Accessibility Mistakes

Anti-patterns with citations from practitioner testing. Every item below has been observed to break real assistive technology.

---

## 1. Treating `aria-activedescendant` as Equivalent to DOM Focus

**What goes wrong:**
```html
<!-- Developer moves tabindex to each option, thinking this is "focus" -->
<input role="combobox" ...>
<ul role="listbox">
  <li role="option" tabindex="0">Apple</li>
  <li role="option" tabindex="-1">Banana</li>
</ul>
```

**Why it breaks:**
- Only one element can have true focus (`document.activeElement`)
- `aria-activedescendant` is purely a screen reader semantic — keyboard events still fire on the element with real focus (the input)
- Moving DOM focus to options means keyboard events fire on the option, not the input — typing stops working

**Correct approach:**
```html
<input role="combobox" aria-activedescendant="opt-apple" ...>
<ul role="listbox">
  <li id="opt-apple" role="option" aria-selected="true">Apple</li>
  <li id="opt-banana" role="option">Banana</li>
</ul>
```

DOM focus stays on the input. `aria-activedescendant` tells the screen reader which option is "active." Arrow keys update `aria-activedescendant`; typing updates the input value.

Source: [Higley — aria-activedescendant is not focus](https://sarahmhigley.com/writing/activedescendant/)

---

## 2. Pointing `aria-activedescendant` at Non-Option Elements

**What goes wrong:**
```html
<input role="combobox" aria-activedescendant="clear-btn" ...>
<ul role="listbox">
  <li role="option">Apple</li>
</ul>
<button id="clear-btn">Clear</button>
```

**Why it breaks:**
- Pointing `aria-activedescendant` at a button or other interactive element triggers unwanted screen reader mode switches
- JAWS may switch from forms mode to browse mode; NVDA may switch to application mode
- The user's keyboard interaction changes unpredictably

**Rule:** Keep `aria-activedescendant` pointed only at elements with `role="option"` (or `gridcell`, `treeitem` for those popup types).

Source: [Higley — aria-activedescendant is not focus](https://sarahmhigley.com/writing/activedescendant/)

---

## 3. No `aria-live` Supplement for Announcements

**What goes wrong:**
- Developer relies entirely on `aria-activedescendant` for option announcements
- VoiceOver on Safari ignores `aria-activedescendant` changes when the input is empty
- VoiceOver on Chrome ignores them when `aria-selected="true"` is missing
- NVDA fails to announce text deletions
- Mobile screen readers ignore `aria-activedescendant` almost entirely

**Fix:**
```html
<div aria-live="assertive" aria-atomic="true" class="sr-only">
  Apple, 1 of 5
</div>
```

Update this region when the active option changes. React Aria found this was the only reliable cross-AT approach.

Source: [React Aria — Building a ComboBox](https://react-aria.adobe.com/blog/building-a-combobox)

---

## 4. Using `role="group"` on Option Groups

**What goes wrong:**
```html
<ul role="listbox">
  <li role="group" aria-label="Fruits">
    <ul>
      <li role="option">Apple</li>
      <li role="option">Banana</li>
    </ul>
  </li>
</ul>
```

**Why it breaks:**
- VoiceOver completely fails to announce focus when options are wrapped in `role="group"`
- The user arrows through options and hears nothing

**Workaround:** Use a flat list. If grouping context is needed, include it in the option's accessible name:
```html
<ul role="listbox">
  <li role="option">Apple</li>
  <li role="option">Banana</li>
</ul>
```

Or use `aria-live` to announce group transitions.

Source: [React Aria — Building a ComboBox](https://react-aria.adobe.com/blog/building-a-combobox)

---

## 5. Missing `aria-controls` When Popup Is Hidden

**What goes wrong:**
```javascript
// Developer removes aria-controls when popup closes
input.removeAttribute('aria-controls');
```

**Why it breaks:**
- The APG spec requires `aria-controls` to reference the popup element even when the popup is not visible
- Some screen readers use this reference to determine the combobox's associated popup type
- Removing and re-adding the attribute can cause announcement glitches

**Rule:** `aria-controls` must always be present. Toggle `aria-expanded` and the popup's visibility, but never remove the `aria-controls` reference.

Source: [APG Combobox Pattern — WAI-ARIA Roles, States, Properties](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)

---

## 6. Adding Custom Screen Reader Instructions

**What goes wrong:**
```html
<input role="combobox" aria-description="Press down arrow to see suggestions, escape to close">
```

**Why it breaks:**
- Screen readers already announce how to interact with combobox controls
- Custom instructions conflict with built-in guidance, creating redundancy
- Extra verbosity slows down experienced screen reader users
- Instructions may be wrong for some AT (e.g., VoiceOver uses different gestures on iOS)

**Rule:** Let the screen reader provide its own instructions. Focus on correct ARIA markup so the AT has accurate information.

Source: [Roselli — Stop Giving Control Hints to Screen Readers](https://adrianroselli.com/2019/10/stop-giving-control-hints-to-screen-readers.html)

---

## 7. Using the ARIA 1.1 Readonly Input Pattern

**What goes wrong:**
```html
<!-- ARIA 1.1 pattern — do not use -->
<input type="text" role="combobox" readonly aria-owns="listbox-1">
```

**Why it breaks:**
- NVDA's scan/browse mode does not detect these comboboxes at all — they are invisible
- Users navigating by element type will never find them
- The ARIA 1.2 pattern (using `aria-controls` instead of `aria-owns`) replaced this

**Use instead:** The select-only pattern with `<div role="combobox">` or the editable pattern with `<input role="combobox">` (without `readonly`).

Source: [24a11y — Select Your Poison Part 2](https://www.24a11y.com/2019/select-your-poison-part-2/)

---

## 8. Auto-Filtering Without User Request

**What goes wrong:**
- Combobox immediately filters options as the user types, before any explicit request
- Users with cognitive disabilities or unfamiliarity with autocomplete lose context
- Options disappear and reappear unpredictably

**What testing found:**
- The 24a11y study reported reduced success rates when options auto-filtered
- Recommendation: show the full option list first, then filter only after explicit user interaction (typing, pressing a filter key)

Source: [24a11y — Select Your Poison Part 2](https://www.24a11y.com/2019/select-your-poison-part-2/)

---

## 9. Inconsistent `<datalist>` Behavior Across Platforms

**What goes wrong:**
- Developer uses `<datalist>` assuming consistent behavior
- Chrome/Edge show dropdown arrows on hover; Firefox shows no visual cue
- When `<option value="X">Display text</option>` has differing value and text: Firefox shows text only, Chrome shows both, Safari shows both differently
- VoiceOver announces only the `value`, omitting visible text
- Firefox on Android completely fails to expose datalist
- VoiceOver on iPadOS cannot navigate beyond first 3 options

**Rule:** Use `<datalist>` only if you accept all these inconsistencies. Do not use it if: you need Android Firefox support, users zoom text, voice control is required, `value` differs from displayed text, or iOS/iPadOS must work.

Source: [Roselli — Under-Engineered Comboboxen](https://adrianroselli.com/2023/06/under-engineered-comboboxen.html)
