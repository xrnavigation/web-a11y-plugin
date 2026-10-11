# Tab mistakes

## Neutral wrapper called invalid

```html
<!-- Valid descendant ownership; add panel relationships and behavior. -->
<div role="tablist" aria-label="Sections">
  <div><button role="tab" aria-selected="true">Overview</button></div>
</div>
```

A tablist can own descendant tabs; direct DOM children are not universally
required. Inspect the accessibility-tree relationship rather than rejecting
neutral layout wrappers ([WAI-ARIA tablist](https://www.w3.org/TR/wai-aria-1.2/#tablist)).

## Nested control inside a tab

Wrong: `<button role="tab">Settings <button>Close</button></button>`.
Right: use one focusable tab element and design deletion with a supported
keyboard action or a separate control. Do not assume an interactive descendant
is safely erased by presentational child semantics
([APG tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/),
[ARIA in HTML](https://w3c.github.io/html-aria/)).

## Focus and selection conflated in manual mode

Wrong: leave the selected tab as the only Tab stop even after arrows focus a
different tab. Right: move the roving Tab stop with focus; update selection only
on Enter/Space in manual activation
([APG tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)).

## Focusable content hidden only from AT

```html
<!-- Wrong: link can remain visible and focusable. -->
<div role="tabpanel" aria-hidden="true"><a href="/details">Details</a></div>
<!-- Right inactive panel visibility. -->
<div role="tabpanel" hidden><a href="/details">Details</a></div>
```

`aria-hidden` does not hide rendering or implement keyboard focus exclusion
([WAI-ARIA aria-hidden](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden),
[HTML hidden](https://html.spec.whatwg.org/multipage/interaction.html#the-hidden-attribute)).

## Panel focus forced on every arrow

Wrong: automatically move focus into a panel after arrowing to a tab.
Right: keep focus on the tab and make the panel reachable using Tab; choose
manual activation when panel display has noticeable delay
([APG tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)).
