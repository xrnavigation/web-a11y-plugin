---
name: cognitive-neurodivergent-experience
description: Guides design review for cognitive, learning, attention, sensory, and memory access needs. Use when creating timed tasks, multi-step forms, animations, notification-heavy interfaces, or save-and-resume flows; complements cognitive-a11y implementation patterns without treating diagnoses as uniform experiences.
---

# Cognitive and Neurodivergent Experience

Identify barriers in the task rather than inferring how every person with a diagnosis experiences it. W3C's cognitive guidance describes diverse needs and goes beyond WCAG; it is supplemental guidance, not a separate conformance level. ([COGA usable](https://www.w3.org/TR/coga-usable/))

## Start with a task and an observed need

Ask what the person must remember, read, decide, input, or tolerate to complete the task. Use user stories to explore possible barriers, then test with actual participants; a persona is not a universal user profile. ([WAI user stories](https://www.w3.org/WAI/people-use-web/user-stories/))

| Task demand | Design question | Suggested project response |
|---|---|---|
| Remember information across steps | Can the user review previous answers? | Review page, retained input, clear Back action. |
| Complete without a break | Can work be saved and resumed? | Explicit save state and recoverable progress. |
| Interpret unfamiliar terms | Are explanations close to the task? | Define necessary terms and show examples. |
| Handle interruptions | Can optional prompts be postponed? | Dismissible prompts; defer promotional interruptions. |
| Process changing content | Can motion and updates be controlled? | User-initiated progression and pause controls. |

These responses are project choices informed by [COGA guidance](https://www.w3.org/TR/coga-usable/); validate them against the audience and task.

## Time, anxiety, and data loss

Some people need extra time or breaks; design the recovery path before adding a countdown. Protect draft work using an appropriate retention policy and truthful save feedback. Do not claim that all neurodivergent users panic, freeze, or abandon a task. ([COGA data-loss pattern](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p09-data-loss/))

Distinguish WCAG requirements from the project's preferred design:

- SC 2.2.1 (A) offers turn-off, adjustment before encounter over a range at least ten times the default, or extension with at least 20 seconds to act and at least ten extensions. Real-time, essential, and over-20-hour exceptions have conditions; ordinary security/product preferences do not automatically establish an exception. ([Timing Adjustable](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html))
- SC 2.2.6 (AAA) requires warning about inactivity duration that could cause data loss unless data persists for more than 20 hours without action. That retention is not a universal A/AA obligation. ([Timeouts](https://www.w3.org/WAI/WCAG22/Understanding/timeouts.html))
- Prefer explainable irreversible actions and recoverable reversible actions as project guidance. Example: “Delete 47 photos permanently” and “Keep photos”, rather than ambiguous Yes/No choices. ([COGA usable](https://www.w3.org/TR/coga-usable/))

See [anxiety and recovery patterns](references/anxiety-patterns.md).

## Sensory control

Review animation, audio, bright/competing content, and transient notifications as possible barriers. Responses vary; avoid claiming that one palette, font, or contrast ratio universally suits a diagnosis. Maintain required contrast and support user preferences. ([COGA usable](https://www.w3.org/TR/coga-usable/))

Prefer static or user-initiated presentation for optional motion. For nonessential interaction-triggered animation, SC 2.3.3 is AAA and permits disabling it. SC 2.2.2 (A) has specific pause/stop/hide conditions for moving and auto-updating information. Reduced-motion CSS alone does not establish conformance. ([Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html), [Pause Stop Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html))

Project example, scoped to a decorative transition:

```css
.card { transition: transform 200ms ease; }
@media (prefers-reduced-motion: reduce) {
  .card { transition: none; }
}
```

Check loading/status information remains available after removing decoration; do not globally hide functional controls. See [sensory review](references/sensory-overload-triggers.md).

## Reading and memory

Use clear structure, understandable instructions, familiar words, and field-specific examples. Support review and reuse of earlier answers where applicable. Do not infer that all dyslexic people see moving letters or that all autistic people need the same layout. ([COGA usable](https://www.w3.org/TR/coga-usable/))

Project example:

```html
<label for="birthdate">Date of birth</label>
<p id="date-hint">For example, 27 March 1990</p>
<input id="birthdate" name="birthdate" aria-describedby="date-hint">
```

Accept only formats the implementation actually supports and explain any constraints. Use `form-a11y` and `accessible-content-writing` for markup/validation details.

## Review and report

Test the complete task with optional motion off, long labels, a break/resume cycle, validation failure, and timeout recovery. Record the participant's feedback and the observed barrier; do not generalize it to a population or manufacture prevalence/conversion estimates. Use [evidence interpretation](references/prevalence-data.md), [common mistakes](references/common-mistakes.md), and [sources](references/sources.yaml).

Use `cognitive-a11y` for technical timing/error patterns, `zoom-reflow` for enlarged/spaced text, and `disability-user-stories` for task acceptance criteria. Report which user and assistive technology tests actually ran.
