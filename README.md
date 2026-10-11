# web-a11y-plugin

Web accessibility agent skills for Claude Code, Codex CLI, and Gemini CLI. Part of the [Agent Skills](https://agentskills.io) open standard.

## Why this exists

Accessibility work needs more than plausible markup. These skills guide native semantics, keyboard behavior, focus, content alternatives and verification using WCAG, WAI-ARIA, APG and cited implementation guidance. They provide concrete examples and identify the checks that require browser or assistive technology evidence.

Skills include cited reference material and distinguish requirements, authoring guidance and tested behavior. Compatibility observations require verification against the product support matrix.

## Skills

### APG Widget Patterns
| Skill | What it covers |
|---|---|
| `a11y-accordion` | `<details>`/`<summary>` vs ARIA accordion, disclosure pattern |
| `a11y-combobox` | Combobox, autocomplete, typeahead, select-with-search |
| `a11y-dialog` | Modal/non-modal dialogs, `<dialog>` element, focus trapping, `inert` |
| `a11y-grid` | Data grids, sortable tables, table vs grid decision |
| `a11y-listbox` | Single/multi-select lists, reorderable lists |
| `a11y-menu` | Application menus, menu buttons, menu vs navigation distinction |
| `a11y-tabs` | Tab interfaces, automatic vs manual activation |
| `a11y-tree` | Tree views, treegrid, file browsers |

### Foundations
| Skill | What it covers |
|---|---|
| `aria-decision-framework` | First rule of ARIA — use native HTML before ARIA roles |
| `focus-management` | Focus trapping, restoration, SPA route changes, skip nav |
| `form-a11y` | Error messaging, validation, accessible auth (WCAG 2.2), autocomplete |
| `css-a11y` | Focus indicators, forced-colors, prefers-reduced-motion, target sizing |
| `live-regions` | ARIA live regions for notifications, toasts, status messages |
| `zoom-reflow` | Text resizing, reflow thresholds, spacing overrides and layout test matrices |
| `pointer-gestures` | Dragging and gesture alternatives, cancellation, hybrid input and target spacing |
| `media-a11y` | Captions, transcripts, audio description and usable media players |

### Audit & Testing
| Skill | What it covers |
|---|---|
| `a11y-audit` | Automated scanning with axe-core, pa11y, Lighthouse, eslint-plugin-jsx-a11y |
| `testing-strategy` | What to test automatically vs manually vs with AT |
| `at-experience-verification` | Actual AT journey evidence, support matrices and observed versus predicted output |

### Content & UX
| Skill | What it covers |
|---|---|
| `accessible-content-writing` | Link text, error messages, alt text, plain language, headings |
| `alt-text-quality` | W3C decision tree for decorative vs informative vs functional images |
| `disability-user-stories` | Accessibility-centered user stories and acceptance criteria |

### Cognitive & Inclusive Design
| Skill | What it covers |
|---|---|
| `cognitive-a11y` | Error messages, consistent nav, timeouts, progress indicators |
| `cognitive-neurodivergent-experience` | Predictability, sensory preferences and variable support needs |

### Guardrails
| Skill | What it covers |
|---|---|
| `hostile-pattern-detection` | Carousels, infinite scroll, hover-only, auto-play, CAPTCHAs |
| `overlay-resistance` | Source remediation, overlay limitations and bounded evidence |

## Install in Claude Code

Add the marketplace, then install:

```
/plugin marketplace add xrnavigation/web-a11y-plugin
/plugin install a11y@web-a11y-skills-marketplace
```

## Install in Codex

```text
codex plugin marketplace add xrnavigation/web-a11y-plugin
codex plugin add a11y@web-a11y-skills-marketplace
```

Adding the marketplace registers its catalog; the second command installs the plugin.
For local development, replace the repository name in either marketplace command with `.`.

## Layout

```text
.claude-plugin/marketplace.json
.agents/plugins/marketplace.json
plugins/a11y/
  .claude-plugin/plugin.json
  .codex-plugin/plugin.json
  skills/<skill-name>/SKILL.md
```

## Validate and develop

There are 26 skills. Work in the plugin source repository; the xr-skills repository
is a catalog. For a locally reviewed working copy in Codex:

```text
codex plugin marketplace add .
codex plugin add a11y@web-a11y-skills-marketplace --json
codex plugin list --marketplace web-a11y-skills-marketplace --json
```

Installed skills are available on the next turn. After changing source files,
reinstall and compare the cached files with the reviewed source; registering a
marketplace alone does not install skills.

```text
uv run --with pyyaml python scripts/check_skills.py
```

The validator checks metadata, required references, local file links, citation
registration, plugin JSON and line budgets. It does not validate every claim,
external link or browser/AT behavior. Local audit reports are kept in the ignored
`reports/` directory; they record source-review scope and verification limits.
