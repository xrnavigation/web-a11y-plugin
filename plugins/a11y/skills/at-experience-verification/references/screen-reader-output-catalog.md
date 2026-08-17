# Screen Reader Output Catalog

What screen readers actually say for common HTML elements. Use this to verify your markup produces the right announcements.

## NVDA Announcement Patterns

| HTML | NVDA Announces |
|---|---|
| `<h1>Products</h1>` | "heading level 1, Products" |
| `<h2>Enterprise Plan</h2>` | "heading level 2, Enterprise Plan" |
| `<h3>Features</h3>` | "heading level 3, Features" |
| `<a href="/pricing">View pricing</a>` | "link, View pricing" |
| Previously visited `<a>` | "visited link, View pricing" |
| `<button>Submit</button>` | "button, Submit" |
| `<button disabled>Submit</button>` | "button, Submit, unavailable" |
| `<img alt="A tornado-damaged house">` | "graphic, A tornado-damaged house" |
| `<img>` (no alt attribute) | "graphic, IMG_20240315_crop2.jpg" (reads filename) |
| `<img alt="">` (decorative) | *(skipped -- no announcement)* |
| `<input>` with `<label>First name</label>` | "First name, edit, has auto complete" |
| `<input>` with no label | "edit" or "edit, blank" |
| `<input type="checkbox">` with label | "Accept terms, checkbox, not checked" |
| `<input type="checkbox" checked>` with label | "Accept terms, checkbox, checked" |
| `<input type="radio">` with label | "Option A, radio button, not selected" |
| `<select>` with label | "Country, combo box, collapsed, United States" |
| `<textarea>` with label | "Comments, edit, multi line" |
| `<table>` | "table with 4 columns and 12 rows" |
| `<th>` while navigating table | "column header, Name" or "row header, January" |
| `<nav>` | "navigation landmark" |
| `<main>` | "main landmark" |
| `<aside>` | "complementary landmark" |
| `<header>` (page-level) | "banner landmark" |
| `<footer>` (page-level) | "content info landmark" |
| `<section aria-label="Results">` | "Results, region" |
| `role="alert"` content | *(interrupts current speech to read alert text)* |
| `aria-live="polite"` content change | *(waits for pause, then reads new content)* |
| `aria-live="assertive"` content change | *(interrupts current speech to read new content)* |
| `<details>/<summary>` | "Summary text, collapsed, button" / "Summary text, expanded, button" |
| `<dialog>` | "dialog, Dialog Title" |
| `<progress value="75" max="100">` | "progress bar, 75%" |

## Cross-Screen-Reader Differences

| Element | NVDA | JAWS | VoiceOver (macOS) |
|---|---|---|---|
| Image | "graphic" | "image" | "image" |
| Text input | "edit" | "edit text" | "text field" |
| Heading | "heading level 2" | "heading level 2" | "heading level 2, 2 of 5" (includes position) |
| Link | "link" | "link" | "link" |
| Button | "button" | "button" | "button" |
| Checkbox | "checkbox, not checked" | "check box, not checked" | "unticked, tick box" |

(Sources: [Deque NVDA Shortcuts](https://dequeuniversity.com/screenreaders/nvda-keyboard-shortcuts), [Illinois SR Guide](https://doit.illinois.gov/initiatives/accessibility/testing/screen-reader-guide.html), [CSS-Tricks SR Comparison](https://css-tricks.com/comparing-jaws-nvda-and-voiceover/))

## Navigation Shortcuts

Screen reader users don't Tab through everything. They use shortcut keys to jump by element type:

| Key (NVDA/JAWS) | Jumps To |
|---|---|
| `H` | Next heading |
| `1`-`6` | Next heading at that level |
| `K` | Next link |
| `F` | Next form field |
| `T` | Next table |
| `D` | Next landmark |
| `B` | Next button |
| `G` | Next graphic |

**71.6% of screen reader users navigate by headings** -- it is the most common navigation strategy. When headings are missing, NVDA says "no next heading" and the user is stranded with no structural map of the page. ([WebAIM Survey #10](https://webaim.org/projects/screenreadersurvey10/))

## What "No Next Heading" Means

When a user presses `H` and hears "no next heading," it means:

- There is no heading structure on the page
- The only option is to arrow down line by line through the entire document
- A 2-minute visual scan becomes a 20-30 minute linear listen
- The user cannot skim, cannot jump, must listen to everything or leave

> Sites lacking useful headings AND landmarks are instant-leave triggers.
> -- ([Allyant](https://allyant.com/blog/my-experience-of-navigating-the-web-as-a-blind-user/))
