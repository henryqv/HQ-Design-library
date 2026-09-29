---
name: Accessible Contact Form
category: forms
tags: ["forms", "contact", "accessibility"]
industries: ["general", "legal", "professional-services", "corporate"]
styles: ["modern", "minimal"]
moods: ["calm", "trustworthy"]
intents: ["establish-trust", "drive-contact"]
---

# Accessible Contact Form

Simple form structure with visible labels and predictable fields.

## When to use

Use this pattern when its information hierarchy matches the content. Do not use it merely because it looks attractive.

## HTML

```html
<form class="c-form">
  <div class="c-form__field">
    <label for="name">Name</label>
    <input id="name" name="name" type="text" autocomplete="name" required>
  </div>
  <div class="c-form__field">
    <label for="email">Email</label>
    <input id="email" name="email" type="email" autocomplete="email" required>
  </div>
  <div class="c-form__field">
    <label for="message">Message</label>
    <textarea id="message" name="message" rows="6"></textarea>
  </div>
  <button class="c-button c-button--primary" type="submit">Send</button>
</form>
```

## CSS reference

```css
.c-form{display:grid;gap:1.25rem;max-width:42rem}.c-form__field{display:grid;gap:.5rem}.c-form input,.c-form textarea{width:100%;padding:.8rem 1rem;border:1px solid var(--color-border);background:var(--color-surface);font:inherit}.c-form input:focus,.c-form textarea:focus{outline:3px solid color-mix(in srgb,var(--color-primary),transparent 75%);outline-offset:2px}
```

## Accessibility

- Keep semantic elements.
- Preserve visible focus.
- Do not rely on color alone.
- Test keyboard navigation.
- Verify contrast against the final background.
