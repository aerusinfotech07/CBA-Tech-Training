# Example 03 from: PySpark Groupby Explained with Example

from pyspark.sql.functions import sum,avg,max

# Using filter on aggregate data
df.groupBy("department") \
    .agg(sum("salary").alias("sum_salary"), \
      avg("salary").alias("avg_salary"), \
      sum("bonus").alias("sum_bonus"), \
      max("bonus").alias("max_bonus")) \
    .where(col("sum_bonus") >= 50000) \
    .show(truncate=False)
