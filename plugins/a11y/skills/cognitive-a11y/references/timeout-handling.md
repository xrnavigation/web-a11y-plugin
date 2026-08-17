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


Implementation patterns for WCAG-compliant session timeout handling.

---

## WCAG Requirements

**SC 2.2.1 Timing Adjustable (Level A):** For every time limit, provide at least one of:

1. **Turn off** — user can disable the limit before encountering it.
2. **Adjust** — user can set the limit to at least 10x the default.
3. **Extend** — warn before expiration, give at least 20 seconds to extend with a simple action, allow extension at least 10 times.

Exceptions: real-time events (auctions), essential limits (exams), and limits exceeding 20 hours.
([WCAG SC 2.2.1](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html))

**SC 2.2.6 Timeouts (Level AAA):** Warn users of the inactivity duration that causes data loss, unless data is preserved for 20+ hours.
([WCAG SC 2.2.6](https://www.w3.org/WAI/WCAG21/Understanding/timeouts.html))

---

## Warning Dialog Pattern

Warn at least 2 minutes before session expiration. Use an alertdialog:

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

### Requirements

- Use `role="alertdialog"` — this is announced immediately by screen readers.
- Set `aria-modal="true"` and trap focus within the dialog.
- The primary action ("Continue session") must receive focus automatically.
- Extension must work with a single keypress (Enter on the focused button).
- If using a countdown timer, ensure it is announced to screen readers (use `aria-live="polite"` on the countdown element, updating at reasonable intervals — not every second).

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

A banner is less disruptive and allows users to finish their current action before responding.

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
  // Save user data to sessionStorage/localStorage FIRST
  preserveFormData();
  // Then redirect or show expired message
}

function preserveFormData() {
  // Serialize all form inputs to sessionStorage
  // Restore on next page load
}
```

---

## Data Preservation

If the session does expire, preserve user-entered data:

1. Before expiry, serialize all form field values to `sessionStorage` or `localStorage`.
2. On the next page load (after re-authentication), restore the saved values.
3. Inform the user: "Your previous entries have been restored."

Never silently discard form progress.

---

## Known Failures

These patterns violate SC 2.2.1:

| Pattern | Problem |
|---------|---------|
| `<meta http-equiv="refresh" content="1800">` | Automatic reload without warning |
| Server-side redirect after timeout | No client-side warning possible |
| `<meta http-equiv="refresh" content="5;url=...">` | Timed redirect without user control |
| Silent session expiry | User data lost without notice |

([WCAG SC 2.2.1](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html))

---

## Checklist

- [ ] Warning appears at least 2 minutes (or 20 seconds minimum per WCAG) before expiry
- [ ] Warning uses `role="alertdialog"` or `role="alert"`
- [ ] Extension requires only a single keypress
- [ ] Extension is available at least 10 times
- [ ] User data is preserved if session expires
- [ ] Countdown (if present) is accessible to screen readers
- [ ] No `<meta http-equiv="refresh">` used for session management
- [ ] Users informed of inactivity timeout duration at start of session
