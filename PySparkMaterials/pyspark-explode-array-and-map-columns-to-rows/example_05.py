# Example 05 from: PySpark Explode Array and Map Columns to Rows

# posexplode() on array and map
from pyspark.sql.functions import posexplode
df.select(df.name,posexplode(df.knownLanguages)).show()
df.select(df.name,posexplode(df.properties)).show()
