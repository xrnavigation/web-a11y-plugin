# Live Region Recipes
## Contents

- [Form Validation Errors](#form-validation-errors)
  - [Vanilla HTML/JS](#vanilla-htmljs)
  - [React](#react)
  - [Angular](#angular)
  - [Vue](#vue)
- [Search Results Count](#search-results-count)
  - [Vanilla HTML/JS](#vanilla-htmljs-1)
  - [React](#react-1)
- [Loading States](#loading-states)
  - [Vanilla HTML/JS](#vanilla-htmljs-2)
  - [React](#react-2)
- [SPA Route Changes](#spa-route-changes)
  - [Vanilla HTML/JS](#vanilla-htmljs-3)
  - [React](#react-3)
  - [Angular (using CDK LiveAnnouncer)](#angular-using-cdk-liveannouncer)
- [Chat / Message Log](#chat-message-log)
- [Global Announcer Services](#global-announcer-services)
  - [Angular: CDK LiveAnnouncer](#angular-cdk-liveannouncer)
  - [React: @react-aria/live-announcer](#react-react-arialive-announcer)
  - [Vue: @vue-a11y/announcer](#vue-vue-a11yannouncer)
- [Universal Framework Guidance](#universal-framework-guidance)


Complete implementation patterns for common live region use cases, with framework-specific variants.

---

## Form Validation Errors

Use `role="alert"` (implicit `aria-live="assertive"`, implicit `aria-atomic="true"`) because validation errors are important and time-sensitive.

### Vanilla HTML/JS

```html
<!-- Container exists from page load -->
<div id="form-errors" role="alert" aria-atomic="true"></div>
```

```javascript
function showErrors(errors) {
  const container = document.getElementById('form-errors');
  container.textContent = errors.join('. ');
  // role="alert" provides assertive announcement
}

function clearErrors() {
  document.getElementById('form-errors').textContent = '';
}
```

### React

```tsx
// Container always mounted — never conditionally render
function FormErrors({ errors }: { errors: string[] }) {
  return (
    <div role="alert" aria-atomic="true">
      {errors.length > 0 ? errors.join('. ') : ''}
    </div>
  );
}
```

### Angular

```html
<!-- Use [hidden] instead of @if to preserve DOM presence -->
<div role="alert" aria-atomic="true">
  {{ errors.join('. ') }}
</div>
```

### Vue

```vue
<template>
  <!-- v-show keeps element in DOM; v-if would destroy it -->
  <div role="alert" aria-atomic="true">
    {{ errors.join('. ') }}
  </div>
</template>
```

---

## Search Results Count

Use `role="status"` (implicit `aria-live="polite"`, implicit `aria-atomic="true"`) — informational, not urgent.

### Vanilla HTML/JS

```html
<div id="search-status" role="status"></div>
```

```javascript
function updateResults(count) {
  document.getElementById('search-status').textContent =
    `${count} results found`;
}
```

### React

```tsx
function SearchStatus({ count }: { count: number }) {
  return <div role="status">{count} results found</div>;
}
```

---

## Loading States

Use `aria-busy` to suppress intermediate announcements. Because `aria-busy` support is inconsistent, also provide a simple polite announcement.

### Vanilla HTML/JS

```html
<div id="loading-region" aria-live="polite" aria-busy="false">
  <p>Content here</p>
</div>
```

```javascript
async function loadContent() {
  const region = document.getElementById('loading-region');
  region.setAttribute('aria-busy', 'true');
  region.textContent = 'Loading...';

  const data = await fetchData();

  region.textContent = data.content;
  region.setAttribute('aria-busy', 'false');
  // Only this final state is announced (if aria-busy is supported)
}
```

### React

```tsx
function LoadingRegion({ isLoading, content }: { isLoading: boolean; content: string }) {
  return (
    <div aria-live="polite" aria-busy={isLoading}>
      {isLoading ? 'Loading...' : content}
    </div>
  );
}
```

---

## SPA Route Changes

SPAs replace content without a full page load, so screen readers receive no navigation announcement. Use two complementary strategies:

1. **Live region announcement:** Announce the new page title.
2. **Focus management:** Move focus to the new page's `<h1>` (with `tabindex="-1"`).

Source: [Almero Steyn](https://almerosteyn.com/2017/03/accessible-react-navigation)

### Vanilla HTML/JS

```html
<!-- Visually hidden, persistent from page load -->
<div id="route-announcer" aria-live="polite" class="sr-only"></div>
```

```javascript
router.onRouteChange((newRoute) => {
  document.getElementById('route-announcer').textContent =
    `Navigated to ${newRoute.title}`;

  // Also move focus to the main heading
  const h1 = document.querySelector('h1');
  if (h1) {
    h1.setAttribute('tabindex', '-1');
    h1.focus();
  }
});
```

### React

```tsx
import { useEffect, useRef } from 'react';
import { useLocation } from 'react-router-dom';

function RouteAnnouncer() {
  const location = useLocation();
  const [announcement, setAnnouncement] = useState('');

  useEffect(() => {
    setAnnouncement(`Navigated to ${document.title}`);
  }, [location.pathname]);

  return (
    <div aria-live="polite" className="sr-only">
      {announcement}
    </div>
  );
}
```

### Angular (using CDK LiveAnnouncer)

```typescript
import { LiveAnnouncer } from '@angular/cdk/a11y';
import { Router, NavigationEnd } from '@angular/router';
import { filter } from 'rxjs';

@Component({ /* ... */ })
export class AppComponent {
  #liveAnnouncer = inject(LiveAnnouncer);
  #router = inject(Router);

  constructor() {
    this.#router.events.pipe(
      filter(e => e instanceof NavigationEnd)
    ).subscribe(() => {
      this.#liveAnnouncer.announce(
        `Navigated to ${document.title}`, 'polite'
      );
    });
  }
}
```

---

## Chat / Message Log

Use `role="log"` with `aria-relevant="additions"` to announce only new messages.

```html
<div role="log" aria-live="polite" aria-relevant="additions">
  <!-- New messages appended here -->
</div>
```

```javascript
function addMessage(text, sender) {
  const log = document.querySelector('[role="log"]');
  const msg = document.createElement('p');
  msg.textContent = `${sender}: ${text}`;
  log.appendChild(msg);
  // Only the new message is announced
}
```

Note: Add redundant `aria-live="polite"` on `role="log"` for compatibility with older screen readers. ([MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions))

---

## Global Announcer Services

Prefer a global announcer over local live regions. A single persistent container at the app root avoids all timing and lifecycle issues.

### Angular: CDK LiveAnnouncer

```typescript
import { LiveAnnouncer } from '@angular/cdk/a11y';

@Component({
  selector: 'app-save-button',
  template: `<button (click)="onSave()">Save</button>`
})
export class SaveButton {
  #liveAnnouncer = inject(LiveAnnouncer);

  onSave() {
    this.#liveAnnouncer.announce('Settings saved.', 'polite');
  }
}
```

Source: [Angular CDK LiveAnnouncer](https://github.com/angular/components/blob/main/src/cdk/a11y/live-announcer/live-announcer.md)

### React: @react-aria/live-announcer

```tsx
import { announce } from '@react-aria/live-announcer';

function SaveButton() {
  const handleSave = () => {
    announce('Settings saved.', 'polite');
  };
  return <button onClick={handleSave}>Save</button>;
}
```

Source: [Almero Steyn](https://almerosteyn.com/2017/09/aria-live-regions-in-react)

### Vue: @vue-a11y/announcer

```vue
<script setup>
import { useAnnouncer } from '@vue-a11y/announcer';
const { polite } = useAnnouncer();

function onSave() {
  polite('Settings saved.');
}
</script>
```

Source: [dev.to](https://dev.to/dkoppenhagen/when-your-live-region-isnt-live-fixing-aria-live-in-angular-react-and-vue-1g0j)

---

## Universal Framework Guidance

1. **Prefer a global announcer service** over local live regions.
2. **Never conditionally render live region containers.** Use CSS hiding to preserve DOM presence.
3. **Update text content, not element structure.** Replacing the node containing `aria-live` breaks registration.
4. **Debounce rapid updates** to prevent announcement spam.
