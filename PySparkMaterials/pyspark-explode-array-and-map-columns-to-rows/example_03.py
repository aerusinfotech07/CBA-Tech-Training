# Example 03 from: PySpark Explode Array and Map Columns to Rows

# explode() on map column
from pyspark.sql.functions import explode
df3 = df.select(df.name,explode(df.properties))
df3.printSchema()
df3.show()
