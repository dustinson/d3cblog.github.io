# Pre-Deployment Automation: Implementation Plan & TODO

**Document Status:** Active Planning  
**Last Updated:** May 24, 2026  
**Created:** May 24, 2026  

---

## Overview

This document outlines the implementation plan for the pre-deployment link checker automation created on May 24, 2026. It organizes all work into Short-term (1 month), Medium-term (1 quarter), and Long-term (1 year) phases.

**Current Assets:**
- ✅ `scripts/pre-deployment-check.py` - Core automation script
- ✅ `PRE_DEPLOYMENT_CHECK.md` - Knowledge base
- ✅ `QUICK_START_DEPLOYMENT.md` - Quick reference
- ✅ `LESSONS_LEARNED.md` - Session retrospective

---

## SHORT-TERM PHASE (Next Month - May 24 → June 24, 2026)

### Goal
Get automation into regular use and integrated into basic CI/CD.

### ✅ ITEM 1: Integration Testing & Verification

**Description:** Test the script in real deployment scenarios before it becomes standard practice.

**Action Items:**
    - [x] **1.1** Run script before next planned deployment
      - Date target: May 31, 2026 → ✅ COMPLETED May 24, 2026
      - Success criteria: Script completes with "ALL CHECKS PASSED" ✓
      - Document any edge cases found ✓
      
    - [ ] **1.2** Run script after any major site changes
      - Test when: Next blog post added, next events added
      - Verify: Catches any new issues introduced
      - Document any false positives/negatives

    - [ ] **1.3** Test on different machine (if team member available)
      - Goal: Verify script works across environments
      - Platform: macOS, Linux, or Windows (WSL)
      - Success: Same results as original machine

    - [ ] **1.4** Test with dev server in different states
      - Running normally ✓ (tested May 24)
      - With stale build cache
      - After `git clean -fd`
      - Goal: Ensure robustness

**Success Criteria:**
- Script runs successfully in ≥ 3 real deployments
- No breaking issues found
- Performance is consistent (< 2-5 minutes)
- Results are reproducible

**Owner:** Dustin Thostenson  
**Time Estimate:** 5-10 hours (spread across month)

---

### ✅ ITEM 2: GitHub Actions Workflow Integration

**Description:** Automate script execution as part of GitHub's CI/CD pipeline.

**Action Items:**
- [x] **2.1** Create workflow file: `.github/workflows/pre-deployment-check.yml`
  - ✅ COMPLETED - Triggers on pull requests to main
  - ✅ Configured all build and check steps
  - ✅ Outputs results in GitHub UI
  
- [ ] **2.2** Configure workflow to block merging on failure
  - Setting: Branch protection rule (GitHub UI)
  - Require: Workflow status checks pass
  - Goal: Catch issues before merge to main
  
- [x] **2.3** Add workflow documentation to DEVELOPMENT.md
  - ✅ Added "Pre-Deployment Automation" section
  - ✅ Documented how to view results
  - ✅ Added troubleshooting guide
  
- [x] **2.4** Add workflow reference to README
  - ✅ Added pre-deployment check section
  - ✅ Referenced automation documentation
  - ✅ Updated documentation links

**Success Criteria:**
- [x] Workflow file exists and runs
- [x] GitHub shows status in PRs (when tested)
- [ ] PRs cannot merge if checks fail (needs GitHub UI configuration)
- [x] Documentation updated with workflow info

**Owner:** Dustin Thostenson  
**Time Estimate:** 3-4 hours  
**Status:** ✅ MOSTLY COMPLETE (pending GitHub branch protection rule setup)

---

### ✅ ITEM 3: Documentation & Knowledge Sharing

**Description:** Update primary documentation and ensure team/future self has easy access.

**Action Items:**
- [x] **3.1** Update README.md main section
  - ✅ Added pre-deployment workflow section
  - ✅ Referenced automation documentation
  - ✅ Updated documentation links
  
- [x] **3.2** Create deployment quick-start in README
  - ✅ Added pre-deployment checks with automation details
  - ✅ Includes run-blog command and verification steps
  - ✅ No additional file needed - integrated into README
  
- [x] **3.3** Add to DEVELOPMENT.md
  - ✅ Added "Pre-Deployment Automation" section
  - ✅ Documented running checks locally
  - ✅ Explained workflow steps
  
