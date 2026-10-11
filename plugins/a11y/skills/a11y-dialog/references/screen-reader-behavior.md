# Screen reader verification

This reference specifies checks to run, not results observed in this repository.
Historical support reports describe tested versions and settings; do not turn
them into universal support tables or guaranteed spoken output.

## Task checks

Test initial focus, the title, structured content reading, background exclusion, Tab boundaries, close requests, and restoration. The pattern's roles, states and keyboard contract are described
in [APG dialog-modal](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/).

Use the project's supported browser/OS/screen reader combinations and include
mobile interaction when the product supports it. Record versions, input method,
settings, starting state, action, actual output and task outcome. Check that
users can reach, understand and operate the control; exact wording can vary.

## Handle failures with evidence

Inspect name, role, state, ownership and real DOM focus first. Reproduce the
failure on the identified combination. Test a targeted fix and check other
combinations for regressions. Do not add blanket live announcements, force a
screen reader mode, or promise a native-control fallback behaves identically
everywhere.

```text
Environment and settings:
Initial state / action:
Expected information and task outcome:
Observed behavior:
Fix and retest result:
Untested combinations:
```
