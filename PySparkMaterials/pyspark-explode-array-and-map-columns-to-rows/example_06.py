# Example 06 from: PySpark Explode Array and Map Columns to Rows

# posexplode_outer() on array and map 
from pyspark.sql.functions import posexplode_outer
df.select($"name",posexplode_outer($"knownLanguages")).show()
df.select(df.name,posexplode_outer(df.properties)).show()
