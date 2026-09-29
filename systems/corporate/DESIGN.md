---
name: Corporate
version: 0.1.0
category: corporate
---

# Corporate

Clear, trustworthy and systematic. Suitable for B2B, consulting, technology and institutional sites.

## Principles

- Clarity before decoration.
- Use grids consistently.
- Make actions obvious.
- Keep information density controlled.

## Tokens

```json
{
  "colors": {
    "background": "#F5F7FA",
    "surface": "#FFFFFF",
    "text": "#172033",
    "muted": "#5E6878",
    "primary": "#1456D8",
    "accent": "#11A36A",
    "border": "#DCE2EA"
  },
  "typography": {
    "display": "Inter, Arial, sans-serif",
    "body": "Inter, Arial, sans-serif",
    "scale": {
      "xs": "0.75rem",
      "sm": "0.875rem",
      "md": "1rem",
      "lg": "1.25rem",
      "xl": "1.75rem",
      "2xl": "2.75rem",
      "3xl": "4rem"
    }
  },
  "spacing": {
    "section": "clamp(4rem, 8vw, 7rem)",
    "content": "clamp(1rem, 3vw, 2rem)"
  },
  "radius": {
    "card": "12px",
    "button": "8px"
  }
}
```

## Implementation

Translate the tokens into CSS custom properties or the project's existing token system.
Do not assume React, Tailwind or a component framework.
