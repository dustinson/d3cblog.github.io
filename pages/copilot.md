---
layout: page
title: "Copilot References"
subheadline: "Notes, prompts, and a working todo list"
teaser: "A lightweight starting point for future Copilot-assisted changes and release checks."
permalink: "/copilot/"
header:
  image_fullwidth: "header_roadmap_3.jpg"
---

## Quick start

Launch the blog locally with one command:

```bash
./run-blog
```

This will:
1. Start the Jekyll development server
2. Automatically open the site in your browser at `http://localhost:4000`
3. Keep the server running until you press `Ctrl+C`

## Quick references

Use these files first when you want to understand or change the site:

- `_config.yml` — global site settings, title, and environment behavior
- `_data/navigation.yml` — top navigation links
- `_includes/_footer.html` — bottom footer and build stamp
- `_sass/_07_layout.scss` — footer and layout styling
- `_layouts/default.html` and `_layouts/page.html` — page structure
- `pages/*.md` — standalone pages and landing pages
- `_posts/` — blog posts

## Good Copilot prompts for this repo

- "Update the footer without changing the rest of the theme."
- "Check the page layout and keep the front matter style consistent."
- "Add a small release note and verify the navigation link still works."
- "Make a minimal Jekyll-safe change and preserve existing Liquid templates."

## Production checklist

1. Make the content or code change.
2. Build locally and confirm Jekyll succeeds.
3. Verify the footer still renders on the homepage and at least one content page.
4. Check the hidden build stamp in the grey footer bar.
5. Push to the production branch.
6. Confirm the live site after deployment.

## Todo list

- [ ] Add a simple changelog entry for each user-facing site change.
- [ ] Document the exact production branch and deploy command in `README.md`.
- [ ] Add a smoke-test checklist for the homepage, blog, and contact page.
- [ ] Review whether any pages should be moved into a dedicated release-notes section.
- [ ] Add a short "how to use Copilot here" note for future edits.
- [ ] Decide if more internal maintenance pages should be linked in the top navigation.

## Notes

This page is intentionally small and easy to extend. Add project-specific reminders, release links, or prompt snippets here as the workflow evolves.

