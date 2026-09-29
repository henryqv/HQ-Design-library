---
name: Editorial Hero
category: hero
tags: ["hero", "editorial", "professional", "content-first"]
industries: ["editorial", "professional-services"]
styles: ["minimal", "editorial"]
moods: ["confident", "calm"]
intents: ["navigate-content"]
---

# Editorial Hero

Large typographic hero with supporting copy and one primary action.

## When to use

Use this pattern when its information hierarchy matches the content. Do not use it merely because it looks attractive.

## HTML

```html
<section class="c-hero c-hero--editorial">
  <div class="c-hero__inner">
    <p class="c-hero__eyebrow">Eyebrow</p>
    <h1 class="c-hero__title">A clear statement of the value proposition.</h1>
    <p class="c-hero__intro">Supporting copy explains the offer without competing with the headline.</p>
    <div class="c-hero__actions">
      <a class="c-button c-button--primary" href="#">Primary action</a>
      <a class="c-button c-button--text" href="#">Secondary action</a>
    </div>
  </div>
</section>
```

## CSS reference

```css
.c-hero--editorial{padding:var(--space-section) 0}.c-hero__inner{max-width:72rem;margin:auto;padding:0 var(--space-content)}.c-hero__title{max-width:12ch;margin:.25em 0;font-size:clamp(3rem,8vw,6rem);line-height:.98}.c-hero__intro{max-width:48rem;font-size:clamp(1.05rem,2vw,1.35rem);line-height:1.6}.c-hero__actions{display:flex;gap:1rem;flex-wrap:wrap;margin-top:2rem}
```

## Accessibility

- Keep semantic elements.
- Preserve visible focus.
- Do not rely on color alone.
- Test keyboard navigation.
- Verify contrast against the final background.
