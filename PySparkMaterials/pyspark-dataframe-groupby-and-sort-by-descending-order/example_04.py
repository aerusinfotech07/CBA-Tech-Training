# Example 04 from: PySpark DataFrame groupBy and Sort by Descending Order

# Group by using by giving alias name.
from pyspark.sql.functions import sum
dfGroup=df.groupBy("department") \
          .agg(sum("bonus").alias("sum_salary"))

#+-----+----------+
#|state|sum_salary|
#+-----+----------+
#|NJ   |91000     |
#|NV   |166000    |
#|CA   |171000    |
#|DE   |99000     |
#|NY   |252000    |
#+-----+----------+
