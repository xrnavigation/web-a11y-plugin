# Skill installation documentation

## Goal
Refresh the published installation instructions for current agent hosts within Q's approved plan.

## State
Branch docs/skills-installation. Documentation edits prepared; MapLibre also adds Codex manifests pointing to its existing skills directory. No skill behavior or installer changes. Awaiting publication and existing PR checks. Merge and release are not authorized.

## Decisions and why
Keep one canonical skill tree and preserve current versions. Use direct Antigravity skill locations; do not claim native plugin compatibility. Preserve existing Claude/Codex installation workflows. For CRM, retain its bootstrap, configuration, and credential dependencies; Antigravity support remains unverified.

## Surprises
Antigravity App/IDE and CLI have different user-wide skill locations. Existing repositories already support Codex except MapLibre's missing host manifests. No GitHub Actions workflow files were present in this checkout.

## Next step
Commit and push this independent branch, open its PR, and read any checks to completion. Report absent CI explicitly; do not add CI or run substitute local test gates.
