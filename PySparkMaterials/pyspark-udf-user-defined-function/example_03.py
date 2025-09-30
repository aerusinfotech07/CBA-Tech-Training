# Example 03 from: PySpark UDF (User Defined Function)

from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType

# Converting function to UDF 
convertUDF = udf(lambda z: convertCase(z),StringType())
