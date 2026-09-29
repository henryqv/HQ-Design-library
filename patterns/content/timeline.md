---
name: Content Timeline
category: content
tags: ["timeline", "process", "history", "content"]
industries: ["legal", "corporate", "education", "medical"]
styles: ["editorial", "institutional"]
moods: ["authoritative", "calm", "technical"]
intents: ["educate", "present-information", "build-credibility"]
---

# Content Timeline

A vertical chronology for process, history or milestones.

## When to use

Use this pattern when it matches the content intent and information hierarchy.

## HTML

```html
<section class="c-timeline" aria-labelledby="timeline-title">
  <h2 id="timeline-title">How the process works</h2>
  <ol>
    <li><strong>01 — Discovery</strong><p>Understand objectives and constraints.</p></li>
    <li><strong>02 — Strategy</strong><p>Define priorities and direction.</p></li>
    <li><strong>03 — Delivery</strong><p>Implement, test and refine.</p></li>
  </ol>
</section>
```

## CSS reference

```css
.c-timeline{padding:var(--space-section) var(--space-content);max-width:58rem;margin:auto}.c-timeline ol{list-style:none;margin:2rem 0 0;padding:0;border-left:1px solid var(--color-border)}.c-timeline li{padding:0 0 2rem 2rem;position:relative}.c-timeline li:before{content:'';position:absolute;left:-5px;top:.35rem;width:9px;height:9px;border-radius:50%;background:var(--color-primary)}.c-timeline p{color:var(--color-muted)}
```

## Accessibility

- Preserve semantic HTML.
- Maintain visible keyboard focus.
- Do not rely on color alone.
- Verify contrast in the final theme.
- Test at narrow viewport widths.
