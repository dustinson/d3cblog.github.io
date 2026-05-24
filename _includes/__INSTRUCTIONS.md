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

### Events System
All events live in the `_events/` folder as a Jekyll collection.

- **All events** → Store in `_events/` folder
  - Files follow naming convention: `YYYY-MM-DD-event-name.md`
  - These render with the `post` layout at `/events/:path/`
  - Keep `categories: - community` in frontmatter (used by the back-button in `post.html`)

- **Display Logic** (`_includes/_event-pagination.html`):
  - Uses `site.events | sort: "date" | reverse`

**Note:** Legacy static HTML exists under `community/` at the repo root. These are orphaned files left for continuity of old bookmarked URLs. They are not maintained and do not need to be updated.
