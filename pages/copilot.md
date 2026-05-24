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

## Standard Operating Procedures (SOPs)

### Copilot Rules & Boundaries
- ⛔ **Copilot does NOT push code to production.** All edits are staged locally; the user reviews and pushes to prod.
- ✅ **Copilot makes local edits** to files, runs builds, and reports status.
- ✅ **Copilot can commit to feature branches** if requested, but never to main/prod branches.
- 🔍 **Copilot verifies changes** with local builds before declaring a task complete.
- 📋 **All breaking changes** require explicit user approval before implementation.

### Release Process
1. Make the content or code change locally.
2. Build locally: `./run-blog` or `JEKYLL_ENV=production bundle exec jekyll build`
3. Verify the footer renders on homepage and at least one content page.
4. Check the hidden build stamp in the grey footer bar (select all text in footer).
5. **User reviews and commits changes manually.**
6. **User pushes to production branch.**
7. Verify the live site after deployment.

---

## Setting Up Copilot for Future Work

### Prompts for Blog Entry Creation

Use this prompt to add a new blog post:

```
"Create a new blog post in _posts/ dated today with:
- Title: [your title]
- Teaser: [short description]
- Keep the front matter style consistent with existing posts.
- Use the post.html layout."
```

### Prompts for Dependency Updates

Use this prompt to check and update dependencies:

```
"Check Gemfile and dependencies for outdated or vulnerable packages.
List current versions and suggest safe upgrades.
Update relevant packages and verify Jekyll still builds."
```

### The "Grill Me" Prompt

Use this prompt for deeper design discussions and architecture questions:

```
"Grill me on the blog architecture:
- Where are the pain points?
- What would improve maintainability?
- Are there any technical debt items?
- What would make adding content easier?
- Suggest one improvement and explain the tradeoffs."
```

---

## Copilot Skills

### 🎯 Grill Me

**Skill Name:** `grill-me`

**Description:** Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".

**How to use it:**
Simply say "grill me on [topic]" and I will:
1. Interview you relentlessly about every aspect of the plan
2. Walk down each branch of the design tree
3. Resolve dependencies between decisions one-by-one
4. Ask questions one at a time
5. Provide my recommended answer for each question
6. Explore the codebase where applicable to ground the discussion

**Example:**
- "Grill me on the footer implementation"
- "Grill me on adding a new content type"
- "Grill me on the deployment strategy"

---

## Good Copilot Prompts for Quick Tasks

- "Update the footer without changing the rest of the theme."
- "Check the page layout and keep the front matter style consistent."
- "Add a small release note and verify the navigation link still works."
- "Make a minimal Jekyll-safe change and preserve existing Liquid templates."
- "Verify all files build cleanly with `bundle exec jekyll build`."

---

## Todo List

- [ ] Create first new blog post using Copilot.
- [ ] Run full dependency audit and update Gemfile.
- [ ] Use "grill me" prompt to identify one quick improvement.
- [ ] Add a changelog section to the site or README.
- [ ] Document any custom build or deploy steps in `README.md`.
- [ ] Set up automated build checks (GitHub Actions) if not already done.
- [ ] Add smoke-test checklist for homepage, blog, events, and contact pages.
- [ ] Review footer styling and build stamp visibility across devices.

---

## Notes

This page is your Copilot playbook. Update it with new prompts, rules, or workflow lessons as you discover what works best. Copilot should help you ship faster while you stay in control of what goes to production.

