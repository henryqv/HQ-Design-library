---
name: Editorial Testimonial
category: testimonials
tags: ["testimonials", "social-proof", "editorial"]
industries: ["professional-services", "editorial", "legal"]
styles: ["minimal", "editorial"]
moods: ["calm", "trustworthy"]
intents: ["navigate-content"]
---

# Editorial Testimonial

Large quotation with restrained attribution.

## When to use

Use this pattern when its information hierarchy matches the content. Do not use it merely because it looks attractive.

## HTML

```html
<figure class="c-quote">
  <blockquote>“A concise statement that communicates the experience without becoming a wall of text.”</blockquote>
  <figcaption>
    <strong>Person Name</strong>
    <span>Role, Organization</span>
  </figcaption>
</figure>
```

## CSS reference

```css
.c-quote{max-width:60rem;margin:auto;padding:var(--space-section) var(--space-content)}.c-quote blockquote{margin:0;font-family:var(--font-display);font-size:clamp(2rem,4vw,3.5rem);line-height:1.12}.c-quote figcaption{display:grid;gap:.2rem;margin-top:2rem;color:var(--color-muted)}
```

## Accessibility

- Keep semantic elements.
- Preserve visible focus.
- Do not rely on color alone.
- Test keyboard navigation.
- Verify contrast against the final background.
