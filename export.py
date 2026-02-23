"""
University & Course Data Scraper - Excel Export Module
Exports cleaned data to a styled Excel file using pandas and openpyxl.
"""

import pandas as pd
from openpyxl.styles import Font, Fill, PatternFill
import logging
import os

logger = logging.getLogger(__name__)

def export_to_excel(df_uni: pd.DataFrame, df_courses: pd.DataFrame):
    """
    Exports the university and course DataFrames to a styled Excel file.
    
    - Sheet 1: "Universities"
    - Sheet 2: "Courses"
    - Styling: Bold headers with light blue background.
    - Auto-fitted column widths.
    
    Args:
        df_uni: Cleaned university DataFrame.
        df_courses: Cleaned course DataFrame.
    """
    output_dir = "output"
    file_name = "universities_data.xlsx"
    file_path = os.path.join(output_dir, file_name)
    
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    logger.info(f"Exporting data to {file_path}...")

    try:
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            # 1. Write DataFrames to sheets
            df_uni.to_excel(writer, sheet_name='Universities', index=False)
            df_courses.to_excel(writer, sheet_name='Courses', index=False)
            
            # 2. Apply styling and auto-fit columns
            workbook = writer.book
            header_fill = PatternFill(start_color='BDD7EE', end_color='BDD7EE', fill_type='solid')
            header_font = Font(bold=True)

            for sheet_name in writer.sheets:
                worksheet = writer.sheets[sheet_name]
                
                # Style header row
                for cell in worksheet[1]:
                    cell.fill = header_fill
                    cell.font = header_font
                
                # Auto-fit column widths
                for col in worksheet.columns:
                    max_length = 0
                    column = col[0].column_letter # Get the column name
                    for cell in col:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    adjusted_width = (max_length + 2)
                    worksheet.column_dimensions[column].width = adjusted_width

        print(f"Exported {len(df_uni)} universities and {len(df_courses)} courses to {file_path}")
        logger.info("Excel export successful.")

    except Exception as e:
        logger.error(f"✗ Failed to export to Excel: {e}")
