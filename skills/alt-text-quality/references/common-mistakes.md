# Common Alt Text Mistakes

Sources: [BOIA](https://www.boia.org/blog/8-common-image-alt-text-mistakes-to-stop-making), [WebAIM](https://webaim.org/techniques/alttext/), [Allyant](https://allyant.com/blog/6-common-alt-text-mistakes-and-best-practices/)

---

## 1. Starting with "image of", "photo of", "graphic of"

Screen readers already announce the element as "image" or "graphic." Adding these words creates redundancy — the user hears: "Image. Image of a sunset."

**Exception:** The image *type* is relevant when the medium matters:
- "Oil painting of..." on an art history page
- "Screenshot of..." in a UI walkthrough
- "X-ray showing..." in a medical context

---

## 2. Missing alt attribute entirely

Without any `alt` attribute, screen readers read the **filename** aloud. The user hears something like "DSC underscore zero four three seven dot jpeg." This is worse than no image at all.

**Rule:** Always include `alt`. Use `alt=""` for decorative images. Never omit the attribute.

---

## 3. Using the filename as alt text

`alt="IMG_0437.jpg"` or `alt="hero-banner-v2-final.png"` provides no useful information. It is functionally equivalent to having no alt text.

---

## 4. Adding alt text to decorative images

Decorative images (borders, spacers, ambient backgrounds, ornamental flourishes) should have `alt=""`. Describing them forces screen reader users to listen to irrelevant content, creating noise that slows navigation.

---

## 5. Duplicating caption text in alt

When an image has a visible caption (e.g., in a `<figcaption>`), use `alt=""` to avoid the screen reader reading the same information twice. The caption already serves as the description.

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

Screen readers read alt text as a single uninterruptible string. Long descriptions are exhausting to listen to and cannot be skimmed.

**Guidelines:**
- Aim for under 150 characters
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

Cramming keywords into alt text for search engine purposes degrades the experience for screen reader users. Alt text is for humans, not crawlers. Search engines also penalize keyword-stuffed alt text.
