# User Flows

## Flow 1: Full Scraping Pipeline (Main Flow)

Entry: Run `python main.py`

1. Script initializes
   - Import all libraries
   - Define 5 university targets with their course listing URLs
   - Initialize empty lists for universities and courses

2. Loop through each university
   - Send HTTP GET request to course listing page
   - If request fails (timeout / 403) → Log error → Skip university → Continue to next
   - If request succeeds → Parse HTML with BeautifulSoup

3. Extract university data
   - Scrape: university name, country, city, website
   - Assign unique university_id (1 through 5)
   - Append to universities list

4. Extract course data for this university
   - Find all course listing elements on the page
   - For each course:
     - Extract: course_name, level, discipline, duration, fees, eligibility
     - If field not found → Set value to "N/A"
     - Assign unique course_id (auto-increment)
     - Link university_id to this course
   - Append each course to courses list

5. Polite delay
   - Sleep 1–3 seconds before next university request
   - Prevents rate limiting / IP blocking

6. Data cleaning
   - Convert both lists to pandas DataFrames
   - Strip whitespace from all string fields
   - Remove duplicate rows (drop_duplicates)
   - Fill any remaining nulls with "N/A"
   - Validate: every university_id in courses exists in universities

7. Export to Excel
   - Create universities_data.xlsx
   - Write Sheet 1: Universities DataFrame
   - Write Sheet 2: Courses DataFrame
   - Apply header styling (bold, background color)
   - Auto-fit column widths
   - Save file to /output/ folder

8. Done
   - Print success message with file path
   - Print summary: X universities, Y courses scraped

---

## Flow 2: Single University Scrape (Debug Mode)

Entry: Run with university name argument
`python main.py --university manchester`

1. Load only that university's config
2. Scrape just that one university
3. Print raw extracted data to console
4. Do NOT export to Excel (debug only)

Use this to test and fix selectors for a specific university without running the full pipeline.

---

## Flow 3: Error Handling Flow

Entry: Any point during scraping

- HTTP 403 (Blocked) → Log "Blocked by [university]" → Skip → Continue
- HTTP 404 (Page not found) → Log "Page not found" → Skip → Continue
- Timeout (>10 seconds) → Log "Timeout on [university]" → Skip → Continue
- Parsing error (tag not found) → Set field to "N/A" → Continue scraping
- Zero courses found for a university → Log warning → Still include university in Sheet 1

---

## Flow 4: Excel Export Validation

After export, verify:
- Sheet 1 has exactly 5 rows (one per university)
- Sheet 2 has at least 25 rows (5 per university minimum)
- No blank cells (all filled with data or "N/A")
- university_id column in Sheet 2 only contains values 1–5
- course_id column in Sheet 2 has no duplicates

If validation fails → Print specific warning → Do not overwrite previous good export
