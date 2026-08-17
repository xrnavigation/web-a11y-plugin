# Good vs Bad: AT Experience Side-by-Side
## Contents

- [Headings](#headings)
- [Form Fields](#form-fields)
- [Images](#images)
- [Buttons and Interactive Elements](#buttons-and-interactive-elements)
- [Links](#links)
- [Modals and Dialogs](#modals-and-dialogs)
- [Focus Indicators](#focus-indicators)
- [Error Messages](#error-messages)


Every example shows what the user actually hears or experiences, not what the code intends.

## Headings

| Scenario | Screen Reader Output | User Experience |
|---|---|---|
| No headings | "no next heading" | Must listen to entire page linearly. 20-30 min for what takes 2 min visually. |
| Bold text styled to look like heading | *(no announcement -- just bold text)* | User skips past it. Visual hierarchy invisible to them. |
| Proper `<h2>` | "heading level 2, Section Title" | User jumps directly to relevant section in seconds. |
| Skipped levels (`<h1>` then `<h4>`) | "heading level 4, Subsection" | User wonders what happened to levels 2 and 3. Disorienting. |

(Sources: [Yale Headings](https://usability.yale.edu/web-accessibility/articles/headings), [WebAIM Headings](https://webaim.org/techniques/headings/))

## Form Fields

| Scenario | Screen Reader Output | User Experience |
|---|---|---|
| No label | "edit" or "edit, blank" | User guesses what to type. May submit wrong data. |
| Placeholder only | "edit, Enter your email" (disappears on focus) | Label gone after typing starts. User forgets what field wants. |
| `aria-label` mismatches visible label | Hears one name, sighted helper sees another | Communication breakdown between user and helper. |
| Proper `<label for="email">` | "Email address, edit text, required" | User knows exactly what to enter. |
| Grouped with `<fieldset>/<legend>` | "Shipping address, Street, edit text" | User understands context of the group. |

(Sources: [W3C Form Labels](https://www.w3.org/WAI/tutorials/forms/labels/), [BeAccessible Forms](https://beaccessible.com/post/forms-accessibility/))

## Images

| Scenario | Screen Reader Output | User Experience |
|---|---|---|
| No alt attribute | "graphic, IMG_20240315_crop2.jpg" | Noise. No information conveyed. |
| Stock photo no alt | "graphic, shutterstock_123456789.jpg" | Even more noise. |
| `alt=""` on informative image | *(silence)* | Information permanently lost. |
| `alt=""` on decorative image | *(silence)* | Correct -- no noise from decoration. |
| AI-generated alt | "graphic, A picture containing outdoor, person, working, raft" | Technically describes pixels, communicates no meaning. |
| Good alt text | "graphic, Team members collaborating at a whiteboard" | User understands image purpose. |
| Image link with no alt | "link, graphic" | Clickable but destination unknown. |
| Image link with alt | "link, graphic, View our product catalog" | User knows where the link goes. |

(Sources: [WebAIM Alt Text](https://webaim.org/techniques/alttext/), [WCAG.com Alt Text](https://www.wcag.com/blog/good-alt-text-bad-alt-text-making-your-content-perceivable/))

## Buttons and Interactive Elements

| Scenario | Screen Reader Output | User Experience |
|---|---|---|
| `<div onclick="...">` | *(no announcement)* | User doesn't know it exists as interactive. |
| `<div role="button" onclick="...">` (no keyboard) | "Send, button" | User presses Enter. Nothing happens. Interface lied. |
| `<span>` styled as link (no `href`, no role) | *(announced as plain text)* | User cannot Tab to it, cannot activate it. |
| `<button>Send</button>` | "Send, button" | Enter/Space works. Tab reaches it. Everything works. |
| Icon button with no label | "button" | User knows it's a button but has no idea what it does. |
| Icon button with `aria-label` | "Close dialog, button" | User knows exactly what it does. |

(Sources: [MDN ARIA button](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role), [BOIA ARIA Mistakes](https://www.boia.org/blog/4-mistakes-to-avoid-when-using-aria-roles))

## Links

| Scenario | Screen Reader Output (Links List) | User Experience |
|---|---|---|
| "Click here" x12 | "click here, click here, click here..." | Impossible to distinguish destinations. |
| "Read more" x8 | "read more, read more, read more..." | Same problem. Cannot navigate by links list. |
| Raw URL as text | "https colon slash slash www dot example dot com slash products slash enterprise slash pricing" | Painful to listen to, hard to understand. |
| "View enterprise pricing" | "View enterprise pricing" | User finds the right link immediately. |
| "Download annual report (PDF, 2.3MB)" | "Download annual report (PDF, 2.3MB)" | User knows format and size before downloading. |

(Sources: [Yale Links](https://usability.yale.edu/web-accessibility/articles/links), [WCAG.com Meaningful Links](https://www.wcag.com/blog/writing-meaningful-link-text/))

## Modals and Dialogs

| Scenario | User Experience |
|---|---|
| Focus stays on trigger after modal opens | User tabs through background page, completely unaware modal is open. |
| No focus trap in modal | User tabs out of modal into obscured background content. |
| No Escape handler | User cannot close modal by keyboard. Trapped or lost. |
| Focus not returned on close | Focus jumps to `<body>`. User must re-navigate entire page. |
| Stacked modals (newsletter + cookie + promo) | User is lost in layers of overlapping dialogs. |
| Proper: `<dialog>`, focus trap, Escape, return | Focus enters modal, cycles within it, Escape closes, focus returns to trigger. |

(Sources: [TestParty Modal](https://testparty.ai/blog/modal-dialog-accessibility), [OpenReplay Modals](https://blog.openreplay.com/common-accessibility-issues-modals-fix/))

## Focus Indicators

| Scenario | User Experience |
|---|---|
| `outline: none` globally | Sighted keyboard user cannot see where focus is. Every Tab press is blind. |
| Default browser outline | Visible but appears on mouse click too. Visually unappealing. |
| `:focus-visible` with custom style | Visible only for keyboard users. Clear, high-contrast ring. Best outcome. |
| Low-contrast focus ring | User can technically see it but struggles in bright environments. |

(Sources: [A11Y Project Outlines](https://www.a11yproject.com/posts/never-remove-css-outlines/), [MDN :focus-visible](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible))

## Error Messages

| Scenario | Screen Reader Output | User Experience |
|---|---|---|
| "Invalid input." | "Invalid input." | User has no idea what's wrong or how to fix it. |
| "Error." | "Error." | Useless. |
| "Please correct the errors below." | "Please correct the errors below." | Which errors? Where? |
| "Email address must include an @ symbol." | "Email address must include an @ symbol." | User knows exactly what to fix. |
| Error linked with `aria-describedby` | "Email address, edit text, invalid, Email must include @" | Error announced in context of the field. |

(Sources: [TetraLogical Form Validation](https://tetralogical.com/blog/2024/10/21/foundations-form-validation-and-error-messages/), [WebAIM Form Validation](https://webaim.org/techniques/formvalidation/))
