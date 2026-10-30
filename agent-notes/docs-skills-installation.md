# Skill installation documentation

## Goal
Refresh the published installation instructions for current agent hosts within Q's approved plan.

## State
PR #1 on docs/skills-installation contains the installation documentation and a public reusable skills CI workflow. Q approved the CI plan and normal merges of all six PRs after CI rollout and base refresh. The shared owner must pass and merge before consumers reference it. No skill behavior or installer changes.

## Decisions and why
Keep one canonical skill tree and preserve current versions. Use direct Antigravity skill locations; do not claim native plugin compatibility. Preserve existing Claude/Codex installation workflows. For CRM, retain its bootstrap, configuration, and credential dependencies; Antigravity support remains unverified.

## Surprises
Antigravity App/IDE and CLI have different user-wide skill locations. Existing repositories already support Codex except MapLibre's missing host manifests. No GitHub Actions workflow files were present in this checkout.

## Next step
Refresh against integrated main, push the shared workflow and its local caller, and read hosted checks to completion. Root verifies the result and performs the normal merge. Then consumer PRs can pin the integrated workflow revision; no open-PR references. CI validation lives once, inline in the reusable workflow, and checks out the caller's repository by design. Run no local CI substitute gates.
