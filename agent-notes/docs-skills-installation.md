# Skill installation documentation

## Goal
Refresh the published installation instructions for current agent hosts within Q's approved plan.

## State
PR #1 on docs/skills-installation contains the installation documentation and a public reusable skills CI workflow. Q approved the CI plan and normal merges of all six PRs after CI rollout and base refresh. The shared owner must pass and merge before consumers reference it. No skill behavior or installer changes.

## Decisions and why
Keep one canonical skill tree and preserve current versions. Use direct Antigravity skill locations; do not claim native plugin compatibility. Preserve existing Claude/Codex installation workflows. For CRM, retain its bootstrap, configuration, and credential dependencies; Antigravity support remains unverified.

## Surprises
Antigravity App/IDE and CLI have different user-wide skill locations. Existing repositories already support Codex except MapLibre's missing host manifests. No GitHub Actions workflow files were present in this checkout.

The first hosted CI run caught workspace-relative composition and an unlocked native CLI install; both were fixed in source with self-repository references and a single locked tool package. The next run exposed that original actionlint does not recognize GitHub's current self-repository syntax, even on its main branch. The maintained kjanat/actionlint release supports that syntax through the existing validation path; the shared workflow now pins its release and explicitly disables unused cache access. No audit was ignored or disabled. The locked CLI action uses self-repository composition so consumers fetch the exact integrated shared workflow revision without a moving source ref.

The next hosted run passed syntax/security and exposed a validation-contract mismatch: four working plugin skills use documented Claude Code argument-hint/context fields, which the stricter claude.ai upload format rejects. The native plugin-directory validator now runs first with strict warnings, checking the full skills. The reference validator checks their portable core while retaining errors for every unknown field except those two documented native extensions. Standalone skills receive no such projection. Skill behavior and metadata are unchanged.

## Next step
Refresh against integrated main, push the shared workflow and its local caller, and read hosted checks to completion. Root verifies the result and performs the normal merge. Then consumer PRs can pin the integrated workflow revision; no open-PR references. CI validation lives once, inline in the reusable workflow, and checks out the caller's repository by design. Run no local CI substitute gates.
