# Low-vision layout verification

Test text enlargement to 200% separately from 320 CSS pixel width reflow for
vertical content (256 CSS pixel height for horizontal content). Document any
essential two-dimensional section exception and verify surrounding text still
reflows. Check modal/error states and sticky controls as well as the initial view
([Resize text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html),
[Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)).

Override line height 1.5, paragraph spacing 2, letter spacing .12 and word spacing
.16 times font size, without losing information or operation
([Text spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)).
Record browser zoom, CSS viewport, content state and observed barriers. A viewport
screenshot is useful evidence for that layout; it does not establish speech output
or every browser-zoom behavior. See `zoom-reflow` for the full matrix.
