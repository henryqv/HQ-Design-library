---
name: Professional Team Grid
category: team
tags: ["team", "people", "professional-services", "credibility"]
industries: ["legal", "professional-services", "corporate", "medical"]
styles: ["editorial", "corporate", "minimal"]
moods: ["trustworthy", "calm", "authoritative"]
intents: ["build-credibility", "establish-trust"]
---

# Professional Team Grid

A restrained team presentation focused on names, roles and credibility.

## When to use

Use this pattern when it matches the content intent and information hierarchy.

## HTML

```html
<section class="c-team" aria-labelledby="team-title">
  <div class="c-team__intro">
    <p class="c-eyebrow">Our people</p>
    <h2 id="team-title">The people behind the work.</h2>
  </div>
  <div class="c-team__grid">
    <article class="c-person"><div class="c-person__image"></div><h3>Name Surname</h3><p>Partner / Director</p></article>
    <article class="c-person"><div class="c-person__image"></div><h3>Name Surname</h3><p>Senior Associate</p></article>
    <article class="c-person"><div class="c-person__image"></div><h3>Name Surname</h3><p>Consultant</p></article>
  </div>
</section>
```

## CSS reference

```css
.c-team{padding:var(--space-section) var(--space-content)}.c-team__grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem}.c-person__image{aspect-ratio:4/5;background:var(--color-surface);margin-bottom:1rem}.c-person h3{margin:.25rem 0}.c-person p{color:var(--color-muted);margin:0}@media(max-width:767px){.c-team__grid{grid-template-columns:1fr 1fr}}@media(max-width:520px){.c-team__grid{grid-template-columns:1fr}}
```

## Accessibility

- Preserve semantic HTML.
- Maintain visible keyboard focus.
- Do not rely on color alone.
- Verify contrast in the final theme.
- Test at narrow viewport widths.
