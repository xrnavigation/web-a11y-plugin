# Audit mistakes

## A passing command conceals violations

Wrong: run `axe URL` and infer no findings from exit zero.
Right: run `axe URL --exit --stdout`, preserve results and distinguish execution
errors from findings ([axe CLI](https://github.com/dequelabs/axe-core-npm/blob/develop/packages/cli/README.md)).

## A subtree is excluded because another team owns it

Wrong: `.exclude('.third-party-widget')` in every scan, report whole-page success.
Right: retain the full scan; scope any temporary exception to an owned issue and
report the untested subtree. Exclusion skips all its descendants and rules
([Playwright](https://playwright.dev/docs/accessibility-testing)).

## A scan becomes a conformance claim

Wrong: `test('page meets WCAG AA', ...)` with only `violations.length === 0`.
Right: name it `no automatically detected violations in checkout error state`;
record manual and AT checks separately
([Playwright](https://playwright.dev/docs/accessibility-testing)).
