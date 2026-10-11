# Modal focus lifecycle

Prefer an existing tested dialog component or native modal. showModal makes
background content inert; show is modeless. Native modal behavior comes from HTML,
while APG describes the expected widget interaction
([WHATWG dialog](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element),
[APG modal](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)).

For a custom modal, verify:

1. A useful initial destination for content length and action risk.
2. Forward/reverse traversal within the current modal controls.
3. Background pointer, keyboard and AT navigation blocked appropriately.
4. Operable close and Escape behavior consistent with the selected pattern.
5. Usable trigger restoration or logical fallback when the trigger is removed.
6. Long content and focus visibility at zoom, with sticky controls.

Do not apply inert to an ancestor containing a custom modal, or expect aria-modal
alone to block interaction. A static CSS selector omits dynamic/hidden controls,
radio behavior, disabled fieldsets and shadow DOM; it is not a complete trap
([WHATWG inert](https://html.spec.whatwg.org/multipage/interaction.html#the-inert-attribute)).

Record actual focus and observed AT output; APG examples require support testing
([APG read me first](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)).
