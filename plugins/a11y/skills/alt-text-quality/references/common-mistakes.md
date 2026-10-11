# Common Alt Text Mistakes
## Contents

- [1. Starting with "image of", "photo of", "graphic of"](#1-starting-with-image-of-photo-of-graphic-of)
- [2. Missing alt attribute entirely](#2-missing-alt-attribute-entirely)
- [3. Using the filename as alt text](#3-using-the-filename-as-alt-text)
- [4. Adding alt text to decorative images](#4-adding-alt-text-to-decorative-images)
- [5. Duplicating caption text in alt](#5-duplicating-caption-text-in-alt)
- [6. Describing the wrong thing](#6-describing-the-wrong-thing)
- [7. Using "company logo" as alt text](#7-using-company-logo-as-alt-text)
- [8. Overly long alt text](#8-overly-long-alt-text)
- [9. Poor spelling and punctuation](#9-poor-spelling-and-punctuation)
- [10. SEO keyword stuffing](#10-seo-keyword-stuffing)


Sources: [BOIA](https://www.boia.org/blog/8-common-image-alt-text-mistakes-to-stop-making), [WebAIM](https://webaim.org/techniques/alttext/), [Allyant](https://allyant.com/blog/6-common-alt-text-mistakes-and-best-practices/)

---

## 1. Starting with "image of", "photo of", "graphic of"

Image semantics can make generic prefixes redundant. Spoken role wording depends on the browser, screen reader and settings; do not treat illustrative speech as observed output.

**Exception:** The image *type* is relevant when the medium matters:
- "Oil painting of..." on an art history page
- "Screenshot of..." in a UI walkthrough
- "X-ray showing..." in a medical context

---

## 2. Missing alt attribute entirely

Without `alt`, a browser or screen reader may expose a filename or another unhelpful fallback. Record the actual behavior in supported combinations instead of promising a particular spoken string.

**Rule:** Always include `alt`. Use `alt=""` for decorative images. Never omit the attribute.

---

## 3. Using the filename as alt text

`alt="IMG_0437.jpg"` or `alt="hero-banner-v2-final.png"` provides no useful information. It is functionally equivalent to having no alt text.

---

## 4. Adding alt text to decorative images

Decorative images (borders, spacers, ambient backgrounds, ornamental flourishes) should have `alt=""`. Describing them forces screen reader users to listen to irrelevant content, creating noise that slows navigation.

---

## 5. Duplicating caption text in alt

A caption alone does not make an image decorative. Use empty alt only if nearby text conveys all meaningful visual information; otherwise describe what the caption omits ([WAI decorative images](https://www.w3.org/WAI/tutorials/images/decorative/)).

```html
<!-- RIGHT -->
<figure>
  <img src="ochoa.jpg" alt="">
  <figcaption>Astronaut Ellen Ochoa aboard the Space Shuttle</figcaption>
</figure>

<!-- WRONG — redundant -->
<figure>
  <img src="ochoa.jpg" alt="Astronaut Ellen Ochoa aboard the Space Shuttle">
  <figcaption>Astronaut Ellen Ochoa aboard the Space Shuttle</figcaption>
</figure>
```

---

## 6. Describing the wrong thing

Alt text must match the image's purpose **in context**, not its visual appearance.

| Context | Wrong | Right |
|---|---|---|
| News article about her achievement | `alt="Woman in blue suit at podium"` | `alt="Senator Jane Doe"` |
| Fashion article about the outfit | `alt="Senator Jane Doe"` | `alt="Navy blue tailored suit with pearl brooch"` |

---

## 7. Using "company logo" as alt text

`alt="company logo"` is useless — it tells the user nothing about *which* company.

| Context | Alt Text |
|---|---|
| General use | `alt="Acme Corporation"` |
| Brand assets page (where "logo" is relevant) | `alt="Acme Corporation logo"` |

---

## 8. Overly long alt text

Keep alt focused on purpose; put complex information in an accessible longer description. There is no universal uninterruptible-speech or character-limit rule ([WAI complex images](https://www.w3.org/WAI/tutorials/images/complex/)).

**Guidelines:**
- Use concise purpose-focused text; add a long description when the information needs structure.
- For complex images needing longer descriptions, use a long-description technique:
  - Adjacent text in the page
  - `<figcaption>`
  - `aria-describedby` referencing a description element
  - A linked page with the full description

---

## 9. Poor spelling and punctuation

Screen readers interpret text phonetically. Misspelled words may be mispronounced. Missing periods and commas cause text to run together without natural pauses.

---

## 10. SEO keyword stuffing

Cramming keywords into alt text for search engine purposes degrades the experience for screen reader users. Alt text is for humans, not crawlers. Do not use a speculative search-ranking claim to justify image alternatives.
