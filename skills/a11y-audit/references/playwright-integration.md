# Playwright + axe-core Integration

Patterns for integrating accessibility testing into Playwright E2E test suites.

---

## Install

```bash
npm install --save-dev @axe-core/playwright
```

---

## Full Page Scan

```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('page has no accessibility violations', async ({ page }) => {
  await page.goto('https://example.com');

  const results = await new AxeBuilder({ page }).analyze();

  expect(results.violations).toEqual([]);
});
```

---

## WCAG Level Filtering

```typescript
test('page meets WCAG 2.1 AA', async ({ page }) => {
  await page.goto('https://example.com');

  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
    .analyze();

  expect(results.violations).toEqual([]);
});
```

---

## Targeted Scan (include/exclude)

```typescript
test('main content is accessible', async ({ page }) => {
  await page.goto('https://example.com');

  const results = await new AxeBuilder({ page })
    .include('#main-content')
    .exclude('.known-issue-component')
    .exclude('.third-party-widget')
    .analyze();

  expect(results.violations).toEqual([]);
});
```

---

## Disabling Specific Rules

```typescript
test('page accessible (ignoring color contrast)', async ({ page }) => {
  await page.goto('https://example.com');

  const results = await new AxeBuilder({ page })
    .disableRules(['color-contrast'])
    .analyze();

  expect(results.violations).toEqual([]);
});
```

---

## Reusable Test Fixture

Create a shared fixture so all tests use consistent configuration:

```typescript
// a11y-fixtures.ts
import { test as base } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

type A11yFixtures = {
  makeAxeBuilder: () => AxeBuilder;
};

export const test = base.extend<A11yFixtures>({
  makeAxeBuilder: async ({ page }, use) => {
    await use(() =>
      new AxeBuilder({ page })
        .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
        .exclude('.third-party-widget')
    );
  },
});

export { expect } from '@playwright/test';
```

Usage:

```typescript
// my-page.spec.ts
import { test, expect } from './a11y-fixtures';

test('homepage is accessible', async ({ page, makeAxeBuilder }) => {
  await page.goto('/');
  const results = await makeAxeBuilder().analyze();
  expect(results.violations).toEqual([]);
});

test('about page is accessible', async ({ page, makeAxeBuilder }) => {
  await page.goto('/about');
  const results = await makeAxeBuilder().analyze();
  expect(results.violations).toEqual([]);
});
```

---

## Attaching Results for Debugging

Attach scan results to the Playwright test report for post-run analysis:

```typescript
test('a11y audit with attached results', async ({ page }, testInfo) => {
  await page.goto('https://example.com');

  const results = await new AxeBuilder({ page }).analyze();

  await testInfo.attach('a11y-results', {
    body: JSON.stringify(results, null, 2),
    contentType: 'application/json',
  });

  expect(results.violations).toEqual([]);
});
```

---

## Scanning After Interaction

For SPAs and dynamic content, scan after the page reaches the desired state:

```typescript
test('modal dialog is accessible', async ({ page }) => {
  await page.goto('/');
  await page.click('button#open-settings');
  await page.waitForSelector('[role="dialog"]');

  const results = await new AxeBuilder({ page })
    .include('[role="dialog"]')
    .analyze();

  expect(results.violations).toEqual([]);
});
```

---

## Scanning Multiple States

Test accessibility across different component states:

```typescript
test('form accessibility across states', async ({ page }) => {
  await page.goto('/register');

  // Empty form state
  const emptyResults = await new AxeBuilder({ page })
    .include('form')
    .analyze();
  expect(emptyResults.violations).toEqual([]);

  // Validation error state
  await page.click('button[type="submit"]');
  await page.waitForSelector('.error-message');

  const errorResults = await new AxeBuilder({ page })
    .include('form')
    .analyze();
  expect(errorResults.violations).toEqual([]);
});
```

---

## CI Configuration

### Playwright config for a11y tests

```typescript
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests/a11y',
  use: {
    baseURL: 'http://localhost:3000',
  },
  webServer: {
    command: 'npm start',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
});
```

### Run a11y tests separately

```bash
npx playwright test --config playwright.a11y.config.ts
```
