# Custom Slash Commands for Blog Project

**Location to configure:** JetBrains IDE → Settings → Tools → GitHub Copilot → Commands

Copy these slash command definitions into your IDE. They'll make development much faster.

---

## Essential Commands

### `/run-blog`
**Description:** Start dev server and open in browser  
**Command:** `./run-blog`  
**Context:** Development  
**Output:** URL of running server

### `/test-build`
**Description:** Run production build to verify no errors  
**Command:** `JEKYLL_ENV=production bundle exec jekyll build --verbose 2>&1 | tail -30`  
**Context:** Testing  
**Output:** Build status, exit code, last 30 lines (errors surface here)  
**Pass criteria:** Exit 0, contains "done in", no "Error:" or "Liquid Exception:" lines

### `/deploy`
**Description:** Push changes to production (USER ONLY — Copilot never runs this)  
**Command:** `git push origin main`  
**Context:** Deployment  
**Output:** Deployment status and GitHub Pages URL  
**⚠️ Note:** Always run `/check` first. Copilot stages and commits; you push.

### `/check`
**Description:** Run pre-deployment checklist  
**Command:** `bundle audit && JEKYLL_ENV=production bundle exec jekyll build --verbose 2>&1 | tail -30`  
**Context:** Testing  
**Output:** Security audit + build verification  
**Use before:** Every `git push origin main`

---

## Cleanup Commands

### `/cleanup-item`
**Description:** Address a specific item from SITE_CLEANUP_AUDIT.md  
**Usage:** "Address cleanup item C-1" or "Address items H-1 through H-3"  
**Context:** Cleanup  
**Protocol:**
1. Read the item from `SITE_CLEANUP_AUDIT.md`
2. Make only the described changes
3. Run `/test-build` — must pass before proceeding
4. Show `git diff --stat` for review
5. `git add [specific files]` + `git commit -m "cleanup: [ID] [description]"`
6. Report: files changed, build status, commit hash, what to verify in browser
7. **Never `git push`** — user always pushes to production

**Commit format:** `cleanup: C-1 Short description of what changed`

### `/audit-status`
**Description:** Show open cleanup items from SITE_CLEANUP_AUDIT.md  
**Context:** Cleanup  
**Output:** Summary of remaining open items grouped by priority (🔴🟠🟡🟢)

---

## Development Commands

### `/serve-dev`
**Description:** Start jekyll dev server with verbose output  
**Command:** `./dev-serve.sh`  
**Context:** Development  
**Output:** Server status and local URL

### `/build`
**Description:** Quick development build  
**Command:** `bundle exec jekyll build`  
**Context:** Development  
**Output:** Build results

### `/clean`
**Description:** Clean build artifacts  
**Command:** `./clean.sh`  
**Context:** Development  
**Output:** Cleanup status

---

## Event Discovery Commands

### `/discover-events`
**Description:** Show event discovery prompt  
**Context:** Event Management  
**Output:** Display `EVENT_DISCOVERY_PROMPT.md` instructions

### `/add-event`
**Description:** Template for adding a new event  
**Context:** Event Management  
**Output:** Event markdown template

---

## Content Commands

### `/new-post`
**Description:** Create a new blog post template  
**Context:** Content  
**Output:** New post file path

### `/new-draft`
**Description:** Create a new draft post  
**Context:** Content  
**Output:** New draft file path

---

## Reference Commands

### `/docs`
**Description:** Show development documentation  
**Context:** Help  
**Output:** Links to DEVELOPMENT.md, README.md, etc.

### `/troubleshoot`
**Description:** Show troubleshooting guide  
**Context:** Help  
**Output:** TROUBLESHOOTING.md contents

### `/status`
**Description:** Show project status  
**Context:** Help  
**Output:** Current phase status, blockers, and todos

---

## Security Commands

### `/audit`
**Description:** Check for security vulnerabilities  
**Command:** `bundle audit`  
**Context:** Security  
**Output:** Vulnerability report

