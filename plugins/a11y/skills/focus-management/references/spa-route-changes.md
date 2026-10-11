# Route focus policy

Select a policy for full navigations, hash jumps, back/forward, dialog routes and
background refresh. A meaningful page title is required; live output from changing
it is not assured ([Page titled](https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html)).

One project policy: after a user-requested full route commits, focus its h1 with
`tabindex="-1"`. Preserve focus for background updates. Avoid running the focus
move on initial render or on a stale request. Coordinate any router announcer to
avoid speaking the same heading twice. Focus order must preserve meaning and
operation ([Focus order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html)).

Test loading/error routes, render races, Back/Forward restoration, anchor
navigation, form-submission navigation and persistent skip targets. Record actual
focus, visible context and AT output on the target combinations. Do not prescribe
an assertive region for every route.
