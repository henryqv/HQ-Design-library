from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.json"
mcp = FastMCP("hq-design-library")

def load_catalog() -> dict[str, Any]:
    return json.loads(CATALOG.read_text(encoding="utf-8"))

def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")

def normalize(value: str) -> list[str]:
    return [x.lower() for x in re.findall(r"[a-z0-9-]+", value.lower())]

def score(query: str, item: dict[str, Any]) -> int:
    q = normalize(query)
    fields = {
        "title": item.get("title",""),
        "name": item.get("name",""),
        "description": item.get("description",""),
        "tags": " ".join(item.get("tags",[])),
        "industries": " ".join(item.get("industries",[])),
        "styles": " ".join(item.get("styles",[])),
        "moods": " ".join(item.get("moods",[])),
        "intents": " ".join(item.get("intents",[])),
        "category": item.get("category","")
    }
    total = 0
    for term in q:
        for field, value in fields.items():
            if term in str(value).lower():
                total += {"title":5,"name":5,"category":4,"industries":4,"styles":4,"moods":4,"intents":5,"tags":3,"description":2}.get(field,1)
    return total

def filter_meta(items, industry=None, style=None, mood=None, intent=None, component=None):
    def has(item, field, value):
        if not value: return True
        vals = [str(x).lower() for x in item.get(field,[])]
        return value.lower() in vals
    out = items
    if industry: out = [x for x in out if has(x,"industries",industry)]
    if style: out = [x for x in out if has(x,"styles",style)]
    if mood: out = [x for x in out if has(x,"moods",mood)]
    if intent: out = [x for x in out if has(x,"intents",intent)]
    if component:
        out = [x for x in out if component.lower() == str(x.get("category","")).lower()
               or component.lower() in [str(t).lower() for t in x.get("tags",[])]
               or component.lower() in str(x.get("title","")).lower()]
    return out

@mcp.tool()
def list_design_systems() -> str:
    """List all local HQ design systems and their taxonomy."""
    return json.dumps(load_catalog()["systems"], ensure_ascii=False, indent=2)

@mcp.tool()
def list_pattern_categories() -> str:
    """List available UI pattern categories."""
    data = load_catalog()
    return json.dumps(sorted({p["category"] for p in data["patterns"]}), ensure_ascii=False, indent=2)

@mcp.tool()
def search_designs(query: str, industry: str | None = None, style: str | None = None,
                   mood: str | None = None, intent: str | None = None, limit: int = 8) -> str:
    """Search design systems by visual direction, industry, style, mood and user intent."""
    items = filter_meta(load_catalog()["systems"], industry, style, mood, intent)
    ranked = sorted(items, key=lambda x: score(query, x), reverse=True)
    return json.dumps(ranked[:max(1,min(limit,25))], ensure_ascii=False, indent=2)

@mcp.tool()
def search_patterns(query: str, category: str | None = None, industry: str | None = None,
                    style: str | None = None, mood: str | None = None,
                    intent: str | None = None, limit: int = 10) -> str:
    """Search patterns by component, industry, style, mood and intent."""
    items = load_catalog()["patterns"]
    if category:
        items = [x for x in items if x["category"].lower() == category.lower()]
    items = filter_meta(items, industry, style, mood, intent)
    ranked = sorted(items, key=lambda x: score(query, x), reverse=True)
    return json.dumps(ranked[:max(1,min(limit,30))], ensure_ascii=False, indent=2)

@mcp.tool()
def get_design_system(name: str) -> str:
    """Return the complete DESIGN.md for a design system."""
    data = load_catalog()
    for item in data["systems"]:
        if name.lower() in (item["name"].lower(), item["title"].lower()):
            return read(item["path"])
    return f"Design system not found: {name}"

@mcp.tool()
def get_pattern(category: str, name: str) -> str:
    """Return a pattern with HTML, CSS and accessibility guidance."""
    for item in load_catalog()["patterns"]:
        if item["category"].lower() == category.lower() and item["name"].lower() == name.lower():
            return read(item["path"])
    return f"Pattern not found: {category}/{name}"

@mcp.tool()
def get_tokens(system: str | None = None) -> str:
    """Return core tokens or the token file for a named design system."""
    if not system:
        return read("tokens/core.json")
    data = load_catalog()
    for item in data["systems"]:
        if item["name"].lower() == system.lower():
            return read(f"systems/{item['name']}/tokens.json")
    return f"Design system not found: {system}"

@mcp.tool()
def get_preview_path(category: str, name: str) -> str:
    """Return the local HTML preview path for a pattern."""
    for item in load_catalog()["patterns"]:
        if item["category"].lower() == category.lower() and item["name"].lower() == name.lower():
            return str(ROOT / item["preview"])
    return f"Pattern not found: {category}/{name}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
