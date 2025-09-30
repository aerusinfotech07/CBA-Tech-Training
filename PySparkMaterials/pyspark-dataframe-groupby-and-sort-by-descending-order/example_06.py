# Example 06 from: PySpark DataFrame groupBy and Sort by Descending Order

# Sort by descending order.
from pyspark.sql.functions import desc
dfFilter.sort(desc("sum_salary")).show()

#+-----+----------+
#|state|sum_salary|
#+-----+----------+
#|   NY|    252000|
#|   CA|    171000|
#|   NV|    166000|
#+-----+----------+
