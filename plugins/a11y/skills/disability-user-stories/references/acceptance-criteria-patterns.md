# Acceptance Criteria Patterns
## Contents

- [The Three-Level Model](#the-three-level-model)
  - [Page Level](#page-level)
  - [Container Level](#container-level)
  - [Component Level](#component-level)
- [AT Verification Patterns](#at-verification-patterns)
  - [Screen Reader Announcement Pattern](#screen-reader-announcement-pattern)
  - [Focus Management Pattern](#focus-management-pattern)
  - [Keyboard Operability Pattern](#keyboard-operability-pattern)
  - [State Communication Pattern](#state-communication-pattern)
- [The Coles Supermarket Model (10 Accessibility Acceptance Criteria)](#the-coles-supermarket-model-10-accessibility-acceptance-criteria)
  - [1. Keyboard](#1-keyboard)
  - [2. Content on Hover](#2-content-on-hover)
  - [3. Page Title](#3-page-title)
  - [4. Visible Focus](#4-visible-focus)
  - [5. Semantic Markup](#5-semantic-markup)
  - [6. Form Control Labeling](#6-form-control-labeling)
  - [7. Screen Reader (Dynamic Content)](#7-screen-reader-dynamic-content)
  - [8. Zoom and Resize](#8-zoom-and-resize)
  - [9. Alt Text](#9-alt-text)
  - [10. Orientation and Reflow](#10-orientation-and-reflow)
- [Experience-Focused vs Code-Focused Criteria](#experience-focused-vs-code-focused-criteria)
- [Definition of Done Accessibility Checklist](#definition-of-done-accessibility-checklist)


Patterns for writing acceptance criteria that verify real assistive technology experiences, not just code attributes.

## The Three-Level Model

Define acceptance criteria at three levels to catch issues at every scope (per [Cerovac](https://cerovac.com/a11y/2020/10/acceptance-criteria-and-accessibility/)):

### Page Level

```
- [ ] HTML validates without errors
- [ ] Page has a unique, descriptive <title>
- [ ] Page language is set via lang attribute
- [ ] Landmark regions are defined (header/banner, nav, main, footer/contentinfo)
- [ ] Skip navigation link is present and functional
- [ ] Only one <main> landmark exists
```

### Container Level

```
- [ ] Section headings are present and follow a logical hierarchy (ranks reflect section relationships; avoiding downward skips is authoring guidance)
- [ ] Heading text accurately describes the section content
- [ ] Related form fields are grouped with <fieldset> and <legend>
- [ ] Lists use semantic list markup (<ul>, <ol>, <dl>)
- [ ] Data tables have proper <th> elements with scope attributes
```

### Component Level

```
- [ ] Interactive element has an accessible name that matches or contains its visible text
- [ ] Element role is communicated to assistive technology (native HTML or correct ARIA role)
- [ ] State changes are announced (expanded/collapsed, checked/unchecked, selected, disabled)
- [ ] Keyboard interaction pattern matches the expected behavior for this widget type
- [ ] Focus indicator is visible with at least 3:1 contrast ratio
- [ ] Focus order follows a logical sequence
```

---

## AT Verification Patterns

These patterns specify what the user experiences rather than what the code does.

### Screen Reader Announcement Pattern

```
When [trigger event],
the user can identify [required name, role, state, description, or status] in [versioned environment and settings].
Record actual speech separately as observed evidence; mark unexecuted checks not run.
```

**Examples:**
- On email-field focus, the user can identify its name, input role, required state, and associated instructions.
- After failed submission, errors are discoverable through associated descriptions and the chosen notification/focus strategy.
- On dialog opening, the user can identify its dialog role, name, and relevant description.
- On selecting a tab, the user can identify its label, tab role, selected state, and associated panel.

### Focus Management Pattern

```
When [trigger event]:
1. Focus moves to [target element]
2. [Target element] has a visible focus indicator
3. Tab cycles within [container] only (if modal/trapped)
4. When [dismiss event], focus returns to [original trigger]
```

**Examples:**
- When dialog opens: focus moves to dialog heading; Tab cycles within dialog; Escape closes dialog and returns focus to the button that opened it
- When route changes in SPA: focus moves to the new page heading or main content area
- On failed submission: use the chosen summary or first-invalid-field focus strategy; ordinary inline validation need not move focus.

### Keyboard Operability Pattern

```
[Component] is fully operable using only:
- Tab/Shift+Tab: [what they do for this component]
- Enter: [what it does]
- Space: [what it does]
- Arrow keys: [what they do, if applicable]
- Escape: [what it does, if applicable]
- Home/End: [what they do, if applicable]
```

### State Communication Pattern

```
When [state change occurs]:
- Visual indicator changes to show [new state]
- Updated state is available to assistive technology and understandable in the specified environment
- aria-[state attribute] updates to [new value]
```

**Examples:**
- When an accordion section expands: the visual indicator reflects expansion and `aria-expanded` updates to `true`; the user can determine the expanded state in the specified environment.
- When a checkbox is checked: its visual and accessible checked state update; native inputs expose their checked state without requiring redundant ARIA. Record observed speech separately.

---

## The Coles Supermarket Model (10 Accessibility Acceptance Criteria)

Coles developed 10 high-impact criteria using Given-When-Then format accessible to non-specialists. Key insight: **progress over perfection** -- 10 focused criteria drive more improvement than 50 ignored ones.

### 1. Keyboard

```
Given I am a keyboard user,
When I encounter interactive content,
Then I can control it solely from the keyboard.
```

### 2. Content on Hover

```
Given I am a keyboard or mouse user,
When content appears on hover or focus,
Then the content is dismissable, hoverable, and persistent.
```

### 3. Page Title

```
Given I navigate to a page,
When the page loads,
Then the page title clearly and uniquely identifies the page content.
```

### 4. Visible Focus

```
Given I am a keyboard user,
When I tab through interactive elements,
Then each element has a clearly visible focus indicator.
```

### 5. Semantic Markup

```
Given content has visual structure (headings, lists, tables),
When I access it with assistive technology,
Then the structure is communicated through appropriate HTML semantics.
```

### 6. Form Control Labeling

```
Given I encounter a form,
When I focus on each form control,
Then my AT announces a clear label, required state, and any format instructions.
When I submit with errors,
Then inline error messages describe the problem and how to fix it.
```

### 7. Screen Reader (Dynamic Content)

```
Given dynamic content changes occur,
When content is added, removed, or updated,
Then relevant status information is exposed without requiring focus under SC 4.1.3; other changes use an appropriate focus or notification strategy. Avoid announcing every DOM update.
```

### 8. Zoom and Resize

```
Given I zoom to 200%,
When I view the page,
Then text can be resized to 200% without loss of content or functionality (SC 1.4.4). Separately verify reflow at 320 CSS pixels width or 256 CSS pixels height, including the essential two-dimensional-content exception (SC 1.4.10).
```

### 9. Alt Text

```
Given images are present on the page,
When I access them with a screen reader,
Then meaningful images have descriptive alt text and decorative images are hidden from AT.
```

### 10. Orientation and Reflow

```
Given I access the site on different devices and orientations,
When content reflows,
Then all content and functionality remain accessible.
```

Source: [CANAXESS / Coles Accessibility Acceptance Criteria](https://www.canaxess.com.au/articles/accessibility-acceptance-criteria/)

---

## Experience-Focused vs Code-Focused Criteria

Always prefer experience-focused criteria. Use code-focused criteria only as internal implementation notes.

| Component | Code-Focused (avoid) | Experience-Focused (use) |
|---|---|---|
| Image | "Image has `alt` attribute" | "Screen reader announces descriptive text that conveys the image's purpose" |
| Button | "Button has `aria-label`" | "Screen reader announces the button's visible text and purpose" |
| Error | "Error div has `role=alert`" | "When I submit invalid data, I can find which fields have errors and their correction guidance through associated field descriptions and a deliberate submission notification/focus strategy" |
| Modal | "Dialog has `aria-modal=true`" | "When the dialog opens, focus moves inside; I can tab through contents without reaching the background; Escape closes it and returns focus to the trigger" |
| Form field | "Input has associated `<label>`" | "When I tab to this field, my screen reader announces its label, whether it is required, and any format instructions" |
| Link | "Link has text content" | "When I pull up my screen reader's links list, each link text clearly describes its destination" |
| Heading | "Page has `<h1>` element" | "When I navigate by headings, the heading structure gives me a scannable outline of the page content" |
| Table | "Table has `<th>` elements" | "When I navigate between table cells, my screen reader announces the relevant column and row headers" |

Sources: [TetraLogical](https://tetralogical.com/blog/2022/05/26/how-to-write-user-stories-for-accessibility/), [Section 508](https://www.section508.gov/develop/user-stories/)

---

## Definition of Done Accessibility Checklist

Add these to your team's Definition of Done:

```
### Accessibility (required for every story)
- [ ] Automated accessibility testing passed (axe-core, zero violations)
- [ ] Keyboard-only operation verified (full workflow, no traps)
- [ ] Focus management correct (modals, route changes, dynamic content)
- [ ] Screen reader announces all content meaningfully (tested with NVDA or VoiceOver)
- [ ] Color contrast meets WCAG AA (4.5:1 text, 3:1 large text, 3:1 UI components)
- [ ] Text resize to 200% retains content/functionality; reflow is separately checked at the SC 1.4.10 viewport thresholds and exceptions
- [ ] Error states announced and associated with fields
- [ ] Heading hierarchy logical (ranks reflect section relationships; avoiding downward skips is authoring guidance)
```

Source: [Accessibility for Teams](https://accessibility-for-teams.com/article/accessibility-in-the-definition-of-done)
