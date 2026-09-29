---
version: "0.2.0"
name: Corporate
description: Clear, trustworthy and systematic. Suitable for B2B, consulting, technology and institutional sites.
colors:
  background: "#F5F7FA"
  surface: "#FFFFFF"
  text: "#172033"
  muted: "#5E6878"
  primary: "#1456D8"
  accent: "#11A36A"
  border: "#DCE2EA"
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
    fontSize: 1.75rem
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
    letterSpacing: 0.04em
rounded:
  sm: 8px
  md: 12px
  lg: 20px
  full: 9999px
spacing:
  section: clamp(4rem, 8vw, 7rem)
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

# Corporate

## Overview

Clear, trustworthy and systematic. Suitable for B2B, consulting, technology and institutional sites. Clarity comes before decoration, actions stay obvious, and information density is kept under control so a busy B2B page still reads calmly.

## Colors

- **Primary (#1456D8):** a confident, saturated blue reserved for primary actions and key interactive elements — never used decoratively.
- **Accent (#11A36A):** a supporting green for success states and secondary emphasis, used sparingly.
- **Surface (#FFFFFF) on Background (#F5F7FA):** content lives on white cards that sit on a very light grey canvas, giving just enough separation without heavy borders.
- **Text (#172033) / Muted (#5E6878):** near-black for primary copy, a cooler grey for secondary/metadata text.
- **Border (#DCE2EA):** a quiet neutral for dividers and card outlines — never a focal point.

## Typography

Inter carries the whole system, from display headlines down to labels — one typeface, systematic weight and size steps, so the hierarchy comes from scale and weight rather than mixing families. Headlines sit at 600–700 weight for confidence; body copy stays at 400 for long-form readability; labels pick up a touch of letter-spacing and medium weight to read as metadata rather than prose.

## Layout

Sections breathe with generous, fluid spacing (`clamp(4rem, 8vw, 7rem)` between major sections) that scales with the viewport instead of jumping between fixed breakpoints. Content blocks use a tighter, still-fluid rhythm (`clamp(1rem, 3vw, 2rem)`) so grids stay consistent whether viewed on mobile or a wide desktop monitor.

## Elevation & Depth

Depth is conveyed through surface contrast and the 1px `border` token, not shadows — a flat, systematic feel that reads as trustworthy rather than flashy.

## Shapes

A moderate 12px radius on cards and 8px on buttons keeps corners soft enough to feel modern without softening the system into something playful — grids stay consistent throughout.

## Components

- **Buttons:** primary buttons fill with `{colors.primary}`, white text, `{rounded.sm}` corners — the only element allowed the primary color as a background.
- **Cards:** white surface, `{rounded.md}` corners, generous internal padding so content never feels cramped against the edge.

## Do's and Don'ts

- Do keep the primary blue for actions only — never as decoration.
- Do use the grid consistently across every section.
- Do keep information density controlled, even on data-heavy B2B pages.
- Don't mix in additional accent colors beyond `accent` — the palette stays restrained on purpose.
