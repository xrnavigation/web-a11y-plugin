# Low Vision Experience

What the web looks and feels like for users with low vision, and what breaks when developers don't account for zoom, contrast, and reflow.

## Who Has Low Vision

Low vision is not blindness. Low-vision users can see -- but not well enough to read standard text without magnification. This includes:

- Age-related vision loss (macular degeneration, cataracts, glaucoma)
- Diabetic retinopathy
- Color blindness (8% of men, 0.5% of women)
- Anyone in bright sunlight, using a dim screen, or dealing with eye fatigue

Low-vision users typically zoom browsers to 200-400% to read text. They may also use OS-level screen magnifiers, high-contrast modes, or custom stylesheets.

## Zoom at 200%: What Breaks

### Horizontal Scrolling

When layouts use fixed widths, `min-width`, or absolute positioning, zooming forces horizontal scrolling. The user must scroll right to finish each line, then scroll left to start the next line, for every single line of text.

**Reading effort increases 40-100x** compared to reflowing text that wraps naturally.

WCAG 1.4.10 (Reflow) requires content to reflow without horizontal scrolling at 400% zoom (equivalent to 320px viewport width).

(Source: [W3C Low Vision TF](https://www.w3.org/WAI/GL/low-vision-a11y-tf/wiki/Resize_content))

### Overlapping Content

Fixed-position elements (sticky headers, floating buttons, fixed sidebars) stack on top of content at high zoom levels. Both the fixed element and the content beneath it become unreadable.

### Content Clipped by `overflow: hidden`

Text inside containers with `overflow: hidden` disappears off the edge when zoomed. The content exists in the DOM but is visually gone -- the user cannot scroll to reach it.

### Broken Navigation

Menus designed for specific viewport widths collapse into unusable states at high zoom. Navigation items overlap, dropdowns extend off-screen, and hamburger menus may not trigger correctly.

### The Mobile Layout Advantage

Low-vision users often trigger mobile/responsive layouts by zooming on desktop browsers. When responsive design works correctly, this is actually helpful -- single-column layouts reflow naturally. But many sites only test responsive design on actual mobile devices, not on zoomed desktop browsers.

## Low Contrast: The Most Common Violation

### The Numbers

- **83.9%** of the top million homepages have low-contrast text violations
- Average of **31.6** low-contrast text instances per page
- This is the #1 most common accessibility error on the web, every year

(Source: [WebAIM Million 2022](https://webaim.org/projects/million/))

### What It Feels Like

> "Straining our eyes, making us all feel older and a little less capable."
> -- [NNGroup](https://www.nngroup.com/articles/low-contrast/)

> "Users blame themselves when they are unable to accomplish tasks on a modern-looking website, because they cannot see the text or they struggle to read it."
> -- [NNGroup](https://www.nngroup.com/articles/low-contrast/)

Users with low vision, color blindness, or anyone in bright ambient light cannot read gray-on-white or light-colored text. The emotional impact: they don't realize the site is broken. They think something is wrong with them.

(Source: [BOIA Low Contrast](https://www.boia.org/blog/low-contrast-text-remains-the-most-common-accessibility-issue-in-2023))

### WCAG Contrast Requirements

| Content Type | Minimum Ratio | WCAG SC |
|---|---|---|
| Normal text (< 18pt / < 14pt bold) | 4.5:1 | 1.4.3 (AA) |
| Large text (>= 18pt / >= 14pt bold) | 3:1 | 1.4.3 (AA) |
| UI components and graphical objects | 3:1 | 1.4.11 (AA) |
| Enhanced contrast (normal text) | 7:1 | 1.4.6 (AAA) |

### Common Low-Contrast Patterns

| Pattern | Why It Fails |
|---|---|
| Light gray text on white background | Ratio often < 3:1 |
| Placeholder text (default browser gray) | Typically fails 4.5:1 |
| Disabled button text | Often too low contrast to read |
| Links that only differ by color (no underline) | Color-blind users can't distinguish them from body text |
| Text over images without overlay | Contrast varies wildly across the image |
| Light text on gradient backgrounds | Parts of the gradient may pass, parts may fail |

## Placeholder Text: A Double Problem

Placeholder text fails on two fronts:

1. **Contrast:** Default placeholder color is light gray, typically failing the 4.5:1 ratio
2. **Persistence:** Placeholders disappear when the user focuses the field or starts typing

For users with short-term memory difficulties (traumatic brain injury, ADHD, aging), the vanishing label means they forget what the field wanted. They must click away from the field to see the placeholder again -- and risk losing what they typed.

**The fix:** Use visible, persistent `<label>` elements. Never use placeholder text as the only label.

(Source: [Deque Placeholder](https://www.deque.com/blog/accessible-forms-the-problem-with-placeholders/), [W3C Placeholder Research](https://www.w3.org/WAI/GL/low-vision-a11y-tf/wiki/Placeholder_Research))

## Color as the Only Indicator

### The Problem

Using color alone to convey information excludes color-blind users:

- Red/green for error/success states -- indistinguishable for deuteranopia/protanopia (the most common types)
- Required fields marked only with red asterisks
- Chart data differentiated only by color
- Links distinguished from body text only by color (no underline)

### The Fix

Always pair color with a second indicator:

| Instead of Color Only | Add |
|---|---|
| Red border on error | Error icon + text message |
| Green checkmark for success | "Saved" text label |
| Red asterisk for required | "(required)" text |
| Colored chart lines | Patterns, labels, or shapes |
| Blue link text (no underline) | Underline or other visual cue |

## What Correct Low-Vision Design Looks Like

- Text reflows at 400% zoom without horizontal scrolling
- All text meets 4.5:1 contrast ratio (7:1 for AAA)
- UI components meet 3:1 contrast ratio
- Color is never the only indicator
- Labels are visible and persistent (not placeholder-dependent)
- Fixed/sticky elements don't obscure content at high zoom
- `prefers-contrast: more` media query adjusts for users who request high contrast
- Responsive layouts work on zoomed desktop browsers, not just mobile devices
