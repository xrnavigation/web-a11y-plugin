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

## Install in Antigravity

Clone this repository and install complete directories from `plugins/a11y/skills/<skill-name>/` into a skill location below. Keep each `SKILL.md` with its references and scripts; do not install the repository's marketplace root as a skill.

| Surface | Project location | User location |
| --- | --- | --- |
| App and IDE | `.agents/skills/<skill-name>/` | `~/.gemini/config/skills/<skill-name>/` |
| CLI | `.agents/skills/<skill-name>/` | `~/.gemini/antigravity-cli/skills/<skill-name>/` |

Invoke `/a11y-dialog` or ask the agent to use the skill. Inspect active skills in the IDE's Customizations menu. These are direct skill installations; native Antigravity plugin compatibility has not been established for this bundle.

See [Antigravity skill locations](https://antigravity.google/docs/skills), [Claude Code plugin installation](https://code.claude.com/docs/en/discover-plugins), and [Codex skill discovery](https://learn.chatgpt.com/docs/build-skills). Installing skills does not install any external tools their workflows need.

## Layout

```text
.claude-plugin/marketplace.json
.agents/plugins/marketplace.json
plugins/a11y/
  .claude-plugin/plugin.json
  .codex-plugin/plugin.json
  skills/<skill-name>/SKILL.md
```
