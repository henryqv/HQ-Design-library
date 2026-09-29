---
name: Simple Header Navigation
category: navigation
tags: ["navigation", "header", "responsive", "accessibility"]
industries: ["general", "corporate", "saas", "ecommerce"]
styles: ["modern", "minimal"]
moods: ["confident", "calm"]
intents: ["navigate-content"]
---

# Simple Header Navigation

Accessible navigation with a strong primary action.

## When to use

Use this pattern when its information hierarchy matches the content. Do not use it merely because it looks attractive.

## HTML

```html
<header class="c-header">
  <a class="c-header__brand" href="/">Brand</a>
  <nav class="c-header__nav" aria-label="Primary">
    <a href="#">Services</a>
    <a href="#">About</a>
    <a href="#">Insights</a>
    <a class="c-button c-button--primary" href="#">Contact</a>
  </nav>
</header>
```

## CSS reference

```css
.c-header{display:flex;align-items:center;justify-content:space-between;gap:2rem;padding:1rem var(--space-content);border-bottom:1px solid var(--color-border)}.c-header__nav{display:flex;align-items:center;gap:1.5rem}@media(max-width:767px){.c-header__nav{gap:.75rem}.c-header__nav a:not(.c-button){display:none}}
```

## Accessibility

- Keep semantic elements.
- Preserve visible focus.
- Do not rely on color alone.
- Test keyboard navigation.
- Verify contrast against the final background.
