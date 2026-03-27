---
name: alt-text-quality
description: Guides alt text decision-making beyond presence — the W3C decision tree for decorative vs informative vs functional vs complex images, context-dependent descriptions, SVG accessibility, CSS background image alternatives, and icon button labeling. Auto-invokes when adding images, SVGs, icons, or image-based components.
allowed-tools: Read, Glob, Grep
compatibility: "Claude Code, Codex CLI, Gemini CLI"
---

# Alt Text Quality

> "If I removed this image, what information would be lost *in this specific context*?"
> — The answer is the alt text.

The `alt` attribute is required on every `<img>`. But *presence* is not *quality*. A bad alt text is worse than `alt=""` on a decorative image, and `alt=""` on an informative image is an accessibility failure. This skill encodes the W3C decision tree and practitioner-tested patterns for writing correct alt text.

---

## 1. The Decision Tree

Follow from top to bottom. Stop at the first matching branch.

```
START: "I have an image. What alt text does it need?"
  │
  ├─ Q1: Does the image contain text?
  │   │
  │   ├─ Text is also present as real text nearby → alt=""
  │   ├─ Text is only for visual effect → alt=""
  │   ├─ Text functions as icon/symbol → alt describes the FUNCTION
  │   └─ Text is unique, not elsewhere on page → alt contains the SAME TEXT
  │
  ├─ Q2: Is the image used in a link or button?
  │   │
  │   └─ YES → alt describes the DESTINATION or ACTION
  │         Example: logo linking to home → alt="Acme Corp home"
  │
  ├─ Q3: Does the image contribute meaning to the page?
  │   │
  │   ├─ Simple graphic/photo → brief alt describing the MEANING
  │   ├─ Graph/chart/complex data → short alt summary + long description elsewhere
  │   └─ Redundant to adjacent text → alt=""
  │
  ├─ Q4: Is the image purely decorative?
  │   │
  │   └─ YES → alt="" (null alt attribute)
  │
  └─ Q5: None of the above?
      │
      └─ Consult the full W3C Images Tutorial
```

