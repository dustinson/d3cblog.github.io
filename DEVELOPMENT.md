# Development Guide

Everything you need to know about developing the d3cblog site locally.

## Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/dustinson/d3cblog.github.io.git
cd d3cblog.github.io

# Install dependencies and setup git hooks
./scripts/setup-dev-env.sh
```

### 2. Start Development Server

```bash
# Option A: Open in browser automatically
make dev

# Option B: Start server manually (http://localhost:4000)
make serve

# Option C: Using the shell script directly
./run-blog
```

## Available Commands

### Development
```bash
make dev           # Start server with auto-browser launch
make serve         # Start server (no browser launch)
```

### Building
```bash
make build         # Full production build with cleanup
make clean         # Remove _site/ and cache
```

### Testing & Checks
```bash
make audit         # Security vulnerability scan
make outdated      # Check for outdated gems
make check         # Run all pre-deploy checks (audit + build)
make status        # Show environment info
```

### Deployment
```bash
make deploy        # Push to main (requires clean git state)
make update        # Update gems conservatively
```

### Help
```bash
make help          # Show all available commands
```

## Workflow

### Creating a Blog Post

1. Create new file: `_posts/YYYY-MM-DD-title.md`
   ```yaml
   ---
   layout: post
   title: "Your Post Title"
   author: Dustin Thostenson
   categories: [category]
   ---
   
   Your content here...
   ```

2. Test locally:
   ```bash
   make dev
   ```

3. Commit and push:
   ```bash
   git add _posts/YYYY-MM-DD-title.md
   git commit -m "Post: Your Post Title"
   make deploy
   ```

### Creating an Event

1. Create new file: `_events/event-slug.md`
   ```yaml
   ---
   layout: post
   title: "Event Name"
   date: YYYY-MM-DD
   ---
   
   Event details...
   ```

2. Test locally: `make dev`
3. Commit and deploy the same way as posts

### Updating Site Configuration

1. Edit `_config.yml` for production settings
2. Edit `_config_dev.yml` for development overrides
3. Test locally to verify changes
4. Commit and push

## Git Hooks

### Pre-push Hook

After running `./scripts/setup-dev-env.sh`, a pre-push hook will automatically:
- Run security audit
- Test production build
- Prevent pushing if either check fails

**To skip in an emergency:**
```bash
git push --no-verify origin main
```

## Editor Configuration

The repo includes `.editorconfig` for consistent formatting. Most editors (VS Code, JetBrains, etc.) support it automatically.

If your editor doesn't support editorconfig, follow these conventions:
- **Lines:** 2 spaces (Ruby, YAML, Markdown)
- **Line endings:** LF (Unix-style)
- **Charset:** UTF-8
- **Trim trailing whitespace:** Yes (except markdown)

## Dependency Management

### Check Security Issues
```bash
bundle audit
```

### Check Outdated Gems
```bash
bundle outdated
```

### Update Gems Safely
```bash
# Conservative update (recommended)
bundle update --conservative

# Review changes
git diff Gemfile.lock

# Test the build
make build

# Commit if successful
git add Gemfile.lock
git commit -m "Update dependencies"
```

### Ruby Version Notes

**Local Development:** Ruby 3.1.2 (working directory)
**Production:** Ruby 3.3 (GitHub Actions)

This means:
- Local builds work but may show nokogiri CVE warnings (expected)
- Production builds via GitHub Actions are fully patched (Ruby 3.3)
- To remove local warnings, upgrade to Ruby 3.2+:
  ```bash
  rbenv install 3.3.0
  rbenv local 3.3.0
  bundle update
  ```

## Build Process

### Development Build
```bash
JEKYLL_ENV=development bundle exec jekyll serve --config _config.yml,_config_dev.yml
```

Uses `_config_dev.yml` overrides for:
- URL redirects to localhost
- Asset rewriting (localhost:4000)
- Development banner

### Production Build
```bash
JEKYLL_ENV=production bundle exec jekyll build --verbose
```

Creates `_site/` directory with:
- All posts and pages
- Optimized CSS/JS
- Proper URLs (delta3consulting.com)
- No development banner

### What Gets Built

- **Posts:** 80+ blog posts from `_posts/`
- **Events:** Collections from `_events/`
- **Pages:** Static pages (contact, about, etc.)
- **Community:** Leadership, presentations, interviews
- **Videos:** Embedded video listings
- **Static:** CSS, JS, images, favicon

Total: 100+ pages generated in ~5 seconds

## Troubleshooting

### Port Already in Use
```bash
lsof -ti:4000 | xargs kill -9
make dev
```

### Build Fails with Liquid Errors
```bash
JEKYLL_ENV=production bundle exec jekyll build --verbose
# Look at the error (includes file and line number)
# Fix the template or data file
```

### Bundle Install Fails
```bash
rm -rf Gemfile.lock vendor
bundle install
```

### Changes Not Showing

1. Hard refresh browser: **Cmd+Shift+R** (Mac) or **Ctrl+Shift+R** (Windows/Linux)
2. Stop and restart server: **Ctrl+C**, then `make dev`
3. Clear Jekyll cache: `make clean && make dev`

### Slow Builds

Use incremental rebuild:
```bash
bundle exec jekyll serve --incremental
```

Only rebuilds changed files (much faster once initial build is done).

## Testing Before Deploy

Always run these before pushing:

```bash
# 1. Security check
bundle audit

