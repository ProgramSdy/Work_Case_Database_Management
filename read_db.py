import sqlite3
import pandas as pd

# Connect to your existing database
conn = sqlite3.connect("case_db.sqlite")

# Read the 'cases' table into a Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM cases", conn)

# Close the connection
conn.close()

# Display the table
print("📋 Cases Table:\n")
print(df)
