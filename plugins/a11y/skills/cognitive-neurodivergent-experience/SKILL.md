---
name: cognitive-neurodivergent-experience
description: Guides understanding of how cognitive disabilities and neurodivergence affect web interaction — why timeouts cause panic, why unpredictability causes distress, why sensory overload is pain not preference. Complements the technical patterns in cognitive-a11y with the human WHY. Auto-invokes when creating animations, multi-step flows, timed interactions, or notification-heavy interfaces.
allowed-tools: Read, Glob, Grep
---

# Cognitive and Neurodivergent Experience

> "Everything hits me in one go like a blastwave and it can take a moment to process and adjust."
> — Ashlea McKay, autistic UX designer ([UX Mastery](https://uxmastery.com/researching-designing-for-autism/))

> "Users' cognitive skills may diminish as they get tired, but when users know that their data won't be lost, they can recover from mental fatigue and return to successfully complete the task."
> — [W3C COGA Data Loss Pattern](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p09-data-loss/)

This skill is about people. It explains WHY cognitive and neurodivergent accessibility patterns exist — the human experiences that make them necessary. For the technical HOW, see the cross-references in Section 8.

---

## 1. This Is About People

Neurodivergence and cognitive disability are not edge cases. They are a substantial portion of every user base.

| Condition | Prevalence | Source |
|-----------|-----------|--------|
| Neurodivergent (any) | 15-20% of population | [WCAG.com](https://www.wcag.com/blog/digital-accessibility-and-neurodiversity/) |
| Anxiety disorders | ~19% of US adults | NIMH |
| Cognitive disability (any) | ~12% of US population | CDC |
| Dyslexia | 6-8% of children; persists into adulthood | [IDA](https://dyslexiaida.org/) |
| ADHD | ~5% of adults worldwide | Clinical estimates |
| Dyscalculia | 3-6% of population | [Cleveland Clinic](https://my.clevelandclinic.org/health/diseases/23949-dyscalculia) |
| Autism spectrum | ~2.8% of children (CDC 2024) | CDC |
| Vestibular disorders | 8 million US adults (chronic balance) | [vestibular.org via A List Apart](https://alistapart.com/article/designing-safer-web-animation-for-motion-sensitivity/) |

These conditions overlap. A person with ADHD frequently also has anxiety. An autistic person may also have dyslexia. The combined affected population is not a niche — it is a significant fraction of humanity.

**For agents:** When someone says "that's an edge case," these numbers are your response. One in five users is neurodivergent. One in five has an anxiety disorder. Designing only for neurotypical cognition excludes millions.

See: [references/prevalence-data.md](references/prevalence-data.md)

---

## 2. Sensory Overload: Pain, Not Preference

Sensory overload is not mild annoyance. Autistic adults describe it as "physically painful" or "making my skin crawl." When overwhelmed, the result is meltdown (loss of control) or shutdown (complete withdrawal). Many cannot articulate thoughts while experiencing it. ([Advanced Autism Services](https://www.advancedautism.com/post/autism-sensory-overload-and-overstimulation))

### What Triggers It in Web Interfaces

- **Auto-playing media:** Sudden sound disrupts focus (ADHD), triggers sensory overload (autism), causes dizziness/vertigo/nausea in vestibular disorders. Screen readers mixed with auto-playing audio create chaotic layered noise. ([216digital](https://216digital.com/web-accessibility-for-neurodivergent-users/))
- **Animations and motion:** Full-screen transitions, parallax scrolling, carousels, pulsing buttons. If everything moves, users cannot determine where to focus. For vestibular disorder users, large-scale motion causes physical symptoms that persist after the animation ends. ([A List Apart](https://alistapart.com/article/designing-safer-web-animation-for-motion-sensitivity/))
- **Busy layouts:** Dense information without visual hierarchy. Bright banners competing for attention. Multiple elements demanding attention simultaneously.
- **High contrast extremes:** Pure black on pure white causes words to "swirl or blur together" for dyslexic users. Bright saturated colors overwhelm autistic users. ([UX Movement](https://uxmovement.com/content/6-surprising-bad-practices-that-hurt-dyslexic-users/))
- **Notification spam:** Pop-ups, cookie banners, chat widgets, newsletter prompts, and discount offers all arriving simultaneously.

### Who Is Affected

Autistic individuals (hypersensitivity), ADHD (motion hijacks attention), vestibular disorders (physical symptoms from animation), migraine conditions (visual triggers), sensory processing disorder.

### What to Build Instead

- Respect `prefers-reduced-motion`. When enabled, disable or reduce ALL non-essential animation.
- Never auto-play media. Provide explicit play controls.
- Offer user controls to toggle animation globally.
- Use calm color palettes with sufficient but not extreme contrast.
- Limit simultaneous attention-competing elements.

See: [references/sensory-overload-triggers.md](references/sensory-overload-triggers.md)

---

## 3. Executive Function: When Interfaces Become Walls

Executive function governs planning, focus, task-switching, working memory, and impulse control. For people with ADHD, autism, traumatic brain injuries, or intellectual disabilities, a complex multi-step form is not "this is long" — it is "I cannot hold all of this in my head at once." Each field drains a finite cognitive resource. When capacity is exceeded, the result is abandonment, errors, or emotional distress. ([NWS Digital](https://www.nwsdigital.com/Blog/Why-ADHD-Accessibility-Matters-in-Website-Development), [NN/g](https://www.nngroup.com/articles/4-principles-reduce-cognitive-load/))

### Specific Barriers

- **Long single-page forms:** Everything visible at once overwhelms working memory. Users cannot tell how much remains.
- **No progress indicators:** "Am I on step 2 of 3 or step 2 of 12?" The unknown creates anxiety about remaining effort.
- **Redundant data entry:** Asking for the same information twice wastes limited cognitive resources.
- **Complex field formats:** "Enter date as MM/DD/YYYY" — users with dyscalculia (3-6% of population) struggle with number formatting and sequencing. ([W3C COGA Dyscalculia Gap Analysis](https://www.w3.org/WAI/GL/task-forces/coga/wiki/Gap_Analysis/Dyscalculia))
- **Decision overload:** Dropdowns with 50+ items. Configuration pages with dozens of toggles. Too many options without guidance.
- **No save-and-resume:** Users who need breaks cannot return.

### What to Build Instead

- Break processes into clearly labeled steps with progress indicators ("Step 3 of 5 — Payment details").
- Show only what is needed at each step (progressive disclosure).
- Auto-save continuously so users can take breaks.
- Pre-fill where possible; never ask for the same data twice.
- Provide clear, specific labels ("Your home address" not "Address 1").
- Limit choices per screen. Provide defaults for common selections.

---

## 4. Time Pressure and Anxiety: Countdowns as Panic

For users with cognitive disabilities, ADHD, dyslexia, or anxiety disorders, a countdown timer creates panic. The anxiety of the countdown itself degrades their ability to complete the task — the more anxious they become, the slower they work, the less time they have. Many timeout notices expire before users finish reading them. ([TPGi](https://www.tpgi.com/a-web-of-anxiety-accessibility-for-people-with-anxiety-and-panic-disorders-part-2/))

### What Triggers Panic

- **Visible countdown timers:** The ticking clock creates urgency that degrades performance. "Only 3 left!" and "Offer expires in 04:32" exploit this deliberately.
- **Session timeouts on forms:** Users who need more time lose all entered data.
- **2FA timeouts:** Short windows to enter codes while context-switching between devices.
- **Auto-logout:** Banking and government sites that log users out mid-task.

### The Data Loss Dimension

For users with memory impairments, traumatic brain injuries, or cognitive fatigue, lost form data may be **unrecoverable** — they cannot remember what they typed. The W3C COGA personas include Alison (mild cognitive impairment), George (Down syndrome), Maria (memory loss), and Kwame (traumatic brain injury survivor). Data loss is not inconvenience for these users; it is access denial. ([W3C Data Loss Pattern](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p09-data-loss/))

### Irreversible Actions: The Freeze Response

Any action that might be irreversible triggers disproportionate distress for anxious users. "Delete this account?" with only Yes/No — and no indication of what "delete" means — creates a freeze response. The vagueness itself is the problem. ([Neurodivergent Insights](https://neurodivergentinsights.com/neurodivergent-anxiety/), [NN/g](https://www.nngroup.com/articles/confirmation-dialog/))

Generic "Are you sure?" dialogs provide no protection — users develop automatic "yes" responses. Specific consequences ("This will permanently delete 47 photos and cannot be undone") with specific button labels ("Delete 47 photos" / "Keep photos") are what actually help.

### What to Build Instead

- Eliminate timeouts whenever feasible. When necessary, allow extension (up to 10x per WCAG 2.1 SC 2.2.1).
- Auto-save form data continuously so nothing is lost.
- Preserve session data for at least 20 hours during inactive sessions.
- Provide undo for all reversible actions. Undo is always better than "Are you sure?"
- For irreversible actions, state exactly what will happen in specific terms.
- Use specific button labels, not "Yes" / "No."
- Never use urgency or scarcity messaging to pressure decisions.

See: [references/anxiety-patterns.md](references/anxiety-patterns.md)

---

## 5. Predictability as Safety

Autistic users rely heavily on predictable patterns. When a website behaves inconsistently — navigation that moves, carousels that auto-advance, content that shifts — the mental model the user has carefully constructed is violated. Rebuilding it costs significant cognitive energy. For users with anxiety disorders, unpredictable interfaces create constant vigilance: "What will happen when I click this? Will I lose my work?" ([Today Design](https://today.design/news/neurodiversity-and-the-digital-divide-how-our-neurological-differences-shape-the-way-we-experience-the-web/), [TetraLogical](https://tetralogical.com/blog/2026/03/10/designing-for-people-with-anxiety/))

### Patterns That Cause Distress

- **Auto-advancing carousels:** Content disappears while being read.
- **Pop-ups without user action:** Chat widgets, newsletter prompts, cookie banners covering content.
- **Inconsistent interaction patterns:** A checkbox that submits immediately on one page, requires a save button on another.
- **Unexpected redirects:** Internal-looking links opening external sites in new tabs.
- **Layout shift:** Elements moving as the page loads, especially if the user has started reading or clicking.

### What to Build Instead

- Consistent layouts across all pages.
- Navigation in the same position, working the same way, throughout.
- Interactive elements that behave identically everywhere they appear.
- No auto-advancing content. User controls for all transitions.
- Clear visual cues about what is interactive and what will happen.

**The principle:** Consistency matters more than creativity for these users. A predictable interface is a safe interface. An unpredictable one is hostile.

---

## 6. Memory and Cognitive Fatigue

Cognitive fatigue is a real physiological state — not laziness. The key insight from W3C COGA: fatigue is temporary and recoverable — **if the interface allows it**. If it does not (session timeouts, no save state, forced single-session completion), the user is locked out by their neurology. ([W3C COGA Data Loss Pattern](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p09-data-loss/))

### Specific Barriers

- **No save-and-resume:** Users who need breaks lose their progress.
- **Session timeouts that destroy state:** Users may not remember what they entered.
- **Redundant information requests:** Same data across multiple pages wastes limited memory.
- **Password hostility:** Complex password rules without password manager support. Blocking paste into password fields.
- **Multi-tab workflows:** "Open this link in a new tab to verify" — users lose track of which tab contains which step.

### What to Build Instead

- Auto-save all user input continuously.
- Preserve session data for extended periods (at least 20 hours per W3C).
- Never require the same information twice.
- Support password managers; never block paste into password fields.
- Keep workflows within a single page/tab where possible.
- Provide clear "you are here" indicators at all times.
- Allow users to review what they have already entered.

---

## 7. Reading and Language

### Dyslexia: When Text Is the Barrier

For dyslexic users, reading is an active, exhausting process. Letters "jump around." Users re-read sentences multiple times. The mental health impact is documented: higher risk of depression and anxiety from cumulative frustration. ([CNN](https://www.cnn.com/2016/03/05/health/dyslexia-simulation))

Six documented typographic barriers ([UX Movement](https://uxmovement.com/content/6-surprising-bad-practices-that-hurt-dyslexic-users/)):

1. **Justified text** — creates "rivers of whitespace" that cause readers to lose their place. Use left-aligned.
2. **Pure black on pure white** — words swirl/blur. Use off-white backgrounds with dark gray text.
3. **Long unbroken paragraphs** — readers lose their place. Break into short paragraphs, one idea each.
4. **Serif fonts** — letter hooks cause letters to "run together." Use sans-serif.
5. **Italicized text** — jagged angles make letters difficult to read. Use bold for emphasis.
6. **Double spacing after periods** — creates visual rivers. Use single spacing.

### Dyscalculia: Numbers as Barriers

Affects 3-6% of the population. Users struggle with number formatting, sequencing, and recognizing which of two numbers is larger. Forms requiring specific date formats, phone number groupings, or financial figures create real barriers. ([Cleveland Clinic](https://my.clevelandclinic.org/health/diseases/23949-dyscalculia), [W3C COGA Dyscalculia Gap Analysis](https://www.w3.org/WAI/GL/task-forces/coga/wiki/Gap_Analysis/Dyscalculia))

### Language Complexity

Jargon, acronyms, and complex sentences are barriers for users with cognitive disabilities, intellectual disabilities, or non-native speakers. WCAG 3.1.5 recommends content at lower secondary reading level. ([W3C COGA Usable](https://www.w3.org/TR/coga-usable/), [Siteimprove](https://www.siteimprove.com/blog/readability-plain-language-wcag/))

### What to Build Instead

- Left-aligned text, never justified.
- Sans-serif fonts at minimum 16px body text.
- Sufficient but not extreme contrast (dark gray on off-white).
- Short paragraphs with clear headings and visual breaks.
- Bold for emphasis, never italics for body text.
- Plain language: short sentences, common words, defined acronyms.
- Flexible input formats (accept "March 27 2026" not just "03/27/2026").
- Examples next to form fields showing expected format.

---

## 8. Cross-References

This skill explains the **human WHY**. These companion skills provide the **technical HOW**:

- **`cognitive-a11y`** — technical patterns for cognitive accessibility: timing controls, error prevention, simplified layouts, reading level, WCAG SC coverage
- **`css-a11y`** — `prefers-reduced-motion`, `prefers-contrast`, `prefers-color-scheme`, responsive text sizing, focus indicators
- **`form-a11y`** — label association, error messaging markup, fieldset/legend grouping, autocomplete attributes, validation patterns
- **`hostile-pattern-detection`** — identifies carousels, infinite scroll, auto-play, dark patterns, and overlays that disproportionately harm the users described in this skill
- **`aria-decision-framework`** — native HTML first; when ARIA is needed, what behavior you must implement

### The W3C COGA Framework

The W3C Cognitive and Learning Disabilities Accessibility Task Force provides supplemental guidance beyond WCAG covering ADHD, autism, dyslexia, dyscalculia, mild cognitive impairment, Down syndrome, aphasia, and dementia. Core design objectives: adaptability, distinguishability, timing, navigation, readability, predictability, error prevention. ([W3C COGA Usable](https://www.w3.org/TR/coga-usable/), [W3C Cognitive Accessibility](https://www.w3.org/WAI/cognitive/))

### The TetraLogical Anxiety Framework (2026)

Seven principles for designing for anxiety: give people time, limit urgency, keep interactions predictable, provide clear progress, be transparent, enable review, accessible wayfinding. The underlying principle: "Ensure people are in control." ([TetraLogical](https://tetralogical.com/blog/2026/03/10/designing-for-people-with-anxiety/))

---

## Sources

All claims in this skill are cited inline. For the complete source list with URLs and retrieval dates, see: [references/sources.yaml](references/sources.yaml)
