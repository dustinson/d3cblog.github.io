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

### Phase 1: Stabilization (Block everything until done)

**Dependencies & Security**
- [ ] Run `bundle audit` and fix all security vulnerabilities
- [ ] Update `Gemfile.lock` with latest compatible versions
- [ ] Document current Ruby version (3.2) and GitHub Actions environment
- [ ] Verify no broken dependencies with full build: `JEKYLL_ENV=production bundle exec jekyll build`

**Build Validation**
- [ ] Test full build locally and on GitHub Actions
- [ ] Verify footer renders on homepage, blog, events, and contact pages
- [ ] Check hidden build stamp is visible on all page types
- [ ] Smoke test: Homepage → Blog → Events → Contact → back to Homepage

**Testing & CI/CD**
- [ ] Create `.github/workflows/lint.yml` for pre-commit checks (Jekyll builds, no broken links)
- [ ] Document deployment process in README (who pushes, when, how to verify production)
- [ ] Add pre-push checklist to copilot.md

**Documentation**
- [ ] Update README with exact production push command
- [ ] Document Gemfile upgrade process for future maintainers
- [ ] Create TROUBLESHOOTING.md for common issues

---

### Phase 2: Modernization (After stabilization)

**Dependency Updates**
- [ ] Evaluate asciidoctor 1.5.4 → 2.0.26 upgrade (check for breaking changes)
- [ ] Update activesupport, addressable, commonmarker to latest safe versions
- [ ] Test blog build after each major dependency update
- [ ] Update Ruby version in `.github/workflows/gh-pages.yml` if needed

**Performance & UX**
- [ ] Review and optimize CSS/JS bundle sizes
- [ ] Check page load times on production
- [ ] Audit lighthouse performance on homepage and blog page

**Code Quality**
- [ ] Review for any `TODO` or `FIXME` comments in codebase
- [ ] Consider linting setup (markdownlint, prettier for consistency)

---

### Phase 3: Events (After stabilization)

**Upcoming Events to Add**

- [ ] ✅ **PMI Agile 2026 Review Team** (4/15/26) — *Status: Past event — add for archive*
  - Create event file: `_events/2026-04-15-PMI-Agile-Review-Team.md`
  - Add teaser, image, and link
  
- [ ] 🔴 **"The Past Didn't Go Anywhere" (7/25/26)** — *Next upcoming*
  - Create event file: `_events/2026-07-25-The-Past-Didnt-Go-Anywhere.md`
  - Add teaser, image, and important link
  - Set reminder to cross-post 2 weeks before

- [ ] Plan remaining ~4 events (TBD — awaiting details)
  - Gather event info: name, date, teaser, image, external link
  - Create event files using consistent naming: `_events/YYYY-MM-DD-Event-Name.md`
  - Update events index if needed

**Event Creation Template**
```markdown
---
layout: post
sidebar: left
subheadline: Presentation
title: "[Event Name]"
teaser: "[Short description]"
breadcrumb: false
tags:
    - event
    - [relevant-tag]
categories:
    - community
    - presentation
event_date: YYYY-MM-DD
image:
    thumb: [image-file].png
    title: [image-file].png
    caption: "[Caption]"
    caption_url: [external-url]
---

[Event description and details]
```

---

### Blocked Until Complete

⛔ **Do NOT add any new features or content** until Phase 1 is complete.  
✅ **Events can be added in batches** after stabilization passes.

---

## Notes

This page is your Copilot playbook. Update it with new prompts, rules, or workflow lessons as you discover what works best. Copilot should help you ship faster while you stay in control of what goes to production.

