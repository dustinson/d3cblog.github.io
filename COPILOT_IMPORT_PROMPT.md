# Return Prompt: Event Data to Blog Automation

Once you have the JSON event data from GPT searches, use this prompt with GitHub Copilot to automatically create all blog event files.

---

## Master Prompt for Copilot

```
I have gathered event data for Dustin Thostenson and Delta3Consulting from LinkedIn, Meetup, and Sessionize.
Create event markdown files for each in my blog's _events/ directory.

Here is the consolidated event data as JSON:

[PASTE YOUR JSON DATA HERE]

Instructions:
1. For each event object in the JSON:
   - Create a new markdown file: _events/YYYY-MM-DD-[slugified-event-name].md
   - Use this exact front matter structure:
     ---
     layout: post
     sidebar: left
     subheadline: [type: Presentation/Conference/Workshop/Webinar]
     title: "[event name]"
     teaser: "[2-sentence teaser about the event/talk]"
     breadcrumb: false
     tags:
         - presentation
         - [topic-based tags from the event]
     categories:
         - community
         - presentation
     event_date: YYYY-MM-DD
     image:
         thumb: [event-name-placeholder].png
         title: [event-name-placeholder].png
         caption: "[Event name or organization]"
         caption_url: [url from JSON]
     ---

   - Write 2-3 sentences describing the event/talk in the body
   - If role is "speaker" or "presenter", focus on what Dustin presented
   - If role is "panelist" or "organizer", mention that context
   - If it's a past event, use past tense; if upcoming, present/future tense
   - Include the URL in the caption_url field

2. File naming: _events/YYYY-MM-DD-[event-name].md
   - Use hyphens for spaces
   - Keep filename concise (max 60 chars)
   - Format: YYYY-MM-DD-Iowa-Code-Camp.md

3. For images:
   - Use placeholder names: [event-name-placeholder].png
   - I will add actual images later
   - Do NOT create image files, just reference them in front matter

4. Output format:
   After creating files, provide:
   - [ ] List each file created with its path
   - [ ] Total event count
   - [ ] Date range of events
   - [ ] Any events that were skipped and why

5. Validate:
   - All dates are valid (YYYY-MM-DD)
   - All URLs are included in caption_url
   - No duplicate events
   - File paths follow the pattern: _events/YYYY-MM-DD-[name].md
```

---

## Step-by-Step Process

### Step 1: Run GPT Searches
Use the prompts from `RESEARCH_PROMPTS.md` in ChatGPT or Claude.ai to gather event data. Ask the AI to return ONLY valid JSON.

### Step 2: Consolidate the JSON
Combine results from all searches into a single array. Example:

```json
{
  "consolidated_events": [
    {
      "name": "Iowa Code Camp",
      "date": "2024-10-01",
      "type": "conference",
      "dustin_role": "speaker",
      "topic": "Techniques to Tackle Tech Debt",
      "url": "https://iowacodecamp.com"
    },
    {
      "name": "PMI Agile 2026",
      "date": "2026-04-15",
      "type": "conference",
      "dustin_role": "review_team",
      "topic": "PMI Agile Review and Strategy",
      "url": "https://www.pmi.org/agile"
    }
  ]
}
```

### Step 3: Use the Master Prompt
Copy the master prompt above and paste to GitHub Copilot with your JSON data.

### Step 4: Verify Files Created
After Copilot creates the files:
```bash
ls -la _events/
# Should show new YYYY-MM-DD-*.md files
```

### Step 5: Build and Test Locally
```bash
./run-blog
# Visit http://localhost:4000/events
# Verify all new events appear in the list
```

### Step 6: Add Images (Manual Step)
- Gather promotional images for each event
- Place in: `assets/images/`
- Note the filename
- Update the `image:` section in each event file with correct filename

### Step 7: Commit and Deploy
```bash
git add _events/
git add assets/images/  # if you added images
git commit -m "Add events: [event names]"
git push origin main
```

---

## Troubleshooting

**Q: Copilot says "file already exists"**
- A: The event file is already in your _events/ folder. Check if it's a duplicate before recreating.

**Q: Images aren't showing**
- A: Make sure image filenames in front matter match the actual files in assets/images/

**Q: Event doesn't appear on /events page**
- A: Check that `event_date` is in YYYY-MM-DD format and the layout is `post`

**Q: URL is broken in event page**
- A: Make sure `caption_url` in front matter is a complete, valid URL

---

## Future Runs

This process is **repeatable**:

1. Run GPT searches monthly for new events
2. Consolidate JSON data
3. Paste to Copilot with master prompt
4. Copilot auto-creates files
5. Add images and deploy

**No manual YAML formatting needed.** Copilot handles the structure automatically.

---

## Quick Reference

| Step | Tool | Time |
|------|------|------|
| 1. Search for events | ChatGPT / Claude.ai | 10-15 min |
| 2. Consolidate JSON | Copy-paste | 2 min |
| 3. Create blog files | GitHub Copilot | 2 min |
| 4. Test locally | ./run-blog | 2 min |
| 5. Deploy | git push | 1 min |
| **Total** | **Various** | **~20 min** |

---

## Example: Complete JSON Input

Here's a fully formatted example you can use as a template:

```json
{
  "consolidated_events": [
    {
      "name": "Iowa Code Camp - Techniques To Tackle Tech Debt",
      "date": "2024-10-01",
      "type": "conference",
      "dustin_role": "speaker",
      "topic": "Technical, political, and procedural techniques to create more joy in new work with less pain from the old",
      "url": "https://iowacodecamp.com/schedule"
    },
    {
      "name": "The Past Didn't Go Anywhere",
      "date": "2026-07-25",
      "type": "presentation",
      "dustin_role": "speaker",
      "topic": "[Get topic from LinkedIn/Meetup]",
      "url": "[Get URL from event registration]"
    }
  ]
}
```

Copy this format when returning results to me. 🚀

