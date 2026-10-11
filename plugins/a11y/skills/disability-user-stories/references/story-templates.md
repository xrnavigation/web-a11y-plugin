# Story Templates
## Contents

- [Full Story Template](#full-story-template)
- [Worked Example: Login Form](#worked-example-login-form)
- [Worked Example: Data Table](#worked-example-data-table)
- [Worked Example: Search Autocomplete](#worked-example-search-autocomplete)
- [Quick-Reference: Story Starters by Disability Type](#quick-reference-story-starters-by-disability-type)
  - [Vision](#vision)
  - [Motor](#motor)
  - [Hearing](#hearing)
  - [Cognitive](#cognitive)
  - [Multiple / Compounding](#multiple-compounding)


These are hypothetical story and acceptance-criteria examples, not executed tests or claims about every person with a disability. Specify browser, operating system, assistive technology versions, navigation mode, verbosity/language settings, and fixtures. Record evidence as observed, failed, or not run; quote speech only when actually observed in that environment. Test semantic outcomes rather than a universal speech transcript. Page title correctness is a separate check from announcements after navigation.

## Full Story Template

```markdown
## User Story
As a [persona name] who [specific disability/AT context],
I want to [specific interaction with the feature],
So that [human outcome -- what they can accomplish].

## Persona Context
- **Disability:** [specific condition]
- **Environment:** [OS, browser, AT and versions; input method, navigation mode, language/verbosity settings]
- **Navigation pattern:** [how they typically navigate: headings, landmarks, tab, voice commands]
- **Key frustration:** [what blocks them most often]

## Acceptance Criteria

### Functional (what works)
- [ ] [Action] produces [result] when using [AT]
- [ ] [Component] is operable with [input method]

### Perceivable (what is announced/visible)
- [ ] The relevant name, role, state, description, or status is available and understandable using [specified environment] when [trigger]
- [ ] Focus indicator is visible when [component] receives focus
- [ ] Color is not the only means of conveying [information]

### Understandable (what makes sense)
- [ ] Error messages state what went wrong AND how to fix it
- [ ] Instructions are provided before the user needs them
- [ ] Layout and navigation are consistent with other pages

### Robust (what holds up)
- [ ] Works with [specific AT combinations: NVDA+Firefox, VoiceOver+Safari, JAWS+Chrome]
- [ ] No keyboard traps
- [ ] Focus returns to [trigger element] when [component] is dismissed

## WCAG References
- SC [number]: [name] (Level [A/AA/AAA])

## BDD Scenarios
Given [context with AT]
When [user action]
Then [observable outcome for user]

## Evidence
- Status: [observed / failed / not run]
- Environment and settings: [versions and configuration]
- Observed result: [user outcome; actual speech if collected]
```

---

## Worked Example: Login Form

```markdown
## User Story
As Lakshmi, a blind accountant who uses NVDA with Firefox,
I want to log in to my account using the login form,
So that I can access my financial dashboard independently.

## Persona Context
- **Disability:** Blind
- **AT Used:** NVDA screen reader with Firefox
- **Navigation pattern:** Navigates by headings first, then Tab through interactive elements
- **Key frustration:** Unlabeled form fields, missing error descriptions

## Acceptance Criteria

### Functional
- [ ] All form fields are reachable and operable via keyboard Tab
- [ ] Form submits on Enter when a submit button has focus
- [ ] Password field allows paste (for password managers)

### Perceivable
- [ ] The email field exposes the name Email address, text-input role, and required state in the specified environment
- [ ] The password field exposes the name Password, protected-input semantics, and required state
- [ ] The submit control exposes the name Log in and button role
- [ ] Failed submission makes specific errors discoverable through associated descriptions and the chosen focus/notification strategy
- [ ] Focus moves to the first field in error state after failed submission

### Understandable
- [ ] Error messages state the specific problem: "Email address must include an @ symbol" not "Invalid input"
- [ ] "Forgot password" link text is descriptive (not "click here")

### Robust
- [ ] Works with NVDA+Firefox, JAWS+Chrome, VoiceOver+Safari
- [ ] No keyboard traps in the form
- [ ] Form does not time out while user is entering data

## WCAG References
- SC 1.3.1: Info and Relationships (Level A)
- SC 2.1.1: Keyboard (Level A)
- SC 2.4.7: Focus Visible (Level AA)
- SC 3.3.1: Error Identification (Level A)
- SC 3.3.2: Labels or Instructions (Level A)
- SC 3.3.3: Error Suggestion (Level AA)
- SC 4.1.2: Name, Role, Value (Level A)

## BDD Scenarios

Given I am using NVDA with Firefox
When I Tab to the email field
Then I can identify the email field, its required state, and any applicable instructions

Given I have entered an invalid email address
When I activate the Log In button
Then focus moves to the email field
And I can discover the associated email error and understand how to correct it

Given I have entered valid credentials
When I activate the Log In button
Then I am taken to the dashboard
And focus/context identifies the dashboard through the chosen navigation strategy
And the document title describes the dashboard
And any actual screen reader announcement is recorded separately for this environment
```

Source: [Section 508 User Stories](https://www.section508.gov/develop/user-stories/), [TetraLogical User Stories](https://tetralogical.com/blog/2022/05/26/how-to-write-user-stories-for-accessibility/)

---

## Worked Example: Data Table

```markdown
## User Story
As Lakshmi, a blind accountant who uses NVDA with Firefox,
I want to navigate a financial data table and understand which values belong to which categories,
So that I can review quarterly revenue without sighted assistance.

## Persona Context
- **Disability:** Blind
- **AT Used:** NVDA screen reader with Firefox
- **Navigation pattern:** Uses table navigation (Ctrl+Alt+Arrow keys in NVDA) to move between cells
- **Key frustration:** Tables without proper header associations

## Acceptance Criteria

### Perceivable
- [ ] NVDA announces column and row headers when navigating to each cell
- [ ] The table is identifiable and its row/column structure is available through table navigation in the specified environment
- [ ] Table has a caption or `aria-label` describing its purpose

### Understandable
- [ ] Data cells are not empty; missing data shows "N/A" or equivalent
- [ ] Currency values include the currency symbol

### Robust
- [ ] Table uses `<th>` elements with proper `scope` attributes
- [ ] Works with NVDA+Firefox and JAWS+Chrome

## BDD Scenarios

Given I am using NVDA with Firefox
When I navigate to the data table
Then I can identify the table as Quarterly Revenue and navigate its fixture rows and columns

Given I am in the table
When I press Ctrl+Alt+Right to move to the next column
Then I can determine the cell value and its associated column/row headers; speech order is recorded as observed
```

---

## Worked Example: Search Autocomplete

```markdown
## User Story
As Ade, who has limited arm use from a spinal cord injury and navigates by keyboard,
I want to search for products using the autocomplete search field,
So that I can find items without excessive typing or mouse use.

## Persona Context
- **Disability:** Limited arm use (spinal cord injury)
- **AT Used:** Keyboard navigation, switch device
- **Navigation pattern:** Tab key, arrow keys, minimal keystrokes preferred
- **Key frustration:** Mouse-dependent interfaces, excessive tabbing

## Acceptance Criteria

### Functional
- [ ] Suggestions appear after typing 2+ characters
- [ ] Arrow keys navigate the suggestion list without mouse
- [ ] Enter selects the highlighted suggestion
- [ ] Escape closes the suggestion list and returns focus to the input

### Perceivable
- [ ] Screen reader announces the number of suggestions available
- [ ] Screen reader announces the currently highlighted suggestion
- [ ] Focus indicator is visible on the highlighted suggestion

### Robust
- [ ] Combobox uses `role="combobox"` with `aria-expanded` and `aria-controls`
- [ ] Each suggestion has `role="option"` with `aria-selected` on the active one
- [ ] Works with keyboard alone (no mouse required at any point)

## BDD Scenarios

Given I am a keyboard user
When I type "lap" in the search field
Then a list of suggestions appears
And a status communicates the fixture's available suggestion count without moving focus; record actual speech separately

Given the suggestion list is open
When I press Down Arrow
Then the first suggestion is highlighted
And my screen reader announces the suggestion text

Given a suggestion is highlighted
When I press Enter
Then the search field is populated with the suggestion text
And the suggestion list closes
```

---

## Quick-Reference: Story Starters by Disability Type

Use these as starting points, then add specific acceptance criteria:

### Vision
- "As a screen reader user, I want to [action] so that [outcome]."
- "As a user with low vision who uses 200% zoom, I want to [action] so that [outcome]."
- "As a user who is color blind, I want to [action] so that [outcome]."

### Motor
- "As a keyboard-only user, I want to [action] so that [outcome]."
- "As a voice input user (Dragon NaturallySpeaking), I want to [action] so that [outcome]."
- "As a user with limited dexterity, I want to [action] so that [outcome]."

### Hearing
- "As a deaf user, I want to [action] so that [outcome]."
- "As a user with limited hearing who uses a hearing aid, I want to [action] so that [outcome]."

### Cognitive
- "As a user with ADHD who is easily distracted, I want to [action] so that [outcome]."
- "As a user with dyslexia, I want to [action] so that [outcome]."
- "As a user with a learning disability who needs plain language, I want to [action] so that [outcome]."
- "As an autistic user who relies on predictable interfaces, I want to [action] so that [outcome]."

### Multiple / Compounding
- "As an older user with low vision and hand tremor, I want to [action] so that [outcome]."
- "As a deafblind user who relies on a Braille display, I want to [action] so that [outcome]."
