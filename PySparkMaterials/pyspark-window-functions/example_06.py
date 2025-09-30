# Example 06 from: PySpark Window Functions

#ntile() Example
from pyspark.sql.functions import ntile
df.withColumn("ntile",ntile(2).over(windowSpec)) \
    .show()
