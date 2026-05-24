# Event Research Prompts for Web-Capable AI

Use these prompts with ChatGPT, Claude.ai, or Perplexity to gather event data. Format the output as specified so it can be easily processed into blog events.

---

## Prompt 1: LinkedIn Search for Dustin Thostenson

```
Search LinkedIn for "Dustin Thostenson" and "Delta3Consulting"

Find and return ONLY speaking engagements, conferences, presentations, and events.

Format results EXACTLY as JSON:
{
  "source": "LinkedIn",
  "search_date": "[TODAY'S DATE]",
  "events": [
    {
      "name": "[Event Name]",
      "date": "[YYYY-MM-DD or 'TBD' if unknown]",
      "type": "[presentation/conference/panel/workshop/webinar]",
      "dustin_role": "[speaker/panelist/attendee/organizer]",
      "topic": "[Brief description of topic]",
      "company": "[Organizing company if applicable]",
      "url": "[Direct LinkedIn URL if available]",
      "notes": "[Any additional context]"
    }
  ]
}

Return empty array [] if no events found. Include only verified/confirmed events, not speculative ones.
```

---

## Prompt 2: Meetup.com Search

```
Search Meetup.com for:
1. "Dustin Thostenson" in speaker bios
2. Events organized by or featuring "Delta3Consulting"
3. Meetup groups where Dustin Thostenson has spoken or organized

Find ONLY past and upcoming events (not general group memberships).

Format results EXACTLY as JSON:
{
  "source": "Meetup",
  "search_date": "[TODAY'S DATE]",
  "events": [
    {
      "name": "[Event/Meetup Group Name]",
      "date": "[YYYY-MM-DD]",
      "type": "[meetup/conference/webinar]",
      "dustin_role": "[speaker/organizer/attendee]",
      "topic": "[What the talk/event was about]",
      "location": "[City, State or Virtual]",
      "url": "[Meetup.com event URL]",
      "notes": "[Any additional details]"
    }
  ]
}

Return empty array [] if no events found.
```

---

## Prompt 3: Sessionize.com Search

```
Search Sessionize.com for:
1. Speaking profiles for "Dustin Thostenson"
2. Events/conferences where Delta3Consulting is listed
3. Any sessions given by Dustin Thostenson on Sessionize

Return past and upcoming speaking engagements.

Format results EXACTLY as JSON:
{
  "source": "Sessionize",
  "search_date": "[TODAY'S DATE]",
  "events": [
    {
      "name": "[Sessionize Event/Conference Name]",
      "date": "[YYYY-MM-DD]",
      "type": "[conference/summit/workshop]",
      "session_title": "[Title of Dustin's talk]",
      "topic": "[Brief description]",
      "dustin_role": "[speaker]",
      "url": "[Direct Sessionize event URL]",
      "notes": "[Any additional context]"
    }
  ]
}

Return empty array [] if no events found.
```

---

## Prompt 4: General Web Search (Fallback)

```
Search the web broadly for:
1. "Dustin Thostenson" speaking engagements, presentations, conferences
2. "Delta3Consulting" events, webinars, workshops
3. Any podcasts, interviews, or panel discussions featuring Dustin Thostenson

Look for events from 2024-2026.

Format results EXACTLY as JSON:
{
  "source": "Web Search",
  "search_date": "[TODAY'S DATE]",
  "events": [
    {
      "name": "[Event Name]",
      "date": "[YYYY-MM-DD or 'TBD']",
      "type": "[conference/podcast/webinar/presentation/panel]",
      "topic": "[Topic or description]",
      "dustin_role": "[speaker/guest/panelist]",
      "url": "[URL to event or announcement]",
      "source_site": "[Where you found it: LinkedIn/Twitter/Company site/etc]",
      "notes": "[Any details that help verify legitimacy]"
    }
  ]
}

Return empty array [] if no relevant events found.
```

---

## How to Use

1. **Run each search independently** (or combine into one conversation)
2. **Copy the JSON output** from the AI response
3. **Paste it back to GitHub Copilot** with this prompt:

```
I've gathered event data for Dustin Thostenson and Delta3Consulting. 
Please create event files for each in my blog's _events/ directory.
Use this data:

[PASTE JSON HERE]

For each event:
- Create a markdown file: _events/YYYY-MM-DD-[event-name].md
- Use the existing format from _events/IowaCodeCamp-TechDebt.md as template
- Fill in title, teaser, description, date
- Mark as past or upcoming appropriately
- Leave image placeholder if not available (I'll add manually)

Return a summary of files created.
```

---

## Data Validation Checklist

When returning results, ensure:
- [ ] All dates are in YYYY-MM-DD format (or marked "TBD")
- [ ] Role is accurately captured (speaker, panelist, organizer, etc.)
- [ ] URLs are direct links to the event/profile (not generic sites)
- [ ] Duplicates are removed (same event from multiple sources)
- [ ] Only verified events included (not speculation)
- [ ] JSON is valid (use JSONLint if unsure)

---

## Future Queries

For ongoing event discovery, you can:
1. Run these searches **monthly** to catch new events
2. Combine all results into one JSON array
3. Paste back to GitHub Copilot with update request
4. Copilot creates/updates event files automatically

This creates a **fully automated pipeline**:
```
You → GPT (web search) → JSON → Copilot (blog automation) → Live blog
```

---

## Notes

- Keep responses in **pure JSON** (no markdown wrappers, no explanations)
- If AI returns explanatory text, ask it to "Return ONLY valid JSON"
- Test one search first before running all four prompts
- Save successful searches for future reference

