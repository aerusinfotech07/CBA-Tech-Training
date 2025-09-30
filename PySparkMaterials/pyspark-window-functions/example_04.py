# Example 04 from: PySpark Window Functions

# dense_rank() example 
from pyspark.sql.functions import dense_rank
df.withColumn("dense_rank",dense_rank().over(windowSpec)) \
    .show()
