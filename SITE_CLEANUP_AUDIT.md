# Site Cleanup Audit

**Created:** May 24, 2026  
**Scope:** Full site sweep for dead content, poor decisions, and cleanup opportunities  

---

## How to Use This Document

Each item is labelled with a **priority tag** and a **category**. Work through them highest-priority first. Many can be batched.

| Tag | Meaning |
|-----|---------|
| 🔴 CRITICAL | Bug, conflict, or bad data actively causing problems |
| 🟠 HIGH | Significant clutter, dead content, or tech debt |
| 🟡 MEDIUM | Should be cleaned up but won't break anything |
| 🟢 LOW | Nice-to-have polish |

---

## 🔴 CRITICAL — Fix These First

### C-1: Year-3024 blog post (typo in filename/date)
- **File:** `_posts/3024-07-23-LossModeling.markdown`
- **Problem:** The filename starts with `3024` instead of `2024`. Jekyll uses the date in the filename as the post date, so this post is dated 1,000 years in the future and will never appear in your post listing.
- **Also:** The post has `title: "ACE model"` but a different ACE model post (`_posts/2022-09-23-ACEmodel.markdown`) already exists — may be duplicate content.
- **Fix:** Rename to `2024-07-23-LossModeling.markdown` OR move to `_drafts/` if still WIP.

### C-2: Duplicate `404.html` conflict
- **Files:** `404.html` (root, static pre-rendered HTML) and `pages/pages-root-folder/404.md` (Jekyll source, `permalink: /404.html`)
- **Problem:** Both output to `/404.html`. Jekyll will try to process `pages/pages-root-folder/404.md` but the static `404.html` at root will always override it. One of these needs to go.
- **Fix:** Delete the static `404.html` at root and rely on the Jekyll-processed `pages/pages-root-folder/404.md`. Or delete the `pages/pages-root-folder/404.md` and keep the static one — but the static one has no "Edit on GitHub" link or site navigation.

