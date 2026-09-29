# HQ Design Library v0.2

A local, open, framework-agnostic design knowledge base for AI coding agents.

Designed for:

- Cursor
- Claude Code
- Codex
- MCP-compatible agents
- WordPress / PHP / HTML / CSS / vanilla JS

## What v0.2 adds

- Design-system taxonomy: industry, style, mood, intent.
- Rich pattern metadata.
- Local HTML previews for every pattern.
- HQ Design Skill.
- Better MCP search with metadata filters.
- CSS token exporter.
- WordPress-first agent workflow.
- Local-only operation; no API key required.

## Main concepts

### Design systems

A complete visual direction:

```text
systems/legal/
systems/editorial/
systems/corporate/
systems/saas/
systems/luxury/
systems/ecommerce/
```

### Patterns

Reusable information/interaction patterns:

```text
patterns/hero/
patterns/navigation/
patterns/cards/
patterns/stats/
patterns/team/
patterns/faq/
patterns/pricing/
patterns/content/
patterns/testimonials/
patterns/forms/
patterns/cta/
patterns/footer/
```

### Taxonomy

Every item can be described through:

```text
industry
style
mood
intent
component
```

This is important because an agent can search for the reason a component exists, not only its name.

Example:

```text
industry = legal
style = editorial
mood = authoritative
intent = establish-trust
component = hero
```

## MCP

Install:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r mcp/requirements.txt
```

Run:

```bash
python mcp/server.py
```

Register that command as a local MCP server in your coding agent.

### Search example

Conceptually:

```text
search_designs(
  query="premium legal editorial",
  industry="legal",
  style="editorial",
  mood="authoritative",
  intent="establish-trust"
)
```

Then:

```text
search_patterns(
  query="law firm hero",
  category="hero",
  industry="legal",
  intent="establish-trust"
)
```

## CSS token export

```bash
python mcp/export_css.py legal
```

The command prints CSS custom properties for the selected design system.

## HTML previews

Every pattern has a local preview next to its Markdown definition.

Example:

```text
patterns/hero/editorial.md
patterns/hero/editorial.html
```

Open the `.html` file directly in a browser.

## Agent Skill

Read:

```text
skills/hq-design/SKILL.md
```

The skill defines the workflow:

```text
inspect project
→ understand intent
→ search references
→ select system
→ select patterns
→ synthesize
→ implement
→ accessibility review
→ responsive review
```

## WordPress

HQ Design Library deliberately does not require React or Tailwind.

For WordPress, the expected output is:

```text
PHP templates
+
semantic HTML
+
CSS custom properties
+
vanilla JS
+
ACF/Gutenberg when appropriate
```

## Important licensing note

HQ Design Library's original code, documentation, schemas and examples are MIT.

Third-party repositories or design references should be added only with their own license/attribution preserved. A brand reference should be treated as design research, not permission to reproduce trademarks, logos or proprietary assets.
