.PHONY: help install dev prod build clean audit check deploy serve

help:
	@echo "d3cblog Development Commands"
	@echo "============================"
	@echo ""
	@echo "Development:"
	@echo "  make dev              - Start dev server with auto-reload (http://localhost:4000)"
	@echo "  make serve            - Start dev server without browser launch"
	@echo ""
	@echo "Build & Testing:"
	@echo "  make build            - Build site for production"
	@echo "  make check            - Run pre-deployment checks (bundle audit, build test)"
	@echo "  make clean            - Clean _site and .jekyll-cache"
	@echo ""
	@echo "Security & Dependencies:"
	@echo "  make audit            - Check gems for security vulnerabilities"
	@echo "  make outdated         - Show outdated gems"
	@echo "  make update           - Update gems conservatively"
	@echo ""
	@echo "Deployment:"
	@echo "  make deploy           - Commit, push to production (requires clean git state)"
	@echo ""
	@echo "Info:"
	@echo "  make status           - Show Ruby, bundle, and build info"
	@echo "  make help             - Show this help message"

status:
	@echo "Environment Status"
	@echo "=================="
	@ruby -v
	@bundle --version
	@echo "Gems installed: $$(bundle list | wc -l)"
	@echo "Git status:"
	@git status --short
	@echo ""
	@echo "Build info:"
	@JEKYLL_ENV=production bundle exec jekyll build --verbose 2>&1 | tail -3

dev:
	@echo "Starting development server..."
	@./run-blog

serve:
	@echo "Starting development server (http://localhost:4000)..."
	@JEKYLL_ENV=development bundle exec jekyll serve --config _config.yml,_config_dev.yml

prod:
	@echo "Building production site..."
	@JEKYLL_ENV=production bundle exec jekyll build --verbose

build: clean prod
	@echo "✅ Production build complete"

clean:
	@echo "Cleaning build artifacts..."
	@rm -rf _site
	@rm -rf .jekyll-cache
	@rm -rf .jekyll-metadata
	@echo "✅ Clean complete"

audit:
	@echo "Running security audit..."
	@bundle audit

outdated:
	@echo "Checking for outdated gems..."
	@bundle outdated

update:
	@echo "Updating gems (conservative)..."
	@bundle update --conservative
	@echo "✅ Update complete - review Gemfile.lock before committing"

check: audit build
	@echo ""
	@echo "✅ All pre-deployment checks passed!"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Review changes:  git diff --cached"
	@echo "  2. Commit:          git add . && git commit -m 'Your message'"
	@echo "  3. Push:            git push origin main"
	@echo "  4. Verify:          https://github.com/dustinson/d3cblog.github.io/actions"

deploy:
	@if [ -z "$$(git status --short)" ]; then \
		echo "Deploying to production..."; \
		git push origin main; \
		echo ""; \
		echo "✅ Pushed to main - GitHub Actions will deploy in ~3-4 minutes"; \
		echo ""; \
		echo "Monitor deployment: https://github.com/dustinson/d3cblog.github.io/actions"; \
	else \
		echo "❌ Working directory not clean. Commit or discard changes first."; \
		git status; \
		exit 1; \
	fi

