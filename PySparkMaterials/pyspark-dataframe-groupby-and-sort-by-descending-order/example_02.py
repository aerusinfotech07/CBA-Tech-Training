# Example 02 from: PySpark DataFrame groupBy and Sort by Descending Order

from pyspark.sql.functions import sum, col, desc
df.groupBy("state") \
  .agg(sum("salary").alias("sum_salary")) \
  .filter(col("sum_salary") > 100000)  \
  .sort(desc("sum_salary")) \
  .show()

#+-----+----------+
#|state|sum_salary|
#+-----+----------+
#|   NY|    252000|
#|   CA|    171000|
#|   NV|    166000|
#+-----+----------+
