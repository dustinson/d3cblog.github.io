# Quick Reference: Event Discovery Workflow

**Goal:** Search web for "Dustin Thostenson" + "Delta3Consulting" events, then auto-add to blog.

---

## The Pipeline (TL;DR)

```
GPT (search web with prompts from RESEARCH_PROMPTS.md)
    ↓
Consolidate JSON
    ↓
Copilot (run COPILOT_IMPORT_PROMPT with JSON)
    ↓
Verify locally: ./run-blog
    ↓
Deploy: git push origin main
```

---

## Step 1: Search (Use ChatGPT/Claude.ai)

Use prompts from **`RESEARCH_PROMPTS.md`**:
1. LinkedIn prompt → paste to ChatGPT → get JSON
2. Meetup prompt → paste to ChatGPT → get JSON
3. Sessionize prompt → paste to ChatGPT → get JSON
4. Web Search prompt → paste to ChatGPT → get JSON

**Key:** Ask AI to return ONLY JSON (no explanations).

---

## Step 2: Consolidate

Combine all JSON results into single structure:

```json
{
  "consolidated_events": [
    { "name": "...", "date": "YYYY-MM-DD", "dustin_role": "speaker", "url": "..." },
    { "name": "...", "date": "YYYY-MM-DD", "dustin_role": "speaker", "url": "..." }
  ]
}
```

---

## Step 3: Create Files

**In GitHub Copilot (this IDE):**

Paste the prompt from **`COPILOT_IMPORT_PROMPT.md`** with your JSON data.

That's it. Copilot creates all the markdown files automatically.

---

## Step 4: Verify

```bash
# Check files were created
ls -la _events/

# Build locally
./run-blog

# Visit http://localhost:4000/events
```

---

## Step 5: Deploy

```bash
git add _events/
git commit -m "Add events: [names]"
git push origin main
```

Done. ✅

---

## Monthly Maintenance

Every month (or as needed):
1. Run GPT searches with RESEARCH_PROMPTS.md
2. Get consolidated JSON
3. Paste to Copilot + COPILOT_IMPORT_PROMPT.md
4. Deploy

**Time per run: ~20 minutes**

---

## File Reference

| File | Purpose |
|------|---------|
| `RESEARCH_PROMPTS.md` | Prompts to use in ChatGPT/Claude to search the web |
| `COPILOT_IMPORT_PROMPT.md` | Prompt to paste in GitHub Copilot with JSON data |
| `QUICK_REFERENCE.md` | This file |

---

## One-Liner Quick Start

👉 **Go to ChatGPT. Copy a prompt from `RESEARCH_PROMPTS.md`. Paste it. Get JSON. Return to GitHub Copilot with JSON + `COPILOT_IMPORT_PROMPT.md` content.**

That's the entire workflow. 🚀

