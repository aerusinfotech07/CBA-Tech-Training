# Example 02 from: PySpark where() & filter() for efficient data filtering

# Using SQL col() function
from pyspark.sql.functions import col
df.filter(col("state") == "OH") \
    .show(truncate=False)
