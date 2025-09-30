# Example 02 from: PySpark apply Function to Column

# Apply function using withColumn
from pyspark.sql.functions import upper
df.withColumn("Upper_Name", upper(df.Name)) \
  .show()
