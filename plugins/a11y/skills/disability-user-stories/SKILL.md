---
name: disability-user-stories
description: Generates accessibility-centered user stories, personas, and acceptance criteria that verify real assistive technology experiences. Use when writing user stories, sprint planning, defining acceptance criteria, or creating accessibility-specific test cases. Provides W3C, GOV.UK, and Microsoft persona frameworks plus Given/When/Then patterns for AT verification.
argument-hint: "[feature-or-component]"
---

# Disability-Centered User Stories

> "As a user, I want the site to be accessible" is not a user story. It is a wish.
> — [TetraLogical](https://tetralogical.com/blog/2022/05/26/how-to-write-user-stories-for-accessibility/)

Automated tools assist evaluation but do not determine accessibility on their own. ([WAI evaluation tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/))

Stories that say "accessible" are not testable. Stories that name the assistive technology, the persona, and the experience are. This skill generates user stories, acceptance criteria, and BDD scenarios that center the disability experience rather than the code implementation.

---

## 1. Why Disability-Centered Stories

Accessibility stories fail when they describe code attributes instead of human experiences. Two symptoms:

**Vague stories nobody can test:**
- "As a user, I want the site to be accessible." (No persona, no AT, no outcome)
- "As a disabled user, I want to use the site." (Disability is not monolithic)
- "As a developer, I want to add aria-labels to all buttons." (This is a task, not a story)

**Code-focused acceptance criteria that miss the point:**

| Bad (Code-Focused) | Good (Experience-Focused) |
|---|---|
| "Image has alt attribute" | "Screen reader announces descriptive text that conveys the image's purpose" |
| "Button has aria-label" | "Screen reader announces the button's visible text and purpose" |
| "Error div has role=alert" | "When I submit invalid data, I can find which fields have errors and their correction guidance through associated field descriptions and a deliberate submission notification/focus strategy" |
| "Dialog has aria-modal=true" | "When the dialog opens, focus moves inside it; I can tab through its contents without escaping to the background; Escape closes it and returns focus to the trigger" |
| "Input has associated label element" | "When I tab to this field, my screen reader announces its label, whether it is required, and any format instructions" |

The criterion is what the human experiences, not what the code does.

Sources: [TetraLogical](https://tetralogical.com/blog/2022/05/26/how-to-write-user-stories-for-accessibility/), [Section 508](https://www.section508.gov/develop/user-stories/)

---

## 2. Persona Frameworks

Three established frameworks provide ready-made personas. Use them directly or as templates for project-specific personas.

### W3C WAI Personas (9 personas)

| Persona | Disability | AT / Needs |
|---|---|---|
| **Ade** | Limited arm use (spinal cord injury) | Keyboard, switch device |
| **Ian** | Autism | Predictable structure, calm design |
| **Lakshmi** | Blind | Screen reader (desktop + mobile) |
| **Lexie** | Color blind (deuteranopia/protanopia) | Non-color indicators |
| **Sophie** | Down syndrome | Plain language, simple layouts |
| **Dhruv** | Deaf | Captions, transcripts |
| **Marta** | Deafblind | Braille display, screen magnification, captions |
| **Stefan** | Dyslexia + ADHD | Customizable text, reduced distractions |
| **Elias** | Low vision + hand tremor + memory loss | Screen magnification, consistent layouts |

Source: [W3C WAI User Stories](https://www.w3.org/WAI/people-use-web/user-stories/)

### GOV.UK Accessibility Personas (7 personas)

Simulated Chrome browser profiles for empathy testing. Teams run 50-minute sessions where each member adopts a persona and attempts real user tasks.

| Persona | Condition | AT Simulation |
|---|---|---|
| **Claudia** | Sight impaired | Screen magnifier |
| **Ashleigh** | Severely sight impaired | Screen reader |
| **Ron** | Older user, multiple conditions | Multiple AT |
| **Chris** | Rheumatoid arthritis | Voice control / limited dexterity |
| **Pawel** | Autistic | Neurodivergent interaction patterns |
| **Simone** | Dyslexic | Text-to-speech, dyslexia-friendly formatting |
| **Saleem** | Profoundly deaf | No audio access |

**Critical caveat from GDS:** "A simulation is never a true representation of an impairment. It's only a tool trying to make some things roughly as difficult for someone without that impairment."

Sources: [GDS Persona Profiles](https://accessibility.blog.gov.uk/2019/02/11/using-persona-profiles-to-test-accessibility/), [GOV.UK Accessibility Personas](https://alphagov.github.io/accessibility-personas/)

### Microsoft Inclusive Design Persona Spectrum

Disability as a mismatch between person and environment, not an inherent deficit. Solutions for permanent disabilities cascade benefits to temporary and situational contexts.

| Ability | Permanent | Temporary | Situational |
|---|---|---|---|
| Touch | One arm | Arm in cast | Holding a baby |
| See | Blind | Cataracts | Distracted driver |
| Hear | Deaf | Ear infection | Bartender in loud bar |
| Speak | Nonverbal | Laryngitis | Heavy accent in foreign country |

This spectrum expands the "who benefits" framing and builds organizational buy-in: keyboard accessibility benefits the one-armed user, the broken-arm user, AND the parent holding a baby.

Source: [Microsoft Inclusive Design](https://inclusive.microsoft.design/)

Full persona details: [references/persona-catalog.md](references/persona-catalog.md)

---

## 3. Story Template

```
As a [persona name] who [specific disability/AT context],
I want to [specific interaction with the feature],
So that [human outcome -- what they can accomplish].
```

Every slot matters:
- **Persona slot:** Must name the specific disability or AT. "As a user" is never acceptable for an accessibility story.
- **Goal slot:** Describes an interaction, not a technical implementation.
- **Benefit slot:** States the human outcome, not a WCAG reference.

Full template with persona context, acceptance criteria sections, WCAG references, and BDD scenarios: [references/story-templates.md](references/story-templates.md)

---

## 4. Example Stories by Disability Type

### Blind (Screen Reader Users)

- "As a screen reader user, I want to hear the text equivalent for each image button so that I will know what function it performs."
- "As a screen reader user, I want to know the column and row headers for each table cell so that I can understand the meaning of the data."
- "As a screen reader user, I want to know the page language so that my screen reader uses the correct pronunciation."

### Keyboard-Only Users

- "As a keyboard-only user, I want to know where I am on the screen so that I can perform an action or navigate."
- "As a keyboard-only user, I want to be able to navigate content without getting stuck so that I can complete my task."
- "As a keyboard-only user, I want to be able to skip repeated navigation so that I can reach the main content quickly."

### Low Vision

- "As a user with limited vision, I want to be able to zoom to 200% without losing content so that I can read text at a comfortable size."
- "As a user who sees better with high contrast, I want sufficient contrast between text and its background so that I can read content."

### Cognitive / Learning Disabilities

- "As a user who struggles to comprehend a lot of content at once, I want descriptive headings so that I can understand the type of content in each section."
- "As a user who has limited attention, I want to stop all moving or blinking content so that I can focus on reading."
- "As a user who has trouble following detailed instructions, I want to easily understand what is required in each form field so that I can complete the form."

### Deaf / Hard of Hearing

- "As a user without hearing, I want captions on multimedia so that I can understand the audio content."
- "As a user with limited hearing, I want to be able to easily turn off auto-playing audio so that it does not interfere with my hearing aid."

### Motor / Limited Manipulation

- "As a user with limited ability to use a keyboard and mouse, I want time outs to allow me sufficient time so that I can complete tasks at my own pace."
- "As a voice input user, I want to be able to use my dictation software to control the interface so that I can work hands-free."

### Photosensitive

- "As a user with photoepileptic seizures, I want to navigate content without it triggering a medical response so that I can use the web safely."

Source: [Section 508 Sample User Stories](https://www.section508.gov/develop/user-stories/)

---

## 5. Acceptance Criteria Patterns

### Three-Level Model

Acceptance criteria should be defined at three levels to ensure nothing falls through the cracks (per [Cerovac](https://cerovac.com/a11y/2020/10/acceptance-criteria-and-accessibility/)):

**Page level:**
- Valid HTML; unique, descriptive page title; language attribute set; landmark regions defined

**Container level:**
- Section headings present and hierarchical; heading text describes section content; related form fields grouped with fieldset/legend

**Component level:**
- Interactive element has accessible name; role communicated to AT; state changes announced; keyboard interaction matches expected behavior

### AT Verification, Not Code Attributes

Acceptance criteria must specify what the user experiences:

```
### Perceivable (what is announced/visible)
- [ ] The relevant semantic name, role, state, description, or status is understandable in the specified test environment when [trigger]
- [ ] Focus indicator is visible when [component] receives focus
- [ ] Color is not the only means of conveying [information]

### Understandable (what makes sense)
- [ ] Error messages state what went wrong AND how to fix it
- [ ] Instructions are provided before the user needs them

### Robust (what holds up)
- [ ] Works with [specific AT: NVDA+Firefox, VoiceOver+Safari, JAWS+Chrome]
- [ ] No keyboard traps
- [ ] Focus returns to [trigger element] when [component] is dismissed
```

### The Coles Supermarket Model

Australian supermarket Coles developed 10 Accessibility Acceptance Criteria covering the most commonly failing WCAG success criteria. Key insight: **10 high-impact criteria beat 50 ignored ones.** A focused set drives more actual improvement than a comprehensive checklist teams skip.

The 10 criteria: Keyboard, Content on Hover, Page Title, Visible Focus, Semantic Markup, Form Control Labeling, Screen Reader announcements, Zoom and Resize, Alt Text, Orientation and Reflow.

Source: [CANAXESS / Coles AACs](https://www.canaxess.com.au/articles/accessibility-acceptance-criteria/)

Full patterns and templates: [references/acceptance-criteria-patterns.md](references/acceptance-criteria-patterns.md)

---

## 6. BDD / Given-When-Then for Accessibility

### When to Use Gherkin

**Use Gherkin** for scenarios describing user behavior: keyboard navigation, screen reader interaction, visual feedback, form behavior.

**Do NOT use Gherkin** for technical validation requiring source code inspection (checking ARIA attributes, validating HTML). Use axe-core, Pa11y, or Lighthouse for those.

**Rule of thumb:** If the test describes what a user does and perceives, use Gherkin. If it requires looking at markup, use automated tools. Combine both.

Source: [Hassell Inclusion](https://www.hassellinclusion.com/blog/gherkin-accessibility-tests/)

### Examples

**Skip Navigation:**
```gherkin
Given I am on the homepage
When I press Tab as the first keyboard action
Then a "Skip to content" link becomes visible
When I activate the skip link
Then the main content area has keyboard focus
```

**Form Validation:**
```gherkin
Given I am a screen reader user
When I submit a form with validation errors
Then focus moves to the first field in error state
And my screen reader announces the error message and how to fix it
```

**Dialog/Modal:**
```gherkin
Given I am a screen reader user
When I activate a button that opens a dialog
Then keyboard focus moves to the dialog
And I can navigate within the dialog using Tab
And I cannot Tab to content behind the dialog
When I press Escape
Then the dialog closes
And focus returns to the button that opened it
```

**Dynamic Content:**
```gherkin
Given I am a screen reader user
When I click a button that loads content asynchronously
Then I hear an announcement that content is loading
When the content finishes loading
Then I hear a confirmation that new content is available
```

### What NOT to Write in Gherkin

These require code inspection, not user behavior testing:
- "Then each anchor tag has the href attribute"
- "Then the page has exactly one h1 element"
- "Then all images have non-empty alt attributes"
- "Then ARIA landmarks are correctly defined"

Sources: [Hassell Inclusion](https://www.hassellinclusion.com/blog/gherkin-accessibility-tests/), [accessibility-gherkin GitHub](https://github.com/bshack/accessibility-gherkin)

---

## 7. Shift-Left Integration

Accessibility acceptance criteria belong in the story before development starts, not in a QA phase after. Define and test accessibility behavior before release; do not apply a universal repair-cost multiplier. ([IAPM](https://www.iapm.net/en/blog/shift-left-accessibility/))

### Definition of Done

A team's Definition of Done should include four accessibility gates (per [Accessibility for Teams](https://accessibility-for-teams.com/article/accessibility-in-the-definition-of-done)):

1. **Automated accessibility testing passed** -- axe, WAVE, Lighthouse, or Pa11y (use multiple tools; each catches different issues)
2. **Manual WCAG review completed** -- scope manual review to the applicable criteria and combine keyboard, zoom, visual/content, pointer, and supported assistive technology checks; a screen reader alone does not cover every criterion
3. **Accessibility statement updated** -- if the feature has known limitations, document them
4. **Content style guide followed** -- plain language, descriptive link text, proper alt text, meaningful headings

### Sprint Planning

- Estimate accessibility work as part of the story, not a separate task
- Include keyboard testing and screen reader testing in the test plan
- Identify which WCAG criteria the story touches

### Design Review

- Review mockups for color contrast, focus states, keyboard interaction patterns
- Annotate designs with heading levels, landmark regions, reading order
- Define all component states (hover, focus, active, disabled, error, loading)

---

## 8. Anti-Patterns

### Vague "Accessible" Stories

| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| "As a user, I want the site to be accessible" | No persona, no AT, no testable outcome | Name the persona, the AT, and the specific interaction |
| "As a disabled user, I want to use the site" | Disability is not monolithic; different disabilities have different barriers | One story per disability type and interaction |
| "Make it accessible" as a task | No acceptance criteria, no way to verify | Write specific AT-verified acceptance criteria |

### Testing Attributes, Not Experiences

| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| "Image has alt attribute" | Alt may be empty, wrong, or unhelpful | "Screen reader announces descriptive text that conveys the image's purpose" |
| "Button has aria-label" | Label may not match visible text (WCAG 2.5.3 violation) | "Screen reader announces the button's visible text and purpose" |
| "axe passes, so we're accessible" | Automated coverage depends on the rules, content, states, and evaluation scope | Add keyboard testing and screen reader verification |
| "We tested with Chrome DevTools" | DevTools shows the accessibility tree, not what users hear | Run NVDA or VoiceOver and listen |

### Missing the Spectrum

Consider permanent, temporary, and situational access needs using the persona spectrum, then evaluate actual task outcomes. Do not infer a population percentage or universal benefit from that framework.

---

## 9. Cross-References

- `at-experience-verification` -- what screen readers, keyboard, and voice control users actually experience; "what bad sounds like" examples
- `testing-strategy` -- three-tier testing model (automated, keyboard, screen reader); acceptance criteria templates
- `cognitive-neurodivergent-experience` -- sensory overload, predictability, anxiety patterns for neurodivergent users
- `accessible-content-writing` -- link text, error messages, alt text, plain language quality
- `form-a11y` -- form labeling, error handling, validation patterns
- `focus-management` -- modal focus trapping, SPA route changes, focus restoration

For detailed reference material:

- [references/persona-catalog.md](references/persona-catalog.md) -- full persona details from all three frameworks
- [references/story-templates.md](references/story-templates.md) -- complete story-to-criteria templates with worked examples
- [references/acceptance-criteria-patterns.md](references/acceptance-criteria-patterns.md) -- three-level model, Coles AACs, AT verification patterns
- [references/sources.yaml](references/sources.yaml) -- provenance for all cited sources

Read [common mistakes](references/common-mistakes.md) for concrete wrong/right examples.
