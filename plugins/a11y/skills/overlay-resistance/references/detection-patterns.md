# Overlay Detection Patterns
## Contents

- [1. Script Tag Patterns](#1-script-tag-patterns)
  - [accessiBe](#accessibe)
  - [UserWay](#userway)
  - [AudioEye](#audioeye)
  - [EqualWeb](#equalweb)
  - [FACIL'iti](#faciliti)
  - [TruAbilities](#truabilities)
  - [MaxAccess](#maxaccess)
  - [ReciteMe](#reciteme)
- [2. Grep Patterns for Codebases](#2-grep-patterns-for-codebases)
- [3. DOM Indicators (Runtime)](#3-dom-indicators-runtime)
  - [Visual](#visual)
  - [DOM Elements](#dom-elements)
  - [JavaScript Globals](#javascript-globals)
  - [Meta Tags](#meta-tags)
- [4. Package Manager Indicators](#4-package-manager-indicators)
- [5. Agent Response on Detection](#5-agent-response-on-detection)


Use these patterns to identify overlay products in code, HTML, or running websites.

---

## 1. Script Tag Patterns

Search for `<script>` tags with `src` attributes matching these domains:

### accessiBe
```
acsbapp.com
acsbap.com
accesswidget
accessibe
```

### UserWay
```
cdn.userway.org
```

### AudioEye
```
audioeye.com
audioeye-cdn
```

### EqualWeb
```
equalweb
```

### FACIL'iti
```
facil-iti
```

### TruAbilities
```
truabilities
```

### MaxAccess
```
maxaccess
```

### ReciteMe
```
reciteme
```

---

## 2. Grep Patterns for Codebases

Run these against HTML files, templates, and JavaScript bundles:

```bash
# Script sources
grep -rE "(acsbapp|acsbap|accesswidget|accessibe|cdn\.userway\.org|audioeye|equalweb|facil-iti|truabilities|maxaccess|reciteme)" --include="*.html" --include="*.js" --include="*.jsx" --include="*.tsx" --include="*.vue" --include="*.svelte" --include="*.php" --include="*.erb" --include="*.hbs"

# CSS class names injected by overlays
grep -rE "(class=\"[^\"]*acsb|class=\"[^\"]*userway|class=\"[^\"]*audioeye|class=\"[^\"]*equalweb)" --include="*.html" --include="*.css"

# Global JavaScript variables
grep -rE "(window\._acsb|window\.UserWay|window\.AudioEye)" --include="*.js" --include="*.ts"

# Data attributes
grep -rE "(data-acsb)" --include="*.html"
```

---

## 3. DOM Indicators (Runtime)

When inspecting a live page:

### Visual
- Floating accessibility icon (wheelchair symbol), typically bottom-right corner
- Toolbar or panel that appears when the icon is clicked
- Options for text enlargement, contrast changes, "screen reader mode"

### DOM Elements
- `div` or `iframe` elements injected at the end of `<body>` with vendor identifiers
- Elements with class names containing: `acsb`, `userway`, `audioeye`, `equalweb`
- Vendor-prefixed data attributes on `<body>` or `<html>` (e.g., `data-acsb`)

### JavaScript Globals
- `window._acsb` (accessiBe)
- `window.UserWay` (UserWay)
- `window.AudioEye` (AudioEye)

### Meta Tags
- `<meta>` tags referencing overlay vendor names or products

---

## 4. Package Manager Indicators

Check `package.json`, `composer.json`, or CMS plugin lists for:

```
accessibe
userway
audioeye
equalweb
facil-iti
```

Also check WordPress plugin directories, Shopify app installations, and CMS extension lists for overlay vendor names.

---

## 5. Agent Response on Detection

When any of these patterns are found:

1. **Report the finding.** Name the vendor and the specific file/line where the overlay is loaded.
2. **Recommend removal.** The overlay is adding legal risk, degrading performance, and harming disabled users.
3. **Do not recommend keeping it temporarily.** There is no safe interim.
4. **Provide the remediation path:** manual audit, source code fixes, design system accessibility, CI/CD integration, user testing with disabled people.
5. **Cite the evidence** if challenged: FTC $1M fine, 1,000+ lawsuits/year, NFB ban, Overlay Fact Sheet (1,000+ signatories), Roselli testing showing overlays double violations.
