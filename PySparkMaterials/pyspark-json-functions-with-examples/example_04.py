# Example 04 from: PySpark JSON Functions with Examples

from pyspark.sql.functions import json_tuple
df.select(col("id"),json_tuple(col("value"),"Zipcode","ZipCodeType","City")) \
    .toDF("id","Zipcode","ZipCodeType","City") \
    .show(truncate=False)

//+---+-------+-----------+-----------+
//|id |Zipcode|ZipCodeType|City       |
//+---+-------+-----------+-----------+
//|1  |704    |STANDARD   |PARC PARQUE|
//+---+-------+-----------+-----------+
