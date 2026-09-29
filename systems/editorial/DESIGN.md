---
version: "0.2.0"
name: Editorial
description: Typography-led, spacious and content-first. Suitable for publishing, professional services and institutional storytelling.
colors:
  background: "#F7F6F2"
  surface: "#FFFFFF"
  text: "#1B1B1B"
  muted: "#6B6B67"
  primary: "#1F3A4A"
  accent: "#A47C48"
  border: "#DDD9D0"
typography:
  headline-display:
    fontFamily: Georgia, "Times New Roman", serif
    fontSize: 5rem
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Georgia, "Times New Roman", serif
    fontSize: 3.5rem
    fontWeight: 700
    lineHeight: 1.1
  headline-md:
    fontFamily: Georgia, "Times New Roman", serif
    fontSize: 2rem
    fontWeight: 600
    lineHeight: 1.2
  body-lg:
    fontFamily: Inter, Arial, sans-serif
    fontSize: 1.25rem
    fontWeight: 400
    lineHeight: 1.65
  body-md:
    fontFamily: Inter, Arial, sans-serif
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.65
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
    letterSpacing: 0.05em
rounded:
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  section: clamp(4rem, 9vw, 8rem)
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
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.text}"
    rounded: "{rounded.full}"
    padding: 4px
  meta:
    textColor: "{colors.muted}"
    typography: "{typography.label-md}"
---

# Editorial

## Overview

Typography-led, spacious and content-first. Suitable for publishing, professional services and institutional storytelling. Typography establishes the hierarchy on its own — whitespace separates ideas, photography supports the story rather than dominating it, and the single accent color stays restrained throughout.

## Colors

- **Primary (#1F3A4A):** a deep, quiet navy for links and primary actions — authoritative without competing with the serif headlines.
- **Accent (#A47C48):** a warm bronze used only as text or a thin rule — a restrained highlight, never a large fill.
- **Surface (#FFFFFF) on Background (#F7F6F2):** articles and cards sit on white, the page canvas is a warm off-white that keeps long reading sessions comfortable.
- **Text (#1B1B1B) / Muted (#6B6B67):** near-black body copy, a warm grey for bylines, dates and captions.
- **Border (#DDD9D0):** a soft warm-grey rule between articles and sections.

## Typography

Two families carry the whole system: Georgia (a serif) for display and headline levels gives the storytelling weight of a printed publication, while Inter handles body copy and labels for contemporary on-screen readability. The serif never drops below headline-md — body text stays sans-serif throughout for long-form comfort.

## Layout

The most spacious rhythm in the catalog (`clamp(4rem, 9vw, 8rem)` between sections) — whitespace is doing real work here, separating one idea from the next the way a magazine layout would. Content spacing stays the same fluid `clamp(1rem, 3vw, 2rem)` used across the library.

## Elevation & Depth

No shadows — separation comes from generous whitespace and the soft `border` rule between sections, keeping the page feeling like print, not software.

## Shapes

An 8px radius on cards, 4px on buttons — soft enough to feel considered without reading as a tech product.

## Components

- **Buttons:** primary uses the navy `{colors.primary}` fill with white text; secondary inverts to an outline-style white fill with navy text — both quiet, neither shouts.
- **Badges:** the only place `accent` fills a surface — a small bronze pill with dark text, used sparingly for category tags.

## Do's and Don'ts

- Do let typography establish the hierarchy before reaching for color or weight tricks.
- Do let whitespace separate ideas — don't compress sections to fit more above the fold.
- Do let photography support the story rather than dominate the layout.
- Don't use more than the single `accent` color as a highlight — it stays restrained by design.
