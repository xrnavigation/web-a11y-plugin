# Tool Invocation Recipes

Complete CLI commands and configuration for each accessibility audit tool.

---

## axe-core CLI

### Install

```bash
npm install -g @axe-core/cli
# or per-project
npm install --save-dev @axe-core/cli
```

### Commands

```bash
# Basic scan
axe https://example.com

# Multiple URLs
axe https://example.com https://example.com/about https://example.com/contact

# WCAG 2.1 AA only
axe https://example.com --tags wcag2a,wcag2aa,wcag21a,wcag21aa

# WCAG 2.2 AA
axe https://example.com --tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa

# Best practices (not WCAG-required but recommended)
axe https://example.com --tags best-practice

# Run specific rules only
axe https://example.com --rules color-contrast,image-alt,label

# Disable specific rules
axe https://example.com --disable color-contrast

# JSON to stdout
axe https://example.com --stdout

# JSON to file
axe https://example.com --save report.json --dir ./results

# Verbose with timing
axe https://example.com --verbose --timer
```

### Key Flags

| Flag | Purpose |
|---|---|
| `--tags <tags>` | Run rules matching tags (e.g., `wcag2a`, `wcag2aa`, `best-practice`) |
| `--rules <rules>` | Run only specific rules by ID |
| `--disable <rules>` | Disable specific rules |
| `--save <filename>` | Save JSON results to file |
| `--dir <path>` | Directory for saved results |
| `--stdout` | Output JSON to stdout, silence other logs |
| `--verbose` / `-v` | Show tool name, version, environment |
| `--timer` | Log page load and scan duration |
| `--browser` | Choose browser (default: chromium) |

### Exit Codes

- **0**: No violations
- **1**: Violations found or error

### JSON Output Structure

```json
{
  "violations": [
    {
      "id": "color-contrast",
      "impact": "serious",
      "tags": ["wcag2aa", "wcag143"],
      "description": "Ensures the contrast between foreground and background colors meets WCAG 2 AA thresholds",
      "help": "Elements must have sufficient color contrast",
      "helpUrl": "https://dequeuniversity.com/rules/axe/4.x/color-contrast",
      "nodes": [
        {
          "html": "<p style=\"color: #aaa\">Low contrast</p>",
          "target": ["p"],
          "failureSummary": "Fix any of the following: ..."
        }
      ]
    }
  ],
  "passes": [],
  "incomplete": [],
  "inapplicable": []
}
```

### Parsing Results

```bash
# Count violations by impact
axe https://example.com --stdout | jq '[.[] | .violations[] | .impact] | group_by(.) | map({(.[0]): length}) | add'

# List violation rule IDs with element counts
axe https://example.com --stdout | jq '[.[] | .violations[] | {id: .id, count: (.nodes | length)}]'

# Get just critical/serious violations
axe https://example.com --stdout | jq '[.[] | .violations[] | select(.impact == "critical" or .impact == "serious")]'

# Extract HTML snippets of failures
axe https://example.com --stdout | jq '[.[] | .violations[] | .nodes[] | .html]'
```

---

## pa11y

### Install

```bash
npm install -g pa11y
```

Requires Node.js 20, 22, or 24.

### Commands

```bash
# Basic scan (htmlcs runner, WCAG2AA)
pa11y https://example.com

# Use axe runner
pa11y https://example.com --runner axe

# Use both runners
pa11y https://example.com --runner axe --runner htmlcs

# Set WCAG standard (htmlcs only)
pa11y https://example.com --standard WCAG2AAA

# JSON output
pa11y https://example.com --reporter json

# CSV output
pa11y https://example.com --reporter csv > report.csv

# HTML report
pa11y https://example.com --reporter html > report.html

# Allow N issues before failing
pa11y https://example.com --threshold 10

# Fail on warnings too (default: error only)
pa11y https://example.com --level warning

# Ignore specific rules
pa11y https://example.com --ignore "WCAG2AA.Principle1.Guideline1_1.1_1_1.H30.2"

# Scan specific page section
pa11y https://example.com --root-element "#main-content"

# Hide elements from scan
pa11y https://example.com --hide-elements ".cookie-banner,.ad-overlay"

# Timeout and wait
pa11y https://example.com --timeout 30000 --wait 2000
```

### Runners

| Runner | Coverage | WCAG AAA | Notes |
|---|---|---|---|
| `htmlcs` (default) | Broader rule set | Yes | HTML_CodeSniffer engine |
| `axe` | Industry standard | No | Deque axe-core engine |

### Exit Codes

- **0**: No errors (or below threshold)
- **1**: Technical failure
- **2**: Accessibility issues found (above threshold)

### Config File (pa11y.json)

```json
{
  "runner": ["axe"],
  "standard": "WCAG2AA",
  "level": "error",
  "threshold": 0,
  "timeout": 30000,
  "ignore": [],
  "hideElements": ".cookie-banner"
}
```

---

## pa11y-ci

### Install

