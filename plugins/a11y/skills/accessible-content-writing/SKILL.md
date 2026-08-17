---
name: accessible-content-writing
description: Guides accessible content writing — link text, error messages, alt text as craft, plain language, headings as navigation, and microcopy. Auto-invokes when writing UI text, link labels, error messages, button labels, form instructions, or heading structures. Content is an interface — bad content is an accessibility barrier.
allowed-tools: Read, Glob, Grep
---

# Accessible Content Writing

> "Content IS the interface. For screen reader users, there is no visual layout, no color coding, no spatial relationships. The words are the entire experience."

> "86% said more accessible websites would have a bigger impact than better assistive technology."
> — [WebAIM Screen Reader Survey #10](https://webaim.org/projects/screenreadersurvey10/)

Bad content is an accessibility barrier, not just bad UX. Correct markup with vague link text, hostile error messages, or missing heading structure is still inaccessible. Every piece of text — label, heading, link, error, alt text — is interface design.

---

## 1. Content Is an Interface

Screen reader users do not see your layout. They hear a linear stream of text, navigate by headings, pull up link lists, and tab through interactive elements. Every word you write is a navigation aid or a navigation obstacle.

**The test for all content:** Does it make sense when ripped from its surrounding context — in a links list, a headings outline, or a screen reader announcement? If not, rewrite it.

---

## 2. Link Text

### What Bad Links Sound Like

Screen reader users pull up a **links list** — every link on the page, stripped of context, sorted alphabetically. Generic link text produces this:

```
Click here
Click here
Click here
here
Learn more
Learn more
Read more
Read more
Read more
```

The user has no idea where any link goes. This is a primary navigation strategy rendered useless. ([WebAIM Survey #10](https://webaim.org/projects/screenreadersurvey10/) — 71.6% navigate by headings; link lists are comparably common.)

### WCAG Requirement

**2.4.4 Link Purpose (In Context), Level A:** Purpose determinable from link text alone or with programmatic context. **2.4.9 Link Purpose (Link Only), Level AAA:** Purpose determinable from link text alone. ([W3C SC 2.4.4](https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-in-context.html))

### Bad vs. Good

| Bad | Good | Why |
|-----|------|-----|
| "Click here to view our annual report" | "2025 annual report" | Screen readers already announce "link." "Click here" is noise. |
| "Read more" (repeated 8 times) | "How we reduced carbon emissions by 40%" | Eight "Read more" entries are indistinguishable in a links list. |
| "here" in "Download the PDF here" | "Download the quarterly earnings PDF" | "here" conveys zero information out of context. |
| `https://www.example.com/reports/q3.pdf` | "Q3 2025 earnings report (PDF, 2.4 MB)" | Raw URLs force screen readers to read every character. |

### Rules

- **Do not include "link" in link text.** Screen readers announce "link" before reading the text. "Link to our products page" becomes "link, link to our products page."
- **Be concise.** Users must listen to the entire link text. "Today's weather" beats "click here to access today's weather forecast for your area."
- **Images as links:** The `alt` attribute serves as the link text. Describe the destination, not the image. `alt="Product catalog"` not `alt="photo of books."`
- **Unique text for unique destinations.** If two links go to different places, they must have different text.

For detailed examples and techniques, see: [references/link-text-guide.md](references/link-text-guide.md)

([WebAIM Link Text](https://webaim.org/techniques/hypertext/link_text); [Yale Links](https://usability.yale.edu/web-accessibility/articles/links); [Section508 Descriptive Links](https://www.section508.gov/blog/accessibility-bytes/descriptive-links-and-hypertext/))

---

## 3. Error Messages

### The Framework: Visibility, Communication, Efficiency

**Visibility** — the user must notice the error:
- Display adjacent to the field, not in a distant banner.
- Use 3+ redundant indicators: bold, color, icon, border. Never color alone (350M people have color-vision deficiency).
- Do not show premature errors while the user is still typing.

**Communication** — the user must understand the error:
- Plain language. No jargon, no error codes.
- Specific: what went wrong AND how to fix it.
- Non-blaming tone. No "invalid," "illegal," "you failed to."

**Efficiency** — the user must be able to fix the error:
- Preserve user input. Never clear a field on error.
- Suggest corrections when possible ("Did you mean gmail.com?").

([NN/g Error-Message Guidelines](https://www.nngroup.com/articles/error-message-guidelines/))

### Bad vs. Good

| Bad | Good | Why |
|-----|------|-----|
| "Invalid input" | "Enter a date of birth in the format DD/MM/YYYY" | Bad version says nothing about what is wrong or how to fix it. |
| "Error: field required" | "Enter your email address" | Generic message forces the user to guess which field and what it wants. |
| "Please enter a valid email" | "Enter an email address in the correct format, like name@example.com" | "Valid" is jargon. The example shows what "correct" means. |
| "Oops! Something went wrong" | "Your payment could not be processed. Check your card details and try again." | Humor is patronizing when the user is trying to complete a task. |

### GOV.UK Error Patterns

- Show BOTH an error summary at page top AND inline errors next to each field.
- Use identical wording in both locations.
- Prefix with visually hidden "Error:" so screen readers announce "Error: Enter your first name."
- Match the field label: if the label says "How many hours do you work a week?" the error says "Enter how many hours you work a week."
- Vary by error type: empty ("Enter your email address"), wrong format ("Enter an email address in the correct format, like name@example.com"), too long ("Email address must be 256 characters or fewer").

For full GOV.UK patterns and AT integration, see: [references/error-message-craft.md](references/error-message-craft.md)

([GOV.UK Error Message](https://design-system.service.gov.uk/components/error-message/); [GOV.UK Validation](https://design-system.service.gov.uk/patterns/validation/))

---

## 4. Headings as Navigation

### What Heading Navigation Sounds Like

Screen reader users press H to jump heading to heading, hearing an outline:

> "Heading level 1: Apply for Disability Benefits. Heading level 2: Who is eligible. Heading level 3: Age requirements. Heading level 3: Income requirements. Heading level 2: How to apply..."

They jump to the section they need and read from there. **71.6% of screen reader users navigate by headings as their first action on a new page.** Without heading structure, a 2-minute visual scan becomes a 20-30 minute linear listen. ([WebAIM Survey #10](https://webaim.org/projects/screenreadersurvey10/))

### Bad vs. Good Structure

Bad (no hierarchy, skipped levels, vague):
```html
<h1>Welcome</h1>
<h3>Info</h3>          <!-- skipped h2 -->
<h4>Details</h4>       <!-- what details? -->
<h2>More</h2>          <!-- more what? -->
```

Good (logical hierarchy, informative):
```html
<h1>Apply for Disability Benefits</h1>
  <h2>Who is eligible</h2>
    <h3>Age requirements</h3>
    <h3>Income requirements</h3>
  <h2>How to apply</h2>
    <h3>Documents you need</h3>
    <h3>Where to submit</h3>
```

### Rules

- One `<h1>` per page, describing the page topic.
- Nest hierarchically: h1 > h2 > h3. Do not skip levels.
- Every content section needs a heading — without one, screen reader users cannot jump to it.
- Headings must be informative: "How to apply" not "Section 3."
- Do not use heading tags for visual styling. Use CSS instead.

For detailed heading patterns, see: [references/heading-navigation.md](references/heading-navigation.md)

([A11Y Project Headings](https://www.a11yproject.com/posts/how-to-accessible-heading-structure/); [Yale Headings](https://usability.yale.edu/web-accessibility/articles/headings))

---

## 5. Plain Language

Plain language means the reader can understand and act on the content the first time they read it. The US Plain Writing Act of 2010 codifies this for federal agencies. ([Plain Language Guidelines](https://digital.gov/guides/plain-language))

### Rules

1. **Write for the least expert reader.** Not your peers.
2. **Use everyday words.** "Use" not "utilize." "Start" not "commence." "About" not "approximately."
3. **Use active voice.** "We will review your application" not "Your application will be reviewed."
4. **Write short sentences.** One idea per sentence. 15-20 words average.
5. **Aim for 6th-8th grade reading level.** This reduces cognitive load for everyone, including expert readers.

### WCAG Connection

WCAG 3.1.5 (Reading Level, AAA) recommends content at lower secondary education level. WCAG 3.1.3 (Unusual Words) requires definitions for jargon and idioms.

### Bad vs. Good

| Bad | Good | Why |
|-----|------|-----|
| "Individuals utilizing this application shall be required to furnish documentation substantiating their eligibility." | "You need to provide documents that show you are eligible." | Half the length, uses "you," replaces four pieces of jargon. |
| "Failure to comply with the aforementioned requirements may result in the termination of benefits." | "If you do not meet these requirements, your benefits may stop." | Active voice, concrete consequence, no legalese. |

([MN.gov Plain Language and Accessibility](https://mn.gov/mnit/about-mnit/accessibility/news/?id=38-614411))

---

## 6. Button Labels and Microcopy

### Button Labels

Button text must make sense when read aloud, without visual context. Screen readers announce "button" before the text.

| Bad | Good | Why |
|-----|------|-----|
| "Submit" (on multiple forms) | "Submit application" / "Submit payment" | Multiple "Submit" buttons are ambiguous in a buttons list. |
| "X" (close button) | "Close dialog" or `aria-label="Close"` | "X" is visual convention; conveys nothing audibly. |
| "Go" | "Search" or "Search products" | "Go" gives no indication of what happens. |

### Form Element Order

Screen reader users encounter elements sequentially. Correct order:

1. **Label**
2. **Hint/instruction text**
3. **Error message** (if applicable)
4. **Input field**

If the hint appears after the input, users reach the field before knowing the format requirement, type something wrong, and only then discover the instruction.

### The Placeholder Problem

Never use placeholder as the only label. Placeholder text:

1. **Disappears on input** — users with cognitive disabilities cannot reference it while typing.
2. **Low contrast by default** — typically fails WCAG 1.4.3 (4.5:1).
3. **Not reliably announced** by screen readers.
4. **Looks pre-filled** — users with cognitive disabilities may skip it.
5. **Is not a label** — fails WCAG 1.3.1.

**Instead:** Use visible, persistent `<label>` elements. Use hint text outside the input for format examples.

```html
<!-- WRONG -->
<input placeholder="Email">

<!-- RIGHT -->
<label>Email address</label>
<span class="hint">For example, name@company.com</span>
<input type="email">
```

### Help Text

- Place help text before the input, not after.
- Never put critical information only in a tooltip.
- Use `aria-describedby` to link help text to its field programmatically.
- Do not place important microcopy below a submit button — screen reader users may submit before encountering it.

([W3C Form Instructions](https://www.w3.org/WAI/tutorials/forms/instructions/); [Deque Placeholder Problem](https://www.deque.com/blog/accessible-forms-the-problem-with-placeholders/); [Harvard Labels and Instructions](https://accessibility.huit.harvard.edu/provide-accessible-labels-and-instructions))

---

## 7. Anti-Patterns

### Generic Links

"Click here," "Read more," "Learn more," "here," "more" — all useless in a links list. Fix: make the link text describe the destination.

If the visual design requires "Read more," use visually hidden text:
```html
<a href="...">Read more<span class="sr-only"> about carbon reduction program</span></a>
```

Prefer making the article title the link instead. ([Vision Australia Read More Links](https://www.visionaustralia.org/business-consulting/digital-access/blog/how-to-make-read-more-links-accessible))

### Placeholder as Label

`<input placeholder="Email">` with no `<label>` — the label disappears on focus, fails WCAG 1.3.1, and is not reliably announced by screen readers.

### Filename Alt Text

`alt="IMG_20240315_crop2.jpg"` — the user hears every character, underscore, and file extension. This happens when alt text is auto-populated from file metadata. Always write a human description.

### Missing Alt vs. Empty Alt

No `alt` attribute at all causes screen readers to read the file path. Empty `alt=""` is intentional silence for decorative images. These are not the same thing.

### Headings for Styling

Using `<h3>` to make text large and bold when it is not a section heading — breaks heading navigation and creates false outline entries.

### Required Field Asterisks Only

Red asterisks without explanation fail for color-blind users and may not be announced by screen readers. Spell it out: "Date of birth (required)."

---

## 8. Cross-References

For related skills in this plugin:

- **alt-text-quality** — detailed alt text writing framework with context-dependent examples
- **form-a11y** — form markup, label association, fieldset/legend, validation patterns
- **cognitive-a11y** — cognitive load reduction, timeout handling, predictable layouts
- **aria-decision-framework** — when to use ARIA vs. native HTML elements

For detailed reference material:

- [references/link-text-guide.md](references/link-text-guide.md) — link text patterns, "Read more" fixes, links list examples
- [references/error-message-craft.md](references/error-message-craft.md) — NN/g framework, GOV.UK patterns, AT integration
- [references/heading-navigation.md](references/heading-navigation.md) — heading outlines, screen reader navigation, structural patterns
- [references/sources.yaml](references/sources.yaml) — provenance for all cited sources
