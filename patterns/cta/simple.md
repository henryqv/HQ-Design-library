---
name: Simple CTA
category: cta
tags: ["cta", "conversion", "footer"]
industries: ["general", "corporate", "saas"]
styles: ["modern", "minimal"]
moods: ["confident", "calm"]
intents: ["navigate-content"]
---

# Simple CTA

Focused call to action with one clear next step.

## When to use

Use this pattern when its information hierarchy matches the content. Do not use it merely because it looks attractive.

## HTML

```html
<section class="c-cta">
  <div class="c-cta__inner">
    <h2>Ready to take the next step?</h2>
    <p>One sentence of supporting context.</p>
    <a class="c-button c-button--primary" href="#">Contact us</a>
  </div>
</section>
```

## CSS reference

```css
.c-cta{padding:var(--space-section) var(--space-content);background:var(--color-primary);color:#fff}.c-cta__inner{max-width:56rem;margin:auto;text-align:center}.c-cta h2{font-size:clamp(2rem,5vw,4rem);margin:0 0 1rem}.c-cta p{opacity:.85;margin:0 auto 2rem;max-width:40rem}
```

## Accessibility

- Keep semantic elements.
- Preserve visible focus.
- Do not rely on color alone.
- Test keyboard navigation.
- Verify contrast against the final background.
