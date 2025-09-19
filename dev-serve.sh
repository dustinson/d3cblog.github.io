#!/bin/bash

echo "=== DEVELOPMENT SERVER WITH DEBUGGING ==="
echo "Link fixing enabled: Production links will be redirected to localhost"

# Clean any previous build to avoid cached production URLs
bundle exec jekyll clean

# Set environment to development explicitly with verbose output
JEKYLL_ENV=development bundle exec jekyll serve \
  --config _config.yml,_config_dev.yml \
  --verbose \
  --livereload \
  "$@"
