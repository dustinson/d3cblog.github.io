#!/bin/bash
#
# Setup Development Environment
#
# This script installs optional development tools and git hooks.
# Run after cloning the repo:
#
#   ./scripts/setup-dev-env.sh
#

set -e

echo "🔧 Setting up d3cblog development environment..."
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

# 1. Bundle install
echo -e "${BLUE}1. Installing Ruby dependencies...${NC}"
bundle install
echo -e "${GREEN}✓ Dependencies installed${NC}"
echo ""

# 2. Git hooks
echo -e "${BLUE}2. Setting up git hooks...${NC}"

# Create hooks directory if needed
mkdir -p .git/hooks

# Copy pre-push hook
if [ -f "scripts/pre-push" ]; then
    cp scripts/pre-push .git/hooks/pre-push
    chmod +x .git/hooks/pre-push
    echo -e "${GREEN}✓ Pre-push hook installed${NC}"
    echo "  (Runs security audit and build test before pushing)"
else
    echo "  ⚠ scripts/pre-push not found"
fi

echo ""

# 3. Verify setup
echo -e "${BLUE}3. Verifying setup...${NC}"
ruby -v | sed 's/^/  /'
bundle exec jekyll --version | sed 's/^/  /'
echo -e "${GREEN}✓ Verification complete${NC}"
echo ""

# 4. Next steps
echo "🎉 Development environment ready!"
echo ""
echo "Next steps:"
echo "  1. Start dev server:    make dev"
echo "  2. Build for prod:      make build"
echo "  3. Run checks:          make check"
echo "  4. View all commands:   make help"
echo ""
echo "Git hooks installed:"
echo "  • pre-push: Runs security audit and build test before push"
echo ""
echo "To disable any hook temporarily:"
echo "  git push --no-verify origin main"

