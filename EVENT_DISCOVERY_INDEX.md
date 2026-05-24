# Event Discovery & Blog Automation Files

**All the files you need for event research and automation are here.**

---

## 📍 Files in Your Repo

### Quick Start (Start Here)
- **`EVENT_DISCOVERY_PROMPT.md`** ← **USE THIS ONE**
  - One-stop prompt for web research
  - Includes ChatGPT search prompt + Copilot return prompt
  - Copy → run search → paste back to me
  - Fastest path forward

### Detailed Guides (Reference)
- **`QUICK_REFERENCE.md`** — TL;DR of the entire workflow
- **`RESEARCH_PROMPTS.md`** — Individual prompts for LinkedIn, Meetup, Sessionize, web
- **`COPILOT_IMPORT_PROMPT.md`** — Detailed import instructions
- **`EVENT_DISCOVERY_INDEX.md`** ← This file

---

## 🚀 The Fast Path (What to Actually Do)

1. **Open this IDE** (you're already here)
2. **Open `EVENT_DISCOVERY_PROMPT.md`**
3. **Copy the "Web Search Prompt" section**
4. **Paste into ChatGPT**
5. **Get JSON back from ChatGPT**
6. **Return to this IDE**
7. **Copy the "Return to Copilot" section**
8. **Replace `[JSON DATA HERE]` with your JSON**
9. **Paste it back to me (GitHub Copilot)**
10. **Done** — files are created automatically

**Total time: ~20 minutes**

---

## 📋 Event Files Created So Far

Check your `_events/` directory to see what's been added:

```bash
ls -la _events/
```

Current events:
- `2025-10-20-NDC-Porto-2025.md`
- `2026-04-09-DotNet-Noon-Past-Didnt-Go-Anywhere.md`
- `2026-11-07-Iowa-Code-Camp-Fall-2026.md`

---

## 🔄 Monthly Workflow

Every month (or as needed):

1. Run `EVENT_DISCOVERY_PROMPT.md` through ChatGPT
2. Copy JSON back here with return prompt
3. Copilot auto-creates files
4. `./run-blog` to verify locally
5. `git push` to deploy

---

## 📖 Which File Should I Use?

| Your Situation | File to Use |
|---|---|
| First time, want it quick | `EVENT_DISCOVERY_PROMPT.md` |
| Want detailed step-by-step | `QUICK_REFERENCE.md` |
| Want individual search templates | `RESEARCH_PROMPTS.md` |
| Need deep instructions | `COPILOT_IMPORT_PROMPT.md` |

---

## ✅ Success Criteria

After each run, verify:
- [ ] Event files created in `_events/YYYY-MM-DD-*.md`
- [ ] `./run-blog` works locally
- [ ] Events appear at http://localhost:4000/events
- [ ] `git push` succeeds

---

## Event Discovery Checklist

**Before running research:**
- [ ] Have ChatGPT or Claude.ai ready with web access
- [ ] Have this IDE open
- [ ] Understand the 2-step process (search → return)

**After running research:**
- [ ] Received JSON from ChatGPT
- [ ] Consolidated all events into one JSON array
- [ ] Returned JSON to me with return prompt
- [ ] Verified files created with `ls -la _events/`

---

## Files You Created / Reference

- **Your blog repo:** `/Users/dustinson/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/d3cblog.github.io`
- **Events directory:** `_events/`
- **Assets for images:** `assets/images/`

---

## Questions?

Refer back to:
1. `EVENT_DISCOVERY_PROMPT.md` — for prompts
2. `QUICK_REFERENCE.md` — for workflow overview  
3. `COPILOT_IMPORT_PROMPT.md` — for detailed instructions

---

## Next Steps

👉 **Ready to find more events?**

1. Open `EVENT_DISCOVERY_PROMPT.md`
2. Follow the steps
3. Return here with JSON

**That's the entire process.** 🚀

