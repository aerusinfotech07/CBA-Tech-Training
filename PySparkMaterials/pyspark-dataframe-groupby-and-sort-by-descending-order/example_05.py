# Example 05 from: PySpark DataFrame groupBy and Sort by Descending Order

# Sory by on group by column
from pyspark.sql.functions import asc
dfFilter.sort("sum_salary").show()

#+-----+----------+
#|state|sum_salary|
#+-----+----------+
#|   NV|    166000|
#|   CA|    171000|
#|   NY|    252000|
#+-----+----------+
