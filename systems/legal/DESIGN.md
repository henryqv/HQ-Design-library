---
version: "0.2.0"
name: Legal
description: Authoritative, calm and premium without feeling ostentatious. Suitable for law firms and professional services.
colors:
  background: "#F6F4EF"
  surface: "#FFFFFF"
  text: "#20252B"
  muted: "#687079"
  primary: "#1C2B39"
  accent: "#92754D"
  border: "#D8D2C8"
typography:
  headline-display:
    fontFamily: Georgia, "Times New Roman", serif
    fontSize: 4.5rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Georgia, "Times New Roman", serif
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.15
  headline-md:
    fontFamily: Georgia, "Times New Roman", serif
    fontSize: 1.9rem
    fontWeight: 600
    lineHeight: 1.25
  body-lg:
    fontFamily: Arial, sans-serif
    fontSize: 1.2rem
    fontWeight: 400
    lineHeight: 1.65
  body-md:
    fontFamily: Arial, sans-serif
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.65
  body-sm:
    fontFamily: Arial, sans-serif
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5
  label-md:
    fontFamily: Arial, sans-serif
    fontSize: 0.75rem
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.05em
rounded:
  sm: 2px
  md: 2px
  lg: 4px
  full: 9999px
spacing:
  section: clamp(4.5rem, 10vw, 9rem)
  content: clamp(1.25rem, 4vw, 2.5rem)
  gutter: 24px
  margin: 40px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: 14px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 14px
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 32px
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: 12px
  meta:
    textColor: "{colors.muted}"
    typography: "{typography.label-md}"
---

# Legal

## Overview

Authoritative, calm and premium without feeling ostentatious. Suitable for law firms and professional services. Authority comes from hierarchy and restraint, not decoration — the visual language deliberately avoids anything that reads as startup-casual, and photography stays authentic and timeless rather than stock-perfect.

## Colors

- **Primary (#1C2B39):** a near-black navy for headings and primary actions — authoritative without reaching for black.
- **Accent (#92754D):** a muted bronze used only as a thin rule or small non-text detail — at this palette's contrast, it does not clear AA for text or fills, so it stays decorative and small, never a filled surface carrying text.
- **Surface (#FFFFFF) on Background (#F6F4EF):** cards and content sit on white, the page canvas is a warm parchment tone that avoids clinical pure white.
- **Text (#20252B) / Muted (#687079):** near-black body copy, a cooler grey for citations, dates and secondary detail.
- **Border (#D8D2C8):** a warm, quiet hairline for dividers — never a bold rule.

## Typography

A serif (Georgia) for headlines carries the editorial, institutional gravity a law firm needs; Arial for body copy keeps long clauses and case summaries legible and neutral. The scale is more compressed than the Editorial system's — this is a system about restraint, not spectacle.

## Layout

The most generous content padding in the catalog (`clamp(1.25rem, 4vw, 2.5rem)`) and a long section rhythm (`clamp(4.5rem, 10vw, 9rem)`) — pages take their time, never feeling rushed or crowded, which reads as confidence rather than slowness.

## Elevation & Depth

No shadows — hierarchy comes from generous whitespace and the quiet `border` hairline, never from drop shadows or heavy chrome that would read as startup-like.

## Shapes

A near-sharp 2px radius on cards and buttons — the most restrained corner treatment in the catalog, deliberately avoiding the soft, friendly rounding of consumer products.

## Components

- **Buttons:** primary fills with the near-black navy `{colors.primary}`, minimal `{rounded.sm}` corners, generous padding — confident without being loud.
- **Cards:** white surface, extra-generous 32px padding, near-sharp corners.

## Do's and Don'ts

- Do let hierarchy and restraint carry authority — not size or color.
- Don't use startup-like visual language: no playful rounding, no saturated fills, no casual iconography.
- Do use editorial typography carefully — the serif headline is a signal, not a decoration.
- Don't fill a surface with `accent` — at this contrast it never passes AA against the rest of the palette, so it stays a small, non-text detail only.
