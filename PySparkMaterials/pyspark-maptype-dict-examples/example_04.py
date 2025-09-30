# Example 04 from: PySpark MapType (Dict) Usage with Examples

from pyspark.sql.functions import explode
df.select(df.name,explode(df.properties)).show()

+----------+----+-----+
|      name| key|value|
+----------+----+-----+
|     James| eye|brown|
|     James|hair|black|
|   Michael| eye| null|
|   Michael|hair|brown|
|    Robert| eye|black|
|    Robert|hair|  red|
|Washington| eye| grey|
|Washington|hair| grey|
| Jefferson| eye|     |
| Jefferson|hair|brown|
+----------+----+-----+
