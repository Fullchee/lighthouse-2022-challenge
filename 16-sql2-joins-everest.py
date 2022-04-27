import sqlite3
import pandas as pd
conn = sqlite3.connect("himalayas.db")

# Relations
# https://imgur.com/pEdUYXq

# pd.read_sql("select * from peaks where pkname = 'Everest'", conn)

expeditions_to_everest_count = """
SELECT COUNT(*)
FROM exped
WHERE peakid = (
  SELECT peakid
  FROM peaks
  WHERE pkname = 'Everest')
"""

pd.read_sql(expeditions_to_everest_count, conn)
# 2161

people_to_everest_count = """
SELECT COUNT(*)
FROM members
WHERE peakid = (
  SELECT peakid
  FROM peaks
  WHERE pkname = 'Everest')
"""

pd.read_sql(people_to_everest_count, conn)
# 21900

