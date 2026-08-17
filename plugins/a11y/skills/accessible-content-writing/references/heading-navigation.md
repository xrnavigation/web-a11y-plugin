# Heading Navigation
## Contents

- [How Screen Reader Users Navigate](#how-screen-reader-users-navigate)
  - [1. Navigate by Headings (H key)](#1-navigate-by-headings-h-key)
  - [2. List All Headings](#2-list-all-headings)
  - [3. Navigate by Heading Level (Number Keys)](#3-navigate-by-heading-level-number-keys)
  - [Without Heading Structure](#without-heading-structure)
- [What Good Heading Structure Looks Like](#what-good-heading-structure-looks-like)
  - [Rules](#rules)
- [Bad vs. Good Structure](#bad-vs-good-structure)
  - [Bad: No Hierarchy, Skipped Levels, Vague](#bad-no-hierarchy-skipped-levels-vague)
  - [Good: Logical Hierarchy, Informative](#good-logical-hierarchy-informative)
- [Common Mistakes](#common-mistakes)
  - [Using Bold Text Instead of Heading Elements](#using-bold-text-instead-of-heading-elements)
  - [Using Headings for Visual Styling](#using-headings-for-visual-styling)
  - [Skipping Heading Levels](#skipping-heading-levels)
  - [Multiple h1 Elements](#multiple-h1-elements)
- [Heading Writing Guidelines](#heading-writing-guidelines)
- [Sources](#sources)


This reference covers how screen reader users navigate by headings, why heading structure is critical for accessibility, and patterns for writing effective heading hierarchies.

---

## How Screen Reader Users Navigate

Screen reader users do not read pages top-to-bottom like sighted users scan visually. Their primary heading-based strategies:

### 1. Navigate by Headings (H key)

The user presses H (JAWS/NVDA) to jump from heading to heading, hearing an outline:

> "Heading level 1: Products. Heading level 2: Enterprise Plan. Heading level 3: Features."

They jump to the section they want and start reading from there. **71.6% of screen reader users navigate by headings as their first action on a new page.**

### 2. List All Headings

Screen readers generate a headings list (like a table of contents). Users scan this list to understand page structure and jump directly to any section.

### 3. Navigate by Heading Level (Number Keys)

Users press a number key (1-6) to jump only to headings of that level. Pressing "2" repeatedly jumps between h2 headings, giving a section-level overview.

### Without Heading Structure

The user's only option is to listen linearly through the entire page. **A 2-minute visual scan becomes a 20-30 minute linear listen.** Many users simply leave.

([WebAIM Screen Reader Survey #10](https://webaim.org/projects/screenreadersurvey10/); [Yale Headings](https://usability.yale.edu/web-accessibility/articles/headings))

---

## What Good Heading Structure Looks Like

### Rules

1. **One `<h1>` per page**, describing the page topic.
2. **Nest hierarchically:** h1 > h2 > h3. Do not skip levels (h2 directly to h4).
3. **Every section of content should have a heading.** If content has no heading, screen reader users cannot jump to it.
4. **Headings must be informative.** "How to apply" not "Section 3." The heading IS the user's navigation label.
5. **Do not use headings for visual styling.** If text should be large/bold but is not a section heading, use CSS — not an `<h3>` tag. False headings pollute the outline.
6. **Do not style non-headings to look like headings.** Bold/large text that is not marked up as `<h2>` etc. is invisible to heading navigation.

---

## Bad vs. Good Structure

### Bad: No Hierarchy, Skipped Levels, Vague

```html
<h1>Welcome</h1>
<h3>Info</h3>          <!-- skipped h2 -->
<h4>Details</h4>       <!-- what details? -->
<h2>More</h2>          <!-- more what? -->
<h4>Click here</h4>    <!-- not a heading concept, skipped h3 -->
```

**What the user hears in headings list:** "Welcome... Info... Details... More... Click here..." — no information about page content, no predictable structure, no way to find anything without reading everything.

### Good: Logical Hierarchy, Informative

```html
<h1>Apply for Disability Benefits</h1>
  <h2>Who is eligible</h2>
    <h3>Age requirements</h3>
    <h3>Income requirements</h3>
  <h2>How to apply</h2>
    <h3>Documents you need</h3>
    <h3>Where to submit</h3>
  <h2>After you apply</h2>
    <h3>Processing time</h3>
    <h3>How to check your status</h3>
```

**What the user hears:** "Apply for Disability Benefits... Who is eligible... Age requirements... Income requirements... How to apply..." — a complete outline. The user knows immediately whether this page has what they need and exactly where to find it.

---

## Common Mistakes

### Using Bold Text Instead of Heading Elements

```html
<!-- WRONG — invisible to heading navigation -->
<p><strong>Eligibility Requirements</strong></p>

<!-- RIGHT — screen readers can navigate to this -->
<h2>Eligibility Requirements</h2>
```

Bold text looks like a heading visually but does not appear in the headings list. Screen reader users will never find this section.

### Using Headings for Visual Styling

```html
<!-- WRONG — creates false outline entries -->
<h3>Note: This form must be completed by March 31.</h3>

<!-- RIGHT — use CSS for visual emphasis -->
<p class="callout">Note: This form must be completed by March 31.</p>
```

This note is not a section heading, but it appears in the headings list, polluting the outline and confusing navigation.

### Skipping Heading Levels

```html
<!-- WRONG — h2 to h4 skip -->
<h2>Products</h2>
<h4>Enterprise Features</h4>

<!-- RIGHT — maintain hierarchy -->
<h2>Products</h2>
<h3>Enterprise Features</h3>
```

Skipped levels suggest a broken structure. Users navigating by level (pressing "3" to jump between h3s) will miss content under incorrectly-leveled headings.

### Multiple h1 Elements

```html
<!-- WRONG — confusing page structure -->
<h1>Company Name</h1>
<h1>Product Page</h1>

<!-- RIGHT — one h1, use h2 for sections -->
<h1>Product Page</h1>
```

Multiple h1 elements create ambiguity about the page's primary topic. The h1 is the page title; all other sections are h2 and below.

---

## Heading Writing Guidelines

1. **Front-load key information.** "Eligibility requirements" not "Here are the eligibility requirements you need to know about."
2. **Use question headings when appropriate.** "What documents do I need?" is more scannable than "Required Documentation" for users looking for answers.
3. **Be specific.** "Age requirements for disability benefits" is better than "Requirements" when multiple types of requirements exist on the page.
4. **Keep headings concise.** Users hear headings in a list. Long headings are harder to scan aurally.
5. **Do not end headings with punctuation** (colons, periods). They create unnecessary pauses in screen reader output.

---

## Sources

- [WebAIM Screen Reader Survey #10](https://webaim.org/projects/screenreadersurvey10/)
- [A11Y Project: Heading Structure](https://www.a11yproject.com/posts/how-to-accessible-heading-structure/)
- [Yale: Headings](https://usability.yale.edu/web-accessibility/articles/headings)
- [Section508: Document Headings](https://www.section508.gov/blog/accessibility-bytes/document-headings/)
- [WebAIM: Semantic Structure — Headings](https://webaim.org/techniques/headings/)
- [web.dev: Headings and Landmarks](https://web.dev/articles/headings-and-landmarks)
