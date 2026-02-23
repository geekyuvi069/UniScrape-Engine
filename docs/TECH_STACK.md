# Tech Stack

## Language
Python 3.10+
- Widely supported, rich scraping ecosystem, clean syntax for data pipelines

## Scraping Libraries

### requests
- Sends HTTP GET requests to university pages
- Lightweight, fast, no browser overhead
- Works perfectly for static HTML pages (our target sites)

### BeautifulSoup4 (bs4)
- Parses raw HTML into navigable tree
- Extract data using tag names, class names, CSS selectors
- Simple and readable syntax

### Why NOT Selenium?
- Our target universities (Manchester, Leeds, Edinburgh, Melbourne, Sydney) all have static course listing pages
- Selenium adds complexity, slow execution, and requires browser driver setup
- We only use Selenium if a specific page requires JavaScript rendering (fallback option)

## Data Processing

### pandas
- Clean and normalize scraped data
- Handle missing values (fillna with "N/A")
- Remove duplicates (drop_duplicates)
- Structure data into DataFrames before export

## Excel Export

### openpyxl
- Write two sheets into one .xlsx file
- Style header rows (bold, background color)
- Auto-adjust column widths for readability
- Used via pandas ExcelWriter engine

## Development Tools

### python-dotenv (optional)
- Store any config variables cleanly

### time / random
- Add delays between requests to avoid rate limiting
- Polite scraping: sleep 1-3 seconds between requests

## File Structure
```
project/
│
├── docs/
│   ├── PROJECT_OVERVIEW.md
│   ├── TECH_STACK.md
│   ├── DATA_MODELS.md
│   ├── USER_FLOWS.md
│   └── FEATURES.md
│
├── scraper.py          ← Main scraping script
├── export.py           ← Excel export logic
├── main.py             ← Entry point (runs everything)
├── requirements.txt    ← All dependencies
└── output/
    └── universities_data.xlsx
```

## Requirements.txt
```
requests==2.31.0
beautifulsoup4==4.12.2
pandas==2.1.0
openpyxl==3.1.2
lxml==4.9.3
```
