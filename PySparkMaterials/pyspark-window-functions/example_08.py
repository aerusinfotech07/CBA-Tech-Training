# Example 08 from: PySpark Window Functions

# lag() Example
from pyspark.sql.functions import lag    
df.withColumn("lag",lag("salary",2).over(windowSpec)) \
      .show()
