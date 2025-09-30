# PySpark JSON Functions with Examples

---

In PySpark, the JSON functions allow you to work with JSON data within DataFrames. These functions help you parse, manipulate, and extract data from JSON columns or strings. These functions can also be used to convert JSON to a struct, map type, etc. I will explain the most used JSON SQL functions with Python examples in this article.

Advertisements

## 1. PySpark JSON Functions
JSON FunctionsDescriptionfrom_json()Converts JSON string into Struct type or Map type.to_json()Converts MapType or Struct type to JSON string.json_tuple()Extract the Data from JSON and create them as a new columns.get_json_object()Extracts JSON element from a JSON string based on json path specified.schema_of_json()Create schema string from JSON stringPySpark JSON Functions
### 1.1. Create DataFrame with Column containing JSON String

To explain these JSON functions first, let’s create a DataFrame with a column containing JSON string.

```

from pyspark.sql import SparkSession,Row
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

jsonString="""{"Zipcode":704,"ZipCodeType":"STANDARD","City":"PARC PARQUE","State":"PR"}"""
df=spark.createDataFrame([(1, jsonString)],["id","value"])
df.show(truncate=False)

//+---+--------------------------------------------------------------------------+
//|id |value                                                                     |
//+---+--------------------------------------------------------------------------+
//|1  |{"Zipcode":704,"ZipCodeType":"STANDARD","City":"PARC PARQUE","State":"PR"}|
//+---+--------------------------------------------------------------------------+

```

## 2. PySpark JSON Functions Examples

## 2.1. from_json()

PySpark from_json() function is used to convert JSON string into Struct type or Map type. The below example converts JSON string to Map key-value pair. I will leave it to you to convert to struct type. Refer, Convert JSON string to Struct type column .

```

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

```

## 2.2. to_json()

to_json() function is used to convert DataFrame columns MapType or Struct type to JSON string. Here, I am using df2 that created from above from_json() example.

```

from pyspark.sql.functions import to_json,col
df2.withColumn("value",to_json(col("value"))) \
   .show(truncate=False)

//+---+----------------------------------------------------------------------------+
//|id |value                                                                       |
//+---+----------------------------------------------------------------------------+
//|1  |{"Zipcode":"704","ZipCodeType":"STANDARD","City":"PARC PARQUE","State":"PR"}|
//+---+----------------------------------------------------------------------------+

```

## 2.3. json_tuple()

Function json_tuple() is used the query or extract the elements from JSON column and create the result as a new columns.

```

from pyspark.sql.functions import json_tuple
df.select(col("id"),json_tuple(col("value"),"Zipcode","ZipCodeType","City")) \
    .toDF("id","Zipcode","ZipCodeType","City") \
    .show(truncate=False)

//+---+-------+-----------+-----------+
//|id |Zipcode|ZipCodeType|City       |
//+---+-------+-----------+-----------+
//|1  |704    |STANDARD   |PARC PARQUE|
//+---+-------+-----------+-----------+

```

## 2.4. get_json_object()

get_json_object() is used to extract the JSON string based on path from the JSON column.

```

from pyspark.sql.functions import get_json_object
df.select(col("id"),get_json_object(col("value"),"$.ZipCodeType").alias("ZipCodeType")) \
    .show(truncate=False)

//+---+-----------+
//|id |ZipCodeType|
//+---+-----------+
//|1  |STANDARD   |
//+---+-----------+

```

## 2.5. schema_of_json()

Use schema_of_json() to create schema string from JSON string column.

```

from pyspark.sql.functions import schema_of_json,lit
schemaStr=spark.range(1) \
    .select(schema_of_json(lit("""{"Zipcode":704,"ZipCodeType":"STANDARD","City":"PARC PARQUE","State":"PR"}"""))) \
    .collect()[0][0]
print(schemaStr)

//struct<City:string,State:string,ZipCodeType:string,Zipcode:bigint>

```

## 3. Complete Example of PySpark JSON Functions

```

from pyspark.sql import SparkSession,Row
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

jsonString="""{"Zipcode":704,"ZipCodeType":"STANDARD","City":"PARC PARQUE","State":"PR"}"""
df=spark.createDataFrame([(1, jsonString)],["id","value"])
df.show(truncate=False)

#Convert JSON string column to Map type
from pyspark.sql.types import MapType,StringType
from pyspark.sql.functions import from_json
df2=df.withColumn("value",from_json(df.value,MapType(StringType(),StringType())))
df2.printSchema()
df2.show(truncate=False)

from pyspark.sql.functions import to_json,col
df2.withColumn("value",to_json(col("value"))) \
   .show(truncate=False)

from pyspark.sql.functions import json_tuple
df.select(col("id"),json_tuple(col("value"),"Zipcode","ZipCodeType","City")) \
    .toDF("id","Zipcode","ZipCodeType","City") \
    .show(truncate=False)

from pyspark.sql.functions import get_json_object
df.select(col("id"),get_json_object(col("value"),"$.ZipCodeType").alias("ZipCodeType")) \
    .show(truncate=False)

from pyspark.sql.functions import schema_of_json,lit
schemaStr=spark.range(1) \
    .select(schema_of_json(lit("""{"Zipcode":704,"ZipCodeType":"STANDARD","City":"PARC PARQUE","State":"PR"}"""))) \
    .collect()[0][0]
print(schemaStr)

```

## Related Article
- PySpark collect_list() and collect_set() functions
- PySpark String Functions with Examples
- PySpark SQL Date and Timestamp Functions
- PySpark Column Class | Operators & Functions
- PySpark Window Functions
- PySpark Aggregate Functions with Examples
- PySpark Apply udf to Multiple Columns
- PySpark printSchema() to String or JSON
- PySpark Parse JSON from String Column | TEXT File
- PySpark Read JSON file into DataFrame
- PySpark Read Multiple Lines (multiline) JSON File
- PySpark Write to CSV File
- PySpark printSchema() Example
- PySpark Retrieve DataType & Column Names of DataFrame

### References
- https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html

