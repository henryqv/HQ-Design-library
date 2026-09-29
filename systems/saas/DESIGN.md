---
version: "0.2.0"
name: SaaS
description: Product-led, modular and conversion-aware. Suitable for software and digital products.
colors:
  background: "#F8FAFC"
  surface: "#FFFFFF"
  text: "#101828"
  muted: "#667085"
  primary: "#635BFF"
  accent: "#12B76A"
  border: "#E4E7EC"
typography:
  headline-display:
    fontFamily: Inter, Arial, sans-serif
    fontSize: 4.5rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter, Arial, sans-serif
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.15
  headline-md:
    fontFamily: Inter, Arial, sans-serif
    fontSize: 2rem
    fontWeight: 600
    lineHeight: 1.25
  body-lg:
    fontFamily: Inter, Arial, sans-serif
    fontSize: 1.25rem
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
    letterSpacing: 0.03em
rounded:
  sm: 10px
  md: 16px
  lg: 24px
  full: 9999px
spacing:
  section: clamp(4rem, 8vw, 8rem)
  content: clamp(1rem, 3vw, 2rem)
  gutter: 24px
  margin: 32px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 24px
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: 10px
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.text}"
    rounded: "{rounded.full}"
    padding: 4px
  meta:
    textColor: "{colors.muted}"
    typography: "{typography.label-md}"
---

# SaaS

## Overview

Product-led, modular and conversion-aware. Suitable for software and digital products. The product's value leads every screen, surfaces are built from consistent modular cards, primary actions stay visible at all times, and states/feedback (success, error, loading) are always shown clearly.

## Colors

- **Primary (#635BFF):** a vivid indigo/violet for primary actions and key interactive states — the loudest color in the system, reserved for what matters.
- **Accent (#12B76A):** a clear success green, used for positive states and small highlights (badges, status dots).
- **Surface (#FFFFFF) on Background (#F8FAFC):** modular cards sit on a barely-tinted cool grey canvas — enough separation to read as distinct surfaces without heavy shadows.
- **Text (#101828) / Muted (#667085):** near-black for primary copy, a cool grey for secondary labels, timestamps and helper text.
- **Border (#E4E7EC):** a light, cool hairline around cards, inputs and dividers.

## Typography

Inter throughout, leaning bolder than the Corporate system (700 weight on display/headline levels) to give the product confidence and energy. Body copy stays at a comfortable 400 weight; labels pick up medium weight and slight letter-spacing to read clearly at small sizes in dense UI.

## Layout

A fluid section rhythm (`clamp(4rem, 8vw, 8rem)`) and the same content spacing (`clamp(1rem, 3vw, 2rem)`) used elsewhere in the catalog — but the larger `rounded` and `spacing` scale gives cards more visual weight, matching a "modular surfaces" product UI rather than an editorial page.

## Elevation & Depth

Flat, with the `border` hairline and `surface`/`background` contrast doing the separation — no drop shadows, keeping the product feeling fast and modern rather than skeuomorphic.

## Shapes

The most rounded system in the catalog — 16px cards, 10px buttons — a friendly, contemporary product feel that still reads as systematic, not playful.

## Components

- **Buttons:** primary fills with the vivid `{colors.primary}` and white text — the single loudest, most visible action on any screen.
- **Badges:** a small `accent` green pill with dark text — status indicators (e.g. "Active", "Synced") that need to read instantly without shouting.

## Do's and Don'ts

- Do lead with product value — the hero and primary CTA should never be buried.
- Do use modular, card-based surfaces consistently across the product.
- Do show states and feedback clearly — success, error and loading all need a visible treatment.
- Don't let secondary actions compete visually with the primary `{colors.primary}` button.
