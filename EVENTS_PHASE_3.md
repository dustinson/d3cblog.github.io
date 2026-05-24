# Upcoming Events - Phase 3 Task List

**Blocked:** Until Phase 1 (stabilization) is complete.

---

## Event 1: PMI Agile 2026 Review Team (Archive Event)

**Date:** April 15, 2026 (Past)  
**Status:** ⏳ To be added for archive  
**Template Ready:** ✅

```markdown
---
layout: post
sidebar: left
subheadline: Review Session
title: "PMI Agile 2026 - Review Team"
teaser: "Delta3Consulting participated in the PMI Agile 2026 Review Team"
breadcrumb: false
tags:
    - agile
    - pmi
    - community
categories:
    - community
event_date: 2026-04-15
image:
    thumb: pmi-agile-logo.png
    title: pmi-agile-logo.png
    caption: "PMI Agile 2026"
    caption_url: https://www.pmi.org/
---

Details about the PMI Agile 2026 review team involvement.
```

**Action Items:**
- [ ] Get event image/logo
- [ ] Write event description (2-3 sentences)
- [ ] Create `_events/2026-04-15-PMI-Agile-Review-Team.md`
- [ ] Build and verify it appears on /events page
- [ ] Commit and push

---

## Event 2: "The Past Didn't Go Anywhere" Presentation (LIVE UPCOMING)

**Date:** July 25, 2026 (Upcoming — 2 months away)  
**Status:** 🔴 Priority — add ASAP for early promotion  
**Template Ready:** ⏳ Awaiting details

```markdown
---
layout: post
sidebar: left
subheadline: Presentation
title: "The Past Didn't Go Anywhere"
teaser: "[Add short teaser here - what is this talk about?]"
breadcrumb: false
tags:
    - presentation
    - [relevant-tag]
categories:
    - community
    - presentation
event_date: 2026-07-25
image:
    thumb: [event-image].png
    title: [event-image].png
    caption: "[Event name]"
    caption_url: [external-url-to-event]
---

[Add full event description, key points, and call-to-action]
```

**Action Items:**
- [ ] Get event image/promotional material
- [ ] Write teaser (1-2 sentences about the talk)
- [ ] Write full description (3-5 sentences)
- [ ] Get external link (Eventbrite, speaker site, etc.)
- [ ] Create `_events/2026-07-25-The-Past-Didn't-Go-Anywhere.md`
- [ ] Build and verify on /events page
- [ ] Cross-promote (blog post? social media?)
- [ ] Commit and push
- [ ] ⚠️ **Set reminder:** 2 weeks before (7/11/26) — boost promotion

---

## Events 3-6: TBD

**Status:** 📋 Awaiting details  
**Template:** Same as above — just fill in the details

```markdown
---
layout: post
sidebar: left
subheadline: Presentation / Session / Workshop
title: "[Event Name]"
teaser: "[Short description]"
breadcrumb: false
tags:
    - [relevant-tags]
categories:
    - community
    - presentation
event_date: YYYY-MM-DD
image:
    thumb: [image].png
    title: [image].png
    caption: "[Caption]"
    caption_url: [external-url]
---

[Event description]
```

**For each remaining event, provide:**
- Name
- Date (YYYY-MM-DD)
- Teaser (1-2 sentences)
- Full description
- Image file (or provide image to add)
- External link if applicable

---

## How to Add Events

**Copilot prompt:**

```
"Add a new event to _events/ for [Event Name] on [Date].
- Title: [title]
- Teaser: [teaser]
- Description: [description]
- Event date: [YYYY-MM-DD]
- Image: [image-filename]
- External link: [url]
Keep the front matter consistent with existing events in _events/."
```

**Manual verification:**
```bash
# 1. Build locally
./run-blog

# 2. Navigate to http://localhost:4000/events/
# 3. Verify event appears in list
# 4. Click event and verify all details render
# 5. Check footer on event page
```

---

## Success Criteria for Phase 3

Phase 3 is ✅ DONE when:
1. ✅ PMI Agile 2026 Review Team event is published and live
2. ✅ "The Past Didn't Go Anywhere" event is published and live with external link
3. ✅ All 6 events display on /events page
4. ✅ All events render correctly with images and links
5. ✅ Footer appears on all event detail pages
6. ✅ Committed and pushed to production

**Then:** Blog is ready for ongoing event additions and Copilot can help with content creation.

