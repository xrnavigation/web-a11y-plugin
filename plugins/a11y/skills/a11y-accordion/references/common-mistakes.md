# Accordion mistakes

Wrong: reject adjacent details because they have no role=group.
Right: use native disclosures or the chosen accordion structure; add a named
wrapper only when useful. APG does not mandate a group wrapper
([APG accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)).

Wrong: prohibit panel regions whenever six panels exist.
Right: consider how many can be expanded simultaneously and whether region
landmarks aid navigation. APG's approximate count is authoring guidance
([APG accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)).

Wrong: `<div role="region" aria-labelledby="...">Answer</div>`.
Right: reference an existing useful trigger ID, or omit the optional region role
([APG accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)).

Wrong: updating only aria-expanded leaves closed controls operable.
Right: synchronize the actual panel visibility and state; native details supplies
basic disclosure behavior
([WHATWG details](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element)).

Wrong: assume a 2019 screen reader report describes every current summary.
Right: test heading navigation and state information on the support matrix
([APG testing](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)).
