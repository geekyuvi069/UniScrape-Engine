# University & Course Data Scraper

An automated Python-based scraping pipeline that extracts, cleans, and structures data from prominent universities in the UK and Australia into a professional relational Excel file.

## 🏛️ Target Universities

| ID | University Name | Country | City |
|:---|:---|:---|:---|
| 1 | University of Manchester | UK | Manchester |
| 2 | University of Leeds | UK | Leeds |
| 3 | University of Birmingham | UK | Birmingham |
| 4 | University of Glasgow | UK | Glasgow |
| 5 | University of Sydney | Australia | Sydney |

## 📁 Project Structure

```text
webscrapping/
├── docs/                      # Project documentation and specifications
│   ├── DATA_MODELS.md
│   ├── FEATURES.md
│   ├── PROJECT_OVERVIEW.md
│   ├── TECH_STACK.md
│   └── USER_FLOWS.md
├── output/                    # Generated data exports
│   └── universities_data.xlsx
├── cleaner.py                 # Data cleaning and normalization pipeline
├── export.py                  # Excel generation and styling module
├── scraper.py                 # Web scraping logic and configurations
├── main.py                    # Unified entry point for the full pipeline
├── requirements.txt           # Python dependencies
└── venv/                      # Virtual environment
```

## 🚀 Setup & Installation

### 1. Initialize Environment
It is recommended to use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Scraper
Execute the full pipeline (Scrape -> Clean -> Export) with a single command:
```bash
python3 main.py
```

## 📊 Output Format

The output is saved to `output/universities_data.xlsx` with two relational sheets:

### Sheet 1: Universities
- `university_id` (Primary Key)
- `university_name`
- `country`
- `city`
- `website`

### Sheet 2: Courses
- `course_id` (Primary Key)
- `university_id` (Foreign Key)
- `course_name`
- `level` (Bachelor's, Master's, PhD, etc.)
- `discipline`
- `duration`
- `fees`
- `eligibility`

## 🛠️ Tech Stack
- **Python**: Core logic
- **Requests**: HTTP handling
- **BeautifulSoup4**: HTML parsing
- **Pandas**: Data cleaning and DataFrame management
- **Openpyxl**: Professional Excel styling and export

## 🔗 Relational Integrity
The system maintains strict relational integrity between the two sheets. Every entry in the **Courses** sheet is linked to the **Universities** sheet via the `university_id`. During the cleaning pipeline, the system validates that all course entries have a corresponding university record, ensuring a consistent and valid data model for analysis.

---
**Author / Submission Note**
Building a University & Course Data Scraper for an internship assignment.
