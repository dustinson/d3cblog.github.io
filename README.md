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
