#!/usr/bin/env python3
"""
Pre-Deployment Link Checker for d3cblog.github.io

Crawls through all event pages and the main site to check for:
- Broken internal links (404s, timeouts)
- Missing images and resources
- Unreachable pages
- General site health before production deployment

Usage:
    python3 scripts/pre-deployment-check.py

Requirements:
    - Local Jekyll dev server running on http://localhost:4000
    - Python 3.6+
    - curl installed (usually pre-installed on macOS/Linux)

Exit Codes:
    0 = All checks passed, safe to deploy
    1 = Issues found, review before deploying
"""

import subprocess
import re
import sys
from collections import defaultdict


class LinkChecker:
    def __init__(self, base_url="http://localhost:4000", verbose=False):
        self.base_url = base_url
        self.verbose = verbose
        self.errors = defaultdict(list)
        self.warnings = defaultdict(list)
        self.passed_checks = []

    def curl_fetch(self, url, timeout=5, head_only=False):
        """Fetch a URL using curl and return (status_code, content)"""
        try:
            cmd = ["/usr/bin/curl", "-s"]
            if head_only:
                cmd.append("-o")
                cmd.append("/dev/null")
            else:
                pass
            cmd.extend(["-w", "%{http_code}"])
            cmd.append(url)

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            return "TIMEOUT"
        except Exception as e:
            return f"ERROR: {e}"

    def get_page_content(self, url):
        """Get full HTML content of a page"""
        try:
            result = subprocess.run(["/usr/bin/curl", "-s", url],
                                  capture_output=True, text=True, timeout=5)
            return result.stdout
        except Exception:
            return ""

    def extract_links(self, html):
        """Extract all href links from HTML"""
        return set(re.findall(r'href="([^"]*)"', html))

    def extract_resources(self, html):
        """Extract all resource URLs (src attributes) from HTML"""
        return set(re.findall(r'src="([^"]*)"', html))

    def should_check_link(self, link):
        """Determine if a link should be checked"""
        if not link:
            return False
        if link.startswith(('#', 'mailto:', 'javascript:', 'tel:', 'data:')):
            return False
        return True

    def check_url(self, url):
        """Check if a URL is accessible and return status code"""
        status = self.curl_fetch(url, head_only=True)
        return status

    def check_main_pages(self):
        """Check that main navigation pages load"""
        print("\n1. CHECKING MAIN PAGES...")
        print("-" * 70)

        main_pages = [
            ("/", "Homepage"),
            ("/events/", "Events Index"),
            ("/blog/", "Blog"),
            ("/videos/", "Videos"),
            ("/search/", "Search"),
        ]

        for path, name in main_pages:
            url = f"{self.base_url}{path}"
            status = self.check_url(url)
            if status == "200":
                print(f"✓ {name:25} ({path})")
                self.passed_checks.append(f"Main page: {name}")
            else:
                print(f"❌ {name:25} ({path}) - HTTP {status}")
                self.errors["main_pages"].append((name, path, status))

    def check_assets(self):
        """Check that CSS and JS assets are accessible"""
        print("\n2. CHECKING ASSETS...")
        print("-" * 70)

        assets = [
            ("/assets/css/styles_feeling_responsive.css", "CSS"),
            ("/assets/js/modernizr.min.js", "JavaScript"),
        ]

        for path, name in assets:
            url = f"{self.base_url}{path}"
            status = self.check_url(url)
            if status == "200":
                print(f"✓ {name}")
                self.passed_checks.append(f"Asset: {name}")
            else:
                print(f"❌ {name} - HTTP {status}")
                self.errors["assets"].append((name, path, status))

    def get_all_events(self):
        """Extract all event URLs from the events index page"""
        print("\n3. DISCOVERING EVENTS...")
        print("-" * 70)

        events_page_url = f"{self.base_url}/events/"
        content = self.get_page_content(events_page_url)

        # Extract event URLs (format: /events/YYYY-MM-DD-slug)
        events = sorted(set(re.findall(r'/events/\d{4}-\d{2}-\d{2}-[^/"]*', content)))

        print(f"Found {len(events)} events")
        self.passed_checks.append(f"Event discovery: {len(events)} events found")

        return events

    def check_event_pages(self, events):
        """Check that all event pages load"""
        print("\n4. CHECKING EVENT PAGE ACCESSIBILITY...")
        print("-" * 70)

        broken = 0
        working = 0

        for event_path in events:
            url = f"{self.base_url}{event_path}/"
            status = self.check_url(url)

            if status == "200":
                working += 1
            else:
                broken += 1
                self.errors["event_pages"].append((event_path, status))

        print(f"✓ {working}/{len(events)} event pages accessible")

        if broken > 0:
            print(f"❌ {broken} broken event pages found")
        else:
            self.passed_checks.append(f"Event pages: All {len(events)} accessible")

        return broken == 0

    def check_event_links(self, events):
        """Check for broken links within event pages"""
        print("\n5. CHECKING LINKS WITHIN EVENT PAGES...")
        print("-" * 70)

        broken_links = []

        for event_path in events:
            url = f"{self.base_url}{event_path}/"
            content = self.get_page_content(url)
            links = self.extract_links(content)

            for link in links:
                if not self.should_check_link(link):
                    continue
                if link.startswith("http"):
                    continue  # Skip external links

                full_url = f"{self.base_url}{link if link.startswith('/') else '/' + link}"
                status = self.check_url(full_url)

                if status not in ["200", "301", "302"]:
                    broken_links.append((event_path, link, status))

        if broken_links:
            print(f"❌ {len(broken_links)} broken links found")
            for event, link, status in broken_links[:5]:
                print(f"   {event}: {link} (HTTP {status})")
            self.errors["broken_links"] = broken_links
        else:
            print("✓ No broken links in event pages")
            self.passed_checks.append("Event links: All accessible")

        return len(broken_links) == 0

    def check_event_resources(self, events):
        """Check for broken images and resources within event pages"""
        print("\n6. CHECKING IMAGES AND RESOURCES...")
        print("-" * 70)

        broken_resources = []

        for event_path in events:
            url = f"{self.base_url}{event_path}/"
            content = self.get_page_content(url)
            resources = self.extract_resources(content)

            for src in resources:
                if not src or src.startswith("data:") or src.startswith("http"):
                    continue

                full_url = f"{self.base_url}{src if src.startswith('/') else '/' + src}"
                status = self.check_url(full_url)

                if status != "200":
                    broken_resources.append((event_path, src, status))

        if broken_resources:
            print(f"❌ {len(broken_resources)} broken resources found")
            for event, src, status in broken_resources[:5]:
                print(f"   {event}: {src} (HTTP {status})")
            self.errors["broken_resources"] = broken_resources
        else:
            print("✓ All resources accessible")
            self.passed_checks.append("Event resources: All accessible")

        return len(broken_resources) == 0

    def print_summary(self):
        """Print final summary and recommendations"""
        print("\n" + "=" * 70)
        print("PRE-DEPLOYMENT CHECK SUMMARY")
        print("=" * 70)

        print(f"\n✓ Passed Checks: {len(self.passed_checks)}")
        for check in self.passed_checks:
            print(f"  • {check}")

        total_errors = sum(len(v) for v in self.errors.values())

        if total_errors == 0:
            print("\n" + "=" * 70)
            print("✅ ALL CHECKS PASSED - READY FOR PRODUCTION")
            print("=" * 70)
            return 0
        else:
            print(f"\n❌ Issues Found: {total_errors}")
            for category, issues in self.errors.items():
                print(f"\n{category.upper()} ({len(issues)}):")
                for issue in issues[:3]:
                    print(f"  • {issue}")
                if len(issues) > 3:
                    print(f"  ... and {len(issues) - 3} more")

            print("\n" + "=" * 70)
            print("⚠️  ISSUES FOUND - DO NOT DEPLOY UNTIL FIXED")
            print("=" * 70)
            return 1

    def run(self):
        """Run all checks"""
        print("=" * 70)
        print("D3 BLOG PRE-DEPLOYMENT LINK CHECKER")
        print("=" * 70)
        print(f"\nChecking server at: {self.base_url}")

        try:
            # Test server connectivity
            status = self.check_url(self.base_url)
            if status != "200":
                print(f"\n❌ ERROR: Cannot reach {self.base_url}")
                print("Make sure the Jekyll dev server is running with: ./dev-serve.sh")
                return 1

            # Run all checks
            self.check_main_pages()
            self.check_assets()
            events = self.get_all_events()
            self.check_event_pages(events)
            self.check_event_links(events)
            self.check_event_resources(events)

            # Print summary and return appropriate exit code
            return self.print_summary()

        except KeyboardInterrupt:
            print("\n\n⏸️  Check interrupted by user")
            return 1
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            return 1


def main():
    """Entry point"""
    checker = LinkChecker(verbose=True)
    exit_code = checker.run()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

