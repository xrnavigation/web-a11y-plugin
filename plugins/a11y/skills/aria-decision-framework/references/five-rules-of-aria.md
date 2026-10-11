# ARIA authoring principles

The W3C Using ARIA document is an informative authoring guide, not a separate
normative WCAG checklist. Use its principles with ARIA/HTML requirements and
verify the actual interaction ([Using ARIA](https://www.w3.org/TR/using-aria/)).

1. Prefer native HTML with the required semantics and behavior. Example:
   `<button type="button">Save</button>` instead of a click-only div.
2. Avoid unnecessary semantic overrides; check permitted overrides. A native
   button may legitimately gain `role="tab"` for a fully implemented tab widget.
3. Implement keyboard behavior for custom interactive roles. `role="button"`
   does not implement focusability or Enter/Space activation.
4. Keep focusable content available to assistive technology. Negative tabindex
   does not make `aria-hidden` safe for a programmatically focused control.
5. Provide a name for controls using visible text, native labels or supported
   ARIA naming mechanisms.

These authoring principles are explained in
[Using ARIA](https://www.w3.org/TR/using-aria/); permitted HTML overrides are
specified in [ARIA in HTML](https://w3c.github.io/html-aria/).

## Do not equate presentation with hiding

`role="presentation"` removes an element's role semantics under applicable
conditions; it does not remove all descendants or content from the accessibility
tree. User agents ignore presentational roles on focusable elements. In
contrast, `aria-hidden="true"` excludes content from accessibility exposure
without implementing keyboard exclusion
([WAI-ARIA presentation](https://www.w3.org/TR/wai-aria-1.2/#presentation),
[WAI-ARIA aria-hidden](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden)).

```html
<!-- Wrong: can still receive focus programmatically. -->
<button aria-hidden="true" tabindex="-1">Close</button>
<!-- Rendering hidden, or an inert region, excludes interaction appropriately. -->
<button hidden>Close</button>
<div inert><button>Close</button></div>
```

Check supported environments and actual focus behavior
([HTML inert](https://html.spec.whatwg.org/multipage/interaction.html#inert),
[HTML tabindex](https://html.spec.whatwg.org/multipage/interaction.html#the-tabindex-attribute)).
