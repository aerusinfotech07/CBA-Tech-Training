# Example 04 from: PySpark Explode Array and Map Columns to Rows

# explode_outer() on array and map column
from pyspark.sql.functions import explode_outer
df.select(df.name,explode_outer(df.knownLanguages)).show()
df.select(df.name,explode_outer(df.properties)).show()
