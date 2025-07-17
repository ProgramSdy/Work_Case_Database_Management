import os
import sqlite3
from datetime import datetime

# Path to the root of Hardware folder
ROOT_PATH = r"C:\Users\sesa747199\OneDrive - Schneider Electric\1.0 Technical Support\1. Product_Category_with_Case\1. Hardware"

def extract_case_info(case_path, product_model, product_group):
    case_folder = os.path.basename(case_path)
    case_id = case_folder.split('_')[1] if '_' in case_folder else "UNKNOWN"
    title = case_folder
    files = os.listdir(case_path)
    files_list = ", ".join(files)
    has_tech_doc = 'Tech_Doc' in files

    return (case_id, title, "Hardware", product_group, product_model, case_path, files_list, has_tech_doc)

def scan_hardware():
    conn = sqlite3.connect("case_db.sqlite")
    cursor = conn.cursor()

    # Create cases table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            case_id TEXT PRIMARY KEY,
            title TEXT,
            category TEXT,
            group_name TEXT,
            model TEXT,
            path TEXT,
            files TEXT,
            has_tech_doc BOOLEAN
        )
    """)

    for group_name in os.listdir(ROOT_PATH):
        group_path = os.path.join(ROOT_PATH, group_name)
        if not os.path.isdir(group_path):
            continue

        for model_name in os.listdir(group_path):
            model_path = os.path.join(group_path, model_name)
            if not os.path.isdir(model_path):
                continue

            for case_name in os.listdir(model_path):
                case_path = os.path.join(model_path, case_name)
                if not os.path.isdir(case_path) or not case_name.startswith("Case_"):
                    continue

                case_data = extract_case_info(case_path, model_name, group_name)

                cursor.execute("""
                    INSERT OR IGNORE INTO cases
                    (case_id, title, category, group_name, model, path, files, has_tech_doc)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, case_data)

    conn.commit()
    conn.close()
    print("✅ Hardware folder scan completed and cases saved.")

if __name__ == "__main__":
    scan_hardware()
