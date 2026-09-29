---
name: Service Card Grid
category: cards
tags: ["cards", "services", "grid", "professional"]
industries: ["professional-services", "legal", "corporate"]
styles: ["modern", "minimal"]
moods: ["confident", "calm"]
intents: ["navigate-content"]
---

# Service Card Grid

Scannable service cards with restrained visual hierarchy.

## When to use

Use this pattern when its information hierarchy matches the content. Do not use it merely because it looks attractive.

## HTML

```html
<section class="c-services">
  <div class="c-services__grid">
    <article class="c-service-card">
      <p class="c-service-card__number">01</p>
      <h2>Service title</h2>
      <p>Concise explanation of the service and its value.</p>
      <a href="#">Learn more</a>
    </article>
    <article class="c-service-card">
      <p class="c-service-card__number">02</p>
      <h2>Service title</h2>
      <p>Concise explanation of the service and its value.</p>
      <a href="#">Learn more</a>
    </article>
  </div>
</section>
```

## CSS reference

```css
.c-services__grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1px;background:var(--color-border)}.c-service-card{padding:clamp(1.5rem,4vw,3rem);background:var(--color-surface)}.c-service-card__number{font-size:.8rem;color:var(--color-muted)}.c-service-card h2{margin:2rem 0 .75rem}@media(max-width:767px){.c-services__grid{grid-template-columns:1fr}}
```

## Accessibility

- Keep semantic elements.
- Preserve visible focus.
- Do not rely on color alone.
- Test keyboard navigation.
- Verify contrast against the final background.
