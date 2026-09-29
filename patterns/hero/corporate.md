---
name: Corporate Hero
category: hero
tags: ["hero", "corporate", "b2b", "conversion"]
industries: ["corporate", "saas", "professional-services"]
styles: ["modern", "minimal"]
moods: ["confident", "calm"]
intents: ["navigate-content"]
---

# Corporate Hero

Two-column hero with clear product/value hierarchy.

## When to use

Use this pattern when its information hierarchy matches the content. Do not use it merely because it looks attractive.

## HTML

```html
<section class="c-hero c-hero--corporate">
  <div class="c-hero__content">
    <p class="c-hero__eyebrow">Category</p>
    <h1>Make complex work easier to understand.</h1>
    <p>Short supporting copy explains the outcome and establishes credibility.</p>
    <a class="c-button c-button--primary" href="#">Get started</a>
  </div>
  <div class="c-hero__media" aria-hidden="true"></div>
</section>
```

## CSS reference

```css
.c-hero--corporate{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(2rem,6vw,6rem);align-items:center;padding:var(--space-section) var(--space-content)}.c-hero__content{max-width:42rem}.c-hero__media{min-height:28rem;background:var(--color-surface);border-radius:var(--radius-card)}@media(max-width:767px){.c-hero--corporate{grid-template-columns:1fr}.c-hero__media{min-height:16rem}}
```

## Accessibility

- Keep semantic elements.
- Preserve visible focus.
- Do not rely on color alone.
- Test keyboard navigation.
- Verify contrast against the final background.
