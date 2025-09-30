# Example 07 from: PySpark Window Functions

# cume_dist() Example
from pyspark.sql.functions import cume_dist    
df.withColumn("cume_dist",cume_dist().over(windowSpec)) \
   .show()
