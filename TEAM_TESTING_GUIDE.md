# Team Testing Guide: Pre-Deployment Automation

**Purpose:** Guide team members through using the pre-deployment check script  
**Target Audience:** Developers, content managers, and anyone deploying the D3 Blog  
**Last Updated:** May 26, 2026

---

## Quick Start (5 minutes)

### For Developers

1. **Start the development server:**
   ```bash
   cd ~/path/to/d3cblog.github.io
   ./dev-serve.sh
   ```
   
   Wait for: `Server running on http://localhost:4000`

2. **In a new terminal, run the check:**
   ```bash
   python3 scripts/pre-deployment-check.py
   ```

3. **Review the output:**
   - ✅ If you see "ALL CHECKS PASSED" → Safe to deploy
   - ❌ If you see issues → Fix them before deploying

4. *(Optional) Generate a report for team visibility:*
   ```bash
   python3 scripts/pre-deployment-check.py --html deployment-report.html
   ```

### For Non-Developers

If you've made changes to content (events, blog posts, etc.):

1. Ask your developer to run the check before deployment
2. Wait to see the result (takes ~20-30 seconds)
3. If issues are found, they'll let you know what to fix

---

## Complete Setup Instructions

### Prerequisites

- Python 3.6 or higher (check with `python3 --version`)
- macOS or Linux (or Windows with WSL/Git Bash)
- Git installed and repository cloned
- cURL available (comes pre-installed on macOS/Linux)

### Verify Prerequisites

```bash
# Verify Python
python3 --version

# Verify cURL
which curl
curl --version

# Verify in the right directory
pwd  # Should end in "d3cblog.github.io"
ls scripts/pre-deployment-check.py  # Should exist
```

### First-Time Run

```bash
# Terminal 1: Start dev server
cd ~/path/to/d3cblog.github.io
./dev-serve.sh

# Wait for: "Server running on http://localhost:4000"
# Keep this terminal open

# Terminal 2: Run the check (in new terminal)
cd ~/path/to/d3cblog.github.io
python3 scripts/pre-deployment-check.py

# Wait ~20-30 seconds for results
```

---

## Understanding Results

### Success Example

```
======================================================================
PRE-DEPLOYMENT CHECK SUMMARY
======================================================================

✓ Passed Checks: 11
  • Main page: Homepage
  • Main page: Events Index
  • Main page: Blog
  • Main page: Videos
  • Main page: Search
  • Asset: CSS
  • Asset: JavaScript
  • Event discovery: 75 events found
  • Event pages: All 75 accessible
  • Event links: All accessible
  • Event resources: All accessible

======================================================================
✅ ALL CHECKS PASSED - READY FOR PRODUCTION
======================================================================
```

**Interpretation:** All checks passed. Safe to deploy. Exit code: 0

### Failure Example

```
❌ Issues Found: 2

BROKEN_LINKS (2):
  • /events/2024-01-01-Event: /missing-page (HTTP 404)
  • /events/2024-01-02-Event: /about-us (HTTP 404)

BROKEN_RESOURCES (1):
  • /events/2024-01-03-Event: /images/logo.png (HTTP 404)

======================================================================
⚠️  ISSUES FOUND - DO NOT DEPLOY UNTIL FIXED
======================================================================
```

**Interpretation:** 3 issues found:
- 2 broken internal links (need to fix URLs)
- 1 missing image (need to add image or fix path)

**Exit code:** 1 (do not deploy)

---

## Troubleshooting

### "Cannot reach http://localhost:4000"

**Problem:** Dev server is not running

**Solution:**
```bash
# In Terminal 1, start the server
./dev-serve.sh

# Wait for message: "Server running on http://localhost:4000"
# Then try the check again
```

### "command not found: python3"

**Problem:** Python 3 is not installed or not in PATH

**Solution (macOS):**
```bash
# Install with Homebrew
brew install python3

# Or use full path
/usr/local/bin/python3 scripts/pre-deployment-check.py
```

**Solution (Linux):**
```bash
# Install with apt
apt-get install python3

# Or with yum
yum install python3
```

### "found 0 events"

**Problem:** Event discovery failed

**Causes:**
- Dev server not running properly
- Events index page changed
- Broken HTML in events/index.md

**Solutions:**
1. Restart dev server: `./dev-serve.sh`
2. Check events page loads: `curl http://localhost:4000/events/`
3. Check for HTML errors in events/index.md

### Script hangs for >60 seconds

**Problem:** Script might be waiting for slow network responses

**Solution:**
- Press `Ctrl+C` to stop
- Check your internet connection
- Try running again
- If it's always slow, consider using without `--check-external` flag

---

## Advanced Usage

### Generate HTML Reports

Perfect for sharing results with team or keeping records:

```bash
# Generate report
python3 scripts/pre-deployment-check.py --html deployment-report.html

# Open in browser (macOS)
open deployment-report.html

# View on macOS with default app
python3 scripts/pre-deployment-check.py --html report.html && open report.html
```

**Report includes:**
- Overall status (pass/fail)
- Summary statistics
- Itemized list of checks
- Performance timing
- Timestamp

### Check External Links

Be cautious: This is slower and may have false positives

```bash
# Check external links with retry logic
python3 scripts/pre-deployment-check.py --check-external

# With report
python3 scripts/pre-deployment-check.py --check-external --html report.html
```

