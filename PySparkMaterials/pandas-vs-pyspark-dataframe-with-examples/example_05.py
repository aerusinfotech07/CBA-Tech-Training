# Example 05 from: Pandas vs PySpark DataFrame With Examples

# PySpark transformations
from pyspark.sql.functions import mean, col, max
# Example 1
df2=pysparkDF.select(mean("age"),mean("salary"))
             .show()

# Example 2
pysparkDF.groupBy("gender") \
         .agg(mean("age"),mean("salary"),max("salary")) \
         .show()
