# Menu Keyboard Interaction (Complete Spec)

Source: [APG Menu and Menubar Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/)

Arrow key directions below assume default orientation: menubar = horizontal, menu = vertical. If orientation is reversed via `aria-orientation`, arrow key directions swap accordingly.

---

## Tab / Shift+Tab

- **Into menubar:** focuses first item (or optionally last-focused item)
- **Out of menu/menubar:** exits and closes all open submenus

## Enter

- **On parent menuitem (has submenu):** opens submenu, focuses first item
- **On other menuitem:** activates the item, closes the menu
- **On menuitemcheckbox:** toggles `aria-checked`, **closes the menu**
- **On menuitemradio:** checks the item (unchecks others in group), **closes the menu**

## Space

- **On menuitemcheckbox:** toggles checked state (**without closing**)
- **On unchecked menuitemradio:** checks it, unchecks siblings (**without closing**)
- **On parent menuitem (has submenu):** opens submenu, focuses first item
- **On non-parent menuitem:** activates the item, closes the menu

> **Important:** The distinction between Enter and Space on checkbox/radio items is significant. Enter closes the menu after toggling; Space keeps it open. This allows users to change multiple checkbox items in sequence with Space.

## Down Arrow

- **In menubar on parent item:** opens submenu, focuses first item
- **In menu:** focuses next item (wrapping from last to first is optional)

## Up Arrow

- **In menu:** focuses previous item (wrapping from first to last is optional)
- **In menubar on parent item:** (optional) opens submenu, focuses last item

## Right Arrow

- **In menubar:** focuses next menubar item (wrapping is optional)
- **In menu on parent menuitem:** opens submenu, focuses first item
- **In menu on non-parent item:** closes current submenu, moves focus right in menubar, optionally opens that item's submenu

## Left Arrow

- **In menubar:** focuses previous menubar item (wrapping is optional)
- **In submenu (not top-level menu):** closes submenu, focuses parent menuitem
- **In top-level menu from menubar:** closes menu, moves focus left in menubar, optionally opens that item's submenu

## Escape

- Closes the current menu
- Returns focus to the invoking element (menu button or parent menuitem)

## Home

- Focuses first item in the current menu/menubar

## End

- Focuses last item in the current menu/menubar

## Character Keys (Optional)

- Focuses next item whose label starts with the typed character
- If multiple items start with the same character, cycles through them

---

## Menu Button Keyboard Interaction

Source: [APG Menu Button Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/)

### On the Button (Menu Closed)

| Key | Action |
|-----|--------|
| Enter | Opens menu, focuses first item |
| Space | Opens menu, focuses first item |
| Down Arrow | (Optional) Opens menu, focuses first item |
| Up Arrow | (Optional) Opens menu, focuses last item |

### Once Menu Is Open

Keyboard behavior follows the menu pattern above.

### Focus Management

- **Open:** focus moves to first menu item (or checked item for persistent selections — [Pickering](https://inclusive-components.design/menus-menu-buttons/))
- **Close (Escape or activation):** focus returns to the button
- **Tab:** exits the menu and closes it

---

## Implementation Notes

### Roving Tabindex

The recommended focus management approach:

1. First menubar item: `tabindex="0"`
2. All other items: `tabindex="-1"`
3. When focus moves, update `tabindex` values accordingly
4. The menu container itself should not be in the tab order

### Alternative: `aria-activedescendant`

Instead of roving tabindex, the container can manage focus via `aria-activedescendant`:

1. Container gets `tabindex="0"` and receives focus
2. `aria-activedescendant` is set to the ID of the visually focused item
3. Arrow keys update `aria-activedescendant` without moving DOM focus

Both approaches are valid per the APG specification.
