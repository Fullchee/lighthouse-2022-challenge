import sqlite3
import pandas as pd
conn = sqlite3.connect("himalayas.db")

peak_height_query = """
SELECT COUNT(*) as peak_count_higher_than_8000
FROM peaks
WHERE heightm > 8000"""
display(pd.read_sql(peak_height_query, conn))

woman_count_query = """
SELECT COUNT(*) as woman_count
FROM members
WHERE sex = 'F'
"""

pd.read_sql(woman_count_query, conn)
