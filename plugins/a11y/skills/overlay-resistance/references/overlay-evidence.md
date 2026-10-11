# Overlay evidence and limits

## Project decision

Recommend maintained source/component remediation with automated and manual evaluation. Do not treat an overlay widget, a passing scan, or a vendor guarantee as proof of conformance. WAI explicitly describes evaluation tools as assistance, with human judgment still required. ([WAI evaluation tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/))

## Correct the technical model

Accessibility APIs can reflect runtime changes to names, descriptions, states, relations, and structure. The tree is not frozen before JavaScript executes. A carefully implemented runtime update can improve semantics; adding roles alone does not supply keyboard behavior or establish a working end-to-end task. ([Core AAM, state/property changes](https://www.w3.org/TR/core-aam-1.2/#mapping_events_state-change), [WAI-ARIA author requirements](https://www.w3.org/TR/wai-aria-1.2/#managingfocus_authors))

The project's source-remediation preference concerns maintainability and demonstrated outcomes. It is not based on an impossibility claim about all scripts, all dynamically associated labels, or every third-party control.

## Dated enforcement evidence

The FTC announced its final consent order against accessiBe on **April 22, 2025**. It requires a $1 million payment and bars misleading claims. The announced allegations concerned accessWidget's ability to make all customer websites WCAG-compliant and undisclosed connections in purportedly independent reviews. ([FTC final order announcement](https://www.ftc.gov/news-events/news/press-releases/2025/04/ftc-approves-final-order-requiring-accessibe-pay-1-million))

Keep the parties, date, claims, and procedural outcome attached to the statement. Do not call the case a fine against every overlay company, extrapolate it to unnamed products, or provide a legal guarantee about a specific site.

## Evidence to collect for this application

Use this project comparison matrix before recommending an installation/removal:

| Area | Record |
|---|---|
| Loading | Source configuration, script URL/package, loading condition, error behavior. |
| Semantics | DOM and accessibility inspector observations for affected names, roles, states. |
| Interaction | Keyboard/touch alternatives, focus, cancellation, error and recovery behavior. |
| Content | Human review of image descriptions, labels, media alternatives, and instructions. |
| Dynamic states | Navigation, dialog, validation, loading, permission, and error states. |
| Evaluation scope | Actual browser/AT combinations and checks run; remaining manual coverage. |

Compare observed outcomes with a reproducible task, not with a generic “accessibility score.” No fixed percentage describes all automated tools' coverage. ([WAI evaluation tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/))
