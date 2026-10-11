# CSS mistakes

Wrong: `*:focus { outline: none; }`.
Right: retain the native ring or test a visible outline such as
`.control:focus { outline: 3px solid #005fcc; }` in each theme
([Focus visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)).

Wrong: transparent outline alone is the visible focus fix in ordinary colors.
Right: provide a visible normal-color indicator and forced-color fallback
([MDN forced-colors](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors)).

Wrong: every AA focus ring must meet AAA 2.4.13 perimeter rules.
Right: apply 2.4.7 AA and applicable 1.4.11 AA; label 2.4.13 AAA separately
([WCAG 2.2](https://www.w3.org/TR/WCAG22/)).

Wrong: reduce touch hit areas when `any-pointer:fine` matches.
Right: account for hybrid input; test target sizes and spacing directly
([MDN any-pointer](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/any-pointer),
[Target minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)).

Wrong: reduce-motion CSS is treated as the pause mechanism for all animation.
Right: reduce decorative motion, retain status and evaluate actual pause/stop/hide
conditions ([Pause Stop Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)).
