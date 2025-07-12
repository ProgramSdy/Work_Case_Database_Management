import sqlite3

# Connect to (or create) the SQLite database file
conn = sqlite3.connect("case_db.sqlite")  # Creates case_db.sqlite in this folder
cursor = conn.cursor()

# Create a table for storing work cases
cursor.execute("""
CREATE TABLE IF NOT EXISTS cases (
    case_id TEXT PRIMARY KEY,
    title TEXT,
    product TEXT,
    model TEXT,
    date TEXT
)
""")

# Insert a sample case (you can add more later)
cursor.execute("""
INSERT OR IGNORE INTO cases (case_id, title, product, model, date)
VALUES (?, ?, ?, ?, ?)
""", ("CASE0001", "PLC IOScan Issue", "PLC", "M221", "2025-07-13"))

# Save and close
conn.commit()
conn.close()

print("✅ Database created and sample case inserted.")
