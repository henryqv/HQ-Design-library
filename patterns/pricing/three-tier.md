---
name: Three Tier Pricing
category: pricing
tags: ["pricing", "conversion", "comparison", "saas"]
industries: ["saas", "ecommerce", "professional-services"]
styles: ["corporate", "modern", "minimal"]
moods: ["confident", "technical"]
intents: ["compare-options", "drive-signup", "reduce-friction"]
---

# Three Tier Pricing

Three-plan comparison with a clear primary tier.

## When to use

Use this pattern when it matches the content intent and information hierarchy.

## HTML

```html
<section class="c-pricing" aria-labelledby="pricing-title">
  <div class="c-pricing__intro"><h2 id="pricing-title">Choose the right plan.</h2></div>
  <div class="c-pricing__grid">
    <article class="c-plan"><h3>Essential</h3><p class="c-plan__price">€29</p><a href="#">Choose plan</a></article>
    <article class="c-plan c-plan--featured"><p class="c-plan__badge">Popular</p><h3>Professional</h3><p class="c-plan__price">€79</p><a href="#">Choose plan</a></article>
    <article class="c-plan"><h3>Business</h3><p class="c-plan__price">€149</p><a href="#">Choose plan</a></article>
  </div>
</section>
```

## CSS reference

```css
.c-pricing{padding:var(--space-section) var(--space-content)}.c-pricing__grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin-top:2rem}.c-plan{position:relative;padding:2rem;border:1px solid var(--color-border);background:var(--color-surface)}.c-plan--featured{border:2px solid var(--color-primary)}.c-plan__price{font-size:2.5rem;font-weight:700}.c-plan a{display:inline-block;margin-top:1rem}@media(max-width:767px){.c-pricing__grid{grid-template-columns:1fr}}
```

## Accessibility

- Preserve semantic HTML.
- Maintain visible keyboard focus.
- Do not rely on color alone.
- Verify contrast in the final theme.
- Test at narrow viewport widths.
