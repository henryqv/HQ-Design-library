---
name: Editorial
version: 0.1.0
category: editorial
---

# Editorial

Typography-led, spacious and content-first. Suitable for publishing, professional services and institutional storytelling.

## Principles

- Typography establishes hierarchy.
- Whitespace separates ideas.
- Photography should support rather than dominate content.
- Use restrained accents.

## Tokens

```json
{
  "colors": {
    "background": "#F7F6F2",
    "surface": "#FFFFFF",
    "text": "#1B1B1B",
    "muted": "#6B6B67",
    "primary": "#1F3A4A",
    "accent": "#A47C48",
    "border": "#DDD9D0"
  },
  "typography": {
    "display": "Georgia, 'Times New Roman', serif",
    "body": "Inter, Arial, sans-serif",
    "scale": {
      "xs": "0.75rem",
      "sm": "0.875rem",
      "md": "1rem",
      "lg": "1.25rem",
      "xl": "2rem",
      "2xl": "3.5rem",
      "3xl": "5rem"
    }
  },
  "spacing": {
    "section": "clamp(4rem, 9vw, 8rem)",
    "content": "clamp(1rem, 3vw, 2rem)"
  },
  "radius": {
    "card": "8px",
    "button": "4px"
  }
}
```

## Implementation

Translate the tokens into CSS custom properties or the project's existing token system.
Do not assume React, Tailwind or a component framework.
