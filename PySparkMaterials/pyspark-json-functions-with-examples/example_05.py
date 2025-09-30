# Example 05 from: PySpark JSON Functions with Examples

from pyspark.sql.functions import get_json_object
df.select(col("id"),get_json_object(col("value"),"$.ZipCodeType").alias("ZipCodeType")) \
    .show(truncate=False)

//+---+-----------+
//|id |ZipCodeType|
//+---+-----------+
//|1  |STANDARD   |
//+---+-----------+
