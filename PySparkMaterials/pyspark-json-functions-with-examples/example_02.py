# Example 02 from: PySpark JSON Functions with Examples

#Convert JSON string column to Map type
from pyspark.sql.types import MapType,StringType
from pyspark.sql.functions import from_json
df2=df.withColumn("value",from_json(df.value,MapType(StringType(),StringType())))
df2.printSchema()
df2.show(truncate=False)

//root
// |-- id: integer (nullable = false)
// |-- value: map (nullable = true)
// |    |-- key: string
// |    |-- value: string (valueContainsNull = true)

//+---+---------------------------------------------------------------------------+
//|id |value                                                                      |
//+---+---------------------------------------------------------------------------+
//|1  |[Zipcode -> 704, ZipCodeType -> STANDARD, City -> PARC PARQUE, State -> PR]|
//+---+---------------------------------------------------------------------------+