### C-3: Duplicate permalink collision — `/changelog/`
- **Files:** `pages/changelog.md` (`permalink: "/changelog/"`, layout `page`) AND `changelog/index.md` (`permalink: /changelog/`, layout `changelog`)
- **Problem:** Both Jekyll sources declare the same permalink. One will silently clobber the other during build.
- **Fix:** Delete `changelog/index.md` (it references the blog theme's own version history, which is not relevant to this site anyway — see H-4 below). Or delete `pages/changelog.md`.

### C-4: Old committed build artifacts in repo
- **Problem:** Multiple directories in the repo root are pre-rendered HTML output accidentally committed to git — they are NOT source files. They don't have Jekyll front matter, they are rendered `<!doctype html>` pages. The `.gitignore` ignores `_site` but these were generated to the root directory by an older deploy strategy.
- **Directories to delete (confirmed build artifacts):**
  - `community/` — entire directory tree of old event HTML (dozens of subdirectories)
  - `blog/ACEmodel/`, `blog/HermitCrab/`, `blog/IndianFood/`, `blog/MonteCarlo/`, `blog/Succinct/`, `blog/TechniquesToTackleTech-debtToday/`, `blog/MemoryOverflowErrors/`
  - `blog/archive/`, `blog/page2/`, `blog/page3/`, `blog/page4/`
  - `events/archive/`
  - `getting-started/index.html`
  - `design/index.html`
  - `contact/index.html`
  - `xindex/index.html` (and the `xindex/` directory)
  - `redirect-page/index.html` (and the `redirect-page/` directory — also references `phlow.github.io`)
- **Note:** `blog/index.html`, `blog/archive.html`, and `events/archive.html` DO have front matter and ARE source files — keep those.
- **Fix:** `git rm -r community/ blog/ACEmodel blog/HermitCrab blog/IndianFood blog/MonteCarlo blog/Succinct blog/TechniquesToTackleTech-debtToday blog/MemoryOverflowErrors blog/archive blog/page2 blog/page3 blog/page4 events/archive getting-started/index.html design/index.html contact/index.html xindex redirect-page`

### C-5: WIP posts published (not in drafts)
- **Files:**
  - `_posts/2024-07-23-Succinct.markdown` — first line of content is `-- work in progress --`
  - `_posts/3024-07-23-LossModeling.markdown` — first line is `--WIP--`
- **Problem:** These appear on the live site as published blog posts with visible WIP markers.
- **Fix:** Move to `_drafts/` until they're ready, or remove the WIP markers if content is actually complete enough.

---

## 🟠 HIGH — Significant Cleanup

### H-1: Leftover Feeling Responsive theme pages (not your content)
The following pages are copied verbatim from the [`Feeling Responsive` Jekyll theme](https://github.com/Phlow/feeling-responsive) and contain content about the **theme itself**, not about Delta3Consulting. They are live, indexed pages on your site that are confusing and irrelevant to your audience.

| File | Permalink | Issue |
|------|-----------|-------|
| `pages/info.md` | `/info/` | "Why another Jekyll Theme?" — written by Moritz Sauer, the theme creator |
| `pages/changelog.md` | `/changelog/` | Theme version history (2014-2021), not site history |
| `pages/changelog/index.md` | `/changelog/` | Duplicate of above using `changelog` layout |
| `pages/roadmap.md` | `/roadmap/` | Theme "Feeling Responsive" roadmap, says "I have no plans to make it better or worse" |
| `pages/documentation.md` | `/documentation/` | Full Feeling Responsive theme documentation |
| `pages/getting-started.md` | `/getting-started/` | Theme getting-started guide, not D3C-specific |
| `pages/headers.md` | `/headers/` | Theme demo page showing header variations |
| `pages/design.md` | `/design/` | Theme demo page listing design posts (none exist) |
| `pages/redirected_page.md` | `/redirected_page/` | Demo redirect page from the theme |

- **Fix:** Delete all of the above. None are reachable from your navigation or needed for your site. If you want a real About/Info page, create a new one about Delta3Consulting.

### H-2: `pages/copilot.md` is a live public page
- **File:** `pages/copilot.md`, `permalink: /copilot/`
- **Problem:** This page is publicly accessible at `https://delta3consulting.com/copilot/`. It contains internal tool instructions, Copilot prompts, and your internal TODO list. It's not linked in navigation but it's indexed and crawlable.
- **Fix:** Move content to a root-level markdown file (e.g., `COPILOT.md`) to keep it developer-side only. Remove the front matter/permalink so it's not processed as a page.

### H-3: `xindex.markdown` abandoned root file
- **File:** `xindex.markdown` at repo root
- **Problem:** Has `layout: home` which doesn't exist in the theme. This was likely an early attempt to set up a home page that was abandoned. The `x` prefix suggests it was intentionally "disabled" by renaming, but it still gets processed by Jekyll with a broken layout reference.
- **Fix:** Delete `xindex.markdown`.

### H-4: `authors.yml` is entirely empty/commented out
- **File:** `_data/authors.yml`
- **Problem:** All 14 lines are comments. The file documents the format but has no actual author data. Author attribution in posts and pages won't work with named authors.
- **Fix:** Add your author entry (Dustin Thostenson) so author metadata renders correctly.

### H-5: `humans.txt` credits the wrong person
- **File:** `humans.txt`
- **Problem:** The TEAM section is blank, and the THANKS section credits Moritz Sauer (Feeling Responsive theme creator) as if he's the site author. Your name doesn't appear at all.
- **Fix:** Add a TEAM section with your name and contact info. Keep Moritz in THANKS (he deserves credit for the theme) but it should be clear this is Delta3Consulting's site.

### H-6: `improve_content` URL in `_config.yml` is wrong
- **Line 36:** `improve_content: https://dustinson.github.io/d3cblog.github.io/edit/gh-pages`
- **Problem:** This is the wrong URL format. It should be `https://github.com/dustinson/d3cblog.github.io/edit/main` (or whatever the default branch is). The current URL would result in broken "Edit on GitHub" links on pages that use `{% include _improve_content.html %}`.
- **Fix:** `improve_content: https://github.com/dustinson/d3cblog.github.io/edit/main`

### H-7: Redundant planning/status docs at repo root
The following 12+ markdown files at the repo root are internal planning artifacts that have accumulated. They have no permalinks and aren't served as pages, but they clutter the project and make navigation confusing for future maintainers:

| File | Status |
|------|--------|
| `ADDITIONAL_STABILIZATION.md` | Superseded by STABILIZATION.md |
| `STABILIZATION.md` | Superseded by PHASE_1_SUMMARY.md |
| `PHASE_1_COMPLETE.md` | Status doc, superseded |
| `PHASE_1_SUMMARY.md` | Referenced in README — keep or archive |
| `EVENTS_PHASE_3.md` | Planning doc, events are now live |
| `EVENT_DISCOVERY_INDEX.md` | Research artifact |
| `EVENT_DISCOVERY_PROMPT.md` | Research artifact |
| `MIGRATION_EVENTS_PLAN.md` | Migration is complete |
| `RESEARCH_PROMPTS.md` | Dev tool, not release artifact |
| `COPILOT_IMPORT_PROMPT.md` | Dev tool |
| `CUSTOM_SLASH_COMMANDS.md` | Dev tool |
| `test-deployment.md` | Clearly temporary |

- **Fix:** Create a `docs/` or `_dev/` folder (gitignored or just organized) and move these there. Or delete the completed/superseded ones. Keep the actively useful ones: `DEVELOPMENT.md`, `TROUBLESHOOTING.md`, `DEPLOYMENT_CHECKLIST.md`, `README.md`, `PRE_DEPLOYMENT_TODO.md`.

### H-8: `_posts/TechDebt/` and `_posts/Events/` are not posts
- **`_posts/TechDebt/`** — Contains only image files (CodeSmells.png, CostOfChange.png, etc.) — misplaced. These should be in `images/TechDebt/`.
- **`_posts/Events/`** — Empty directory, appears to be a ghost folder.
- **Fix:** Move the images to `images/TechDebt/` (they may already be there — check for duplicates). Delete the empty `Events/` folder.

---

## 🟡 MEDIUM — Should Be Cleaned Up

### M-1: `asciidoctor` plugin loaded but disabled — inconsistency
- **In `_config.yml`:** `asciidoctor-enabled: false`
- **In `Gemfile`:** `gem 'jekyll-asciidoc'` and `gem 'asciidoctor', '~> 1.5.4'`
- **In `_config.yml` plugins list:** `- jekyll-asciidoc`
- **Problem:** The plugin is installed, loaded, and listed but explicitly disabled. This wastes build time and loads an unnecessary gem. Also, `asciidoctor 1.5.4` is extremely old (current is 2.x).
- **Fix Option A (remove it):** Remove `jekyll-asciidoc` from plugins and Gemfile, remove `asciidoctor` and `coderay` gems, remove the `asciidoctor:` config block.
- **Fix Option B (keep it):** Change `asciidoctor-enabled: false` to `true` and update to `asciidoctor ~> 2.0`.

### M-2: Duplicate Google Analytics configuration in `_config.yml`
- **Lines 227-229:** Both `google_analytics_tracking_id: G-R4TVL0TF0M` AND `google_analytics: G-R4TVL0TF0M` set to the same value.
- **Also:** Line 159 has a TODO comment "wire up the google analytics!" even though GA IS configured below it — this comment is stale and misleading.
- **Fix:** Pick one variable name, remove the other, delete the stale TODO comment.

### M-3: Facebook social media config is empty
- **`_config.yml` line 200:** `facebook  :` (no value)
- **Problem:** An empty Facebook key may cause unexpected template behavior.
- **Fix:** Either add a valid Facebook page URL or remove the line entirely.

### M-4: Twitter/X rebranding in `socialmedia.yml`
- **File:** `_data/socialmedia.yml`
- **Problem:** Twitter is now X. The `class: icon-twitter` may still render the Twitter bird icon, and the URL format is `http://twitter.com/dustinson` (HTTP, not HTTPS). If the icon font doesn't have an X icon, consider updating text or icon class.
- **Fix:** Update URL to `https://twitter.com/dustinson` (or `https://x.com/dustinson`). Consider whether the Twitter/X icon is still desired.

### M-5: Duplicate feed files (root vs pages-root-folder)
- **Files:** `feed.xml` (root, static pre-rendered) AND `pages/pages-root-folder/feed.xml` (Jekyll source, `permalink: /feed.xml`)
- **Same for:** `atom.xml` at root and `pages/pages-root-folder/atom.xml` (`permalink: /atom.xml`)
- **Problem:** Static root files will conflict with Jekyll-processed equivalents. The static root `feed.xml` is a pre-rendered snapshot with hardcoded content and won't update.
- **Fix:** Delete the static `feed.xml` and `atom.xml` at the root level. Let Jekyll process the ones in `pages/pages-root-folder/`.

### M-6: Duplicate sitemap/robots.txt at root
- **Same pattern as M-5:** Static `sitemap.xml` and `robots.txt` at root AND Jekyll-processed versions in `pages/pages-root-folder/`.
- **Fix:** Delete the static root versions (`sitemap.xml`, `robots.txt`) and let Jekyll generate them.

### M-7: `_data/language.yml` and `language_de.yml` unused
- **Files:** `_data/language.yml`, `_data/language_de.yml`
- **Problem:** These are theme translation files. The site is English-only and never switches languages. They add confusion but no value.
- **Fix:** Review if any template references `site.data.language.*`. If not, delete both files.

### M-8: `images/b/` — cryptic directory name
- **Directory:** `images/b/` containing BeWise and monteCarlo images
- **Problem:** The directory is named a single letter `b`. This is completely non-descriptive. Images include `BeWise-*.jpeg` and `monteCarlo*.png`.
- **Fix:** Rename to `images/BeWise/` or `images/blog/` and update all references in posts.

### M-9: `images/iadnugSpeakerHistory.pdf` in wrong location
- **File:** `images/iadnugSpeakerHistory.pdf`
- **Problem:** A PDF file in the images directory. This is the wrong location for a document.
- **Fix:** Move to an `assets/docs/` or `assets/pdfs/` directory and update any links to it.

### M-10: `_drafts/` has old content that should be committed or deleted
- **Files:** Several event files dating from 2015-2020
  - `2015?-HeartlandsDeveloperConference.md` (undated, 10+ years old)
  - `2015?-OmahaDotNet.md`
  - `2015?-OmahaJava.md`
  - `2015?-PrarieCode-NebraskaCodeCamp.md`
  - `2018-NYC-Startup.md`
  - `2019-08-19-RealEstateWorld-Podcast.md`
  - `2020-AgileIowa.md`
  - Theme demo drafts (gallery.md, page_*.md, post_*.md, video.md)
- **Problem:** These have been sitting in drafts for 5-10 years. Either publish them (they're old history worth keeping) or delete them.
- **Fix:** Move the 2015-2020 event files to `_events/` with proper dates. Delete the theme demo drafts (gallery.md, page_simple.md, etc.) — they're boilerplate.

### M-11: `peaceiris/actions-gh-pages@v3` is outdated
- **File:** `.github/workflows/gh-pages.yml` (line 45)
- **Problem:** `peaceiris/actions-gh-pages@v3` is an older community action. GitHub now has an official `actions/deploy-pages` action for deploying to GitHub Pages. The v3 action is maintained but not the modern canonical approach.
- **Fix:** Optionally migrate to the official GitHub Pages deploy action (`actions/configure-pages`, `actions/upload-pages-artifact`, `actions/deploy-pages`). Not urgent but worth a future modernization.

### M-12: `_config.yml` exclude list is missing new planning docs
- **Lines 72-79:** The `exclude:` list only has a few entries and doesn't exclude any of the planning markdown docs (LESSONS_LEARNED.md, TROUBLESHOOTING.md, PRE_DEPLOYMENT_TODO.md, etc.).
- **Problem:** These docs are likely being included in the build output and potentially accessible from the site.
- **Fix:** Add all the internal planning/dev docs to the `exclude:` list.

### M-13: `contact.md` uses Wufoo — verify it still works
- **File:** `pages/contact.md`
- **Problem:** The contact form is embedded via Wufoo JavaScript. Wufoo still exists but free plans have limitations, and the form hash `z14kby6v0cgtk1g` could have expired. There's no fallback if the script fails.
- **Fix:** Test the contact form works. Consider adding a simple fallback email link. Alternatively evaluate modern form services (Formspree, Netlify Forms, etc.).

---

## 🟢 LOW — Polish Items

### L-1: `coderay` gem pinned to old version
- **Gemfile line 25:** `gem 'coderay', '1.1.1'`
- **Problem:** This pins to a specific old version. coderay 1.1.3 is current.
- **Fix:** Change to `gem 'coderay', '~> 1.1'` or remove if asciidoctor is removed (M-1).

### L-2: Multiple root-level image files that duplicate `/images/`
- **Files:** `D3-icon.png`, `D3-icon300.png`, `d3.png` at repo root
- **Problem:** These appear to be the same images that exist in `/images/`. Root-level image files are atypical and may have been placed there for specific legacy reasons (e.g., GitHub repo icon).
- **Fix:** Verify they're referenced anywhere. If only used in GitHub (not Jekyll templates), document that. If duplicates, remove root copies.

### L-3: `_config.yml` still has `google_site_verification` and `bing_webmastertools_id` commented out
- **Lines 160-162:** Both webmaster verification codes are commented out.
- **Problem:** These were never set up, which means the site is not verified with Google Search Console or Bing Webmaster Tools.
- **Fix:** Either set these up and uncomment the config, or delete the commented-out lines.

### L-4: `redirect-page/` contains link to `phlow.github.io`
- **File:** `redirect-page/index.html` (old build artifact — see C-4)
- **Content:** `<link rel="canonical" href="http://phlow.github.io/feeling-responsive/info/"/>` — links to the original theme demo, not your site.
- **Fix:** This file should be deleted as part of C-4. Calling it out separately because it could cause unexpected canonical URL indexing if not caught first.

### L-5: `_config.yml` has commented-out Facebook OpenGraph section
- **Lines 187-189:** `og_image`, `og_locale`, `og_type` all commented out.
- **Problem:** OpenGraph metadata is important for social sharing previews (LinkedIn, Slack, etc.). The site likely has limited sharing previews.
- **Fix:** Enable and configure `og_image` with the D3 logo, set `og_locale: en_US`, `og_type: website`.

### L-6: `images/gallery-example-*.jpg` and other theme demo images
- **Files:** At least 16 gallery-example images (1-8, with thumbs), plus `widget-*.jpg`, `webdesign_screenshot_*.jpg`, `homepage_typography*.jpg`, `presentation-*.jpg`, `video-feeling-responsive-*.jpg`, `start-video-feeling-responsive-302x182.jpg`
- **Problem:** These are all demo images from the Feeling Responsive theme, not Delta3Consulting content. They're taking up space (each a few hundred KB) and cluttering the images directory.
- **Fix:** Search for references to each file in templates and posts. Delete any not actively referenced.

### L-7: `network.yml` — "Rockline Enterprises" uses wrong image
- **File:** `_data/network.yml` line 41
- **Problem:** `Rockline Enterprises` has `img: "deere.png"` — the John Deere logo is being shown for Rockline Enterprises.
- **Fix:** Either get the correct logo for Rockline or remove them from the network list.

### L-8: `_posts/2022/` subdirectory with a single file
- **Directory:** `_posts/2022/2022-09-23-MonteCarlo.markdown`
- **Problem:** There's a `2022/` subdirectory inside `_posts/`, but all other posts are directly in `_posts/`. This creates an inconsistency. Jekyll will still process it but it looks unintentional.
- **Fix:** Move `_posts/2022/2022-09-23-MonteCarlo.markdown` to `_posts/2022-09-23-MonteCarlo.markdown`.

### L-9: `_config.yml` has `events_paginate_path` that may not be used
- **Line 64:** `events_paginate_path: "/events/page:num"`
- **Problem:** `jekyll-paginate` only supports `paginate_path` for a single paginated collection. The `events_paginate_path` custom variable won't be used by the paginate plugin — you'd need a custom template to use it.
- **Fix:** Verify if events pagination actually works. If not, clean up the unused config variable.

### L-10: `_posts/2026-04-09-DotNet-Noon-Past-Didnt-Go-Anywhere.md` needs review
- **Problem:** This is listed as a 2026 past event. The corresponding upcoming event listed in `pages/copilot.md` is `2026-07-25`. Verify this event date/title is correct.

---

## Suggested Cleanup Script

```bash
#!/bin/bash
# site-cleanup.sh — Run from repo root AFTER reviewing each item
# REVIEW the lists carefully before uncommenting and running sections!

# C-4: Remove old committed build artifacts
# git rm -r community/ \
#   blog/ACEmodel blog/HermitCrab blog/IndianFood blog/MonteCarlo \
#   blog/Succinct "blog/TechniquesToTackleTech-debtToday" blog/MemoryOverflowErrors \
#   blog/archive blog/page2 blog/page3 blog/page4 \
#   "events/archive" \
#   getting-started/index.html \
#   design/index.html \
#   contact/index.html \
#   xindex \
#   redirect-page

# H-1: Remove Feeling Responsive theme leftover pages
# rm pages/info.md pages/changelog.md pages/roadmap.md pages/documentation.md
# rm pages/getting-started.md pages/headers.md pages/design.md pages/redirected_page.md

# H-3: Remove abandoned xindex file
# rm xindex.markdown

# C-3: Remove duplicate changelog
# rm changelog/index.md   # keep pages/changelog.md OR delete both if deploying H-1

# C-1: Fix year-3024 post
# git mv _posts/3024-07-23-LossModeling.markdown _drafts/2024-07-23-LossModeling.markdown

# L-8: Fix post in subdirectory
# git mv "_posts/2022/2022-09-23-MonteCarlo.markdown" "_posts/2022-09-23-MonteCarlo.markdown"
# rmdir _posts/2022/

echo "Review items before uncommenting and running!"
```

---

## Quick-Win Batch (30 minutes of work, high impact)

1. **Delete** `xindex.markdown` — zero risk, no purpose
2. **Move** `_posts/3024-07-23-LossModeling.markdown` → `_drafts/2024-07-23-LossModeling.markdown`
3. **Fix** `improve_content` URL in `_config.yml` (wrong GitHub URL)
4. **Delete** `redirect-page/` directory (links to phlow.github.io!)
5. **Fix** `network.yml` Rockline Enterprises image (uses John Deere logo)
6. **Fix** `_posts/2022/2022-09-23-MonteCarlo.markdown` → move to `_posts/` root
7. **Remove** stale `google_analytics` TODO comment from `_config.yml` (line 159)
8. **Delete** theme demo drafts from `_drafts/` (gallery.md, page_simple.md, etc.)

---

## Summary Statistics

| Category | Count |
|----------|-------|
| 🔴 Critical items | 5 |
| 🟠 High items | 8 |
| 🟡 Medium items | 13 |
| 🟢 Low items | 10 |
| **Total** | **36** |

| Issue Type | Count |
|------------|-------|
| Old build artifacts committed to git | ~200+ files across 15+ dirs |
| Feeling Responsive theme leftovers (pages) | 8 pages |
| WIP posts published live | 2 posts |
| Config/data inconsistencies | 8 items |
| Redundant planning docs at root | 12 files |
| Unused/misplaced images | 20+ images |
| Stale/broken links | 3 items |

