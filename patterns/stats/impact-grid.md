---
name: Impact Statistics Grid
category: stats
tags: ["stats", "metrics", "credibility", "corporate"]
industries: ["corporate", "saas", "professional-services"]
styles: ["corporate", "minimal"]
moods: ["confident", "technical"]
intents: ["build-credibility", "establish-trust"]
---

# Impact Statistics Grid

A restrained metrics section for communicating scale, evidence or outcomes.

## When to use

Use this pattern when it matches the content intent and information hierarchy.

## HTML

```html
<section class="c-stats" aria-labelledby="stats-title">
  <div class="c-stats__intro">
    <p class="c-eyebrow">At a glance</p>
    <h2 id="stats-title">Evidence that supports the story.</h2>
  </div>
  <div class="c-stats__grid">
    <div class="c-stat"><strong>98%</strong><span>Customer satisfaction</span></div>
    <div class="c-stat"><strong>24k</strong><span>Projects delivered</span></div>
    <div class="c-stat"><strong>12+</strong><span>Years of experience</span></div>
  </div>
</section>
```

## CSS reference

```css
.c-stats{padding:var(--space-section) var(--space-content)}.c-stats__grid{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--color-border);border-bottom:1px solid var(--color-border)}.c-stat{padding:2rem;border-right:1px solid var(--color-border)}.c-stat:last-child{border-right:0}.c-stat strong{display:block;font-size:clamp(2rem,5vw,4rem);line-height:1}.c-stat span{display:block;margin-top:.75rem;color:var(--color-muted)}@media(max-width:767px){.c-stats__grid{grid-template-columns:1fr}.c-stat{border-right:0;border-bottom:1px solid var(--color-border)}.c-stat:last-child{border-bottom:0}}
```

## Accessibility

- Preserve semantic HTML.
- Maintain visible keyboard focus.
- Do not rely on color alone.
- Verify contrast in the final theme.
- Test at narrow viewport widths.
