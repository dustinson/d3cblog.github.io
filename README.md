# d3cBlog
 Delta3Consulting Blog

## Quick Start

Launch the blog locally with a single command:

```bash
./run-blog
```

This will start the dev server and automatically open the site in your browser at `http://localhost:4000`.

Alternatively, use the convenient Makefile:

```bash
make dev    # Opens in browser automatically
make serve  # Just start the server
make help   # View all available commands
```

## Development

Use one of these commands to start the development server manually:

```bash
# Using ./run-blog (fastest)
./run-blog

# Using Makefile (recommended)
make dev
make serve

# Using bundle directly
./serve.sh
./dev-serve.sh
```

### Development Mode Features

When running in development mode:
- A banner will appear showing you're in development mode
- All links to delta3consulting.com will be automatically redirected to localhost:4000
- CSS, JavaScript, and image references will also be fixed

## Convenient Commands

The `Makefile` provides convenient commands for common tasks:

```bash
make dev         # Start dev server (opens in browser)
make build       # Build production version
make audit       # Check security vulnerabilities  
make check       # Run all pre-deploy checks
make deploy      # Push to production
make help        # View all commands
```

For detailed command reference, see section "Available Commands" in `DEVELOPMENT.md`.

## Detailed Documentation

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

## Documentation

Complete documentation for development, deployment, and troubleshooting:

- **[DEVELOPMENT.md](DEVELOPMENT.md)** - Full development guide including setup, workflow, and commands
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Solutions for common issues
- **[DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)** - Pre-deployment verification steps
- **[Makefile](Makefile)** - Quick reference for all available commands
- **[PHASE_1_SUMMARY.md](PHASE_1_SUMMARY.md)** - Stabilization status and next steps

## Setup for Contributors

New contributors should run:

```bash
./scripts/setup-dev-env.sh
```

This installs dependencies and sets up optional git hooks for automatic pre-push checks.

