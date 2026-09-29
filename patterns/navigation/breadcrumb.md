---
name: Breadcrumb Navigation
category: navigation
tags: ["breadcrumb", "navigation", "wayfinding", "accessibility"]
industries: ["general", "legal", "ecommerce", "editorial"]
styles: ["minimal", "editorial", "corporate"]
moods: ["calm", "technical"]
intents: ["navigate-content", "reduce-friction"]
---

# Breadcrumb Navigation

A compact semantic breadcrumb for deep content hierarchies.

## When to use

Use this pattern when it matches the content intent and information hierarchy.

## HTML

```html
<nav class="c-breadcrumb" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/services/">Services</a></li>
    <li aria-current="page">Current page</li>
  </ol>
</nav>
```

## CSS reference

```css
.c-breadcrumb{padding:1rem var(--space-content);font-size:.875rem}.c-breadcrumb ol{display:flex;gap:.6rem;flex-wrap:wrap;list-style:none;padding:0;margin:0}.c-breadcrumb li+li:before{content:'/';margin-right:.6rem;color:var(--color-muted)}.c-breadcrumb [aria-current]{color:var(--color-muted)}
```

## Accessibility

- Preserve semantic HTML.
- Maintain visible keyboard focus.
- Do not rely on color alone.
- Verify contrast in the final theme.
- Test at narrow viewport widths.
