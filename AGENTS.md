# HQ Design Library — Agent Instructions

## Before creating UI

1. Inspect the project's existing `DESIGN.md`, if present.
2. Search HQ Design Library for relevant systems and patterns.
3. Do not blindly copy a reference.
4. Synthesize a coherent visual language.
5. Preserve the project's existing technical architecture.

## WordPress rules

When the target is WordPress:

- Prefer PHP templates over JSX.
- Prefer semantic HTML.
- Prefer CSS custom properties and maintainable CSS.
- Use vanilla JavaScript unless the project already requires a framework.
- Respect WordPress escaping and sanitization.
- Do not introduce npm/build tooling unless the project already uses it or the task explicitly requires it.
- Keep accessibility requirements explicit.
- Preserve responsive behavior.

## Design rules

- Do not mix unrelated design systems without a reason.
- Do not invent arbitrary spacing values when tokens exist.
- Use a limited type scale.
- Maintain visible focus states.
- Ensure interactive targets are usable on touch devices.
- Avoid decorative complexity that harms hierarchy.
- Treat motion as progressive enhancement.

## Output expectation

When implementing a design reference, explain internally:

- selected visual direction
- relevant tokens
- selected patterns
- adaptation decisions

Do not reproduce brand assets or proprietary visual identities unless the project has the right to use them.
