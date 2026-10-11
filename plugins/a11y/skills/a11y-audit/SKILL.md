---
name: a11y-audit
description: Runs and interprets automated web accessibility checks with axe, Playwright, pa11y, Lighthouse, or JSX linting. Use when scanning a URL, rendered component state, or codebase; reports bounded findings and manual follow-up.
argument-hint: "[url-or-path] [--tool axe|pa11y|lighthouse|eslint]"
context: fork
allowed-tools: Read, Glob, Grep, Bash
---

# Automated accessibility audit

Audit the requested journey and rendered states. Report the evidence and tested
scope. Automated checks find some barriers; a clean scan does not establish WCAG
conformance ([Playwright accessibility testing](https://playwright.dev/docs/accessibility-testing)).

## Choose and prepare

1. Read the repository's test helpers, dependencies, scripts and browser setup.
   Reuse its pinned tools; record versions. Avoid introducing a second browser
   harness for an existing suite.
2. Identify URLs, authentication state, viewport, component states and the requested
   WCAG version/level. Include opened menus, validation failures, loading and
   empty states; axe scans the state present at analysis time
   ([Playwright](https://playwright.dev/docs/accessibility-testing)).
3. Use JSX lint for source, axe/Playwright for rendered interaction states, and
   pa11y for URL sweeps. Lighthouse's accessibility score describes its weighted
   audits rather than conformance
   ([Lighthouse scoring](https://developer.chrome.com/docs/lighthouse/accessibility/scoring)).

## Run a bounded scan

With an existing project installation of `@axe-core/cli`:

```sh
npx --no-install axe https://example.com --exit --stdout
```

`--exit` makes rule failures return a failing process status. Without it, do not
interpret exit zero as zero violations. Distinguish tool/browser/network errors
from findings; retain stdout and stderr
([axe CLI](https://github.com/dequelabs/axe-core-npm/blob/develop/packages/cli/README.md)).

For interaction coverage in an existing Playwright suite:

```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('checkout has no detected violations in its error state', async ({ page }, testInfo) => {
  await page.goto('/checkout'); // Requires the project's configured baseURL.
  await page.getByRole('button', { name: 'Place order' }).click();
  await expect(page.getByRole('heading', { name: 'Check your details' })).toBeVisible();
  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'])
    .analyze();
  await testInfo.attach('axe-results', {
    body: JSON.stringify(results, null, 2), contentType: 'application/json'
  });
  expect(results.violations).toEqual([]);
});
```

Verify tag availability in the installed axe version. Tags select rules, not
severity or complete criterion coverage
([axe API](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md),
[Playwright](https://playwright.dev/docs/accessibility-testing)).

## Interpret and remediate

- Preserve `violations`, `incomplete`, `passes` and `inapplicable`. Investigate
  `incomplete` results manually; do not count them as passing
  ([axe API](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md)).
- Report rule ID, affected targets, rendered state, rule help URL, user impact,
  proposed fix and retest. Tool impact is a triage input; agree release policy
  with the project rather than treating it as a WCAG severity scheme.
- Separate WCAG-tagged rules from tool best practices. For example, a heading
  order warning alone does not prove a particular WCAG failure
  ([Playwright](https://playwright.dev/docs/accessibility-testing)).
- Keep third-party UI in scope when users encounter it. An exclusion suppresses
  all rules for the subtree. Record any approved exception with an issue, owner,
  scope and review date; retain the original result. Prefer narrow fingerprints
  over blanket rule suppression or count thresholds
  ([Playwright known issues](https://playwright.dev/docs/accessibility-testing)).
- Retest the same state after repair and its adjacent states. Do not remove a rule
  merely to obtain a green result.

## Report and completion

Return a report containing target/revision, environment/tool versions, states,
commands, findings, incomplete checks, exclusions and evidence artifact paths.
Identify checks not run and why. Summarize keyboard, screen reader, zoom/reflow,
pointer and media follow-up from `testing-strategy`; do not invent an automation
coverage percentage or assert that an untested page is accessible
([WAI evaluation](https://www.w3.org/WAI/test-evaluate/)).

Read [common mistakes](references/common-mistakes.md),
[tool recipes](references/tool-invocation-recipes.md),
[Playwright integration](references/playwright-integration.md),
[fix examples](references/top-violations.md), and
[source registry](references/sources.yaml) as needed.
