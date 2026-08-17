# Screen Reader Commands Reference
## Contents

- [NVDA (Windows) — Essential Testing Subset](#nvda-windows-essential-testing-subset)
  - [Setup](#setup)
  - [Mode Switching](#mode-switching)
  - [Reading](#reading)
  - [Element Navigation (Browse Mode)](#element-navigation-browse-mode)
  - [Elements List](#elements-list)
  - [Tables](#tables)
  - [Forms](#forms)
- [VoiceOver (macOS) — Essential Testing Subset](#voiceover-macos-essential-testing-subset)
  - [Setup](#setup-1)
  - [Reading](#reading-1)
  - [Navigation](#navigation)
  - [Rotor](#rotor)
  - [Tables](#tables-1)
  - [Safari Prerequisite](#safari-prerequisite)
- [TalkBack (Android) — Essential Testing Subset](#talkback-android-essential-testing-subset)
  - [Setup](#setup-2)
  - [Touch Navigation](#touch-navigation)
  - [Reading Controls](#reading-controls)
  - [Navigation by Element Type](#navigation-by-element-type)


## NVDA (Windows) — Essential Testing Subset

NVDA is free and covers 37.7% of desktop screen reader users. ([WebAIM Survey #10, 2024](https://webaim.org/projects/screenreadersurvey10/))

### Setup

| Action | Keys |
|--------|------|
| Start NVDA | Ctrl + Alt + N |
| Stop NVDA | Insert + Q |
| Toggle Speech Viewer (shows output as text) | NVDA menu > Tools > Speech Viewer |
| Keyboard help mode | Insert + 1 |

### Mode Switching

| Action | Keys |
|--------|------|
| Toggle Browse/Focus mode | Insert + Space |

Browse mode: navigate page with single-letter shortcuts. Focus mode: type into form fields.

### Reading

| Action | Keys |
|--------|------|
| Start reading from current position | Insert + Down Arrow |
| Stop reading | Ctrl |
| Read current line | Insert + Up Arrow |
| Read next/previous line | Down / Up Arrow |

### Element Navigation (Browse Mode)

| Action | Keys |
|--------|------|
| Next heading | H |
| Heading level 1-6 | 1, 2, 3, 4, 5, 6 |
| Next landmark/region | D |
| Next link | K |
| Next unvisited link | U |
| Next visited link | V |
| Next form field | F |
| Next button | B |
| Next table | T |
| Next list | L |
| Next graphic | G |

All support Shift + key for previous (e.g., Shift + H for previous heading).

### Elements List

| Action | Keys |
|--------|------|
| Open Elements List (links, headings, landmarks, form fields) | Insert + F7 |

### Tables

| Action | Keys |
|--------|------|
| Move between cells | Ctrl + Alt + Arrow Keys |

### Forms

| Action | Keys |
|--------|------|
| Toggle checkbox | Space |
| Open combo box | Alt + Down Arrow |
| Select radio button | Up / Down Arrow |

Sources: [Deque University NVDA Shortcuts](https://dequeuniversity.com/screenreaders/nvda-keyboard-shortcuts), [WebAIM NVDA Shortcuts](https://webaim.org/resources/shortcuts/nvda)

---

## VoiceOver (macOS) — Essential Testing Subset

VO = Control + Option (the VoiceOver modifier)

VoiceOver covers 9.7% of desktop users and all iOS users (70.6% of mobile SR users). ([WebAIM Survey #10, 2024](https://webaim.org/projects/screenreadersurvey10/))

### Setup

| Action | Keys |
|--------|------|
| Start/Stop VoiceOver | Cmd + F5 (or Triple-click TouchID) |
| VoiceOver help | VO + H |
| Screen Curtain (blacken screen for true SR testing) | VO + Shift + F11 |

### Reading

| Action | Keys |
|--------|------|
| Read all from current position | VO + A |
| Stop reading | Ctrl |
| Read next item | VO + Right Arrow |
| Read previous item | VO + Left Arrow |
| Read current item | VO + F3 |

### Navigation

| Action | Keys |
|--------|------|
| Next heading | VO + Cmd + H |
| Next link | VO + Cmd + L |
| Next form control | VO + Cmd + J |
| Next table | VO + Cmd + T |
| Next list | VO + Cmd + X |
| Next image | VO + Cmd + G |
| Activate element | VO + Space |
| Tab to next interactive element | Tab |

All support adding Shift for previous (e.g., Shift + VO + Cmd + H for previous heading).

### Rotor

| Action | Keys |
|--------|------|
| Open Rotor | VO + U |
| Navigate Rotor categories | Left / Right Arrow |
| Navigate within category | Up / Down Arrow |
| Go to selected item | Enter |

The Rotor provides categorized lists of: headings, links, form controls, tables, landmarks, images.

### Tables

| Action | Keys |
|--------|------|
| Read column header | VO + C |
| Read row header | VO + R |

### Safari Prerequisite

Enable: Safari > Preferences > Advanced > Accessibility > "Press Tab to highlight each item on a webpage"

Source: [WebAIM Using VoiceOver](https://webaim.org/articles/voiceover/)

---

## TalkBack (Android) — Essential Testing Subset

TalkBack covers 27.6% of mobile screen reader users. ([WebAIM Survey #10, 2024](https://webaim.org/projects/screenreadersurvey10/))

### Setup

| Action | Gesture/Command |
|--------|----------------|
| Enable TalkBack | Settings > Accessibility > TalkBack |
| Quick toggle | Hold both volume buttons for 3 seconds |

### Touch Navigation

| Action | Gesture |
|--------|---------|
| Explore screen | Drag one finger across screen |
| Next element | Swipe right |
| Previous element | Swipe left |
| Activate element | Double tap anywhere |
| Scroll | Two-finger swipe |

### Reading Controls

| Action | Gesture |
|--------|---------|
| Read from top | Global Context Menu > "Read from the top" |
| Read from next item | Global Context Menu > "Read from next item" |
| Change navigation granularity | Swipe up/down (cycles: headings, links, controls, words, characters) |

### Navigation by Element Type

Use the Local Context Menu to select element type (Headings, Links, Controls, Landmarks), then swipe right/left to navigate through them.

Sources: [WebAIM Using TalkBack](https://webaim.org/articles/talkback/), [Harvard Digital Accessibility](https://accessibility.huit.harvard.edu/test-android-talkback)