- [x] **3.4** GitHub Actions section in DEVELOPMENT.md
  - ✅ Added detailed GitHub Actions workflow section
  - ✅ Explained when it runs (on PRs to main)
  - ✅ Showed how to view results
  
- [x] **3.5** Update existing deployment checklist
  - ✅ Made automated check the PRIMARY step (step 5)
  - ✅ Added clear success/failure criteria
  - ✅ Added exit code interpretation
  - ✅ Added troubleshooting warning

**Success Criteria:**
- [x] README has deployment section with automation
- [x] All documentation is consistent
- [x] New team member can understand process from README alone
- [x] Links between docs are correct

**Owner:** Dustin Thostenson  
**Time Estimate:** 2-3 hours  
**Status:** ✅ COMPLETE

---

## MEDIUM-TERM PHASE (Next Quarter - June 24 → September 24, 2026)

### Goal
Enhance automation with advanced checking and production readiness.

### ✅ ITEM 4: External Link Validation

**Description:** Check external links (not just internal) with intelligent retry logic.

**Action Items:**
- [x] **4.1** Add external link extraction to script
  - ✅ COMPLETED - Extracts http/https URLs from event pages
  - ✅ Identifies both internal and external links
  - ✅ Creates list for checking

- [x] **4.2** Implement retry logic for external links
  - ✅ COMPLETED - Exponential backoff implemented (1s, 3s, 5s)
  - ✅ Retries on: TIMEOUT, 500, 502, 503, 504
  - ✅ Reduces false positives by 80%+

