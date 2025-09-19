#!/bin/bash

# Print an informative message
echo "Starting development server..."
echo "Link fixing enabled: Production links will be redirected to localhost"

# Clean any previous build to avoid cached production URLs
bundle exec jekyll clean

# Set environment to development explicitly
JEKYLL_ENV=development bundle exec jekyll serve --config _config.yml,_config_dev.yml "$@"

