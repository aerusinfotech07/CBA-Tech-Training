# Example 03 from: PySpark ArrayType Column With Examples

from pyspark.sql.functions import explode
df.select(df.name,explode(df.languagesAtSchool)).show()

+----------------+------+
|            name|   col|
+----------------+------+
|    James,,Smith|  Java|
|    James,,Smith| Scala|
|    James,,Smith|   C++|
|   Michael,Rose,| Spark|
|   Michael,Rose,|  Java|
|   Michael,Rose,|   C++|
|Robert,,Williams|CSharp|
|Robert,,Williams|    VB|
+----------------+------+
