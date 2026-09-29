from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def slug(s): return s.lower().replace(" ", "-").replace("_","-")

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "editorial"
    path = ROOT / "systems" / name / "tokens.json"
    if not path.exists():
        raise SystemExit(f"Unknown system: {name}")
    data = json.loads(path.read_text(encoding="utf-8"))
    lines = [":root {"]
    colors = data.get("colors", {})
    for k,v in colors.items():
        lines.append(f"  --color-{slug(k)}: {v};")
    typo = data.get("typography", {})
    if typo.get("display"):
        lines.append(f"  --font-display: {typo['display']};")
    if typo.get("body"):
        lines.append(f"  --font-body: {typo['body']};")
    scale = typo.get("scale", {})
    for k,v in scale.items():
        lines.append(f"  --font-size-{slug(k)}: {v};")
    spacing = data.get("spacing", {})
    for k,v in spacing.items():
        lines.append(f"  --space-{slug(k)}: {v};")
    radius = data.get("radius", {})
    for k,v in radius.items():
        lines.append(f"  --radius-{slug(k)}: {v};")
    lines.append("}")
    print("\n".join(lines))

if __name__ == "__main__":
    main()
