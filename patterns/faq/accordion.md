---
name: Accessible FAQ
category: faq
tags: ["faq", "accordion", "content", "accessibility"]
industries: ["general", "legal", "saas", "ecommerce", "education"]
styles: ["minimal", "editorial"]
moods: ["calm", "trustworthy"]
intents: ["educate", "reduce-friction", "establish-trust"]
---

# Accessible FAQ

Native details/summary FAQ that works without JavaScript.

## When to use

Use this pattern when it matches the content intent and information hierarchy.

## HTML

```html
<section class="c-faq" aria-labelledby="faq-title">
  <h2 id="faq-title">Frequently asked questions</h2>
  <div class="c-faq__items">
    <details><summary>Question goes here</summary><p>Answer content goes here.</p></details>
    <details><summary>Another question</summary><p>Answer content goes here.</p></details>
  </div>
</section>
```

## CSS reference

```css
.c-faq{padding:var(--space-section) var(--space-content);max-width:64rem;margin:auto}.c-faq__items{margin-top:2rem;border-top:1px solid var(--color-border)}.c-faq details{border-bottom:1px solid var(--color-border);padding:1.25rem 0}.c-faq summary{cursor:pointer;font-weight:600}.c-faq details p{max-width:52rem;color:var(--color-muted);line-height:1.7;margin:1rem 0 0}
```

## Accessibility

- Preserve semantic HTML.
- Maintain visible keyboard focus.
- Do not rely on color alone.
- Verify contrast in the final theme.
- Test at narrow viewport widths.
