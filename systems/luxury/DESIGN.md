---
version: "0.2.0"
name: Luxury
description: Minimal, tactile and image-led. Suitable for premium brands, hospitality and high-end services.
colors:
  background: "#F3F0EA"
  surface: "#FCFBF8"
  text: "#191816"
  muted: "#77736C"
  primary: "#191816"
  accent: "#A58B63"
  border: "#D8D1C4"
typography:
  headline-display:
    fontFamily: Georgia, "Times New Roman", serif
    fontSize: 5.5rem
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Georgia, "Times New Roman", serif
    fontSize: 3.2rem
    fontWeight: 400
    lineHeight: 1.1
  headline-md:
    fontFamily: Georgia, "Times New Roman", serif
    fontSize: 1.8rem
    fontWeight: 400
    lineHeight: 1.2
  body-lg:
    fontFamily: Arial, sans-serif
    fontSize: 1.15rem
    fontWeight: 400
    lineHeight: 1.7
  body-md:
    fontFamily: Arial, sans-serif
    fontSize: 0.95rem
    fontWeight: 400
    lineHeight: 1.7
  body-sm:
    fontFamily: Arial, sans-serif
    fontSize: 0.8rem
    fontWeight: 400
    lineHeight: 1.6
  label-md:
    fontFamily: Arial, sans-serif
    fontSize: 0.7rem
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.12em
rounded:
  sm: 0px
  md: 0px
  lg: 0px
spacing:
  section: clamp(5rem, 12vw, 11rem)
  content: clamp(1rem, 4vw, 3rem)
  gutter: 32px
  margin: 48px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: 16px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 16px
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 0px
  body:
    textColor: "{colors.text}"
    typography: "{typography.body-md}"
  meta:
    textColor: "{colors.muted}"
    typography: "{typography.label-md}"
  label-accent:
    textColor: "{colors.accent}"
    typography: "{typography.label-md}"
---

# Luxury

## Overview

Minimal, tactile and image-led. Suitable for premium brands, hospitality and high-end services. The system uses fewer elements on purpose, lets imagery breathe with generous negative space, treats typography as an object in its own right, and avoids any UI decoration that isn't earning its place.

## Colors

- **Primary (#191816):** near-black, used sparingly for text and the rare filled button — restraint is the whole point.
- **Accent (#A58B63):** a warm, muted gold used only as text (small labels, eyebrow text) — never as a filled surface, keeping the palette quiet.
- **Surface (#FCFBF8) on Background (#F3F0EA):** an almost-imperceptible shift between canvas and content, closer to paper than screen.
- **Text (#191816) / Muted (#77736C):** near-black for the rare block of copy, a soft warm grey for captions under full-bleed imagery.
- **Border (#D8D1C4):** used only where structurally necessary — a system this minimal relies on space, not lines, for separation.

## Typography

Georgia at a regular weight (never bold) carries the display and headline levels — typography as an object, not a shout — while Arial handles the sparse body copy. Sizes and line-heights are slightly tighter than Editorial's, giving headlines a compact, considered presence rather than editorial sprawl.

## Layout

The most spacious rhythm in the entire catalog: sections breathe at `clamp(5rem, 12vw, 11rem)` and content padding alone can reach `3rem`. Imagery is given the room the "let imagery breathe" principle asks for — nothing crowds a full-bleed photograph.

## Elevation & Depth

No shadows, and `border` is used only where structurally unavoidable — depth and hierarchy come entirely from negative space and image scale, never from chrome.

## Shapes

Zero radius everywhere — architectural sharpness on every button, card and container. This is the one system in the catalog with no rounding at all, matching its "avoid unnecessary UI decoration" principle literally.

## Components

- **Buttons:** primary is a sharp-edged near-black fill with light text; secondary inverts to a light fill with dark text — no other button variant exists, deliberately.
- **Labels:** the only place `accent` (warm gold) appears — small eyebrow/label text above a headline, never a filled badge.

## Do's and Don'ts

- Do use fewer elements — if a component isn't earning its place, remove it.
- Do let imagery breathe with generous surrounding space.
- Do treat typography as an object — deliberate, not merely functional.
- Don't add UI decoration (shadows, gradients, rounded corners, badges) that isn't structurally necessary.
