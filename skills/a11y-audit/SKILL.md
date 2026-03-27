---
name: a11y-audit
description: Runs automated accessibility scans with axe-core, pa11y, Lighthouse, or eslint-plugin-jsx-a11y. Interprets results, prioritizes violations, and generates fix recommendations. Use when asked to audit, scan, or check accessibility of a page, component, or codebase.
argument-hint: "[url-or-path] [--tool axe|pa11y|lighthouse|eslint]"
context: fork
allowed-tools: Read, Glob, Grep, Bash
compatibility: "Claude Code, Codex CLI, Gemini CLI"
---

# Accessibility Audit

Run automated accessibility scans, interpret results, prioritize violations, and generate actionable fix recommendations.

**Important:** Automated tools catch 30-50% of WCAG violations. Always recommend manual testing for complete coverage — keyboard navigation, screen reader testing, and cognitive review cannot be automated.

---

## 1. Tool Selection Guide

Pick the right tool for the situation:

| Situation | Tool | Why |
|---|---|---|
| Quick audit of a URL | `@axe-core/cli` | Fast, reliable, JSON output, exit code for CI |
| Single page with custom config | `pa11y` | Flexible runners, threshold control, multiple output formats |
| Multi-page CI sweep | `pa11y-ci` | Sitemap support, concurrent scanning, CI-native |
| Accessibility score tracking | `lighthouse` | 0-100 score, trend tracking, holistic view |
| Static analysis of JSX/React | `eslint-plugin-jsx-a11y` | Catches issues at build time, no browser needed |
| E2E test integration | `@axe-core/playwright` | Component-level, state-aware, part of test suite |
| Maximum coverage | Combine eslint (static) + axe/playwright (runtime) + pa11y-ci (sweep) | Layers catch different issue types |

**Default recommendation:** Start with `@axe-core/cli` for URL audits, `eslint-plugin-jsx-a11y` for codebases.

---

## 2. Quick Start — axe-core CLI

### Install

```bash
npm install -g @axe-core/cli
# or per-project
npm install --save-dev @axe-core/cli
```

### Run a Scan

```bash
# Basic scan — human-readable output
axe https://example.com

# WCAG 2.1 AA compliance check
axe https://example.com --tags wcag2a,wcag2aa,wcag21a,wcag21aa

# JSON output to stdout (for parsing)
axe https://example.com --stdout

# JSON output to file
axe https://example.com --save report.json --dir ./results

# Multiple URLs
axe https://example.com https://example.com/about https://example.com/contact

# Scan specific rules only
axe https://example.com --rules color-contrast,image-alt,label

# Disable noisy rules
axe https://example.com --disable color-contrast
```

### Exit Codes

- **0** — No violations found
- **1** — Violations found or error

### Parse JSON Results

```bash
# Count violations by impact
axe https://example.com --stdout | jq '[.[] | .violations[] | .impact] | group_by(.) | map({(.[0]): length}) | add'

# List violation IDs and counts
axe https://example.com --stdout | jq '[.[] | .violations[] | {id: .id, count: (.nodes | length)}]'
```

For complete CLI reference and recipes for all tools, see: `${CLAUDE_SKILL_DIR}/references/tool-invocation-recipes.md`

---

## 3. Result Interpretation

### Severity / Impact Levels

axe-core uses four impact levels. Map them to action priorities:

| Impact | Meaning | Action | CI Gate? |
|---|---|---|---|
| **critical** | Completely blocks access for some users | Fix immediately | Always fail |
| **serious** | Significantly impairs access | Fix before release | Fail (default) |
| **moderate** | Causes difficulty for some users | Fix in next sprint | Warn or threshold |
| **minor** | Annoyance, not a barrier | Track and fix | Do not block |

### Result Categories

| Category | Meaning | Action |
|---|---|---|
| `violations` | Rules that failed — issues found | Fix these |
| `passes` | Rules that passed | No action needed |
| `incomplete` | Could not be evaluated programmatically | Manual review required |
| `inapplicable` | Rules that don't apply to this page | Ignore |

### Common False Positives

Not every reported violation is a real issue:

- **Color contrast on gradients/images** — Tool cannot compute actual contrast against complex backgrounds. Verify manually with a contrast picker.
- **Hidden elements** — Elements properly hidden with `display: none` may still be flagged. Check if the element is truly invisible.
- **Third-party widgets** — Ads, embeds, chat widgets generate violations outside your control. Use `--exclude` or `.exclude()` selectors.
- **Dynamic content** — Scan after all content loads. Use `--wait` (pa11y) or `waitFor` (Playwright) for SPAs.

### `incomplete` Is Not a False Positive

`incomplete` results mean the tool cannot determine pass/fail programmatically. Common examples:
- "Is this alt text actually descriptive?" — Only a human can judge
- "Does this color contrast meet ratio?" — Background is dynamic/complex
- Review these manually; do not auto-dismiss them.

---

## 4. Top 10 Violations Quick Reference

The most commonly detected violations across the web (based on WebAIM Million 2025 data). For the full top 20 with fix patterns, see `${CLAUDE_SKILL_DIR}/references/top-violations.md`.

