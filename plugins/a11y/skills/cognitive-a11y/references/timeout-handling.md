# Timeout Handling Patterns
## Contents

- [WCAG Requirements](#wcag-requirements)
- [Warning Dialog Pattern](#warning-dialog-pattern)
  - [Requirements](#requirements)
- [Banner Alternative](#banner-alternative)
- [JavaScript Implementation Skeleton](#javascript-implementation-skeleton)
- [Data Preservation](#data-preservation)
- [Known Failures](#known-failures)
- [Checklist](#checklist)


Example patterns to adapt and verify for session timeout handling; markup and timer skeletons alone do not establish conformance.

---

## WCAG Requirements

**SC 2.2.1 Timing Adjustable (Level A):** For every time limit set by the content, provide at least one of:

1. **Turn off** — user can disable the limit before encountering it.
2. **Adjust** — before encountering the limit, the user can adjust it over a range at least ten times the default length.
3. **Extend** — warn before expiration, give at least 20 seconds to extend with a simple action, allow extension at least 10 times.

Exceptions: real-time events (auctions), essential limits whose extension would invalidate the activity, and limits exceeding 20 hours.
([WCAG SC 2.2.1](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html))

**SC 2.2.6 Timeouts (Level AAA):** Warn users of the inactivity duration that causes data loss, unless data is preserved for more than 20 hours without user action.
([WCAG SC 2.2.6](https://www.w3.org/WAI/WCAG21/Understanding/timeouts.html))

---

## Warning Dialog Pattern

Project example: warn 2 minutes before session expiration where feasible; WCAG extension requires at least 20 seconds to act. Implement actual modal behavior before claiming an alertdialog is operable:

```html
<div role="alertdialog"
     aria-label="Session expiring"
     aria-describedby="timeout-msg"
     aria-modal="true">
  <p id="timeout-msg">
    Your session will end in 2 minutes.
    Any unsaved changes will be lost.
  </p>
  <button autofocus>Continue session</button>
  <button>Sign out now</button>
</div>
```

### Project Implementation Choices for This Extension Example

- For a modal warning, implement the dialog pattern and inspect role, name, description, and focus in supported environments. A role alone does not implement behavior.
- Set `aria-modal="true"` and trap focus within the dialog.
- Choose initial focus deliberately; the Continue session action is suitable for this short warning. Other dialog contents may justify a different target.
- The extension route requires a simple action; this example uses Enter on a focused Continue session button.
- Expose remaining time if displayed. Avoid announcing every second; test whether occasional updates help users without interrupting their task.

([DWP Design System](https://design-system.dwp.gov.uk/patterns/manage-a-session-timeout))

---

## Banner Alternative

When a modal would obscure the user's work, use a banner instead:

```html
<div role="alert" class="timeout-banner">
  <p>Your session will end in 2 minutes.
     <button>Continue session</button>
  </p>
</div>
```

A nonmodal banner can preserve the current interaction. Verify users notice it and can reach the extension action within the available time; suitability depends on the workflow and supported environments.

---

## JavaScript Implementation Skeleton

```javascript
const SESSION_DURATION = 30 * 60 * 1000; // 30 minutes
const WARNING_BEFORE = 2 * 60 * 1000;    // warn 2 minutes before

let sessionTimer;
let warningTimer;

function startSession() {
  clearTimeout(sessionTimer);
  clearTimeout(warningTimer);

  warningTimer = setTimeout(showWarning, SESSION_DURATION - WARNING_BEFORE);
  sessionTimer = setTimeout(expireSession, SESSION_DURATION);
}

function showWarning() {
  // Show the alertdialog, focus the "Continue" button
}

function extendSession() {
  // Dismiss the dialog, restart timers
  startSession();
}

function expireSession() {
  // Save only policy-approved draft fields through the application's persistence layer.
  // Do not persist credentials or restricted sensitive values.
  preserveFormData();
  // Then redirect or show expired message
}

function preserveFormData() {
  // Persist an allowlisted subset of eligible draft inputs in the approved store
  // Restore on next page load
}
```

---

## Data Preservation

If the session expires, recover eligible draft progress under the application's security/privacy policy:

1. Before expiry, save only eligible draft fields in the approved persistence layer. Exclude credentials and restricted sensitive data; browser storage is not a blanket recommendation.
2. After re-authentication, restore only the permitted saved values and explain any required re-entry.
3. Inform the user: "Your previous entries have been restored."

Explain which eligible progress was saved and which policy-restricted fields require re-entry.

---

## Known Failures

These patterns need evaluation against the chosen SC 2.2.1 route, not a blanket failure classification:

| Pattern | Condition to assess |
|---------|---------------------|
| Timed reload or redirect | Does the content-set limit provide turn-off, adjustment, or extension, or meet an exception? Avoid unnecessary interruptions as a project policy. |
| Server-side expiry or redirect | Server authority can coordinate a client warning and extension endpoint. Verify that the client has accurate expiry information and the server honors extension. |
| Silent session expiry | A missing applicable timing-control route can fail SC 2.2.1. Inactivity data-loss warning is separately covered by SC 2.2.6 at AAA. |

([WCAG SC 2.2.1](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html))

---

## Checklist

- [ ] Identify each content-set limit and record the chosen turn-off, adjustment, extension route, or justified exception (Level A)
- [ ] For the selected extension route: warn before expiry and provide at least 20 seconds for a simple extension action, at least 10 times (Level A)
- [ ] For this project's extension example: prefer a 2-minute warning where feasible; test the chosen notification, focus behavior, and reachable action
- [ ] Verify the server and client agree on expiry and extension; test delay, stale warnings, and re-authentication
- [ ] Recover eligible draft progress under policy, excluding credentials and restricted sensitive values; explain required re-entry
- [ ] If a countdown is displayed, expose its meaning without excessive announcements
- [ ] At Level AAA, warn about the inactivity duration that can cause data loss before the timeout is encountered, unless data is preserved for more than 20 hours without user action

([Timing Adjustable, Level A](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html); [Timeouts, Level AAA](https://www.w3.org/WAI/WCAG22/Understanding/timeouts.html))
