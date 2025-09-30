# Example 02 from: PySpark – explode nested array into rows

from pyspark.sql.functions import explode
df.select(df.name,explode(df.subjects)).show(truncate=False)
