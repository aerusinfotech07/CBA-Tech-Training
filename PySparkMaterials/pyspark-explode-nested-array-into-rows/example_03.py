# Example 03 from: PySpark – explode nested array into rows

from pyspark.sql.functions import flatten
df.select(df.name,flatten(df.subjects)).show(truncate=False)
