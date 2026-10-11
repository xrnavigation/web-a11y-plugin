# SVG accessibility patterns

Expose meaningful images with a useful name. Hide decorative graphics. The
[SVG-AAM mapping](https://www.w3.org/TR/svg-aam-1.0/#mapping_additional_nd)
defines name and description sources, including `title`, `desc`, and ARIA
references. It does not guarantee a spoken string in every screen reader.

## Meaningful image with separate description

```html
<svg role="img" aria-labelledby="sales-title" aria-describedby="sales-desc"
     viewBox="0 0 100 100">
  <title id="sales-title">Q3 sales</title>
  <desc id="sales-desc">Sales increased from two million dollars in July
    to three and a half million dollars in September.</desc>
  <path d="M10 90 L50 50 L90 20" fill="none" stroke="currentColor" />
</svg>
```

`role="img"` presents a single graphic; give it an author-provided name
([ARIA img](https://www.w3.org/TR/wai-aria-1.2/#img)). Keep structured data or
long explanations in reachable page content as well, rather than relying on
speech of a flat description ([WAI complex images](https://www.w3.org/WAI/tutorials/images/complex/)).

## Decorative icon inside a named button

```html
<button type="button" aria-label="Search">
  <svg aria-hidden="true" viewBox="0 0 100 100">
    <circle cx="40" cy="40" r="25" fill="none" stroke="currentColor" />
    <path d="M60 60 L90 90" stroke="currentColor" />
  </svg>
</button>
```

This project prefers naming the control directly and hiding its decorative
image. Confirm the resulting button name; do not rely on an untested
SVG name propagation path ([WAI functional images](https://www.w3.org/WAI/tutorials/images/functional/)).

## Verification

Inspect the image/control role, name and description. Test keyboard access
where interactive, actual speech in supported browser/AT versions, and
forced colors for meaningful strokes. Record versions, settings and observed
results; mark unrun checks explicitly. Historic practitioner tests inform a
test plan but do not establish current universal compatibility
([APG production testing](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)).