Source: [W3C Alt Text Decision Tree](https://www.w3.org/WAI/tutorials/images/decision-tree/)

For the complete decision tree with examples, see: `${CLAUDE_SKILL_DIR}/references/decision-tree.md`

---

## 2. Context Matters

The same image requires different alt text depending on where it appears. This is the most commonly misunderstood aspect of alt text.

### Example: Photo of Ellen Ochoa

| Context | Alt Text | Why |
|---|---|---|
| Article body, no caption | `alt="Astronaut Ellen Ochoa"` | Provides needed identification |
| With visible caption identifying her | `alt=""` | Caption already provides the info |
| Linked image to her biography | `alt="Astronaut Ellen Ochoa"` | Link needs an accessible name |

### Example: Photo of a building

| Context | Alt Text | Why |
|---|---|---|
| Article about spring weather | `alt="Students lounge in brightly colored chairs in Harvard Yard"` | The *activity* is the point |
| Article about architecture | `alt="Hollis Hall, a red brick building adjacent to Harvard Yard"` | The *building* is the point |

### Example: Company logo

| Context | Alt Text | Why |
|---|---|---|
| Header logo linking to home | `alt="UT Austin home"` | Function (navigation) is the point |
| Brand guidelines page | `alt="The UT Austin logo featuring a shield..."` | Visual description is the point |

**The test:** Ask "If I removed this image, what information would be lost *in this specific context*?" The answer is the alt text.

Sources: [WebAIM Alternative Text](https://webaim.org/techniques/alttext/), [Harvard Digital Accessibility](https://accessibility.huit.harvard.edu/describe-content-images)

---

## 3. SVG Accessibility

SVGs require explicit accessibility markup. Without it, screen readers either ignore them or announce them as unnamed groups.

### Meaningful Inline SVG

```html
<!-- With tooltip (via <title>) -->
<svg role="img" focusable="false" aria-labelledby="svg-title">
  <title id="svg-title">Descriptive name here</title>
  <use xlink:href="#icon-id" aria-hidden="true" />
</svg>

<!-- Without tooltip -->
<svg role="img" aria-label="Descriptive name" focusable="false">
  <use xlink:href="#icon-id" aria-hidden="true"></use>
</svg>
```

Key attributes:
- `role="img"` — ensures announced as "image" across screen readers
- `aria-labelledby` or `aria-label` — provides the accessible name
- `aria-hidden="true"` on `<use>` — prevents redundant announcements
- `focusable="false"` — prevents keyboard focus in IE/old Edge

### Complex SVG (chart/diagram)

```html
<svg role="img" aria-labelledby="chart-title chart-desc">
  <title id="chart-title">Q3 Sales Overview</title>
  <desc id="chart-desc">Bar chart showing sales increasing from $2M in July to $3.5M in September</desc>
</svg>
```

### Decorative SVG

```html
<svg aria-hidden="true" focusable="false">
  <!-- decorative content -->
</svg>
```

### SVG in a Button or Link

The SVG is decorative within the interactive element. The **button** carries the accessible name — never rely on SVG `<title>` or `aria-label` on the SVG for button labeling.

```html
<button>
  <svg aria-hidden="true" focusable="false"><!-- icon --></svg>
  <span class="visually-hidden">Search</span>
</button>
```

**Warning:** SVGs from design tools (Figma, Illustrator, Sketch) often export with `<title>Layer 1</title>` or similar. Remove or replace these.

For the complete SVG pattern reference, see: `${CLAUDE_SKILL_DIR}/references/svg-accessibility.md`

Sources: [Scott O'Hara](https://www.scottohara.me/blog/2019/05/22/contextual-images-svgs-and-a11y.html), [Deque](https://www.deque.com/blog/creating-accessible-svgs/)

---

## 4. CSS Background Images

CSS background images have no `alt` attribute. If a background image conveys meaningful content, provide a text alternative in the markup.

### Technique 1: Separate Element with role="img" (Recommended)

```html
<div>
  <span class="hero-bg" role="img" aria-label="Team celebrating product launch"></span>
  <h1>Our Latest Release</h1>
</div>
```

**Critical:** Never put `role="img"` with `aria-label` on a `<div>` that contains other content — the ARIA name calculation will obscure the inner text from assistive technology.

### Technique 2: Visually Hidden Text

```html
<div class="hero-background">
  <span class="visually-hidden">Description of the background image</span>
  <h1>Visible heading</h1>
</div>
```

### When No Alternative Is Needed

Truly decorative backgrounds (textures, gradients, ambient photography) do not need text alternatives. No markup changes required.

**Best practice:** Do not use CSS background images for meaningful content. Use `<img>` instead.

Sources: [David MacDonald](http://www.davidmacd.com/blog/alternate-text-for-css-background-images.html), [ASU IT Accessibility](https://accessibility.asu.edu/articles/css)

---

## 5. Icon Buttons

Icon-only buttons (no visible text) need an accessible name. The icon itself is always decorative within the button context.

### Technique 1: Visually Hidden Text (Most Robust)

```html
<button>
  <svg aria-hidden="true" focusable="false"><!-- icon --></svg>
  <span class="visually-hidden">Menu</span>
</button>
```

### Technique 2: aria-label on the Button

```html
<button aria-label="Menu">
  <svg aria-hidden="true" focusable="false"><!-- icon --></svg>
</button>
```

Caveats: `aria-label` is not translated by automated translation tools. If visible text exists, `aria-label` must contain it (WCAG 2.5.3 Label in Name).

### Do NOT Label the Icon

```html
<!-- WRONG — fails across browser/screen reader combos -->
<button>
  <svg aria-label="Menu"><!-- icon --></svg>
</button>

<!-- WRONG — also fails -->
<button>
  <svg aria-labelledby="icon-title">
    <title id="icon-title">Menu</title>
  </svg>
</button>
```

The **button** must carry the accessible name. The icon gets `aria-hidden="true"`.

For the complete icon button reference, see: `${CLAUDE_SKILL_DIR}/references/icon-button-patterns.md`

Source: [Sara Soueidan](https://www.sarasoueidan.com/blog/accessible-icon-buttons/)

---

## 6. Anti-Patterns

These are the most common alt text mistakes. Each degrades the screen reader experience.

| Anti-Pattern | Why It's Wrong | Fix |
|---|---|---|
| Starting with "image of", "photo of" | Screen readers already announce "image" — user hears "Image. Image of..." | Drop the prefix. Exception: medium matters (e.g., "Oil painting of..." on an art page) |
| Missing `alt` attribute entirely | Screen reader reads the **filename** aloud ("DSC underscore zero four three seven dot jpeg") | Always include `alt`. Use `alt=""` for decorative images |
| Filename as alt text | `alt="IMG_0437.jpg"` provides no information | Describe the content or use `alt=""` |
| Describing decorative images | Forces users to listen to irrelevant content | Use `alt=""` for decorative images |
| Duplicating caption in alt | Screen reader reads the same information twice | Use `alt=""` when a `<figcaption>` provides the description |
| Describing appearance instead of purpose | Photo used for a news story gets "Woman in blue suit" instead of "Senator Jane Doe" | Match alt text to the image's purpose in context |
| "company logo" as alt text | Useless — use the company name | `alt="Acme Corporation"` |
| Overly long alt text | Read as one uninterruptible string; aim for under 150 characters | Use long-description techniques for complex images |
| SEO keyword stuffing | Degrades experience for screen reader users | Alt text is for humans, not crawlers |

For the complete anti-patterns reference with examples, see: `${CLAUDE_SKILL_DIR}/references/common-mistakes.md`

Sources: [BOIA](https://www.boia.org/blog/8-common-image-alt-text-mistakes-to-stop-making), [WebAIM](https://webaim.org/techniques/alttext/), [Allyant](https://allyant.com/blog/6-common-alt-text-mistakes-and-best-practices/)

---

## 7. Cross-References

For related accessibility patterns, see these companion skills:

- `aria-decision-framework` — when to use ARIA vs native HTML; the five rules of ARIA
- `form-a11y` — form labeling, error messages, and field descriptions
- `css-a11y` — visually-hidden class, focus indicators, and high contrast mode

For detailed reference material:

- `${CLAUDE_SKILL_DIR}/references/decision-tree.md` — complete W3C decision tree with examples
- `${CLAUDE_SKILL_DIR}/references/svg-accessibility.md` — all SVG patterns with testing notes
- `${CLAUDE_SKILL_DIR}/references/icon-button-patterns.md` — icon button labeling techniques
- `${CLAUDE_SKILL_DIR}/references/common-mistakes.md` — anti-patterns with citations
- `${CLAUDE_SKILL_DIR}/references/sources.yaml` — provenance for all cited sources
