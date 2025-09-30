# Example 03 from: PySpark – Difference between two dates (days, months, years)

# Imports
from pyspark.sql.functions import col, current_date, datediff, months_between, round, lit

# Calculate the difference between two dates in years
df4 = df.withColumn("datesDiff", datediff(current_date(), col("date"))) \
  .withColumn("yearsDiff", months_between(current_date(), col("date")) / lit(12)) \
  .withColumn("yearsDiff_round", round(months_between(current_date(), col("date")) / lit(12), 2))
df4.show()
