# Deployment Verification Checklist

Use this checklist before pushing to production to ensure the site builds and deploys correctly.

## Pre-Deployment: Local Testing

### 1. Code Changes
- [ ] Changes committed and staged
- [ ] No uncommitted changes (`git status` is clean)
- [ ] Branch is `main` (`git branch`)

### 2. Security Check
```bash
bundle audit
```
- [ ] No critical vulnerabilities found
- [ ] Known limitations documented (e.g., nokogiri on Ruby 3.1.2)

### 3. Build Validation
```bash
JEKYLL_ENV=production bundle exec jekyll build --verbose
```
- [ ] Build completes without errors
- [ ] No "Liquid Error" messages in output
- [ ] `_site/` directory is generated
- [ ] No warnings about missing includes

### 4. Live Server Test
```bash
./run-blog
```
- [ ] Server starts successfully
- [ ] Opens to http://localhost:4000 automatically
- [ ] No errors in terminal output

### 5. Automated Link & Resource Check

```bash
# Start dev server in one terminal
./dev-serve.sh

# Run link checker in another terminal
python3 scripts/pre-deployment-check.py
```
- [ ] Script completes with "ALL CHECKS PASSED"
- [ ] Exit code is 0 (check: `echo $?` after script runs)
- [ ] No broken internal links reported
- [ ] No missing images or resources
- [ ] All 75 event pages accessible

**Note:** This automated check is faster and more reliable than manual testing. See [PRE_DEPLOYMENT_CHECK.md](PRE_DEPLOYMENT_CHECK.md) for details.

### 6. Manual Browser Testing (Spot Check)

After automated checks pass, do spot checks:

#### Homepage (http://localhost:4000)
- [ ] Page loads without errors
- [ ] Logo displays correctly
- [ ] Navigation bar is visible and clickable
- [ ] Main content renders
- [ ] Footer appears at bottom with build timestamp
- [ ] Select all text in footer (shows hidden build stamp)

#### Blog Page (http://localhost:4000/blog/)
- [ ] Page loads
- [ ] Recent posts are listed
- [ ] Post titles are clickable
- [ ] Pagination works (if > 20 posts)
- [ ] Footer visible with timestamp

#### Individual Post (click any post)
- [ ] Post content displays
- [ ] Metadata (author, date) shows
- [ ] Navigation breadcrumb works
- [ ] Footer visible

#### Events Page (http://localhost:4000/events/)
- [ ] Page loads
- [ ] Events are listed
- [ ] Event pagination works (if > 20 events)
- [ ] Footer visible

#### Contact Page (http://localhost:4000/contact/)
- [ ] Page loads
- [ ] Form is visible
- [ ] All form fields render
- [ ] Footer visible

#### Navigation Links
- [ ] Click each main navigation item
- [ ] Verify each leads to correct page
- [ ] Back button works

### 6. Search & Functionality
- [ ] Search box is visible (if enabled)
- [ ] Links in footer are clickable
- [ ] External links work (verify 1-2 links)

---

## Post-Deployment: Verification (After Push)

### 1. Push to GitHub
```bash
git push origin main
```
- [ ] Push completes without errors
- [ ] GitHub Dashboard shows latest commit

### 2. GitHub Actions Workflow
- [ ] Visit: https://github.com/dustinson/d3cblog.github.io/actions
- [ ] Latest workflow run shows ✅ (green check)
- [ ] Build completed in < 5 minutes
- [ ] No errors in "Build site" step
- [ ] No errors in "Deploy to GitHub Pages" step

### 3. Live Site Verification
- [ ] Visit: https://delta3consulting.com
- [ ] Wait 30-60 seconds for DNS/CDN refresh (if needed)
- [ ] Homepage loads
- [ ] Latest post appears on blog page
- [ ] Same items tested locally render correctly on live site

### 4. Browser Cache Check
- [ ] Hard refresh (Cmd+Shift+R on Mac)
- [ ] Verify changes actually rendered (not cached)
- [ ] Check mobile view (different screen size)

### 5. Footer Timestamp
- [ ] Select all text in footer (Cmd+A then specifically in footer)
- [ ] Build timestamp is visible and recent
- [ ] Timestamp reflects your deployment time

### 6. Search Engines & Monitoring
- [ ] Visit Google Search Console (if configured)
- [ ] Check for crawl errors
- [ ] Verify sitemap.xml is updated

---

## Rollback Plan (If Deployment Fails)

If the production site breaks:

### 1. Identify the Problem
```bash
# Check GitHub Actions logs:
# https://github.com/dustinson/d3cblog.github.io/actions
```

### 2. Quick Revert
```bash
# Revert to previous commit
git revert HEAD
git push origin main

# Wait for GitHub Actions to rebuild (3-4 minutes)
```

### 3. Fix & Redeploy
```bash
# Fix the issue locally
# Run all checks from "Pre-Deployment" section above
# Commit and push again
git add .
git commit -m "Fix deployment issue"
git push origin main
```

---

## Troubleshooting Quick Reference

| Issue | Solution |
|-------|----------|
| Build fails locally | Run `bundle install` then `bundle update --conservative` |
| Workflow fails (GitHub Actions) | Check logs at https://github.com/dustinson/d3cblog.github.io/actions |
| CSS/JS not loading | Hard refresh browser (Cmd+Shift+R), clear `_site/` |
| Post won't appear | Check post filename format (YYYY-MM-DD-slug.md) |
| Templates broken | Run build with `--verbose` to find Liquid errors |
| Port 4000 in use | Kill process: `lsof -ti:4000 \| xargs kill -9` |

See **TROUBLESHOOTING.md** for detailed solutions.

---

## Schedule for Future Updates

### Weekly
- [ ] Review recent blog posts/posts for errors
- [ ] Check GitHub notifications

### Monthly  
- [ ] Run `bundle outdated` to check for updates
- [ ] Run `bundle audit` for security

### Quarterly
- [ ] Update gems: `bundle update --conservative`
- [ ] Test production build thoroughly
- [ ] Update documentation

### Yearly
- [ ] Major version updates (Jekyll 4.x, etc.)
- [ ] Consider Ruby version upgrade
- [ ] Review all dependencies for EOL status

---

## Success Criteria

✅ **Deployment is successful when:**
1. GitHub Actions workflow shows ✅
2. Live site loads at https://delta3consulting.com
3. All pages tested above render correctly
4. No 404 or 500 errors
5. Footer shows current build timestamp
6. Browser has no console errors

**🎉 Deployment Complete!**

