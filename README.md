# d3cBlog
 Delta3Consulting Blog

## Quick Start

Launch the blog locally with a single command:

```bash
./run-blog
```

This will start the dev server and automatically open the site in your browser at `http://localhost:4000`.

## Development

Use one of these commands to start the development server manually:

```bash
# Standard development server
./serve.sh

# Development server with debugging
./dev-serve.sh

# One-command launch (opens in browser)
./run-blog
```

### Development Mode Features

When running in development mode:
- A banner will appear showing you're in development mode
- All links to delta3consulting.com will be automatically redirected to localhost:4000
- CSS, JavaScript, and image references will also be fixed

## Production

For production builds:

```bash
JEKYLL_ENV=production bundle exec jekyll build
```

### Deployment to GitHub Pages

The site is automatically deployed to GitHub Pages via GitHub Actions on every push to `main`. The workflow:

1. Runs on Ubuntu with Ruby 3.3
2. Installs dependencies via bundler
3. Builds the site in production mode
4. Deploys to GitHub Pages

**To deploy:** Simply push to the `main` branch:

```bash
git add .
git commit -m "Your message"
git push origin main
```

The deployment will appear at https://delta3consulting.com within a few minutes.

### Before Deploying

Run these checks locally:

```bash
# Run security audit
bundle audit

# Run production build
JEKYLL_ENV=production bundle exec jekyll build --verbose

# Smoke test in browser
./run-blog

# Visit http://localhost:4000 and verify:
# - Homepage loads correctly
# - Navigation links work
# - Blog page lists recent posts
# - Events page displays events  
# - Contact page is accessible
# - Footer appears on all pages
```

See **TROUBLESHOOTING.md** for common issues and solutions.

