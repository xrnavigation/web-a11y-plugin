# Carousel Alternatives
## Contents

- [Why You Are Here](#why-you-are-here)
- [Alternative 1: Static Hero Content](#alternative-1-static-hero-content)
- [Alternative 2: Tabbed Content](#alternative-2-tabbed-content)
- [Alternative 3: Paginated Grid](#alternative-3-paginated-grid)
- [Alternative 4: Accordion / Disclosure](#alternative-4-accordion-disclosure)
- [If a Carousel Is Truly Required](#if-a-carousel-is-truly-required)
  - [Sources](#sources)


## Why You Are Here

You are about to build a carousel. Less than 1% of users click carousel features ([Notre Dame study](https://www.nngroup.com/articles/designing-effective-carousels/)). NNGroup usability testing found a user failed to find a prominent 100-pound discount displayed in the largest element on the homepage because "it keeps flashing too quickly." Eye-tracking shows animated content gets looked at only 27% of the time due to banner blindness.

This page helps you build something better.

---

## Alternative 1: Static Hero Content

**When to use:** Homepage hero, landing page feature, marketing banner.

**What to do:** Display the single most important message. No rotation. If stakeholders want multiple messages, prioritize — the carousel was hiding the fact that no one decided what mattered most.

```html
<section aria-labelledby="hero-heading">
  <h2 id="hero-heading">Spring Sale — 30% Off All Plans</h2>
  <p>Use code SPRING30 at checkout. Ends April 15.</p>
  <a href="/pricing">View pricing</a>
</section>
```

**Why it works:** Every user sees the message. No timing pressure. No motion. Screen readers announce it once. Keyboard users tab through it predictably.

---

## Alternative 2: Tabbed Content

**When to use:** Multiple content panels where the user should choose which to view (product features, plan comparisons, category highlights).

**What to do:** Use a proper tab pattern. Each panel is visible only when its tab is selected. No auto-rotation.

```html
<div role="tablist" aria-label="Product features">
  <button role="tab" aria-selected="true" aria-controls="panel-1" id="tab-1">Performance</button>
  <button role="tab" aria-selected="false" aria-controls="panel-2" id="tab-2" tabindex="-1">Security</button>
  <button role="tab" aria-selected="false" aria-controls="panel-3" id="tab-3" tabindex="-1">Integrations</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- Performance content -->
</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>
  <!-- Security content -->
</div>
<div role="tabpanel" id="panel-3" aria-labelledby="tab-3" hidden>
  <!-- Integrations content -->
</div>
```

**Keyboard behavior:** Arrow keys move between tabs. Home/End jump to first/last. Tab moves into panel content. See the `a11y-tabs` skill for full implementation.

---

## Alternative 3: Paginated Grid

**When to use:** Product listings, article collections, image galleries.

**What to do:** Display items in a static grid with pagination controls.

```html
<section aria-labelledby="products-heading">
  <h2 id="products-heading">Featured Products</h2>
  <ul>
    <li><!-- Product card 1 --></li>
    <li><!-- Product card 2 --></li>
    <li><!-- Product card 3 --></li>
  </ul>
  <nav aria-label="Product pages">
    <a href="?page=1" aria-current="page">1</a>
    <a href="?page=2">2</a>
    <a href="?page=3">3</a>
  </nav>
</section>
```

**Why it works:** Users control navigation. Position is clear. Bookmarkable. No motion. No timing pressure.

---

## Alternative 4: Accordion / Disclosure

**When to use:** Sequential content where users need to expand sections on demand (FAQs, feature details, announcements).

```html
<details>
  <summary>Spring Sale — 30% Off All Plans</summary>
  <p>Use code SPRING30 at checkout. Ends April 15.</p>
</details>
<details>
  <summary>New Feature: Team Dashboards</summary>
  <p>Collaborate in real-time with shared dashboards.</p>
</details>
```

**Why it works:** Native HTML. Keyboard accessible by default. Screen readers announce expanded/collapsed state. No JavaScript required. See the `a11y-accordion` skill for enhanced patterns.

---

## If a Carousel Is Truly Required

If stakeholders insist, apply these minimum requirements:

1. **Disable auto-advance by default.** Users control when content changes.
2. **Pause/stop controls** — keyboard-accessible, labeled ("Pause slideshow"), placed before the carousel in tab order.
3. **Hide non-visible slides** from the accessibility tree entirely (`hidden` attribute or `display: none`).
4. **Announce position** on user-initiated changes: `aria-live="polite"` region with "Slide 2 of 5."
5. **Respect `prefers-reduced-motion`** — disable all slide transitions and auto-advance.
6. **Navigation targets** — minimum 44x44px for dots/arrows ([WCAG 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)).
7. **Keyboard navigation** — arrow keys between slides, Tab to controls, Enter/Space to activate.
8. **Focus management** — focus follows the visible slide. Focus never lands on hidden content.

### Sources

- [NNGroup: Auto-Forwarding Carousels Annoy Users](https://www.nngroup.com/articles/auto-forwarding/)
- [NNGroup: Designing Effective Carousels](https://www.nngroup.com/articles/designing-effective-carousels/)
- [WebAIM: Carousels](https://webaim.org/techniques/carousels/)
- [Chrome Developers: Accessible Carousel](https://developer.chrome.com/blog/accessible-carousel)
- [A11Y Collective: Accessible Carousel Guide](https://www.a11y-collective.com/blog/accessible-carousel/)
- [Baymard: 10 UX Requirements for Homepage Carousels](https://baymard.com/blog/homepage-carousel)