### `/update-deps`
**Description:** Check for outdated dependencies  
**Command:** `bundle outdated`  
**Context:** Security  
**Output:** Outdated packages list

---

## Git Commands

### `/status-git`
**Description:** Show git status  
**Command:** `git status`  
**Context:** Version Control  
**Output:** Current git status

### `/commit`
**Description:** Template for committing changes  
**Context:** Version Control  
**Output:** Commit message template

### `/log`
**Description:** Show recent commits  
**Command:** `git log --oneline -10`  
**Context:** Version Control  
**Output:** Last 10 commits

---

## Most Useful Commands (Quick Start)

If you only want to add a few, prioritize these:

1. ✅ `/run-blog` — Start dev server
2. ✅ `/test-build` — Verify production build (always before committing)
3. ✅ `/check` — Full pre-deployment checklist (always before pushing)
4. ✅ `/cleanup-item` — Address an item from `SITE_CLEANUP_AUDIT.md` safely
5. ✅ `/audit-status` — See what cleanup is still open
6. ✅ `/discover-events` — Event discovery workflow

---

## How to Add These to Your IDE

**In JetBrains (Rider/RD):**

1. **Settings** → **Tools** → **GitHub Copilot**
2. Click **"Commands"** or **"Slash Commands"**
3. Click **"+"** to add new command
4. Fill in:
   - **Command:** `/run-blog` (example)
   - **Description:** Start dev server and open in browser
   - **Action:** `./run-blog`
5. Repeat for other commands

---

## Example Configuration (JSON Format)

If your IDE supports JSON import:

```json
{
  "commands": [
    {
      "command": "/run-blog",
      "description": "Start dev server and open in browser",
      "action": "./run-blog",
      "context": "development"
    },
    {
      "command": "/test-build",
      "description": "Run production build verification — must pass before any commit",
      "action": "JEKYLL_ENV=production bundle exec jekyll build --verbose 2>&1 | tail -30",
      "context": "testing"
    },
    {
      "command": "/check",
      "description": "Full pre-deployment checks — run before every push",
      "action": "bundle audit && JEKYLL_ENV=production bundle exec jekyll build --verbose 2>&1 | tail -30",
      "context": "testing"
    },
    {
      "command": "/deploy",
      "description": "Push to production (user-only, never Copilot)",
      "action": "git push origin main",
      "context": "deployment"
    },
    {
      "command": "/cleanup-item",
      "description": "Address a SITE_CLEANUP_AUDIT.md item: build-test-commit workflow",
      "context": "cleanup"
    },
    {
      "command": "/audit-status",
      "description": "Show remaining open items from SITE_CLEANUP_AUDIT.md",
      "context": "cleanup"
    },
    {
      "command": "/discover-events",
      "description": "Event discovery workflow",
      "context": "event-management"
    }
  ]
}
```

---

## Usage Examples

Once configured, in your IDE chat:

```
/run-blog
→ Starts dev server automatically

/test-build
→ Runs production build, exits 0 = clean

/check
→ Runs security audit + build check (run before every push)

"Address cleanup item C-1"
→ Copilot reads audit, makes change, builds, commits — you review and push

"Address items H-1 through H-3"
→ Copilot batches related items into a single tested commit

/audit-status
→ Shows remaining open cleanup items by priority

/discover-events  
→ Shows event discovery instructions
```

---

## Notes

- Commands are **local to your IDE** — no web access needed
- They're **reusable** every time you open this project
- Add more commands as your workflow evolves
- Keep this file updated as new processes are created

---

## File Reference

This file helps you set up:
- **Faster development** (~2 seconds to start dev server with `/run-blog`)
- **Safer deployments** (pre-check with `/check` before pushing)
- **Consistent workflows** (same commands every time)

**Your setup: Next steps to enable these commands in your IDE!** 🚀

