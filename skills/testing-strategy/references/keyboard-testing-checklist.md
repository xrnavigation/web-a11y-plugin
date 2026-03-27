# Keyboard Testing Checklist

## Pre-test Setup

- Disconnect or do not touch the mouse
- Start from the browser address bar
- Note the starting point for tracking cycle completion

## Core Checks

### 1. Tab Order

- [ ] Tab moves forward through all interactive elements
- [ ] Shift + Tab moves backward
- [ ] Tab order matches visual layout / reading order
- [ ] No interactive elements are skipped
- [ ] Tab cycle completes (returns to browser address bar)

### 2. Focus Visibility

- [ ] Every focused element has a visible focus indicator
- [ ] Focus indicator has minimum 3:1 contrast ratio against adjacent colors ([WCAG 2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html))
- [ ] Focus indicator is consistent across the interface
- [ ] Custom focus styles do not disappear on any component

### 3. Keyboard Operability

- [ ] Links: activated with Enter
- [ ] Buttons: activated with Enter or Space
- [ ] Checkboxes: toggled with Space
- [ ] Radio buttons: navigated with Arrow keys
- [ ] Select/dropdown: opened with Alt + Down Arrow (or Space), navigated with arrows
- [ ] Custom widgets: operable with expected key patterns (see [ARIA APG](https://www.w3.org/WAI/ARIA/apg/))

### 4. Keyboard Traps

- [ ] Focus never gets stuck in any component
- [ ] Focus can always move away using Tab, Shift+Tab, or Escape
- [ ] Rich text editors and embedded content do not trap focus
- [ ] Media players are keyboard escapable

### 5. Modal/Dialog Focus Management

- [ ] Focus moves into modal when opened
- [ ] Focus is trapped within modal while open (Tab cycles within modal)
- [ ] Escape closes modal
- [ ] Focus returns to trigger element when modal closes

### 6. Skip Links

- [ ] Skip-to-content link is first focusable element
- [ ] Activating it moves focus past navigation
- [ ] Skip link becomes visible on focus (if visually hidden by default)

### 7. Dropdown/Menu Patterns

- [ ] Menu opens with Enter, Space, or Arrow keys (as appropriate)
- [ ] Arrow keys navigate within menu
- [ ] Escape closes menu
- [ ] Focus returns to trigger on close

## Standard Keyboard Commands Reference

| Key | Expected Action |
|-----|----------------|
| Tab | Move to next interactive element |
| Shift + Tab | Move to previous interactive element |
| Enter | Activate link or button |
| Space | Activate button, toggle checkbox, open select |
| Arrow keys | Navigate within widget (radio group, menu, tabs, listbox) |
| Escape | Close modal, menu, or dialog |
| Home / End | Jump to first/last item in list or menu |

## WCAG Success Criteria Tested

| Criterion | Description |
|-----------|-------------|
| [2.1.1 Keyboard](https://www.w3.org/WAI/WCAG21/Understanding/keyboard.html) | All functionality available from keyboard |
| [2.1.2 No Keyboard Trap](https://www.w3.org/WAI/WCAG21/Understanding/no-keyboard-trap.html) | Focus can always be moved away |
| [2.4.3 Focus Order](https://www.w3.org/WAI/WCAG21/Understanding/focus-order.html) | Tab order preserves meaning and operability |
| [2.4.7 Focus Visible](https://www.w3.org/WAI/WCAG21/Understanding/focus-visible.html) | Keyboard focus indicator is visible |
| [2.4.11 Focus Appearance](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html) | Focus indicator meets size and contrast requirements (WCAG 2.2) |

Sources: [WebAIM Keyboard Accessibility](https://webaim.org/techniques/keyboard/), [University of Washington Keyboard Checklist](https://www.washington.edu/accesstech/checklist/keyboard/), [W3C Easy Checks: Keyboard Focus](https://www.w3.org/WAI/test-evaluate/easy-checks/keyboard-focus/)