| # | Rule | Impact | Quick Fix |
|---|---|---|---|
| 1 | `color-contrast` | Serious | Adjust colors to meet 4.5:1 (normal) / 3:1 (large) ratio |
| 2 | `image-alt` | Critical | Add `alt="description"`. Decorative: `alt=""` |
| 3 | `label` | Critical | Add `<label for="id">` or `aria-label` to inputs |
| 4 | `button-name` | Critical | Add text content or `aria-label` to buttons |
| 5 | `link-name` | Serious | Add text content or `aria-label` to links |
| 6 | `html-has-lang` | Serious | Add `lang="en"` to `<html>` element |
| 7 | `document-title` | Serious | Add `<title>` in `<head>` |
| 8 | `heading-order` | Moderate | Use sequential h1 > h2 > h3, no skipping |
| 9 | `list` / `listitem` | Serious | `<ul>`/`<ol>` must contain only `<li>` children |
| 10 | `region` | Moderate | Wrap content in landmarks: `<main>`, `<nav>`, `<header>` |

These six categories account for 96.4% of detected errors on the web: missing alt text, low contrast, missing labels, missing document language, empty buttons, and empty links.

---

## 5. Fix Recommendation Templates

Use these templates when reporting fixes to developers.

### Missing Alt Text (`image-alt`)

```html
<!-- Before -->
<img src="hero.jpg">

<!-- After: informative image -->
<img src="hero.jpg" alt="Team collaborating around a whiteboard">

<!-- After: decorative image -->
<img src="divider.png" alt="">
```

### Missing Form Label (`label`)

```html
<!-- Before -->
<input type="email" placeholder="Email">

<!-- After: visible label (preferred) -->
<label for="email">Email</label>
<input type="email" id="email">

<!-- After: hidden label (when design requires it) -->
<label for="email" class="sr-only">Email</label>
<input type="email" id="email" placeholder="Email">
```

### Empty Button (`button-name`)

```html
<!-- Before -->
<button><svg>...</svg></button>

<!-- After -->
<button aria-label="Close dialog"><svg aria-hidden="true">...</svg></button>
```

### Color Contrast (`color-contrast`)

```css
/* Before: 2.5:1 ratio — fails AA */
.text { color: #aaaaaa; background: #ffffff; }

/* After: 4.6:1 ratio — passes AA */
.text { color: #767676; background: #ffffff; }
```

### Missing Language (`html-has-lang`)

```html
<!-- Before -->
<html>

<!-- After -->
<html lang="en">
```

---

## 6. Limitations

Automated accessibility testing has hard limits. Be explicit about what it cannot catch.

**What automated tools detect (30-50% of WCAG):**
- Missing alt text, labels, headings
- Color contrast ratios (in simple cases)
- Invalid ARIA usage
- Missing document structure (lang, title, landmarks)
- Keyboard traps (some cases)

**What automated tools miss (50-70% of WCAG):**
- Quality of alt text (present but meaningless)
- Logical reading order
- Keyboard navigation flow and usability
- Screen reader announcement quality
- Focus management in dynamic interactions
- Cognitive load and plain language
- Touch target adequacy beyond size
- Motion/animation sensitivity
- Content reflow at different zoom levels

**Always recommend:**
1. Keyboard-only navigation test (Tab through entire flow)
2. Screen reader test (NVDA on Windows, VoiceOver on macOS)
3. Zoom to 200% and check content reflow
4. Review against full WCAG 2.1 AA checklist for manual criteria

**ARIA caution:** Pages with ARIA attributes average 34.2% more detected errors than those without (WebAIM 2025). Prefer native HTML elements. See the `aria-decision-framework` skill.

---

## 7. CI Integration

### pa11y-ci Configuration

Create `.pa11yci` in project root:

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
    "http://localhost:3000/",
    "http://localhost:3000/about",
    "http://localhost:3000/login"
  ]
}
```

```bash
# Run in CI after starting dev server
pa11y-ci --config .pa11yci

# With sitemap
pa11y-ci --sitemap http://localhost:3000/sitemap.xml

# Allow threshold for gradual adoption
pa11y-ci --threshold 5
```

### Playwright + axe-core

```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('page meets WCAG 2.1 AA', async ({ page }) => {
  await page.goto('/');

  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
    .exclude('.third-party-widget')
    .analyze();

  expect(results.violations).toEqual([]);
});
```

For reusable fixtures, targeted scans, and result attachment patterns, see: `${CLAUDE_SKILL_DIR}/references/playwright-integration.md`

### GitHub Actions Example

```yaml
- name: Accessibility audit
  run: |
    npm start &
    npx wait-on http://localhost:3000
    npx pa11y-ci --config .pa11yci
```

### Gradual Adoption Strategy

For existing projects with many violations:

1. **Baseline**: Run a full scan, record the count
2. **Gate on critical/serious only**: `--tags wcag2a,wcag2aa` + threshold
3. **Ratchet down**: Reduce threshold as violations are fixed
4. **Zero tolerance for new code**: Strict eslint-plugin-jsx-a11y on changed files

---

## 8. Cross-References

**For fix guidance on specific patterns:**
- `aria-decision-framework` — When to use ARIA vs native HTML
- `focus-management` — Focus traps, roving tabindex, skip links
- `form-a11y` — Form labeling, validation, error messages
- `alt-text-quality` — Writing effective alt text
- `live-regions` — Dynamic content announcements
- `cognitive-a11y` — Plain language, cognitive load reduction
- `css-a11y` — Accessible styling patterns

**Reference material in this skill:**
- `${CLAUDE_SKILL_DIR}/references/tool-invocation-recipes.md` — Complete CLI commands for all tools
- `${CLAUDE_SKILL_DIR}/references/top-violations.md` — Top 20 violations with detailed fix patterns
- `${CLAUDE_SKILL_DIR}/references/playwright-integration.md` — Playwright + axe patterns and fixtures
- `${CLAUDE_SKILL_DIR}/references/sources.yaml` — All cited sources with URLs