```bash
npm install -g pa11y-ci
```

### Config File (.pa11yci)

```json
{
  "defaults": {
    "timeout": 10000,
    "concurrency": 2,
    "runners": ["axe"],
    "reporters": [
      "cli",
      ["json", { "fileName": "./a11y-results.json" }]
    ]
  },
  "urls": [
    "https://example.com/",
    "https://example.com/about",
    {
      "url": "https://example.com/login",
      "timeout": 50000,
      "actions": [
        "wait for element #login-form to be visible"
      ]
    }
  ]
}
```

### Commands

```bash
# Run from config
pa11y-ci

# Custom config path
pa11y-ci --config ./my-config.json

# JSON output
pa11y-ci --json

# Allow N errors total
pa11y-ci --threshold 5

# Sitemap-based testing
pa11y-ci --sitemap https://example.com/sitemap.xml

# Sitemap with URL rewriting (prod -> staging)
pa11y-ci --sitemap https://example.com/sitemap.xml \
  --sitemap-find example.com --sitemap-replace localhost:3000

# Exclude URLs from sitemap
pa11y-ci --sitemap https://example.com/sitemap.xml \
  --sitemap-exclude "admin|private"
```

---

## Lighthouse

### Install

```bash
npm install -g lighthouse
```

Requires Chrome/Chromium installed.

### Commands

```bash
# Accessibility-only audit, JSON output, headless
lighthouse https://example.com \
  --only-categories=accessibility \
  --output=json \
  --output-path=./a11y-report.json \
  --chrome-flags="--headless"

# HTML report
lighthouse https://example.com \
  --only-categories=accessibility \
  --output=html \
  --output-path=./a11y-report.html \
  --chrome-flags="--headless"

# Multiple output formats
lighthouse https://example.com \
  --only-categories=accessibility \
  --output=json,html \
  --chrome-flags="--headless"

# Desktop viewport (default is mobile)
lighthouse https://example.com \
  --only-categories=accessibility \
  --preset=desktop \
  --output=json \
  --chrome-flags="--headless"

# Quiet mode
lighthouse https://example.com \
  --only-categories=accessibility \
  --output=json \
  --quiet \
  --chrome-flags="--headless"
```

### Key Flags

| Flag | Purpose |
|---|---|
| `--only-categories=accessibility` | Run only a11y audits |
| `--output=json` | Output format: `json`, `html`, `csv` |
| `--output-path=<path>` | Where to write the report |
| `--chrome-flags="--headless"` | Run headless Chrome |
| `--quiet` | Suppress log output |
| `--preset=desktop` | Desktop viewport (default is mobile) |

Lighthouse produces a 0-100 accessibility score and uses axe-core internally.

---

## eslint-plugin-jsx-a11y

### Install

```bash
npm install --save-dev eslint-plugin-jsx-a11y
```

### Flat Config (ESLint 9+, recommended)

```javascript
// eslint.config.js
import jsxA11y from 'eslint-plugin-jsx-a11y';

export default [
  jsxA11y.flatConfigs.recommended,
  // or jsxA11y.flatConfigs.strict for thorough audits
];
```

### Legacy Config (.eslintrc)

```json
{
  "plugins": ["jsx-a11y"],
  "extends": ["plugin:jsx-a11y/recommended"]
}
```

### Recommended vs Strict

| Aspect | Recommended | Strict |
|---|---|---|
| Scope | Essential violations | Comprehensive coverage |
| False positives | Fewer | More |
| Use case | Production CI gating | Thorough audits, new projects |

### Custom Component Mapping

```json
{
  "settings": {
    "jsx-a11y": {
      "polymorphicPropName": "as",
      "components": {
        "CustomButton": "button",
        "CustomImage": "img",
        "CustomInput": "input"
      }
    }
  }
}
```

### Key Rules

| Rule | What It Catches |
|---|---|
| `alt-text` | Images/media missing alt text |
| `anchor-has-content` | Empty `<a>` elements |
| `anchor-is-valid` | Invalid href on `<a>` |
| `aria-proptypes` | Invalid ARIA property values |
| `aria-role` | Invalid ARIA roles |
| `click-events-have-key-events` | onClick without keyboard handler |
| `heading-has-content` | Empty heading elements |
| `interactive-supports-focus` | Interactive elements not focusable |
| `label-has-associated-control` | Labels not linked to inputs |
| `no-autofocus` | Use of autoFocus attribute |
| `no-noninteractive-element-interactions` | Events on non-interactive elements |
| `no-static-element-interactions` | Events on `<div>`, `<span>` |
| `role-has-required-aria-props` | Roles missing required ARIA attributes |
| `tabindex-no-positive` | Positive tabindex values |

### Run

```bash
# Scan all JSX/TSX files
npx eslint --ext .jsx,.tsx src/

# Fix auto-fixable issues
npx eslint --ext .jsx,.tsx src/ --fix

# JSON output
npx eslint --ext .jsx,.tsx src/ -f json > eslint-a11y.json
```
