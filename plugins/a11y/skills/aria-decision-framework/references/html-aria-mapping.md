# HTML semantics and ARIA overrides

Use this as a starting map, not a replacement for the element-specific allowed
role and attribute tables. Conditions matter: labels, ancestor context, select
size/multiple and input type can change semantics
([ARIA in HTML](https://w3c.github.io/html-aria/)).

| HTML | Usual implicit role / condition |
|---|---|
| button | button |
| a with href | link |
| input type checkbox / radio | checkbox / radio |
| input type range / number | slider / spinbutton |
| input type text without list | textbox |
| input type text with list | combobox |
| textarea | textbox |
| select without multiple; size absent or at most 1 | combobox |
| select with multiple or size > 1 | listbox |
| option | option |
| nav / main / aside | navigation / main / complementary |
| header / footer outside specified sectioning ancestors | banner / contentinfo |
| section with accessible name | region |
| section without accessible name | generic |
| form with accessible name | form |
| dialog | dialog |
| table | table (grid override is permitted) |
| tr / tbody / thead / tfoot | row / rowgroup |
| td | cell; gridcell under grid |
| th | header/cell according to context |
| ul / ol / menu | list |
| li | listitem in list context |
| progress / output | progressbar / status |
| div / span | generic in ordinary context |

These mappings and contextual restrictions are defined by
[ARIA in HTML](https://w3c.github.io/html-aria/).

## Check overrides individually

Omit redundant roles by default, such as `<button role="button">`. An explicitly
permitted override is different: `<button role="tab">` can implement a tab,
and `<table role="grid">` can implement a data grid. Do not infer that every
role is allowed wherever one override is allowed
([ARIA in HTML](https://w3c.github.io/html-aria/),
[APG grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)).

Do not add unsupported names or states to generic roles. Verify actual name,
role, state and ownership after CSS or JavaScript changes; specification
semantics alone do not prove behavior across target combinations.
