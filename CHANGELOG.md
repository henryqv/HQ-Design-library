# Changelog

## 0.2.0 — 2026-09-29

- All six systems' `DESIGN.md` rewritten to the [google-labs-code/design.md](https://github.com/google-labs-code/design.md) standard format: tokens live only in the YAML front matter (colors, typography as per-level objects, `rounded`, `spacing`, `components`), and the markdown body follows the canonical section order (Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts). `npx @google/design.md lint` passes with 0 errors on every system.
- Removed per-system `tokens.json` and `metadata.json` — they duplicated the DESIGN.md front matter and `catalog.json` respectively and would have gone out of sync. Tokens now have one source of truth per system (its `DESIGN.md`); taxonomy (industries/styles/moods/intents) lives only in `catalog.json`.
- `mcp/server.py`'s `get_tokens()` now parses the DESIGN.md front matter directly instead of reading the removed `tokens.json`.
- Removed `mcp/export_css.py` (read the removed `tokens.json`, and its output format predated the current token schema) — CSS/Tailwind/DTCG export is now the official `design.md export` CLI command.

## 0.1.0 — 2026-09-29

- Initial HQ Design Library.
- Six original design systems.
- Eight original UI patterns.
- Core tokens.
- Local JSON catalog.
- MCP server over stdio.
- Cursor / Claude Code / Codex-oriented agent instructions.
- WordPress/PHP-first guidance.
