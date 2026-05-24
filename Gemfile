source 'https://rubygems.org'

# Requires Ruby 3.2+ for full security patches (set in GitHub Actions)
# Local dev on 3.1.2 will build but won't fix all vulnerabilities--
# Production builds via GitHub Actions (Ruby 3.3) will have all security patches
gem 'github-pages', group: :jekyll_plugins
gem 'webrick'

# Security updates - compatible with Ruby 3.1.2 locally, but GitHub Actions will use Ruby 3.3
gem 'activesupport', '>= 7.1.5.2'  # Can upgrade to 7.2+ on Ruby 3.2+
gem 'addressable', '>= 2.9.0'      # ReDoS vulnerability fixed
gem 'faraday', '>= 2.14.1'         # SSRF vulnerability fixed
gem 'rexml', '>= 3.4.2'            # DoS vulnerability fixed
# nokogiri stays at 1.18.9 (requires 1.19.1+, but that needs Ruby 3.2+)

group :jekyll_plugins do
  gem 'jekyll-gist'
  gem 'jekyll-paginate'
  gem "jekyll-asciidoc"
end

gem 'asciidoctor', '~> 1.5.4'
gem 'coderay', '1.1.1'
gem 'faraday-retry'

# Remove explicit dependency on commonmarker, kramdown-parser-gfm, and rdiscount
# to let github-pages gem dictate the appropriate versions






