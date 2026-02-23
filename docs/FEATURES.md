# Features

## MVP Features

---

### Feature 1: University Data Scraper
Description: Automatically scrape basic info for all 5 target universities

Acceptance Criteria:
- [ ] Script sends HTTP request to each university's website
- [ ] Extracts: university name, country, city, official website URL
- [ ] Assigns unique university_id (1–5) to each
- [ ] Handles failed requests gracefully (logs error, skips, continues)
- [ ] Adds 1–3 second delay between requests

Dependencies: None (core feature)
Priority: MVP - Critical

---

### Feature 2: Course Data Scraper
Description: For each university, scrape at least 5 courses with full details

Acceptance Criteria:
- [ ] Navigates to course listing page for each university
- [ ] Extracts per course: name, level, discipline, duration, fees, eligibility
- [ ] Assigns unique course_id (auto-incrementing from 101)
- [ ] Links correct university_id to each course
- [ ] Missing fields default to "N/A" (never blank)
- [ ] Minimum 5 courses per university (25+ total)

Dependencies: Feature 1 (needs university_id)
Priority: MVP - Critical

---

### Feature 3: Data Cleaning Pipeline
Description: Clean and normalize all scraped raw data before export

Acceptance Criteria:
- [ ] Strip leading/trailing whitespace from all string fields
- [ ] Remove duplicate university rows
- [ ] Remove duplicate course rows
- [ ] Fill all null/None values with "N/A"
- [ ] Validate all university_ids in courses exist in universities list
- [ ] Normalize level field values (e.g. "Bachelors" → "Bachelor's")

Dependencies: Feature 1, Feature 2
Priority: MVP - Critical

---

### Feature 4: Excel Export with Two Sheets
Description: Export cleaned data to a professional .xlsx file

Acceptance Criteria:
- [ ] Creates single .xlsx file: universities_data.xlsx
- [ ] Sheet 1 named "Universities" with correct columns and data
- [ ] Sheet 2 named "Courses" with correct columns and data
- [ ] Header row is bold with light blue background color
- [ ] Column widths auto-fitted to content
- [ ] university_id correctly links both sheets
- [ ] No duplicate records in either sheet
- [ ] File saved to /output/ directory

Dependencies: Feature 3
Priority: MVP - Critical

---

### Feature 5: Error Handling & Logging
Description: Handle all failure scenarios gracefully without crashing

Acceptance Criteria:
- [ ] HTTP errors (403, 404, 500) logged and skipped
- [ ] Request timeouts (10s limit) logged and skipped
- [ ] Missing HTML elements handled (return "N/A", not crash)
- [ ] At end of run: print total universities scraped, total courses scraped
- [ ] At end of run: print any universities that were skipped and why

Dependencies: Feature 1, Feature 2
Priority: MVP - Critical

---

## Post-MVP / Later Features

### Feature 6: Selenium Fallback
Description: If a page requires JavaScript rendering, fall back to Selenium
Priority: Later - only if static scraping fails on a target site

### Feature 7: CLI Arguments
Description: Run scraper for specific university only (debug mode)
`python main.py --university manchester`
Priority: Later - nice to have for development

### Feature 8: Data Validation Report
Description: After export, print a validation summary:
- universities count
- courses count per university
- any missing field percentages
Priority: Later
