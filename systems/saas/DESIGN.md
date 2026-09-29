---
name: SaaS
version: 0.1.0
category: saas
---

# SaaS

Product-led, modular and conversion-aware. Suitable for software and digital products.

## Principles

- Lead with the product value.
- Use modular surfaces.
- Keep actions visible.
- Show states and feedback clearly.

## Tokens

```json
{
  "colors": {
    "background": "#F8FAFC",
    "surface": "#FFFFFF",
    "text": "#101828",
    "muted": "#667085",
    "primary": "#635BFF",
    "accent": "#12B76A",
    "border": "#E4E7EC"
  },
  "typography": {
    "display": "Inter, Arial, sans-serif",
    "body": "Inter, Arial, sans-serif",
    "scale": {
      "xs": "0.75rem",
      "sm": "0.875rem",
      "md": "1rem",
      "lg": "1.25rem",
      "xl": "2rem",
      "2xl": "3rem",
      "3xl": "4.5rem"
    }
  },
  "spacing": {
    "section": "clamp(4rem, 8vw, 8rem)",
    "content": "clamp(1rem, 3vw, 2rem)"
  },
  "radius": {
    "card": "16px",
    "button": "10px"
  }
}
```

## Implementation

Translate the tokens into CSS custom properties or the project's existing token system.
Do not assume React, Tailwind or a component framework.
