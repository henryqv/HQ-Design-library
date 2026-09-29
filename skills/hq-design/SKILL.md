---
name: hq-design
description: Use HQ Design Library to research, select and implement visual design for web projects, especially WordPress/PHP/HTML/CSS.
---

# HQ Design Skill

## Purpose

Use HQ Design Library as a design research layer before implementing UI.

## Workflow

### 1. Inspect the project

Look for:

- `DESIGN.md`
- `AGENTS.md`
- existing CSS tokens
- component conventions
- template architecture
- accessibility conventions

Project-specific rules take priority.

### 2. Understand the request

Extract:

- industry
- visual style
- mood
- user intent
- page type
- required components

Example:

> "Elegant law firm homepage, authoritative but not old-fashioned."

Translate to:

```text
industry: legal
style: editorial + premium
mood: authoritative + timeless
intent: establish-trust + drive-contact
```

### 3. Search HQ Design Library

Use MCP tools when available:

```text
search_designs()
search_patterns()
get_design_system()
get_pattern()
get_tokens()
```

Do not search only by component name. Include the user's intent.

### 4. Select a coherent direction

Prefer:

- one primary design system
- one secondary reference when necessary
- a small set of patterns

Avoid mixing unrelated visual languages.

### 5. Synthesize

References are guidance.

Do not reproduce a proprietary website or brand identity.

Adapt:

- hierarchy
- rhythm
- spacing
- composition
- interaction patterns
- responsive behavior

### 6. Implement

For WordPress:

- semantic PHP
- semantic HTML
- CSS custom properties
- existing project architecture
- ACF/Gutenberg where appropriate
- vanilla JS unless the project already uses another framework

Do not introduce React/Tailwind/npm unless requested or already present.

### 7. Accessibility review

Check:

- keyboard navigation
- focus states
- labels
- heading hierarchy
- landmark structure
- contrast
- reduced motion
- touch target size

### 8. Responsive review

Check at minimum:

- 320px
- 375px
- 768px
- 1024px
- 1440px

### 9. Explain design decisions

When useful, report:

- selected system
- selected patterns
- important tokens
- adaptation decisions
