# Tool invocation recipes

Inspect local package versions and command help before adapting these recipes.
Record scope, options, tool failures and artifacts with each result.

## axe CLI

```sh
npx --no-install axe https://example.com --exit --stdout
npx --no-install axe https://example.com --exit --save report.json --dir ./results
```

Use `--exit` for violation-based process failure; `--stdout` emits JSON. Wait for
an explicit application-ready state through an interaction harness when possible;
a fixed delay is not proof of readiness
([axe CLI](https://github.com/dequelabs/axe-core-npm/blob/develop/packages/cli/README.md)).

## pa11y

```sh
npx --no-install pa11y https://example.com --reporter json
npx --no-install pa11y-ci --config .pa11yci
```

Use the repository's installed runners and config. Read each tool's exit-code and
threshold policy. A threshold permits findings and is not a conformance level
([pa11y](https://github.com/pa11y/pa11y), [pa11y-ci](https://github.com/pa11y/pa11y-ci)).

## Lighthouse and JSX lint

```sh
npx --no-install lighthouse https://example.com --only-categories=accessibility --output=json --output-path=./lighthouse.json
npx --no-install eslint .
```

Use existing JSX lint configuration rather than replacing it. Static JSX checks
cannot evaluate the whole rendered application
([jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y)).
A Lighthouse score represents its own weighted audit set
([Chrome scoring](https://developer.chrome.com/docs/lighthouse/accessibility/scoring)).