**When to use:**
- Monthly site health review
- Before major releases
- If you added new external references

**When NOT to use:**
- Daily pre-deployment checks (too slow)
- CI/CD workflows (external sites are unreliable)

### Verbose Output

See detailed results for every check:

```bash
python3 scripts/pre-deployment-check.py --verbose

# Shows:
# - Each page checked
# - Each link checked
# - Each resource checked
# Useful for debugging specific issues
```

---

## Common Issues When Deploying

### "Script says all checks passed but I see errors on the live site"

**What the script checks:**
- ✅ Pages load (HTTP 200)
- ✅ Links point to real pages (HTTP 200)
- ✅ Images exist (HTTP 200)

**What the script DOES NOT check:**
- ❌ Visual rendering (CSS/design)
- ❌ JavaScript functionality
- ❌ Form validation
- ❌ Mobile responsiveness
- ❌ Accessibility

**How to debug:**
1. Visit http://localhost:4000 in your browser
2. Open DevTools (F12 in Chrome/Firefox)
3. Check Console tab for JavaScript errors
4. Check Network tab for failed requests
5. Check if content looks right visually

### "Some links are red in the report but work manually"

This can happen with:
- Sites that block automated requests
- Rate limiting (too many requests)
- Temporary server issues

**Solution:**
1. Use `--check-external` flag to enable retry logic
2. Manually verify the link in browser
3. If manual check works, link is fine

### "New content added but script doesn't see it"

**Common causes:**
- Dev server has stale cache
- Jekyll hasn't rebuilt the site

**Solution:**
```bash
# Stop dev server (Ctrl+C in Terminal 1)
# Clear cache and rebuild
bundle exec jekyll clean

# Restart dev server
./dev-serve.sh

# Then run check again
python3 scripts/pre-deployment-check.py
```

---

## Integration into Your Workflow

### Before Every Deployment

**Checklist:**
1. ✓ All changes committed
2. ✓ Dev server running
3. ✓ Check script passed
4. ✓ Quick visual review in browser
5. ✓ Ready to `git push`

### For Pull Requests

GitHub Actions will automatically run checks. If checks fail:

1. Fix the issues locally
2. Test locally: `python3 scripts/pre-deployment-check.py`
3. Commit fix
4. Push to branch
5. Check runs automatically
6. PR can be merged

### For Production Monitoring

After deployment, there is currently no scheduled daily GitHub Actions monitor in this repository. To verify production:

1. Run the local check manually when needed
2. Review the live site directly to confirm expected behavior
3. Use PR checks to catch issues before deployment
4. Fix and redeploy if problems are found

---

## Feedback & Improvements

### What We Want to Know

- ✅ **What works well:**
  - Easy to run?
  - Output is clear?
  - Found real issues?

- ❌ **What's confusing:**
  - Commands hard to understand?
  - Output doesn't make sense?
  - Unexpected results?

- 💡 **What could improve:**
  - Missing checks?
  - Too slow?
  - Want different output format?

### How to Give Feedback

1. **During Testing:** Take notes
2. **After Testing:** Share with Dustin
3. **Issues Found:** Document exactly what happened
   - What command did you run?
   - What was the output?
   - What did you expect?
   - What actually happened?

### Example Feedback

**Good:** "When I added a new event page, the script correctly caught that internal links were broken. It helped me fix the issue before deploying."

**Good:** "The HTML report is nice for sharing with non-technical people. It's clear which checks passed and failed."

**Constructive:** "Running the external link check takes 5 minutes and gave mostly false positives. I'd prefer it be faster or have better filtering."

---

## Success Criteria

The script is working well if:

1. ✅ Takes 20-30 seconds to run normally
2. ✅ Catches real issues (broken links, missing images)
3. ✅ Doesn't give false positives too often
4. ✅ Output is clear and actionable
5. ✅ Team members understand how to use it
6. ✅ Catches issues before they reach production

---

## Resources

- **Quick Start:** See `QUICK_START_DEPLOYMENT.md`
- **Technical Details:** See `PRE_DEPLOYMENT_CHECK.md`
- **Full Checklist:** See `DEPLOYMENT_CHECKLIST.md`
- **Troubleshooting:** See `TROUBLESHOOTING.md`
- **Setup Guide:** See `DEVELOPMENT.md`

---

## FAQ

**Q: Can I use this on Windows?**  
A: Yes! Use WSL (Windows Subsystem for Linux) or Git Bash. Then follow the same steps.

**Q: What if I don't have Python installed?**  
A: Install Python 3 from python.org or use package manager (brew, apt, etc)

**Q: Can I add this to my Git workflow?**  
A: Yes! See `.git/hooks/pre-push` section in QUICK_START_DEPLOYMENT.md

**Q: Why does the check take so long?**  
A: It's checking 75 event pages + links + resources. Can't be much faster without losing accuracy.

**Q: Can I check only specific pages?**  
A: Currently, no. But you could run manual curl commands: `curl http://localhost:4000/events/DATE-slug`

**Q: What if I find a bug in the script?**  
A: Document the issue and let Dustin know with exact steps to reproduce.

---

**Questions?** Ask Dustin or the team. We want to make this tool work for everyone!


