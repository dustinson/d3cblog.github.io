# Cleanup Execution Plan — Decisions Locked In

**Generated:** May 24, 2026  
**Branch:** `cleanup/`  
**Strategy:** Sequential execution, build-test-commit, stop on first failure  

---

## Decision Log (Per User Approval)

| Item | Decision | Rationale |
|------|----------|-----------|
| **C-1, C-5 (WIP Posts)** | Move to `_drafts/`, don't delete | Preserve history, can review later, no risk |
| **L-8 (images/b rename)** | Leave as-is | `/b` is intentional naming convention for blog images |
| **C-3 (Changelog)** | Keep `pages/changelog.md`, delete `changelog/index.md` | D3C needs its own changelog; theme version not relevant |
| **C-2 (404.html)** | Keep static `404.html`, delete Jekyll version | Static is fine, no need for Edit on GitHub |
| **M-5, M-6 (Feed/Sitemap/Robots)** | Delete static root versions, rebuild from Jekyll | Jekyll is source of truth; no custom overrides to preserve |
| **H-7 (Planning Docs)** | Create `_archive/` folder, move superseded docs there | Non-aggressive; can clean up later at leisure |
| **M-1 (Asciidoctor)** | Remove if not using | Currently disabled and wasteful; remove gems + config |
| **M-10 (Old Event Drafts)** | Leave for manual review later | User will decide what to do (archive/delete/publish) |
| **H-1 (Theme Pages)** | Search for references first, then delete | Confirm not referenced before removing |
| **L-7 (Rockline Logo)** | Find correct logo or remove from list | Don't leave wrong attribution |
| **L-8 (_posts/2022)** | Check for better org scheme while moving file | Opportunity to improve structure |
| **M-13 (Contact Form)** | Test it, auto-report if broken | Not a manual user verification item |
| **Build Failures** | Stop on first failure, report, don't continue | No failed builds to production |
| **Branch** | `cleanup/` | User will review, squash, merge |

---

## Execution Order

The following items will be addressed in this sequence:

### Phase 1: Quick Wins (No Dependencies)
- [ ] L-1: Remove `coderay` version pin or upgrade
- [ ] L-2, L-3, L-4: Config cleanup (comments, Google Analytics, open graph)
- [ ] H-5: Update `humans.txt` to credit D3C
- [ ] H-6: Fix `improve_content` URL in `_config.yml`

### Phase 2: File Moves & Deletions (Medium Risk)
- [ ] C-1: Move `_posts/3024-07-23-LossModeling.markdown` → `_drafts/`
- [ ] C-5: Move `_posts/2024-07-23-Succinct.markdown` → `_drafts/` (remove WIP marker from body)
- [ ] H-3: Delete `xindex.markdown`
- [ ] C-3: Delete `changelog/index.md` (keep `pages/changelog.md`)

### Phase 3: Static File Replacements (Higher Risk)
- [ ] C-2: Delete Jekyll version `pages/pages-root-folder/404.md`, keep static `404.html`
- [ ] M-5, M-6: Delete static `feed.xml`, `atom.xml`, `sitemap.xml`, `robots.txt` at root (rebuild from Jekyll)

### Phase 4: Config Changes (High Risk — Build Verification Critical)
- [ ] M-1: Remove `jekyll-asciidoc`, `asciidoctor`, `coderay` from Gemfile
- [ ] M-12: Add planning docs to `exclude:` in `_config.yml`
- [ ] M-4: Fix Twitter URL to HTTPS in `socialmedia.yml`
- [ ] M-3: Remove empty Facebook entry from `_config.yml`
- [ ] M-9: Move `images/iadnugSpeakerHistory.pdf` to `assets/docs/` (create if needed)

### Phase 5: Directory Removals (Clean Up)
- [ ] C-4: `git rm -r` old committed build artifacts (community/, blog/ACEmodel, etc.)
- [ ] H-1: Search for references to theme pages, then delete
- [ ] H-7: Create `_archive/` folder, archive superseded planning docs
- [ ] M-10: Leave old event drafts in `_drafts/` — user will review manually (add to todo)
- [ ] L-8 (_posts/2022): Check org scheme, move file

### Phase 6: Post-Cleanup Verification
- [ ] M-13: Test contact form at `/contact/`
- [ ] L-7: Find/add correct Rockline Enterprises logo
- [ ] L-6: Search for theme demo image references, delete unused ones

---

## Build Test Strategy

After **each commit**:
```bash
JEKYLL_ENV=production bundle exec jekyll build --verbose 2>&1 | tail -50
# Check: Exit code 0, "done in" present, no "Error:" or "Liquid Exception:" lines
```

**Stop on first failure:** If any build fails, stop, revert that commit, report, and ask for guidance.

---

## Commit Naming

- `cleanup: [ID] [description]` (e.g., `cleanup: C-1 Move year-3024 post to drafts`)
- Batch related items if they're all in same file (e.g., `cleanup: L-2 L-3 L-4 Config cleanup`)
- Each commit must have a passing build before proceeding

---

## What Will NOT Happen

- ❌ No `git push` (user does this)
- ❌ No scope creep (only items in audit)
- ❌ No failed builds committed
- ❌ No deletion without reference search (where applicable)
- ❌ No aggressive cleanup (archive, don't force delete)

---

## Manual TODOs for User (Post-Merge)

1. **M-10:** Review old event drafts in `_drafts/` — decide on archiving/publishing (2015-2020 events)
2. **L-7:** Verify Rockline Enterprises logo is correct
3. **M-13:** Test contact form at `https://delta3consulting.com/contact/`
4. **H-7:** Later: Review items in `_archive/` folder and decide what to permanently delete

---

**Status:** Ready to execute  
**Next Step:** Create `cleanup/` branch and begin Phase 1

