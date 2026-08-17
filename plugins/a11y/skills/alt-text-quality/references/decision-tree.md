# W3C Alt Text Decision Tree — Complete Reference

Source: [W3C Alt Text Decision Tree](https://www.w3.org/WAI/tutorials/images/decision-tree/), [W3C Images Tutorial](https://www.w3.org/WAI/tutorials/images/)

Follow from top to bottom. Stop at the first matching branch.

---

## Node 1: Does the image contain text?

**Yes — and the text is also present as real text nearby:**
- Use `alt=""` (decorative — the real text carries the information)

**Yes — and the text is only for visual effect:**
- Use `alt=""` (decorative)

**Yes — and the text functions as an icon or symbol:**
- `alt` describes the **function**, not the text itself
- Example: phone icon with number → `alt="Call us"`, not `alt="Phone"`

**Yes — and the text is unique to the image, not present elsewhere:**
- `alt` contains the **same text** as shown in the image
- Example: badge reading "Certified Organic" → `alt="Certified Organic"`

**No:** Continue to Node 2.

---

## Node 2: Is the image used in a link or button?

**Yes:**
- `alt` describes the **destination or action**, not the image's appearance
- Examples:
  - Logo linking to homepage → `alt="Acme Corp home"`
  - Thumbnail linking to full article → `alt="Read: Article Title"`
  - Arrow icon in a "next" button → `alt="Next page"`

**No:** Continue to Node 3.

---

## Node 3: Does the image contribute meaning to the page?

**Yes — simple graphic or photograph:**
- Brief `alt` describing the meaning it conveys in context
- Example: photo illustrating a news story → `alt="Senator Doe announcing the new policy"`

**Yes — graph, chart, or complex information:**
- Short `alt` summarizing what the image shows
- Full data provided elsewhere: `<figcaption>`, adjacent text, `aria-describedby`, or a linked page
- Example: `alt="Bar chart: Q3 revenue by region"` with a data table below

**Yes — but redundant to adjacent real text:**
- Use `alt=""` — the adjacent text already carries the information

**No:** Continue to Node 4.

---

## Node 4: Is the image purely decorative?

**Yes:**
- Use `alt=""` (null alt attribute — the attribute is present but empty)
- Never omit the `alt` attribute entirely
- Examples: borders, spacers, ambient backgrounds, ornamental flourishes

**No:** Continue to Node 5.

---

## Node 5: Not covered above

Edge cases not addressed by the tree. Consult the full [W3C Images Tutorial](https://www.w3.org/WAI/tutorials/images/).

### Groups of Images

Multiple images conveying a single piece of information (e.g., star ratings):
- One image carries the alt text for the group
- Others get `alt=""`
- Example: 4 of 5 stars filled → first star: `alt="Rating: 4 out of 5"`, others: `alt=""`

### Image Maps

- Overall `<img>` alt provides context for the set of links
- Each `<area>` has its own alt describing the link destination

---

## Image Categories Summary

| Category | Rule | Example |
|---|---|---|
| **Decorative** | `alt=""` | Background texture, divider line, ambient photo |
| **Informative** | `alt` describes essential information | News photo, illustration, diagram |
| **Functional** | `alt` describes action/destination | Logo link, icon button, image map area |
| **Images of text** | `alt` contains the same words | Badge, banner with text, certificate |
| **Complex** | Short `alt` + long description elsewhere | Chart, graph, infographic, architectural diagram |
| **Groups** | One image carries group alt, rest `alt=""` | Star rating, multi-part illustration |
