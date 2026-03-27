# Anxiety Patterns in Web Interfaces

## Overview

Anxiety disorders affect approximately 19% of US adults (NIMH). Many neurodivergent people experience anxiety as a baseline state because their nervous systems are wired for vigilance. Web interfaces that create uncertainty, time pressure, or fear of irreversible consequences trigger disproportionate distress in these users — not because they are "overreacting," but because their neurological response to perceived threat is stronger and harder to regulate.

## Pattern 1: Time Pressure

### The Mechanism

A countdown timer creates a feedback loop: time pressure increases anxiety, anxiety degrades performance, degraded performance means the user needs more time, and the shrinking timer increases anxiety further. This cycle is not metaphorical — it is a documented cognitive phenomenon. ([TPGi](https://www.tpgi.com/a-web-of-anxiety-accessibility-for-people-with-anxiety-and-panic-disorders-part-2/))

### Hostile Examples

| Pattern | What the User Experiences | WCAG Reference |
|---------|--------------------------|----------------|
| Visible countdown on form | Panic; performance degradation; abandonment | SC 2.2.1 (Timing Adjustable) |
| "Offer expires in 04:32" | Manufactured urgency; pressured decision-making | Dark pattern |
| "Only 3 left!" | Scarcity anxiety; fear of missing out overrides careful evaluation | Dark pattern |
| Session timeout without warning | Data loss; unrecoverable if user has memory impairment | SC 2.2.6 (Timeouts) |
| 2FA code expiry (30-60 seconds) | Context-switching anxiety between devices under time pressure | SC 2.2.1 |
| Timed assessments | Speed measured instead of ability; excludes cognitive disabilities | SC 2.2.1 |

### Safe Alternatives

- **Eliminate timeouts** whenever feasible.
- **Allow extension** up to 10x the original time (WCAG 2.1 SC 2.2.1).
- **Hide visible countdowns** — offer the option to disable timer display.
- **Auto-save continuously** so nothing is lost regardless of timeout.
- **Preserve data for 20+ hours** during inactive sessions (W3C COGA recommendation).
- **Use reassuring language:** "Take your time" rather than "Hurry!"
- **Request sensitive data last** — credit cards, SSNs only at the final step.

## Pattern 2: Irreversible Actions

### The Mechanism

Loss aversion research shows that when users perceive a misstep could lead to permanent loss, anxiety increases, leading to hesitation, mistrust, or abandonment. For neurodivergent users with heightened threat detection, "Delete this account?" with only Yes/No triggers a freeze response — the user does not know what "delete" actually means, what data will be lost, or whether recovery is possible. The vagueness is the problem. ([NN/g](https://www.nngroup.com/articles/confirmation-dialog/), [Neurodivergent Insights](https://neurodivergentinsights.com/neurodivergent-anxiety/))

### Hostile Examples

| Pattern | Why It Causes Anxiety |
|---------|----------------------|
| "Are you sure?" (generic) | No information about consequences; trains automatic "yes" response |
| "Delete" with no scope | User doesn't know: one item? All items? Account? Data? |
| "Yes" / "No" buttons | Forces re-reading the question to map which button does what |
| "Your settings have been updated" | Which settings? What changed? Can I revert? |
| No undo capability | Every action is permanent; user must be perfect |
| "This action cannot be undone" without specifics | Threat without information; maximum anxiety, minimum protection |

### Safe Alternatives

- **Provide undo** for all reversible actions. Undo is always better than confirmation dialogs.
- **State exact consequences:** "This will permanently delete 47 photos and cannot be undone."
- **Use specific button labels:** "Delete 47 photos" / "Keep photos" — never "Yes" / "No."
- **Add appropriate friction** for high-consequence actions (type project name to confirm).
- **Offer preview/review** before submission.
- **Never use urgency or scarcity messaging** to pressure decisions.

## Pattern 3: Unpredictable Interactions

### The Mechanism

For anxious users, every interaction with an unfamiliar interface involves a risk assessment: "What will happen when I click this? Will I lose my work? Can I go back?" Predictable interfaces reduce this cognitive burden because the user can rely on learned patterns. Unpredictable interfaces force continuous vigilance — an exhausting state that depletes cognitive resources and eventually leads to abandonment. ([TetraLogical](https://tetralogical.com/blog/2026/03/10/designing-for-people-with-anxiety/))

### Hostile Examples

| Pattern | Why It Causes Anxiety |
|---------|----------------------|
| Links that open new tabs without warning | User didn't consent to leaving context |
| Form submission with no confirmation | User doesn't know if it worked or what was submitted |
| Controls that behave differently on different pages | Learned patterns violated; must re-evaluate every interaction |
| Content that appears/disappears unpredictably | User cannot trust the stability of what they see |
| State changes with no feedback | Did anything happen? Should I click again? |

### Safe Alternatives

- **Consistent behavior** across all pages.
- **Clear feedback** for every user action (submitted, saved, failed — with specifics).
- **Warn before leaving context** (external links, new tabs).
- **Preview before commit** for any consequential action.
- **Breadcrumbs and navigation landmarks** so users always know where they are.

## The TetraLogical Framework (2026)

Seven principles for designing for people with anxiety ([TetraLogical](https://tetralogical.com/blog/2026/03/10/designing-for-people-with-anxiety/)):

1. **Give people time** — allow disabling/adjusting/extending timers; hide countdowns; use reassuring language.
2. **Limit urgency** — remove scarcity messaging; avoid manipulative pressure; create space for thoughtful decisions.
3. **Keep interactions predictable** — use recognizable UI conventions; make interactive elements visually distinct.
4. **Provide clear progress** — multi-step progress indicators; current position and total steps visible.
5. **Be transparent** — explain why information is requested; provide instructions before forms; justify data collection.
6. **Enable review** — preview before submission; confirmation before finalizing.
7. **Accessible wayfinding** — breadcrumbs, clear navigation, search on complex sites.

The underlying principle: "Ensure people are in control. People should be able to access and interact with content in their preferred way."

## Sources

- TPGi — A Web of Anxiety, Part 2: https://www.tpgi.com/a-web-of-anxiety-accessibility-for-people-with-anxiety-and-panic-disorders-part-2/
- W3C COGA — Avoid Data Loss Pattern: https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p09-data-loss/
- NN/g — Confirmation Dialogs: https://www.nngroup.com/articles/confirmation-dialog/
- Neurodivergent Insights — Anxiety: https://neurodivergentinsights.com/neurodivergent-anxiety/
- TetraLogical — Designing for People with Anxiety: https://tetralogical.com/blog/2026/03/10/designing-for-people-with-anxiety/
- NIMH — Anxiety Disorders Statistics: https://www.nimh.nih.gov/health/statistics/any-anxiety-disorder
