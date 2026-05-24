# Quick Reference: Pre-Deployment Workflow

A quick guide for running pre-deployment checks before pushing to production.

## ⚡ TL;DR (Fast Path)

```bash
# Terminal 1: Start dev server
./dev-serve.sh

# Terminal 2: Run link checker (while dev server runs)
python3 scripts/pre-deployment-check.py

# ✅ If you see: "ALL CHECKS PASSED - READY FOR PRODUCTION"
# Push to GitHub
git push origin main

# ❌ If issues found: Fix them first, then re-run script
```

## Step-by-Step

### 1. Prepare Your Changes

```bash
# Make sure everything is committed
git status
git add .
git commit -m "Your changes"
```

### 2. Start Dev Server

```bash
./dev-serve.sh
```

You should see:
```
=== DEVELOPMENT SERVER WITH DEBUGGING ===
... 
Server running on http://localhost:4000
```

**Leave this running in its terminal.**

### 3. Run Pre-Deployment Check (New Terminal)

```bash
python3 scripts/pre-deployment-check.py
```

Wait for results (~1-2 minutes).

### 4. Interpret Results

#### Success ✅
```
✓ Passed Checks: 8
  • Main page: Homepage
  • Main page: Events Index
  • ... etc

======================================================================
✅ ALL CHECKS PASSED - READY FOR PRODUCTION
======================================================================
```

**Exit code: 0** → Safe to deploy!

#### Failure ❌
```
❌ Issues Found: 2

BROKEN_LINKS (2):
  • /events/2024-01-01-Event: /missing-page (HTTP 404)

BROKEN_RESOURCES (1):
  • /events/2024-01-01-Event: /images/missing.png (HTTP 404)
```

**Exit code: 1** → Fix issues, don't deploy yet

### 5. Fix Issues (If Needed)

Identify what's broken from the report, fix it, then:

```bash
# Re-run the check
python3 scripts/pre-deployment-check.py
```

Repeat until you see "✅ ALL CHECKS PASSED"

### 6. Deploy When Ready

Once script passes:

```bash
# Still in Terminal 2, after script completes
git push origin main
```

Then monitor:
- GitHub Actions: https://github.com/dustinson/d3cblog.github.io/actions
- Live site: https://delta3consulting.com

## What Gets Checked

| Check | What We Test | Catches |
|-------|--------------|---------|
| **Main Pages** | Homepage, Events, Blog, Videos, Search | Missing pages, broken navigation |
| **Assets** | CSS and JavaScript files | Removed stylesheets or scripts |
| **Event Discovery** | Crawls events index | Pagination issues |
| **Event Pages** | All 75+ events load | Missing or misconfigured events |
| **Internal Links** | Links within each event | Typos in URLs, removed pages |
| **Resources** | Images in events | Missing images, broken paths |

## Exit Codes

```bash
python3 scripts/pre-deployment-check.py
echo $?

# 0 = All checks passed, ready to deploy
# 1 = Issues found, do not deploy yet
```

## Common Issues & Solutions

### "Cannot reach http://localhost:4000"

**Problem:** Dev server not running

**Solution:**
```bash
# In Terminal 1
./dev-serve.sh
```

### "ModuleNotFoundError: No module named subprocess"

**Problem:** Python version issue (shouldn't happen in Python 3.6+)

**Solution:**
```bash
which python3
# Use the output from this, e.g.:
/usr/bin/python3 scripts/pre-deployment-check.py
```

### Script finds broken links

**Typical causes:**
- Typo in markdown: `/abotu/` instead of `/about/`
- Removed a page but didn't update links
- Image path changed

**Solution:** Edit the offending file, save, then re-run script

### Some checks pass but I see errors in browser

The script checks **links and resources**, not **rendering**.

**For rendering issues:**
1. View page at http://localhost:4000
2. Check browser developer tools (F12) for JavaScript errors
3. Check for Liquid template errors in terminal output

## Pro Tips

### Add to Git Hook (Optional)

Create `.git/hooks/pre-push` to auto-run:

```bash
#!/bin/bash
echo "Running pre-deployment checks..."
python3 scripts/pre-deployment-check.py
exit_code=$?

if [ $exit_code -ne 0 ]; then
  echo "❌ Fix issues before pushing"
  exit 1
fi

echo "✅ Checks passed, proceeding with push"
exit 0
```

Then:
```bash
chmod +x .git/hooks/pre-push
# Now it runs automatically before git push
```

### Check Specific Page

To manually test a specific page while dev server runs:

```bash
# In Terminal 2 (where you'd run the script)
curl -s http://localhost:4000/events/ | grep "href=" | head -5
```

### Monitor GitHub Actions

After pushing:

```bash
# Watch the workflow in real-time
open https://github.com/dustinson/d3cblog.github.io/actions
```

## Related Documentation

- **Full Details:** [PRE_DEPLOYMENT_CHECK.md](PRE_DEPLOYMENT_CHECK.md)
- **Full Checklist:** [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Development Setup:** [DEVELOPMENT.md](DEVELOPMENT.md)

---

**Last Updated:** May 24, 2026  
**Recommended Workflow:** Use this before every deployment


