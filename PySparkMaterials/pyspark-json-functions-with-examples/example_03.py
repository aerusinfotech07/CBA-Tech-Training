# Example 03 from: PySpark JSON Functions with Examples

from pyspark.sql.functions import to_json,col
df2.withColumn("value",to_json(col("value"))) \
   .show(truncate=False)

//+---+----------------------------------------------------------------------------+
//|id |value                                                                       |
//+---+----------------------------------------------------------------------------+
//|1  |{"Zipcode":"704","ZipCodeType":"STANDARD","City":"PARC PARQUE","State":"PR"}|
//+---+----------------------------------------------------------------------------+
