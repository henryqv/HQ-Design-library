---
name: Ecommerce
version: 0.1.0
category: ecommerce
---

# Ecommerce

Product-focused, scannable and conversion-aware while maintaining a strong editorial hierarchy.

## Principles

- Products remain the visual focus.
- Make comparison easy.
- Keep checkout friction low.
- Use consistent image ratios.

## Tokens

```json
{
  "colors": {
    "background": "#FFFFFF",
    "surface": "#F7F7F5",
    "text": "#171717",
    "muted": "#666666",
    "primary": "#171717",
    "accent": "#C65A3A",
    "border": "#E5E5E2"
  },
  "typography": {
    "display": "Inter, Arial, sans-serif",
    "body": "Inter, Arial, sans-serif",
    "scale": {
      "xs": "0.75rem",
      "sm": "0.875rem",
      "md": "1rem",
      "lg": "1.2rem",
      "xl": "1.8rem",
      "2xl": "2.75rem",
      "3xl": "4rem"
    }
  },
  "spacing": {
    "section": "clamp(3rem, 7vw, 6rem)",
    "content": "clamp(1rem, 3vw, 2rem)"
  },
  "radius": {
    "card": "4px",
    "button": "4px"
  }
}
```

## Implementation

Translate the tokens into CSS custom properties or the project's existing token system.
Do not assume React, Tailwind or a component framework.
