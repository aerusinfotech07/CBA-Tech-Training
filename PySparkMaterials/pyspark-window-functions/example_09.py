# Example 09 from: PySpark Window Functions

# lead() Example
from pyspark.sql.functions import lead    
df.withColumn("lead",lead("salary",2).over(windowSpec)) \
    .show()
