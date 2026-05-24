# Troubleshooting Guide

## Local Development Issues

### Bundle Install Fails

**Problem:** `bundle install` fails with dependency resolution errors

**Solution:**
```bash
# Clear bundle cache
rm -rf vendor/bundle Gemfile.lock

# Reinstall with fresh lockfile
bundle install
```

### Build Fails with "Ruby version too old"

**Problem:** `nokogiri` or other gems require Ruby 3.2+, but you're running 3.1.2

**Context:** 
- Local development: Ruby 3.1.2 (limited to older nokogiri version)
- GitHub Actions: Ruby 3.3 (uses latest patched gems)

**Solution:** This is expected behavior in local development
- Your local builds may have minor gem version differences
- **Production builds via GitHub Actions use Ruby 3.3** and have all security patches
- Production site is fully secure despite local development notes

### Port Already in Use

**Problem:** `./run-blog` fails because port 4000 is already in use

**Solution:**
```bash
# Kill the existing process
lsof -ti:4000 | xargs kill -9

# Or use a different port
bundle exec jekyll serve --port 4001
```

### CSS/JavaScript Not Loading

**Problem:** Site loads but styles and scripts are missing

**Solution:**
```bash
# Run clean build
./clean.sh
JEKYLL_ENV=production bundle exec jekyll build

# Clear browser cache (Cmd+Shift+R on Mac)
```

### "Liquid Error" in Output

**Problem:** Pages show `Liquid Error: Undefined variable` or similar

**Possible causes:**
1. Missing front matter in a post/page
2. Broken include file referenced in a template
3. Missing variable in `_data/` files

**Solution:**
```bash
# Check the build with verbose output
JEKYLL_ENV=production bundle exec jekyll build --verbose

# Look for error lines, then examine that file
```

---

## Security & Dependencies

### Nokogiri CVEs in Local Development

**Issue:** `bundle audit` shows nokogiri 1.18.10 with CVEs:
- GHSA-c4rq-3m3g-8wgx (CSS selector regex backtracking)
- GHSA-v2fc-qm4h-8hqv (XSLT memory leak)
- GHSA-wx95-c6cv-8532 (xmlC14NExecute return value)

**Context:**
- nokogiri 1.19.3+ requires Ruby 3.2+
- Local environment: Ruby 3.1.2 (can't use patched version)
- Production: GitHub Actions uses Ruby 3.3 → gets patched nokogiri
- **Production site is secure; local dev has known limitation**

**To fix locally:**
```bash
# Upgrade local Ruby to 3.2+
# This allows nokogiri >= 1.19.3
# Then run: bundle update
```

Or simply ensure/verify:
1. Push changes to `main` branch
2. GitHub Actions builds with Ruby 3.3
3. Verify deployment succeeded
4. Your production site is secure

### Check for Other Vulnerabilities

```bash
# Full security audit
bundle audit

# See what can be updated
bundle outdated

# Try a conservative update (safest)
bundle update --conservative

# Or update specific gems
bundle update <gemname>
```

---

## Deployment Issues

### GitHub Actions Build Failed

**Where to check:** https://github.com/dustinson/d3cblog.github.io/actions

**If build failed:**
1. Click the failed workflow run
2. Expand "Build site" step
3. Look for error messages
4. Common causes:
   - Bad frontmatter in a post
   - Broken liquid template reference
   - Post with future date (excluded from build)

### Site Not Updated After Push

**Problem:** You pushed to `main` but site didn't update

**Troubleshooting:**
```bash
# Verify your push reached main
git log -1 main

# Check GitHub Actions status
# Visit: https://github.com/dustinson/d3cblog.github.io/actions
# Wait for workflow to complete (green checkmark)

# Workflow takes ~1-2 minutes
# Site takes another 30 seconds to refresh
# Total: ~3-4 minutes for updates to appear
```

**If workflow is stuck:**
- Check for invalid YAML in posts/config
- Check for circular template includes
- Try running locally: `JEKYLL_ENV=production bundle exec jekyll build --verbose`

### Gemfile.lock Platform Issue

**Problem:** 
```
Bundler attempted to update github-pages but its version stayed the same
```

**This is normal!** GitHub Pages gem is managed by GitHub and may not update frequently.

To ensure Linux platform is included for GitHub Actions:
```bash
bundle lock --add-platform x86_64-linux
```

---

## Performance & Caching

### Site Building Slowly

**Problem:** `jekyll build` takes longer than expected

**Causes:**
- Large number of posts/pages
- Slow disk I/O
- Missing `--incremental` flag

**Solution:**
```bash
# Incremental build (faster)
bundle exec jekyll serve --incremental

# Watch mode (rebuilds on file changes)
bundle exec jekyll serve --watch
```

### Stale Content in Browser

**Problem:** Changes appear locally but not after deployment

**Solution:**
```bash
# Hard refresh browser (clear cache)
Mac: Cmd + Shift + R
Windows: Ctrl + Shift + R
Linux: Ctrl + Shift + R

# Or disable cache in browser DevTools
```

---

## Getting Help

### Jekyll Documentation
- https://jekyllrb.com/docs/

### GitHub Pages Docs
- https://docs.github.com/en/pages

### Ruby Version Management
```bash
# Check installed Ruby versions
rbenv versions

# Switch Ruby version
rbenv local 3.3.0

# Install new Ruby version
rbenv install 3.3.0
```

### Common GitHub Pages Gems
See `github-pages` gem for all included plugins:
```bash
bundle show github-pages
```

---

## Phase 1 Stabilization Checklist

- ✅ Security audit run (`bundle audit`)
- ✅ Gemfile.lock updated
- ✅ Production build succeeds
- ✅ All pages render correctly
- ✅ Footer appears with build stamp
- ✅ GitHub Actions workflow validated (Ruby 3.3)
- ✅ README updated with deployment steps
- ✅ TROUBLESHOOTING.md created
- **Next:** Phase 2 - Modernization (Jekyll 4.x, etc)

