"""
University & Course Data Scraper - Main Entry Point
Runs the full pipeline: Scrape -> Clean -> Export.
"""

from scraper import UNIVERSITIES, scrape_universities, scrape_courses
from cleaner import clean_data
from export import export_to_excel
import logging

# --- Logging Setup ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

def run_pipeline():
    """ Runs the end-to-end scraper pipeline. """
    print("\n" + "="*50)
    print("🚀 STARTING UNIVERSITY & COURSE SCRAPER PIPELINE")
    print("="*50 + "\n")

    # 1. Scrape Universities
    raw_universities = scrape_universities()
    
    # 2. Scrape Courses for all 5 target universities
    # (Requirement: Call for all 5 universities and collect all courses into one list)
    logger.info("Initializing course scraping for all target universities...")
    raw_all_courses = []
    for uni in UNIVERSITIES:
        courses = scrape_courses(uni["university_id"], uni["courses_url"])
        raw_all_courses.extend(courses)
        
    # 3. Clean Data
    cleaned_uni_df, cleaned_courses_df = clean_data(raw_universities, raw_all_courses)
    
    # 4. Export to Excel
    export_to_excel(cleaned_uni_df, cleaned_courses_df)
    
    # 5. Final Summary
    print("\n" + "="*50)
    print(f"✅ Done! {len(cleaned_uni_df)} universities scraped, {len(cleaned_courses_df)} courses collected.")
    
    # Check for failures (universities in config not in final clean list)
    scraped_names = cleaned_uni_df['university_name'].tolist()
    failed = [uni['name'] for uni in UNIVERSITIES if uni['name'] not in scraped_names]
    
    if failed:
        print(f"⚠️  Skipped: {', '.join(failed)}")
    
    print("="*50 + "\n")

if __name__ == "__main__":
    run_pipeline()
