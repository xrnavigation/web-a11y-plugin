# Link Text Guide
## Contents

- [The Links List](#the-links-list)
  - [What Generic Links Sound Like in a Links List](#what-generic-links-sound-like-in-a-links-list)
  - [What Descriptive Links Sound Like](#what-descriptive-links-sound-like)
- [WCAG Requirements](#wcag-requirements)
- [Bad vs. Good Examples](#bad-vs-good-examples)
- [Rules](#rules)
- [Fixing "Read More" Links](#fixing-read-more-links)
  - [Option 1: Make the Article Title the Link (Preferred)](#option-1-make-the-article-title-the-link-preferred)
  - [Option 2: Visually Hidden Text (Acceptable)](#option-2-visually-hidden-text-acceptable)
  - [Option 3: aria-label (Acceptable, With Caveats)](#option-3-aria-label-acceptable-with-caveats)
- [Sources](#sources)


This reference covers accessible link text writing in depth — what links sound like to assistive technology users, why generic link text is hostile, and how to fix common patterns.

---

## The Links List

Screen reader users navigate by pulling up a **links list** — a summary of every link on the page, stripped of surrounding context, presented alphabetically or in document order. This is a primary navigation strategy, faster than listening to the full page.

### What Generic Links Sound Like in a Links List

```
Click here
Click here
Click here
here
Learn more
Learn more
More
Read more
Read more
Read more
```

The user has no way to distinguish these links. They must leave the links list, navigate to each link in context, read surrounding text, and decide if that is the link they want — defeating the entire purpose of the links list.

### What Descriptive Links Sound Like

```
2025 annual report (PDF, 1.2 MB)
Apply for disability benefits
Carbon reduction program results
Employee handbook
How to reset your password
Manager training schedule
Parental leave policy
Q3 earnings summary
Workplace safety guidelines
```

Every link is self-explanatory. The user picks the one they need and goes directly there.

([WebAIM Screen Reader Survey #10](https://webaim.org/projects/screenreadersurvey10/); [Section508 Descriptive Links](https://www.section508.gov/blog/accessibility-bytes/descriptive-links-and-hypertext/))

---

## WCAG Requirements

**2.4.4 Link Purpose (In Context), Level A:** Purpose determinable from link text alone or with programmatic context (same sentence, paragraph, list item, or table cell).

**2.4.9 Link Purpose (Link Only), Level AAA:** Purpose determinable from link text alone, without any surrounding context.

([W3C Understanding SC 2.4.4](https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-in-context.html))

---

## Bad vs. Good Examples

| Bad | Good | Why |
|-----|------|-----|
| "Click here to view our annual report" | "2025 annual report" | "Click here" is noise. Screen readers already announce "link." The user needs the destination, not the mechanic of clicking. |
| "Read more" (repeated 8 times) | "How we reduced carbon emissions by 40%" | In a links list, eight "Read more" entries are indistinguishable. |
| "here" in "Download the PDF here" | "Download the quarterly earnings PDF" | "here" conveys zero information out of context. |
| `https://www.example.com/reports/q3-2025-earnings.pdf` | "Q3 2025 earnings report (PDF, 2.4 MB)" | A descriptive title makes the destination clearer than a raw URL; pronunciation varies. |
| "Learn more" | "Learn how to apply for disability benefits" | "Learn more" is ambiguous in a links list. |

---

## Rules

1. **Do not include "link" in link text.** Screen readers announce "link" before reading the text. "Link to our products page" causes "link, link to our products page."

2. **Be concise.** Screen reader users must listen to the entire text. "Today's weather" beats "click here to access today's weather forecast for your area."

3. **Images as links:** The `alt` attribute serves as the link text. Describe the destination, not the image appearance. `alt="Product catalog"` not `alt="photo of books on shelf."`

4. **Unique text for unique destinations.** Two links that go to different pages must have different text.

5. **Underline links in body text.** If underlines are removed, links must have 3:1 contrast against surrounding body text AND a non-color visual cue on focus/hover.

---

## Fixing "Read More" Links

"Read more" is especially common on blog/news index pages. A page with 10 articles has 10 indistinguishable "Read more" links.

### Option 1: Make the Article Title the Link (Preferred)

```html
<article>
  <h2><a href="/articles/carbon-reduction">How we reduced carbon emissions by 40%</a></h2>
  <p>Our latest sustainability report shows...</p>
</article>
```

### Option 2: Visually Hidden Text (Acceptable)

Preserves visual design while adding screen reader context:

```html
<a href="/articles/carbon-reduction">
  Read more<span class="sr-only"> about how we reduced carbon emissions by 40%</span>
</a>
```

### Option 3: aria-label (Acceptable, With Caveats)

```html
<a href="/articles/carbon-reduction" aria-label="Read more about carbon reduction program">Read more</a>
```

**Caveat:** The visible text ("Read more") and aria-label diverge. Speech recognition users (Dragon NaturallySpeaking) who say "click Read more" may not activate the correct link because the accessible name does not start with the visible text, violating WCAG 2.5.3 Label in Name.

Option 1 is strongly preferred. Options 2 and 3 are workarounds for situations where the visual design cannot change.

([Vision Australia: Read More Links](https://www.visionaustralia.org/business-consulting/digital-access/blog/how-to-make-read-more-links-accessible); [WCAG 2.5.3](https://www.w3.org/WAI/WCAG21/Understanding/label-in-name.html))

---

## Sources

- [WebAIM Link Text](https://webaim.org/techniques/hypertext/link_text)
- [Yale Accessible Links](https://usability.yale.edu/web-accessibility/articles/links)
- [Section508 Descriptive Links](https://www.section508.gov/blog/accessibility-bytes/descriptive-links-and-hypertext/)
- [Pope Tech: Why Ambiguous Links Are Problematic](https://blog.pope.tech/2018/07/26/why-ambiguous-links-are-problematic/)
- [Vision Australia: Read More Links](https://www.visionaustralia.org/business-consulting/digital-access/blog/how-to-make-read-more-links-accessible)
- [W3C Understanding SC 2.4.4](https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-in-context.html)
- [WCAG.com Meaningful Link Text](https://www.wcag.com/blog/writing-meaningful-link-text/)
