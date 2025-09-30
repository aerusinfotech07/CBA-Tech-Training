# Example 07 from: PySpark MapType (Dict) Usage with Examples

from pyspark.sql.functions import map_values
df.select(df.name,map_values(df.properties)).show()

+----------+----------------------+
|      name|map_values(properties)|
+----------+----------------------+
|     James|        [brown, black]|
|   Michael|             [, brown]|
|    Robert|          [black, red]|
|Washington|          [grey, grey]|
| Jefferson|             [, brown]|
+----------+----------------------+
