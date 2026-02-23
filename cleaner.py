"""
University & Course Data Scraper - Data Cleaning Module
Cleans and normalizes scraped data using pandas.
"""

import pandas as pd
import logging

logger = logging.getLogger(__name__)

def clean_data(universities: list[dict], courses: list[dict]) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Cleans and normalizes the scraped university and course data.
    
    - Strips whitespace from all string fields.
    - Removes duplicate universities by name.
    - Removes duplicate courses by name + university_id.
    - Fills None/null values with "N/A".
    - Normalizes the 'level' field.
    - Validates relational integrity (university_id).
    
    Args:
        universities: Raw list of university dictionaries.
        courses: Raw list of course dictionaries.
        
    Returns:
        A tuple of (cleaned_universities_df, cleaned_courses_df).
    """
    logger.info("Starting data cleaning pipeline...")
    
    # 1. Convert to DataFrames
    df_uni = pd.DataFrame(universities)
    df_courses = pd.DataFrame(courses)
    
    if df_uni.empty or df_courses.empty:
        logger.warning("One or both input lists are empty. Returning empty DataFrames.")
        return df_uni, df_courses

    # 2. Strip whitespace and fill nulls for all string columns
    def clean_strings(df):
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].astype(str).str.strip()
        return df.fillna("N/A").replace('None', "N/A").replace('nan', "N/A")

    df_uni = clean_strings(df_uni)
    df_courses = clean_strings(df_courses)

    # 3. Remove duplicate universities (by name)
    uni_count_before = len(df_uni)
    df_uni = df_uni.drop_duplicates(subset=['university_name'])
    if len(df_uni) < uni_count_before:
        logger.info(f"Removed {uni_count_before - len(df_uni)} duplicate universities.")

    # 4. Remove duplicate courses (by name + university_id)
    course_count_before = len(df_courses)
    df_courses = df_courses.drop_duplicates(subset=['course_name', 'university_id'])
    if len(df_courses) < course_count_before:
        logger.info(f"Removed {course_count_before - len(df_courses)} duplicate courses.")

    # 5. Normalize level field
    level_map = {
        "Bachelors": "Bachelor's",
        "Bachelor": "Bachelor's",
        "Masters": "Master's",
        "Master": "Master's",
        "Doctorate": "PhD"
    }
    
    # Apply normalization only to the level column
    df_courses['level'] = df_courses['level'].replace(level_map)
    logger.info("Normalized course levels.")

    # 6. Validate relational integrity (university_id)
    valid_uni_ids = df_uni['university_id'].unique()
    initial_courses = len(df_courses)
    df_courses = df_courses[df_courses['university_id'].isin(valid_uni_ids)]
    
    if len(df_courses) < initial_courses:
        logger.warning(f"Removed {initial_courses - len(df_courses)} orphan courses (no matching university_id).")

    # 7. Renumber course_ids to ensure zero gaps
    df_courses = df_courses.sort_values(by=['university_id', 'course_name'])
    df_courses['course_id'] = range(101, 101 + len(df_courses))

    logger.info(f"Data cleaning complete. Universities: {len(df_uni)}, Courses: {len(df_courses)}.")
    return df_uni, df_courses