# 2. Production build test
JEKYLL_ENV=production bundle exec jekyll build --verbose

# 3. Automated link & page check
./dev-serve.sh &
sleep 5
python3 scripts/pre-deployment-check.py
# Press Ctrl+C to stop the server

# 4. Manual browser test
make dev
# Visit http://localhost:4000
# Click around, verify nothing is broken

# 5. Commit and push
git add .
git commit -m "Your change description"
make deploy
```

Or use the shortcut:
```bash
make check
```

## Pre-Deployment Automation

### Overview

The site includes automated checks to catch broken links, missing resources, and inaccessible pages before deployment.

**Why this matters:**
- Catches issues early before they reach production
- Prevents broken links to content
- Ensures all events and pages are accessible
- Saves debugging time post-deploy

### Running Locally

Before deploying, run the automated pre-deployment check:

```bash
# Terminal 1: Start dev server
./dev-serve.sh

# Terminal 2: Run checks
python3 scripts/pre-deployment-check.py
```

**Expected output on success:**
```
======================================================================
✅ ALL CHECKS PASSED - READY FOR PRODUCTION
======================================================================
```

**Exit codes:**
- `0` = Success (all checks passed)
- `1` = Failure (broken links or missing resources found)

### GitHub Actions Workflow

When you create a pull request to `main`, the automated workflow runs automatically:

1. **Checkout code** - Gets the PR changes
2. **Setup Ruby** - Prepares Ruby 3.1.2 environment
3. **Install dependencies** - Runs `bundle install`
4. **Build site** - Production build with `-verbose` flag
5. **Start dev server** - Launches Jekyll server on port 4000
6. **Run checks** - Executes pre-deployment check script
7. **Report results** - Shows pass/fail status in PR

**Viewing workflow results:**
- Check appears in the pull request under "Checks" tab
- Click through to see detailed logs
- Review any failures before merging

**Workflow file:** `.github/workflows/pre-deployment-check.yml`

### What Gets Checked

✅ **Main Pages**
- Homepage
- Events index page
- Blog page
- Videos page
- Search page

✅ **Assets**
- CSS stylesheets
- JavaScript files

✅ **Events**
- All 75+ event pages load
- Links within event pages work
- Event resources accessible

✅ **Resources**
- All images load correctly
- All dependent resources available

### Troubleshooting Checks

**If checks fail locally:**
1. Check the error message (usually indicates which page failed)
2. Try: `make clean && make dev`
3. Try: `bundle update --conservative`
4. Check: See `TROUBLESHOOTING.md` for specific issues

**If GitHub workflow fails:**
1. Click the workflow run in GitHub Actions
2. View detailed logs
3. Fix the issue locally
4. Re-run workflow by pushing a new commit

For more info, see: `PRE_DEPLOYMENT_CHECK.md`

## Deploying

### Standard Deployment

```bash
# Make changes
# Test locally (make dev)  
# Commit

git add .
git commit -m "Describe your changes"
git push origin main

# GitHub Actions deploys automatically (~3-4 minutes)
```

### Using make deploy

```bash
# Ensures git is clean, then pushes
make deploy
```

### Verify Deployment

1. Check GitHub Actions: https://github.com/dustinson/d3cblog.github.io/actions
2. Wait for ✅ status
3. Visit https://delta3consulting.com
4. Verify changes appear (hard refresh if needed)

## Environment Variables

### Development
```bash
JEKYLL_ENV=development  # Show dev banner, rewrite URLs to localhost
```

### Production
```bash
JEKYLL_ENV=production   # Normal build, real URLs, no dev banner
```

Set in shell before building:
```bash
export JEKYLL_ENV=production
bundle exec jekyll build
```

Or inline:
```bash
JEKYLL_ENV=production bundle exec jekyll build
```

## Additional Resources

- **Jekyll Docs:** https://jekyllrb.com/docs/
- **GitHub Pages Docs:** https://docs.github.com/en/pages
- **Liquid Template Docs:** https://jekyll.github.io/liquid/
- **Markdown Reference:** https://www.markdownguide.org/
- **YAML Syntax:** https://yaml.org/

## Getting Help

### Site Documentation
- `README.md` - Quick start
- `TROUBLESHOOTING.md` - Common issues
- `DEPLOYMENT_CHECKLIST.md` - Pre-deploy verification
- `DEVELOPMENT.md` - (This file)

### Project Files
- `Makefile` - Command reference
- `.editorconfig` - Code formatting standards
- `scripts/` - Utility scripts

### Questions?
Contact: Dustin Thostenson
Repository: https://github.com/dustinson/d3cblog.github.io

---

**Happy developing! 🚀**

