# Detecting and reviewing overlay integration

These are project investigation heuristics, not vendor attestations or evidence that a specific website is inaccessible. Confirm behavior in the actual application before changing dependencies.

## Source inspection

Search scripts, lockfiles, configuration, and templates for the product name the user identified. Inspect where the code is loaded, which settings it applies, and whether it claims automated conformance. A third-party CDN or floating accessibility icon alone does not establish the product category.

```powershell
# Start from the repository's actual file list and relevant app directory.
rg --files src public
rg -n -i 'accessibe|accesswidget|userway|audioeye|accessibility.widget' src public
```

Do not print secret configuration or headers. Treat each result as a lead: read the caller, dependency metadata, and deployment condition.

## Runtime comparison

When browser testing is authorized and available, record DOM/accessibility inspector observations and complete task outcomes with the integration enabled and with a controlled local comparison. Re-run affected keyboard, zoom, validation, and supported screen-reader flows. Do not infer runtime behavior solely from a class name.

Accessibility APIs support runtime semantic updates; the question is whether this implementation preserves correct state and behavior. ([Core AAM change events](https://www.w3.org/TR/core-aam-1.2/#mapping_events_state-change))

## Action and report

Identify the source component owning each barrier. Implement and test durable fixes within the authorized scope; propose removal/replacement alongside its verified effects. Preserve useful explicit preferences rather than removing every customization feature indiscriminately.

Report:

```text
Integration location and observed purpose:
Task/barrier and reproduction:
Source remediation and controlled comparison:
Browser/AT checks executed:
Checks not run and remaining uncertainty:
```

Automated evidence assists evaluation; it cannot determine accessibility by itself. ([WAI evaluation tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/))
