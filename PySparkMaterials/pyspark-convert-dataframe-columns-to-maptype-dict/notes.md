# PySpark Convert DataFrame Columns to MapType (Dict)

---

To convert DataFrame columns to a MapType (dictionary) column in PySpark, you can use the create_map function from the pyspark.sql.functions module. This function allows you to create a map from a set of key-value pairs, where the keys and values are columns from the DataFrame.

Advertisements

Let’s create a DataFrame

```

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data = [ ("36636","Finance",3000,"USA"), 
    ("40288","Finance",5000,"IND"), 
    ("42114","Sales",3900,"USA"), 
    ("39192","Marketing",2500,"CAN"), 
    ("34534","Sales",6500,"USA") ]
schema = StructType([
     StructField('id', StringType(), True),
     StructField('dept', StringType(), True),
     StructField('salary', IntegerType(), True),
     StructField('location', StringType(), True)
     ])

df = spark.createDataFrame(data=data,schema=schema)
df.printSchema()
df.show(truncate=False)

```

This yields below output

```

root
 |-- id: string (nullable = true)
 |-- dept: string (nullable = true)
 |-- salary: integer (nullable = true)
 |-- location: string (nullable = true)

+-----+---------+------+--------+
|id   |dept     |salary|location|
+-----+---------+------+--------+
|36636|Finance  |3000  |USA     |
|40288|Finance  |5000  |IND     |
|42114|Sales    |3900  |USA     |
|39192|Marketing|2500  |CAN     |
|34534|Sales    |6500  |USA     |
+-----+---------+------+--------+

```

## Convert DataFrame Columns to MapType

Now, using create_map() SQL function let’s convert PySpark DataFrame columns salary and location to MapType .

```

#Convert columns to Map
from pyspark.sql.functions import col,lit,create_map
df = df.withColumn("propertiesMap",create_map(
        lit("salary"),col("salary"),
        lit("location"),col("location")
        )).drop("salary","location")
df.printSchema()
df.show(truncate=False)

```

This yields below output.

```

root
 |-- id: string (nullable = true)
 |-- dept: string (nullable = true)
 |-- propertiesMap: map (nullable = false)
 |    |-- key: string
 |    |-- value: string (valueContainsNull = true)

+-----+---------+---------------------------------+
|id   |dept     |propertiesMap                    |
+-----+---------+---------------------------------+
|36636|Finance  |[salary -> 3000, location -> USA]|
|40288|Finance  |[salary -> 5000, location -> IND]|
|42114|Sales    |[salary -> 3900, location -> USA]|
|39192|Marketing|[salary -> 2500, location -> CAN]|
|34534|Sales    |[salary -> 6500, location -> USA]|
+-----+---------+---------------------------------+

```

Happy Learning !!

## Related Articles
- PySpark Convert StructType (struct) to Dictionary/MapType (map)
- PySpark StructType & StructField Explained with Examples
- PySpark printSchema() Example
- PySpark Create DataFrame From Dictionary (Dict)
- PySpark Convert Dictionary/Map to Multiple Columns
- PySpark Explode Array and Map Columns to Rows
- PySpark mapPartitions() Examples
- PySpark MapType (Dict) Usage with Examples
- PySpark flatMap() Transformation

