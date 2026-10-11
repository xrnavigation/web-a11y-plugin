# Focus mistakes

Wrong: always focus h1, change title and send an assertive route announcement.
Right: choose a route policy and test for useful orientation without duplicates.
A title must describe the page; its change is not guaranteed speech
([Page titled](https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html)).

Wrong: close then focus a disconnected trigger.
Right: restore a usable surviving trigger or a logical workflow destination
([APG dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).

Wrong: `aria-hidden="true"` alone disables the page behind a modal.
Right: use native showModal or actual background inertness plus custom focus
lifecycle ([WHATWG inert](https://html.spec.whatwg.org/multipage/interaction.html#the-inert-attribute)).

Wrong: every Undo toast steals focus.
Right: keep a reachable action and status, preserving the user's focus; an
interrupting decision belongs to the dialog pattern
([APG alert](https://www.w3.org/WAI/ARIA/apg/patterns/alert/)).
