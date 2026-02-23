# University & Course Data Scraper

## Overview
An automated Python scraping project that collects university and course data from 5 structured, scraping-friendly universities across the UK and Australia. Data is cleaned, structured, and exported into a professional Excel file with two relational sheets.

## Problem
Manually collecting university and course data is time-consuming, error-prone, and unscalable. This project automates the entire pipeline — from scraping to Excel export — in one clean script.

## Solution
Scrape 5 target universities using Python (BeautifulSoup + Requests), extract structured course data, clean and normalize it, then export to a relational Excel file with proper ID linking between sheets.

## Target Universities
1. University of Manchester (UK)
2. University of Leeds (UK)
3. University of Edinburgh (UK)
4. University of Melbourne (Australia)
5. University of Sydney (Australia)

## MVP Scope
- Scrape 5 universities → at least 5 courses each (25+ courses total)
- Export Sheet 1: Universities (university_id, name, country, city, website)
- Export Sheet 2: Courses (course_id, university_id, name, level, discipline, duration, fees, eligibility)
- Handle missing values gracefully (fill with "N/A")
- No duplicate records
- Proper relational ID linking between sheets

## Out of Scope
- Real-time scraping / live updates
- Database storage (Excel only)
- More than 10 universities
- Login-required pages
- Image or PDF scraping
