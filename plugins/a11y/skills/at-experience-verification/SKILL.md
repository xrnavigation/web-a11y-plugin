---
name: at-experience-verification
description: Helps verify accessibility by describing what assistive technology users actually experience — what screen readers announce, what keyboard navigation feels like, what broken focus sounds like. Auto-invokes when writing forms, headings, ARIA, or interactive components. User-invocable for full AT experience walkthrough of a component.
argument-hint: "[component-or-page]"
allowed-tools: Read, Glob, Grep
---

# AT Experience Verification

> "Will it work for me?" -- the question a blind screen reader user asks before every digital task, approaching it with "trepidation, caution, and a fair degree of uncertainty."
> -- [UsableNet blog](https://blog.usablenet.com/a-screen-reader-users-honest-take)

> "I was constantly trying to catch up, not because I couldn't understand the material, but because I couldn't *get to it*."
> -- [UsableNet - Growing Up](https://blog.usablenet.com/growing-up-with-accessibility-gaps-a-screen-reader-user-reflects)

This skill is not about passing audits. It is about understanding what real people experience when they use your code with assistive technology. Every heading you skip, every label you omit, every focus trap you create has a human on the other end who hears silence, gets lost, or gives up.

---

## 1. What This Skill Is For

When you write a component, you see pixels. A screen reader user hears announcements. A keyboard user feels tab stops. A low-vision user sees a narrow, magnified viewport. This skill helps you verify the *experience* your code creates -- not just whether it passes automated checks.

**Use this skill to:**
- Walk through what a screen reader will actually announce for your component
- Check whether keyboard navigation works and feels logical
- Verify that focus management doesn't strand users
- Confirm that zoom and low-contrast scenarios don't break the experience

**When this skill auto-invokes:** Writing forms, headings, ARIA attributes, interactive components (buttons, modals, tabs, menus, dialogs).

---

## 2. Screen Reader Announcements

Screen readers are literal. They announce exactly what the markup says. If the markup lies, the announcement lies.

### What Correct Sounds Like

| Element | NVDA Announces |
|---|---|
| `<h2>Products</h2>` | "heading level 2, Products" |
| `<a href="/pricing">View pricing</a>` | "link, View pricing" |
| `<button>Submit</button>` | "button, Submit" |
| `<img alt="Team at whiteboard">` | "graphic, Team at whiteboard" |
| `<img alt="">` (decorative) | *(silence -- correctly skipped)* |
| `<input>` with `<label>Email</label>` | "Email, edit text" |
| `<input type="checkbox">` with label | "Accept terms, checkbox, not checked" |
| `<nav>` landmark | "navigation landmark" |
| `role="alert"` content | *(interrupts current speech to read the alert)* |

JAWS and VoiceOver follow similar patterns with slight wording differences. The key: every screen reader announces what the markup provides. ([Deque NVDA Shortcuts](https://dequeuniversity.com/screenreaders/nvda-keyboard-shortcuts); [CSS-Tricks SR Comparison](https://css-tricks.com/comparing-jaws-nvda-and-voiceover/))

### What Broken Sounds Like

| Broken Pattern | User Hears | User Experience |
|---|---|---|
| No headings on page | "no next heading" | Stranded. Must listen to entire page linearly. A 2-min visual scan becomes 20-30 min. ([Yale Headings](https://usability.yale.edu/web-accessibility/articles/headings)) |
| Bold text styled as heading | *(nothing -- it's just bold)* | User skips past it. Visual hierarchy is invisible. |
| `<input>` with no label | "edit" or "edit, blank" | User guesses what to type. May submit wrong data or abandon form. ([W3C Form Labels](https://www.w3.org/WAI/tutorials/forms/labels/)) |
| Placeholder as only label | "edit, Enter your email" | Label vanishes on focus. User forgets what field wants. |
| `<img>` with no alt | "graphic, IMG_20240315_crop2.jpg" | Noise. No information. ([WebAIM Alt Text](https://webaim.org/techniques/alttext/)) |
| Image link with no alt | "link, graphic" | User knows something is clickable but has zero idea where it goes. |
| 12 "Click here" links | Links list: "click here, click here, click here..." | Impossible to distinguish destinations. ([WebAIM Survey #10](https://webaim.org/projects/screenreadersurvey10/)) |

**71.6% of screen reader users navigate by headings.** Missing headings is an instant-leave trigger -- users close the page immediately. ([WebAIM Survey #10](https://webaim.org/projects/screenreadersurvey10/))

---

## 3. Missing or Wrong ARIA

ARIA makes promises. When you add `role="button"` to a `<div>`, the screen reader announces "button." The user expects button behavior: Enter or Space to activate. If those handlers don't exist, you have lied to the user.

> "ARIA creates promises to AT users. Broken ARIA is worse than no ARIA -- it actively lies about what the interface will do."
> -- [APG Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)

### Specific Broken Scenarios

| Code | User Hears | What Actually Happens |
|---|---|---|
| `<div role="button" onclick="...">Send</div>` (no keyboard handler) | "Send, button" | Enter/Space does nothing. Only mouse works. The interface lied. ([MDN ARIA button](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role)) |
| `<a role="button">` without `href` | "Send, button" | Not focusable by Tab. User cannot reach it at all. |
| `<button aria-label="Submit application form">` displaying "Send" | "Submit application form, button" | Sighted helper says "click Send" -- user can't find it. Violates WCAG 2.5.3 Label in Name. ([WCAG 2.5.3](https://www.w3.org/WAI/WCAG21/Understanding/label-in-name.html)) |
| `<div role="navigation">` wrapping body text | "navigation landmark" | User jumps to "navigation" expecting links. Finds paragraphs. |

### Why No ARIA Is Better Than Wrong ARIA

No ARIA on a `<div>`: the screen reader says nothing special. The user knows it's text or a container. Wrong ARIA on a `<div>`: the screen reader announces a specific role, the user forms expectations, and those expectations are violated. ([BOIA ARIA Mistakes](https://www.boia.org/blog/4-mistakes-to-avoid-when-using-aria-roles))

**Fix:** Use native HTML elements. A `<button>` already has focus, Enter, Space, and the correct role. See the `aria-decision-framework` skill for the full decision tree.

---

## 4. Focus Management Experience

### Modal Opens, Focus Stays Behind

The user clicks "Settings." A modal opens visually, but focus stays on the trigger button behind the overlay. The user presses Tab and moves through the background page -- completely unaware a modal is open. They interact with elements they cannot see, obscured behind the backdrop.

### Focus Escapes the Modal

The modal opens and focus moves inside it. But there is no focus trap. Tab past the last element and focus moves into the obscured background. The user is navigating behind a visual wall.

### Focus Disappears on Close

The modal closes. Focus does not return to the trigger. It jumps to `<body>` -- the top of the page. The user must Tab through the entire page to get back to where they were.

> "Walking through a door into a room but your hands are still in the previous room. You can hear the new room but can't interact with it."

> "Opening the search bar and then pressing Tab causes focus to move completely off-screen. The user is essentially 'lost' with no visual indication of where they are."
> -- GitLab accessibility audit ([Focus Containment - DEV](https://dev.to/jantimon/focus-containment-the-broken-state-of-keyboard-navigation-45l1))

### Keyboard Traps

The user tabs into a custom date picker, video player, or rich text editor. Tab does nothing. Shift+Tab does nothing. Escape does nothing. They are stuck. The only escape is refreshing the page -- losing all form progress.

> "You tab into a custom modal or dropdown, and suddenly you're stuck. Focus won't move. The Tab key feels broken."
> -- ([216digital Keyboard Traps](https://216digital.com/lost-in-focus-blame-keyboard-traps/))

Specific trap patterns:
- Custom date pickers intercept Tab and arrow keys without exit routes
- Media players swallow every keydown -- Space, arrows, Tab all consumed
- `preventDefault()` on Tab in JavaScript links creates instant traps
- `onBlur` validation that forces focus back to the field on failure

([BOIA Keyboard Traps](https://www.boia.org/blog/why-keyboard-traps-are-one-of-the-most-frustrating-accessibility-issues); [A11Y Collective Keyboard Trap](https://www.a11y-collective.com/blog/keyboard-trap/))

### Invisible Focus Indicators

CSS `outline: none` on all focusable elements. The keyboard user presses Tab. Nothing visually changes. They know something is focused (screen reader may announce it) but cannot see where.

> Pressing Tab and seeing nothing change. You know you moved somewhere, but you don't know where. Navigating a room in the dark.

For sighted keyboard users (motor impairments -- can see the screen, can't use a mouse), this is devastating. They see the entire page but cannot locate the one element that will respond to Enter. ([A11Y Project - Never Remove Outlines](https://www.a11yproject.com/posts/never-remove-css-outlines/))

### What Correct Focus Feels Like

- Focus moves to the modal heading or first interactive element on open
- Tab cycles within the modal only (focus trap)
- Escape closes the modal and returns focus to the trigger button
- Every focusable element has a visible focus indicator (`:focus-visible` with at least 2px, sufficient contrast)
- Tab order follows logical reading order
- The user always knows where they are

See the `focus-management` skill for implementation patterns.

---

## 5. Low Vision Experience

### Zoom at 200-400%: What Breaks

Low-vision users zoom browsers to 200-400% to read text. When layouts use fixed widths or absolute positioning:

- **Horizontal scrolling** -- the user must scroll right to finish each line, then left to start the next. Reading effort increases 40-100x compared to reflowing text. ([W3C Low Vision TF](https://www.w3.org/WAI/GL/low-vision-a11y-tf/wiki/Resize_content))
- **Overlapping text** -- fixed-position elements stack on content, making both unreadable
- **Content clipped by `overflow: hidden`** -- text disappears off the edge of its container
- **Broken navigation** -- menus designed for specific viewport widths collapse into unusable states

### Low Contrast: The Most Common Violation

**83.9%** of the top million homepages have low-contrast text, averaging **31.6 instances per page**. ([WebAIM Million 2022](https://webaim.org/projects/million/))

> "Straining our eyes, making us all feel older and a little less capable."
> -- [NNGroup](https://www.nngroup.com/articles/low-contrast/)

> "Users blame themselves when they are unable to accomplish tasks on a modern-looking website, because they cannot see the text."
> -- [NNGroup](https://www.nngroup.com/articles/low-contrast/)

Users with low vision, color blindness, or anyone in bright ambient light cannot read gray-on-white text. They don't realize the site is broken -- they think something is wrong with them.

**Placeholder text** is a particular offender: default placeholder color is light gray, typically failing the 4.5:1 contrast ratio. And since placeholders disappear on focus, users with memory difficulties lose the label entirely. ([Deque Placeholder](https://www.deque.com/blog/accessible-forms-the-problem-with-placeholders/))

See the `css-a11y` skill for contrast and zoom-safe layout patterns.

---

## 6. First-Person Voices

These are quotes from real assistive technology users. They are the reason accessibility matters.

### The constant question

> "Will it work for me?" -- asked before every digital task, with "trepidation, caution, and a fair degree of uncertainty."
> -- Blind screen reader user ([UsableNet](https://blog.usablenet.com/a-screen-reader-users-honest-take))

### Giving up on travel booking

> "Just a few weeks ago, I was trying to purchase plane tickets and reserve a hotel room and had an experience so poor in terms of accessibility that I had to give up and ask a sighted user for assistance."
> -- ([UsableNet](https://blog.usablenet.com/a-screen-reader-users-honest-take))

### Half of mobile apps are unusable

> "About half of the apps on my phone right now do not work for me. I keep them around in the hope that software updates will bring accessibility improvements."
> -- ([UsableNet](https://blog.usablenet.com/a-screen-reader-users-honest-take))

### Social media isolation

> "Most images had no descriptions. Links weren't labeled. Video players didn't work with my screen reader."
> "I felt isolated. Everyone else was reacting to something I couldn't access."
> -- ([UsableNet - Growing Up](https://blog.usablenet.com/growing-up-with-accessibility-gaps-a-screen-reader-user-reflects))

### Fighting to reach educational content

> "I was constantly trying to catch up, not because I couldn't understand the material, but because I couldn't *get to it*."
> -- ([UsableNet - Growing Up](https://blog.usablenet.com/growing-up-with-accessibility-gaps-a-screen-reader-user-reflects))

### The asymmetry of effort

> "I have spent years learning how to operate my screen reader...just to have to forget all that."
> -- ([Allyant](https://allyant.com/blog/my-experience-of-navigating-the-web-as-a-blind-user/))

### Overlays making things worse

> "Every time I hear the notification that this site is adjusted to my screen reader, I know my blocker is not working properly, and I am in for a hellish experience."
> -- ([Overlay Fact Sheet](https://overlayfactsheet.com/en/))

### The restaurant QR code

A screen reader user at a resort: the QR code bill-pay let them hear the itemized check, but none of the action buttons worked with the screen reader. They could not charge the meal to their room or enter card details. The information was accessible but the actions were not. ([UsableNet - Summer 2025](https://blog.usablenet.com/summer-2025-digital-accessibility-a-screen-readers-review))

---

## 7. Cross-References to Technical Skills

When you identify an experience problem, these skills have the fixes:

| Problem | Skill |
|---|---|
| Wrong or redundant ARIA roles | `aria-decision-framework` |
| Missing alt text, bad alt text | `alt-text-quality` |
| Broken focus, keyboard traps, missing indicators | `focus-management` |
| Unlabeled forms, bad error messages | `form-a11y` |
| Broken modals/dialogs | `a11y-dialog` |
| Bad tab/tablist patterns | `a11y-tabs` |
| Broken combobox/autocomplete | `a11y-combobox` |
| Missing live region announcements | `live-regions` |
| Contrast, zoom, motion problems | `css-a11y` |
| Cognitive load, plain language, predictability | `cognitive-a11y` |
| Hostile design patterns (carousels, infinite scroll, overlays) | `overlay-resistance` |

For detailed reference material:
- [references/screen-reader-output-catalog.md](references/screen-reader-output-catalog.md) -- complete SR announcement reference
- [references/good-vs-bad-examples.md](references/good-vs-bad-examples.md) -- side-by-side comparisons
- [references/keyboard-experience.md](references/keyboard-experience.md) -- keyboard navigation patterns
- [references/low-vision-experience.md](references/low-vision-experience.md) -- zoom and contrast details
- [references/sources.yaml](references/sources.yaml) -- provenance for all citations
