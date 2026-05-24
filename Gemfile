source 'https://rubygems.org'

# Requires Ruby 3.2+ for full security patches
gem 'github-pages', group: :jekyll_plugins
gem 'webrick'

# Security updates for vulnerable gems
# Ruby 3.2+ allows us to fix nokogiri and newer activesupport versions
gem 'activesupport', '>= 7.2.3.1'
gem 'addressable', '>= 2.9.0'
gem 'faraday', '>= 2.14.1'
gem 'nokogiri', '>= 1.19.1'
gem 'rexml', '>= 3.4.2'

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






