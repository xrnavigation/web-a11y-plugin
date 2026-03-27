# web-a11y-plugin

Web accessibility agent skills for Claude Code, Codex CLI, and Gemini CLI. Part of the [Agent Skills](https://agentskills.io) open standard.

## Why this exists

LLMs write inaccessible code by default. They over-use ARIA, skip keyboard interaction, ignore focus management, and produce markup that fails screen readers. These skills encode the actual rules — sourced from WAI-ARIA Authoring Practices, WCAG 2.2, and accessibility practitioners — so the agent gets it right the first time instead of generating plausible-looking code that breaks for real users.

Every skill includes cited reference material. No hallucinated guidance.

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

### Audit & Testing
| Skill | What it covers |
|---|---|
| `a11y-audit` | Automated scanning with axe-core, pa11y, Lighthouse, eslint-plugin-jsx-a11y |
| `testing-strategy` | What to test automatically vs manually vs with AT |
| `at-experience-verification` | What screen readers actually announce for your markup |

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
| `cognitive-neurodivergent-experience` | Why timeouts cause panic, why unpredictability causes distress |

### Guardrails
| Skill | What it covers |
|---|---|
| `hostile-pattern-detection` | Carousels, infinite scroll, hover-only, auto-play, CAPTCHAs |
| `overlay-resistance` | Never recommend accessibility overlays (accessiBe, UserWay, etc.) |

## Installation

Add the marketplace, then install:

```
/plugin marketplace add xrnavigation/agent-skills
/plugin install a11y@agent-skills
```

Or install directly:

```
/plugin install xrnavigation/web-a11y-plugin
```