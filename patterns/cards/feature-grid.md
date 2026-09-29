---
name: Feature Grid
category: cards
tags: ["features", "cards", "grid", "benefits"]
industries: ["saas", "corporate", "education", "medical"]
styles: ["modern", "corporate", "minimal"]
moods: ["technical", "confident", "friendly"]
intents: ["explain-product", "differentiate", "educate"]
---

# Feature Grid

A modular grid for communicating product or service benefits.

## When to use

Use this pattern when it matches the content intent and information hierarchy.

## HTML

```html
<section class="c-features" aria-labelledby="features-title">
  <h2 id="features-title">Why it works</h2>
  <div class="c-features__grid">
    <article><span aria-hidden="true">01</span><h3>Clear benefit</h3><p>Explain the practical outcome.</p></article>
    <article><span aria-hidden="true">02</span><h3>Clear benefit</h3><p>Explain the practical outcome.</p></article>
    <article><span aria-hidden="true">03</span><h3>Clear benefit</h3><p>Explain the practical outcome.</p></article>
  </div>
</section>
```

## CSS reference

```css
.c-features{padding:var(--space-section) var(--space-content)}.c-features__grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin-top:2rem}.c-features article{padding:1.5rem;border:1px solid var(--color-border)}.c-features article span{font-size:.8rem;color:var(--color-muted)}@media(max-width:767px){.c-features__grid{grid-template-columns:1fr}}
```

## Accessibility

- Preserve semantic HTML.
- Maintain visible keyboard focus.
- Do not rely on color alone.
- Verify contrast in the final theme.
- Test at narrow viewport widths.
