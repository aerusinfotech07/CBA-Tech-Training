# Example 05 from: PySpark apply Function to Column

# Convert function to udf
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
upperCaseUDF = udf(lambda x:upperCase(x),StringType())
