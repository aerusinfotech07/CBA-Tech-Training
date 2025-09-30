# Example 01 from: PySpark MapType (Dict) Usage with Examples

from pyspark.sql.types import StringType, MapType
mapCol = MapType(StringType(),StringType(),False)
