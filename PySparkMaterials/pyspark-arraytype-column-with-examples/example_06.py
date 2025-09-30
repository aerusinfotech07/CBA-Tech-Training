# Example 06 from: PySpark ArrayType Column With Examples

from pyspark.sql.functions import array_contains
df.select(df.name,array_contains(df.languagesAtSchool,"Java")
    .alias("array_contains")).show()

+----------------+--------------+
|            name|array_contains|
+----------------+--------------+
|    James,,Smith|          true|
|   Michael,Rose,|          true|
|Robert,,Williams|         false|
+----------------+--------------+
