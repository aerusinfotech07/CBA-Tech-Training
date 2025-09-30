# Example 05 from: PySpark MapType (Dict) Usage with Examples

from pyspark.sql.functions import map_keys
df.select(df.name,map_keys(df.properties)).show()

+----------+--------------------+
|      name|map_keys(properties)|
+----------+--------------------+
|     James|         [eye, hair]|
|   Michael|         [eye, hair]|
|    Robert|         [eye, hair]|
|Washington|         [eye, hair]|
| Jefferson|         [eye, hair]|
+----------+--------------------+