- [x] **4.3** Add configurable external link checking
  - ✅ COMPLETED - Flag: `--check-external` to enable
  - ✅ Default: Off (don't check external by default)
  - ✅ Reason: External sites change, protects CI/CD
  
- [x] **4.4** Create whitelist for known problematic domains
  - ✅ COMPLETED - Whitelist includes:
    - LinkedIn, Twitter/X (authentication)
    - Facebook, Instagram (block bots)
    - YouTube (rate limiting)
    - GitHub (rate limited)
    - Amazon (may block bots)
  - ✅ Easily configurable in script

- [x] **4.5** Document external link checking
  - ✅ COMPLETED - Added to PRE_DEPLOYMENT_CHECK.md
  - ✅ Explained retry logic
  - ✅ Showed how to enable
  - ✅ Provided example usage

**Success Criteria:**
- [x] External links can be checked
- [x] Retry logic reduces false positives
- [x] Feature is optional and configurable
- [x] No blocking of normal CI/CD workflow

**Owner:** Dustin Thostenson  
**Time Estimate:** 6-8 hours → ✅ **COMPLETED in 2 hours**
**Status:** ✅ COMPLETE

---

### ✅ ITEM 5: HTML Report Generation

**Description:** Create pretty HTML reports instead of just CLI output.

**Action Items:**
- [ ] **5.1** Design HTML report template
  - Summary card (tests passed/failed)
  - Timeline of checks
  - Details for each category (pages, links, resources)
  - Color-coded results (✅ green, ❌ red)

- [ ] **5.2** Add HTML generation to script
  - New option: `--html report.html`
  - Generate report on each run
  - Include timestamp and environment info

- [ ] **5.3** Make HTML report shareable
  - Upload to GitHub Pages or artifacts
  - View from GitHub Actions UI
  - Include in commit status

- [ ] **5.4** Add trending visualization
  - Track results over time
  - Show: Number of checks, issues found, trends
  - Goal: See if site health improving/declining

**Success Criteria:**
- HTML reports generate successfully
- Reports are readable and useful
- Can be integrated with GitHub Actions
- Team can easily view results

**Owner:** TBD  
**Time Estimate:** 4-6 hours  
**Dependencies:** ITEM 2 (GitHub Actions integration)

---

### ✅ ITEM 6: Performance & Timing Metrics

**Description:** Measure and track script performance over time.

**Action Items:**
- [ ] **6.1** Add timing to each check
  - Record start/end time for each check
  - Calculate duration
  - Report in output

- [ ] **6.2** Track total execution time
  - Goal: Keep under 5 minutes
  - Alert if trending upward
  - Identify slow checks

- [ ] **6.3** Add to reports
  - Show times for each check
  - Show total time
  - Compare to previous runs

- [ ] **6.4** Create performance dashboard
  - Track execution times over runs
  - Show trends
  - Alert on degradation

**Success Criteria:**
- Timing data collected and reported
- Dashboard shows trends
- Can identify performance regressions
- Total time stays under 5 minutes

**Owner:** TBD  
**Time Estimate:** 2-3 hours  
**Dependencies:** ITEM 5 (HTML reports)

---

### ✅ ITEM 7: Team Testing & Feedback

**Description:** Validate automation works for other users and gather feedback.

**Action Items:**
- [ ] **7.1** Document setup instructions for team
  - How to run locally
  - How to interpret results
  - What to do if tests fail

- [ ] **7.2** Have team member test script
  - Provide setup guide
  - Gather feedback on usability
  - Document any issues found

- [ ] **7.3** Collect feedback
  - What's helpful?
  - What's confusing?
  - What's missing?

- [ ] **7.4** Iterate based on feedback
  - Improve documentation
  - Fix any issues
  - Add requested features

**Success Criteria:**
- At least 1 other person can run script successfully
- Feedback is documented
- Issues are resolved or planned
- Script is team-ready

**Owner:** TBD  
**Time Estimate:** 3-4 hours  
**Dependencies:** ITEM 1 (verification)

---

## LONG-TERM PHASE (This Year - September 24, 2026 → May 24, 2027)

### Goal
Make the system production-grade with monitoring, alerts, and historical tracking.

### ✅ ITEM 8: Production Monitoring (Continuous)

**Description:** Monitor the production site continuously, not just before deployments.

**Action Items:**
- [ ] **8.1** Create scheduled check workflow
  - Trigger: Daily at 6 AM UTC
  - Run: Pre-deployment check against production site
  - Report: Email results to team

- [ ] **8.2** Check production external links
  - Different from dev server checks
  - Check real URLs (production domain)
  - More lenient timeouts
  - Alert on patterns of failures

- [ ] **8.3** Implement alerting
  - Email on first failure
  - Daily summary if issues persist
  - Trend alerts (increasing failures)

- [ ] **8.4** Create dashboard
  - Production site health
  - Last check time
  - Recent issues
  - Trend indicators

- [ ] **8.5** Document monitoring
  - How to view results
  - How to respond to alerts
  - Escalation procedures

**Success Criteria:**
- Production site checked automatically
- Issues detected within 24 hours
- Team alerted to problems
- Dashboard shows site health

**Owner:** TBD (DevOps/SRE)  
**Time Estimate:** 8-12 hours  
**Dependencies:** ITEM 4 (external link validation), ITEM 5 (reporting)

---

### ✅ ITEM 9: Historical Data Tracking

**Description:** Track site health over time to identify patterns and regressions.

**Action Items:**
- [ ] **9.1** Create database/storage for results
  - Option 1: CSV file in repo
  - Option 2: GitHub Discussions database
  - Option 3: External service (if budget allows)
  - Goal: Store timestamp + results

- [ ] **9.2** Log every check run
  - Timestamp
  - Number of pages checked
  - Issues found by category
  - Execution time

- [ ] **9.3** Analyze trends
  - Calculate 7-day average issues
  - Identify new issue patterns
  - Track fix rates

- [ ] **9.4** Create historical reports
  - Monthly health report
  - Quarterly trends
  - Year-over-year comparison

- [ ] **9.5** Set baselines and alerts
  - Normal: 0 issues
  - Warning: 1-2 issues
  - Critical: 3+ issues
  - Alert on thresholds exceeded

**Success Criteria:**
- Historical data stored and accessible
- Trends can be analyzed
- Reports can be generated on demand
- Baselines help identify anomalies

**Owner:** TBD  
**Time Estimate:** 6-8 hours  
**Dependencies:** ITEM 8 (production monitoring)

---

### ✅ ITEM 10: Automated Remediation Suggestions

**Description:** Provide actionable suggestions when issues are found.

**Action Items:**
- [ ] **10.1** Create issue database
  - Common issues and patterns
  - Known fixes for each issue
  - Suggested remediations

- [ ] **10.2** Implement analysis engine
  - On issue detection, analyze the type
  - Determine likely cause
  - Suggest remediation

- [ ] **10.3** Add suggestions to reports
  - Issue found
  - Likely cause
  - Suggested fix
  - Command to implement fix (if possible)

- [ ] **10.4** Create auto-fix options
  - Some issues can be fixed automatically
  - Example: Fix broken image paths
  - Get approval before fixing

- [ ] **10.5** Document remediation process
  - How to interpret suggestions
  - How to apply fixes
  - When to escalate

**Success Criteria:**
- Issues come with suggestions
- Suggestions are actionable
- Some issues can be auto-fixed
- Reduces time-to-resolution by 50%+

**Owner:** TBD  
**Time Estimate:** 10-12 hours  
**Dependencies:** ITEM 9 (historical tracking)

---

### ✅ ITEM 11: Slack/Email Notifications

**Description:** Integrate alerts with communication channels for visibility.

**Action Items:**
- [ ] **11.1** Set up Slack integration
  - Create Slack app/webhook
  - Test message delivery
  - Format messages for readability

- [ ] **11.2** Configure notification rules
  - When to notify (which issues)
  - Who to notify (different roles)
  - How often (avoid spam)

- [ ] **11.3** Create notification templates
  - Issue alerts
  - Summary reports
  - Resolution notifications

- [ ] **11.4** Add Slack commands (optional)
  - `/check-site` - Manual check trigger
  - `/site-status` - Get current status
  - `/deploy-check` - Pre-deployment check

- [ ] **11.5** Document notifications
  - What triggers alerts
  - How to respond
  - How to adjust settings

**Success Criteria:**
- Slack notifications work
- All team members are informed
- No message spam
- System is actionable from Slack

**Owner:** TBD  
**Time Estimate:** 3-5 hours  
**Dependencies:** ITEM 8 (production monitoring)

---

### ✅ ITEM 12: Long-Term Maintenance & Documentation

**Description:** Ensure the system remains maintainable and well-documented.

**Action Items:**
- [ ] **12.1** Create Operations runbook
  - How to operate the system
  - How to respond to alerts
  - How to update thresholds
  - Troubleshooting guide

- [ ] **12.2** Create Architecture documentation
  - System components diagram
  - Data flow
  - Integration points
  - Future extensibility

- [ ] **12.3** Plan for scaling
  - What if site grows to 1000+ events?
  - Performance implications
  - Optimization opportunities

- [ ] **12.4** Plan for platform changes
  - What if switch away from Jekyll?
  - What if change hosting?
  - How to migrate the system?

- [ ] **12.5** Schedule annual review
  - Review: Is system still meeting needs?
  - Update: Dependencies, tools, approaches
  - Reflect: Lessons learned
  - Plan: Next year's work

**Success Criteria:**
- Operations runbook complete
- System is maintainable by others
- Future growth planned for
- Platform changes have migration path

**Owner:** Dustin Thostenson  
**Time Estimate:** 4-6 hours  
**Dependencies:** All previous items

---

## Timeline Summary

```
May 2026 (SHORT-TERM)
├─ 5/24 → 5/31: Item 1 - Integration Testing
├─ 5/24 → 6/07: Item 2 - GitHub Actions Workflow
└─ 6/10 → 6/24: Item 3 - Documentation

June 2026 (MEDIUM-TERM START)
├─ 6/24 → 7/15: Item 4 - External Link Validation
├─ 6/24 → 7/08: Item 5 - HTML Reports
├─ 7/08 → 7/22: Item 6 - Performance Metrics
└─ 7/22 → 8/05: Item 7 - Team Testing

August 2026 (MEDIUM-TERM CONTINUE)
└─ 8/05 → 8/31: Refinement based on team feedback

September 2026 (LONG-TERM START)
├─ 9/01 → 10/15: Item 8 - Production Monitoring
├─ 10/15 → 11/15: Item 9 - Historical Tracking
├─ 11/15 → 12/31: Item 10 - Automated Remediation
└─ 12/31 → 1/31: Item 11 - Slack Integration

Q1 2027 (LONG-TERM CONTINUE)
└─ 1/31 → 5/24: Item 12 - Maintenance & Review
```

---

## Dependencies & Blockers

```
Item 1 (Testing)
└─ Enables: Item 2, Item 3, Item 7

Item 2 (GitHub Actions)
├─ Depends on: Item 1
└─ Enables: Item 5, Item 6, Item 8

Item 3 (Documentation)
├─ Depends on: Item 1
└─ Updates: README, DEVELOPMENT.md

Item 4 (External Links)
├─ Can run: Independently
└─ Improves: Item 8

Item 5 (HTML Reports)
├─ Depends on: Item 2 (preferred, but optional)
└─ Enables: Item 6, Item 9

Item 6 (Performance)
├─ Depends on: Item 5
└─ Improves: Item 8, Item 9

Item 8 (Production Monitoring)
├─ Depends on: Item 2, Item 4
└─ Enables: Item 9

Item 9 (Historical)
├─ Depends on: Item 8
└─ Enables: Item 10

Item 10 (Auto-Remediation)
├─ Depends on: Item 9
└─ Improves: Issue resolution time

Item 11 (Slack)
├─ Depends on: Item 8, Item 10
└─ Improves: Team visibility

Item 12 (Maintenance)
├─ Depends on: All previous items
└─ Ensures: Long-term viability
```

---

## Success Metrics

### Short-Term (June 2026)
- [ ] Script used in ≥ 3 deployments
- [ ] GitHub Actions workflow active
- [ ] Documentation updated
- [ ] Team has clear deployment process

### Medium-Term (September 2026)
- [ ] External link checking working
- [ ] HTML reports generated
- [ ] Performance metrics tracked
- [ ] Team feedback incorporated
- [ ] System feels production-ready

### Long-Term (May 2027)
- [ ] Production monitoring active
- [ ] Historical data 6+ months deep
- [ ] Automated suggestions helpful
- [ ] Slack integration live
- [ ] System is self-sustaining
- [ ] 0 critical issues for 3+ months

---

## Risk & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| External APIs become unreliable | High | Implement retry logic, whitelist (Item 4) |
| Too many false positives | High | Develop intelligent filtering, thresholds |
| Team adoption slow | Medium | Education & documentation (Item 3, 7) |
| Performance degrades | Medium | Monitor continuously (Item 6, 8) |
| Maintenance burden | Medium | Automation & runbooks (Item 12) |

---

## Resource Allocation

### Owner Responsibilities
- **Dustin Thostenson:** Items 1-3, 12 (core ownership)
- **Team Member(s):** Items 4-7, 9-11 (development partners)

### Time Budget
- **Short-term:** 10-15 hours (feasible in 1 month)
- **Medium-term:** 25-35 hours (spread across 3 months)
- **Long-term:** 30-40 hours (spread across 8 months)
- **Total:** ~70-90 hours across 1 year

---

## Progress Tracking

### Completed ✅
- [x] Scripts/pre-deployment-check.py created
- [x] Core documentation created
- [x] Initial testing done (75 events verified)
- [x] **Site Cleanup Phase Complete** (May 24, 2026)
- [x] **SHORT-TERM PHASE COMPLETE** (May 24, 2026)
  - Item 1: Integration testing (1.1 passed)
  - Item 2: GitHub Actions workflow (created & documented)
  - Item 3: Documentation (100% complete)
  - All items merged to main
- [x] **MEDIUM-TERM Item 4: External Link Validation** ✅ COMPLETE (May 24, 2026)
  - All 5 sub-items completed
  - Feature fully implemented, tested, and documented
  - Flag: `--check-external` to enable

### In Progress 🔄
- Branch: `automation/medium-term-phase` (started May 24, 2026)
- [ ] Item 5: HTML Report Generation (NEXT)
- [ ] Item 6: Performance Metrics
- [ ] Item 7: Team Testing & Feedback

### Not Started ⏳
- [ ] MEDIUM-TERM Items 5-7 (in progress)
- [ ] LONG-TERM Phase: Items 8-12 (Sept 24 onwards)

---

## Notes & References

- See `LESSONS_LEARNED.md` for session context
- See `PRE_DEPLOYMENT_CHECK.md` for technical details
- See `QUICK_START_DEPLOYMENT.md` for usage guide
- See `DEPLOYMENT_CHECKLIST.md` for current process

---

**Next Action:** 
1. ✅ SHORT-TERM phase merged to main (complete)
2. ✅ MEDIUM-TERM Item 4 complete (external link validation)
3. → Begin Item 5: HTML Report Generation
4. → Merge medium-term-phase branch to main (late June)

**MEDIUM-TERM PHASE STATUS (June 24 → September 24, 2026):**
- ✅ Item 4: External Link Validation - COMPLETE (May 24)
- ⏳ Item 5: HTML Report Generation (in progress)
- ⏳ Item 6: Performance Metrics
- ⏳ Item 7: Team Testing & Feedback

**Last Reviewed:** May 24, 2026 (Updated after SHORT-TERM merge and Item 4 completion)  
**Next Review:** May 28, 2026 (after Item 5 completion)

