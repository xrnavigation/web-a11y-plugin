# Playwright scan integration

Reuse the project's existing fixtures and baseURL. Scan the actual state after an
explicit readiness assertion, retaining full results. These samples detect rules
in tested states; they do not establish WCAG conformance
([Playwright](https://playwright.dev/docs/accessibility-testing)).

```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('open settings has no detected axe violations', async ({ page }, testInfo) => {
  await page.goto('/');
  await page.getByRole('button', { name: 'Settings', exact: true }).click();
  await expect(page.getByRole('dialog', { name: 'Settings', exact: true })).toBeVisible();
  const results = await new AxeBuilder({ page }).analyze();
  await testInfo.attach('axe-settings', {
    body: JSON.stringify(results, null, 2), contentType: 'application/json'
  });
  expect(results.violations).toEqual([]);
});
```

Extend the repository's actual test harness for keyboard entry, containment,
close and restoration. Report screen reader checks separately; DOM assertions do
not establish speech output
([Playwright](https://playwright.dev/docs/accessibility-testing)).

## Scope and known issues

Use include for an intentionally component-scoped scan, and name its scope in the
report. Exclude suppresses every rule for the subtree: an excluded third-party
widget or known defect remains unverified. Prefer stable fingerprints with an
owned issue/review date rather than blanket exclusions or full result snapshots
([Playwright known issues](https://playwright.dev/docs/accessibility-testing)).

## Rule tags

Choose supported rule tags from the installed axe version for the requested WCAG
version/level. Tags are not impact filtering, and best-practice rules are not
criteria. Retain incomplete/manual-review results as well as violations
([axe API](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md)).
