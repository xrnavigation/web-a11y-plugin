# Acceptance Criteria Patterns

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
- [ ] Section headings are present and follow a logical hierarchy (no skipped levels)
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
the screen reader announces: "[expected announcement text]"
```

**Examples:**
- When focus moves to the email field, the screen reader announces: "Email address, edit text, required"
- When the user activates the submit button with errors present, the screen reader announces: "Error: [field name] [specific problem]"
- When the dialog opens, the screen reader announces: "Dialog: [dialog title]"
- When the user selects a tab, the screen reader announces: "[tab label], tab [N] of [total]"

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
- When inline error appears: focus moves to the first field in error state

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
- Screen reader announces [state change text]
- aria-[state attribute] updates to [new value]
```

**Examples:**
- When accordion section expands: chevron rotates, screen reader announces "expanded", `aria-expanded` updates to "true"
- When checkbox is checked: checkmark appears, screen reader announces "checked", `aria-checked` updates to "true"

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
Then the change is announced to screen reader users.
```

### 8. Zoom and Resize

```
Given I zoom to 200%,
When I view the page,
Then all content and functionality remain available without horizontal scrolling.
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
| Error | "Error div has `role=alert`" | "When I submit invalid data, my screen reader immediately announces what went wrong and how to fix it" |
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
- [ ] Content reflows at 200% zoom without horizontal scrolling
- [ ] Error states announced and associated with fields
- [ ] Heading hierarchy logical (no skipped levels)
```

Source: [Accessibility for Teams](https://accessibility-for-teams.com/article/accessibility-in-the-definition-of-done)
