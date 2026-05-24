# Stabilization Phase Reference

**Status:** Ready to begin  
**Target:** Get all Phase 1 checkboxes to ✅  
**Blocker:** Nothing moves to events/modernization until stabilization is complete

---

## Phase 1 Dependencies & Security Audit

### Current Dependency Status

**Outdated gems requiring attention:**
- `asciidoctor` (1.5.4 → 2.0.26) — **Major version jump, needs testing**
- `activesupport` (7.1.5.1 → 8.1.3)
- `addressable` (2.8.7 → 2.9.0)
- `commonmarker` (0.23.11 → 2.8.2)
- Plus 10+ minor version updates available

**To audit:**
```bash
bundle audit
bundle outdated
```

**To update safely:**
```bash
bundle update
bundle lock --add-platform x86_64-linux
JEKYLL_ENV=production bundle exec jekyll build --verbose
```

---

## Phase 1 Build Validation

### Current State
- ✅ Build succeeds locally
- ✅ GitHub Actions workflow exists (.github/workflows/gh-pages.yml)
- ✅ Footer renders with build stamp
- ✅ Development server works

### Checklist
- [ ] Run full production build
- [ ] Verify footer on homepage
- [ ] Verify footer on blog page
- [ ] Verify footer on events page
- [ ] Verify footer on contact page
- [ ] Check build stamp visibility (select all text in footer)
- [ ] Test all navigation links work
- [ ] Test events page lists event correctly

---

## Phase 1 Testing & CI/CD

### Current State
- ✅ GitHub Actions auto-deploys on push to main
- ❓ No lint/pre-commit checks

### Gaps to Fill
- [ ] Add GitHub Actions lint workflow
- [ ] Document exact production push process
- [ ] Create pre-push checklist
- [ ] Add smoke-test instructions to README

---

## Phase 1 Documentation

### Current State
- ✅ README.md exists with dev/prod commands
- ✅ Copilot reference page exists

### Gaps to Fill
- [ ] Update README with production deployment details
- [ ] Document Gemfile upgrade process
- [ ] Create TROUBLESHOOTING.md
- [ ] Add deployment verification steps

---

## How to Run Phase 1

**Start with Copilot:**

```
"Let's stabilize the blog. Run bundle audit first, show me any vulnerabilities, 
then update Gemfile.lock and test the production build. Report any breaking changes."
```

**Then verify manually:**

```bash
# 1. Run the build
JEKYLL_ENV=production bundle exec jekyll build --verbose

# 2. Start dev server
./run-blog

# 3. Smoke test all pages manually in browser
# - Homepage (check footer, build stamp)
# - Blog page (check footer, build stamp)
# - Events page (check footer, build stamp)
# - Contact page (check footer, build stamp)
# - Navigation works

# 4. If all green, commit and push
git add .
git commit -m "Phase 1 stabilization: update dependencies and validate build"
git push origin main
```

---

## Success Criteria

Phase 1 is ✅ DONE when:
1. ✅ All security vulnerabilities patched
2. ✅ Gemfile.lock updated and build succeeds
3. ✅ All 4+ page types render correctly with footer
4. ✅ GitHub Actions deployment succeeds
5. ✅ Production site is live and verified
6. ✅ Documentation updated

**Then:** Move to Phase 2 (Modernization)

