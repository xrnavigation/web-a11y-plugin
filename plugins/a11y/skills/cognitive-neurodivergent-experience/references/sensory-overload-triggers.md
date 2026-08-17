# Sensory Overload Triggers in Web Interfaces

## Overview

Sensory overload occurs when the brain receives more sensory input than it can process. For autistic individuals, people with ADHD, vestibular disorders, migraine conditions, and sensory processing disorder, web interfaces can trigger overload through visual, auditory, and motion stimuli that neurotypical users filter unconsciously.

## Trigger Categories

### 1. Motion and Animation

| Trigger | Why It Harms | Who It Affects |
|---------|-------------|----------------|
| Full-screen transitions | Large perceived virtual distance triggers vestibular response | Vestibular disorders, migraine |
| Parallax scrolling | Mismatched direction/speed between layers causes dizziness | Vestibular disorders |
| Auto-advancing carousels | Unpredictable motion hijacks attention; content disappears mid-read | ADHD, autism, cognitive disability |
| Pulsing/bouncing elements | Repetitive motion draws involuntary attention away from task | ADHD, autism |
| Loading spinners (prolonged) | Continuous motion in peripheral vision creates distraction | ADHD, vestibular disorders |
| CSS hover animations | Unexpected motion on interaction; accumulates across many elements | Autism, vestibular disorders |
| Scroll-triggered animations | Motion begins without user intent; cannot be anticipated | Vestibular disorders, anxiety |
| Video backgrounds | Continuous large-area motion; often cannot be paused | All groups |

**Key research:** Craig Grannell documented Apple.com's carousel as problematic due to no pause controls. Greg Tarnoff found Vimeo's Cameo site triggering due to "large areas of motion." Approximately 8 million US adults report chronic balance problems, 2.4 million report chronic dizziness. ([A List Apart](https://alistapart.com/article/designing-safer-web-animation-for-motion-sensitivity/))

**Three factors that drive vestibular symptoms:**
1. Large-scale movement (full-screen transitions)
2. Mismatched direction/speed (parallax effects)
3. Large perceived virtual distances (zooming transitions)

### 2. Audio

| Trigger | Why It Harms | Who It Affects |
|---------|-------------|----------------|
| Auto-playing video/audio | Sudden sound disrupts focus, triggers startle response | ADHD, autism, PTSD |
| Background music | Competes with screen reader output; sensory layering | Screen reader users, autism |
| Notification sounds | Repeated audio alerts create anxiety and sensory accumulation | Anxiety, autism, ADHD |
| Audio with no controls | Cannot stop the stimulus; loss of control escalates distress | All groups |

### 3. Visual Density and Color

| Trigger | Why It Harms | Who It Affects |
|---------|-------------|----------------|
| Pure black (#000) on pure white (#fff) | Words "swirl or blur together" | Dyslexia |
| Bright saturated colors | Visual overwhelm; eye strain escalating to headache | Autism, migraine |
| Flashing/strobing content | Seizure risk (WCAG 2.3.1); migraine trigger | Epilepsy, migraine, vestibular |
| Dense layouts without hierarchy | Cannot determine where to focus; everything demands attention | ADHD, autism, cognitive disability |
| Multiple competing banners/alerts | Simultaneous attention demands exceed processing capacity | All groups |

### 4. Notification and Interruption Overload

| Trigger | Why It Harms | Who It Affects |
|---------|-------------|----------------|
| Cookie banners on arrival | Blocks content before user can orient | Cognitive disability, anxiety |
| Chat widget pop-ups | Unexpected appearance; covers content | Autism, anxiety, ADHD |
| Newsletter prompts | Interrupts task flow; demands decision | Executive function, anxiety |
| Multiple stacked modals | Each requires processing before content access | All groups |
| Toast notifications | Transient information that disappears before processing | Cognitive disability, ADHD |

## Prevention Checklist

For every animation, audio element, or attention-competing element, verify:

- [ ] `prefers-reduced-motion` is respected — all non-essential animation disabled when set
- [ ] No media auto-plays — all audio/video requires explicit user activation
- [ ] User can toggle animations globally via site setting
- [ ] Color palette uses sufficient but not extreme contrast (dark gray on off-white, not pure black on pure white)
- [ ] No more than one attention-competing element visible at a time
- [ ] All notification/interruption elements can be dismissed and do not return for the session
- [ ] No content flashes more than 3 times per second (WCAG 2.3.1)
- [ ] Large-area motion (transitions, parallax) has a static alternative
- [ ] Background audio/music has visible, keyboard-accessible pause/stop controls

## Sources

- UX Mastery — Researching and Designing for Autism: https://uxmastery.com/researching-designing-for-autism/
- Advanced Autism Services — Sensory Overload: https://www.advancedautism.com/post/autism-sensory-overload-and-overstimulation
- A List Apart — Designing Safer Web Animation: https://alistapart.com/article/designing-safer-web-animation-for-motion-sensitivity/
- 216digital — Web Accessibility for Neurodivergent Users: https://216digital.com/web-accessibility-for-neurodivergent-users/
- UX Movement — Bad Practices That Hurt Dyslexic Users: https://uxmovement.com/content/6-surprising-bad-practices-that-hurt-dyslexic-users/
- WebAIM — Seizure and Vestibular Disorders: https://webaim.org/articles/seizure/
