# Example 03 from: PySpark Window Functions

# rank() example
from pyspark.sql.functions import rank
df.withColumn("rank",rank().over(windowSpec)) \
    .show()
