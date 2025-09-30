# Example 01 from: PySpark ArrayType Column With Examples

from pyspark.sql.types import StringType, ArrayType
arrayCol = ArrayType(StringType(),False)
