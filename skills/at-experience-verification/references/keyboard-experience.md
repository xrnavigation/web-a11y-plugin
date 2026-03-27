# Keyboard Navigation Experience

What keyboard navigation feels like when it works, and what it feels like when it breaks.

## Who Uses Keyboard Navigation

- People with motor impairments: muscular dystrophy, arthritis, tremors, paralysis, limb loss
- People with temporary injuries: broken arm, RSI, post-surgery
- Blind users navigating with screen readers (keyboard is the primary input)
- Power users who prefer keyboard over mouse
- Voice control users (Dragon NaturallySpeaking, Voice Control) -- voice commands map to keyboard actions

This is not a niche audience. ([Level Access Keyboard Guide](https://www.levelaccess.com/blog/keyboard-navigation-complete-web-accessibility-guide/))

## What Correct Keyboard Navigation Feels Like

- **Tab** moves forward through interactive elements in logical reading order
- **Shift+Tab** moves backward
- **Enter** activates links and buttons
- **Space** activates buttons, toggles checkboxes
- **Arrow keys** navigate within composite widgets (radio groups, tabs, menus, tree views)
- **Escape** closes overlays, cancels operations
- **Skip link** ("Skip to main content") jumps past repeated navigation
- Focus indicator is always visible on the current element
- Tab order matches visual layout -- no jumping between unrelated areas

The user always knows where they are, what they can do, and how to get to the next thing.

## Keyboard Traps

### What Happens

The user tabs into a component -- a modal, a custom date picker, a video player, a rich text editor. They press Tab. Nothing happens. Shift+Tab -- nothing. Escape -- nothing. Arrow keys -- nothing. They are stuck.

> "You tab into a custom modal or dropdown, and suddenly you're stuck. Focus won't move. The Tab key feels broken, Shift+Tab does nothing, and Escape isn't helping either."
> -- ([216digital](https://216digital.com/lost-in-focus-blame-keyboard-traps/))

The only escape is refreshing the page or closing the browser tab. All form progress is lost. The user starts over from zero -- if they come back at all.

### Common Trap Patterns

| Pattern | Why It Traps |
|---|---|
| Custom date pickers / masked inputs | Intercept arrow keys and Tab without providing exit routes |
| Media players (video/audio) | Swallow every keydown -- Space, arrows, Tab all consumed |
| JavaScript-enhanced links | `preventDefault()` on Tab creates instant traps |
| `onBlur` validation | Forces focus back to field when validation fails -- infinite loop |
| Rich text editors | Capture all keyboard input for formatting commands |
| iframes with no focusable content | Focus enters the iframe but has nowhere to go and cannot escape |

(Sources: [216digital Keyboard Traps](https://216digital.com/lost-in-focus-blame-keyboard-traps/), [BOIA Keyboard Traps](https://www.boia.org/blog/why-keyboard-traps-are-one-of-the-most-frustrating-accessibility-issues), [A11Y Collective Keyboard Trap](https://www.a11y-collective.com/blog/keyboard-trap/))

### What Correct Feels Like

- Tab moves through the component's interactive elements
- After the last element, Tab moves to the next element outside the component
- Shift+Tab moves backward out of the component
- Escape closes any overlay
- Focus is never stuck

## Excessive Tabbing

### The Problem

Sequential keyboard navigation through dozens or hundreds of focusable elements is physically painful for users with motor impairments. Every keypress costs effort. A page with 50 navigation links before the main content means 50 Tab presses just to start reading.

### The Fix

- **Skip links** ("Skip to main content") as the first focusable element
- **Landmark regions** (`<nav>`, `<main>`, `<aside>`) so screen reader users can jump by region
- **Logical tab order** that follows visual layout
- **Minimize unnecessary tab stops** -- decorative elements should not be focusable

(Sources: [WebAIM Keyboard](https://webaim.org/techniques/keyboard/), [NNGroup Keyboard](https://www.nngroup.com/articles/keyboard-accessibility/))

## Invisible Focus Indicators

### What It Feels Like

> Pressing Tab and seeing nothing change on the screen. You know you moved somewhere, but you don't know where. It's like navigating a room in the dark.

For sighted keyboard users (can see the screen, can't use a mouse), this is devastating. They see the entire page but cannot locate the one element that will respond to Enter.

### The Cause

Designers dislike the default browser focus ring (blue or dotted outline) because it appears on mouse click too. Rather than styling it to be more attractive, they remove it: `*:focus { outline: none; }`.

### The Fix

Use `:focus-visible` -- shows the indicator only for keyboard navigation, not mouse clicks:

```css
/* Remove outline for mouse users */
:focus:not(:focus-visible) {
  outline: none;
}

/* Clear, visible outline for keyboard users */
:focus-visible {
  outline: 2px solid #005fcc;
  outline-offset: 2px;
}
```

The focus ring should be at least 2px thick with sufficient contrast against the background.

(Sources: [A11Y Project Outlines](https://www.a11yproject.com/posts/never-remove-css-outlines/), [OutlineNone.com](https://www.outlinenone.com/), [MDN :focus-visible](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible))

## Inconsistent Tab Order

### What It Feels Like

Tab moves from the search bar to a footer link, then to a sidebar widget, then back to the header. The user has no mental model of the page layout because the navigation order contradicts the visual layout.

### Common Causes

- Positive `tabindex` values (`tabindex="5"`) that override DOM order
- CSS layout changes (flexbox `order`, absolute positioning) that don't match DOM order
- Dynamically inserted content that appears visually in one place but lives elsewhere in the DOM

### The Fix

- Never use `tabindex` greater than 0
- Ensure DOM order matches visual layout
- When CSS reorders elements visually, restructure the DOM to match

## Drop-Down Select Menus

### The Problem

Some `<select>` implementations fire `onchange` on arrow key navigation. The user presses Down Arrow to browse options and the first option immediately activates -- navigating to a new page or submitting a selection before the user has finished browsing.

### What Correct Feels Like

Arrow keys browse options without activating. Enter or Space confirms the selection. The user can review all choices before committing.

(Sources: [WebAIM Keyboard](https://webaim.org/techniques/keyboard/), [NNGroup Keyboard](https://www.nngroup.com/articles/keyboard-accessibility/))
