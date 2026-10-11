---
name: a11y-tabs
description: Guides accessible tablists, tabs, and tabpanels. Use when building tabbed content, choosing manual or automatic activation, or managing tab focus, ownership, and panel visibility.
---

# Accessible tabs

Use ARIA tabs for layered panels controlled by a tablist. APG supplies design
guidance, not a normative WCAG specification; implement and test the behavior as
well as roles ([APG tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)).

## Structure

```html
<div role="tablist" aria-label="Account">
  <div class="tab-wrapper">
    <button role="tab" id="profile-tab" aria-controls="profile-panel"
            aria-selected="true" tabindex="0">Profile</button>
  </div>
  <button role="tab" id="billing-tab" aria-controls="billing-panel"
          aria-selected="false" tabindex="-1">Billing</button>
</div>
<div role="tabpanel" id="profile-panel" aria-labelledby="profile-tab" tabindex="0">
  Profile information
</div>
<div role="tabpanel" id="billing-panel" aria-labelledby="billing-tab" tabindex="0" hidden>
  Billing information
</div>
```

This scaffold needs event handlers. A neutral wrapper does not inherently break
ownership: descendant tabs can be owned by their tablist. Preserve the required
role relationship and meaningful accessibility-tree structure; avoid unrelated
interactive controls in the tablist
([WAI-ARIA tablist](https://www.w3.org/TR/wai-aria-1.2/#tablist)).

Name the tablist, name each tab, link tabs to panels with `aria-controls`, and
name each panel from its tab with `aria-labelledby`. Keep `aria-selected`,
visibility and focus state synchronized. If a panel has no focusable first
content, `tabindex="0"` on the panel makes it reachable from the tab
([APG tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)).

## Activation and focus

Keep one tab in the page Tab sequence. Horizontal tabs use Left/Right; vertical
tabs use Up/Down and `aria-orientation="vertical"`. Tab exits the tablist.
Automatic activation is suitable when panels appear without noticeable latency;
otherwise use manual activation with Enter/Space. In manual mode, the focused
roving tab can differ from the selected tab
([APG tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)).

Keep focus on the tab during ordinary activation; make the panel reachable
without moving focus there on every arrow key. Hide inactive panels with
`hidden` or equivalent rendering behavior, not `aria-hidden` alone on content
with focusable descendants
([APG tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/),
[WAI-ARIA aria-hidden](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden)).

## Verify

Exercise entry/exit, arrows, manual activation, panel reading and deletion if
supported. Test loading delay and responsive orientation. Observe actual tab
names, selection and panel relationships; do not expect fixed spoken strings.

Read [keyboard interaction](references/keyboard-interaction.md),
[verification](references/screen-reader-behavior.md),
[common mistakes](references/common-mistakes.md) and
[sources](references/sources.yaml).
