#!/usr/bin/env python3
"""
Pre-Deployment Link Checker for d3cblog.github.io

Crawls through all event pages and the main site to check for:
- Broken internal links (404s, timeouts)
- Missing images and resources
- Unreachable pages
- External links (optional, with intelligent retry logic)
- General site health before production deployment

Usage:
    python3 scripts/pre-deployment-check.py                     # Internal links only
    python3 scripts/pre-deployment-check.py --check-external    # Include external links
    python3 scripts/pre-deployment-check.py --html report.html  # Write HTML report

Options:
    --check-external    Enable checking of external links (slower, optional)
    --verbose           Show detailed output
    --html              Write results to an HTML report file

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
import argparse
from html import escape
import time
from collections import defaultdict
from datetime import datetime
from urllib.parse import urlparse


# Whitelist of domains that block automated checks or are unreliable
EXTERNAL_LINK_WHITELIST = {
    'linkedin.com': 'Blocks bot requests',
    'twitter.com': 'Requires authentication',
    'x.com': 'Requires authentication',
    'facebook.com': 'Requires authentication',
    'instagram.com': 'Requires authentication',
    'youtube.com': 'May block bot requests',
    'github.com': 'High request rate limits',
    'amazon.com': 'May block bot requests',
}


class LinkChecker:
    def __init__(self, base_url="http://localhost:4000", verbose=False, check_external=False, html_report=None):
        self.base_url = base_url
        self.verbose = verbose
        self.check_external = check_external
        self.html_report = html_report
        self.errors = defaultdict(list)
        self.warnings = defaultdict(list)
        self.passed_checks = []
        self.external_link_stats = {'total': 0, 'passed': 0, 'skipped': 0, 'warning': 0, 'failed': 0}
        self.check_timings = []
        self.start_time = None
        self.end_time = None

    def curl_fetch(self, url, timeout=5, head_only=False):
        """Fetch a URL using curl and return (status_code, content)"""
        try:
            cmd = ["/usr/bin/curl", "-s"]
            if head_only:
                cmd.append("-I")
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

    def check_external_link_with_retry(self, url, max_retries=2):
        """
        Check external URL with retry logic.
        Returns status_code
        Implements exponential backoff: 1s, 3s, 5s
        """
        backoff_times = [1, 3, 5]

        for attempt in range(max_retries + 1):
            status = self.curl_fetch(url, timeout=10, head_only=True)

            # Success - return status
            if status in ["200", "301", "302", "303"]:
                return status

            # Server errors that warrant retry
            if status in ["TIMEOUT", "500", "502", "503", "504"]:
                if attempt < max_retries:
                    wait_time = backoff_times[attempt]
                    if self.verbose:
                        print(f"       ↻ Retry in {wait_time}s (attempt {attempt+1}/{max_retries}) - {url}")
                    time.sleep(wait_time)
                    continue

            # Final attempt - return status
            return status

    def is_external_link(self, url):
        """Check if URL is external (http/https)"""
        return url.startswith('http://') or url.startswith('https://')

    def is_whitelisted_domain(self, url):
        """Check if URL domain is in the whitelist"""
        try:
            domain = urlparse(url).hostname
            if not domain:
                return False
            domain = domain.lower()
            if domain.startswith('www.'):
                domain = domain[4:]
            return any(
                domain == whitelisted_domain or domain.endswith(f".{whitelisted_domain}")
                for whitelisted_domain in EXTERNAL_LINK_WHITELIST
            )
        except Exception:
            return False

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
        check_start = time.time()
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

        check_duration = time.time() - check_start
        self._track_timing("Main Pages Check", check_duration)

    def check_assets(self):
        """Check that CSS and JS assets are accessible"""
        check_start = time.time()
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

        check_duration = time.time() - check_start
        self._track_timing("Assets Check", check_duration)

    def get_all_events(self):
        """Extract all event URLs from the events index page"""
        check_start = time.time()
        print("\n3. DISCOVERING EVENTS...")
        print("-" * 70)

        events_page_url = f"{self.base_url}/events/"
        content = self.get_page_content(events_page_url)

        # Extract event URLs (format: /events/YYYY-MM-DD-slug)
        events = sorted(set(re.findall(r'/events/\d{4}-\d{2}-\d{2}-[^/"]*', content)))

        print(f"Found {len(events)} events")
        self.passed_checks.append(f"Event discovery: {len(events)} events found")

        check_duration = time.time() - check_start
        self._track_timing("Event Discovery", check_duration)

        return events

    def check_event_pages(self, events):
        """Check that all event pages load"""
        check_start = time.time()
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

        check_duration = time.time() - check_start
        self._track_timing("Event Pages Check", check_duration)

        return broken == 0

    def check_event_links(self, events):
        """Check for broken links within event pages"""
        check_start = time.time()
        print("\n5. CHECKING LINKS WITHIN EVENT PAGES...")
        print("-" * 70)

        broken_links = []
        external_links = []

        for event_path in events:
            url = f"{self.base_url}{event_path}/"
            content = self.get_page_content(url)
            links = self.extract_links(content)

            for link in links:
                if not self.should_check_link(link):
                    continue

                # External links - collect for optional checking
                if self.is_external_link(link):
                    if self.check_external:
                        external_links.append(link)
                    continue

                full_url = f"{self.base_url}{link if link.startswith('/') else '/' + link}"
                status = self.check_url(full_url)

                if status not in ["200", "301", "302"]:
                    broken_links.append((event_path, link, status))

        if broken_links:
            print(f"❌ {len(broken_links)} broken internal links found")
            for event, link, status in broken_links[:5]:
                print(f"   {event}: {link} (HTTP {status})")
            self.errors["broken_links"] = broken_links
        else:
            print("✓ No broken internal links in event pages")
            self.passed_checks.append("Event links: All accessible")

        # Check external links if enabled
        if self.check_external and external_links:
            self.check_external_links(external_links)

        check_duration = time.time() - check_start
        self._track_timing("Event Links Check", check_duration)

        return len(broken_links) == 0

    def check_event_resources(self, events):
        """Check for broken images and resources within event pages"""
        check_start = time.time()
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

        check_duration = time.time() - check_start
        self._track_timing("Event Resources Check", check_duration)

        return len(broken_resources) == 0

    def check_external_links(self, links):
        """Check external links with retry logic and whitelisting"""
        print("\n7. CHECKING EXTERNAL LINKS (with retry logic)...")
        print("-" * 70)

        unique_links = set(links)
        failed_links = []

        for link in sorted(unique_links):
            self.external_link_stats['total'] += 1

            # Check whitelist
            if self.is_whitelisted_domain(link):
                self.external_link_stats['skipped'] += 1
                if self.verbose:
                    print(f"  ⊘ {link[:60]} (whitelisted)")
                continue

            # Check with retry
            status = self.check_external_link_with_retry(link)

            if status == "200" or status in ["301", "302", "303"]:
                self.external_link_stats['passed'] += 1
                if self.verbose:
                    print(f"  ✓ {link[:60]} ({status})")
            elif status in ["TIMEOUT", "500", "502", "503", "504"]:
                self.external_link_stats['warning'] += 1
                self.warnings["external_links"].append((link, status))
                if self.verbose:
                    print(f"  ⚠ {link[:60]} ({status}) - May be transient")
            else:
                self.external_link_stats['failed'] += 1
                failed_links.append((link, status))
                if self.verbose:
                    print(f"  ✗ {link[:60]} ({status})")

        # Report external link summary
        print(f"\nExternal Links Summary:")
        print(f"  Total: {self.external_link_stats['total']}")
        print(f"  ✓ Passed: {self.external_link_stats['passed']}")
        print(f"  ⊘ Skipped (whitelisted): {self.external_link_stats['skipped']}")
        print(f"  ⚠ Warnings (transient): {self.external_link_stats['warning']}")
        print(f"  ✗ Failed: {self.external_link_stats['failed']}")

        if failed_links:
            self.errors["external_links"] = failed_links
            print(f"\n⚠️  {len(failed_links)} external links failed checks")
        else:
            if self.external_link_stats['warning'] > 0:
                print(
                    f"⚠ External links checked with {self.external_link_stats['warning']} transient "
                    f"warning(s); no hard failures detected"
                )
            else:
                print("✓ All external links accessible (or safely whitelisted)")
                if self.external_link_stats['total'] > 0:
                    self.passed_checks.append(
                        f"External links: All {self.external_link_stats['passed']} passed"
                    )

    def _track_timing(self, check_name, duration):
        """Track timing for a check"""
        self.check_timings.append({
            "name": check_name,
            "duration": duration
        })

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

    def generate_html_report(self):
        """Generate HTML report and save to file"""
        if not self.html_report:
            return

        total_errors = sum(len(v) for v in self.errors.values())
        status_color = "#22c55e" if total_errors == 0 else "#ef4444"
        status_text = "✅ ALL CHECKS PASSED" if total_errors == 0 else "❌ ISSUES FOUND"

        # Calculate total time
        total_time = self.end_time - self.start_time

        # Build HTML content
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pre-Deployment Check Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Arial', sans-serif;
            background: #f3f4f6;
            color: #1f2937;
            padding: 20px;
        }}

        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            overflow: hidden;
        }}

        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 20px;
            text-align: center;
        }}

        .header h1 {{
            font-size: 28px;
            margin-bottom: 10px;
        }}

        .header p {{
            opacity: 0.9;
            font-size: 14px;
        }}

        .summary-cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px 20px;
            background: #f9fafb;
            border-bottom: 1px solid #e5e7eb;
        }}

        .card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #3b82f6;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }}

        .card.success {{
            border-left-color: #22c55e;
        }}

        .card.danger {{
            border-left-color: #ef4444;
        }}

        .card.warning {{
            border-left-color: #f59e0b;
        }}

        .card-number {{
            font-size: 32px;
            font-weight: bold;
            color: {status_color};
            margin-bottom: 5px;
        }}

        .card-label {{
            font-size: 14px;
            color: #6b7280;
        }}

        .status-banner {{
            padding: 20px;
            background: {status_color};
            color: white;
            text-align: center;
            font-size: 18px;
            font-weight: 600;
        }}

        .content {{
            padding: 30px 20px;
        }}

        .section {{
            margin-bottom: 30px;
        }}

        .section h2 {{
            font-size: 20px;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid #e5e7eb;
            color: #111827;
        }}

        .check-item {{
            padding: 10px 0;
            border-bottom: 1px solid #f3f4f6;
            font-size: 14px;
        }}

        .check-item:last-child {{
            border-bottom: none;
        }}

        .check-passed {{
            color: #22c55e;
        }}

        .check-failed {{
            color: #ef4444;
        }}

        .check-warning {{
            color: #f59e0b;
        }}

        .timing {{
            color: #6b7280;
            font-size: 12px;
            margin-left: auto;
        }}

        .error-list {{
            background: #fef2f2;
            border: 1px solid #fecaca;
            border-radius: 6px;
            padding: 15px;
            margin-top: 10px;
        }}

        .error-item {{
            padding: 8px;
            margin: 5px 0;
            background: white;
            border-left: 3px solid #ef4444;
            border-radius: 3px;
            font-size: 13px;
            font-family: 'Courier New', monospace;
        }}

        .footer {{
            padding: 20px;
            background: #f9fafb;
            border-top: 1px solid #e5e7eb;
            text-align: center;
            font-size: 12px;
            color: #6b7280;
        }}

        .metadata {{
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 15px;
            font-size: 13px;
            color: #6b7280;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔍 Pre-Deployment Check Report</h1>
            <p>D3 Blog Site Health Verification</p>
        </div>

        <div class="status-banner">
            {status_text}
        </div>

        <div class="summary-cards">
            <div class="card success">
                <div class="card-number">{len(self.passed_checks)}</div>
                <div class="card-label">Checks Passed</div>
            </div>
            <div class="card {'danger' if total_errors > 0 else 'success'}">
                <div class="card-number">{total_errors}</div>
                <div class="card-label">Issues Found</div>
            </div>
            <div class="card">
                <div class="card-number">{total_time:.1f}s</div>
                <div class="card-label">Execution Time</div>
            </div>
            <div class="card">
                <div class="card-number">{datetime.now().strftime('%H:%M:%S')}</div>
                <div class="card-label">Generated At</div>
            </div>
        </div>

        <div class="content">
            <div class="metadata">
                <div><strong>Repository:</strong> d3cblog.github.io</div>
                <div><strong>Server:</strong> {self.base_url}</div>
                <div><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
            </div>

            <div class="section">
                <h2>✅ Passed Checks ({len(self.passed_checks)})</h2>
                <div>
                    {self._render_passed_checks()}
                </div>
            </div>
"""

        # Add error section if there are errors
        if total_errors > 0:
            html += """
            <div class="section">
                <h2>❌ Issues Found</h2>
"""
            for category, issues in self.errors.items():
                html += f"""                <div style="margin-bottom: 20px;">
                    <h3 style="font-size: 16px; margin-bottom: 10px; color: #dc2626;">{category.replace('_', ' ').title()} ({len(issues)})</h3>
                    <div class="error-list">
"""
                for issue in issues[:10]:
                    if isinstance(issue, tuple):
                        issue_text = " → ".join(str(i) for i in issue)
                    else:
                        issue_text = str(issue)
                    html += f'                        <div class="error-item">{escape(issue_text)}</div>\n'

                if len(issues) > 10:
                    html += f'                        <div class="error-item" style="color: #9ca3af;">... and {len(issues) - 10} more</div>\n'

                html += """                    </div>
                </div>
"""
            html += """            </div>
"""

        # Add warnings section if there are warnings
        if any(self.warnings.values()):
            html += f"""            <div class="section">
                <h2>⚠️ Warnings</h2>
                {self._render_warnings()}
            </div>
"""

        # Add timing details
        html += f"""            <div class="section">
                <h2>⏱️ Timing Details</h2>
                <div>
                    <div class="check-item">
                        <strong>Total Execution Time:</strong> {total_time:.2f} seconds
                    </div>
"""
        for timing in self.check_timings:
            html += f'                    <div class="check-item">{timing["name"]}: {timing["duration"]:.2f}s</div>\n'

        html += """                </div>
            </div>
        </div>

        <div class="footer">
            <p>Report generated by D3 Blog Pre-Deployment Check Tool</p>
            <p>For more information, see QUICK_START_DEPLOYMENT.md</p>
        </div>
    </div>
</body>
</html>
"""

        # Write to file
        try:
            with open(self.html_report, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"\n📊 HTML report saved to: {self.html_report}")
        except Exception as e:
            print(f"\n⚠️  Could not save HTML report: {e}")

    def _render_passed_checks(self):
        """Render passed checks as HTML"""
        html = ""
        for check in self.passed_checks:
            html += f'<div class="check-item"><span class="check-passed">✓</span> {escape(str(check))}</div>\n'
        return html

    def _render_warnings(self):
        """Render warnings as HTML"""
        html = '<div>'
        for category, warns in self.warnings.items():
            if warns:
                html += f'<div style="margin-bottom: 15px;">\n'
                html += f'    <h3 style="font-size: 14px; color: #b45309; margin-bottom: 8px;">{category.replace("_", " ").title()}</h3>\n'
                for warn in warns[:5]:
                    if isinstance(warn, tuple):
                        warn_text = " → ".join(str(w) for w in warn)
                    else:
                        warn_text = str(warn)
                    html += f'    <div class="check-item"><span class="check-warning">⚠</span> {escape(warn_text)}</div>\n'
                if len(warns) > 5:
                    html += f'    <div class="check-item" style="color: #9ca3af;">... and {len(warns) - 5} more</div>\n'
                html += '</div>\n'
        html += '</div>'
        return html

    def run(self):
        """Run all checks"""
        self.start_time = time.time()

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

            # Record end time
            self.end_time = time.time()

            # Generate HTML report if requested
            if self.html_report:
                self.generate_html_report()

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
    parser = argparse.ArgumentParser(
        description='Pre-deployment link checker for d3cblog.github.io',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s                           # Check internal links only (fast)
  %(prog)s --check-external          # Check both internal and external links (slower)
  %(prog)s --verbose                 # Show detailed output
  %(prog)s --html report.html        # Generate HTML report
  %(prog)s --check-external --html report.html  # Both external checks and HTML report
        '''
    )
    parser.add_argument('--check-external', action='store_true',
                       help='Enable checking of external links (slower, optional)')
    parser.add_argument('--verbose', action='store_true',
                       help='Show detailed output for each check')
    parser.add_argument('--html', metavar='FILE',
                       help='Generate HTML report and save to FILE')

    args = parser.parse_args()

    checker = LinkChecker(verbose=args.verbose, check_external=args.check_external, html_report=args.html)
    exit_code = checker.run()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
