from pathlib import Path
import sqlite3
import pandas as pd

project_root = Path(__file__).resolve().parent.parent

db_file = (
    project_root
    / "data"
    / "processed"
    / "analytics_fab.db"
)

conn = sqlite3.connect(db_file)

query = """
SELECT *
FROM fab_data
LIMIT 10
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()