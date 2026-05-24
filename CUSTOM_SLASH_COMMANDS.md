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
**Command:** `JEKYLL_ENV=production bundle exec jekyll build`  
**Context:** Testing  
**Output:** Build status and errors (if any)

### `/deploy`
**Description:** Push changes to production  
**Command:** `git push origin main`  
**Context:** Deployment  
**Output:** Deployment status and GitHub Pages URL

### `/check`
**Description:** Run pre-deployment checklist  
**Command:** `bundle audit && JEKYLL_ENV=production bundle exec jekyll build --verbose`  
**Context:** Testing  
**Output:** Security audit + build verification

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
2. ✅ `/test-build` — Verify production build
3. ✅ `/check` — Pre-deployment checklist
4. ✅ `/discover-events` — Event discovery workflow

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
      "description": "Run production build verification",
      "action": "JEKYLL_ENV=production bundle exec jekyll build",
      "context": "testing"
    },
    {
      "command": "/deploy",
      "description": "Push to production",
      "action": "git push origin main",
      "context": "deployment"
    },
    {
      "command": "/check",
      "description": "Pre-deployment checks",
      "action": "bundle audit && JEKYLL_ENV=production bundle exec jekyll build --verbose",
      "context": "testing"
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
→ Runs production build to verify

/check
→ Runs security audit + build check

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

