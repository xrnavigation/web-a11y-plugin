# Persona Catalog
## Contents

- [W3C WAI Personas](#w3c-wai-personas)
  - [Ade -- Limited Arm Use](#ade----limited-arm-use)
  - [Ian -- Autism](#ian----autism)
  - [Lakshmi -- Blind](#lakshmi----blind)
  - [Lexie -- Color Blind](#lexie----color-blind)
  - [Sophie -- Down Syndrome](#sophie----down-syndrome)
  - [Dhruv -- Deaf](#dhruv----deaf)
  - [Marta -- Deafblind](#marta----deafblind)
  - [Stefan -- Dyslexia + ADHD](#stefan----dyslexia-adhd)
  - [Elias -- Multiple Conditions](#elias----multiple-conditions)
- [GOV.UK Accessibility Personas](#govuk-accessibility-personas)
  - [Claudia -- Sight Impaired](#claudia----sight-impaired)
  - [Ashleigh -- Severely Sight Impaired](#ashleigh----severely-sight-impaired)
  - [Ron -- Older User](#ron----older-user)
  - [Chris -- Rheumatoid Arthritis](#chris----rheumatoid-arthritis)
  - [Pawel -- Autistic](#pawel----autistic)
  - [Simone -- Dyslexic](#simone----dyslexic)
  - [Saleem -- Profoundly Deaf](#saleem----profoundly-deaf)
- [Microsoft Inclusive Design Persona Spectrum](#microsoft-inclusive-design-persona-spectrum)
  - [Three Principles](#three-principles)
  - [Spectrum Table](#spectrum-table)
  - [Using the Spectrum in Stories](#using-the-spectrum-in-stories)
- [Building Custom Personas](#building-custom-personas)


Detailed persona information from three established frameworks. Use these personas directly in user stories or as templates for project-specific personas.

## W3C WAI Personas

Nine personas representing different disabilities and barriers. Each grounds user stories in specific AT usage and common frustrations.

### Ade -- Limited Arm Use

- **Disability:** Spinal cord injury, limited arm use
- **AT Used:** Keyboard navigation, switch device
- **Navigation pattern:** Tab key, skip links, keyboard shortcuts
- **Key barriers:** Mouse-dependent interfaces, no skip links, drag-and-drop without keyboard alternative
- **Story starter:** "As Ade, who navigates entirely by keyboard due to limited arm use, I want to..."

### Ian -- Autism

- **Disability:** Autism spectrum
- **AT Used:** Predictable structure, calm design (not traditional AT)
- **Navigation pattern:** Relies on consistent layouts and predictable interaction patterns
- **Key barriers:** Carousels, pop-ups, auto-play media, unexpected layout changes, sensory overload
- **Story starter:** "As Ian, who is autistic and relies on predictable, calm interfaces, I want to..."

### Lakshmi -- Blind

- **Disability:** Blind
- **AT Used:** Screen reader (desktop and mobile)
- **Navigation pattern:** Navigates by headings first, then Tab through interactive elements; uses links list for quick navigation
- **Key barriers:** Unlabeled images/forms, broken heading structure, missing landmarks, ambiguous link text
- **Key frustration:** Unlabeled form fields, missing error descriptions
- **Story starter:** "As Lakshmi, a blind user who navigates with a screen reader, I want to..."

### Lexie -- Color Blind

- **Disability:** Color blind (deuteranopia/protanopia -- red/green color blindness)
- **AT Used:** Non-color indicators (not traditional AT)
- **Key barriers:** Color-only information in charts, error states conveyed only by red text, links distinguished only by color
- **Story starter:** "As Lexie, who cannot distinguish red from green, I want to..."

### Sophie -- Down Syndrome

- **Disability:** Down syndrome
- **AT Used:** Plain language, simple layouts (not traditional AT)
- **Key barriers:** Acronyms, jargon, complex multi-step processes, dense text
- **Story starter:** "As Sophie, who needs plain language and simple layouts, I want to..."

### Dhruv -- Deaf

- **Disability:** Deaf
- **AT Used:** Captions, transcripts
- **Key barriers:** Audio content without text alternatives, auto-playing audio, phone-number-only contact
- **Story starter:** "As Dhruv, who is deaf and relies on captions and transcripts, I want to..."

### Marta -- Deafblind

- **Disability:** Deafblind
- **AT Used:** Braille display, screen magnification, captions
- **Key barriers:** Audio + visual content without text alternatives, content that requires both sight and hearing simultaneously
- **Story starter:** "As Marta, who is deafblind and uses a Braille display, I want to..."

### Stefan -- Dyslexia + ADHD

- **Disability:** Dyslexia and ADHD
- **AT Used:** Customizable text, reduced distractions, text-to-speech
- **Key barriers:** Dense text, animations, time pressure, inability to customize font/spacing
- **Story starter:** "As Stefan, who has dyslexia and ADHD and needs reduced distractions, I want to..."

### Elias -- Multiple Conditions

- **Disability:** Low vision + hand tremor + memory loss
- **AT Used:** Screen magnification, consistent layouts
- **Key barriers:** Multiple compounding barriers -- small targets, inconsistent navigation, content that requires remembering previous steps
- **Story starter:** "As Elias, who has low vision, hand tremor, and memory difficulties, I want to..."

Source: [W3C WAI User Stories](https://www.w3.org/WAI/people-use-web/user-stories/)

---

## GOV.UK Accessibility Personas

Seven personas with Chrome browser profile simulations. Teams run 50-minute sessions where each member adopts a persona and attempts real user tasks through the simulated environment. Available as remote Chrome profiles.

### Claudia -- Sight Impaired

- **Condition:** Partially sighted
- **AT Simulation:** Screen magnifier
- **Testing focus:** Content reflow at magnification, target sizes, contrast

### Ashleigh -- Severely Sight Impaired

- **Condition:** Severely sight impaired
- **AT Simulation:** Screen reader
- **Testing focus:** Heading structure, form labels, image descriptions, navigation

### Ron -- Older User

- **Condition:** Multiple age-related conditions
- **AT Simulation:** Multiple AT tools
- **Testing focus:** Compounding barriers, cognitive load, motor precision

### Chris -- Rheumatoid Arthritis

- **Condition:** Rheumatoid arthritis
- **AT Simulation:** Voice control / limited dexterity
- **Testing focus:** Keyboard-only operation, target sizes, timeout handling

### Pawel -- Autistic

- **Condition:** Autism spectrum
- **AT Simulation:** Neurodivergent interaction patterns
- **Testing focus:** Predictable layouts, sensory overload, plain language

### Simone -- Dyslexic

- **Condition:** Dyslexia
- **AT Simulation:** Text-to-speech, dyslexia-friendly formatting
- **Testing focus:** Readability, text customization, content structure

### Saleem -- Profoundly Deaf

- **Condition:** Profoundly deaf
- **AT Simulation:** No audio access
- **Testing focus:** Captions, transcripts, visual alternatives to audio

**Critical caveat from GDS:** "A simulation is never a true representation of an impairment. It's only a tool trying to make some things roughly as difficult for someone without that impairment."

Sources: [GDS Persona Profiles](https://accessibility.blog.gov.uk/2019/02/11/using-persona-profiles-to-test-accessibility/), [GOV.UK Accessibility Personas](https://alphagov.github.io/accessibility-personas/)

---

## Microsoft Inclusive Design Persona Spectrum

Treats disability as a mismatch between person and environment. Maps each ability across three contexts to show how solutions cascade benefits.

### Three Principles

1. **Recognize exclusion** -- identify who is excluded and why
2. **Learn from diversity** -- people who adapt to barriers are experts in innovation
3. **Solve for one, extend to many** -- solutions can support additional users; validate rather than assuming universal benefit

### Spectrum Table

| Ability | Permanent | Temporary | Situational |
|---|---|---|---|
| **Touch** | One arm | Arm in cast | Holding a baby |
| **See** | Blind | Cataracts | Distracted driver |
| **Hear** | Deaf | Ear infection | Bartender in loud bar |
| **Speak** | Nonverbal | Laryngitis | Heavy accent in foreign country |

### Using the Spectrum in Stories

When writing a story for a permanent disability, add a "who else benefits" note:

```
As Ade, who navigates entirely by keyboard due to limited arm use,
I want to skip repeated navigation blocks,
So that I can reach the main content without excessive tabbing.

Who else benefits:
- Temporary: User with broken wrist in a cast
- Situational: User holding coffee while browsing on laptop
- Power users: Anyone who prefers keyboard shortcuts
```

This framing builds organizational buy-in by showing accessibility improvements benefit far more people than the primary persona.

Sources: [Microsoft Inclusive Design](https://inclusive.microsoft.design/), [UX Booth Persona Spectrums](https://uxbooth.com/articles/persona-spectrums-building-for-inclusion-and-accessibility/)

---

## Building Custom Personas

When creating project-specific disability personas:

- **Include:** Name, background, occupation, disability type, AT preferences, content consumption habits, specific frustrations, goals
- **Frame positively:** "proficient with keyboard shortcuts" rather than "cannot see"
- **Be specific about AT:** Not just "uses a screen reader" but "uses NVDA with Firefox, prefers concise well-structured text, navigates primarily by headings"
- **Ground in research:** Interviews, surveys, usability testing with disabled users. Never invent persona details from assumptions
- **Treat as living documents:** Refine based on feedback and technology changes

Personas complement but never replace automated testing, manual testing, or direct user feedback.

Source: [DubBot Personas](https://dubbot.com/dubblog/2025/personas-a-human-centered-approach-to-accessibility.html)
