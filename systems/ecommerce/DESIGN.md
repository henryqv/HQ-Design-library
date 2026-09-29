---
version: "0.2.0"
name: Ecommerce
description: Product-focused, scannable and conversion-aware while maintaining a strong editorial hierarchy.
colors:
  background: "#FFFFFF"
  surface: "#F7F7F5"
  text: "#171717"
  muted: "#666666"
  primary: "#171717"
  accent: "#C65A3A"
  border: "#E5E5E2"
typography:
  headline-display:
    fontFamily: Inter, Arial, sans-serif
    fontSize: 4rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Inter, Arial, sans-serif
    fontSize: 2.75rem
    fontWeight: 700
    lineHeight: 1.15
  headline-md:
    fontFamily: Inter, Arial, sans-serif
    fontSize: 1.8rem
    fontWeight: 600
    lineHeight: 1.25
  body-lg:
    fontFamily: Inter, Arial, sans-serif
    fontSize: 1.2rem
    fontWeight: 400
    lineHeight: 1.6
  body-md:
    fontFamily: Inter, Arial, sans-serif
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: Inter, Arial, sans-serif
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5
  label-md:
    fontFamily: Inter, Arial, sans-serif
    fontSize: 0.75rem
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.04em
rounded:
  sm: 4px
  md: 4px
  lg: 8px
  full: 9999px
spacing:
  section: clamp(3rem, 7vw, 6rem)
  content: clamp(1rem, 3vw, 2rem)
  gutter: 24px
  margin: 32px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.background}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 16px
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: 10px
  meta:
    textColor: "{colors.muted}"
    typography: "{typography.label-md}"
---

# Ecommerce

## Overview

Product-focused, scannable and conversion-aware while maintaining a strong editorial hierarchy. Products stay the visual focus at every step, comparison between items is made easy, checkout friction is kept low, and image ratios stay consistent across every listing.

## Colors

- **Primary (#171717):** near-black, used for primary actions and the strongest text — product photography carries the color, the UI stays neutral.
- **Accent (#C65A3A):** a warm terracotta reserved for sparing use — sale badges, small highlights — never as a large filled surface, since it does not clear AA text contrast against either the light or dark end of this palette.
- **Surface (#F7F7F5) on Background (#FFFFFF):** a barely-there warm grey separates product cards from the pure white canvas without competing with photography.
- **Text (#171717) / Muted (#666666):** near-black for prices and titles, mid-grey for secondary details (SKU, stock, shipping notes).
- **Border (#E5E5E2):** hairline dividers between grid items, never a heavy outline.

## Typography

Inter end to end, so nothing competes with product photography for attention. Headlines stay confident but compact (the display size only appears on campaign/landing moments, not on every product page); body text favors a slightly smaller scale than an editorial system, since scanability across a grid matters more than long-form reading comfort.

## Layout

Section rhythm is tighter than an editorial system (`clamp(3rem, 7vw, 6rem)`) to keep more product grid visible per scroll. Content spacing stays fluid (`clamp(1rem, 3vw, 2rem)`) so card grids reflow cleanly from a single mobile column to a wide desktop grid.

## Elevation & Depth

No shadows — depth comes from the hairline `border` and the subtle `surface`/`background` split, keeping the focus on product imagery rather than chrome.

## Shapes

A minimal 4px radius on both cards and buttons — barely-there rounding that reads as neutral packaging, not a stylistic statement.

## Components

- **Buttons:** primary fills with `{colors.primary}` (near-black) and white text — the only strong fill in the system, reserved for "Add to cart"/checkout actions.
- **Cards:** live on `{colors.surface}`, tight `{rounded.md}` corners, compact padding so more products fit per row.

## Do's and Don'ts

- Do keep products as the visual focus — chrome and decoration stay out of the way.
- Do use consistent image ratios across every grid and listing.
- Do keep checkout friction low: fewer fields, clear primary action.
- Don't fill large surfaces with `accent` — it's reserved for small highlights only, and does not pass AA text contrast at scale.
