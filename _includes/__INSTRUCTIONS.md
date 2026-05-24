# Includes

There are two types of includes...



## 1. includes for templates.

All includes with `_` are used for templates, like for example the `_head.html` or `_footer.html`.



## 2. includes as commands

Includes without an underscore are commands you can use in posts and pages. I left out the `.html`-ending to reduce the typing and though the commands look cleaner. They only look messy when you open them in your coding-editor of choice.

Checkout for example `alert`:

{% include alert success="Yay! you did it!" %}

or

{% include gallery %}

Enjoy :)


---

## Project-Specific Configuration Notes

### Events System (Hybrid Approach)
**IMPORTANT**: This project uses a HYBRID event storage pattern that differs from pure Jekyll standards:

- **NEW events** → Store in `_events/` folder as a Jekyll collection
  - Files follow naming convention: `YYYY-MM-DD-event-name.md`
  - These render with the `events` layout at `/events/:path/`
  
- **OLD events** → Legacy posts live in `_posts/` with the `community` category
  - These are blog posts that are displayed on the events page
  - Must have `categories: - community` in frontmatter

- **Display Logic** (`_includes/_event-pagination.html`):
  - The events page combines BOTH sources via: `site.events | concat: site.categories.community`
  - Results are sorted by date (newest first) and merged together
  - This ensures old events don't disappear when new events collection is added

**⚠️ KEY LEARNING**: When updating event display templates, always merge both data sources. Do NOT replace one with the other.
