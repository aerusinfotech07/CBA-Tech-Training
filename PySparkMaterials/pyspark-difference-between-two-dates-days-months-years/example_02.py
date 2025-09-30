# Example 02 from: PySpark – Difference between two dates (days, months, years)

# Imports
from pyspark.sql.functions import col, current_date, datediff, months_between, round

# Calculate the difference between two dates in months
df3 = df.withColumn("datesDiff", datediff(current_date(), col("date"))) \
  .withColumn("monthsDiff", months_between(current_date(), col("date"))) \
  .withColumn("monthsDiff_round", round(months_between(current_date(), col("date")), 2))
  
df3.show()
