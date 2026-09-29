---
name: Luxury
version: 0.1.0
category: luxury
---

# Luxury

Minimal, tactile and image-led. Suitable for premium brands, hospitality and high-end services.

## Principles

- Use fewer elements.
- Let imagery breathe.
- Use typography as an object.
- Avoid unnecessary UI decoration.

## Tokens

```json
{
  "colors": {
    "background": "#F3F0EA",
    "surface": "#FCFBF8",
    "text": "#191816",
    "muted": "#77736C",
    "primary": "#191816",
    "accent": "#A58B63",
    "border": "#D8D1C4"
  },
  "typography": {
    "display": "Georgia, 'Times New Roman', serif",
    "body": "Arial, sans-serif",
    "scale": {
      "xs": "0.7rem",
      "sm": "0.8rem",
      "md": "0.95rem",
      "lg": "1.15rem",
      "xl": "1.8rem",
      "2xl": "3.2rem",
      "3xl": "5.5rem"
    }
  },
  "spacing": {
    "section": "clamp(5rem, 12vw, 11rem)",
    "content": "clamp(1rem, 4vw, 3rem)"
  },
  "radius": {
    "card": "0px",
    "button": "0px"
  }
}
```

## Implementation

Translate the tokens into CSS custom properties or the project's existing token system.
Do not assume React, Tailwind or a component framework.
