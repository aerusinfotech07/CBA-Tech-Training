# Example 02 from: PySpark Groupby Explained with Example

from pyspark.sql.functions import sum,avg,max

# Running more aggregations
df.groupBy("department") \
    .agg(sum("salary").alias("sum_salary"), \
         avg("salary").alias("avg_salary"), \
         sum("bonus").alias("sum_bonus"), \
         max("bonus").alias("max_bonus") \
     ) \
    .show(truncate=False)
