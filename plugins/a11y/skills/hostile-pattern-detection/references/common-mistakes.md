# User-control mistakes and corrections

## Claiming keyboard focus cannot scroll

Wrong: “Tabbing never scrolls, therefore every infinite feed is a keyboard trap.”

Right: “Test whether focus and reading navigation reveal/load reachable results, and whether users can exit the feed. Provide explicit paging/loading when needed.” The APG feed includes focus-driven loading and navigation guidance. ([APG feed](https://www.w3.org/WAI/ARIA/apg/patterns/feed/))

## Auto-rotating content with no user control

```html
<!-- Wrong: controls do not offer a way to pause automatic rotation. -->
<button type="button">Next slide</button>
<!-- Right markup sketch: implement pause/resume and stopped-on-focus behavior. -->
<button type="button">Stop slide rotation</button>
<button type="button">Previous slide</button>
<button type="button">Next slide</button>
```

The markup is a sketch, not a complete carousel. Follow the chosen pattern, keep navigation-control focus, and prevent focus in hidden slides. ([APG carousel](https://www.w3.org/WAI/ARIA/apg/patterns/carousel/))

## Calling an AA target requirement 44px

```css
/* Project preference: a comfortable rectangular target. */
button { min-width: 44px; min-height: 44px; border-radius: 0; }
```

Do not describe this preference as SC 2.5.8's number. AA is 24×24 CSS px or a qualifying exception; 44×44 belongs to the enhanced AAA criterion with its own exceptions. ([Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html))

## Placeholder-as-label repair that only changes color

```html
<!-- Wrong: sufficient contrast alone would not supply a persistent label. -->
<input style="color: #222" placeholder="Email address">
<!-- Right -->
<label for="email">Email address</label>
<input id="email" type="email">
```

Associate a visible label rather than relying on a disappearing hint. ([WAI labels](https://www.w3.org/WAI/tutorials/forms/labels/))

## Treating a vendor guarantee as a test result

Wrong: “This widget guarantees all routes are accessible.”

Right: “Identify the source barriers, fix the components, and report automated/manual task evidence and remaining scope.” ([WAI tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/))
