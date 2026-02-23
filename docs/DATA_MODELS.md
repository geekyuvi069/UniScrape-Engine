# Data Models

## Sheet 1: Universities

| Field | Type | Description |
|-------|------|-------------|
| university_id | integer | Unique identifier (1, 2, 3...) |
| university_name | string | Full official university name |
| country | string | Country name (UK / Australia) |
| city | string | City where university is located |
| website | string | Official homepage URL |

### Rules
- university_id must be unique — no duplicates
- website must be official university domain only (e.g. manchester.ac.uk)
- No null values allowed in any field

### Example Data
```
university_id | university_name              | country   | city       | website
1             | University of Manchester     | UK        | Manchester | https://www.manchester.ac.uk
2             | University of Leeds          | UK        | Leeds      | https://www.leeds.ac.uk
3             | University of Edinburgh      | UK        | Edinburgh  | https://www.ed.ac.uk
4             | University of Melbourne      | Australia | Melbourne  | https://www.unimelb.edu.au
5             | University of Sydney         | Australia | Sydney     | https://www.sydney.edu.au
```

---

## Sheet 2: Courses

| Field | Type | Description |
|-------|------|-------------|
| course_id | integer | Unique course identifier (101, 102...) |
| university_id | integer | Foreign key → links to Sheet 1 university_id |
| course_name | string | Full name of the course/programme |
| level | string | Bachelor's / Master's / PhD / Diploma |
| discipline | string | Field of study (e.g. Computer Science, Business) |
| duration | string | Course length (e.g. "3 years", "1 year") |
| fees | string | Annual or total fees (e.g. "£9,250/year") |
| eligibility | string | Entry requirements (e.g. "2:1 undergraduate degree") |

### Rules
- course_id must be unique across ALL courses
- university_id MUST match a valid university_id from Sheet 1
- Missing values filled with "N/A" (never left blank)
- At least 5 courses per university (25+ total)

### Example Data
```
course_id | university_id | course_name              | level      | discipline       | duration | fees          | eligibility
101       | 1             | BSc Computer Science     | Bachelor's | Computer Science | 3 years  | £9,250/year   | A-levels required
102       | 1             | MSc Data Science         | Master's   | Data Science     | 1 year   | £14,000/year  | 2:1 degree required
103       | 1             | PhD Artificial Intelligence | PhD     | AI               | 3-4 years| N/A           | Master's degree
201       | 2             | BSc Business Management  | Bachelor's | Business         | 3 years  | £9,250/year   | A-levels required
```

---

## Relational Integrity Rules
- Every course_id in Sheet 2 must be unique
- Every university_id in Sheet 2 must exist in Sheet 1
- No orphan courses (courses without a matching university)
- No orphan universities (universities with 0 courses)
- university_id numbering: 1–5 (one per university)
- course_id numbering: starts at 101, increments by 1 per course
