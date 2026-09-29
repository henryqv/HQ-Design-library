---
name: Simple Footer
category: footer
tags: ["footer", "navigation", "responsive"]
industries: ["general", "corporate", "saas", "editorial"]
styles: ["modern", "minimal"]
moods: ["confident", "calm"]
intents: ["navigate-content"]
---

# Simple Footer

Four-column footer that collapses to a readable mobile layout.

## When to use

Use this pattern when its information hierarchy matches the content. Do not use it merely because it looks attractive.

## HTML

```html
<footer class="c-footer">
  <div class="c-footer__grid">
    <div><a class="c-footer__brand" href="/">Brand</a></div>
    <nav aria-label="Footer"><a href="#">About</a><a href="#">Services</a><a href="#">Contact</a></nav>
    <nav aria-label="Legal"><a href="#">Privacy</a><a href="#">Terms</a></nav>
  </div>
</footer>
```

## CSS reference

```css
.c-footer{padding:4rem var(--space-content);border-top:1px solid var(--color-border)}.c-footer__grid{display:grid;grid-template-columns:2fr 1fr 1fr;gap:2rem}.c-footer nav{display:grid;gap:.6rem}@media(max-width:767px){.c-footer__grid{grid-template-columns:1fr}}
```

## Accessibility

- Keep semantic elements.
- Preserve visible focus.
- Do not rely on color alone.
- Test keyboard navigation.
- Verify contrast against the final background.
