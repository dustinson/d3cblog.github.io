# Migration Plan: `_posts/Events/` → `_events/`

**Date:** 2026-05-24  
**Status:** IN PROGRESS

---

## Goal
Consolidate all event content into the `_events/` Jekyll collection. Eliminate the hybrid split between `_posts/Events/` (73 legacy files) and `_events/` (1 new file). Remove the template hacks that exist solely because of this split.

---

## What Changes

### URL Impact
| Before | After |
|--------|-------|
| `/community/presentation/IADNUG-TechDebt/` | `/events/2024-09-19-IADNUG-TechDebt/` |
| `/community/IADNUG-VS2010/` | `/events/2010-07-08-IADNUG-VS2010/` |
| etc. | etc. |

**Why this is safe:** The existing static HTML files in the committed `community/` folder at the repo root will continue to serve old URLs — those pages physically exist in the repo as committed files and are not affected by this migration. Anyone who bookmarked an old URL will still reach that page. The events *listing* page (`/events/`) will link to new `/events/...` URLs going forward.

---

## Files Being Changed

### 1. Move — 73 source files
All `.md` files from `_posts/Events/` → `_events/`  
No frontmatter changes required (layout, categories, tags all stay the same).

### 2. Template: `_includes/_event-pagination.html`
**Line 9** — Remove the `concat` hack:
```
# BEFORE
{%- raw %}{% assign my_posts = site.events | concat: site.categories.community | sort: "date" | reverse %}{% endraw %}

# AFTER  
{%- raw %}{% assign my_posts = site.events | sort: "date" | reverse %}{% endraw %}
```

### 3. Template: `events/archive.html`
Two bugs fixed:
- **Line 17**: Change data source from `site.categories.community` → `site.events`
- **Lines 17-20**: Fix broken variable name (`my_posts` assigned, but `my_events` looped — this archive was showing nothing!)

### 4. Template: `_includes/_navigation.html`
**Line 32** — Fix the active-state hack for the Events nav item:
```
# BEFORE  
... and page.url contains '/community/' ...

# AFTER  
... and page.url contains '/events/' ...
```

### 5. Docs: `_includes/__INSTRUCTIONS.md`
Update to reflect the new single-source approach (no more hybrid).

---

## Files Intentionally NOT Changed

| File | Why |
|------|-----|
| `community/` folder (static HTML) | Keep serving old URLs — these are committed static files, unaffected by Jekyll build |
| `_layouts/post.html` | Back-button checks `page.categories contains 'community'` — migrated events KEEP their `community` category in frontmatter, so this continues to work |
| `sitemap.xml` | Static committed file; will show stale URLs but SEO is not a concern. Regenerate manually after confirming migration is good. |
| `_config.yml` | `_events` collection is already correctly configured |

---

## Verification Checklist (post-migration)
- [ ] `bundle exec jekyll serve` builds without errors
- [ ] `/events/` page shows all events (73 legacy + 1 new = 74 total)
- [ ] Clicking an event goes to `/events/YYYY-MM-DD-slug/`
- [ ] Back button on event detail page says "← Back to Events" and returns to `/events/`
- [ ] Events nav item is highlighted when viewing an event
- [ ] `/events/archive/` page shows all events (was broken before due to variable bug)
- [ ] `/blog/` shows only blog posts (no events)



