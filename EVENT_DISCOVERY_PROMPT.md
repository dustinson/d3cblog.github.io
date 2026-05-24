# Easy Event Discovery Prompt

## For Future Event Research Runs

**Location:** This file in your repo for easy discovery and copying.

---

## One-Click Workflow

**When you want to add new events to your blog:**

1. Open ChatGPT (or Claude.ai)
2. Copy the **"Web Search Prompt"** section below
3. Paste into ChatGPT
4. Get JSON results
5. Copy the **"Return to Copilot"** section below
6. Replace `[JSON DATA HERE]` with the actual JSON
7. Paste the whole thing back to me in this IDE

---

## Web Search Prompt (Copy & Paste to ChatGPT)

```
Search the web for speaking engagements and events for "Dustin Thostenson" and "Delta3Consulting" from 2024-2026.

Check these sources:
- LinkedIn profiles
- Meetup.com event listings
- Sessionize.com speaker profiles
- Conference websites

Return ONLY valid JSON with no explanation:

{
  "source": "Combined Event Research",
  "search_date": "[TODAY'S DATE]",
  "events": [
    {
      "name": "[Event Name]",
      "date": "[YYYY-MM-DD]",
      "type": "[conference/meetup/webinar/workshop]",
      "topic": "[Brief description]",
      "dustin_role": "[speaker/panelist/organizer]",
      "url": "[Direct event URL]",
      "source_site": "[Where found: LinkedIn/Meetup/Sessionize/etc]",
      "notes": "[Any verification details]"
    }
  ]
}

If no new events found, return: { "events": [] }
```

---

## Return to Copilot (Copy & Paste Back Here)

Once you have the JSON from ChatGPT, paste this entire section back to me with the JSON data:

```
Create event markdown files for all these events in my blog's _events/ directory.

Event data:
[JSON DATA HERE]

For each event:
1. Create file: _events/YYYY-MM-DD-[event-name].md
2. Use this front matter structure:
   ---
   layout: post
   sidebar: left
   subheadline: [type: Conference/Meetup/Webinar/Workshop]
   title: "[event name]"
   teaser: "[2-sentence teaser]"
   breadcrumb: false
   tags:
       - presentation
       - [other relevant tags]
   categories:
       - community
       - presentation
   event_date: YYYY-MM-DD
   image:
       thumb: [event-name-placeholder].png
       title: [event-name-placeholder].png
       caption: "[Event name]"
       caption_url: [url from JSON]
   ---

3. Write 2-3 sentences describing the event in the body
4. Use past tense if passed, future tense if upcoming
5. Include the URL in caption_url

Output: List each file created with full path
```

---

## Quick Reference for This Workflow

**Step 1:** Copy web search prompt above → paste to ChatGPT → get JSON

**Step 2:** Copy "Return to Copilot" prompt above → replace `[JSON DATA HERE]` → paste back here

**That's it. Everything else is automated.**

---

## Time Estimate
- ChatGPT search: 5-10 min
- Copilot file creation: 2 min
- Local testing: 2 min
- Deploy: 1 min
- **Total: ~20 min**

---

## Example Usage

**In ChatGPT:**
```
[Paste the "Web Search Prompt" section above]
```

**ChatGPT returns JSON**

**Back in GitHub Copilot (this IDE), you paste:**
```
Create event markdown files for all these events in my blog's _events/ directory.

Event data:
{
  "source": "Combined Event Research",
  "search_date": "2026-06-15",
  "events": [
    {
      "name": "TechConf 2026",
      "date": "2026-09-15",
      "type": "conference",
      "topic": "Cloud Architecture",
      "dustin_role": "speaker",
      "url": "https://techconf.com",
      "source_site": "TechConf website",
      "notes": "Confirmed speaker"
    }
  ]
}

For each event:
[Rest of prompt as shown above]
```

---

## Do This Every:
- Monthly for ongoing event discovery
- When you find new speaking opportunities
- For conference season planning

**File:** Keep this file bookmarked in your repo. Copy prompts as needed.

